# Protocol — run `2026-09-19-scopus-oa`

Written **before** PDF retrieval. Defaults below are the ones used because the user asked to fetch PDFs, log tokens, include a PRISMA table, and produce a citation-backed review article from this Scopus export (no further scope confirmation in chat).

## Review question

In this Scopus open-access export, what is reported about **GLP-1 receptor agonists**, **stem-cell / exosome products**, and **drug-delivery systems** in **metabolic disease** (diabetes, obesity, and closely related inflammatory or repair settings)?

## Identification source

- File: user-uploaded Scopus BibTeX (`scopus_export_Sep 19-2026_….bib`)
- Database: Scopus (as stated in the file header)
- Export date: 19 September 2026
- No other databases were searched in this run

## Eligibility (inclusion)

A record is **included** if the full text (or, if unread, the title) is about at least one of:

1. GLP-1, GLP-1 receptor, GLP-1 receptor agonists, liraglutide, semaglutide, or related incretin drugs
2. Stem cells, mesenchymal stromal/stem cells, exosomes, or extracellular vesicles used as therapy or as a delivery vehicle
3. A drug-delivery system (nanoparticles, microneedles, niosomes, hydrogels, inhalation/pulmonary carriers, etc.)

**and** the disease or application context is metabolic (diabetes, obesity, prediabetes, diabetic complications) **or** a closely related inflammatory / tissue-repair setting where those tools are the intervention.

## Eligibility (exclusion)

- No substantive link to the three topic arms above (example: yeast plasmid engineering; molecular cardiology with no GLP-1 / stem-cell product / delivery system as the study intervention)
- Full text not retrieved
- Full text unreadable

Title-only exclusion is used only when the title is unambiguously off-topic. Borderline records go to full text.

## Emphasis

Balanced **methods + findings**. Output is a short **article-style review** with in-text citations, a reference list, a PRISMA 2020 count table, and a phase usage log.

## Accuracy rule

Numeric results, sample sizes, and mechanistic claims are taken from the PDF text (or marked "not stated" / "not retrieved"). Titles and DOIs come from the BibTeX catalog. Nothing is filled in from memory.

## Token / usage logging

Cursor does not expose billed token counts to this workflow. Each phase writes `usage-log.jsonl` with character counts and a **characters/4 token estimate**, plus HTTP call counts for fetching. Token estimates belong only in `usage-log.md` / `usage-log.jsonl`, never in `article.md` or `synthesis-rationale.md`.

## Phases (this run)

1. `workflow` — skills/scripts for bib import, OA fetch, PRISMA, usage log
2. `discovery` — parse the BibTeX export
3. `fetching` — public OA PDF retrieval
4. `screening` — title then full text
5. `extraction` — per-paper notes
6. `table` — comparison table
7. `rationale` — `synthesis-rationale.md` (mandatory before the article)
8. `gap_retrieval` — targeted OA searches for interpretation gaps; extra PDFs only if public
9. `synthesis` — article, following the rationale outline (after extra retrieval)
