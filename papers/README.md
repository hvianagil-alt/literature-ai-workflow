# `papers/` — drop your PDFs here

This folder is the **intake tray**. Put the PDFs you want reviewed directly in here (subfolders are fine too, e.g. `papers/2024-survey/`).

You don't need to rename, tag, or organize anything before starting — the agent will ask you clarifying questions about scope once it sees what's here.

If this folder is empty, you can still start. Tell the agent the topic; it will search **free open-access** papers (OpenAlex) and download public PDFs into a subfolder. If you drop a handful of seed PDFs, it will search for related OA papers on the same topic. It will not use pirate sites or paid logins. It may ask once for a contact email (Unpaywall/OpenAlex polite pool).

## Keep PDFs local (default)

By default, `.gitignore` at the repo root excludes `*.pdf` inside `papers/`. That means:

- You can drop as many PDFs as you like without bloating the git repo or accidentally publishing copyrighted paper content.
- `git status` will not show your PDFs, and `git add .` will not stage them.
- This is almost always what you want for a public repo.

## Option A: keep it local-only (recommended for most people)

Just drop PDFs in here and use the workflow. Nothing extra to configure. Your PDFs never leave your machine unless you explicitly commit them (see Option C).

## Option B: use Git LFS if you want PDFs in version control

If you *do* want to track papers in git (e.g. a private fork for a lab), use [Git LFS](https://git-lfs.com/) instead of committing raw PDFs:

```bash
git lfs install
git lfs track "papers/**/*.pdf"
git add .gitattributes
```

Then PDFs added under `papers/` will be tracked via LFS pointers instead of bloating the repo history.

## Option C: commit one sample paper on purpose

If you want a worked example checked into the repo (e.g. for a demo or CI), put it under `papers/sample/` — that path is explicitly allowed through the `.gitignore` (see the `!papers/sample/*.pdf` rule). Only do this for papers you have the right to redistribute (e.g. your own preprint, or something under a permissive license like arXiv's).

## If a PDF can't be read

Some PDFs are scanned images, DRM-protected, or otherwise not text-extractable. If the agent can't read one:

- It will tell you which file failed and why (rather than silently skipping it).
- You can paste the abstract/key sections as plain text into a `.txt` or `.md` file next to the PDF (e.g. `papers/smith2023.pdf` → `papers/smith2023.txt`), and the agent will use that instead.
- Or you can convert the PDF (e.g. with `pdftotext`, OCR, or the publisher's HTML version) and drop the resulting text file in here.

## What happens next

Once your PDFs are in place — or once you have named a topic with an empty folder — open this repo in Cursor and say something like:

> "Review my papers"

See the root [`README.md`](../README.md) and [`AGENTS.md`](../AGENTS.md) for the full workflow.
