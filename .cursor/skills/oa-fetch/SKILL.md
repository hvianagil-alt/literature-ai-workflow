---
name: oa-fetch
description: "Retrieve publicly available (open-access) PDFs for DOIs in a review catalog. Never bypass paywalls. Use after bib-import when the user asks you to find the PDFs."
---

# Open-access PDF fetch

Download full texts **only** from public OA sources.

## When to use

- After `bib-import` has produced `review/runs/<id>/catalog.json`.
- The user asked you to find/get PDFs (and typically said they should be OA).
- After `synthesis-rationale` lists interpretation gaps: fetch a **separate** catalog of selected OpenAlex hits (`review/runs/<id>/gap-retrieval/catalog.json`) into `papers/<id>-gapfill/`. Never overwrite the original run’s `fetch-log.json`.

## How

```bash
python3 scripts/fetch_oa_pdfs.py \
  --run-dir review/runs/<run-id> \
  --out-dir papers/<run-id> \
  --email <contact-email>
```

Lookup order per DOI: OpenAlex → Unpaywall → Europe PMC → publisher PDF URL conventions → `doi.org` content negotiation. A file is kept only if the body starts with `%PDF-`.

## Hard rules

- **No paywall bypass.** No Sci-Hub, no publisher login stuffing, no copying from sites that require a subscription cookie.
- If a record is marked OA in Scopus but no public PDF is found, log `no_public_pdf_found` and continue. Say so in the run log. Do not summarize from the title alone.
- PDFs stay under `papers/` (gitignored). The fetch log (`fetch-log.json`) is the auditable record.
- Unpaywall requires a real contact email; pass the user's, not a fake one.

## Handoff

For the original identification set: update PRISMA "reports sought / not retrieved" with `scripts/write_prisma.py`, then screen titles, then `paper-extraction` on retrieved files only.

For gap-fill catalogs: extract retrieved PDFs, add rows to the literature table, and log sought / found / not retrieved in `synthesis-rationale.md` section (g). Do not cite a DOI that did not yield a `%PDF-` file.
