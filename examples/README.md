# Worked examples

These show the **destination** of the workflow before you've run it on real papers.

- [`literature-table.md`](literature-table.md) — a sample comparison table.
- [`synthesis-rationale.md`](synthesis-rationale.md) — a sample interpretation file (including a gap-retrieval log) written **before** the article.
- [`sample-article.md`](sample-article.md) — the default destination: a fictional **journal** review (claim-first sentences, phenomenon-first Introduction).
- [`sample-report.md`](sample-report.md) — a short lab-report spine, only if the user asked for that instead of an article.
- [`protocol.md`](protocol.md) — question, inclusion, and “just go” defaults written down at the start of a run.

## Important: these papers are fictional

Every "paper" referenced in these examples — titles, authors, years, findings, everything — is **made up for illustration only**. None of it refers to real research. This is intentional and important: this repo's whole point is to never present invented citations as real (see the `related-paper-exploration` skill's quality bar), so the example papers are deliberately silly/obvious placeholders (e.g. "Fictional Al Researcher, 2024") rather than plausible-sounding real-ish names that someone might mistake for an actual citation.

When you run the real workflow on your own papers in `papers/`, your outputs will land in `review/table/literature-table.md`, then `review/runs/<id>/synthesis-rationale.md` (or `review/notes/_synthesis-rationale.md`), then — after targeted extra retrieval is attempted — `review/runs/<id>/article.md` (and `review/report/final-report.md`). Table, then interpretation and gap-fill, then the article, then `scripts/check_article.py`. The rationale + extra-retrieval step is mandatory. The quality-gate scripts are mandatory.
