# Writing-craft comparison

Published reviews are **form comparators only**. Do not import their findings.
This file records (1) what published guides actually agree on, (2) how those rules
look in same-field OA full texts, and (3) how our `article.md` files score on the
same body-craft features. The title/Abstract form model (`review/ml/model.json`)
is a different gate; it can score `p_published_form = 1.0` while the body is still
a paper catalogue.

Features come from Pautasso (2013), Gopen & Swan (1990), Swales CARS, SANRA
(Baethge et al. 2019), Snyder (2019), Torraco/Callahan, CASRAI (2026), Cochrane
Handbook ch. 12, and from Houška 2022 / Zhang 2022 in *Foods* (form only).

## What the guides converge on

These sources do not share one vocabulary. They describe the same failure and the
same repair.

**The failure.** A review that is an annotated bibliography. Pautasso: “Reviewing
the literature is not stamp collecting.” Snyder: a review is a *method* whose
product is synthesis, not a summary of papers. CASRAI: if a paragraph can be
reordered into a one-line-per-source list without losing structure, it is
summary, not a review. Cochrane ch. 12: a study-by-study narrative without
grouping leaves the reader to synthesise. Torraco/Callahan: chronological or
alphabetical listing does not justify a unique conception.

**The repair, at outline scale.** Organise thematically (or methodologically when
methods drive disagreement), not source-by-source. Nest mechanisms. Close a nest
before opening the next. Pautasso Rule 6: after the review the reader should know
the major achievements, the main areas of debate, and the outstanding questions.
SANRA items 1–2 and Swales CARS: Introduction = territory → niche/gap → aim.

**The repair, at sentence scale.** Gopen & Swan: given information in the topic
position, the new measurement in the stress position, subject next to verb, one
main new idea per sentence.

**Where they disagree, and the choice this workflow makes.** Pautasso notes that
IMRAD is rarely the spine of a review. SANRA still scores a described literature
search. Published *Foods* narrative reviews keep a short Methods block, then nest
the science. Keep brief Methods (2.1–2.3). Nested 3.1 topics are for mechanisms
and disagreements, not for “Search results.”

Those rules now live in `.cursor/skills/review-writing-craft/SKILL.md` and are
enforced on a full manuscript by `scripts/check_review_craft.py`.

## Measured features

| File | nested 3.1 | meta-reviewer | slogan | one-paper para frac | intro words/sent | body words/sent | CARS niche | Author-Year openers | synth close | body words |
|---|---|---|---|---|---|---|---|---|---|
| published: 2026-09-20-hpp-rerun/Houška2022_020223.txt | 25 | 0 | 0 | 0.00 | 29.2 | 15.2 | 1 | 0 | 0.80 | 19323 |
| published: 2026-09-20-hpp-rerun/Zhang2022.txt | 23 | 0 | 0 | 0.00 | 0.0 | 10.1 | 0 | 0 | 0.00 | 11255 |
| published: 2026-09-20-hpp-rerun/Knoerzer2025627.txt | 0 | 0 | 0 | 0.12 | 0.0 | 25.7 | 0 | 0 | 0.00 | 10052 |
| ours: 2026-09-20-hpp-rerun/article.md | 0 | 2 | 3 | 0.04 | 27.2 | 29.4 | 1 | 0 | 0.71 | 8841 |
| ours: 2026-09-20-scopus-hpp/article.md | 11 | 0 | 0 | 0.12 | 18.1 | 22.2 | 1 | 0 | 0.14 | 7327 |
| ours: 2026-09-20-pd-cannabinoids/article.md | 0 | 1 | 0 | 0.00 | 23.4 | 26.3 | 1 | 0 | 0.14 | 9592 |
| ours: 2026-09-19-nanocarriers/article.md | 0 | 3 | 0 | 0.04 | 17.5 | 20.6 | 1 | 1 | 0.12 | 6151 |
| ours: 2026-09-19-scopus-oa-full/article.md | 12 | 0 | 0 | 0.03 | 23.5 | 25.3 | 1 | 0 | 0.00 | 7216 |

## How to read this

- **nested 3.1:** published narrative reviews split mechanisms into 2.1 / 3.1. A flat `## 3` with no children is a catalogue spine.
- **meta-reviewer:** `this sample`, `intellectual model`, `named cycle is not one` — workflow talk, not journal voice.
- **slogan:** repeating the title argument instead of developing it.
- **one-paper para frac:** share of long paragraphs that are a single study with n/MPa. Published reviews group supporting papers.
- **CARS niche:** Introduction states a gap or tension before the aim.
- **synth close:** share of thematic sections that end with a synthesis move (*Taken together*, *Concluding remarks*, *this heading cannot show*).

A draft can pass `check_article.py` and the title/Abstract form model and still fail these body-craft tests.

## Reading the published comparators (form only)

**Houška et al. 2022, *Foods*.** This is the form target. Numbered nests run 2.1 juices, 2.2 concluding remarks, 3.1 fruit-product inactivation, 3.2 vegetable products, 4.2.1 texture enzymes, 4.2.2 colour, 4.2.3 flavour. Several nests are literally titled **Concluding remarks**. The Introduction occupies a niche (“There is a need to provide a reliable overview…”) then states the sections in one sentence. Meta-reviewer diction is absent. One-paper file cards are absent. That is Pautasso Rule 5/7 and Snyder in print.

**Zhang et al. 2022, *Foods*.** Nested 2.1 primary models, 3.1 species, 3.3.1 high-pressure with moderate heat, 3.3.2 with low temperature, 3.5 water activity and pH. PMC text glues `1. Introduction` onto the license line, so the CARS/intro-length columns are not trustworthy for this extract. The nest count is.

**Knoerzer 2025.** A book-chapter extract whose headings are unnumbered (`Introduction to HPTP`). The nested-3.1 detector therefore reads 0. Do not treat that 0 as evidence that published reviews are flat; it is an extraction miss. Houška and Zhang are the usable form models.

## Reading our manuscripts

**HPP rerun (`2026-09-20-hpp-rerun`).** Passes `check_article.py` and `p_published_form = 1.0`. Fails the new craft gate: **0 thematic 3.1 nests** (only Methods 2.1–2.3), 2 meta-reviewer hits, 3 thesis-slogan hits. It *does* close sections (`synth close` 0.71) and it *does* occupy a CARS niche. The Abstract learned published form; the body is a wall of `##` arguments with equal-depth papers. That is the gap the user felt. **This manuscript is not rewritten in this change.** The gate exists so the next draft cannot ship that spine.

**HPP v1 (`2026-09-20-scopus-hpp`).** Nested 11 times (3.1 freezing, 3.2 strain, 4.1 milk, 5.1 spores…). Zero slogans, zero meta-reviewer hits. It still fails the gate because nests rarely close (`synth close` 0.14). Nesting without a Houška-style close is half the published move.

**Parkinson/cannabinoids and nanocarriers.** Flat thematic `##` walls, like the HPP rerun. Nanocarriers also talks like a workflow (`this sample` / `intellectual model`).

**Endocrinology full (`2026-09-19-scopus-oa-full`).** Nested 12 times (including Introduction 1.1–1.7, which is closer to a TOC than to Houška’s mechanism nests). Synth close 0.00. The gate currently fails it on closes, not on nest count.

## What this means for the next article

1. Read `review-writing-craft` with `review-prose` before drafting.
2. Each thematic `##` gets `###` 3.1 / 3.2 that name a mechanism or disagreement.
3. Two or three hinge studies get design + n + result; supporting papers are grouped and still cited.
4. Close each nest. Do not repeat the title as a slogan. Do not say `this sample` outside Methods.
5. `python3 scripts/check_review_craft.py --article …` must exit 0 before the critic. `check_harness.py --full` now runs that script.

Do not add empty `### Overview of paper 1` headings to game the nest count.
Do not import numbers from Houška or Zhang into a manuscript that used them only as form models.
Do not rewrite an earlier run’s `article.md` unless the user asked.
