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
| synthesis | 2026-09-19T19:37:31 | 1 | 0 | 5744 | 3420 | 9163 | article-style review grounded in notes+table+prisma; no claims from Huang |
| rationale | 2026-09-19T20:12:02 | 7 | 0 | 1135 | 4672 | 5807 | synthesis-rationale.md from notes+table (a-e); no tokens in article |
| gap_retrieval | 2026-09-19T20:12:02 | 8 | 6 | 500 | 2000 | 2500 | OpenAlex G1-G8; Huang DOI retry no_public_pdf_found; zero extra full texts included |
| synthesis | 2026-09-19T20:12:02 | 1 | 0 | 4672 | 4710 | 9382 | article rewritten from rationale outline; tokens remain in usage-log.md only |
| gap_retrieval | 2026-09-19T20:16:28 | 8 | 8 | 5000 | 3750 | 8750 | OpenAlex G1-G8; selected 8 DOIs; fetched 5/8 public PDFs into papers/scopus-oa-gapfill; Huang/Nauck/Marso not retrieved |
| extraction | 2026-09-19T20:16:28 | 5 | 0 | 100000 | 3000 | 103000 | gap-fill notes: Wilding STEP1, Knudsen 2019, Lincoff SELECT, Meurot 2022, Wang 2019 |
| table | 2026-09-19T20:16:28 | 12 | 0 | 3000 | 1000 | 4000 | table updated with 5 gap-fill rows |
| synthesis | 2026-09-19T20:16:28 | 1 | 0 | 3750 | 3500 | 7250 | article rewritten after rationale+gap-fill; no tokens in article |
