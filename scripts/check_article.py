#!/usr/bin/env python3
"""Fail a journal-review draft that would not survive a first-pass referee.

Run this after writing article.md. Exit 0 only if the draft is deliverable.
Do not tell the user the article is done while this script fails.

Usage:
    python3 scripts/check_article.py --article review/runs/<id>/article.md \\
        --table review/runs/<id>/table/literature-table.md
    python3 scripts/check_article.py --article path.md --short
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROCESS = [
    r"\bunpaywall\b",
    r"\boa export\b",
    r"\btoken estimate\b",
    r"\busage-log\b",
    r"\bextracted lead\b",
    r"\bin this set\b",
    r"pdfs we could",
    r"this introduction is that map",
    r"the paper's job",
    r"extracts used here",
    r"mechanical first-pass",
    r"\bhttp_calls\b",
    r"est_input_tokens",
]

FLOURISH = [
    r"stands as a testament",
    r"evolving landscape",
    r"rich tapestry",
    r"\bdelve\b",
    r"indelible mark",
    r"setting the stage",
]

INTRO_BAD_OPENERS = (
    "this review discusses",
    "this review aims",
    "this paper reviews",
    "in recent years",
    "in today's world",
    "it is well known that",
)

REQUIRED_HEADINGS = ("abstract", "introduction", "discussion", "conclusions", "references")


def body_before_references(text: str) -> str:
    parts = re.split(r"^##\s+References\s*$", text, maxsplit=1, flags=re.I | re.M)
    return parts[0]


def section_after(text: str, heading: str) -> str:
    m = re.search(rf"^##\s+(?:\d+\.\s+)?{heading}\s*$", text, re.I | re.M)
    if not m:
        return ""
    rest = text[m.end() :]
    nxt = re.search(r"^##\s+", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def first_sentence(section: str) -> str:
    cleaned = re.sub(r"^#+\s+.*$", "", section, flags=re.M).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        return ""
    m = re.search(r"(.+?[.!?])\s", cleaned + " ")
    return (m.group(1) if m else cleaned[:240]).strip()


def heading_lines(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^#{1,4}\s+(.+)$", text, re.M)]


def et_al_openers(text: str) -> int:
    n = 0
    for para in re.split(r"\n\s*\n", text):
        line = para.strip().split("\n", 1)[0].strip()
        if re.match(r"^[A-Z][A-Za-z\-]+ et al\.", line):
            n += 1
    return n


def papers_from_table(table_md: str) -> list[tuple[str, str]]:
    papers: list[tuple[str, str]] = []
    for line in table_md.splitlines():
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s:\-|]+\|$", line.replace(" ", "")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0].lower() in {"paper", "-----"}:
            continue
        if "research question" in cells[0].lower():
            continue
        raw = re.sub(r"\*+", "", cells[0])
        m = re.match(r"(?:Fictional\s+)?(.+?)[,\s]+(\d{4})\b", raw)
        if not m:
            continue
        name = m.group(1).strip().rstrip(",")
        year = m.group(2)
        surname = name.split()[-1]
        papers.append((surname, year))
    return papers


def check(text: str, table: str | None, short: bool) -> list[str]:
    problems: list[str] = []
    lowered = text.lower()
    body = body_before_references(text)
    for h in REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+(?:\d+\.\s+)?{h}\s*$", text, re.I | re.M):
            problems.append(f"missing heading: {h}")
    words = body.split()
    if not short and len(words) < 6000:
        problems.append(f"body word count {len(words)} < 6000 (use --short only if the user asked for a short note)")
    for pat in PROCESS + FLOURISH:
        if re.search(pat, body, re.I):
            problems.append(f"banned phrase: {pat}")
    if re.search(r"^Additionally,", body, re.M):
        problems.append("sentence opener Additionally,")
    intro = section_after(text, "Introduction")
    opener = first_sentence(intro).lower()
    for bad in INTRO_BAD_OPENERS:
        if opener.startswith(bad):
            problems.append(f"Introduction opens with '{bad}'")
    for h in heading_lines(text):
        if re.search(r"\bet al\.", h, re.I) or re.match(r"paper\s+\d+", h, re.I):
            problems.append(f"heading names a paper: {h}")
    results = body
    for stop in ("Discussion", "Conclusions"):
        chunk = section_after(text, stop)
        if chunk:
            results = results.replace(chunk, "")
    intro_full = section_after(text, "Introduction")
    methods = section_after(text, "Methods")
    results = results.replace(intro_full, "").replace(methods, "")
    n_open = et_al_openers(results)
    if n_open >= 4:
        problems.append(f"{n_open} results paragraphs open with 'Author et al.' (max 3)")
    if table:
        missing = []
        for surname, year in papers_from_table(table):
            if surname not in text or year not in text:
                missing.append(f"{surname} {year}")
        if missing:
            problems.append("included papers not named in article: " + ", ".join(missing[:12]))
            if len(missing) > 12:
                problems.append(f"...and {len(missing) - 12} more")
    disc = section_after(text, "Discussion") + "\n" + section_after(text, "Conclusions")
    for pat in (r"\bprisma\.md\b", r"\bfetch-log\b", r"\bnot retrieved\b"):
        if re.search(pat, disc, re.I):
            problems.append(f"Discussion/Conclusions contains process talk: {pat}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article", required=True)
    parser.add_argument("--table", default="")
    parser.add_argument(
        "--short",
        action="store_true",
        help="skip the 6,000-word floor (only if the user asked for a short note)",
    )
    args = parser.parse_args()
    path = Path(args.article)
    if not path.is_file():
        print(f"FAIL article missing: {path}", file=sys.stderr)
        return 2
    table = Path(args.table).read_text(encoding="utf-8") if args.table else None
    problems = check(path.read_text(encoding="utf-8"), table, args.short)
    if problems:
        print("FAIL article is not deliverable:")
        for p in problems:
            print(f"  - {p}")
        print(
            "Rewrite before telling the user it is done. See review-prose and report-writing.",
            file=sys.stderr,
        )
        return 1
    print(f"OK {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
