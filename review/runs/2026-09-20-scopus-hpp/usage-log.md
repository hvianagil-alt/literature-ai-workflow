# Token and phase usage (separate from the review article)

This file is the run meter. **It is not part of the review article** (`article.md`).

Cursor does not expose billed model tokens to this workflow. `est_*` = characters ÷ 4. Do not treat these figures as an invoice.

Two numbers are given for several later phases:

- **Logged** — what `usage-log.jsonl` recorded at the time (several extraction/writing phases were appended with 0 characters).
- **Corpus upper bound** — size of the files that phase actually read or wrote, still characters ÷ 4. Screening/extraction bounds that use extracted PDF text are **upper bounds**, not billed usage.

HTTP counts are real request counts from the fetch scripts.

## HPP review run (`2026-09-20-scopus-hpp`)

### Logged rows (`usage-log.jsonl`)

| Phase | UTC | items | HTTP | est. in tok | est. out tok | est. total | notes |
|---|---|---|---|---|---|---|---|
| discovery | 2026-09-20T00:21:12 | 359 | 0 | 54 323 | 65 738 | 120 061 | BibTeX import of `scopus_export_Sep_20-2026.bib` |
| workflow | 2026-09-20T00:21:37 | 359 | 0 | 0 | 0 | 0 | Intake; narrative review defaults 2021–2026; HPP/nonthermal food |
| fetching | 2026-09-20T00:28:56 | 182 | 615 | 1 131 | 16 238 | 17 369 | 21/182 public PDFs (first pass) |
| fetching | 2026-09-20T00:31:14 | 182 | 290 | 1 131 | 16 018 | 17 149 | 26/182 public PDFs |
| fetching | 2026-09-20T00:41:28 | 182 | 970 | 1 131 | 18 058 | 19 189 | **final OA fetch: 49/182 public files** |
| screening | 2026-09-20T00:43:03 | 359 | 0 | 0 | 0 | 0 | title include 182; 49 OA files; 44 included after full-text exclusions |
| extraction | 2026-09-20T00:54:20 | 44 | 0 | 0 | 0 | 0 | 44 claim-ready notes from OA PDF/JATS (chars not metered) |
| table | 2026-09-20T00:54:20 | 44 | 0 | 0 | 0 | 0 | `table_from_notes.py` (chars not metered) |
| rationale | 2026-09-20T00:57:12 | 44 | 0 | 0 | 0 | 0 | `synthesis-rationale.md` plus OpenAlex gap searches |
| gap_retrieval | 2026-09-20T00:57:12 | 3 | 20 | 0 | 0 | 0 | 3 OpenAlex queries; 1/3 OA full texts |
| gap fetching | 2026-09-20T00:56:00 | 3 | 22 | 19 | 407 | 425 | 1/3 public files into `papers/2026-09-20-scopus-hpp-gapfill` |
| synthesis | 2026-09-20T01:01:46 | 44 | 0 | 0 | 0 | 0 | `article.md` passed `check_article.py` (chars not metered) |

Fetching was retried; the **last** fetch row is the one that matches PRISMA (49 public files sought). HTTP on the three fetch passes sums to **1 875** requests (retries included). Gap retrieval HTTP is **20 + 22 = 42** on top of that.

### Corpus upper bounds (files on disk, characters ÷ 4)

| Phase | What was measured | chars | est. tokens (÷4) |
|---|---|---|---|
| discovery | `identification.bib` | 218 222 | 54 556 |
| discovery catalog | `catalog.json` | 306 440 | 76 610 |
| screening decisions | `screening.json` | 46 900 | 11 725 |
| extraction input (upper bound) | extracted PDF/text under `papers/2026-09-20-scopus-hpp/extracted/` | 5 921 792 | 1 480 448 |
| extraction output | `notes/` (44 claim-ready notes) | 212 005 | 53 002 |
| table | `table/literature-table.md` | 47 981 | 11 996 |
| rationale | `synthesis-rationale.md` | 13 250 | 3 313 |
| gap-fill files | `papers/2026-09-20-scopus-hpp-gapfill/` | 429 701 | 107 426 |
| synthesis manuscript | `article.md` (current) | 46 015 | 11 504 |
| PRISMA trail | `prisma.md` | 29 396 | 7 349 |

If someone later asks “how much text did extraction look at?”, use the **1.48 million token** PDF-text upper bound, not the logged 0. That bound is the size of extracted full texts, not a model invoice.

### Later manuscript rewrites (same article, not a new review)

These were not separate `phase_log.py` rows. They reused `article.md` (~11.5k tokens of manuscript each pass): continuous-prose Abstract/Conclusions, nested headings, glued-heading split (§4.1 / §5.1 / §6.1), and sequential paragraph joins. Each rewrite reads the manuscript plus notes/table as needed; billed chat tokens for those Cursor sessions are **not** available here.

## Craft / form-study side runs (not the HPP science sample)

These runs copied **sentence form** from OA 2026 reviews. Their findings were not imported into the HPP article.

| Run | Phase | UTC | items | HTTP | est. total tok (÷4) | notes |
|---|---|---|---|---|---|---|
| `2026-09-20-style-study` | discovery | 2026-09-20T10:26:42 | 2 000 | 0 | 710 254 | BibTeX import of the 2000-record OA Review export |
| `2026-09-20-style-study` | fetching | 2026-09-20T10:29:28 | 40 | 255 | 6 847 | 40/40 public PDFs (batch 1) |
| `2026-09-20-style-study` | form notes | (file size) | — | 0 | ~1 046 | `form-notes.md` |
| `2026-09-20-style-study-batch2` | fetching | 2026-09-20T10:51:10 | 50 | 302 | 8 826 | 47/50 public PDFs; 3 `no_public_pdf_found` |

## What you cannot get from this log

Native Cursor/Grok **billed** input/output tokens per chat turn are not written into the repo. The meter above is the workflow’s own character-based estimate, plus HTTP counts for Unpaywall/OpenAlex/PMC fetches.
