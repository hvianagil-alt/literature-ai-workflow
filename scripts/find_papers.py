#!/usr/bin/env python3
"""Search public OpenAlex OA works for a topic or seed-related query.

Free. No API key. Does not invent titles. Does not download PDFs
(use fetch_oa_pdfs.py for that). Low cost: one HTTP search, JSON only.

Usage:
    python3 scripts/find_papers.py \\
        --query "oral GLP-1 type 2 diabetes delivery" \\
        --mailto you@example.com \\
        --run-dir review/runs/<id> \\
        --origin topic_search
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from search_oa_related import catalog_rows, search_openalex  # noqa: E402

ORIGINS = ("topic_search", "related_to_seeds")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument(
        "--mailto",
        required=True,
        help="Contact email for OpenAlex polite pool (free; not a login)",
    )
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--per-page", type=int, default=20)
    parser.add_argument("--from-year", type=int, default=None)
    parser.add_argument("--to-year", type=int, default=None)
    parser.add_argument(
        "--journal-quality",
        choices=("none", "journal", "doaj", "cited"),
        default="journal",
        help="Venue bar asked at direction check (default: peer-reviewed journals)",
    )
    parser.add_argument("--min-cited-by", type=int, default=None)
    parser.add_argument(
        "--sort",
        choices=("cited_by_count:desc", "relevance_score:desc", "publication_date:desc"),
        default="cited_by_count:desc",
        help="Use relevance_score:desc for related-to-seeds so generic mega-reviews do not crowd the list",
    )
    parser.add_argument(
        "--origin",
        choices=ORIGINS,
        default="topic_search",
        help="topic_search if the folder was empty; related_to_seeds if expanding PDFs the user dropped",
    )
    args = parser.parse_args()
    if args.per_page < 1 or args.per_page > 50:
        print("FAIL --per-page must be 1–50 (keep the search cheap)", file=sys.stderr)
        return 2

    records, status = search_openalex(
        args.query,
        mailto=args.mailto,
        per_page=args.per_page,
        from_year=args.from_year,
        to_year=args.to_year,
        journal_quality=args.journal_quality,
        min_cited_by=args.min_cited_by,
        sort=args.sort,
    )
    out_dir = Path(args.run_dir) / "seed-search"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "query": args.query,
        "from_year": args.from_year,
        "to_year": args.to_year,
        "journal_quality": args.journal_quality,
        "min_cited_by": args.min_cited_by,
        "sort": args.sort,
        "origin": args.origin,
        "source": "openalex",
        "status": status,
        "warning": (
            "These are API hits, not included studies. Fetch OA PDFs next. "
            "Do not cite from this list without a retrieved full text. "
            "Never invent a paper that is not in this JSON."
        ),
        "records": records,
    }
    search_path = out_dir / "search.json"
    search_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    cat = catalog_rows(records, origin=args.origin)
    cat_path = out_dir / "catalog.json"
    cat_path.write_text(json.dumps(cat, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {search_path}  ok={status.get('ok')}  hits={len(records)}  "
        f"origin={args.origin}  error={status.get('error')}"
    )
    print(f"wrote catalog {cat_path} ({len(cat)} rows; not yet included)")
    return 0 if status.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
