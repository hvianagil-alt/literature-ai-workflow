---
name: article-qa
description: "Mandatory machine check after drafting article.md. Do not tell the user the review is done while check_extraction.py or check_article.py fails. Use as the last writing step of the literature-review workflow."
---

# First-pass quality gate

The article is **not done** when the file exists. It is done when the scripts below exit 0. Previous runs failed because mechanical notes and catalog sentences were delivered as a manuscript. This skill exists so the next sample works the first time.

## When to use

- Automatically after extraction (notes) and after drafting `article.md`.
- Before telling the user the review is ready.

## 1. Notes must be claim-ready (before the table)

```bash
python3 scripts/check_extraction.py \
  --notes-dir review/runs/<run-id>/notes \
  --screening review/runs/<run-id>/screening.json
```

If this fails: open each included PDF, fill `## Claim-ready facts` in the note (design, population, n, comparator, endpoint, result with units, what the design cannot show), and delete stub phrases (`mechanical first-pass`, `extracted lead`, `not stated in the extracted lead`). Then rebuild the literature table with `python3 scripts/table_from_notes.py --run-dir review/runs/<run-id>` — do not leave `write_table.py` DRAFT cells in the final table. `check_article.py --table` fails if those DRAFT markers remain.

## 2. Article must be a deliverable journal review (after drafting)

```bash
python3 scripts/check_article.py \
  --article review/runs/<run-id>/article.md \
  --table review/runs/<run-id>/table/literature-table.md
```

A full journal manuscript must pass the ~6,000-word body floor **and** the teaching-Introduction / thematic-spine gates. Word count alone is not enough.

If this fails: rewrite using `review-prose` (phenomenon-first Introduction; claim-first sentences; **continuous prose, never First/Second/Third or (i)/(ii) as the Abstract/Conclusions spine**; **thematic headings, never a generic Results dump**; no process talk; numbered Markdown results tables with in-text “Table 1” callouts; Abstract is a topic map with **no citations, no named papers, and no search/OA/year-window language**; numbered citations are Vancouver first-appearance order with a blank line between References entries; repeated terms are `Full term (ABBR)` once, then the abbreviation, without turning the Abstract into a glossary) and run the script again. Repeat until exit 0. The script fails if the Introduction is too short to teach, if the last Introduction paragraph lacks an aim, if a defined abbreviation still crowds the prose, if the Abstract defines unused or too many abbreviations, if `[n]` is not first-appearance order, **if the Abstract (or any section other than Methods) describes how papers were acquired**, **or if Abstract/Conclusions list the argument as First/Second or (i)/(ii)**. If only the numbers are out of sequence, run `python3 scripts/renumber_citations.py --article …` and re-check.

## Hard rules

- Do not skip these scripts.
- Do not argue with a failure. Fix the draft.
- Do not change a previous run’s `article.md` unless the user asked to rewrite that manuscript.
- Copy **form only** from published reviews used as craft models. Do not import their findings.

## Handoff

Only after both scripts pass: run the `double-check` skill (spot-check claims; write `double-check.md`). Only then tell the user where the **Markdown** article is and offer to iterate (add papers, adjust scope, refine a section, or export Word/PDF with `export-manuscript`).
