# Literature AI

Drop your papers in a folder, talk with an AI agent about your research direction, and get back per-paper notes, a comparable literature table, and a structured report — without needing to know anything about AI.

This repo is built for **[Cursor](https://cursor.com)**. It's not a web app or a service you sign up for — it's a folder structure plus a set of instructions ("skills") that tell Cursor's AI exactly how to do a literature review, so you don't have to write a custom prompt every time.

## You do not need to be an AI expert

If you've never used Cursor or an AI coding tool before, here's the entire mental model you need:

- **Cursor** is an editor (like Word, but for code and text files) that has an AI chat built in.
- This repo has a folder called `papers/` where you put PDFs, and a file called `AGENTS.md` that tells the AI how to review them.
- You open this repo in Cursor, type a plain-English request in the chat, and the AI follows the instructions in this repo automatically.
- No API key, no account, no billing setup is required for the core workflow — it runs on whatever AI model is already part of your Cursor account.

## Quickstart

1. **Get this repo onto your machine.**

   ```bash
   git clone <this-repo-url>
   cd literature-ai
   ```

2. **Drop your PDFs into `papers/`.** Subfolders are fine. See [`papers/README.md`](papers/README.md) if you're wondering whether this will accidentally publish your papers (short answer: no, they're excluded from git by default).

3. **Open the folder in Cursor.** (File → Open Folder, or `cursor .` from the terminal if you have the CLI installed.)

4. **Open the chat and type:**

   > Review my papers

   The AI will look at what's in `papers/`, ask you what your research question is and what you're trying to get out of the review, and then walk through the workflow below — checking in with you before doing the deep work, never just silently processing everything.

That's it. You don't need to open or read `AGENTS.md` or the `.cursor/skills/` files yourself — they're instructions for the AI, not for you. (Though you're welcome to — see [How it works](#how-it-works) below.)

## What you get

For each review you run, in a `review/` folder that appears once you start:

- **Per-paper notes** (`review/notes/`) — one Markdown file per paper: research question, methods, sample/data, findings, limitations, and why it matters to *your* question.
- **A literature table** (`review/table/literature-table.md`) — one row per paper, same columns, so you can actually compare them side by side.
- **A synthesized report** (`review/report/final-report.md`) — themes, where the literature agrees and disagrees, gaps, and what it means for your research direction.

Want to see what these look like before running anything? Check [`examples/`](examples/README.md) — a fully worked example built from clearly fictional placeholder papers (no real citations, so nothing there could be mistaken for actual research).

## The workflow

This is deliberately a conversation, not a batch job:

1. **Intake** — you drop PDFs and say what you're trying to answer.
2. **Direction check (the AI always does this before going deep)** — it confirms scope, what to include/exclude, and what to emphasize. It will not silently extract 20 papers before checking with you first.
3. **Optional: explore related papers** — if you want broader coverage, the AI can suggest search queries, authors, or venues to check. It will not invent fake-sounding citations to pad out a list — see the [related-paper-exploration skill](.cursor/skills/related-paper-exploration/SKILL.md) for exactly how it handles uncertainty.
4. **Extract** — one structured note per in-scope paper.
5. **Table** — all notes compared side by side.
6. **Report** — a full write-up grounded in the table, with themes, tensions, gaps, and implications.

Full detail lives in [`AGENTS.md`](AGENTS.md), which is the file the AI actually reads to run this.

## Do I need an API key?

**No, not for the core workflow.** Reading PDFs, extracting notes, building the table, and writing the report all happen inside Cursor's chat using whatever model your Cursor account already has — no separate signup.

The only place an external tool could optionally help is if a PDF is a scanned image that can't be read as text (rare, but it happens — old papers, bad scans). In that case:

- The AI will tell you exactly which file failed and why.
- You can paste the text yourself into a `.txt` file next to the PDF, or
- Use any OCR tool you already have (there's no required or recommended one — this repo doesn't bundle one), and drop the resulting text next to the PDF.

Either way, nothing in this workflow requires you to sign up for or pay for an external API.

## Repo structure

```
.
├── AGENTS.md                    # workflow instructions the AI follows
├── .cursor/
│   ├── agents/                  # the "review my papers" agent persona
│   └── skills/                  # one SKILL.md per step (extraction, table, report, exploration)
├── papers/                      # <- put your PDFs here
├── review/                      # <- outputs land here when you run the workflow
│   ├── notes/
│   ├── table/
│   ├── report/
│   └── runs/                    # methods trail (PRISMA, fetch log, token estimates)
├── examples/                    # worked example table + report (fictional papers)
└── scripts/
    ├── list_papers.py           # optional: list papers/, stub an empty table
    ├── import_bib.py            # optional: parse a Scopus/BibTeX export
    ├── fetch_oa_pdfs.py         # optional: download public OA PDFs
    ├── write_prisma.py          # optional: PRISMA 2020 counts from run logs
    └── phase_log.py             # optional: per-phase usage / token estimates
```

## Optional helper script

If you like, there's a tiny, dependency-free Python script that lists what's in `papers/` and can stub out an empty table file:

```bash
python3 scripts/list_papers.py
python3 scripts/list_papers.py --stub-table
```

This is entirely optional — the AI workflow doesn't require you to run any code. It's just a shortcut if you'd rather glance at a terminal than ask the chat "what's in my papers folder?"

If you start from a Scopus export instead of PDFs:

```bash
python3 scripts/import_bib.py path/to/scopus.bib --run-dir review/runs/my-review
python3 scripts/fetch_oa_pdfs.py --run-dir review/runs/my-review --out-dir papers/my-review --email you@example.com
python3 scripts/write_prisma.py --run-dir review/runs/my-review
```

`fetch_oa_pdfs.py` only keeps files that are actually public PDFs. It will not log into publishers or use pirate sites. Failures are written to `fetch-log.json`.

## How it works (for the curious)

Cursor supports **skills**: small instruction files that tell the AI exactly how to do a specific job, including what "good" looks like and how to handle failure cases. This repo has seven:

| Skill | What it does |
|---|---|
| [`paper-extraction`](.cursor/skills/paper-extraction/SKILL.md) | Reads one paper, produces one structured note |
| [`literature-table`](.cursor/skills/literature-table/SKILL.md) | Turns notes into a comparable table |
| [`report-writing`](.cursor/skills/report-writing/SKILL.md) | Synthesizes the table into a full report |
| [`related-paper-exploration`](.cursor/skills/related-paper-exploration/SKILL.md) | Suggests related papers/searches, with an explicit no-fake-citations rule |
| [`bib-import`](.cursor/skills/bib-import/SKILL.md) | Parses a Scopus/BibTeX export into a screening catalog |
| [`oa-fetch`](.cursor/skills/oa-fetch/SKILL.md) | Retrieves public open-access PDFs for those DOIs |
| [`prisma-logging`](.cursor/skills/prisma-logging/SKILL.md) | PRISMA 2020 counts and per-phase usage / token estimates |

[`AGENTS.md`](AGENTS.md) ties these together into the step-by-step workflow, and [`.cursor/agents/literature-review.md`](.cursor/agents/literature-review.md) is the short persona that makes "review my papers" trigger this workflow instead of generic chat.

## Contributing

Issues and pull requests welcome — especially if you hit a workflow edge case (a PDF type that trips things up, a discipline whose literature table needs different columns, etc.).

## License

[MIT](LICENSE).
