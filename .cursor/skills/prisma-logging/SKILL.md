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
| `notes/` `table/` `synthesis-rationale.md` `article.md` | Extraction, interpretation, then the article. Token estimates stay in `usage-log.md`, not in the rationale or article. |
| `gap-retrieval/` | Targeted extra-paper search JSON, selected catalog, and fetch log for interpretation gaps. Do **not** overwrite the original run `fetch-log.json`. |

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

Phases to log: `workflow`, `discovery`, `fetching`, `screening`, `extraction`, `table`, `rationale`, `gap_retrieval`, `synthesis`.

`est_*_tokens_chars_div_4` is **characters/4**, not vendor billing. Write a human-readable copy to `usage-log.md`. **Do not put token estimates or phase meters in `article.md`.** The review article is a normal scientific paper; usage stays in this run folder as a separate analysis file.

## Handoff

After PRISMA + notes + table exist, write `synthesis-rationale.md` (`synthesis-rationale` skill), attempt targeted OA retrieval for each interpretation gap (log in section (g); extract and update the table if PDFs arrive), **then** the article (`report-writing` skill) following the updated outline, **then** `article-qa` until `check_article.py` exits 0. Do not draft `article.md` first. Point at `prisma.md` from **Methods** if useful. Ground every claim in included full texts. **Do not put PRISMA counts, fetch logs, or usage meters in Discussion or Conclusions.** Keep `usage-log.md` beside the article, not inside it. Additional gap-fill records belong in PRISMA “additional records” if they were included.

Write `protocol.md` at the start of the run:

```markdown
# Protocol — <run-id>

- **Research question:**
- **Inclusion:**
- **Exclusion:**
- **Emphasis:**
- **Article kind:** narrative journal review (default) / systematic / short lab report
- **Defaults used (if the user said just go):**
```
