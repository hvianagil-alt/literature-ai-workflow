#!/usr/bin/env python3
"""Tiny form-quality model: logistic regression + field centroids.

No scikit-learn. Numpy only. Weights live in review/ml/model.json so scoring
works offline after a train pass.

Labels: 1 = published-review form, 0 = catalog / chatbot draft.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from review_form_features import FRONT_FEATURES, FEATURE_NAMES, vectorize


def sigmoid(z: np.ndarray | float) -> np.ndarray | float:
    z = np.clip(z, -30.0, 30.0)
    return 1.0 / (1.0 + np.exp(-z))


def standardize(X: np.ndarray, mean: np.ndarray | None = None, std: np.ndarray | None = None):
    if mean is None:
        mean = X.mean(axis=0)
    if std is None:
        std = X.std(axis=0)
    std = np.where(std < 1e-8, 1.0, std)
    return (X - mean) / std, mean, std


def train_logreg(
    X: np.ndarray,
    y: np.ndarray,
    *,
    l2: float = 1.0,
    lr: float = 0.15,
    epochs: int = 600,
) -> tuple[np.ndarray, float]:
    """L2-regularised logistic regression via gradient descent."""
    n, d = X.shape
    w = np.zeros(d, dtype=float)
    b = 0.0
    y = y.astype(float)
    for _ in range(epochs):
        p = sigmoid(X @ w + b)
        err = p - y
        grad_w = (X.T @ err) / n + l2 * w / max(n, 1)
        grad_b = float(err.mean())
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b


def predict_proba(X: np.ndarray, w: np.ndarray, b: float) -> np.ndarray:
    return np.asarray(sigmoid(X @ w + b), dtype=float)


def roc_auc(y: np.ndarray, p: np.ndarray) -> float:
    y = y.astype(int)
    pos = p[y == 1]
    neg = p[y == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    # Mann–Whitney U / Wilcoxon-Mann-Whitney
    n_correct = 0.0
    for a in pos:
        n_correct += float(np.sum(a > neg)) + 0.5 * float(np.sum(a == neg))
    return n_correct / (len(pos) * len(neg))


def accuracy(y: np.ndarray, p: np.ndarray, thresh: float = 0.5) -> float:
    pred = (p >= thresh).astype(int)
    return float((pred == y.astype(int)).mean())


def stratified_kfold(
    X: np.ndarray,
    y: np.ndarray,
    k: int = 5,
    seed: int = 0,
) -> list[float]:
    rng = np.random.default_rng(seed)
    aucs: list[float] = []
    idx_pos = np.where(y == 1)[0]
    idx_neg = np.where(y == 0)[0]
    rng.shuffle(idx_pos)
    rng.shuffle(idx_neg)
    if len(idx_pos) < k or len(idx_neg) < k:
        # Too small to fold; train/test on a 70/30 split instead.
        n = len(y)
        order = rng.permutation(n)
        cut = max(1, int(0.7 * n))
        tr, te = order[:cut], order[cut:]
        if len(te) == 0 or y[tr].min() == y[tr].max() or y[te].min() == y[te].max():
            return []
        Xs, mean, std = standardize(X[tr])
        w, b = train_logreg(Xs, y[tr])
        p = predict_proba((X[te] - mean) / std, w, b)
        aucs.append(roc_auc(y[te], p))
        return aucs
    folds_pos = np.array_split(idx_pos, k)
    folds_neg = np.array_split(idx_neg, k)
    for i in range(k):
        te = np.concatenate([folds_pos[i], folds_neg[i]])
        tr = np.array([j for j in range(len(y)) if j not in set(te.tolist())])
        Xs, mean, std = standardize(X[tr])
        w, b = train_logreg(Xs, y[tr])
        p = predict_proba((X[te] - mean) / std, w, b)
        aucs.append(roc_auc(y[te], p))
    return aucs


def field_centroids(
    rows: list[dict],
    *,
    names: list[str],
) -> dict[str, dict]:
    """Mean/std of feature vectors grouped by field."""
    grouped: dict[str, list[list[float]]] = {}
    for row in rows:
        field = row.get("field") or "all"
        grouped.setdefault(field, []).append(vectorize(row["features"], names))
    out: dict[str, dict] = {}
    for field, vecs in grouped.items():
        arr = np.asarray(vecs, dtype=float)
        std = arr.std(axis=0)
        std = np.where(std < 1e-8, 1.0, std)
        out[field] = {
            "n": int(arr.shape[0]),
            "mean": arr.mean(axis=0).tolist(),
            "std": std.tolist(),
        }
    if rows:
        arr = np.asarray([vectorize(r["features"], names) for r in rows], dtype=float)
        std = arr.std(axis=0)
        std = np.where(std < 1e-8, 1.0, std)
        out["all"] = {
            "n": int(arr.shape[0]),
            "mean": arr.mean(axis=0).tolist(),
            "std": std.tolist(),
        }
    return out


def z_scores(vec: list[float], centroid: dict) -> list[float]:
    mean = np.asarray(centroid["mean"], dtype=float)
    std = np.asarray(centroid["std"], dtype=float)
    std = np.where(std < 1e-8, 1.0, std)
    return ((np.asarray(vec, dtype=float) - mean) / std).tolist()


def mean_abs_z(zs: list[float]) -> float:
    if not zs:
        return 0.0
    return float(np.mean(np.abs(zs)))


def train_bundle(
    positives: list[dict],
    negatives: list[dict],
    *,
    names: list[str] | None = None,
    l2: float = 1.0,
) -> dict:
    names = names or FRONT_FEATURES
    X = np.asarray(
        [vectorize(r["features"], names) for r in positives + negatives],
        dtype=float,
    )
    y = np.asarray([1] * len(positives) + [0] * len(negatives), dtype=int)
    Xs, mean, std = standardize(X)
    w, b = train_logreg(Xs, y.astype(float), l2=l2)
    p = predict_proba(Xs, w, b)
    cv = [a for a in stratified_kfold(X, y) if not math.isnan(a)]
    centroids = field_centroids(positives, names=names)
    coefs = sorted(
        zip(names, w.tolist()),
        key=lambda kv: abs(kv[1]),
        reverse=True,
    )
    return {
        "feature_names": names,
        "mean": mean.tolist(),
        "std": std.tolist(),
        "weights": w.tolist(),
        "bias": float(b),
        "n_positive": len(positives),
        "n_negative": len(negatives),
        "train_auc": roc_auc(y, p),
        "train_accuracy": accuracy(y, p),
        "cv_auc_mean": float(np.mean(cv)) if cv else None,
        "cv_auc_folds": cv,
        "coefficients_by_abs": [{"feature": n, "weight": w_} for n, w_ in coefs],
        "centroids": centroids,
        "label_positive": "published_review_form",
        "label_negative": "catalog_or_chatbot_draft",
        "note": (
            "Form only. Do not import scientific findings from gold reviews. "
            "Positive class is published OA review title+abstract form."
        ),
    }


def score_vector(vec: list[float], model: dict) -> dict:
    names = model["feature_names"]
    if len(vec) != len(names):
        raise ValueError(f"expected {len(names)} features, got {len(vec)}")
    mean = np.asarray(model["mean"], dtype=float)
    std = np.asarray(model["std"], dtype=float)
    std = np.where(std < 1e-8, 1.0, std)
    w = np.asarray(model["weights"], dtype=float)
    b = float(model["bias"])
    x = (np.asarray(vec, dtype=float) - mean) / std
    p = float(predict_proba(x.reshape(1, -1), w, b)[0])
    contrib = (x * w).tolist()
    top = sorted(
        zip(names, contrib),
        key=lambda kv: abs(kv[1]),
        reverse=True,
    )[:8]
    return {
        "p_published_form": p,
        "decision": "published_like" if p >= 0.5 else "catalog_like",
        "top_contributions": [{"feature": n, "signed_logit": c} for n, c in top],
    }


def compare_to_field(vec: list[float], model: dict, field: str | None) -> dict:
    names = model["feature_names"]
    centroids = model.get("centroids") or {}
    key = field if field and field in centroids else "all"
    if key not in centroids and "all" in centroids:
        key = "all"
    if key not in centroids:
        return {"field": field, "centroid": None, "mean_abs_z": None, "z": []}
    zs = z_scores(vec, centroids[key])
    ranked = sorted(zip(names, zs), key=lambda kv: abs(kv[1]), reverse=True)
    return {
        "field": key,
        "centroid_n": centroids[key]["n"],
        "mean_abs_z": mean_abs_z(zs),
        "top_divergences": [
            {"feature": n, "z": z} for n, z in ranked[:10] if abs(z) >= 0.75
        ],
    }


def save_model(model: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")


def load_model(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# Re-export names used by trainers
__all__ = [
    "FRONT_FEATURES",
    "FEATURE_NAMES",
    "train_bundle",
    "score_vector",
    "compare_to_field",
    "save_model",
    "load_model",
    "roc_auc",
    "accuracy",
]
