# Phase usage log (token estimates)

Cursor does not expose billed tokens. `est_*` = characters/4. Screening/extraction
estimates that use extracted PDF text are **upper bounds**, not billed usage.
Do not treat these figures as an invoice.


| Phase | UTC | items | HTTP | est. in tok | est. out tok | est. total | notes |
|---|---|---|---|---|---|---|---|
| discovery | 2026-09-20T13:25:54 | 279 | 0 | 47369 | 55934 | 103303 | BibTeX import of scopus_export_Sep_20-2026-pd-cannabinoids.bib |
| fetching | 2026-09-20T13:38:32 | 134 | 819 | 838 | 16819 | 17657 | fetched 63/134 public PDFs into papers/2026-09-20-pd-cannabinoids |
| synthesis | 2026-09-20T13:58:07 | 31 | 0 | 0 | 0 | 0 | narrative article from 31 included full texts |
