---
name: related-paper-exploration
description: "Find related papers without inventing citations. Opt-in browse, or mandatory gap-driven OA retrieval after the rationale. Intake search when the folder is empty is the find-papers skill."
---

# Related-Paper Exploration

Help find more of the literature — without ever presenting a fabricated citation as real. This skill produces *leads* (search queries, named authors/venues/concepts, and API-verified records) and, in gap-driven mode, a fetch list for public OA PDFs. It is not a padded bibliography.

## Two modes in this skill (browse / gap-fill)

Intake search-and-fetch (empty folder, or expand a seed set) is the `find-papers` skill, not this file. This file stays: (1) opt-in browse of queries without download, and (2) mandatory gap-driven OA retrieval after the synthesis rationale.

### Mode A — opt-in browse (before extraction)

- Run only when the user asks for broader coverage (e.g. "what else should I read?") **before** notes/table exist.
- Expanding the *initial* scope is a direction decision; that still goes through the user (see step 2 in `AGENTS.md`).
- Output is leads, not automatic downloads, unless the user then asks to fetch.

### Mode B — gap-driven retrieval (mandatory after the table, before the article)

- This mode **is** part of the default pipeline. After `literature-table`, the `synthesis-rationale` skill lists interpretation gaps. For **each** gap you **must** attempt targeted extra retrieval before writing `article.md`.
- You still **never invent citations**. You still fetch **only public OA**. Failure to retrieve is an allowed, explicit outcome — not a reason to skip the attempt, and not a reason to fill the gap from memory.

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

## Mode B extras (gap-driven, after rationale)

For each interpretation gap in `synthesis-rationale.md`:

1. Ground the query in the gap (and in citations that already appear in the included PDFs, when those titles are visible in the notes).
2. Search OpenAlex (API hits only):

   ```bash
   python3 scripts/search_oa_related.py \
     --query "<gap-specific query>" \
     --mailto <user-email> \
     --out review/runs/<run-id>/gap-retrieval/search-<gap-id>.json
   ```

3. Select a small number of hits that actually address the gap. Write why each was chosen or skipped. Do not treat the JSON file as a reference list.
4. Copy selected rows into `review/runs/<run-id>/gap-retrieval/catalog.json` and fetch with `oa-fetch` into a **separate** PDF folder (`papers/<run-id>-gapfill/`) so the original `fetch-log.json` is not overwritten.
5. Log **sought / found / not retrieved** in the rationale. Extract found PDFs; update the table; do not cite not-retrieved records.

If OpenAlex errors, Unpaywall has no PDF, or the publisher returns HTML/403: record `not retrieved` and leave the gap open. **No Sci-Hub, no publisher login, no paywall bypass.**

## Quality bar — this is the highest-stakes skill in this repo

- **Never fabricate a citation.** Do not invent author names, titles, years, DOIs, or venues that sound plausible. This is the single most damaging failure mode for a literature review tool: a confidently wrong citation can end up in someone's actual paper.
- For every specific paper you name, be explicit about your confidence: "I'm confident this exists and is roughly on-topic" vs. "I recall something like this but you should verify the exact title/year before citing it."
- Prefer **search queries and named subfields/authors** (low risk of being wrong in a damaging way) over **specific paper titles** (high risk) when you're not certain.
- Explicitly tell the user: "Verify every suggested paper actually exists and says what I think before citing it or adding it to your table." Put this reminder in the output itself, not just in conversation.
- Ground suggestions in the seed papers' own citations/context when possible (e.g. "Paper X's related-work section mentions a body of work on Y — worth searching for that") rather than free-associating from the topic alone.

## Failure modes and how to handle them

| Situation | What to do |
|---|---|
| User asks "just give me 10 papers to read" | Do **not** invent a list from memory. If they want real files, run `find-papers` (OpenAlex API hits + OA fetch). If they only want ideas, give search queries plus any papers you're genuinely confident about. |
| You're not sure if a paper you're thinking of is real or a conflation of two papers | Don't list it. Describe the idea/topic and suggest a search query instead. |
| The gap is in a subfield you have little grounded knowledge of | Say so plainly rather than generating generic-sounding suggestions to fill space. |
| User wants to actually fetch/download suggested papers (Mode A) | Use `find-papers` / `oa-fetch`. Do not bypass paywalls. If they prefer to download manually, they drop PDFs in `papers/` and you re-run extraction. |
| Mode B search or fetch fails | Log not retrieved in `synthesis-rationale.md`. Do not invent a stand-in citation. Proceed to the article with the gap explicit. |

## Handoff

- **Mode A:** once new PDFs are in `papers/`, route to `paper-extraction`, then rebuild the table. Do not jump to the article.
- **Mode B:** extract new OA full texts, rebuild the table, finish the retrieval log in `synthesis-rationale.md`, **then** `report-writing`. Don't bolt exploration notes onto an old article.
