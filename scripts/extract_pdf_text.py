#!/usr/bin/env python3
"""Extract text from PDFs in a folder to sibling .txt files (pypdf)."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-dir", required=True)
    args = parser.parse_args()
    pdf_dir = Path(args.pdf_dir)
    try:
        from pypdf import PdfReader
    except ImportError:
        raise SystemExit("pypdf is required: pip install pypdf")
    n_ok = 0
    for pdf in sorted(pdf_dir.glob("*.pdf")):
        dest = pdf.with_suffix(".txt")
        try:
            reader = PdfReader(str(pdf))
            pages = [(page.extract_text() or "") for page in reader.pages]
            dest.write_text("\n\n".join(pages), encoding="utf-8")
            n_ok += 1
            print(f"OK {pdf.name} pages={len(pages)} chars={sum(len(p) for p in pages)}")
        except Exception as e:
            print(f"FAIL {pdf.name} {type(e).__name__}: {e}")
    print(f"extracted {n_ok} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
