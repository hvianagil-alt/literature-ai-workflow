---
name: review-writing-craft
description: "PhD-level review writing distilled from published guides and same-field OA reviews: CARS introductions, given-new sentences, nested topics, hinge vs supporting papers. Read with review-prose before drafting article.md."
---

# Review writing craft (how published reviews actually write)

Read this **with** `review-prose` and `scientific-synthesis` before drafting or rewriting `article.md`. Those files cover genre, banned chatbot diction, and evidence layers. This file is what they still miss: **how a published narrative review moves**, sentence by sentence, compared with the papers a food scientist would actually read.

Copy **form only** from published reviews used as models. Do not import their findings.

## Why this file exists

`check_article.py` and the title/Abstract form model can score a draft as published-like while a reader still feels a catalogue. That happened on the high-pressure food reviews: the Abstract passed, the body still flattened every included paper into equal-depth paragraphs and never nested 3.1 topics the way *Foods* reviews do.

The guides below **converge**. Where they disagree, this workflow follows the published full texts in the same field, not the loudest blog.

## Sources (method, not citations for the manuscript)

| Source | What to take |
|---|---|
| Pautasso 2013, *Ten simple rules for writing a literature review* (PLOS Comput Biol) | Focus; criticise methods; logical structure; a diagram of the argument; do not stamp-collect papers |
| Gopen & Swan 1990, *The science of scientific writing* | Given information first (topic position); new information last (stress position); subject next to verb |
| Swales CARS (Create a Research Space) | Introduction = territory → niche/gap → occupy with an aim |
| SANRA (Baethge et al. 2019) | Importance, aims, search, referencing, **scientific reasoning**, endpoint data |
| Snyder 2019, *Literature review as a research methodology* | A review is a **method** whose product is synthesis, not a summary of papers |
| Torraco 2005 / Callahan 2014 (integrative reviews) | A new conception must emerge; chronological or alphabetical listing is not an argument |
| CASRAI *How to write a literature review* (2026) | Organise thematically, not source-by-source; synthesis vs summary self-check |
| Cochrane Handbook ch. 12 | Study-by-study narrative without grouping leaves the reader to synthesise |
| Gasparyan et al. / EASE; JBI step-by-step scientific review | Thematic body; strengths/weaknesses of studies in the same breath as the result; aim in the last intro sentence |
| Same-field OA reviews in *this* sample (form only), e.g. Houška 2022 and Zhang 2022 in *Foods* | Nested 2.1 / 3.1 / 4.2.1; a **Concluding remarks** close on each nest; supporting papers grouped |

## Where the sources agree (write this way)

They do not all use the same vocabulary. They do describe the same failure: a review that is an annotated bibliography. Pautasso: “Reviewing the literature is not stamp collecting.” Snyder: the product is synthesis. CASRAI: if a paragraph can be reordered into a one-line-per-source list without losing anything, it is summary, not a review. Cochrane: a study-by-study narrative without grouping leaves the reader to do the intellectual work. Torraco/Callahan: mechanistic listing (chronological or alphabetical) does not justify a unique conception. Houška and Zhang in *Foods* nest mechanisms (3.1 fruit products, 3.2 vegetable products, 4.2.1 texture enzymes) and close several nests with **Concluding remarks**.

They also agree on the Introduction: name why the topic matters, occupy a gap or tension, then state the aim. That is Swales CARS and SANRA items 1–2. Gopen & Swan then apply at sentence scale: old information in the topic position, the new measurement in the stress position.

## Where they disagree (this workflow’s choice)

Pautasso notes that IMRAD is rarely the spine of a review. SANRA still scores a described literature search. Published *Foods* narrative reviews keep a short Methods block, then nest the science. **Keep brief Methods (2.1–2.3). Do not turn the rest of the article into Results/Discussion dump headings.** Nested 3.1 topics are for mechanisms and disagreements, not for “Search results.”

## The convergence (write this way)

### 1. The unit of the paragraph is a question, not a paper

Wrong: one paragraph per included full text, each with design, n, and a log.

Right: the paragraph names a variable or a disagreement. Two or three **hinge** studies get design + n + result. Everyone else is grouped: *Several storage trials on chilled seafood report the same split between plates and colour [a,b,c].*

**All included papers are still cited** (somewhere in the argument or in Table 1). Citation is not a 120-word methods card.

Self-check (CASRAI): read the paragraph back. If it could become a bulleted, one-line-per-source list without losing structure, rewrite it around the relationship between the studies.

Pautasso Rule 5: keep the review focused. Snyder: synthesis changes the organising unit from the paper to the question.

### 2. Nest the body the way journals nest mechanisms

Published *Foods* HPP reviews do not run `## 3` then a wall of text. They use **3.1 Modelling fruit products**, **3.2 Vegetable products**, **4.2.1 Texture enzymes**. Houška ends several nests with **Concluding remarks**.

On a full manuscript, each thematic `##` needs at least one `###` that names a part of the mechanism or the disagreement. Methods `2.1 Search` does not count.

### 3. Introduction follows CARS, then teaches

1. **Territory** — the phenomenon is important (present tense). Teach the machine or physiology later sections assume.
2. **Niche** — what current options already do and still fail; the live controversy.
3. **Occupy** — last paragraph only: `The aim of this review is…`

Do not preview every later heading as a table of contents. Houška states the sections in one sentence; it does not list 3.1/3.2/3.3 as a menu.

### 4. Given → new (Gopen & Swan)

Start the sentence with what the reader already has (the coefficient you just named, `that hold`, `those spores`). Put the new measurement at the end, where stress falls. Do not open with `At 400 MPa for 9 min at 4 °C, unfrozen PBS…` unless the number **is** the topic.

One main new idea per sentence. A 60-word clause that stacks four statistics is two or three sentences.

Subject as close to the verb as English allows.

### 5. Be critical in the same sentence as the result

Pautasso Rule 6: after the review, the reader should know **the major achievements**, **the main areas of debate**, and **the outstanding research questions**. SANRA item 5 is scientific reasoning: name the evidence grade beside the claim (*laboratory challenge; scientific opinion; no food *C. botulinum* curve*).

Do not wait for the Discussion to mention that the assay was broth, or that n = 3.

### 6. State the thesis once; develop it

Do not repeat *a named cycle is not one outcome* / *the same megapascal* as a slogan. The title can carry that. The body shows ice, aW, agar, heat.

### 7. Close each nest before opening the next

Last paragraph of 3.1 (or a short 3.2 Concluding remarks): *Taken together… This heading cannot show…*

### 8. Discussion is a new intellectual move

Not a second Results. Answer: what is established; why the pattern; what cannot be concluded; what to measure. If a Discussion paragraph could be pasted into §3 unchanged, it is not doing the job.

### 9. Voice

Write as a scientist in the field, not as a reviewer of a folder. Banned outside Methods: `this sample`, `in this set`, `intellectual model`, `claim-ready`, `the literature table`, `harness`.

## Machine gate

```bash
python3 scripts/check_review_craft.py \
  --article review/runs/<run-id>/article.md
```

It fails a full manuscript that has no thematic 3.1 nests, that talks like a workflow, that repeats a thesis slogan, that is mostly one-paper paragraphs, or that never states a CARS niche before the aim.

Compare a draft to published OA full texts (form only):

```bash
python3 scripts/compare_review_craft.py \
  --ours review/runs/<id>/article.md \
  --published papers/<run>/SomePublishedReview.txt \
  --report review/ml/writing-craft-report.md
```

## Hard rules

- Do not import numbers from a published review that was opened only as a writing model.
- Do not skip this file because `check_article.py` already passed.
- Do not “fix” craft by adding empty `###` labels (`### Overview of paper 1`).
- Do not rewrite an earlier run’s `article.md` unless the user asked.
