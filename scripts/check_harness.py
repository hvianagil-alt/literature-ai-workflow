#!/usr/bin/env python3
"""Fail a review run that is missing a harness gate.

The article is not done when article.md exists. Exit 0 only when the
run directory has protocol, claim-ready notes, table, rationale, article,
double-check, and (with --full) structure benchmark, field memory, and
a passing critic.

Usage:
    python3 scripts/check_harness.py --run-dir review/runs/<id>
    python3 scripts/check_harness.py --run-dir review/runs/<id> --full
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def evaluate(run_dir: Path, full: bool = False, run_scripts: bool = True) -> list[str]:
    problems: list[str] = []
    run_dir = run_dir.resolve()
    if not run_dir.is_dir():
        return [f"run dir missing: {run_dir}"]

    protocol = run_dir / "protocol.md"
    notes = run_dir / "notes"
    table = run_dir / "table" / "literature-table.md"
    rationale = run_dir / "synthesis-rationale.md"
    article = run_dir / "article.md"
    double = run_dir / "double-check.md"
    screening = run_dir / "screening.json"

    for path, label in (
        (protocol, "protocol.md"),
        (table, "table/literature-table.md"),
        (rationale, "synthesis-rationale.md"),
        (article, "article.md"),
        (double, "double-check.md"),
    ):
        if not path.is_file():
            problems.append(f"missing {label}")

    if not notes.is_dir() or not any(notes.glob("*.md")):
        problems.append("missing notes/*.md")

    rat = _read(rationale)
    if rationale.is_file():
        if "(e)" not in rat and "## (e)" not in rat:
            problems.append("synthesis-rationale.md has no (e) outline")
        if "Intellectual model" not in rat and "(i)" not in rat:
            problems.append("synthesis-rationale.md has no intellectual model (i)")

    tab = _read(table)
    if table.is_file():
        low = tab.lower()
        if "draft" in low.split("\n", 1)[0] or "mechanical first-pass" in low:
            problems.append("literature table still looks like a DRAFT")

    dub = _read(double)
    if double.is_file():
        if "Adjacent-field reader test" not in dub and "adjacent-field" not in dub.lower():
            problems.append("double-check.md missing adjacent-field reader test")

    if full:
        bench = run_dir / "structure-benchmark.md"
        if not bench.is_file():
            problems.append("missing structure-benchmark.md")
        else:
            btxt = _read(bench)
            if "Memory consulted" not in btxt and "memory/" not in btxt.lower():
                problems.append("structure-benchmark.md does not record field memory consulted")
        critic = run_dir / "critic-log.md"
        critic_txt = _read(critic) + "\n" + dub
        if "Critic verdict: PASS" not in critic_txt and "Critic verdict:PASS" not in critic_txt:
            problems.append("critic did not PASS (need critic-log.md or double-check.md line: Critic verdict: PASS)")
        if "graphical abstract" in _read(article).lower() and "lovable" in _read(article).lower():
            problems.append("article.md still points at a graphical abstract")

    if run_scripts and not problems:
        py = sys.executable
        if notes.is_dir() and screening.is_file():
            ext = subprocess.run(
                [
                    py,
                    str(ROOT / "scripts" / "check_extraction.py"),
                    "--notes-dir",
                    str(notes),
                    "--screening",
                    str(screening),
                ],
                capture_output=True,
                text=True,
            )
            if ext.returncode != 0:
                problems.append("check_extraction.py failed")
        if article.is_file() and table.is_file():
            art = subprocess.run(
                [
                    py,
                    str(ROOT / "scripts" / "check_article.py"),
                    "--article",
                    str(article),
                    "--table",
                    str(table),
                ],
                capture_output=True,
                text=True,
            )
            if art.returncode != 0:
                problems.append("check_article.py failed")

    return problems


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run-dir", required=True, type=Path)
    p.add_argument("--full", action="store_true", help="require structure benchmark, memory, critic PASS")
    p.add_argument("--no-scripts", action="store_true", help="skip check_extraction/check_article")
    args = p.parse_args(argv)
    problems = evaluate(args.run_dir, full=args.full, run_scripts=not args.no_scripts)
    if problems:
        print("Harness is not done. Missing or failed gates:", file=sys.stderr)
        for item in problems:
            print(f"- {item}", file=sys.stderr)
        print("Do not tell the user the article is done.", file=sys.stderr)
        return 1
    print(f"OK harness {args.run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
