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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    index = json.loads((run_dir / "extraction-index.json").read_text(encoding="utf-8"))
    screen = json.loads((run_dir / "screening.json").read_text(encoding="utf-8"))
    index = sorted(index, key=lambda r: ((r.get("year") or ""), r.get("citekey") or ""))
    lines = [
        f"# Literature Table — run {run_dir.name}",
        "",
        "**Research question:** In this Scopus open-access export (2024–2026), what is reported about GLP-1 receptor agonists, stem-cell/exosome products, and drug-delivery systems in metabolic disease (diabetes, obesity, prediabetes, and closely related inflammatory or repair settings)?",
        "",
        f"**Scope:** {len(index)} included full texts after title screen, public-OA retrieval, and full-text eligibility. Sorted by year then citekey. Every findings cell is the extracted abstract/lead from the matching note — not a new claim.",
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
        "Rows are included studies only. Cells compress the per-paper note (abstract/lead). Mechanical extraction can garble columns; treat numbers as provisional until checked against the PDF. Sorted by year, then citekey.",
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
