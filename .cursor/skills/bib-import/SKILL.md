---
name: bib-import
description: "Parse a Scopus/BibTeX export into a screening catalog for a review run. Use when the user provides a .bib/.ris export instead of (or before) dropping PDFs."
---

# BibTeX / Scopus import

Turn a database export into a numbered identification set (PRISMA "records identified"). Do this **before** fetching PDFs.

## When to use

- The user uploaded a Scopus, PubMed, or other `.bib` file.
- The user wants a documented identification set, not an ad-hoc folder of PDFs.

## How

```bash
python3 scripts/import_bib.py path/to/export.bib --run-dir review/runs/<run-id>
```

That writes `catalog.json`, `catalog.csv`, copies the bib to `identification.bib`, and appends a `discovery` line to `usage-log.jsonl`.

## Quality bar

- Count every `@ARTICLE` / `@article` (and other entry types). Do not drop records silently.
- Do not invent DOIs, titles, or years. If a field is missing, leave it blank.
- Scopus `note = {Cited by: N; All Open Access; ...}` is metadata, not a finding. Preserve it on the catalog row.
- This step is identification only. Inclusion/exclusion happens later (see `prisma-logging`).

## Handoff

Next: `oa-fetch` skill if the user asked you to retrieve PDFs, then title screening, then `paper-extraction`.
