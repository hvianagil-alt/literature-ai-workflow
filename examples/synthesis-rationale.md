<!--
EXAMPLE OUTPUT — fictional papers, for illustration only.
See examples/README.md. This is what synthesis-rationale.md looks like
after the table and before the journal article. Do not cite as real research.
-->

# Synthesis rationale — EXAMPLE (fictional papers)

**Research question (example):** Does structured note-taking during reading improve recall of technical material compared to unstructured note-taking?

This file is the interpretation step. It is not a token or phase meter, and it is not the article.

## (a) What each included study actually measured

Four fictional papers (Al Researcher 2021; Bea Scholar 2022; Chen Example 2023; Dee Sample 2024). See [`literature-table.md`](literature-table.md). One paper (Eli Notincluded 2020) was excluded (wrong domain).

## (b) Themes the data support vs themes that would be forced

**Supported:** a small positive recall effect in the same direction in three papers; domain as a possible moderator in one paper.

**Would be forced:** “structured notes are proven for STEM,” which rests on a single study with a null STEM result.

## (c) Real disagreements and why

Bea Scholar 2022’s null STEM finding sits in tension with Chen Example 2023’s pooled positive effect. A plausible reason is that the meta-analysis averages across domains — **this is a hypothesis until more domain-stratified trials are in the sample.**

## (d) What this sample cannot answer

Longer-than-one-week retention; school-age learners; whether the STEM/humanities split replicates.

## (e) Outline of the review

1. Scope of this four-paper example set.
2. Direction of the recall effect (Al Researcher, Chen Example, Dee Sample).
3. Domain as a moderator (Bea Scholar) — single-study, preliminary.
4. Gaps and implications.

## (f) Interpretation gaps (must attempt retrieval)

1. **G1 — striking finding without a comparator.** Bea Scholar 2022 reports no structured-note effect for STEM material. This sample has no other STEM-only trial, so that null cannot be put in perspective.
2. **G2 — missing duration.** All four papers stop at one week. No included paper tests semester-length recall.

## (g) Targeted extra retrieval log

*(In a real run this table is filled from OpenAlex + OA fetch. Here the “hits” are also fictional, to show the log format.)*

| Gap | Sought | Found (PDF kept) | Not retrieved | Included in table? |
|---|---|---|---|---|
| G1 STEM null | OpenAlex query `structured note-taking STEM recall experiment` (fictional) | Fictional Fay Replicator, 2023, *Placeholder STEM Education* — OA PDF retrieved | Fictional famous trial remembered from memory — **not listed as a citation; no DOI from the API** | Yes, after extraction |
| G2 duration | OpenAlex query `note-taking delayed recall semester` (fictional) | none | API returned 0 OA hits with DOIs | No — gap left open |

**Rule illustrated:** a paper you “remember” but did not retrieve is not a citation. An empty found-column is allowed.

## (h) Decision to write

Rationale + extra retrieval are done. The article may be written from the updated table (four original rows + Fay Replicator 2023). G2 remains open and must be stated in the article. No token estimates in the article.
