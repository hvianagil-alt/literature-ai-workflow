---
name: double-check
description: "Mandatory second look after the machine quality gate. Spot-check claims against notes and PDFs, confirm the Abstract and tables, write a short log, and only then call the article done. Use after article-qa scripts pass."
---

# Double-check (after the scripts)

`check_extraction.py` and `check_article.py` catch stubs, catalog voice, missing tables, and citations in the Abstract. They do **not** catch a wrong number, a DRAFT literature table, or a note that still only contains the PDF lead. This step is that second look. Do not tell the user the review is done until it is finished.

## When to use

- Automatically after step 8 (`article-qa`) exits 0.
- When the user asks to re-run the same papers, compare two passes, or “make sure it is high quality.”
- On a re-run of the same sample: keep the previous `article.md` as `article-pass1.md` (or dated), write the new manuscript as `article.md`, and record ranks in `double-check.md`.

## What to do (in order)

1. **Keep the previous manuscript** if this is a second pass on the same papers. Copy `article.md` to `review/runs/<run-id>/article-pass1.md` before rewriting.
2. **Notes vs scripts.** If `check_extraction.py` failed, stop and fill `## Claim-ready facts` from the PDF. Do not double-check a stub corpus.
3. **Literature table.** If cells still say “mechanical first-pass”, “extracted lead”, or paste the PDF lead into Key findings, rewrite every included row from Claim-ready facts (`scripts/table_from_notes.py`). The extraction worksheet is not finished while those phrases remain.
4. **Spot-check numbers.** Pick at least **five** numeric claims in `article.md` (n, %, RR, bioavailability, *P*). Open the matching note. If the note and the sentence disagree, open the PDF. Correct the note, the table row, and the article. Never invent the number.
5. **Abstract and title.** No `[n]`, no *et al.*, no stack of effect sizes. Title is `Topic: a narrative review of …` (or the matching kind). See `review-prose`.
6. **Abbreviations.** Repeated terms are `Full term (ABBR)` at first use, then the abbreviation (`type 2 diabetes (T2D)`, then `T2D`). Headings may stay expanded. Fix leftover long forms in Results and Discussion.
7. **In-article tables.** At least one Markdown pipe table and an in-text `Table N` sentence. Cells must match the notes.
8. **Discussion.** Interprets findings. No identification counts, fetch logs, or token meters.
9. **Write the log** to `review/runs/<run-id>/double-check.md` (or `review/report/double-check.md`):

```markdown
# Double-check — <run-id>

- Scripts: check_extraction.py … ; check_article.py …
- Notes still stub? yes/no (count)
- Table still DRAFT/lead-paste? yes/no
- Claims spot-checked (paper, number, note/PDF agree?):
  - …
- Abstract: citations? named papers?
- Abbreviations: repeated terms defined once then shortened?
- Tables in article: Table 1 … mentioned in prose?
- If two passes: rank pass 1 vs pass 2 on abstract, tables, traceability, Discussion, completeness (1–5 each) and say which is the deliverable.
```

## Re-running the same papers

Scope stays the agreed protocol. Do not silently drop or add papers. Extra OA retrieval is only for interpretation gaps (step 6), not a new field survey. The deliverable is the **new** `article.md` after this log, not the pass-1 file.

## Hard rules

- Never fabricate a correction. If the PDF cannot be read, say so in the log and in the article.
- Do not skip this step because the scripts passed.
- Do not import findings from reviews that were read only to learn form.

## Handoff

After the log exists and remaining fixes are in `article.md`, tell the user the article is ready and point at `double-check.md`. Offer to iterate (add papers, adjust scope, refine a section).
