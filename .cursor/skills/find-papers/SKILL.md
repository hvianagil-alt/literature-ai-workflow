---
name: find-papers
description: "When the user did not drop PDFs, or dropped a small seed set, search free open-access databases and fetch the PDFs. Never invent citations. Never use a paid API. Ask before any login. Use at intake, before extraction."
---

# Find papers (free search + OA fetch)

The user may not have a folder of PDFs. They may drop ten papers on a topic and expect you to find more like them. This skill does that **without inventing citations** and **without a paid subscription**.

It is **not** a bibliography from memory. Hits come from the OpenAlex API. A paper is evidence only after `oa-fetch` saved a real `%PDF-` file.

## When to use

- `papers/` is empty (or has no PDFs) **and** the user named a topic or research question.
- The user dropped a **seed set** (for example ten PDFs or a short `.bib`) and said to review that topic — search for **related** OA papers from those titles.
- The user said “find papers on X” / “I don’t have the PDFs yet.”

Do **not** wait for a special opt-in if the search is free and cheap. Do it. Still stop at the **direction check** before you extract a large fetched set.

Do **not** use this instead of gap-driven retrieval after the table (that remains `related-paper-exploration` Mode B). This skill is **intake**.

## Free only — ask before any login

Allowed, no API key:

- OpenAlex (`scripts/find_papers.py` / `scripts/search_oa_related.py`)
- Unpaywall, Europe PMC, publisher OA URLs already in `oa-fetch`

Need a **contact email** once (OpenAlex polite pool and Unpaywall). That is not a paid account.

1. Reuse `OPENALEX_MAILTO`, `UNPAYWALL_EMAIL`, or an email the user already gave for a fetch in this run.
2. If none: **ask once** — “I need a contact email for the free OpenAlex/Unpaywall pool. It is not a login and not a paid API.”
3. Do **not** invent an email. Do **not** sign up for Scopus, Semantic Scholar paid tiers, Sci-Hub, or publisher logins.
4. If they would rather drop PDFs themselves, point at `papers/README.md` and wait.

If a later step needs a connection you do not have (institutional proxy, Scopus API key), **ask first**. Never buy anything.

## Low token cost

- Search with the **script**. Read the JSON (title, year, DOI, OA flag). Do not paste PDF bytes into the chat to “search.”
- One to three queries, not one query per seed paper. `--per-page` 15–25 (max 50).
- Fetch PDFs to disk with `fetch_oa_pdfs.py`. Extract later in step 4.
- Do not open every landing page in a browser.

## How

### A. Empty folder — search the topic

After they state the topic (or you already have it from intake):

```bash
python3 scripts/find_papers.py \
  --query "<topic in ordinary words, from the user>" \
  --mailto <contact-email> \
  --run-dir review/runs/<run-id> \
  --origin topic_search \
  --per-page 20 \
  --from-year <year they chose, or current year minus 5 if they said just go> \
  --to-year <year they chose, or the current year> \
  --journal-quality journal \
  --sort relevance_score:desc
```

`--journal-quality` is `none` | `journal` | `doaj` | `cited` (see `scripts/search_oa_related.py`). Optional `--min-cited-by`. Ask at the direction check; do not silently search all years or all venues.

### B. Seed papers — search related work

Build **one or two** queries from the **shared topic** of the seeds (filenames, first-page titles, or bib titles). Do not invent extra keywords the seeds do not support.

```bash
python3 scripts/find_papers.py \
  --query "<shared topic of the seeds>" \
  --mailto <contact-email> \
  --run-dir review/runs/<run-id> \
  --origin related_to_seeds \
  --per-page 20 \
  --from-year <agreed year floor> \
  --to-year <agreed year ceiling> \
  --journal-quality journal
```

## Seeds vs filters

Do **not** drop the user's seed PDFs because they are older than `--from-year`. The year and journal-quality flags apply to **retrieved** related work.

### Then fetch (public OA only)

```bash
python3 scripts/fetch_oa_pdfs.py \
  --run-dir review/runs/<run-id>/seed-search \
  --out-dir papers/<run-id>-found \
  --email <contact-email>
```

A file is kept only if it starts with `%PDF-`. Log not-retrieved rows. **No paywall bypass.**

## What you tell the user

In plain language:

- How many API hits came back, how many PDFs were actually retrieved.
- The **titles as the API returned them** (not a list you recalled).
- That paywalled records were skipped, not stolen.
- That you will confirm scope (step 2) before extracting.

If OpenAlex errors or returns zero hits: say so. Do not pad with remembered papers. They can still drop PDFs into `papers/` by hand.

## Quality bar

- **Never fabricate a citation.** If it is not in `seed-search/search.json`, you do not name it as found.
- Do not cite a hit until the PDF is on disk.
- Do not treat `catalog.json` as the included set. Inclusion is after the direction check and screening.
- Duplicate DOIs already in the seed folder: skip the fetch or say it is already there.

## Handoff

Fetched PDFs live in `papers/<run-id>-found/` (gitignored). Then **direction check** on the combined set (seeds + retrieved). Then `paper-extraction`. Then the rest of `AGENTS.md`. Do not jump to the article.
