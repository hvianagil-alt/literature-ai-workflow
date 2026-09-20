# Form-quality model

This folder is **not** a literature review of findings. It stores a small classifier that asks: does this draft’s title and Abstract look like a **published open-access review**, or like a paper catalogue / chatbot draft?

| File | Role |
|---|---|
| `gold-catalog.json` | OpenAlex `type:review` hits (titles, DOIs, fields). Abstracts are stripped after training. |
| `gold-features.json` | Numeric form features for the gold set (enough to retrain offline). |
| `model.json` | Logistic weights + per-field centroids. Offline scoring. |
| `comparison-report.md` | Scores for in-repo articles vs the gold set. |
| `comparison.json` | Same numbers, machine-readable. |

Retrain:

```bash
python3 scripts/collect_gold_reviews.py --mailto you@example.com --out-dir review/ml --include-style-study
python3 scripts/score_review_form.py train --catalog review/ml/gold-catalog.json --model review/ml/model.json
python3 scripts/score_review_form.py compare --model review/ml/model.json
```

Do **not** copy science from `gold-catalog.json` into any `article.md`.
