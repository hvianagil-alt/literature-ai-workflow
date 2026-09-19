#!/usr/bin/env python3
"""Full-text eligibility from extracted PDF text + fetch log.

Does not invent findings. Unreadable or missing files are logged, not skipped.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from screen_titles import DELIVERY, INCRETIN, METABOLIC, RELATED, VESICLE  # noqa: E402

MIN_CHARS = 500
REF_SPLIT = re.compile(r"\n\s*references\b|\n\s*bibliography\b", re.I)


def split_body_refs(text: str) -> tuple[str, str]:
    parts = REF_SPLIT.split(text, maxsplit=1)
    if len(parts) == 1:
        return text, ""
    return parts[0], parts[1]


def assess_text(title: str, text: str) -> tuple[str, str]:
    """Return (include|exclude|unreadable, reason)."""
    if len((text or "").strip()) < MIN_CHARS:
        return "unreadable", "Extracted text too short or empty to assess eligibility"
    body, refs = split_body_refs(text)
    blob = f"{title}\n{body}"
    inc_body = bool(INCRETIN.search(blob))
    ves_body = bool(VESICLE.search(blob))
    del_body = bool(DELIVERY.search(blob))
    met = bool(METABOLIC.search(blob))
    rel = bool(RELATED.search(blob))
    inc_refs_only = (not inc_body) and bool(INCRETIN.search(refs))
    ves_refs_only = (not ves_body) and bool(VESICLE.search(refs))
    del_refs_only = (not del_body) and bool(DELIVERY.search(refs))
    topic = inc_body or ves_body or del_body
    if not topic:
        if inc_refs_only or ves_refs_only or del_refs_only:
            return (
                "exclude",
                "Incretin/vesicle/delivery terms appear only in the references list, not as the study topic",
            )
        return (
            "exclude",
            "No GLP-1/incretin, stem-cell/exosome, or delivery-system intervention in extracted full text",
        )
    setting = met or rel or inc_body
    if not setting:
        return (
            "exclude",
            "Topic tools present but no metabolic or closely related setting in extracted full text",
        )
    if inc_body:
        return "include", "Incretin/GLP-1 family in extracted full text"
    if ves_body:
        return "include", "Stem-cell/exosome product in a metabolic or related setting (full text)"
    return "include", "Delivery system in a metabolic or related setting (full text)"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--txt-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    txt_dir = Path(args.txt_dir)
    catalog = json.loads((run_dir / "catalog.json").read_text(encoding="utf-8"))
    fetch_rows = []
    fp = run_dir / "fetch-log.json"
    if fp.exists():
        fetch_rows = json.loads(fp.read_text(encoding="utf-8"))
    fetch = {r.get("citekey"): r for r in fetch_rows}
    screen_path = run_dir / "screening.json"
    screen = json.loads(screen_path.read_text(encoding="utf-8")) if screen_path.exists() else {}

    sought = screen.get("sought_for_retrieval") or [
        r["record_id"] for r in catalog if r.get("title_decision") == "title_include"
    ]
    by_id = {r["record_id"]: r for r in catalog}

    not_retrieved: list[dict] = []
    full_ex: list[dict] = []
    included: list[str] = []
    n_assessed = 0

    for rid in sought:
        rec = by_id.get(rid) or {"title": "", "record_id": rid}
        dest_pdf_ok = fetch.get(rid, {}).get("ok")
        txt_path = txt_dir / f"{rid}.txt"
        if not txt_path.exists():
            err = fetch.get(rid, {}).get("error") or "missing extracted text"
            if dest_pdf_ok:
                err = "pdf_present_but_text_missing_or_unreadable"
            not_retrieved.append({"citekey": rid, "reason": err, "title": rec.get("title")})
            rec["fulltext_decision"] = "not_retrieved"
            rec["fulltext_reason"] = err
            continue
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        n_assessed += 1
        status, reason = assess_text(rec.get("title") or "", text)
        rec["fulltext_decision"] = status
        rec["fulltext_reason"] = reason
        if status == "include":
            included.append(rid)
        elif status == "unreadable":
            full_ex.append({"citekey": rid, "reason": reason, "title": rec.get("title")})
        else:
            full_ex.append({"citekey": rid, "reason": reason, "title": rec.get("title")})

    screen["n_fulltext_assessed"] = n_assessed
    screen["fulltext_excluded"] = full_ex
    screen["not_retrieved"] = not_retrieved
    screen["included"] = included
    screen["notes"] = (
        f"Title include {len(sought)}; not retrieved {len(not_retrieved)}; "
        f"full text assessed {n_assessed}; full-text excluded {len(full_ex)}; "
        f"included {len(included)}. Eligibility from extracted PDF text only."
    )
    screen_path.write_text(json.dumps(screen, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (run_dir / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"sought {len(sought)}  not_retrieved {len(not_retrieved)}  "
        f"assessed {n_assessed}  excluded {len(full_ex)}  included {len(included)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
