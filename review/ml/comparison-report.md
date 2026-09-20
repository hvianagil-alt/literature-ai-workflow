# Form-quality comparison

This report scores **how** our reviews are written against a logistic model trained on published open-access review titles and abstracts (positive) versus catalog/chatbot mutations (negative). **Copy form only.** Do not import findings from gold reviews.

Trained: `2026-09-20T15:03:59.879388+00:00`  
Gold positives in model: 117  
Negatives: 229  
Train AUC: 1.0  
CV AUC: 1.0

## Scores

| Run                        | Field             | p(published form) | Decision       | Mean |z| vs field |
| -------------------------- | ----------------- | ----------------- | -------------- | ----------------- |
| 2026-09-19-nanocarriers    | nanomedicine      | 1.000             | published_like | 0.59              |
| 2026-09-19-scopus-oa-full  | endocrinology     | 1.000             | published_like | 0.44              |
| 2026-09-19-scopus-oa       | endocrinology     | 0.976             | published_like | 0.74              |
| 2026-09-20-scopus-hpp      | food-science      | 0.999             | published_like | 0.78              |
| 2026-09-20-pd-cannabinoids | neuroscience      | 0.999             | published_like | 0.33              |
| fixture-good               | generic-narrative | 1.000             | published_like | 0.56              |
| fixture-bad                | generic-narrative | 0.047             | catalog_like   | 1.13              |

## What the model treats as published-like

Positive weights (toward published form):

- `abstract_word_count` (+0.869)
- `abstract_sentence_mean` (+0.501)
- `abstract_contrast_per_100w` (+0.486)
- `abstract_sigla_defined` (+0.458)
- `abstract_hedge_per_100w` (+0.380)
- `title_has_colon` (+0.375)
- `title_kind_named` (+0.294)
- `abstract_calibration_per_100w` (+0.114)

Negative weights (toward catalog/chatbot form):

- `abstract_has_etal` (-1.009)
- `abstract_acquisition` (-0.952)
- `abstract_catalog_per_100w` (-0.928)
- `abstract_slogan_per_100w` (-0.911)
- `abstract_anaphora_per_100w` (-0.440)
- `title_flourish` (-0.405)
- `abstract_this_review_first_sentence` (-0.386)
- `abstract_ordinal` (-0.355)

## Per-run divergences

### 2026-09-19-nanocarriers

p(published form) = **1.000** (published_like).

- `title_word_count` z=+2.32
- `abstract_evidence_rank_per_100w` z=+2.30
- `abstract_word_count` z=+1.99
- `title_kind_named` z=+1.91
- `abstract_slogan_per_100w` z=-0.86

### 2026-09-19-scopus-oa-full

p(published form) = **1.000** (published_like).

- `abstract_sentence_mean` z=-1.61
- `abstract_hedge_per_100w` z=+1.15
- `abstract_calibration_per_100w` z=+0.82

### 2026-09-19-scopus-oa

p(published form) = **0.976** (published_like).

- `title_flourish` z=+3.87
- `abstract_acquisition` z=+2.65
- `abstract_evidence_rank_per_100w` z=+2.35
- `title_workflow` z=+1.00
- `abstract_sigla_defined` z=-0.92

### 2026-09-20-scopus-hpp

p(published form) = **0.999** (published_like).

- `abstract_hedge_per_100w` z=+6.46
- `abstract_anaphora_per_100w` z=+2.73
- `title_word_count` z=+1.09
- `abstract_contrast_per_100w` z=-0.88
- `abstract_word_count` z=+0.80

### 2026-09-20-pd-cannabinoids

p(published form) = **0.999** (published_like).

- `abstract_sentence_mean` z=+1.15
- `abstract_anaphora_per_100w` z=+0.96

### fixture-good

p(published form) = **1.000** (published_like).

- `abstract_calibration_per_100w` z=+1.84
- `abstract_word_count` z=-1.49
- `abstract_anaphora_per_100w` z=+1.49
- `title_word_count` z=-1.01
- `abstract_hedge_per_100w` z=+0.93
- `title_kind_named` z=+0.79

### fixture-bad

p(published form) = **0.047** (catalog_like).

- `abstract_anaphora_per_100w` z=+6.62
- `abstract_acquisition` z=+2.55
- `abstract_word_count` z=-2.51
- `title_has_colon` z=-2.38
- `title_word_count` z=-2.14
- `title_kind_named` z=-1.27

## How to use this

After `check_article.py` is green, run `python3 scripts/score_review_form.py score --article review/runs/<id>/article.md --field <field>`. If the score is catalog-like, rewrite joinery (claim-first sentences, contrast in the Abstract, no acquisition talk, no flourish title) before telling the user the article is done.

## Optimizations encoded in the workflow

These rules were added because they match the gold set and separate the catalog fixture from published-like drafts:

- Full-manuscript Abstracts must mark a tension or calibration (`yet` / `however` / `do not imply`). Gold abstracts almost never start with “This review discusses”; that opener now fails.
- Titles may not say `open-access set` or `this sample`.
- `check_article.py --form-model review/ml/model.json` fails catalog-like front matter. The harness passes that flag when the model file exists.
- Do **not** require “a narrative review” in the title for nanomedicine: only a minority of those gold titles name the kind. Colon subtitles are the endocrinology/neuroscience default, not a universal law.
- Do not import findings from this gold set into any manuscript.

