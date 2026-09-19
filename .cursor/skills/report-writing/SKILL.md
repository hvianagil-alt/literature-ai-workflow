---
name: report-writing
description: "Synthesize the literature table and per-paper notes into a structured full report covering themes, agreements/disagreements, gaps, and implications. Use when the user wants a written synthesis, not just a table, and the literature table already exists."
---

# Report Writing

Turn the literature table into a structured narrative: what the field agrees on, where it disagrees, what's missing, and what that means for the user's research question. This is synthesis, not summary — the report should say things no single paper says on its own.

## When to use this skill

- After `literature-table` has produced `review/table/literature-table.md`.
- The user asks for "a report", "write this up", "synthesize", or as the final step of the full review workflow.

## Inputs

- `review/table/literature-table.md`
- `review/notes/*.md` (for pulling specific detail/quotes the table compressed away)
- The agreed research direction from intake (the report should be framed around it, not generic)

## Output

One Markdown file: `review/report/final-report.md`, structured as:

```markdown
# Literature Review: <research question / topic>

## Scope
<What was reviewed, what date range/inclusion criteria, how many papers, and a link back to the literature table>

## Themes
<2-5 major themes that emerged across papers, each with a short paragraph and citations to specific papers>

## Where the literature agrees
<Bulleted, each backed by 2+ papers>

## Where the literature disagrees
<Bulleted; name the papers on each side and, if visible, a plausible reason for the disagreement (different methods, populations, time periods) rather than just asserting "results conflict">

## Gaps
<What's under-studied, under-powered, or simply absent given the user's research question>

## Implications for [the user's research question]
<Concrete: what this means for their next step — a hypothesis, a method choice, a population they should study>

## Full literature table
<Link to review/table/literature-table.md, or inline it if the user wants a self-contained document>

## Confidence and caveats
<Be explicit about what's well-supported vs. thin — e.g. "based on only 2 papers" — so the user doesn't over-trust a synthesis of sparse evidence>
```

See [`examples/sample-report.md`](../../../examples/sample-report.md) for a fully worked example.

If the user asked for a **journal-style review article** (in-text citations, reference list, PRISMA methods), write that as `review/report/final-report.md` **and** copy it to `review/runs/<run-id>/article.md`. Use this spine:

```markdown
# <Title>

## Abstract
## 1. Introduction
## 2. Methods
### 2.1 Search and sources
### 2.2 Eligibility
### 2.3 Retrieval
### 2.4 Extraction and synthesis
### 2.5 Usage logging (token estimates)
## 3. Results
### 3.1 Study selection (PRISMA)
### 3.2 Study characteristics
### 3.3 Synthesis
## 4. Discussion
## 5. Conclusions
## References
```

Cite included papers in the text as Author Year or [n] keyed to the References list. **Every factual sentence must map to an extracted note or the PRISMA/fetch log.** If the set is heterogeneous or n is small, say so in the abstract and discussion — do not write as if a 10-paper OA slice were a complete field survey.

## Quality bar

- **Every claim in the report must be traceable to a row in the literature table or a specific note.** If you can't point to which paper(s) support a sentence, cut the sentence or mark it as your own inference clearly labeled as such (e.g. "This is our inference, not something any single paper states directly: ...").
- Do not invent citations, page numbers, or quotes. If you don't have exact page/section info, say "per [paper]" without a fabricated locator rather than making one up.
- Name disagreements explicitly rather than smoothing them into a false consensus — a good literature review makes tension visible.
- Calibrate confidence to evidence volume: 1-2 papers supporting a claim is "preliminary evidence," not "the literature shows."
- Write for the user's stated audience/purpose from intake — a report meant to justify a grant proposal reads differently from one meant to scope a thesis chapter. If that wasn't specified, ask before assuming.

## Failure modes and how to handle them

| Situation | What to do |
|---|---|
| Literature table has very few rows (e.g. 1-3 papers) | Say so plainly in "Scope" and "Confidence and caveats." Do not write a report that reads like a mature field survey when it isn't one. |
| Themes don't cleanly emerge (papers are too heterogeneous) | Report that honestly — "these papers don't share enough methodology/framing to synthesize into unified themes; here's what we can say about each" — instead of forcing artificial themes. |
| User wants the report before the table is reviewed/corrected | Warn them that unreviewed extraction errors will propagate into the synthesis, and offer to proceed anyway if they accept that tradeoff. |
| The topic legitimately needs more papers than are in `papers/` to answer well | Say so in Gaps/Confidence, and suggest using the `related-paper-exploration` skill before finalizing. |

## Handoff

After the report is written, tell the user where it is (`review/report/final-report.md`) and offer to iterate (re-scope, add papers via `related-paper-exploration`, or refine specific sections) rather than treating this as a one-shot final deliverable.
