#!/usr/bin/env python3
"""Tiny, dependency-free helper for the Literature AI workflow.

This script is optional. The workflow works entirely through Cursor's chat
and the skills in .cursor/skills/ without running any code. This script just
saves a little typing for two mechanical tasks:

  1. Listing what's in papers/ (and flagging PDFs with no text fallback file
     you might need if the PDF turns out to be unreadable).
  2. Stubbing out an empty literature table with the right headers, so you
     (or the agent) can fill it in rather than retyping the header row.

Usage:
    python3 scripts/list_papers.py               # list papers/
    python3 scripts/list_papers.py --stub-table   # also write an empty table stub

No third-party dependencies. No network access. No API keys.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = REPO_ROOT / "papers"
TABLE_PATH = REPO_ROOT / "review" / "table" / "literature-table.md"

PAPER_SUFFIXES = {".pdf", ".txt", ".md"}

TABLE_STUB = """# Literature Table

Fill in one row per in-scope paper. See `.cursor/skills/literature-table/SKILL.md`
for column definitions and quality bar, and `examples/literature-table.md` for a
worked example.

| Paper | Research question | Methods | Sample / data | Key findings | Limitations | Relevance |
|---|---|---|---|---|---|---|
| | | | | | | |

## Papers excluded from this table

- (list any extracted-but-out-of-scope papers here, with a one-line reason each)
"""


def find_papers(papers_dir: Path) -> list[Path]:
    if not papers_dir.exists():
        return []
    return sorted(
        p
        for p in papers_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in PAPER_SUFFIXES and "README" not in p.name
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stub-table",
        action="store_true",
        help="write an empty literature table stub to review/table/literature-table.md "
        "if it doesn't already exist",
    )
    args = parser.parse_args()

    papers = find_papers(PAPERS_DIR)

    if not papers:
        print(f"No papers found under {PAPERS_DIR.relative_to(REPO_ROOT)}/.")
        print("Drop PDFs (or .txt/.md fallbacks) there, then re-run this script.")
    else:
        print(f"Found {len(papers)} paper file(s) under {PAPERS_DIR.relative_to(REPO_ROOT)}/:\n")
        pdfs_without_fallback = []
        for p in papers:
            rel = p.relative_to(REPO_ROOT)
            print(f"  - {rel}")
            if p.suffix.lower() == ".pdf":
                has_fallback = (p.with_suffix(".txt").exists()) or (p.with_suffix(".md").exists())
                if not has_fallback:
                    pdfs_without_fallback.append(rel)

        if pdfs_without_fallback:
            print(
                "\nNote: the PDFs above have no .txt/.md fallback file. That's normal — "
                "you only need a fallback if the agent tells you a specific PDF can't be read."
            )

    if args.stub_table:
        if TABLE_PATH.exists():
            print(f"\n{TABLE_PATH.relative_to(REPO_ROOT)} already exists — not overwriting.")
        else:
            TABLE_PATH.parent.mkdir(parents=True, exist_ok=True)
            TABLE_PATH.write_text(TABLE_STUB, encoding="utf-8")
            print(f"\nWrote empty table stub to {TABLE_PATH.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
