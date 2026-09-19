---
name: prisma-logging
description: "Record PRISMA 2020 identification/screening counts and per-phase usage (including token *estimates*) for a literature-review run. Use whenever the user wants a reproducible methods trail."
---

# PRISMA + phase logging

Every review run that claims to be a real article needs a methods trail: where records came from, why each was dropped, and what work happened in each phase.

## Run folder

`review/runs/<run-id>/` holds the auditable copy (this folder is **not** gitignored, unlike `review/notes/*.md`):

| File | What it is |
|---|---|
| `protocol.md` | Question, inclusion/exclusion, defaults used if the user said "just go" |
| `identification.bib` | Exact database export |
| `catalog.json` / `catalog.csv` | Parsed identification set |
| `fetch-log.json` | Per-DOI PDF retrieval outcome |
| `screening.json` | Title and full-text decisions |
| `prisma.md` | PRISMA 2020 counts generated from the files above |
| `usage-log.jsonl` | Per-phase effort, including token *estimates* |
| `notes/` `table/` `article.md` | Copies of extraction/synthesis for later analysis |

## PRISMA 2020 counts (minimum)

Regenerate after screening:

```bash
python3 scripts/write_prisma.py --run-dir review/runs/<run-id>
```

Required numbers (use 0, never skip a row):

1. Records identified (database)
2. Additional records
3. Duplicates removed
4. Records screened
5. Records excluded (title), each with a one-line reason
6. Reports sought for retrieval
7. Reports not retrieved
8. Full-text assessed
9. Full-text excluded, each with a reason
10. Studies included

If a PDF cannot be opened, that is "not retrieved" or "full text unreadable" — not silent omission.

## Token / usage logging

Cursor does not give this workflow a billed token meter. Log anyway, and label estimates as estimates:

```bash
python3 scripts/phase_log.py --run-dir review/runs/<id> --phase extraction \
  --input-chars N --output-chars N --items N --notes "..."
```

Phases to log: `workflow`, `discovery`, `fetching`, `screening`, `extraction`, `table`, `synthesis`.

`est_*_tokens_chars_div_4` is **characters/4**, not vendor billing. Put that sentence in the article methods so a reader is not misled.

## Handoff

After PRISMA + notes + table exist, write the article (`report-writing` skill, article style) and point at `prisma.md` from the methods section. Ground every claim in included full texts.
