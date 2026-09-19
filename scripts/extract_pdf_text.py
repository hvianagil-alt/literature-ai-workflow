#!/usr/bin/env python3
"""Extract text from PDFs in a folder to sibling .txt files (pypdf)."""

from __future__ import annotations

import argparse
import warnings
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-dir", required=True)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="skip PDFs that already have a non-empty sibling .txt",
    )
    args = parser.parse_args()
    pdf_dir = Path(args.pdf_dir)
    try:
        from pypdf import PdfReader
    except ImportError:
        raise SystemExit("pypdf is required: pip install pypdf")
    warnings.filterwarnings("ignore")
    n_ok = 0
    n_skip = 0
    for pdf in sorted(pdf_dir.glob("*.pdf")):
        dest = pdf.with_suffix(".txt")
        if args.resume and dest.exists() and dest.stat().st_size > 200:
            n_skip += 1
            continue
        try:
            reader = PdfReader(str(pdf))
            pages = [(page.extract_text() or "") for page in reader.pages]
            dest.write_text("\n\n".join(pages), encoding="utf-8")
            n_ok += 1
            print(f"OK {pdf.name} pages={len(pages)} chars={sum(len(p) for p in pages)}")
        except Exception as e:
            print(f"FAIL {pdf.name} {type(e).__name__}: {e}")
    print(f"extracted {n_ok} files (skipped {n_skip})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
