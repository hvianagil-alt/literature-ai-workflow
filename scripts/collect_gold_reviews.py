#!/usr/bin/env python3
"""Collect published OA *reviews* for the form-quality model.

Searches OpenAlex (type:review, public OA journal articles only). Never
invents titles. Never bypasses paywalls. Findings from these papers must
not be copied into any manuscript — titles and abstracts are used as
*form* examples only.

Usage:
    python3 scripts/collect_gold_reviews.py \\
        --mailto you@example.com \\
        --out-dir review/ml \\
        --from-year 2019 --to-year 2026
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from search_oa_related import (  # noqa: E402
    OPENALEX_WORKS,
    TIMEOUT,
    CTX,
    USER_AGENT,
    search_openalex,
    work_to_record,
)

ROOT = Path(__file__).resolve().parents[1]

# Queries are field-shaped, not paper lists. Hits come only from the API.
FIELD_QUERIES: dict[str, list[str]] = {
    "endocrinology": [
        "GLP-1 receptor agonist diabetes obesity review",
        "incretin therapy type 2 diabetes narrative review",
    ],
    "nanomedicine": [
        "liposome nanocarrier drug delivery review",
        "stimuli responsive liposome review",
    ],
    "food-science": [
        "high pressure processing food safety review",
        "high hydrostatic pressure milk juice meat review",
    ],
    "neuroscience": [
        "Parkinson cannabinoid cannabidiol review",
        "cannabis Parkinson disease non-motor review",
    ],
    "generic-narrative": [
        "narrative review clinical mechanisms",
        "narrative review pathophysiology",
    ],
}

FIELD_TITLE_HINTS: dict[str, str] = {
    "endocrinology": r"GLP|incretin|diabetes|obesity|insulin|tirzepatide|semaglutide|glucagon",
    "nanomedicine": r"nano|liposom|lipid|vesicle|micelle|drug delivery|PEGyl",
    "food-science": r"high[- ]pressure|hydrostatic|\bHPP\b|pasteur|non[- ]?thermal|food safety|food matrix|ultra-processed|fermented food|food waste|food systems|human milk",
    "neuroscience": r"Parkinson|cannab|dopamin|neurodegener|CB1|CB2",
    "generic-narrative": r".",
}
RUN_FIELDS: dict[str, str] = {
    "2026-09-19-scopus-oa-full": "endocrinology",
    "2026-09-19-scopus-oa": "endocrinology",
    "2026-09-19-nanocarriers": "nanomedicine",
    "2026-09-20-scopus-hpp": "food-science",
    "2026-09-20-pd-cannabinoids": "neuroscience",
}


def _get_json(url: str, mailto: str) -> tuple[int, dict | None]:
    headers = {
        "User-Agent": USER_AGENT,
        "From": mailto,
        "Accept": "application/json",
    }
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as resp:
            body = resp.read()
            code = resp.getcode() or 200
    except urllib.error.HTTPError as e:
        return e.code, None
    except urllib.error.URLError:
        return 0, None
    try:
        return code, json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return code, None


def work_by_doi(doi: str, mailto: str) -> dict | None:
    doi = doi.replace("https://doi.org/", "").strip()
    if not doi:
        return None
    url = (
        OPENALEX_WORKS
        + "/"
        + urllib.parse.quote("doi:" + doi, safe=":")
        + "?"
        + urllib.parse.urlencode({"mailto": mailto})
    )
    code, data = _get_json(url, mailto)
    if code != 200 or not isinstance(data, dict):
        return None
    rec = work_to_record(data)
    return rec if rec.get("doi") else None


def harvest_style_study_dois() -> list[tuple[str, str, str]]:
    """DOIs already sampled as form comparators in this repo (titles only)."""
    paths = [
        ROOT / "review/runs/2026-09-20-style-study/batch1.json",
        ROOT / "review/runs/2026-09-20-style-study-batch2/catalog.json",
        ROOT / "review/runs/2026-09-19-review-craft-study/catalog.json",
    ]
    out: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for path in paths:
        if not path.is_file():
            continue
        try:
            rows = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if isinstance(rows, dict):
            rows = rows.get("records") or rows.get("catalog") or []
        for row in rows:
            if not isinstance(row, dict):
                continue
            doi = (row.get("doi") or "").replace("https://doi.org/", "").strip()
            title = row.get("title") or ""
            if not doi or doi.lower() in seen:
                continue
            seen.add(doi.lower())
            out.append((doi, title, "generic-narrative"))
    return out


def collect_field(
    field: str,
    queries: list[str],
    *,
    mailto: str,
    from_year: int,
    to_year: int,
    per_page: int,
    max_per_field: int,
    journal_quality: str,
) -> tuple[list[dict], list[dict]]:
    seen: set[str] = set()
    records: list[dict] = []
    searches: list[dict] = []
    for query in queries:
        hits, status = search_openalex(
            query,
            mailto=mailto,
            per_page=per_page,
            from_year=from_year,
            to_year=to_year,
            journal_quality=journal_quality,
            sort="relevance_score:desc",
            work_type="review",
        )
        searches.append({"field": field, "query": query, "status": status, "hits": len(hits)})
        for rec in hits:
            doi = (rec.get("doi") or "").lower()
            if not doi or doi in seen:
                continue
            if not (rec.get("abstract") or "").strip():
                continue
            hint = FIELD_TITLE_HINTS.get(field) or r"."
            if not re.search(hint, rec.get("title") or "", re.I):
                continue
            seen.add(doi)
            rec = dict(rec)
            rec["field"] = field
            rec["origin"] = "openalex_type_review"
            rec["query"] = query
            records.append(rec)
            if len(records) >= max_per_field:
                return records, searches
        time.sleep(0.25)
    return records, searches


def maybe_fetch_pdfs(
    records: list[dict],
    *,
    out_dir: Path,
    email: str,
    per_field: int,
) -> list[dict]:
    if per_field <= 0:
        return []
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from fetch_oa_pdfs import fetch_one  # noqa: WPS433

    dest_root = ROOT / "papers" / "ml-gold"
    dest_root.mkdir(parents=True, exist_ok=True)
    by_field: dict[str, int] = {}
    log: list[dict] = []
    for rec in records:
        field = rec.get("field") or "generic-narrative"
        if by_field.get(field, 0) >= per_field:
            continue
        doi = rec.get("doi") or ""
        citekey = rec.get("citekey") or "unknown"
        got = fetch_one(doi, email)
        row = {
            "citekey": citekey,
            "doi": doi,
            "field": field,
            "ok": bool(got.get("ok")),
            "error": got.get("error"),
            "source_url": got.get("source_url"),
            "bytes": got.get("bytes"),
            "format": got.get("format") or ("pdf" if got.get("pdf") else None),
        }
        if got.get("ok") and got.get("pdf"):
            path = dest_root / f"{citekey}.pdf"
            path.write_bytes(got["pdf"])
            row["path"] = str(path)
            by_field[field] = by_field.get(field, 0) + 1
        elif got.get("ok") and got.get("text"):
            path = dest_root / f"{citekey}.txt"
            path.write_text(got["text"], encoding="utf-8")
            row["path"] = str(path)
            by_field[field] = by_field.get(field, 0) + 1
        log.append(row)
        print(
            f"{'OK' if row['ok'] else 'FAIL'}  {field}  {citekey}  {row.get('error') or row.get('bytes')}",
            flush=True,
        )
        time.sleep(0.25)
    (out_dir / "gold-fetch-log.json").write_text(
        json.dumps(log, indent=2) + "\n", encoding="utf-8"
    )
    return log


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mailto", required=True)
    p.add_argument("--out-dir", default=str(ROOT / "review" / "ml"))
    p.add_argument("--from-year", type=int, default=2019)
    p.add_argument("--to-year", type=int, default=2026)
    p.add_argument("--per-page", type=int, default=20)
    p.add_argument("--max-per-field", type=int, default=18)
    p.add_argument(
        "--journal-quality",
        default="journal",
        help="Venue bar passed to search_oa_related (default: journal)",
    )
    p.add_argument(
        "--include-style-study",
        action="store_true",
        help="Look up OpenAlex abstracts for DOIs already in the in-repo craft studies",
    )
    p.add_argument(
        "--fetch-pdfs",
        type=int,
        default=0,
        help="Public OA full texts to fetch per field (0 = titles/abstracts only)",
    )
    args = p.parse_args(argv)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    all_records: list[dict] = []
    searches: list[dict] = []
    seen: set[str] = set()
    for field, queries in FIELD_QUERIES.items():
        recs, meta = collect_field(
            field,
            queries,
            mailto=args.mailto,
            from_year=args.from_year,
            to_year=args.to_year,
            per_page=args.per_page,
            max_per_field=args.max_per_field,
            journal_quality=args.journal_quality,
        )
        searches.extend(meta)
        for rec in recs:
            doi = (rec.get("doi") or "").lower()
            if doi in seen:
                continue
            seen.add(doi)
            all_records.append(rec)
        print(f"{field}: {len(recs)} OA reviews with abstracts", flush=True)

    style_lookups = 0
    if args.include_style_study:
        for doi, title, field in harvest_style_study_dois()[:40]:
            if doi.lower() in seen:
                continue
            rec = work_by_doi(doi, args.mailto)
            time.sleep(0.15)
            if not rec or not (rec.get("abstract") or "").strip():
                continue
            rec["field"] = field
            rec["origin"] = "style_study_doi_lookup"
            rec["seed_title"] = title
            seen.add(doi.lower())
            all_records.append(rec)
            style_lookups += 1
        print(f"style-study DOI lookups with abstracts: {style_lookups}", flush=True)

    catalog_path = out_dir / "gold-catalog.json"
    payload = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "source": "openalex",
        "work_type": "review",
        "from_year": args.from_year,
        "to_year": args.to_year,
        "journal_quality": args.journal_quality,
        "warning": (
            "API hits used as form comparators only. Do not cite these records "
            "in a manuscript unless a public full text was retrieved and extracted "
            "as an included paper. Do not copy findings into article.md."
        ),
        "n_records": len(all_records),
        "searches": searches,
        "records": all_records,
        "run_field_map": RUN_FIELDS,
    }
    catalog_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {catalog_path} n={len(all_records)}")

    if args.fetch_pdfs:
        maybe_fetch_pdfs(
            all_records,
            out_dir=out_dir,
            email=args.mailto,
            per_field=args.fetch_pdfs,
        )
    ok_searches = sum(1 for s in searches if (s.get("status") or {}).get("ok"))
    return 0 if all_records or ok_searches else 2


if __name__ == "__main__":
    raise SystemExit(main())
