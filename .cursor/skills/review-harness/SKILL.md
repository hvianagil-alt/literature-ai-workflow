---
name: review-harness
description: "Deploy the literature-review loop: first conversation, extract-until-green, rationale, field memory, article, machine QA retries, independent critic, then check_harness.py. Use for every full review so a new user in any field gets a first-try journal draft."
---

# Review harness

This is how the workflow is **run**, not a second copy of the science rules. Read `AGENTS.md` for order. This file is the loop, the roles, and the “do not tell them it is done” gate.

A new user in endocrinology, food science, nanomedicine, or an unnamed field should get the **same machine**: conversation → evidence → interpretation → form check against memory → article → scripts → critic. They should not have to know any of those words.

## Roles (one chat can play all of them)

| Role | Cursor agent file | Must not |
|---|---|---|
| Orchestrator | `.cursor/agents/literature-review.md` | Skip gates; talk in pipeline jargon to the user |
| Extractor | `.cursor/agents/literature-extractor.md` | Write `article.md` |
| Field-form reader | `.cursor/agents/field-form-reader.md` | Import findings from memory cards |
| Writer | (orchestrator + `report-writing`) | Draft before rationale + memory |
| Critic | `.cursor/agents/literature-critic.md` | Write the first draft; invent numbers |

If Cursor can launch those agents as subagents, do that for extractor (batches), field-form reader (before draft), and critic (after scripts). If not, **still play the roles in order** and write the same files.

## Loops (do not stop on the first failure)

### Extract loop (max 3 cycles)

1. Extract in-scope PDFs (`paper-extraction`).
2. `python3 scripts/check_extraction.py --notes-dir review/runs/<id>/notes --screening review/runs/<id>/screening.json`
3. If fail: fill Claim-ready facts from the PDF; delete stub phrases; repeat.
4. After 3 cycles, list remaining failures as unreadable or out of scope. Never silently drop them.

Then `python3 scripts/table_from_notes.py --run-dir review/runs/<id>`.

### Rationale loop (once, not optional)

Write `synthesis-rationale.md` with **(i)** and **(a)–(e)**. Attempt OA gap retrieval. Update notes/table. If nothing extra is OA, log that. Then go on.

### Form loop (once, before draft)

1. Open `review/memory/index.md`. Pick the card for this field and the row in `applications.md` for thesis/grant/paper/reading.
2. Run `field-structure-benchmark` on included reviews (and extra OA reviews of the same kind if useful).
3. Record **Memory consulted:** `<card>.md` in `structure-benchmark.md`.
4. Update rationale (e) if the verdict says so.

### Article QA loop (max 3 cycles)

1. Draft `article.md` (`review-prose` + `scientific-synthesis` + `report-writing`).
2. `python3 scripts/renumber_citations.py --article review/runs/<id>/article.md` if needed.
3. `python3 scripts/check_article.py --article … --table …`
4. If fail: rewrite; do not argue with the script.
5. After 3 failures, **do not deliver**. Tell the user the gate is still red and what failed.

### Critic loop (1 rewrite)

1. After scripts are green, run the **critic** (separate agent if possible). It only reads. It writes `critic-log.md` and fills the critic lines in `double-check.md`.
2. Verdict **FAIL** → orchestrator rewrites once, re-runs `check_article.py`, critic again.
3. Still FAIL → do not tell the user the article is done.
4. **PASS** → `python3 scripts/check_harness.py --run-dir review/runs/<id> --full`

## Done means

```bash
python3 scripts/check_harness.py --run-dir review/runs/<id> --full
```

exits 0. That script checks the files exist, the critic passed, memory was consulted, and the two quality scripts are green. **The article file existing is not done.**

Then hand Markdown and ask Word/PDF. Do not start a graphical abstract.

## After a first-try success in a new field

Add a short form card under `review/memory/` and a row in `index.md`. Headings only.

## Talk to the user

Plain language. “I will read the papers, then check the notes, then write a draft, then check it again.” Not “I will spawn the critic subagent.”
---
