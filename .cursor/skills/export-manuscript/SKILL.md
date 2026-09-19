---
name: export-manuscript
description: "Turn the finished Markdown article into HTML, Word, or PDF with Times New Roman and justified body text. Use only after article.md exists and the user asked for another file type. Default delivery is always Markdown."
---

# Export manuscript (optional)

The review is always written as Markdown (`article.md`). Word and PDF are extras. Do **not** delay the `.md` while waiting for an export. Ask once, after double-check, whether they also want `.docx` or `.pdf`.

## When to use

- The user said they want Word or PDF.
- After step 9 (`double-check.md` exists) you asked “Do you also want a Word or PDF copy?” and they said yes.

## What to do

1. Keep `review/runs/<run-id>/article.md` as the source of truth (also `review/report/final-report.md` if that copy exists).
2. Run:

```bash
python3 scripts/export_manuscript.py \
  --article review/runs/<run-id>/article.md \
  --out-dir review/runs/<run-id>/export \
  --format html,docx,pdf
```

`--format` may be a subset. `html` always works (Times New Roman, justified). `docx` and `pdf` need Pandoc (and a PDF engine for pdf). If a format cannot be built, say so and still give the HTML and the `.md`.

3. Tell the user, in plain language:
   - Markdown is the file to edit and to put in git.
   - HTML opens in a browser; Print → Save as PDF keeps the Times New Roman layout if that font is on their computer.
   - Word/PDF are copies; if they edit those, the next review run will not see the edits unless they say so.

## Style

Body text: Times New Roman (or Times), 12 pt, justified. Headings left-aligned. Tables may use a smaller size so they fit the page. Do not invent content while exporting.

## Hard rules

- Never replace `article.md` with a binary.
- Never claim a Word/PDF exists if the script failed.
- PDFs of copyrighted *source papers* stay gitignored; the review manuscript may be exported.
