---
name: related-paper-exploration
description: "Given seed papers already in papers/ and the user's stated research direction, suggest related papers, search queries, or things to look up next. Never invents fake citations. Use when the user wants to expand coverage before extracting/synthesizing, or when the report surfaces a gap."
---

# Related-Paper Exploration

Help the user find more of the literature — without ever presenting a fabricated citation as real. This skill produces *leads* (search queries, named authors/venues/concepts worth checking, and any real, verifiable references you already have grounded knowledge of), not a padded bibliography.

## When to use this skill

- Optional step, explicitly opt-in: only run this when the user asks for it (e.g. "what else should I read?", "are there important papers I'm missing?") or when `report-writing` surfaces a gap and the user wants to fill it before finalizing.
- Never run this automatically as part of a default pipeline — expanding scope is a direction decision, and direction decisions go through the user first (see the intake/direction-check step in `AGENTS.md`).

## Inputs

- The papers already extracted (`review/notes/*.md`) and/or the literature table.
- The user's research question and what they've said "good" coverage looks like (from intake).

## Output

A short Markdown note (either appended to the conversation or saved as `review/notes/_exploration-<date>.md` if the user wants a record) with up to three sections, each clearly separated by confidence level:

```markdown
## Search queries to try
<Concrete strings for Google Scholar / Semantic Scholar / PubMed / arXiv, tailored to the gap identified>

## Authors, labs, or venues worth checking
<Named because they recur in the seed papers' references or are well-known in the subfield — say why each is suggested>

## Specific papers I can verify
<Only papers you have solid, specific knowledge of — title, authors, approximate year, and *why* it's relevant. If you are not confident a citation is exactly correct, do not list it here.>
```

If you cannot confidently name a specific paper, do not include one just to fill the section — an empty section with an honest note ("I don't have verifiable specific titles for this gap; try the search queries above") is strictly better than a plausible-sounding fake citation.

## Quality bar — this is the highest-stakes skill in this repo

- **Never fabricate a citation.** Do not invent author names, titles, years, DOIs, or venues that sound plausible. This is the single most damaging failure mode for a literature review tool: a confidently wrong citation can end up in someone's actual paper.
- For every specific paper you name, be explicit about your confidence: "I'm confident this exists and is roughly on-topic" vs. "I recall something like this but you should verify the exact title/year before citing it."
- Prefer **search queries and named subfields/authors** (low risk of being wrong in a damaging way) over **specific paper titles** (high risk) when you're not certain.
- Explicitly tell the user: "Verify every suggested paper actually exists and says what I think before citing it or adding it to your table." Put this reminder in the output itself, not just in conversation.
- Ground suggestions in the seed papers' own citations/context when possible (e.g. "Paper X's related-work section mentions a body of work on Y — worth searching for that") rather than free-associating from the topic alone.

## Failure modes and how to handle them

| Situation | What to do |
|---|---|
| User asks "just give me 10 papers to read" | Push back gently: explain you can't guarantee the existence/accuracy of a long specific list, and offer search queries plus any papers you're genuinely confident about instead. |
| You're not sure if a paper you're thinking of is real or a conflation of two papers | Don't list it. Describe the idea/topic and suggest a search query instead. |
| The gap is in a subfield you have little grounded knowledge of | Say so plainly rather than generating generic-sounding suggestions to fill space. |
| User wants to actually fetch/download suggested papers | This repo doesn't do that automatically (no network calls, no browsing baked into the workflow) — tell the user to search/download manually and drop new PDFs in `papers/`, then re-run extraction. |

## Handoff

Once the user has downloaded any new papers into `papers/`, route back to `paper-extraction` for the new files, then rebuild the table and report so the new evidence is actually incorporated (don't just bolt exploration notes onto an old report).
