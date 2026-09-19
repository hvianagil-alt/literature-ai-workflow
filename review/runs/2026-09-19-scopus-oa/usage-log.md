# Token and phase usage (separate from the review article)

This file is the run meter. **It is not part of the review article** (`article.md`).

Cursor does not expose billed model tokens. `est_*` = characters ÷ 4. Screening and extraction totals are **upper bounds** (full extracted PDF text size), not an invoice.

| Phase | UTC | items | HTTP | est. in tok | est. out tok | est. total | notes |
|---|---|---|---|---|---|---|---|
| workflow | 2026-09-19T19:32:11 | 0 | 0 | 0 | 0 | 0 | skills+scripts committed before fetch |
| discovery | 2026-09-19T19:32:11 | 10 | 0 | 1806 | 2093 | 3899 | BibTeX import of scopus_export_Sep_19-2026_296e443a-afe1-4c54-b398-619ca85845e3_3144.bib |
| fetching | 2026-09-19T19:32:59 | 10 | 48 | 65 | 2159 | 2224 | fetched 9/10 public PDFs into papers/scopus-oa |
| screening | 2026-09-19T19:36:18 | 10 | 0 | 210068 | 366 | 210434 | title+fulltext decisions; Li excluded on topic; Barrett excluded full text; Huang not retrieved |
| extraction | 2026-09-19T19:36:18 | 7 | 0 | 210068 | 4609 | 214677 | notes for 7 included + exclusion file; claims only from PDFs |
| table | 2026-09-19T19:36:19 | 7 | 0 | 4609 | 1135 | 5744 | literature table from notes |
| synthesis | 2026-09-19T19:37:31 | 1 | 0 | 5744 | 3420 | 9163 | first article draft (later rewritten without usage text in the article body) |
