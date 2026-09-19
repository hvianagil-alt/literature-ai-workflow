# PRISMA 2020 flow — 2026-09-19-scopus-oa

Counts below are taken from this run's catalog, fetch log, and screening log.
They are not inferred. Empty cells mean the step has not been recorded yet.

## Identification

| Source | n |
|---|---|
| Records from Scopus export (`identification.bib`) | 10 |
| Additional records from other sources | 8 |
| Duplicates removed | 0 |
| Records after duplicates removed | 18 |

## Screening

| Step | n |
|---|---|
| Records screened (title/metadata) | 10 |
| Records excluded at title/metadata (with reason) | 1 |
| Reports sought for retrieval (full text) | 9 |
| Reports not retrieved | 1 |
| Reports assessed for eligibility (full text) | 8 |
| Reports excluded at full text (with reason) | 1 |

## Included

| Set | n |
|---|---|
| Studies included in the review | 12 |

## Exclusion reasons (title/metadata)

- `Li2026` — Title/full text is yeast plasmid copy-number engineering; no GLP-1 RA, stem-cell/exosome product, or drug-delivery intervention in metabolic disease.

## Exclusion reasons (full text)

- `Barrett2026` — NHS Digital Weight Management Programme mixed-methods evaluation; GLP-1 drugs appear only in discussion/references, not as the study intervention.

## Not retrieved

- `Huang2026` — Scopus/Unpaywall gold OA, but no public PDF body obtained on the original fetch or the gap-fill retry (`no_public_pdf_found`; ScienceDirect 403; PMC HTML).
- Gap-fill catalog (8 selected DOIs): Nauck 2020 (`10.1016/j.molmet.2020.101102`) and Marso 2016 SUSTAIN-6 (`10.1056/nejmoa1607141`) also `no_public_pdf_found`. Huang counted in both the original “not retrieved” row and this retry.

## Additional records (interpretation-gap retrieval)

Eight DOIs were selected from OpenAlex hits to address named gaps (see `gap-retrieval/selection-log.json`). Off-topic API hits were not fetched. Five public PDFs were extracted and included (Wilding 2021, Knudsen 2019, Lincoff 2023, Meurot 2022, Wang 2019). These five are the “additional records” that entered the included set (7 + 5 = 12). They were not part of the Scopus export.

## Notes

Li2026 was excluded at title (confirmed on full text, which was retrieved). Huang2026 was sought twice and not retrieved. Barrett2026 was assessed in full text and excluded. Guo2026 was kept after full text because the paper reports semaglutide/GLP-1–related angiogenesis experiments, which the title alone did not make obvious. Gap-fill papers are documented in `synthesis-rationale.md` section (g) and `gap-retrieval/`.
