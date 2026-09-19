#!/usr/bin/env python3
"""Write a PRISMA 2020 identification/screening counts file from run logs.

Usage:
    python3 scripts/write_prisma.py --run-dir review/runs/<id>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TEMPLATE = """# PRISMA 2020 flow — {run_id}

Counts below are taken from this run's catalog, fetch log, and screening log.
They are not inferred. Empty cells mean the step has not been recorded yet.

## Identification

| Source | n |
|---|---|
| Records from Scopus export (`identification.bib`) | {n_identified} |
| Additional records from other sources | {n_other} |
| Duplicates removed | {n_duplicates} |
| Records after duplicates removed | {n_after_dedup} |

## Screening

| Step | n |
|---|---|
| Records screened (title/metadata) | {n_screened} |
| Records excluded at title/metadata (with reason) | {n_title_excluded} |
| Reports sought for retrieval (full text) | {n_sought} |
| Reports not retrieved | {n_not_retrieved} |
| Reports assessed for eligibility (full text) | {n_fulltext_assessed} |
| Reports excluded at full text (with reason) | {n_fulltext_excluded} |

## Included

| Set | n |
|---|---|
| Studies included in the review | {n_included} |

## Exclusion reasons (title/metadata)

{title_reasons}

## Exclusion reasons (full text)

{fulltext_reasons}

## Not retrieved

{not_retrieved}

## Notes

{notes}
"""


def _reason_list(rows: list[dict], key: str = "reason") -> str:
    if not rows:
        return "_None recorded yet._"
    lines = [f"- `{r.get('citekey', '?')}` — {r.get(key, 'reason not stated')}" for r in rows]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    catalog = json.loads((run_dir / "catalog.json").read_text(encoding="utf-8"))
    fetch_path = run_dir / "fetch-log.json"
    screen_path = run_dir / "screening.json"
    fetch = json.loads(fetch_path.read_text(encoding="utf-8")) if fetch_path.exists() else []
    screen = json.loads(screen_path.read_text(encoding="utf-8")) if screen_path.exists() else {}

    n_identified = len(catalog)
    n_duplicates = int(screen.get("duplicates_removed", 0))
    title_ex = screen.get("title_excluded") or []
    full_ex = screen.get("fulltext_excluded") or []
    included = screen.get("included") or []
    not_retrieved = [r for r in fetch if not r.get("ok")]
    sought = screen.get("sought_for_retrieval")
    if sought is None:
        sought = [r["citekey"] for r in catalog]

    n_sought = len(sought)
    n_not_retrieved = len(not_retrieved)
    n_fulltext = int(screen.get("n_fulltext_assessed") or 0)
    md = TEMPLATE.format(
        run_id=run_dir.name,
        n_identified=n_identified,
        n_other=int(screen.get("additional_records", 0)),
        n_duplicates=n_duplicates,
        n_after_dedup=n_identified - n_duplicates,
        n_screened=int(screen.get("n_screened") or n_identified),
        n_title_excluded=len(title_ex),
        n_sought=n_sought,
        n_not_retrieved=n_not_retrieved,
        n_fulltext_assessed=n_fulltext,
        n_fulltext_excluded=len(full_ex),
        n_included=len(included),
        title_reasons=_reason_list(title_ex),
        fulltext_reasons=_reason_list(full_ex),
        not_retrieved=_reason_list(not_retrieved, key="error"),
        notes=screen.get("notes")
        or "Screening decisions belong in screening.json; regenerate this file after screening.",
    )
    out = run_dir / "prisma.md"
    out.write_text(md, encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
