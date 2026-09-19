# Agent instructions: Literature AI

This file tells any AI agent (Cursor, or another AGENTS.md-compatible tool) how to run the literature review workflow in this repo. If a user opens this repo and says something like **"review my papers"**, **"help me with my literature review"**, or **"read the PDFs in papers/"**, follow this file — don't default to generic chat.

## Who this is for

Researchers who are not AI experts. Assume the user knows their field deeply but may not know what a "skill" or "agent" is. Explain what you're about to do in plain language before doing it. Don't use ML/agent jargon in your responses to them unless they use it first.

## The workflow, in order

This is an opinionated, sequential workflow. Don't skip steps, and don't silently process everything the moment you see PDFs — direction check (step 2) is mandatory before deep work.

### 1. Intake

Look at what's in `papers/` (recursively, ignoring non-paper files). Tell the user what you found (count, filenames/titles if visible). Then ask them directly:

- What's your research question, or what field/topic is this for?
- What does "good" look like for this review — e.g. a table for a lit-review section of a paper, background reading before starting a project, a sanity check on 3 specific papers?

If `papers/` is empty, say so and point them to `papers/README.md` instead of proceeding.

If the user starts from a **Scopus/PubMed `.bib` export** rather than PDFs, do not skip intake: count the records, then use the `bib-import` skill into `review/runs/<run-id>/`. PDF retrieval is a separate, explicit step (`oa-fetch`) — only public open-access files, with failures logged. Document identification/screening with the `prisma-logging` skill.

### 2. Direction check (mandatory, do not skip)

Before extracting anything in depth, confirm with the user:

- **Scope**: which papers (if any) are out of scope, and why (wrong population, wrong method, too old, off-topic)?
- **Inclusion/exclusion criteria**: is there a study design, date range, population, or venue that should be included/excluded?
- **Emphasis**: should extraction lean toward methods (e.g. for a methods-focused thesis chapter), findings (e.g. for a grant background section), or something else?

Summarize back what you understood in 2-4 sentences and get explicit confirmation ("does that sound right?") before moving on. If the user says "just go", proceed with sensible defaults but state the defaults you're using.

**Do not proceed past this step without user input.** This is the one hard gate in the workflow — everything else can reasonably be run with sensible defaults, but scope cannot be guessed.

### 3. Optional: explore related papers

If the user wants broader coverage, or if you notice the seed papers cite a body of work not represented in `papers/`, offer (don't force) the exploration step: see the `related-paper-exploration` skill. This step **never invents fake citations** — see that skill's quality bar. Only run it if the user opts in.

### 4. Extract

For each in-scope paper, use the `paper-extraction` skill to produce a note in `review/notes/`. Report progress as you go (e.g. "3 of 7 done, 1 unreadable — see below"). Surface unreadable-PDF failures immediately rather than silently skipping them.

### 5. Build the literature table

Use the `literature-table` skill to turn the notes into `review/table/literature-table.md`. Tell the user it's ready and suggest they skim it for obvious extraction errors before you synthesize — catching a misread finding here is much cheaper than catching it in the final report.

### 6. Synthesize the report

Use the `report-writing` skill to produce `review/report/final-report.md`, grounded in the table (not re-derived from scratch). Every claim should be traceable to the table/notes.

### 7. Iterate

Literature reviews are rarely one-shot. After delivering the report, ask if they want to: add more papers (loop back to step 3/4), adjust scope (loop back to step 2), or refine specific sections of the report.

## Hard rules (apply throughout)

1. **Never fabricate a citation, quote, or finding.** If you're not sure a paper says something, say you're not sure. This applies most acutely in the `related-paper-exploration` skill, but holds everywhere.
2. **Never silently skip a paper.** If a PDF can't be read or a paper is deemed out of scope, say so explicitly and why.
3. **Talk to the user before going deep.** Step 2 is not optional. Don't extract 20 papers before confirming direction.
4. **Ground synthesis in the table.** The report should not introduce claims that aren't backed by the literature table or notes.
5. **No required external services.** This workflow runs entirely on what Cursor can already read (PDF/text in the repo) and the model's own reasoning. If a user wants to use an external PDF/OCR tool or LLM API for something this workflow can't do locally (e.g. OCR a scanned PDF), treat it as optional and documented — never a blocker (see the root `README.md`, "Do I need an API key?").
6. **Keep outputs where they belong.** Per-paper notes → `review/notes/`. Table → `review/table/literature-table.md`. Report → `review/report/final-report.md`. Don't scatter outputs elsewhere.

## Skills reference

| Step | Skill | Location |
|---|---|---|
| Reading/extracting a paper | `paper-extraction` | `.cursor/skills/paper-extraction/SKILL.md` |
| Building the comparison table | `literature-table` | `.cursor/skills/literature-table/SKILL.md` |
| Writing the synthesis report | `report-writing` | `.cursor/skills/report-writing/SKILL.md` |
| Suggesting related papers (optional) | `related-paper-exploration` | `.cursor/skills/related-paper-exploration/SKILL.md` |
| Importing a Scopus/BibTeX export | `bib-import` | `.cursor/skills/bib-import/SKILL.md` |
| Fetching public OA PDFs | `oa-fetch` | `.cursor/skills/oa-fetch/SKILL.md` |
| PRISMA counts + phase/token log | `prisma-logging` | `.cursor/skills/prisma-logging/SKILL.md` |

## Worked examples

Before running this for real, you (the agent) and the user can both look at [`examples/`](examples/README.md) for a fully worked, clearly fictional literature table and report — this shows the destination of the workflow without needing real papers first.
