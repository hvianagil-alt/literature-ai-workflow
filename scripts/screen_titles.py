#!/usr/bin/env python3
"""Assign unique record IDs and title-screen a catalog.json.

Usage:
    python3 scripts/screen_titles.py --run-dir review/runs/<id>
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

INCRETIN = re.compile(
    r"glp-?1|glucagon-like peptide|liraglutide|semaglutide|dulaglutide|"
    r"exenatide|lixisenatide|tirzepatide|incretin|beinaglutide",
    re.I,
)
VESICLE = re.compile(
    r"stem cell|mesenchymal|mscs?\b|ad-msc|exosome|extracellular vesicle|"
    r"\bevs?\b|exosomal",
    re.I,
)
DELIVERY = re.compile(
    r"nanoparticle|nanocarrier|nano-?medicine|microneedle|niosome|"
    r"hydrogel|lipid nanoparticle|\blnps?\b|drug delivery|oral delivery|"
    r"pulmonary delivery|inhalable|transdermal|sublingual|micelle|"
    r"microsphere|long-acting|insulin delivery|oral insulin|ionogel|"
    r"mini-tablet",
    re.I,
)
METABOLIC = re.compile(
    r"diabet|obes|prediabet|metabolic|nafld|mafld|nash|insulin|"
    r"t2dm|weight|steatos|retinopath|nephropath|wound|glycemic|"
    r"anti-?diabetic|glucose-lowering",
    re.I,
)
RELATED = re.compile(
    r"arthrit|osteoarth|myocardial|cardiac repair|inflamm|wound|ferroptosis",
    re.I,
)


def unique_id(rec: dict, seen: dict[str, int]) -> str:
    base = rec["citekey"]
    seen[base] = seen.get(base, 0) + 1
    if seen[base] == 1:
        return base
    tail = (rec.get("doi") or "nodoi").split("/")[-1]
    tail = re.sub(r"[^A-Za-z0-9]+", "", tail)[:16]
    return f"{base}__{tail}"


def decision(title: str) -> tuple[str, str]:
    t = title or ""
    inc = bool(INCRETIN.search(t))
    ves = bool(VESICLE.search(t))
    deliv = bool(DELIVERY.search(t))
    met = bool(METABOLIC.search(t))
    rel = bool(RELATED.search(t))
    topic = inc or ves or deliv
    if not topic:
        if re.search(r"anti-?diabetic|glucose-lowering", t, re.I) and met:
            return "title_include", "Anti-diabetic drug paper in a metabolic setting (may include GLP-1; kept for full text)"
        return "title_exclude", "No GLP-1/incretin, stem-cell/exosome, or delivery-system terms in title"
    if inc:
        return "title_include", "Incretin/GLP-1 family in title"
    if ves and (met or rel):
        return "title_include", "Stem-cell/exosome product in a metabolic or related repair/inflammatory setting"
    if deliv and (met or inc or rel):
        return "title_include", "Delivery system in a metabolic or related setting"
    if re.search(r"anti-?diabetic|glucose-lowering", t, re.I) and met:
        return "title_include", "Anti-diabetic drug paper in a metabolic setting (may include GLP-1; kept for full text)"
    if ves or deliv:
        return "title_exclude", "Vesicle or delivery terms present but no metabolic/related setting in title"
    return "title_exclude", "Off-topic on title"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    catalog = json.loads((run_dir / "catalog.json").read_text(encoding="utf-8"))
    seen: dict[str, int] = {}
    rows = []
    for rec in catalog:
        rid = unique_id(rec, seen)
        rec["record_id"] = rid
        status, reason = decision(rec.get("title") or "")
        rec["title_decision"] = status
        rec["title_reason"] = reason
        rows.append(rec)
    (run_dir / "catalog.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    include = [r for r in rows if r["title_decision"] == "title_include"]
    exclude = [r for r in rows if r["title_decision"] == "title_exclude"]
    screening = {
        "duplicates_removed": 0,
        "additional_records": 0,
        "n_screened": len(rows),
        "title_excluded": [
            {"citekey": r["record_id"], "reason": r["title_reason"], "title": r["title"]}
            for r in exclude
        ],
        "sought_for_retrieval": [r["record_id"] for r in include],
        "n_fulltext_assessed": 0,
        "fulltext_excluded": [],
        "included": [],
        "notes": (
            "Title screen only (BibTeX had no abstracts). "
            f"{len(include)} sought for full text; {len(exclude)} excluded on title. "
            "Citekey collisions disambiguated with record_id."
        ),
    }
    (run_dir / "screening.json").write_text(
        json.dumps(screening, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"catalog {len(rows)}  title_include {len(include)}  title_exclude {len(exclude)}")
    print(f"unique record_id {len({r['record_id'] for r in rows})}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
