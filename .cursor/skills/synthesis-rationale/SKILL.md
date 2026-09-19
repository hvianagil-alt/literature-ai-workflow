---
name: synthesis-rationale
description: "Mandatory gated step after the literature table: interpret the whole sample, list interpretation gaps, and attempt targeted OA retrieval of extra papers before any journal article is written. Never invent citations. Use after literature-table and before report-writing."
---

# Synthesis rationale and gap-driven extra retrieval

This is a **hard sequencing gate**. Do **not** write `article.md` / `final-report.md` until this step is finished. It is not optional, not “nice to have,” and not something to skip because the table already looks complete.

The point: understand the corpus as a scientist would — what it actually is, what it can support, and where a result cannot yet be put in perspective — **then** try to fill those interpretation gaps with additional **real, retrievable** open-access papers. Only after that, write the review.

## When to use this skill

- Automatically, after `literature-table` has produced a table for the in-scope sample.
- Never as a substitute for the direction check (that still happens first).
- Never as a license to pad the bibliography with remembered-sounding titles.

## Inputs

- `review/table/literature-table.md` (and the run copy, if any)
- `review/notes/*.md` (or `review/runs/<run-id>/notes/`)
- The agreed research question, inclusion/exclusion, and protocol
- Fetch/PRISMA logs so “not retrieved” papers stay visible

## Output (required files)

Write **`synthesis-rationale.md`** before fetching extras and **before** any article:

- Run-based review: `review/runs/<run-id>/synthesis-rationale.md`
- Folder-of-PDFs review: `review/report/synthesis-rationale.md` or `review/notes/_synthesis-rationale.md`

Use this structure (keep (a)–(e) even if you also write a prose summary; report-writing follows (e)):

```markdown
# Synthesis rationale — <run-id or topic>

## (a) What each included study actually measured
<One short block per included paper: design, population, endpoints, n.
 Say what it did *not* measure. No article prose yet.>

## (b) Themes the data support vs themes that would be forced
<Supported constructs from the table, vs claims that would over-read the set.>

## (c) Real disagreements and why
<Conflicting numbers, or papers that look related but do not share an endpoint.
 Prefer incommensurable over fake controversy.>

## (d) What this sample cannot answer
<Honesty list: missing comparator, mechanism, population, or unread eligible record.>

## (e) Outline of the review
<Numbered section plan for the article. Topic sentences, which papers appear where.
 Do not draft the article here.>

## (f) Interpretation gaps (must attempt retrieval)
<Numbered. Each gap is a result that cannot be put in perspective from the
 current notes/table: thin evidence; conflicting results; missing comparator,
 mechanism, or population; a striking finding with no external anchor;
 an eligible paper that was not retrieved.>

## (g) Targeted extra retrieval log
<Filled in *after* attempting retrieval. For every gap: sought / found /
 not retrieved. Never invent a citation to fill a blank.>

## (h) Decision to write
<Rationale + extra retrieval are done; the article may now be written from the
 *updated* table. List gaps that remain open. Update (e) if new papers were included.>
```

See [`examples/synthesis-rationale.md`](../../../examples/synthesis-rationale.md) for a fictional worked snippet.

**No article yet** when the first draft of this file is written. Do not draft `article.md` in the same breath as the first rationale pass.

## Interpretation gaps — what counts

A gap is **not** “I wish we had more papers.” It is a concrete obstacle to honest interpretation, for example:

- A striking numeric result (effect size, bioavailability, ranking) with no comparator in the sample
- Two included papers that appear to disagree but cannot be compared (different species, endpoint, or dose)
- A missing population, mechanism, or standard-of-care arm that the included papers themselves invoke
- An eligible record that was **not retrieved** (still must not be cited as evidence)
- n, duration, or safety too thin to support the sentence you would otherwise write

If there are genuinely **no** interpretation gaps, say so in the rationale and still write a one-line retrieval log (“no extra retrieval indicated”). Empty-gap claims should be rare; a small heterogeneous sample almost always has some.

## Targeted extra retrieval (mandatory attempt)

For **each** numbered gap:

1. Use the `related-paper-exploration` skill in **gap-driven mode** (not the optional pre-extraction browse). Quality bar is unchanged: **never invent a citation**.
2. Prefer leads already named in the included papers’ own references or discussion (those titles exist in the PDFs).
3. Search public bibliographic APIs; do not guess DOIs. Helper:

   ```bash
   python3 scripts/search_oa_related.py \
     --query "your gap-specific query" \
     --mailto you@example.com \
     --out review/runs/<run-id>/gap-retrieval/search-<gap-id>.json
   ```

4. From the search hits, **select only** papers that actually address that gap. Do not bulk-include the whole hit list. Record why each candidate was chosen or skipped.
5. Fetch **public OA PDFs only** via the `oa-fetch` skill (OpenAlex, Unpaywall, Europe PMC, publisher OA, `doi.org` negotiation). **No paywall bypass.** Use a **separate** catalog so you do not overwrite the original run’s `fetch-log.json`:

   ```bash
   python3 scripts/fetch_oa_pdfs.py \
     --run-dir review/runs/<run-id>/gap-retrieval \
     --out-dir papers/<run-id>-gapfill \
     --email you@example.com
   ```

6. Log every candidate as **sought / found (PDF kept) / not retrieved** (no public PDF, HTTP failure, unreadable). Retrying a previously failed eligible DOI (same OA rules) is allowed; still do not cite it if the PDF never arrives.
7. **Extract** newly included PDFs with `paper-extraction` into `notes/`. Mark them as gap-fill additions (which gap they were fetched for).
8. **Rebuild** the literature table so extra papers are rows, not footnotes the article invents later.
9. Update the **Targeted extra retrieval log** and **Decision to write** sections of `synthesis-rationale.md`.

If the network is down, the API returns nothing, or no OA PDF exists: **say so**. Then write the article with those gaps left open. Do **not** fill them from memory, from a paywalled abstract, or from a title.

## Hard rules

- Never fabricate a citation, quote, DOI, or finding.
- Never silently skip a paper (seed or gap-fill). Unreadable / not retrieved / out of scope must be named.
- Do not cite a paper you did not extract from a full text in this run.
- Do not put token estimates, phase meters, or script names in `article.md`. Usage stays in `usage-log.md`.
- Extra retrieval is **targeted**. It is not a new systematic review of the whole field unless the user asked for that.

## Failure modes

| Situation | What to do |
|---|---|
| Tempted to start the article because the table is done | Stop. Write the rationale first. |
| A gap would be easy to “fill” with a famous trial you remember | Search + OA fetch. If you cannot retrieve the PDF, the gap stays open in both rationale and article. |
| Search returns 50 hits | Pick the few that address the gap; log the rest as not selected (with reason). |
| New PDF is off-topic after reading | Extract a short out-of-scope note; do not add it to the included table rows. |
| Sibling run is fetching hundreds of PDFs in another folder | Do not kill that process. Keep gap-fill PDFs in their own `papers/<id>-gapfill/` directory. |

## Handoff

Only after **Decision to write** is filled: read `review-prose`, then use the `report-writing` skill. That skill must read this file and use section **(e)** as the article outline. The article is a secondary review: the Introduction must teach the field, body text should reach ~6,000 words (~20 Word pages) unless the user asked for a short note, and chatbot flourishes are banned (`review-prose`). The article must be a PhD-quality, argument-driven review of **all** in-scope evidence (original sample **plus** successfully retrieved gap-fill papers). Every included study is discussed with design and results. **Discussion and Conclusions are scientific interpretation** (mechanisms, pooling, clinical meaning, evidence limits). Do not put identification counts, fetch logs, HTTP errors, or token estimates in those sections. Remaining open **scientific** gaps must appear as unanswered questions, not as silent omissions. Do not put token estimates in this file or in the article.
