---
name: review-form-ml
description: "Compare a draft review to published OA reviews with a small form-only model. Use after check_article.py, and when optimizing review-prose gates against real reviews."
---

# Review-form model (published vs catalog)

The quality scripts catch known failure modes. This step **measures** whether the title and Abstract still look like a published review or like a paper catalogue, by comparing them to open-access reviews retrieved from OpenAlex in several fields.

It copies **form only**. It is not a source of citations or findings.

## When to use

- After `check_article.py` is green, before telling the user the article is done.
- When adding or tightening a prose gate: collect gold reviews, retrain, see whether published reviews would fail the new rule.
- When the user asks to compare this draft with reviews in other fields.

Do not skip the ordinary scripts and critic. A high form score is not a licence to invent citations.

## Collect (OpenAlex, public OA only)

Contact email is the same polite-pool address as `find-papers` / `oa-fetch`.

```bash
python3 scripts/collect_gold_reviews.py \
  --mailto <contact-email> \
  --out-dir review/ml \
  --from-year 2019 --to-year 2026 \
  --include-style-study
```

Hits are `type:review` journal articles with abstracts. Title keyword filters keep endocrinology, nanomedicine, food-science, and neuroscience samples on-topic. **Do not cite these records** unless a public full text was retrieved and extracted as an included paper.

## Train and compare

```bash
python3 scripts/score_review_form.py train \
  --catalog review/ml/gold-catalog.json \
  --model review/ml/model.json

python3 scripts/score_review_form.py score \
  --article review/runs/<id>/article.md \
  --field endocrinology \
  --out review/runs/<id>/form-score.json

python3 scripts/score_review_form.py compare \
  --model review/ml/model.json \
  --report review/ml/comparison-report.md
```

`p_published_form` below **0.45** is catalog-like: flourish title, Abstract that starts with “This review discusses”, Author et al. stacks, acquisition talk, First/Second lists. Rewrite joinery (`review-prose`) and re-score.

Field `mean |z|` says how the Abstract differs from published reviews **in that field** (colon titles are common in endocrinology, less so in nanomedicine technology reviews). Large z on `abstract_acquisition` or `title_workflow` is a real defect. Large z on `title_kind_named` in nanomedicine is often a justified departure (those titles often omit “a narrative review”).

## Wire into the machine gate

`check_article.py --form-model review/ml/model.json` fails catalog-like front matter. `check_harness.py` passes that flag when `review/ml/model.json` exists. `article-qa` must run it.

## Hard rules

- Never import numbers, organisms, or claims from gold reviews into `article.md`.
- Never treat an OpenAlex hit as an included citation.
- Do not rewrite an earlier sample’s manuscript just to raise its score.
- Retrain after changing features; commit `review/ml/model.json` so scoring works offline.
