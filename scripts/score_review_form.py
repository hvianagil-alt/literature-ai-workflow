#!/usr/bin/env python3
"""Train, score, and compare review *form* against published OA reviews.

Subcommands:
    train     fit the logistic model + field centroids
    score     score one article.md
    compare   score every in-repo article against the model and write a report

Never copies scientific findings from gold reviews into a manuscript.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from review_form_features import (  # noqa: E402
    FRONT_FEATURES,
    extract_features,
    extract_front_features,
    vectorize,
)
from review_form_model import (  # noqa: E402
    compare_to_field,
    load_model,
    save_model,
    score_vector,
    train_bundle,
)
from collect_gold_reviews import RUN_FIELDS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "review" / "ml" / "model.json"
DEFAULT_CATALOG = ROOT / "review" / "ml" / "gold-catalog.json"
DEFAULT_REPORT = ROOT / "review" / "ml" / "comparison-report.md"

OURS_RUNS = [
    "2026-09-19-nanocarriers",
    "2026-09-19-scopus-oa-full",
    "2026-09-19-scopus-oa",
    "2026-09-20-scopus-hpp",
    "2026-09-20-pd-cannabinoids",
]


def _front_row(title: str, abstract: str, **meta) -> dict:
    feats = extract_front_features(title, abstract)
    row = {"title": title, "features": feats, **meta}
    return row


def catalog_mutations(title: str, abstract: str) -> list[tuple[str, str]]:
    """Contrastive negatives: same topic words, catalog/chatbot form."""
    topic = title.split(":")[0].strip() if ":" in title else title.strip()
    if len(topic.split()) < 3:
        topic = title.strip() or "this topic"
    flourish = f"Recent Advances in {topic}: A Comprehensive Overview"
    catalog_abs = (
        f"This review discusses {topic}. First, we searched Scopus and Unpaywall "
        f"for open full texts from 2021–2026. Second, Author et al. found a striking "
        f"effect in this set. Third, more research is needed, highlighting its "
        f"importance. PDFs we could open are listed below. Token estimate: 12000."
    )
    stack_abs = (
        f"Smith et al. reviewed {topic}. Jones et al. reported similar findings. "
        f"Lee et al. concluded the field is promising. This paper aims to provide "
        f"a holistic look at included papers from the OA export."
    )
    return [(flourish, catalog_abs), (f"A Review of {topic}", stack_abs)]


def fixture_rows() -> tuple[list[dict], list[dict]]:
    good = ROOT / "tests" / "fixtures" / "good-article.md"
    bad = ROOT / "tests" / "fixtures" / "bad-article.md"
    positives: list[dict] = []
    negatives: list[dict] = []
    if good.is_file():
        text = good.read_text(encoding="utf-8")
        feats = extract_features(text)
        positives.append(
            {
                "id": "fixture:good-article",
                "field": "generic-narrative",
                "title": feats and Path(good).name,
                "features": {k: feats[k] for k in FRONT_FEATURES},
                "origin": "fixture",
            }
        )
    if bad.is_file():
        text = bad.read_text(encoding="utf-8")
        feats = extract_features(text)
        negatives.append(
            {
                "id": "fixture:bad-article",
                "field": "generic-narrative",
                "title": Path(bad).name,
                "features": {k: feats[k] for k in FRONT_FEATURES},
                "origin": "fixture",
            }
        )
    return positives, negatives


def gold_rows(catalog_path: Path) -> list[dict]:
    """Gold positives. Prefer live abstracts; fall back to gold-features.json."""
    extracted: list[dict] = []
    if catalog_path.is_file():
        payload = json.loads(catalog_path.read_text(encoding="utf-8"))
        for rec in payload.get("records") or []:
            title = rec.get("title") or ""
            abstract = rec.get("abstract") or ""
            if rec.get("features"):
                feats = rec["features"]
            elif title and abstract.strip():
                feats = extract_front_features(title, abstract)
            else:
                continue
            extracted.append(
                {
                    "id": rec.get("doi") or rec.get("citekey") or rec.get("id"),
                    "doi": rec.get("doi") or "",
                    "field": rec.get("field") or "generic-narrative",
                    "title": title,
                    "year": rec.get("year") or "",
                    "journal": rec.get("journal") or "",
                    "origin": rec.get("origin") or "openalex",
                    "features": feats,
                }
            )
        if extracted:
            return extracted
    feat_path = catalog_path.parent / "gold-features.json"
    if feat_path.is_file():
        payload = json.loads(feat_path.read_text(encoding="utf-8"))
        return payload.get("records") or []
    return []


def build_training_sets(catalog_path: Path) -> tuple[list[dict], list[dict]]:
    positives, negatives = fixture_rows()
    gold = gold_rows(catalog_path)
    positives.extend(gold)
    if catalog_path.is_file():
        payload = json.loads(catalog_path.read_text(encoding="utf-8"))
        for rec in payload.get("records") or []:
            title = rec.get("title") or ""
            abstract = rec.get("abstract") or ""
            if not title:
                continue
            for i, (t, a) in enumerate(catalog_mutations(title, abstract or title)):
                negatives.append(
                    {
                        "id": f"mutation:{rec.get('doi') or rec.get('citekey')}:{i}",
                        "field": rec.get("field") or "generic-narrative",
                        "title": t,
                        "features": extract_front_features(t, a),
                        "origin": "catalog_mutation",
                    }
                )
    # Always include a few hand-written catalog negatives so train works
    # even with an empty gold catalog.
    extra_neg = [
        (
            "Recent Advances in Notes: A Comprehensive Overview",
            "This review discusses notes. First, we searched Scopus. Second, "
            "Author et al. found a striking effect. Third, more research is needed.",
        ),
        (
            "A review of four papers",
            "This OA export found four PDFs we could open. Token estimate: 12000. "
            "Al Researcher et al. randomized 40 students.",
        ),
    ]
    for i, (t, a) in enumerate(extra_neg):
        negatives.append(
            {
                "id": f"synthetic-neg:{i}",
                "field": "generic-narrative",
                "title": t,
                "features": extract_front_features(t, a),
                "origin": "synthetic",
            }
        )
    extra_pos = [
        (
            "Delayed recall of technical prose: a narrative review of format and domain",
            "Readers forget procedures within a week. Structured notes are widely "
            "recommended, yet whether format changes recall, and whether that change "
            "is the same for STEM text, remains unsettled. Laboratory and meta-analytic "
            "work generally points to a small benefit when domains are averaged; the "
            "STEM-specific test did not. Those patterns do not imply a semester-long habit.",
        ),
        (
            "Endosomal escape as a constraint on lipid vesicles: a narrative review",
            "A particle that arrives in a tumour is not yet a drug. Circulation-friendly "
            "coats help vesicles last, yet the same coat can keep a pH-sensitive membrane "
            "from opening. Trial and laboratory readouts do not answer the same question. "
            "Those patterns do not imply a human dose window.",
        ),
        (
            "High pressure without heat: a narrative review of lethality and injury",
            "Heat remains the default kill step because it is predictable. The same heat "
            "damages flavour, yet chilled pressure is not a sterilant. Laboratory challenges "
            "and one scientific opinion cannot be pooled. Those limits do not license "
            "substitution for pasteurisation.",
        ),
    ]
    for i, (t, a) in enumerate(extra_pos):
        positives.append(
            {
                "id": f"synthetic-pos:{i}",
                "field": "generic-narrative",
                "title": t,
                "features": extract_front_features(t, a),
                "origin": "synthetic",
            }
        )
    return positives, negatives


def cmd_train(args: argparse.Namespace) -> int:
    catalog = Path(args.catalog)
    positives, negatives = build_training_sets(catalog)
    if len(positives) < 2 or len(negatives) < 2:
        print("not enough labelled rows to train", file=sys.stderr)
        return 2
    model = train_bundle(positives, negatives, names=FRONT_FEATURES, l2=args.l2)
    model["trained_at_utc"] = datetime.now(timezone.utc).isoformat()
    model["catalog"] = str(catalog) if catalog.is_file() else None
    out = Path(args.model)
    save_model(model, out)
    feat_path = out.parent / "gold-features.json"
    slim = [
        {
            "id": r.get("id"),
            "doi": r.get("doi"),
            "field": r.get("field"),
            "title": r.get("title"),
            "origin": r.get("origin"),
            "features": r["features"],
        }
        for r in positives
        if r.get("origin") in {"openalex", "openalex_type_review", "style_study_doi_lookup"}
        or r.get("doi")
    ]
    feat_path.write_text(json.dumps({"records": slim, "n": len(slim)}, indent=2) + "\n")
    if catalog.is_file():
        payload = json.loads(catalog.read_text(encoding="utf-8"))
        for rec in payload.get("records") or []:
            rec.pop("abstract", None)
        payload["abstracts_stripped"] = True
        payload["note"] = (
            "Abstracts dropped after training. Retrain from gold-features.json "
            "or re-collect. Do not cite these records in a manuscript."
        )
        catalog.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(
        f"OK model {out}  pos={model['n_positive']} neg={model['n_negative']} "
        f"train_auc={model['train_auc']:.3f} cv_auc={model.get('cv_auc_mean')}"
    )
    print("top coefficients (published-like is positive weight):")
    for row in model["coefficients_by_abs"][:10]:
        print(f"  {row['weight']:+.3f}  {row['feature']}")
    return 0


def _score_article(path: Path, model: dict, field: str | None) -> dict:
    text = path.read_text(encoding="utf-8")
    feats = extract_features(text)
    front = {k: feats[k] for k in model["feature_names"]}
    vec = vectorize(front, model["feature_names"])
    scored = score_vector(vec, model)
    compared = compare_to_field(vec, model, field)
    return {
        "article": str(path),
        "field": field,
        "p_published_form": scored["p_published_form"],
        "decision": scored["decision"],
        "top_contributions": scored["top_contributions"],
        "field_comparison": compared,
        "front_features": front,
        "full_features": {k: feats[k] for k in feats if k not in front},
    }


def cmd_score(args: argparse.Namespace) -> int:
    model = load_model(Path(args.model))
    article = Path(args.article)
    if not article.is_file():
        print(f"missing article: {article}", file=sys.stderr)
        return 2
    result = _score_article(article, model, args.field)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out}")
    p = result["p_published_form"]
    print(
        f"{article}  p_published_form={p:.3f}  {result['decision']}  "
        f"field_z={result['field_comparison'].get('mean_abs_z')}"
    )
    floor = args.min_p
    if p < floor:
        print(
            f"FAIL form score {p:.3f} < {floor} (catalog-like vs published reviews)",
            file=sys.stderr,
        )
        return 1
    return 0


def _md_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(c) for c in col) for col in zip(*rows)]
    def fmt(row: list[str]) -> str:
        return "| " + " | ".join(c.ljust(w) for c, w in zip(row, widths)) + " |"
    header, *body = rows
    sep = "| " + " | ".join("-" * w for w in widths) + " |"
    return "\n".join([fmt(header), sep, *[fmt(r) for r in body]])


def cmd_compare(args: argparse.Namespace) -> int:
    model = load_model(Path(args.model))
    results: list[dict] = []
    for run_id in OURS_RUNS:
        article = ROOT / "review" / "runs" / run_id / "article.md"
        if not article.is_file():
            continue
        field = RUN_FIELDS.get(run_id)
        results.append(_score_article(article, model, field) | {"run_id": run_id})

    fixtures = ROOT / "tests" / "fixtures"
    for name, field, label in (
        ("good-article.md", "generic-narrative", "fixture-good"),
        ("bad-article.md", "generic-narrative", "fixture-bad"),
    ):
        path = fixtures / name
        if path.is_file():
            row = _score_article(path, model, field)
            row["run_id"] = label
            results.append(row)

    out_json = Path(args.out_json) if args.out_json else Path(args.model).parent / "comparison.json"
    out_md = Path(args.report)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "model": str(args.model),
        "results": results,
    }
    out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    table = [["Run", "Field", "p(published form)", "Decision", "Mean |z| vs field"]]
    for r in results:
        z = r.get("field_comparison") or {}
        ztxt = z.get("mean_abs_z")
        table.append(
            [
                r.get("run_id") or Path(r["article"]).parent.name,
                str(r.get("field") or ""),
                f"{r['p_published_form']:.3f}",
                r["decision"],
                "" if ztxt is None else f"{ztxt:.2f}",
            ]
        )

    lines = [
        "# Form-quality comparison",
        "",
        "This report scores **how** our reviews are written against a logistic "
        "model trained on published open-access review titles and abstracts "
        "(positive) versus catalog/chatbot mutations (negative). "
        "**Copy form only.** Do not import findings from gold reviews.",
        "",
        f"Trained: `{model.get('trained_at_utc') or 'unknown'}`  ",
        f"Gold positives in model: {model.get('n_positive')}  ",
        f"Negatives: {model.get('n_negative')}  ",
        f"Train AUC: {model.get('train_auc')}  ",
        f"CV AUC: {model.get('cv_auc_mean')}",
        "",
        "## Scores",
        "",
        _md_table(table),
        "",
        "## What the model treats as published-like",
        "",
    ]
    pos_w = [c for c in model.get("coefficients_by_abs") or [] if c["weight"] > 0][:8]
    neg_w = [c for c in model.get("coefficients_by_abs") or [] if c["weight"] < 0][:8]
    lines.append("Positive weights (toward published form):")
    lines.append("")
    for c in pos_w:
        lines.append(f"- `{c['feature']}` ({c['weight']:+.3f})")
    lines.append("")
    lines.append("Negative weights (toward catalog/chatbot form):")
    lines.append("")
    for c in neg_w:
        lines.append(f"- `{c['feature']}` ({c['weight']:+.3f})")
    lines.append("")
    lines.append("## Per-run divergences")
    lines.append("")
    for r in results:
        lines.append(f"### {r.get('run_id')}")
        lines.append("")
        lines.append(
            f"p(published form) = **{r['p_published_form']:.3f}** ({r['decision']})."
        )
        div = (r.get("field_comparison") or {}).get("top_divergences") or []
        if div:
            lines.append("")
            for d in div[:6]:
                lines.append(f"- `{d['feature']}` z={d['z']:+.2f}")
        lines.append("")
    lines.append("## How to use this")
    lines.append("")
    lines.append(
        "After `check_article.py` is green, run `python3 scripts/score_review_form.py "
        "score --article review/runs/<id>/article.md --field <field>`. "
        "If the score is catalog-like, rewrite joinery (claim-first sentences, "
        "contrast in the Abstract, no acquisition talk, no flourish title) "
        "before telling the user the article is done."
    )
    lines.append("")
    lines.append("## Optimizations encoded in the workflow")
    lines.append("")
    lines.append(
        "These rules were added because they match the gold set and separate "
        "the catalog fixture from published-like drafts:"
    )
    lines.append("")
    lines.append(
        "- Full-manuscript Abstracts must mark a tension or calibration "
        "(`yet` / `however` / `do not imply`). Gold abstracts almost never start "
        "with “This review discusses”; that opener now fails."
    )
    lines.append(
        "- Titles may not say `open-access set` or `this sample`."
    )
    lines.append(
        "- `check_article.py --form-model review/ml/model.json` fails catalog-like "
        "front matter. The harness passes that flag when the model file exists."
    )
    lines.append(
        "- Do **not** require “a narrative review” in the title for nanomedicine: "
        "only a minority of those gold titles name the kind. Colon subtitles are "
        "the endocrinology/neuroscience default, not a universal law."
    )
    lines.append(
        "- Do not import findings from this gold set into any manuscript."
    )
    lines.append("")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out_md}")
    print(f"wrote {out_json}")
    for r in results:
        print(
            f"{r.get('run_id'):28}  p={r['p_published_form']:.3f}  {r['decision']}"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("train", help="fit model.json from gold-catalog + fixtures")
    t.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    t.add_argument("--model", default=str(DEFAULT_MODEL))
    t.add_argument("--l2", type=float, default=0.6)
    t.set_defaults(func=cmd_train)

    s = sub.add_parser("score", help="score one article.md")
    s.add_argument("--article", required=True)
    s.add_argument("--model", default=str(DEFAULT_MODEL))
    s.add_argument("--field", default="")
    s.add_argument("--out", default="")
    s.add_argument(
        "--min-p",
        type=float,
        default=0.45,
        help="exit 1 if p_published_form is below this floor",
    )
    s.set_defaults(func=cmd_score)

    c = sub.add_parser("compare", help="score in-repo articles and write a report")
    c.add_argument("--model", default=str(DEFAULT_MODEL))
    c.add_argument("--report", default=str(DEFAULT_REPORT))
    c.add_argument("--out-json", default="")
    c.set_defaults(func=cmd_compare)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
