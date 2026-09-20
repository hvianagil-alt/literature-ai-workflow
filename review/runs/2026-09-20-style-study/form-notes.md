# Form notes (style only) — 2026-09-20 OA review sample

This run is **not** a scientific review of the 2,000 Scopus records. It is a craft study: how published review articles join sentences. **Copy form only.** Do not import findings, doses, diseases, or quotes from these papers into any other `article.md`.

## What was sampled

- Source: Scopus Review + open-access export, 20 September 2026 (`identification.bib`, ~2,000 records).
- Plan: stratified draw across journals/titles, then a small OA fetch; stop if the joinery pattern is stable.
- Fetched: 40 public full texts (`batch1.json`). Usable reviews: 39. **Caselli 2026 was skipped** — the retrieved file was not that paper.
- Stopped after batch 1. Further fetching was not needed: abstracts and introductions already agreed on the same joinery.

Full texts stay local and gitignored. These notes do not reproduce article bodies.

## What the usable reviews share (form)

**Abstracts** open on the phenomenon in present tense, then a tension (`yet`, `however`, `although`, `despite`), then how the review is organised around that tension, then a rank of evidence, then what the rank does not imply. They do not cite. Structured Background/Methods/Results/Conclusions labels appear in some journals; even there the sentences inside a label still argue, they do not enumerate “first thing, second thing.”

**Introductions** stay on one problem. The next sentence is usually a consequence, a scale, or a limit of the sentence before it (`this heterogeneity`, `these decisions`, `that claim`, `those numbers`). Contrast is a hinge, not a new bullet. When two regulatory or clinical questions exist, they are named as *one is… the other is…* inside the same paragraph, not as First/Second/Third.

**Evidence rank** sits inside the clause: which association is most consistent; which site or modality remains limited; which tool is front-line versus adjunct. The reader is not given a numbered tour of headings.

**Conclusions** (when unstructured) restate the calibrated claim and name the next measurement as ordinary sentences. They do not restart the paper as a shopping list.

## Joinery to copy

1. Anaphora: `this`, `these`, `that`, `those` pointing at the previous clause.
2. Semicolon or *and* for two tensions that belong together, rather than a new numbered item.
3. *Yet / however / at the same time / by contrast* when signals disagree.
4. Rank words: *most consistent*, *limited*, *front-line*, *does not imply*.
5. Close on a non-implication in the same voice as the findings.

## Joinery not to copy (common LLM habit)

- *First, … Second, … Third, … Finally, …* as the spine of Abstract, Introduction, Discussion, or Conclusions.
- *(i) (ii) (iii)* or *(1) (2) (3)* as the argument in Abstract or Conclusions (Methods may still number eligibility).
- *The first thing is… The second thing is…*
- *This review will first discuss X, then Y, then Z.*

## Encoded where

- `.cursor/skills/review-prose/SKILL.md` — section **Continuous prose**
- `scripts/check_article.py` — `ordinal_scaffold_problems`
- `AGENTS.md`, `report-writing`, `article-qa`, `double-check`, literature-review agent

The HPP narrative review already uses this joinery in its Abstract and Conclusions (one argument; next measurements as running sentences).
