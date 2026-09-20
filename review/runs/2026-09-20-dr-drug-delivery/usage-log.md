# Phase usage log (token estimates)

Cursor does not expose billed tokens. `est_*` = characters/4. Screening/extraction
estimates that use extracted PDF text are **upper bounds**, not billed usage.
Do not treat these figures as an invoice.


| Phase | UTC | items | HTTP | est. in tok | est. out tok | est. total | notes |
|---|---|---|---|---|---|---|---|
| workflow | 2026-09-20T22:48:32 | 1 | 0 | 0 | 0 | 0 | protocol written; user asked for a test review on drug delivery for diabetic retinopathy; just-go defaults 2021-2026 journal OA |
| discovery | 2026-09-20T22:48:32 | 52 | 3 | 0 | 0 | 0 | OpenAlex 3 queries, 60 hits, 52 unique DOIs after merge |
| fetching | 2026-09-20T22:54:40 | 26 | 155 | 159 | 3663 | 3821 | fetched 14/26 public PDFs into papers/2026-09-20-dr-drug-delivery-found |
| screening | 2026-09-20T23:02:19 | 52 | 0 | 0 | 0 | 0 | title screen 26 sought; 22 full texts included; 4 not retrieved |
| extraction | 2026-09-20T23:09:07 | 22 | 0 | 0 | 0 | 0 | 22 claim-ready notes from public full texts |
| table | 2026-09-20T23:09:07 | 22 | 0 | 0 | 0 | 0 | table_from_notes.py from Claim-ready facts |
