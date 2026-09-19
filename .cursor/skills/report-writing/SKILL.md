---
name: report-writing
description: "Write a PhD-quality review from the synthesis rationale, literature table, and notes. Use only after synthesis-rationale.md exists. Normal journal spine; thematic sections from the rationale; no token meters in the article."
---

# Report Writing

Write the review as a scientific argument about **all** included studies, not a catalogue of abstracts and not a token/phase log. The argument was decided in `synthesis-rationale.md`; this skill executes that outline.

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

**Default (structured lab report).** One Markdown file: `review/report/final-report.md`. Use this spine unless the user asked for a journal article:

```markdown
# Literature Review: <research question / topic>

## Scope
<What was reviewed, inclusion criteria, n papers, link to the table. State that the
 section plan follows synthesis-rationale.md.>

## <Thematic headings from rationale (e)>
<2–5 argument sections, not "paper 1 / paper 2". Each section does a job named in
 the rationale (e.g. establish the only human comparative evidence; show why delivery
 papers cannot be pooled).>

## Where the literature agrees
<Only agreements the rationale marked as supported; each backed by 2+ papers or
 explicitly labeled as a single-study observation.>

## Where the literature disagrees
<From rationale (c): name papers and whether the tension is methods, population, or
 endpoint. Prefer "incommensurable" over fake controversy when endpoints differ.>

## Gaps
<From rationale (d): what this sample cannot answer.>

## Implications for [the user's research question]
<Concrete next step; do not overclaim beyond the included full texts.>

## Full literature table
<Link to the table>

## Confidence and caveats
<Well-supported vs thin. Small n or OA-slice reviews must say so.>
```

See [`examples/sample-report.md`](../../../examples/sample-report.md) for a fictional illustration of tone, not a license to skip the rationale file.

**Journal-style review article** (when the user asked for an article, in-text citations, reference list): write `review/report/final-report.md` **and** copy it to `review/runs/<run-id>/article.md`. Use a **normal journal review spine**. Thematic subsections **must** come from rationale (e).

```markdown
# <Title>

## Abstract
## Keywords
## 1. Introduction
## 2. Methods
### 2.1 Search and sources
### 2.2 Eligibility
### 2.3 Study selection
## 3–N. Thematic sections from synthesis-rationale.md (e)
<Each section is an argument that uses every relevant included paper.
 Do not use a generic "study characteristics / results / synthesis" split.
 Do not devote one numbered section to one paper unless that paper is the
 sole evidence for that construct — and then say so.>
## Discussion
## Conclusions
## References
```

**Do not put token estimates, phase logs, script names, or workflow metering in the article or report.** Those belong only in `review/runs/<run-id>/usage-log.md`.

### Results sections (thematic §§3–N)

Each included paper must be **discussed as science**, not name-checked. For every study, state (as far as the note/PDF extract supports): design, model or population, n if extracted, intervention/comparator, primary finding with units, and what that design cannot show. Group by theme, but do **not** dump many papers into one citation list (`[6], [7], [8]…`). If a number is missing from the extract, say the extract does not state it — do not invent it.

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

## Handoff

After the report is written, tell the user where it is (`review/report/final-report.md` and, if applicable, `review/runs/<run-id>/article.md`) and that the argument follows `synthesis-rationale.md`. Offer to iterate (re-scope, add papers, or refine sections). If they change inclusion, update the rationale before rewriting.
