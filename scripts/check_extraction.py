#!/usr/bin/env python3
"""Fail if included extraction notes are still mechanical first-pass stubs.

The first-run article fails when the writer treats notes_from_text.py output as
finished. This gate exists so a later sample cannot reach the table or article
until every included note has claim-ready facts read from the PDF.

Files that start with ``_`` (synthesis rationale, exclusion logs) are not notes
and are skipped.

Usage:
    python3 scripts/check_extraction.py --notes-dir review/runs/<id>/notes
    python3 scripts/check_extraction.py --notes-dir review/notes \\
        --screening review/runs/<id>/screening.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

STUB_MARKERS = (
    "mechanical first-pass",
    "study design not fully parsed",
    "lead/abstract as extracted",
    "not stated in the extracted lead",
    "numbers not in this lead",
    "numbers not in the lead",
    "check full pdf before using an n",
)

CLAIM_HEADING = re.compile(r"^##\s+claim-ready facts\s*$", re.I | re.M)
SKIP_NOTE = re.compile(
    r"^\s*out of scope|"
    r"\*\*screening:\*\*.*(?:excluded|not retrieved|out of scope)|"
    r"full text \*\*(?:excluded|not retrieved)\*\*",
    re.I | re.M,
)
SKIP_NOTE_NAMES = {"readme.md"}


def is_paper_note(path: Path) -> bool:
    """Skip rationale, exploration, and exclusion logs that live beside notes."""
    name = path.name
    if name.startswith("_"):
        return False
    if name.lower() in SKIP_NOTE_NAMES:
        return False
    return True


def included_note_paths(notes_dir: Path, screening: dict | None) -> list[Path]:
    if screening and screening.get("included"):
        paths = []
        for rid in screening["included"]:
            p = notes_dir / f"{rid}.md"
            if p.exists() and is_paper_note(p):
                paths.append(p)
        return paths
    return sorted(p for p in notes_dir.glob("*.md") if is_paper_note(p))


def check_note(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    if SKIP_NOTE.search(text):
        return []
    problems: list[str] = []
    if not CLAIM_HEADING.search(text):
        problems.append("missing ## Claim-ready facts")
    for marker in STUB_MARKERS:
        if marker in lowered:
            problems.append(f"stub marker: {marker}")
    if CLAIM_HEADING.search(text):
        after = text[CLAIM_HEADING.search(text).end() :]  # type: ignore[union-attr]
        next_h = re.search(r"^##\s+", after, re.M)
        block = after[: next_h.start()] if next_h else after
        filled = [
            line
            for line in block.splitlines()
            if line.strip().startswith("-")
            and not re.search(r"not yet filled|TODO|TBD", line, re.I)
        ]
        if len(filled) < 5:
            problems.append("Claim-ready facts has fewer than 5 filled bullets")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes-dir", required=True)
    parser.add_argument("--screening", default="")
    args = parser.parse_args()
    notes_dir = Path(args.notes_dir)
    if not notes_dir.is_dir():
        print(f"FAIL notes dir missing: {notes_dir}", file=sys.stderr)
        return 2
    screening = None
    if args.screening:
        screening = json.loads(Path(args.screening).read_text(encoding="utf-8"))
    paths = included_note_paths(notes_dir, screening)
    if not paths:
        print("FAIL no included notes found", file=sys.stderr)
        return 2
    failed = 0
    for path in paths:
        problems = check_note(path)
        if problems:
            failed += 1
            print(f"FAIL {path.name}: " + "; ".join(problems))
        else:
            print(f"OK   {path.name}")
    print(f"\n{len(paths) - failed}/{len(paths)} included notes are claim-ready")
    if failed:
        print(
            "Extraction is not done. Read each PDF and fill Claim-ready facts "
            "before the literature table.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
