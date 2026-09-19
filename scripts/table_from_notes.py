#!/usr/bin/env python3
"""Rewrite literature-table.md from claim-ready notes (not from PDF leads).

``write_table.py`` emits a DRAFT from titles/abstracts. This script is the
finished worksheet: every cell comes from ``## Claim-ready facts`` and the
matching note sections. Fail if an included note is still a stub.

Usage:
    python3 scripts/table_from_notes.py --run-dir review/runs/<id>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Reuse the extraction gate so a DRAFT table cannot be written from stubs.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_extraction  # noqa: E402

STUB_MARKERS = check_extraction.STUB_MARKERS


def section(text: str, heading: str) -> str:
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.I | re.M)
    if not m:
        return ""
    rest = text[m.end() :]
    nxt = re.search(r"^##\s+", rest, re.M)
    return (rest[: nxt.start()] if nxt else rest).strip()


def first_bullet(block: str) -> str:
    for line in block.splitlines():
        s = line.strip()
        if s.startswith("- "):
            return s[2:].strip()
    cleaned = re.sub(r"\s+", " ", block).strip()
    return cleaned[:280] if cleaned else "not stated"


def fact(text: str, key: str) -> str:
    m = re.search(rf"-\s+\*\*{re.escape(key)}:\*\*\s*(.+)", text, re.I)
    if not m:
        return "not reported"
    return re.sub(r"\s+", " ", m.group(1)).strip()


def paper_label(row: dict | None, note: str, stem: str) -> str:
    if row:
        authors = (row.get("author") or "").split(" and ")[0]
        last = authors.split(",")[0].strip() if authors else stem
        year = row.get("year") or ""
        journal = (row.get("journal") or "").strip() or "journal not stated"
        return f"{last} {year}, *{journal}*"
    title_line = note.splitlines()[0].lstrip("# ").strip()
    cite = ""
    for line in note.splitlines():
        if line.startswith("- **Citation"):
            cite = line.split(":**", 1)[-1].strip()
            break
    year_m = re.search(r"\b(20\d{2})\b", cite or title_line)
    year = year_m.group(1) if year_m else ""
    last = stem.split("20")[0].rstrip("_") if stem else "Unknown"
    return f"{last} {year}".strip()


def terse(s: str, n: int = 220) -> str:
    s = re.sub(r"\s+", " ", s).replace("|", "/").strip()
    if len(s) > n:
        return s[: n - 1].rstrip() + "…"
    return s or "not stated"


def rows_for_run(run_dir: Path) -> list[dict]:
    notes_dir = run_dir / "notes"
    screen = json.loads((run_dir / "screening.json").read_text(encoding="utf-8"))
    index = {
        r.get("record_id"): r
        for r in json.loads((run_dir / "extraction-index.json").read_text(encoding="utf-8"))
    }
    stems = list(screen.get("included") or [])
    extra = []
    for path in sorted(notes_dir.glob("*.md")):
        if not check_extraction.is_paper_note(path):
            continue
        if path.stem in stems:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"gap-fill", text, re.I):
            extra.append(path.stem)
    stems.extend(extra)
    rows = []
    for stem in stems:
        path = notes_dir / f"{stem}.md"
        if not path.exists():
            raise SystemExit(f"missing note: {path}")
        problems = check_extraction.check_note(path)
        if problems:
            raise SystemExit(f"note not claim-ready: {path.name}: {'; '.join(problems)}")
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for marker in STUB_MARKERS:
            if marker in lowered:
                raise SystemExit(f"stub marker still in {path.name}: {marker}")
        meta = index.get(stem)
        findings = first_bullet(section(text, "Key findings"))
        lim = first_bullet(section(text, "Limitations (as stated by the authors, or evident from the methods)"))
        if not lim:
            lim = first_bullet(section(text, "Limitations"))
        rows.append(
            {
                "paper": paper_label(meta, text, stem),
                "question": terse(section(text, "Research question"), 200),
                "methods": terse(
                    fact(text, "Design")
                    + "; "
                    + (section(text, "Methods").split("\n", 1)[0][:160]),
                    200,
                ),
                "sample": terse(
                    f"n={fact(text, 'n')}; {fact(text, 'Population / model')}",
                    160,
                ),
                "findings": terse(fact(text, "Primary result") or findings, 240),
                "limitations": terse(lim, 180),
                "relevance": terse(section(text, "Relevance to our research question"), 160),
                "gapfill": bool(re.search(r"gap-fill", text, re.I)),
            }
        )
    return rows


def protocol_question(run_dir: Path) -> str:
    proto = run_dir / "protocol.md"
    if not proto.exists():
        return "See protocol.md (do not invent a field-specific question here)."
    text = proto.read_text(encoding="utf-8")
    m = re.search(
        r"##\s+Review question\s*\n+(.+?)(?:\n##|\Z)",
        text,
        re.S | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    for line in text.splitlines():
        mm = re.match(r"\*\*Research question:\*\*\s*(.+)", line)
        if mm:
            return mm.group(1).strip()
    return "See protocol.md (do not invent a field-specific question here)."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    screen = json.loads((run_dir / "screening.json").read_text(encoding="utf-8"))
    rows = rows_for_run(run_dir)
    n_export = sum(1 for r in rows if not r["gapfill"])
    n_gap = sum(1 for r in rows if r["gapfill"])
    lines = [
        f"# Literature Table — run {run_dir.name}",
        "",
        "**Source:** rewritten from `## Claim-ready facts` in the per-paper notes. "
        "Not a `write_table.py` DRAFT. Not a paste of PDF leads.",
        "",
        f"**Research question:** {protocol_question(run_dir)}",
        "",
        f"**Scope:** {n_export} included full texts from the export after title screen, "
        f"public-OA retrieval, and full-text eligibility"
        + (f", plus **{n_gap} gap-fill** OA paper(s)." if n_gap else ".")
        + " Sorted in screening order, with gap-fill rows last.",
        "",
        "| Paper | Research question | Methods | Sample / data | Key findings | Limitations | Relevance |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            "| {paper} | {question} | {methods} | {sample} | {findings} | {limitations} | {relevance} |".format(
                **{k: r[k] for k in ("paper", "question", "methods", "sample", "findings", "limitations", "relevance")}
            )
        )
    lines += [
        "",
        "## How to read this table",
        "",
        "Each cell is compressed from the matching note. Designs and endpoints are not commensurate; "
        "do not pool across rows. Gap-fill rows were retrieved after the export to interpret a stated gap.",
        "",
        "## Papers excluded from this table",
        "",
        f"- Title/metadata excludes: **{len(screen.get('title_excluded') or [])}** (see `prisma.md`).",
        f"- Not retrieved: **{len(screen.get('not_retrieved') or [])}**.",
        f"- Full-text excludes: **{len(screen.get('fulltext_excluded') or [])}**.",
        "",
    ]
    out = run_dir / "table" / "literature-table.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
