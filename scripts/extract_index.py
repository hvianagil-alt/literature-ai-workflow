#!/usr/bin/env python3
"""Build a compact extraction index from PDF text (abstract/lead + flags).

This does not invent numbers. Sample-size regex hits are recorded only when
they appear in the extracted lead; otherwise sample is "not stated".
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from notes_from_text import abstract_or_lead  # noqa: E402
from screen_titles import DELIVERY, INCRETIN, METABOLIC, RELATED, VESICLE  # noqa: E402

N_RE = re.compile(
    r"\b(?:n\s*=\s*|N\s*=\s*|participants?\s+n\s*=\s*|sample of\s+)(\d[\d,]*)",
    re.I,
)


def design_flags(text: str) -> list[str]:
    t = text.lower()
    flags: list[str] = []
    if "network meta-analysis" in t or "network meta analysis" in t:
        flags.append("network_meta_analysis")
    elif "meta-analysis" in t or "meta analysis" in t:
        flags.append("meta_analysis")
    if "systematic review" in t:
        flags.append("systematic_review")
    if "narrative review" in t or "this review" in t[:1500]:
        flags.append("review")
    if re.search(r"\brandomi[sz]ed\b|\bplacebo-controlled\b|\bdouble-blind\b", t):
        flags.append("rct")
    if "case report" in t:
        flags.append("case_report")
    if re.search(r"\b(mice|mouse|rats?\b|murine|in vitro|zebrafish)\b", t):
        flags.append("preclinical")
    if "observational" in t or "cohort" in t or "real-world" in t:
        flags.append("observational")
    return flags or ["not_classified"]


def topic_flags(title: str, text: str) -> list[str]:
    blob = f"{title}\n{text}"
    flags = []
    if INCRETIN.search(blob):
        flags.append("incretin")
    if VESICLE.search(blob):
        flags.append("vesicle")
    if DELIVERY.search(blob):
        flags.append("delivery")
    if METABOLIC.search(blob):
        flags.append("metabolic")
    if RELATED.search(blob):
        flags.append("related_setting")
    return flags


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--txt-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    txt_dir = Path(args.txt_dir)
    catalog = json.loads((run_dir / "catalog.json").read_text(encoding="utf-8"))
    screen = json.loads((run_dir / "screening.json").read_text(encoding="utf-8"))
    included = set(screen.get("included") or [])
    rows = []
    for rec in catalog:
        rid = rec.get("record_id")
        if rid not in included:
            continue
        txt_path = txt_dir / f"{rid}.txt"
        if not txt_path.exists():
            continue
        raw = txt_path.read_text(encoding="utf-8", errors="replace")
        lead = abstract_or_lead(raw)
        n_hit = N_RE.search(lead) or N_RE.search(raw[:4000])
        rows.append(
            {
                "record_id": rid,
                "citekey": rec.get("citekey"),
                "title": rec.get("title"),
                "author": rec.get("author"),
                "year": rec.get("year"),
                "journal": rec.get("journal"),
                "doi": rec.get("doi"),
                "title_reason": rec.get("title_reason"),
                "fulltext_reason": rec.get("fulltext_reason"),
                "lead": lead[:1500],
                "lead_chars": len(lead),
                "text_chars": len(raw),
                "design": design_flags(lead + "\n" + rec.get("title", "")),
                "topics": topic_flags(rec.get("title") or "", lead),
                "n_in_lead": n_hit.group(1).replace(",", "") if n_hit else None,
            }
        )
    out = run_dir / "extraction-index.json"
    out.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} included records to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
