# Structure notes (form only)

These notes describe **how** the sampled review articles are built. They do **not** record scientific claims, numbers, or examples from those papers. Nothing here may be copied into a manuscript as evidence.

## Sample

- 385 Scopus records, all `type = Review`, all OA-flagged; 350 gold OA.
- Title-kind mix (a paper can count in more than one bucket): unlabeled 262; systematic 69; meta-analysis 59; narrative (in the title) 34; scoping 9; network meta-analysis 8; umbrella 1.
- 72% of titles use a colon subtitle (`Topic: a narrative review of…` / `…: a systematic review and meta-analysis`).
- Full texts opened for **form**: 5 OA PDFs (one systematic/meta-analysis; one physiology series review; one labeled narrative review; one mini-review; one mechanisms review).
- Not retrieved as public PDF: 3 sampled records (publisher HTML instead of PDF, or no public PDF). Logged in `sample-fetch/fetch-log.json`. Do not cite them.

## Spines (Match kind → outline)

Published reviews in this sample do not share one template.

1. **Systematic review / meta-analysis** uses IMRaD: structured abstract; Introduction; Methods split into search, eligibility, selection, extraction, quality, statistics; Results split into flow, characteristics, primary, safety, secondary; Discussion; Conclusion.
2. **Narrative clinical review** uses: unstructured abstract; keywords; optional bullet takeaways (claim + evidence grade); Introduction that ends in a thesis; a **short** Methods paragraph; then **thematic** body headings; Discussion/Conclusions.
3. **Physiology / mechanisms review** opens on the organismal problem; may omit Methods in the journal; uses deep nested topic headings; closes with numbered research directions and critical gaps.
4. **Mini-review** may use a summary instead of a structured abstract, numbered thematic sections, and a short closing remarks section.

The default article in this workflow is (2): narrative with brief methods, unless the user asked for a systematic review or a pooled analysis.

## Introduction order

1. First sentence: the phenomenon in **present tense** (biology or the clinical problem). Not “This review discusses…”. Not “In recent years, X has gained attention.”
2. Teach what later sections assume.
3. What current therapy already does and still fails; where the map is incomplete.
4. Last paragraph only: aim or **central argument**. The words “this review” belong here.

## Abstract order

1. Established problem.
2. Tension (*yet…*, *at the same time…*): missing coverage, or two signals that do not point the same way.
3. Calibrated findings (design rank + n + units).
4. What the findings do **not** imply.
5. Keywords. Structured abstract only for SR/MA.

## Headings

- Names of **topics or arguments**, never author names or “Paper 1”.
- Nested numbering when a mechanism has parts (2.1.1).
- Allowed inside a theme: biologic rationale; human evidence; limits to inference; what this literature still lacks.

## Paragraphs

- Topic sentence = claim or working model.
- Rank evidence in the same sentence (preclinical vs human; trial vs retrospective).
- Contrast where the data split; close a cluster with *Taken together, these data suggest…*.
- Present tense for established physiology; past tense for a specific published experiment.
- End the subsection by saying what that heading cannot show.

## Conclusions

Numbered scientific next steps (First… Finally…) and unmeasured endpoints. Not “more research is needed” as a slogan. Not screening counts.

## What was encoded where

Form rules above were written into:

- `.cursor/skills/review-prose/SKILL.md`
- `.cursor/skills/report-writing/SKILL.md`
- `.cursor/skills/synthesis-rationale/SKILL.md` (outline must name the review kind and use topic headings)
- `.cursor/skills/article-qa/SKILL.md` (machine check so the next sample cannot deliver a stub)
- `AGENTS.md` and `.cursor/agents/literature-review.md`

PDFs stay gitignored. This run does not produce an `article.md`. Do not import findings from these papers into any manuscript.
