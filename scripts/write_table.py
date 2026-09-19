#!/usr/bin/env python3
"""Draft a literature table from the extraction index (included papers only)."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def cells(row: dict) -> dict[str, str]:
    lead = re.sub(r"\s+", " ", row.get("lead") or "").strip()
    if len(lead) > 420:
        lead = lead[:417].rstrip() + "…"
    design = ", ".join(row.get("design") or []) or "not classified"
    n = row.get("n_in_lead")
    sample = f"n mentioned in lead: {n}" if n else "not stated in extracted lead"
    authors = (row.get("author") or "").split(" and ")[0]
    last = authors.split(",")[0].strip() if authors else row.get("citekey")
    paper = f"{last} {row.get('year')}, *{(row.get('journal') or '').strip() or 'journal not stated'}*"
    return {
        "paper": paper,
        "question": (row.get("title") or "")[:220],
        "methods": design,
        "sample": sample,
        "findings": lead or "not stated",
        "limitations": "First-pass from extracted PDF text; numbers not in the lead are not stated.",
        "relevance": ", ".join(row.get("topics") or []) or (row.get("fulltext_reason") or "included"),
        "record_id": row.get("record_id"),
        "doi": row.get("doi") or "",
    }


def protocol_question(run_dir: Path) -> str:
    proto = run_dir / "protocol.md"
    if proto.exists():
        for line in proto.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\*\*Research question:\*\*\s*(.+)", line)
            if m:
                return m.group(1).strip()
    return "See protocol.md (do not invent a field-specific question here)."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    index = json.loads((run_dir / "extraction-index.json").read_text(encoding="utf-8"))
    screen = json.loads((run_dir / "screening.json").read_text(encoding="utf-8"))
    index = sorted(index, key=lambda r: ((r.get("year") or ""), r.get("citekey") or ""))
    lines = [
        f"# Literature Table — DRAFT — run {run_dir.name}",
        "",
        "> Mechanical stub from titles/abstracts. **Not the final table.** Rewrite from verified notes after `check_extraction.py` passes. Do not write the article from this draft.",
        "",
        f"**Research question:** {protocol_question(run_dir)}",
        "",
        f"**Scope:** {len(index)} included full texts after title screen, public-OA retrieval, and full-text eligibility. Sorted by year then citekey.",
        "",
        "| Paper | Research question | Methods | Sample / data | Key findings | Limitations | Relevance |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in index:
        c = cells(row)
        def esc(s: str) -> str:
            return s.replace("|", "/").replace("\n", " ")
        lines.append(
            "| {paper} | {question} | {methods} | {sample} | {findings} | {limitations} | {relevance} |".format(
                **{k: esc(str(c[k])) for k in ("paper", "question", "methods", "sample", "findings", "limitations", "relevance")}
            )
        )
    lines += [
        "",
        "## How to read this table",
        "",
        "Rows are a **mechanical draft**. Replace every cell from the per-paper note's Claim-ready facts before synthesis. Sorted by year, then citekey.",
        "",
        "## Papers excluded from this table",
        "",
        f"- Title/metadata excludes: **{len(screen.get('title_excluded') or [])}** (see `prisma.md` for one-line reasons).",
        f"- Not retrieved: **{len(screen.get('not_retrieved') or [])}**.",
        f"- Full-text excludes: **{len(screen.get('fulltext_excluded') or [])}**.",
        "",
    ]
    for r in screen.get("not_retrieved") or []:
        lines.append(f"- `{r.get('citekey')}` — not retrieved: {r.get('reason')}")
    for r in screen.get("fulltext_excluded") or []:
        lines.append(f"- `{r.get('citekey')}` — full-text exclude: {r.get('reason')}")
    out_dir = run_dir / "table"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "literature-table.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(index)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
