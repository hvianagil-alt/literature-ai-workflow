---
name: paper-extraction
description: "Read a single research paper (PDF or text) and produce a structured per-paper note capturing question, methods, sample/data, findings, and limitations. Use when the user has dropped papers in papers/ and wants them read, summarized, or prepped for the literature table."
---

# Paper Extraction

Turn one paper into one structured, faithful note. This is the foundation every other skill (table-building, report-writing) builds on — if extraction is sloppy or invented, everything downstream is wrong.

## When to use this skill

- The user has papers in `papers/` (or a subfolder) and asks to "read", "summarize", "extract", or "take notes on" them.
- As a step inside the larger review workflow (see `AGENTS.md`), after the direction check has happened and scope is agreed.

Do **not** use this skill before the user has confirmed scope (research question, inclusion/exclusion, emphasis) unless they explicitly say "just skim everything first."

## Inputs

- One paper: a PDF at `papers/<name>.pdf`, or a plain-text/Markdown fallback at `papers/<name>.txt`/`.md` if the PDF isn't readable (see Failure modes).
- The agreed research direction from the intake conversation (question, field, what "good" looks like) — extraction should be read *through that lens*, not generically. Two people extracting the same paper for different research questions should end up emphasizing different things.

## Output

One Markdown file at `review/notes/<paper-id>.md` (use a short slug like `smith2023-attention` derived from author/year/keyword; keep it stable so re-running doesn't create duplicates). Use this structure:

```markdown
# <Paper title>

- **Citation (as given in the paper / filename):** <author, year, venue if visible>
- **Source file:** papers/<filename>
- **Extracted:** <date>

## Research question
<1-3 sentences: what the paper is actually trying to answer>

## Methods
<Study design, model/approach, data collection method — whatever is discipline-appropriate>

## Sample / data
<N, population, dataset size, domain — "not applicable" if purely theoretical>

## Key findings
<Bulleted, each tied to where in the paper it came from if possible, e.g. "(Section 4.2)" or "(Table 3)">

## Limitations (as stated by the authors, or evident from the methods)
<Bulleted>

## Relevance to our research question
<1-3 sentences: why this paper matters — or doesn't — for the direction agreed with the user>

## Open questions / things to verify
<Anything ambiguous, or that needs the user's domain expertise to judge>
```

## Quality bar

- **Every claim in the note must trace to the actual paper text.** If you're not sure a section says what you think, say so in "Open questions" rather than asserting it.
- Never fill in a field with a plausible-sounding guess. If sample size isn't stated, write "not stated" — don't estimate.
- Prefer the paper's own terminology over your paraphrase when precision matters (e.g. exact effect sizes, exact model names).
- Keep it skimmable: a domain expert should be able to read one note in under a minute and know whether to read the full paper.
- Flag anything that contradicts the user's stated inclusion criteria (e.g. wrong population, wrong study design) instead of silently including it.

## Failure modes and how to handle them

| Situation | What to do |
|---|---|
| PDF is a scanned image with no extractable text | Tell the user which file failed and why. Ask them to paste text, run OCR, or supply a `.txt`/`.md` fallback in `papers/`. Do not fabricate a summary from the title/filename alone. |
| PDF text extraction is garbled (broken ligatures, missing whitespace, columns interleaved) | Do your best to reconstruct meaning, but flag low-confidence sections explicitly in "Open questions" rather than presenting garbled inference as fact. |
| Paper is not in English | Say so, extract what you can, and flag translation-quality caveats. |
| Paper is out of scope per the agreed direction | Still write a short note, but mark it clearly (e.g. "Out of scope: wrong population") so it can be excluded from the table without losing the paper entirely. |
| Multiple papers share an author/year (citation collision) | Disambiguate the slug (e.g. `smith2023a`, `smith2023b`) and note the collision. |

## Handoff

Once notes exist for all in-scope papers, move to the `literature-table` skill to build the comparison table from these notes — do not re-read the PDFs from scratch for the table.
