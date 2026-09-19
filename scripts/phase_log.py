#!/usr/bin/env python3
"""Append a phase usage record for a literature-review run.

Cursor chat does not expose native model token meters. This logger records
wall-clock time, tool/HTTP counts, character volume, and a chars/4 token
*estimate* so a later analysis can compare phases. Estimates are labeled
as estimates — never as billed tokens.

Usage:
    python3 scripts/phase_log.py --run-dir review/runs/<id> --phase discovery \\
        --input-chars 12000 --output-chars 4000 --http-calls 1 --notes "parsed bib"
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def estimate_tokens(n_chars: int) -> int:
    """Rough token estimate: ~4 characters per token. Never treat as billed usage."""
    if n_chars <= 0:
        return 0
    return (n_chars + 3) // 4


def append_phase(
    run_dir: Path,
    phase: str,
    *,
    input_chars: int = 0,
    output_chars: int = 0,
    http_calls: int = 0,
    tool_calls: int = 0,
    items: int = 0,
    notes: str = "",
    extra: dict | None = None,
) -> Path:
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / "usage-log.jsonl"
    record = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "phase": phase,
        "input_chars": int(input_chars),
        "output_chars": int(output_chars),
        "est_input_tokens_chars_div_4": estimate_tokens(input_chars),
        "est_output_tokens_chars_div_4": estimate_tokens(output_chars),
        "est_total_tokens_chars_div_4": estimate_tokens(input_chars + output_chars),
        "http_calls": int(http_calls),
        "tool_calls": int(tool_calls),
        "items": int(items),
        "notes": notes,
        "meter_source": (
            "estimate_only — Cursor does not expose native model token counts "
            "to this workflow; do not treat these as billed tokens"
        ),
    }
    if extra:
        record["extra"] = extra
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return log_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--phase", required=True)
    parser.add_argument("--input-chars", type=int, default=0)
    parser.add_argument("--output-chars", type=int, default=0)
    parser.add_argument("--http-calls", type=int, default=0)
    parser.add_argument("--tool-calls", type=int, default=0)
    parser.add_argument("--items", type=int, default=0)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()
    path = append_phase(
        Path(args.run_dir),
        args.phase,
        input_chars=args.input_chars,
        output_chars=args.output_chars,
        http_calls=args.http_calls,
        tool_calls=args.tool_calls,
        items=args.items,
        notes=args.notes,
    )
    print(f"appended {args.phase} -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
