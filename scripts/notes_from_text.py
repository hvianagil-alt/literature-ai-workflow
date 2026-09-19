#!/usr/bin/env python3
"""Build first-pass extraction notes from PDF text (abstract + first pages).

This is a mechanical pass: it copies the Abstract (or opening text) and flags
what could not be found. A human/agent still has to verify numbers before
treating a note as final.

Usage:
    python3 scripts/notes_from_text.py --run-dir review/runs/<id> --txt-dir papers/<id>
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

ABSTRACT_RE = re.compile(
    r"(?:abstract|summary)\s*[:\n]\s*(.{200,2500}?)(?=\n(?:keywords|introduction|background|1\.|methods)\b)",
    re.I | re.S,
)


def abstract_or_lead(text: str) -> str:
    m = ABSTRACT_RE.search(text)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    lead = re.sub(r"\s+", " ", text[:1800]).strip()
    return lead


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--txt-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    txt_dir = Path(args.txt_dir)
    notes_dir = run_dir / "notes"
    notes_dir.mkdir(parents=True, exist_ok=True)
    catalog = json.loads((run_dir / "catalog.json").read_text(encoding="utf-8"))
    fetch = {}
    fp = run_dir / "fetch-log.json"
    if fp.exists():
        for row in json.loads(fp.read_text(encoding="utf-8")):
            fetch[row.get("citekey")] = row
    screen = {}
    sp = run_dir / "screening.json"
    if sp.exists():
        screen = json.loads(sp.read_text(encoding="utf-8"))
    included = set(screen.get("included") or [])
    full_ex = {r.get("citekey"): r for r in (screen.get("fulltext_excluded") or [])}
    n = 0
    for rec in catalog:
        if rec.get("title_decision") != "title_include":
            continue
        rid = rec["record_id"]
        txt_path = txt_dir / f"{rid}.txt"
        fetched = fetch.get(rid, {})
        ft_status = rec.get("fulltext_decision")
        if rid in full_ex and not txt_path.exists():
            reason = full_ex[rid].get("reason") or "full-text exclude"
            note = (
                f"# {rec['title']}\n\n"
                f"- **Citation (as given in the paper / filename):** {rec['author']}, {rec['year']}, {rec['journal']}. doi:{rec['doi']}\n"
                f"- **Source file:** papers/{txt_dir.name}/{rid}.pdf\n"
                f"- **Extracted:** {date.today().isoformat()}\n"
                f"- **Screening:** Title include; full text **excluded** — {reason}\n\n"
                "## Research question\nOut of scope after full text (see screening reason).\n\n"
                "## Methods\nnot used — excluded\n\n"
                "## Sample / data\nnot used — excluded\n\n"
                "## Key findings\n- not used as evidence; paper excluded at full text\n\n"
                "## Limitations (as stated by the authors, or evident from the methods)\n- excluded from synthesis\n\n"
                f"## Relevance to our research question\nOut of scope: {reason}\n\n"
                "## Open questions / things to verify\nNone; excluded.\n"
            )
            (notes_dir / f"{rid}.md").write_text(note, encoding="utf-8")
            n += 1
            continue
        if not txt_path.exists():
            note = (
                f"# {rec['title']}\n\n"
                f"- **Citation (as given in the paper / filename):** {rec['author']}, {rec['year']}, {rec['journal']}. doi:{rec['doi']}\n"
                f"- **Source file:** not retrieved\n"
                f"- **Extracted:** {date.today().isoformat()}\n"
                f"- **Screening:** Title include; full text **not retrieved** ({fetched.get('error', 'missing txt')})\n\n"
                "## Research question\nnot retrieved — no full text\n\n"
                "## Methods\nnot retrieved\n\n"
                "## Sample / data\nnot retrieved\n\n"
                "## Key findings\n- not retrieved; no claims taken from this record\n\n"
                "## Limitations (as stated by the authors, or evident from the methods)\n- PDF not retrieved\n\n"
                "## Relevance to our research question\nCannot assess beyond the title.\n\n"
                "## Open questions / things to verify\nRetrieve the PDF before citing.\n"
            )
            (notes_dir / f"{rid}.md").write_text(note, encoding="utf-8")
            n += 1
            continue
        raw = txt_path.read_text(encoding="utf-8", errors="replace")
        lead = abstract_or_lead(raw)
        if rid in full_ex or ft_status == "exclude":
            reason = (full_ex.get(rid) or {}).get("reason") or rec.get("fulltext_reason") or "full-text exclude"
            note = (
                f"# {rec['title']}\n\n"
                f"- **Citation (as given in the paper / filename):** {rec['author']}, {rec['year']}, {rec['journal']}. doi:{rec['doi']}\n"
                f"- **Source file:** papers/{txt_dir.name}/{rid}.pdf\n"
                f"- **Extracted:** {date.today().isoformat()}\n"
                f"- **Screening:** Title include; full text **excluded** — {reason}\n\n"
                f"## Research question\nOut of scope after full text.\n\n"
                f"## Methods\nnot used — excluded\n\n"
                f"## Sample / data\nnot used — excluded\n\n"
                f"## Key findings\n- not used as evidence; paper excluded at full text\n\n"
                f"## Limitations (as stated by the authors, or evident from the methods)\n- excluded from synthesis\n\n"
                f"## Relevance to our research question\nOut of scope: {reason}\n\n"
                f"## Open questions / things to verify\nNone; excluded.\n"
            )
            (notes_dir / f"{rid}.md").write_text(note, encoding="utf-8")
            n += 1
            continue
        in_flag = "included after full text" if (not included or rid in included) else "title include; full-text decision pending"
        note = (
            f"# {rec['title']}\n\n"
            f"- **Citation (as given in the paper / filename):** {rec['author']}, {rec['year']}, {rec['journal']}. doi:{rec['doi']}\n"
            f"- **Source file:** papers/{txt_dir.name}/{rid}.pdf\n"
            f"- **Extracted:** {date.today().isoformat()}\n"
            f"- **Screening:** {in_flag}. First-pass from extracted PDF text (abstract/lead). Numbers not in this lead are marked not stated.\n\n"
            f"## Research question\n"
            f"As stated in the paper title/lead: {rec['title']}\n\n"
            f"## Methods\n"
            f"See lead paragraph; study design not fully parsed in this mechanical pass.\n\n"
            f"## Sample / data\n"
            f"not stated in the extracted lead (check full PDF before using an N).\n\n"
            f"## Claim-ready facts\n"
            f"- **Design:** not yet filled — read the PDF\n"
            f"- **Population / model:** not yet filled\n"
            f"- **n:** not yet filled\n"
            f"- **Intervention / comparator:** not yet filled\n"
            f"- **Primary endpoint:** not yet filled\n"
            f"- **Primary result:** not yet filled\n"
            f"- **Cannot show:** not yet filled\n\n"
            f"## Key findings\n"
            f"- Lead/abstract as extracted: {lead}\n\n"
            f"## Limitations (as stated by the authors, or evident from the methods)\n"
            f"- Mechanical first-pass note; verify against the PDF before citing a number.\n\n"
            f"## Relevance to our research question\n"
            f"Title-screened in because: {rec.get('title_reason')}. Full-text: {rec.get('fulltext_reason') or 'pending'}.\n\n"
            f"## Open questions / things to verify\n"
            f"Confirm sample size, effect sizes, and whether numbers in the lead were OCR/extract artifacts.\n"
        )
        (notes_dir / f"{rid}.md").write_text(note, encoding="utf-8")
        n += 1
    print(f"wrote {n} notes under {notes_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
