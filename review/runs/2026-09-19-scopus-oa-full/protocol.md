# Protocol — run `2026-09-19-scopus-oa-full`

Same review question as the 10-record test run. This run uses the complete Scopus export (459 `@ARTICLE` records).

## Review question

In this Scopus open-access export (2024–2026), what is reported about **GLP-1 receptor agonists**, **stem-cell / exosome products**, and **drug-delivery systems** in **metabolic disease** (diabetes, obesity, prediabetes, and closely related inflammatory or repair settings)?

## Identification

- File: user-uploaded Scopus BibTeX `scopus_export_Sep 19-2026_8427086a-dc52-4a34-8ac9-b27b3cdb9f9b.bib`
- Export date: 19 September 2026
- No other databases

## Eligibility

**Include** if the title (then full text) is about at least one of:

1. GLP-1, GLP-1 RA, liraglutide, semaglutide, dulaglutide, exenatide, tirzepatide, or related incretin drugs
2. Stem cells, MSCs, exosomes, or EVs as therapy or carrier
3. A drug-delivery system (nanoparticles, microneedles, niosomes, hydrogels, inhalation/oral carriers, etc.)

**and** the setting is metabolic disease **or** a closely related inflammatory / tissue-repair context where those tools are the intervention.

**Exclude:** no such link; full text not retrieved; unreadable PDF.

The BibTeX has **no abstracts**, so title screening uses title keywords only. Borderline titles are kept for full text.

## Emphasis

Methods + findings. Article-style review. Claims only from retrieved text (or marked not retrieved / not stated).

## Token logging

Same as the test run: characters/4 estimates in `usage-log.jsonl`, not billed tokens.
