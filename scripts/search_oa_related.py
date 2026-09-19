#!/usr/bin/env python3
"""Search OpenAlex for open-access works related to an interpretation gap.

Returns *only* what the OpenAlex API reports. Does not invent titles, authors,
years, or DOIs. Does not download PDFs (use fetch_oa_pdfs.py for that).

Usage:
    python3 scripts/search_oa_related.py \\
        --query "semaglutide prediabetes weight network meta-analysis" \\
        --mailto you@example.com \\
        --out review/runs/<id>/gap-retrieval/search-g1.json
"""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = (
    "literature-ai-workflow/0.1 (OA related-work search for local literature review; "
    "+https://github.com/hvianagil-alt/literature-ai-workflow)"
)
TIMEOUT = 45
CTX = ssl.create_default_context()
OPENALEX_WORKS = "https://api.openalex.org/works"


def citekey_from_work(work: dict) -> str:
    """Build a filesystem-safe citekey from API fields only."""
    authorships = work.get("authorships") or []
    last = ""
    if authorships:
        author = (authorships[0] or {}).get("author") or {}
        last = (author.get("display_name") or "").split()[-1]
    last = "".join(ch for ch in last if ch.isalnum()) or "Anon"
    year = ""
    date = work.get("publication_date") or work.get("publication_year") or ""
    if isinstance(date, int):
        year = str(date)
    else:
        year = str(date)[:4]
    year = "".join(ch for ch in year if ch.isdigit())[:4] or "0000"
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    suffix = "".join(ch for ch in doi[-6:] if ch.isalnum()) or "x"
    return f"{last}{year}_{suffix}"


def work_to_record(work: dict) -> dict:
    doi_url = work.get("doi") or ""
    doi = doi_url.replace("https://doi.org/", "").strip()
    oa = work.get("open_access") or {}
    best = work.get("best_oa_location") or {}
    loc = work.get("primary_location") or {}
    source = (loc.get("source") or {}) if isinstance(loc, dict) else {}
    authors = []
    for a in work.get("authorships") or []:
        name = ((a or {}).get("author") or {}).get("display_name")
        if name:
            authors.append(name)
    return {
        "citekey": citekey_from_work(work),
        "record_id": citekey_from_work(work),
        "openalex_id": work.get("id"),
        "title": work.get("display_name") or work.get("title") or "",
        "author": " and ".join(authors),
        "authors": authors,
        "year": str(work.get("publication_year") or "") ,
        "doi": doi,
        "journal": source.get("display_name") or "",
        "is_oa": bool(oa.get("is_oa")),
        "oa_status": oa.get("oa_status"),
        "oa_url": oa.get("oa_url") or best.get("pdf_url") or best.get("landing_page_url"),
        "cited_by_count": work.get("cited_by_count"),
        "publication_date": work.get("publication_date") or "",
        "type": work.get("type") or "",
    }


def search_openalex(
    query: str,
    *,
    mailto: str,
    per_page: int = 8,
    from_year: int | None = None,
) -> tuple[list[dict], dict]:
    """Return (records, meta). records is empty on HTTP/parse failure (not invented)."""
    filters = ["is_oa:true", "has_doi:true"]
    if from_year:
        filters.append(f"from_publication_date:{from_year}-01-01")
    params = {
        "search": query,
        "filter": ",".join(filters),
        "per_page": str(per_page),
        "mailto": mailto,
        "sort": "cited_by_count:desc",
    }
    url = OPENALEX_WORKS + "?" + urllib.parse.urlencode(params)
    headers = {"User-Agent": USER_AGENT, "From": mailto, "Accept": "application/json"}
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as resp:
            body = resp.read()
            code = resp.getcode() or 200
    except urllib.error.HTTPError as e:
        return [], {
            "ok": False,
            "http_status": e.code,
            "error": f"HTTP {e.code}",
            "query_url": url,
        }
    except urllib.error.URLError as e:
        return [], {
            "ok": False,
            "http_status": None,
            "error": f"URL error: {e.reason}",
            "query_url": url,
        }
    if code != 200:
        return [], {
            "ok": False,
            "http_status": code,
            "error": f"HTTP {code}",
            "query_url": url,
        }
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return [], {
            "ok": False,
            "http_status": code,
            "error": "invalid JSON from OpenAlex",
            "query_url": url,
        }
    results = data.get("results") or []
    records = [work_to_record(w) for w in results if isinstance(w, dict)]
    # Drop hits with no DOI — cannot fetch, must not be cited from title alone.
    records = [r for r in records if r.get("doi")]
    meta = data.get("meta") or {}
    return records, {
        "ok": True,
        "http_status": code,
        "error": None,
        "query_url": url,
        "openalex_count": meta.get("count"),
        "returned": len(records),
    }


def catalog_rows(records: list[dict]) -> list[dict]:
    """Subset of fields fetch_oa_pdfs.py needs."""
    rows = []
    for r in records:
        rows.append(
            {
                "citekey": r["citekey"],
                "record_id": r["citekey"],
                "entry_type": "ARTICLE",
                "title": r.get("title") or "",
                "author": r.get("author") or "",
                "year": r.get("year") or "",
                "journal": r.get("journal") or "",
                "doi": r.get("doi") or "",
                "open_access_flag": True,
                "gold_oa": (r.get("oa_status") or "") in {"gold", "hybrid"},
                "gap_fill": True,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="OpenAlex search string for one interpretation gap")
    parser.add_argument(
        "--mailto",
        required=True,
        help="Contact email (OpenAlex polite pool; also used as From:)",
    )
    parser.add_argument("--out", required=True, help="JSON file to write (API hits only)")
    parser.add_argument("--per-page", type=int, default=8)
    parser.add_argument(
        "--from-year",
        type=int,
        default=None,
        help="Optional lower bound on publication year (OpenAlex from_publication_date)",
    )
    parser.add_argument(
        "--write-catalog",
        default="",
        help="Optional path to a fetch_oa_pdfs catalog.json of these hits (still not inclusion)",
    )
    args = parser.parse_args()

    records, status = search_openalex(
        args.query,
        mailto=args.mailto,
        per_page=args.per_page,
        from_year=args.from_year,
    )
    payload = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "query": args.query,
        "from_year": args.from_year,
        "source": "openalex",
        "status": status,
        "warning": (
            "These are API hits, not included studies. Verify each record, "
            "select only those that address the stated gap, then fetch OA PDFs. "
            "Do not cite from this list without a retrieved full text."
        ),
        "records": records,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out}  ok={status.get('ok')}  hits={len(records)}  error={status.get('error')}")
    if args.write_catalog:
        cat = Path(args.write_catalog)
        cat.parent.mkdir(parents=True, exist_ok=True)
        cat.write_text(json.dumps(catalog_rows(records), indent=2) + "\n", encoding="utf-8")
        print(f"wrote catalog {cat} ({len(records)} rows; not yet included)")
    return 0 if status.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
