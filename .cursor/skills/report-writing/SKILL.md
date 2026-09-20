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

**Default is a journal-style review article** unless the user asked for a short lab report or a table-only note. Write `review/report/final-report.md` **and** copy it to `review/runs/<run-id>/article.md` when this is a run. **Match the spine to the review kind** (`review-prose`). Default kind is a narrative review with brief methods. Use full IMRaD Results only for a systematic review or meta-analysis. Thematic subsections **must** come from rationale (e) and must be **topic or argument titles**, never author names. The article **must contain numbered Markdown results tables** (Table 1, …) and in-text callouts — see In-article results tables below.

See [`examples/sample-article.md`](../../../examples/sample-article.md) for fictional journal prose (claim-first sentences). The lab-report example in [`examples/sample-report.md`](../../../examples/sample-report.md) is only for a short structured note.

```markdown
# <Title: phenomenon, then colon + kind or angle — see review-prose Title>

## Abstract
<Topic map, not a results dump. No citations, no named papers. See review-prose.>
## Keywords
<At least four topic phrases, semicolon-separated.>
## Key Summary Points (optional)
<Claim plus evidence grade, not slogans.>
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
 sole evidence for that construct — and then say so.
 Include numbered Markdown results tables (Table 1, …) and mention them from the prose.>
## Discussion
## Conclusions
<Scientific next measurements in running sentences, not a First/Second/Third list and not “more research is needed.”>
## References
<Vancouver: [1] is the first paper cited in the body, [2] the next new paper, …>
<One reference per paragraph: blank line between [n] entries. No stacked list.>
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

Each included paper must appear inside **scientific sentences**, not as a stack of “Author et al. did X” abstracts. For every study, the prose must still carry design, model or population, n if reported, intervention/comparator, primary finding with units, and what that design cannot show — but the **claim comes first** and the citation supports it (see `review-prose`, Sentence construction). When a paragraph teaches a **mechanism** (how the method kills, why a matrix protects, why a plant does not use the method), join cause to effect in the same sentence or the next one (`because`, `after`, `therefore`, `so that`); do not emit a stack of short unjoined clauses (see `review-prose`, Mechanism articulation). Group by theme. Rank evidence in the sentence (trial vs observational vs animal). After a cluster of studies, add a synthesis line (*Taken together…*). Close the subsection with what that heading cannot show. Do **not** dump many papers into one citation list (`[6], [7], [8]…`). If a number is missing, write that it was **not reported**; do not write “the extracted lead omits n,” and do not invent the number.

When the paragraph reports comparable numbers, **point at the in-article table**: “Primary endpoints are summarised in Table 1 [1–4].” Then keep writing in sentences. The table does not replace the claim-first prose; the prose does not replace the table.

### In-article results tables

`article.md` is a Markdown manuscript. Put **real Markdown tables** in it (pipe tables), numbered **Table 1**, **Table 2**, …, with a bold caption. Name the paper, n, design, endpoint, and result in the cells. Mention the table from the Results (and, if useful, Methods or Discussion). See `review-prose`, Tables in the article.

This is not the extraction worksheet in `literature-table.md`. Curate: one table per comparable construct. Drop columns that do not help a reader compare those rows. Every cell must already exist in a note.

```markdown
**Table 1.** Primary endpoint results in the included human studies.

| Study | Design | Population (n) | Comparison | Primary endpoint | Result |
|---|---|---|---|---|---|
| Name Year [1] | RCT | adults (n=…) | A vs B | … | … (units; p/CI) |
```

In the text: “Adjunct weekly semaglutide increased time in range by 4.8 percentage points versus placebo (Table 1) [1].”

### Discussion (journal article) — write like a published paper

The Discussion interprets **findings**, not the review pipeline. A reader of a specialty journal in *this topic* should recognize the genre.

**Must include** (map each bullet onto *this* sample’s constructs, not onto a previous run’s disease area):

- What the primary outcome evidence jointly shows, and at what level of design (RCT vs observational vs protocol vs preclinical, as the included papers actually are).
- How supporting papers (mechanism, formulation, pharmacokinetics, qualitative, or methods) relate — or fail to relate — to those results: species or population, route or setting, model, and endpoint.
- Extra-primary or mechanistic work interpreted as the biology or technology it is, not as a second outcomes trial.
- Why papers that look related cannot be pooled (incommensurable endpoints), named as scientific disagreement or non-comparability.
- Translational implications calibrated to design (animal PK is not human approval; a one-week laboratory test is not a semester-long habit; a protocol is not an outcome).
- Evidence limitations a scientist would name: small n, missing human data, protocols without results, confounding, single-study constructs.
- Pointers back to in-article tables when the interpretation rests on a row (“as in Table 1”).

**Must not include in Discussion, Conclusions, Introduction, or Abstract:**

- Identification/screening theatre: database-export sizes, “open full texts from 2021–2026”, “full texts can be cited”, “not retrieved”, “PDFs we could open”, HTTP codes, Unpaywall, OpenAlex, Scopus, script names, token estimates, “this is not an N-paper review”, paths to `prisma.md`.
- Instructions to the reader about the workflow. PRISMA counts, year windows of the export, and “public vs paywall” belong in Methods (briefly) and in `prisma.md`, not in the scientific argument.

Open scientific gaps (a missing human PK study; a protocol without outcomes; a mechanism still debated) **are** in scope for Discussion — as unanswered questions in the field, not as download failures.

Cite included papers in the text as numbered Vancouver citations `[n]` keyed to the References list. **Number papers in the order they first appear in the body** (not Abstract, not Keywords): the first cited paper is `[1]`, the next new paper is `[2]`, and so on. Re-citations keep that number. After drafting, run `python3 scripts/renumber_citations.py --article review/runs/<run-id>/article.md` so the list matches the prose, then `check_article.py` (it fails if the sequence is wrong). **Every factual sentence must map to an extracted note, the table, or (for Methods counts only) the PRISMA/fetch log.** If the set is heterogeneous or n is small, say so as an evidence limitation — do not write as if a small slice were a complete field survey, and do not explain that limitation as a software or export problem.

**Do not wait for the user to complain about structure.** After the first complete draft, reread the Introduction as an adjacent-field expert. If later sections would be opaque, rewrite the Introduction and the heading spine **once** before `check_article.py`. That rewrite is the default path, not a second assignment.

## Quality bar

- **PhD-level argument, not a catalogue.** Topic sentences make claims about the set; papers are evidence for those claims. A reader should not be able to describe the article as “seven consecutive abstracts.”
- **Follow the rationale.** If writing tempts you to add a theme the rationale marked as forced, don’t. Update the rationale first only when the notes/table actually support the change.
- **Every included study appears in the argument.** Do not drop a paper because it is awkward (e.g. a patient-reported instrument beside a network meta-analysis).
- **Every claim is traceable** to a table row or note. If you can't point to which paper(s) support a sentence, cut it or label it as your inference (e.g. "This is our inference, not something any single paper states directly: ...").
- **Do not overclaim.** One network meta-analysis is not class-wide clinical efficacy. Animal pharmacokinetics are not human bioavailability. A mechanistic probe is not an outcomes trial. A botanical receptor study is not a licensed drug.
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

If it fails, rewrite and run it again. Also grep the banned-flourish list in `review-prose`. Prefer copulas (`is`, `are`, `was`) and named numbers over promotional verbs. If the first sentence of the Introduction is “This review discusses…”, rewrite it as the phenomenon in present tense. If headings are author names, rename them as topics or arguments. If the heading spine is `## Results` plus fragment `###` notes, rewrite into numbered thematic sections before the user sees the file. If the Introduction does not teach the field, expand it. If the body has no Markdown results table or no “Table 1” (or Table N) sentence, add both. If a term repeats, write `Full term (ABBR)` once and then the abbreviation, in a sentence that still teaches the thing. Keep the Abstract readable: write terms out unless the Abstract itself reuses the short form (at most four abbreviations). If body text (everything before `## References`) is well under ~6,000 words and the user did not ask for a short note, add teaching and per-paper methods/results — not padding.

## Handoff

After the report is written **and `check_article.py` exits 0**, run the `double-check` skill and write `double-check.md`. Only then tell the user where the **Markdown** article is (`review/report/final-report.md` and, if applicable, `review/runs/<run-id>/article.md`) and that the argument follows `synthesis-rationale.md`. **In that same message, ask if they also want Word and PDF.** Offer to iterate (re-scope, add papers, refine sections). If they change inclusion, update the rationale before rewriting.
