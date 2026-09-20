#!/usr/bin/env python3
"""Rewrite article.md citations into Vancouver first-appearance order.

The first paper cited in the body (after Abstract/Keywords) becomes [1],
the next new paper [2], and so on. The References list is the same sequence,
with a blank line between each entry.

    python3 scripts/renumber_citations.py --article review/runs/<id>/article.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_article import citation_order_problems, renumber_vancouver  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article", required=True)
    args = parser.parse_args()
    path = Path(args.article)
    if not path.is_file():
        print(f"FAIL article missing: {path}", file=sys.stderr)
        return 2
    original = path.read_text(encoding="utf-8")
    rewritten = renumber_vancouver(original)
    path.write_text(rewritten, encoding="utf-8")
    leftover = citation_order_problems(rewritten)
    if leftover:
        print("WARN rewritten file still fails citation checks:")
        for p in leftover:
            print(f"  - {p}")
        return 1
    print(f"OK {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
