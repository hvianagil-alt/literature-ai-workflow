#!/usr/bin/env python3
"""Write usage-log.md from usage-log.jsonl (chars/4 estimates, labeled as such)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

HEADER = """# Phase usage log (token estimates)

Cursor does not expose billed tokens. `est_*` = characters/4. Screening/extraction
estimates that use extracted PDF text are **upper bounds**, not billed usage.
Do not treat these figures as an invoice.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    lines = []
    jsonl = run_dir / "usage-log.jsonl"
    if jsonl.exists():
        for raw in jsonl.read_text(encoding="utf-8").splitlines():
            if raw.strip():
                lines.append(json.loads(raw))
    md = [HEADER, "", "| Phase | UTC | items | HTTP | est. in tok | est. out tok | est. total | notes |", "|---|---|---|---|---|---|---|---|"]
    for rec in lines:
        md.append(
            "| {phase} | {ts} | {items} | {http} | {ein} | {eout} | {etot} | {notes} |".format(
                phase=rec.get("phase", ""),
                ts=(rec.get("ts_utc") or "")[:19],
                items=rec.get("items", 0),
                http=rec.get("http_calls", 0),
                ein=rec.get("est_input_tokens_chars_div_4", 0),
                eout=rec.get("est_output_tokens_chars_div_4", 0),
                etot=rec.get("est_total_tokens_chars_div_4", 0),
                notes=(rec.get("notes") or "").replace("|", "/"),
            )
        )
    out = run_dir / "usage-log.md"
    out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
