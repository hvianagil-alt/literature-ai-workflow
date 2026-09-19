---
name: literature-table
description: "Build a comparable literature table (question, methods, sample, findings, limitations, relevance) from per-paper notes. Use after paper-extraction. Handoff is table → synthesis-rationale → report; do not skip to the article."
---

# Literature Table

Turn N independent per-paper notes into one comparable table. The table is the evidence base the final report must be grounded in, so it needs to be consistent (same columns, same units, same level of detail) even though the source papers are heterogeneous.

## When to use this skill

- After `paper-extraction` has produced notes in `review/notes/` for every in-scope paper.
- The user asks to "build the table", "compare these papers", or as the automatic next step in the full review workflow.

## Inputs

- All files in `review/notes/*.md` that are in scope (i.e. not marked "Out of scope" — see paper-extraction skill), for the current review.
- The agreed research direction (used to decide which columns deserve extra detail, and what counts as "relevant").

## Output

One Markdown file: `review/table/literature-table.md`. Use a real Markdown table with one row per paper and these columns (add/drop columns only if the user asks — consistency matters more than completeness):

```markdown
| Paper | Research question | Methods | Sample / data | Key findings | Limitations | Relevance |
|---|---|---|---|---|---|---|
| Smith 2023 | ... | ... | ... | ... | ... | ... |
```

Follow the table with a short **"How to read this table"** paragraph (1-2 sentences) and a **"Papers excluded from this table"** section listing anything extracted but out of scope, with a one-line reason each — exclusions should be visible, not silently dropped.

See [`examples/literature-table.md`](../../../examples/literature-table.md) for a fully worked example.

## Quality bar

- **Every cell must be traceable to a specific per-paper note.** Don't summarize across papers inside a cell — that belongs in the report, not the table.
- Keep cell content terse (aim for 1-3 short sentences or a tight bullet list) — the table's value is fast comparison, not depth. Depth lives in the notes.
- Use consistent units and terminology across rows (e.g. always "N=..." for sample size, always report effect sizes the same way) so rows are actually comparable, even when the source papers phrase things differently.
- If a paper doesn't report something (e.g. no stated limitations), write "not stated" rather than leaving blank or inventing one.
- Sort rows in a sensible, stated order (e.g. chronological, or by theme if the user has expressed one) and say which ordering you used.

## Failure modes and how to handle them

| Situation | What to do |
|---|---|
| Notes are missing for some papers in `papers/` | Don't silently exclude them — tell the user which papers have no note yet and why (not yet extracted vs. failed extraction). |
| Papers use incompatible methodologies (e.g. mixing RCTs and qualitative interviews) | Keep them in the same table but make the Methods column specific enough that the mismatch is visible — don't force false comparability. |
| A note has "Open questions" flagged by paper-extraction | Carry a light footnote/marker (e.g. `*`) into the table cell so uncertainty isn't lost when compressing the note into a cell. |
| User wants a column this skill doesn't define | Add it, but keep the change consistent across all rows and note the customization at the top of the table file. |

## Handoff

Once the table exists and the user has reviewed/corrected it (tables are good places for a human domain expert to catch errors — encourage a quick look before synthesis), move to the `synthesis-rationale` skill. **Do not skip to `report-writing`.** The sequence is table → synthesis-rationale (including targeted extra-paper retrieval for interpretation gaps) → updated table if new OA full texts were included → report. The article must not be drafted until `review/runs/<run-id>/synthesis-rationale.md` (or `review/notes/_synthesis-rationale.md`) exists **and** section (g) of that file records the extra-retrieval attempt (or an explicit “no extra retrieval indicated”).
