---
name: report-writing
description: "Write a PhD-quality review from the synthesis rationale, literature table, and notes. Use only after synthesis-rationale.md exists. Match the journal spine to the review kind; thematic argument headings; no token meters in the article."
---

# Report Writing

**Read `review-prose` first** (`.cursor/skills/review-prose/SKILL.md`). That file defines the genre (secondary review article, not a primary paper), **how to match the spine to the review kind**, the teaching Introduction (phenomenon first, aim last), abstract order, heading and paragraph craft, manuscript length (~6,000 body words / ~20 Word pages unless the user asked for a short note), and the ban on chatbot diction. This skill executes the outline from `synthesis-rationale.md` **in that voice**. Do not import findings from reviews that were read only to learn form.

Write the review as a scientific argument about **all** included studies, not a catalogue of abstracts and not a token/phase log. The argument was decided in `synthesis-rationale.md`.

## When to use this skill

- After `synthesis-rationale` has produced `review/runs/<run-id>/synthesis-rationale.md`, `review/report/synthesis-rationale.md`, or `review/notes/_synthesis-rationale.md`.
- The user asks for "a report", "write this up", "synthesize", "write the article," or as the report step of the full review workflow.

If the rationale file is missing, **stop and write it first** (see the `synthesis-rationale` skill), even if the user asked only for the article. Then write the report and say that you did the rationale step first.

## Inputs (read in this order)

1. **`synthesis-rationale.md` — required.** Section (e) is the outline. Sections (a)–(d) constrain what you may claim. Do not invent a different structure while writing.
2. `review/table/literature-table.md` (or the run copy)
3. `review/notes/*.md` (detail the table compressed away)
4. The agreed research direction from intake / `protocol.md`
5. PRISMA/screening files for methods counts only

## Output

## Output

**Default is a journal-style review article** unless the user asked for a short lab report or a table-only note. Write `review/report/final-report.md` **and** copy it to `review/runs/<run-id>/article.md` when this is a run. **Match the spine to the review kind** (`review-prose`). Default kind is a narrative review with brief methods. Use full IMRaD Results only for a systematic review or meta-analysis. Thematic subsections **must** come from rationale (e) and must be **topic or argument titles**, never author names.

See [`examples/sample-article.md`](../../../examples/sample-article.md) for fictional journal prose (claim-first sentences). The lab-report example in [`examples/sample-report.md`](../../../examples/sample-report.md) is only for a short structured note.

```markdown
# <Title>

## Abstract
<Problem → tension → calibrated findings → what they do not imply. See review-prose.>
## Keywords
## 1. Introduction
<Present-tense phenomenon first. Teach physiology/technology later sections assume.
 Last paragraph = aim or central argument. “This review” belongs there, not in sentence one.>
## 2. Methods
### 2.1 Search and sources
### 2.2 Eligibility
### 2.3 Study selection
<Keep this short for a narrative review. Expand to PRISMA-complete methods only for SR/MA.>
## 3–N. Thematic sections from synthesis-rationale.md (e)
<Each section is an argument that uses every relevant included paper.
 Nested subheadings (3.1.1) when a mechanism has parts.
 Allowed subsection names include limits to inference and what the literature still lacks.
 Do not use a generic "study characteristics / results / synthesis" split.
 Do not devote one numbered section to one paper unless that paper is the
 sole evidence for that construct — and then say so.>
## Discussion
## Conclusions
<Numbered scientific directions (First… Finally…), not “more research is needed.”>
## References
```

**Short lab report only if the user asked for one:**

```markdown
# Literature Review: <research question / topic>

## Scope
## <Thematic headings from rationale (e)>
## Where the literature agrees
## Where the literature disagrees
## Gaps
## Implications for [the user's research question]
## Full literature table
## Confidence and caveats
```

**Do not put token estimates, phase logs, script names, or workflow metering in the article or report.** Those belong only in `review/runs/<run-id>/usage-log.md`.

### Results sections (thematic §§3–N)

Each included paper must appear inside **scientific sentences**, not as a stack of “Author et al. did X” abstracts. For every study, the prose must still carry design, model or population, n if reported, intervention/comparator, primary finding with units, and what that design cannot show — but the **claim comes first** and the citation supports it (see `review-prose`, Sentence construction). Group by theme. Rank evidence in the sentence (trial vs observational vs animal). After a cluster of studies, add a synthesis line (*Taken together…*). Close the subsection with what that heading cannot show. Do **not** dump many papers into one citation list (`[6], [7], [8]…`). If a number is missing, write that it was **not reported**; do not write “the extracted lead omits n,” and do not invent the number.

### Discussion (journal article) — write like a published paper

The Discussion interprets **findings**, not the review pipeline. A reader of *Diabetes*, *Nature Medicine*, or *Drug Delivery and Translational Research* should recognize the genre.

**Must include:**

- What the human outcome evidence jointly shows (glycaemia, safety, utilisation) and at what level of design (RCT vs observational vs protocol).
- How formulation/PK papers relate (or fail to relate) to those clinical results: species, route, payload, and endpoint.
- Mechanistic extra-glycaemic work (liver, bone, muscle, heart, retina, brain) interpreted as biology, not as a second outcomes trial.
- Why papers that look related cannot be pooled (incommensurable endpoints), named as scientific disagreement or non-comparability.
- Translational implications calibrated to design (e.g. rat lung bioavailability is not human inhaled GLP-1 RA approval).
- Evidence limitations that a scientist would name: small n, missing human PK, protocols without results, observational confounding, single-study constructs.

**Must not include in Discussion, Conclusions, or Abstract:**

- Identification/screening theatre: “459-record export”, “44 full texts can be cited”, “139 not retrieved”, “PDFs we could open”, HTTP codes, Unpaywall, script names, token estimates, “this is not a 15-paper review”, paths to `prisma.md`.
- Instructions to the reader about the workflow. PRISMA counts belong in Methods (briefly) and in `prisma.md`, not in the scientific argument.

Open scientific gaps (no human inhaled liraglutide PK; no second T1D AID RCT in the set; hepatic GLP-1 action still debated) **are** in scope for Discussion — as unanswered biology/clinical questions, not as download failures.

Cite included papers in the text as Author Year or [n] keyed to the References list. **Every factual sentence must map to an extracted note, the table, or (for Methods counts only) the PRISMA/fetch log.** If the set is heterogeneous or n is small, say so as an evidence limitation — do not write as if a small slice were a complete field survey, and do not explain that limitation as a software or export problem.

## Quality bar

- **PhD-level argument, not a catalogue.** Topic sentences make claims about the set; papers are evidence for those claims. A reader should not be able to describe the article as “seven consecutive abstracts.”
- **Follow the rationale.** If writing tempts you to add a theme the rationale marked as forced, don’t. Update the rationale first only when the notes/table actually support the change.
- **Every included study appears in the argument.** Do not drop a paper because it is awkward (e.g. a PRO instrument beside an NMA).
- **Every claim is traceable** to a table row or note. If you can't point to which paper(s) support a sentence, cut it or label it as your inference (e.g. "This is our inference, not something any single paper states directly: ...").
- **Do not overclaim.** One NMA is not “clinical efficacy of the class across diabetes.” Animal PK is not human bioavailability. A mechanistic probe is not an outcomes trial. Botanical GLP-1R agonism is not a licensed GLP-1 RA.
- Do not invent citations, page numbers, or quotes. If you don't have an exact locator, cite the paper without fabricating one.
- Name real disagreements (methods / population / endpoint). Do not smooth them into false consensus, and do not invent conflict where studies never measured the same thing.
- Calibrate confidence to evidence volume: 1–2 papers is preliminary, not “the literature shows.”
- Write for the user's stated audience/purpose from intake. If that wasn't specified, keep the journal-review default above rather than guessing a grant vs thesis voice.

## Failure modes and how to handle them

| Situation | What to do |
|---|---|
| `synthesis-rationale.md` does not exist | Write it first (`synthesis-rationale` skill). Do not draft the article. |
| Literature table has very few rows (e.g. 1–3 papers) | Say so in Scope/Abstract/Discussion. Do not write a mature field survey. |
| Themes don't cleanly emerge | Follow rationale (b): organize by construct and say the set is incommensurable. |
| User wants the report before the table or rationale is reviewed | Warn that extraction errors will propagate; still write the rationale before the article. |
| The topic needs more papers than are in `papers/` | That is rationale (f). Extra retrieval must already have been attempted (rationale g) before this skill runs. Remaining open gaps stay in the article. Do not pad with uncited memory. |
| Extra papers were retrieved for a gap | They are in-scope evidence. Update the table first; then every such paper appears in the argument. Methods must say they were targeted OA additions, not part of the original database export. |

## Prose check (mandatory before calling the article done)

Run the `article-qa` skill. Do not deliver while this fails:

```bash
python3 scripts/check_article.py \
  --article review/runs/<run-id>/article.md \
  --table review/runs/<run-id>/table/literature-table.md
```

If it fails, rewrite and run it again. Also grep the banned-flourish list in `review-prose`. Prefer copulas (`is`, `are`, `was`) and named numbers over promotional verbs. If the first sentence of the Introduction is “This review discusses…”, rewrite it as the phenomenon in present tense. If headings are author names, rename them as topics or arguments. If the Introduction does not teach the field, expand it. If body text (everything before `## References`) is well under ~6,000 words and the user did not ask for a short note, add teaching and per-paper methods/results — not padding.

## Handoff

After the report is written **and `check_article.py` exits 0**, tell the user where it is (`review/report/final-report.md` and, if applicable, `review/runs/<run-id>/article.md`) and that the argument follows `synthesis-rationale.md`. Offer to iterate (re-scope, add papers, or refine sections). If they change inclusion, update the rationale before rewriting.
