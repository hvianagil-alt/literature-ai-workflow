#!/usr/bin/env python3
"""Parse a Scopus (or generic) BibTeX export into a screening catalog.

No third-party dependencies. Writes JSON + CSV under a run directory.

Usage:
    python3 scripts/import_bib.py path/to/export.bib --run-dir review/runs/<id>
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from phase_log import append_phase  # noqa: E402

ENTRY_RE = re.compile(
    r"@(?P<kind>\w+)\s*\{\s*(?P<key>[^,]+)\s*,(?P<body>.*?)\n\}",
    re.DOTALL,
)
FIELD_RE = re.compile(
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*\{(?P<value>.*?)\}(?=\s*,\s*\n|\s*\n\})",
    re.DOTALL,
)


def parse_bibtex(text: str) -> list[dict]:
    records: list[dict] = []
    for match in ENTRY_RE.finditer(text):
        fields: dict[str, str] = {}
        for fm in FIELD_RE.finditer(match.group("body") + "\n}"):
            fields[fm.group("name").lower()] = re.sub(
                r"\s+", " ", fm.group("value")
            ).strip()
        note = fields.get("note", "")
        records.append(
            {
                "citekey": match.group("key").strip(),
                "entry_type": match.group("kind").upper(),
                "title": fields.get("title", ""),
                "author": fields.get("author", ""),
                "year": fields.get("year", ""),
                "journal": fields.get("journal", "").strip(),
                "doi": fields.get("doi", "").strip(),
                "url": fields.get("url", "").strip(),
                "pages": fields.get("pages", ""),
                "volume": fields.get("volume", ""),
                "number": fields.get("number", ""),
                "scopus_type": fields.get("type", ""),
                "note": note,
                "open_access_flag": "open access" in note.lower(),
                "gold_oa": "gold open access" in note.lower(),
                "green_oa": "green open access" in note.lower(),
            }
        )
    return records


def write_catalog(records: list[dict], run_dir: Path) -> tuple[Path, Path]:
    run_dir.mkdir(parents=True, exist_ok=True)
    json_path = run_dir / "catalog.json"
    csv_path = run_dir / "catalog.csv"
    json_path.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    fieldnames = list(records[0].keys()) if records else [
        "citekey",
        "title",
        "doi",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bib_path")
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    bib_path = Path(args.bib_path)
    run_dir = Path(args.run_dir)
    text = bib_path.read_text(encoding="utf-8", errors="replace")
    records = parse_bibtex(text)
    dest_bib = run_dir / "identification.bib"
    run_dir.mkdir(parents=True, exist_ok=True)
    dest_bib.write_text(text, encoding="utf-8")
    json_path, csv_path = write_catalog(records, run_dir)
    out = (
        f"parsed {len(records)} records from {bib_path.name}\n"
        f"wrote {json_path}\n"
        f"wrote {csv_path}\n"
        f"copied bib -> {dest_bib}\n"
    )
    print(out, end="")
    append_phase(
        run_dir,
        "discovery",
        input_chars=len(text),
        output_chars=len(json_path.read_text(encoding="utf-8")),
        http_calls=0,
        items=len(records),
        notes=f"BibTeX import of {bib_path.name}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
