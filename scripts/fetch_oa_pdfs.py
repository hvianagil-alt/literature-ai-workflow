#!/usr/bin/env python3
"""Fetch openly available PDFs for DOIs listed in a run catalog.

Only follows public OA landing/PDF URLs (OpenAlex, Unpaywall, Europe PMC,
publisher PDF conventions, doi.org content negotiation). Does not attempt
paywall bypass, publisher login, or Sci-Hub.

Usage:
    python3 scripts/fetch_oa_pdfs.py --run-dir review/runs/<id> \\
        --out-dir papers/scopus-oa --email you@example.com
"""

from __future__ import annotations

import argparse
import json
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from phase_log import append_phase  # noqa: E402

USER_AGENT = (
    "literature-ai-workflow/0.1 (OA PDF fetch for local literature review; "
    "+https://github.com/hvianagil-alt/literature-ai-workflow)"
)
TIMEOUT = 45
CTX = ssl.create_default_context()


def _request(
    url: str,
    *,
    accept: str | None = None,
    email: str | None = None,
) -> tuple[int, str, bytes]:
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    if email:
        headers["From"] = email
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as resp:
            return resp.getcode() or 200, resp.geturl(), resp.read()
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return e.code, e.geturl() if hasattr(e, "geturl") else url, body


def looks_like_pdf(data: bytes, content_url: str) -> bool:
    if data[:5] == b"%PDF-":
        return True
    # some servers prepend a UTF-8 BOM or whitespace
    stripped = data.lstrip()
    return stripped[:5] == b"%PDF-" or content_url.lower().endswith(".pdf") and stripped[:4] == b"%PDF"


def openalex_oa_url(doi: str) -> tuple[str | None, int]:
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
    code, _, body = _request(url, accept="application/json")
    if code != 200:
        return None, 1
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return None, 1
    oa = data.get("open_access") or {}
    return oa.get("oa_url") or data.get("best_oa_location", {}).get("pdf_url"), 1


def unpaywall_oa_url(doi: str, email: str) -> tuple[str | None, int]:
    url = (
        "https://api.unpaywall.org/v2/"
        + urllib.parse.quote(doi)
        + "?email="
        + urllib.parse.quote(email)
    )
    code, _, body = _request(url, accept="application/json", email=email)
    if code != 200:
        return None, 1
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return None, 1
    loc = data.get("best_oa_location") or {}
    return loc.get("url_for_pdf") or loc.get("url"), 1


def europepmc_pdf_url(doi: str) -> tuple[str | None, int]:
    q = urllib.parse.urlencode(
        {"query": f"DOI:{doi}", "format": "json", "pageSize": 1}
    )
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + q
    code, _, body = _request(url, accept="application/json")
    if code != 200:
        return None, 1
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return None, 1
    hits = (data.get("resultList") or {}).get("result") or []
    if not hits:
        return None, 1
    pmcid = hits[0].get("pmcid")
    if pmcid:
        return f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/", 1
    return None, 1


def publisher_guess_urls(doi: str) -> list[str]:
    urls: list[str] = []
    if doi.startswith("10.1186/"):
        article = doi
        # BMC / SpringerOpen counter PDF
        urls.append(f"https://doi.org/{doi}")
        urls.append(f"https://link.springer.com/content/pdf/{urllib.parse.quote(doi, safe='')}.pdf")
        urls.append(
            "https://jnanobiotechnology.biomedcentral.com/counter/pdf/"
            + urllib.parse.quote(doi)
            + ".pdf"
        )
        urls.append(
            "https://bmcpublichealth.biomedcentral.com/counter/pdf/"
            + urllib.parse.quote(doi)
            + ".pdf"
        )
        urls.append(
            "https://bmcmed.biomedcentral.com/counter/pdf/"
            + urllib.parse.quote(doi)
            + ".pdf"
        )
        urls.append(
            "https://jpro.biomedcentral.com/counter/pdf/"
            + urllib.parse.quote(doi)
            + ".pdf"
        )
        urls.append(
            "https://biolres.biomedcentral.com/counter/pdf/"
            + urllib.parse.quote(doi)
            + ".pdf"
        )
        _ = article
    if doi.startswith("10.1038/"):
        art = doi.split("/", 1)[1]
        urls.append(f"https://www.nature.com/articles/{art}.pdf")
        urls.append(f"https://www.nature.com/articles/{art}")
    if doi.startswith("10.1016/"):
        urls.append(f"https://www.sciencedirect.com/science/article/pii/pdf?doi={urllib.parse.quote(doi)}")
    urls.append(f"https://doi.org/{doi}")
    # de-dupe preserving order
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def try_download_pdf(url: str) -> tuple[bytes | None, str, int]:
    code, final_url, body = _request(url, accept="application/pdf,application/octet-stream;q=0.9,*/*;q=0.1")
    calls = 1
    if looks_like_pdf(body, final_url):
        return body, final_url, calls
    # HTML landing page: look for a PDF link
    if code == 200 and b"%PDF-" not in body[:16]:
        text = body.decode("utf-8", errors="replace")
        for pattern in (
            'citation_pdf_url" content="',
            'citation_pdf_url" content=\'',
        ):
            if pattern in text:
                start = text.index(pattern) + len(pattern)
                end = text.find('"', start)
                if end == -1:
                    end = text.find("'", start)
                if end != -1:
                    pdf_url = text[start:end]
                    code2, final2, body2 = _request(pdf_url, accept="application/pdf")
                    calls += 1
                    if looks_like_pdf(body2, final2):
                        return body2, final2, calls
    return None, final_url, calls


def fetch_one(doi: str, email: str) -> dict:
    http_calls = 0
    tried: list[str] = []
    sources = []

    oa_url, n = openalex_oa_url(doi)
    http_calls += n
    sources.append("openalex")
    if oa_url:
        tried.append(oa_url)

    up_url, n = unpaywall_oa_url(doi, email)
    http_calls += n
    sources.append("unpaywall")
    if up_url and up_url not in tried:
        tried.append(up_url)

    pmc_url, n = europepmc_pdf_url(doi)
    http_calls += n
    sources.append("europepmc")
    if pmc_url and pmc_url not in tried:
        tried.append(pmc_url)

    for u in publisher_guess_urls(doi):
        if u not in tried:
            tried.append(u)

    for url in tried:
        pdf, final, n = try_download_pdf(url)
        http_calls += n
        if pdf:
            return {
                "doi": doi,
                "ok": True,
                "source_url": final,
                "attempted": tried,
                "http_calls": http_calls,
                "bytes": len(pdf),
                "pdf": pdf,
                "error": None,
                "lookup_sources": sources,
            }
        time.sleep(0.3)

    return {
        "doi": doi,
        "ok": False,
        "source_url": None,
        "attempted": tried,
        "http_calls": http_calls,
        "bytes": 0,
        "pdf": None,
        "error": "no_public_pdf_found",
        "lookup_sources": sources,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument(
        "--email",
        required=True,
        help="Contact email sent to Unpaywall/OpenAlex-style APIs (required by Unpaywall)",
    )
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    out_dir = Path(args.out_dir)
    catalog = json.loads((run_dir / "catalog.json").read_text(encoding="utf-8"))
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    total_http = 0
    ok_n = 0
    for rec in catalog:
        doi = rec.get("doi") or ""
        citekey = rec.get("citekey") or "unknown"
        if not doi:
            results.append(
                {
                    "citekey": citekey,
                    "doi": "",
                    "ok": False,
                    "error": "missing_doi",
                    "path": None,
                    "http_calls": 0,
                    "source_url": None,
                    "attempted": [],
                }
            )
            continue
        got = fetch_one(doi, args.email)
        total_http += int(got["http_calls"])
        dest = out_dir / f"{citekey}.pdf"
        row = {
            "citekey": citekey,
            "doi": doi,
            "ok": got["ok"],
            "error": got["error"],
            "path": str(dest) if got["ok"] else None,
            "http_calls": got["http_calls"],
            "source_url": got["source_url"],
            "attempted": got["attempted"],
            "bytes": got["bytes"],
        }
        if got["ok"]:
            dest.write_bytes(got["pdf"])
            ok_n += 1
            print(f"OK  {citekey}  {doi}  {got['bytes']} bytes  {got['source_url']}")
        else:
            print(f"FAIL {citekey}  {doi}  {got['error']}")
        results.append(row)
        time.sleep(0.4)

    log_path = run_dir / "fetch-log.json"
    serializable = [{k: v for k, v in r.items() if k != "pdf"} for r in results]
    log_path.write_text(json.dumps(serializable, indent=2) + "\n", encoding="utf-8")
    append_phase(
        run_dir,
        "fetching",
        input_chars=sum(len(r.get("doi") or "") for r in catalog),
        output_chars=len(log_path.read_text(encoding="utf-8")),
        http_calls=total_http,
        items=len(catalog),
        notes=f"fetched {ok_n}/{len(catalog)} public PDFs into {out_dir}",
        extra={"ok": ok_n, "failed": len(catalog) - ok_n},
    )
    print(f"\n{ok_n}/{len(catalog)} PDFs saved under {out_dir}")
    print(f"log: {log_path}")
    return 0 if ok_n else 1


if __name__ == "__main__":
    raise SystemExit(main())
