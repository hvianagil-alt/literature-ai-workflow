# Run index — 2026-09-19-scopus-oa

Start here for the analysis trail.

| File | Role |
|---|---|
| `protocol.md` | Question, inclusion/exclusion, defaults (written before fetch) |
| `identification.bib` | Exact Scopus export |
| `catalog.json` / `catalog.csv` | Parsed 10 records |
| `fetch-log.json` | Per-DOI PDF outcome (9/10 public PDFs) |
| `screening.json` | Title/full-text decisions |
| `prisma.md` | PRISMA 2020 counts |
| `usage-log.jsonl` / `usage-log.md` | Phase effort and token *estimates* — **not** part of the article |
| `notes/` | Per-paper extraction (included + exclusion file) |
| `table/literature-table.md` | Side-by-side comparison |
| `synthesis-rationale.md` | Interpretation written **before** the article (what was measured, themes, gaps, outline, extra-retrieval log) |
| `gap-retrieval/` | Targeted OpenAlex searches + OA fetch log for interpretation gaps (does not replace `fetch-log.json`) |
| `article.md` | Journal-style review following that outline (no token tables) |

PDFs (gitignored) live in `papers/scopus-oa/`. Do not treat Huang 2026 as read.
