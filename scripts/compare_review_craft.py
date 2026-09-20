#!/usr/bin/env python3
"""Compare our article.md files to published OA reviews on writing-craft features.

Form only. Do not copy findings from the published reviews into a manuscript.

Usage:
    python3 scripts/compare_review_craft.py \
        --ours review/runs/2026-09-20-hpp-rerun/article.md \
        --published papers/2026-09-20-hpp-rerun/Houška2022_020223.txt \
        --report review/ml/writing-craft-report.md
"""

from __future__ import annotations

import argparse
from pathlib import Path

from review_craft_features import extract_from_path

KEYS = [
    "nested_thematic_h3",
    "meta_reviewer_hits",
    "slogan_hits",
    "single_study_frac",
    "intro_mean_sentence_words",
    "body_mean_sentence_words",
    "cars_niche_before_aim",
    "author_year_openers",
    "thematic_synthesis_frac",
    "body_words",
]


def _label(kind: str, path: str) -> str:
    p = Path(path)
    return f"{kind}: {p.parent.name}/{p.name}"


def _row(label: str, feats: dict[str, float]) -> str:
    cells = [label]
    for k in KEYS:
        v = feats[k]
        if k.endswith("frac"):
            cells.append(f"{v:.2f}")
        elif k.endswith("words") and k != "body_words":
            cells.append(f"{v:.1f}")
        else:
            cells.append(str(int(round(v))))
    return "| " + " | ".join(cells) + " |"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ours", action="append", default=[])
    p.add_argument("--published", action="append", default=[])
    p.add_argument("--report", default="review/ml/writing-craft-report.md")
    args = p.parse_args()
    lines = [
        "# Writing-craft comparison",
        "",
        "Published reviews are **form comparators only**. Do not import their findings.",
        "Features come from Pautasso (2013), Gopen & Swan (1990), Swales CARS, SANRA, and Snyder (2019).",
        "",
        "| File | nested 3.1 | meta-reviewer | slogan | one-paper para frac | intro words/sent | body words/sent | CARS niche | Author-Year openers | synth close | body words |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for path in args.published:
        feats = extract_from_path(path)
        lines.append(_row(_label("published", path), feats))
    for path in args.ours:
        feats = extract_from_path(path)
        lines.append(_row(_label("ours", path), feats))
    lines.extend(
        [
            "",
            "## How to read this",
            "",
            "- **nested 3.1:** published narrative reviews split mechanisms into 2.1 / 3.1. A flat `## 3` with no children is a catalogue spine.",
            "- **meta-reviewer:** `this sample`, `intellectual model`, `named cycle is not one` — workflow talk, not journal voice.",
            "- **slogan:** repeating the title argument instead of developing it.",
            "- **one-paper para frac:** share of long paragraphs that are a single study with n/MPa. Published reviews group supporting papers.",
            "- **CARS niche:** Introduction states a gap or tension before the aim.",
            "",
            "A draft can pass `check_article.py` and the title/Abstract form model and still fail these body-craft tests.",
            "",
        ]
    )
    out = Path(args.report)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK wrote {out}")
    print("\n".join(lines[5:-1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
