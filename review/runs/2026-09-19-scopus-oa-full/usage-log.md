# Phase usage log (token estimates)

Cursor does not expose billed tokens. `est_*` = characters/4. Screening/extraction
estimates that use extracted PDF text are **upper bounds**, not billed usage.
Do not treat these figures as an invoice.


| Phase | UTC | items | HTTP | est. in tok | est. out tok | est. total | notes |
|---|---|---|---|---|---|---|---|
| discovery | 2026-09-19T19:53:07 | 459 | 0 | 89267 | 103230 | 192497 | BibTeX import of scopus_export_Sep_19-2026_8427086a-dc52-4a34-8ac9-b27b3cdb9f9b_f563.bib |
| screening | 2026-09-19T19:54:57 | 459 | 0 | 89426 | 19766 | 109191 | title screen 185 include / 274 exclude; no abstracts in bib |
| fetching | 2026-09-19T20:07:22 | 185 | 92 | 1120 | 11915 | 13035 | fetched 46/185 public PDFs into papers/scopus-oa-full |
| screening | 2026-09-19T20:11:28 | 185 | 0 | 757788 | 28237 | 786025 | full-text screen of 46 retrieved PDFs: 44 include / 2 exclude; 139 not retrieved; upper bound = extracted PDF text |
| extraction | 2026-09-19T20:11:28 | 44 | 0 | 757788 | 65014 | 822801 | mechanical notes for 185 title-includes (44 included + not-retrieved/excluded stubs); claims only from retrieved text |
| table | 2026-09-19T20:11:28 | 44 | 0 | 65014 | 10517 | 75530 | literature table from extraction-index leads |
| synthesis | 2026-09-19T20:11:28 | 1 | 0 | 10517 | 6490 | 17007 | article-style review grounded in notes+table+prisma; no claims from 139 unread OA titles |
