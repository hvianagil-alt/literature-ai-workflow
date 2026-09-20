#!/usr/bin/env python3
"""Fail a journal review that still writes like a paper catalogue.

Title/Abstract form (`check_article.py --form-model`) can pass while the body
still gives every included paper equal depth, repeats a slogan, or never nests
a mechanism. This script is the body-craft gate (Pautasso; Gopen & Swan;
Swales CARS; SANRA item 5).

Usage:
    python3 scripts/check_review_craft.py --article review/runs/<id>/article.md
    python3 scripts/check_review_craft.py --article path.md --short
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from review_craft_features import extract_craft_features


def craft_problems(text: str, short: bool) -> list[str]:
    f = extract_craft_features(text)
    problems: list[str] = []
    if short:
        return problems
    if f["body_words"] < 4000:
        return problems
    if f["nested_thematic_h3"] < 3:
        problems.append(
            "thematic body has too few nested subsections (need 3.1 / 3.2 on "
            "mechanisms or questions, not only Methods 2.1 Search; published "
            "narrative reviews nest topics — see review-writing-craft)"
        )
    if f["meta_reviewer_hits"] >= 2:
        problems.append(
            f"meta-reviewer diction outside Methods ({int(f['meta_reviewer_hits'])} hits: "
            "'this sample', 'intellectual model', 'named cycle is not one'); "
            "write as a scientist, not as a workflow log"
        )
    if f["slogan_hits"] >= 3:
        problems.append(
            "thesis slogan repeated too often (named cycle / same megapascal); "
            "state the argument once, then develop it"
        )
    if f["thematic_synthesis_frac"] < 0.4:
        problems.append(
            "thematic sections rarely close with a synthesis sentence "
            "(Taken together / what this heading cannot show / Concluding remarks); "
            "Houška-style published reviews end each nest before the next topic"
        )
    if f["single_study_frac"] >= 0.35 and f["single_study_paragraphs"] >= 8:
        problems.append(
            f"{int(f['single_study_paragraphs'])} paragraphs are one-paper file cards "
            f"({f['single_study_frac']:.0%} of long paragraphs); hinge studies get "
            "design+result, the rest are grouped (Pautasso Rule 5; Snyder synthesis)"
        )
    if f["intro_mean_sentence_words"] >= 52:
        problems.append(
            f"Introduction mean sentence length {f['intro_mean_sentence_words']:.0f} words; "
            "Gopen & Swan: one new idea per sentence, given information first"
        )
    if f["cars_niche_before_aim"] < 0.5:
        problems.append(
            "Introduction never occupies a niche before the aim (Swales CARS: "
            "territory → gap/tension → aim)"
        )
    return problems


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--article", required=True)
    p.add_argument("--short", action="store_true")
    args = p.parse_args(argv)
    path = Path(args.article)
    if not path.is_file():
        print(f"FAIL article missing: {path}", file=sys.stderr)
        return 2
    problems = craft_problems(path.read_text(encoding="utf-8"), args.short)
    if problems:
        print("FAIL review craft is not publishable yet:")
        for item in problems:
            print(f"  - {item}")
        print("Rewrite with review-writing-craft and review-prose before delivering.")
        return 1
    print(f"OK {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
