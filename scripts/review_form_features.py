#!/usr/bin/env python3
"""Form-only features for comparing a review to published reviews.

These features describe *how* a manuscript is written (title, abstract joinery,
headings, catalog vs claim-first prose). They must not copy scientific findings
from gold reviews into any article.md.

Usage:
    python3 scripts/review_form_features.py --article path.md
    python3 scripts/review_form_features.py --title "..." --abstract "..."
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_article as ca  # noqa: E402

FRONT_FEATURES = [
    "title_word_count",
    "title_has_colon",
    "title_flourish",
    "title_workflow",
    "title_kind_named",
    "abstract_word_count",
    "abstract_sentence_mean",
    "abstract_has_citation",
    "abstract_has_etal",
    "abstract_ordinal",
    "abstract_acquisition",
    "abstract_contrast_per_100w",
    "abstract_anaphora_per_100w",
    "abstract_catalog_per_100w",
    "abstract_hedge_per_100w",
    "abstract_slogan_per_100w",
    "abstract_evidence_rank_per_100w",
    "abstract_this_review_first_sentence",
    "abstract_sigla_defined",
    "abstract_calibration_per_100w",
]

FULL_FEATURES = [
    "has_keywords",
    "keyword_count",
    "intro_word_count",
    "intro_paragraphs",
    "intro_sentence_mean",
    "intro_causal_per_100w",
    "intro_bad_opener",
    "intro_has_aim",
    "thematic_h2_count",
    "has_results_h2",
    "process_h2",
    "et_al_opener_count",
    "according_to_count",
    "has_markdown_table",
    "has_table_callout",
    "discussion_word_count",
    "conclusions_ordinal",
    "claim_first_ratio",
    "body_word_count",
    "h3_outside_methods",
    "synthesis_per_100w",
    "methods_before_themes",
    "process_outside_methods",
    "short_sentence_frac",
    "coverage_fulltext",
]

FEATURE_NAMES = FRONT_FEATURES + FULL_FEATURES

CONTRAST_RE = re.compile(
    r"\b(yet|however|whereas|although|though|nonetheless|"
    r"at the same time|by contrast|in contrast|nevertheless)\b",
    re.I,
)
ANAPHORA_RE = re.compile(r"\b(this|these|those|that|such)\b", re.I)
CALIBRATION_RE = re.compile(
    r"\b(do not imply|does not imply|cannot be pooled|cannot show|"
    r"not a (?:single |one )?slogan|under the conditions studied)\b",
    re.I,
)
CATALOG_RE = re.compile(
    r"\bet al\.|this paper (?:reviews|discusses|aims)|"
    r"the authors (?:found|reported|showed)|"
    r"this review discusses|in this set\b",
    re.I,
)
HEDGE_RE = re.compile(
    r"\b(may|might|suggest(?:s|ed)?|consistent with|"
    r"under the conditions|cannot (?:show|be pooled)|do not imply)\b",
    re.I,
)
SLOGAN_RE = re.compile(
    r"\b(promising|remarkable|striking|highly effective|dramatic|"
    r"more research is needed|unlocking|holistic|comprehensive overview|"
    r"recent advances)\b",
    re.I,
)
EVIDENCE_RANK_RE = re.compile(
    r"\b(trial|randomised|randomized|observational|in vitro|"
    r"animal|preclinical|meta-analysis|cohort|placebo)\b",
    re.I,
)
KIND_RE = re.compile(
    r"\b(narrative review|systematic review|scoping review|"
    r"meta-analysis|mini-review|literature review)\b",
    re.I,
)
TITLE_WORKFLOW_RE = re.compile(
    r"\b(open-access set|oa export|this export|this sample|"
    r"included papers|scopus|pdfs we could)\b",
    re.I,
)
SYNTHESIS_RE = re.compile(
    r"\b(taken together|collectively|these data suggest|"
    r"cannot be pooled|incommensurable)\b",
    re.I,
)
AUTHOR_OPENER_RE = re.compile(
    r"^[A-Z][A-Za-z\-]+(?:\s+[A-Z][A-Za-z\-]+)?(?:\s+et al)?\.",
)


def _rate(pattern: re.Pattern[str], text: str) -> float:
    words = max(len(text.split()), 1)
    return 100.0 * len(pattern.findall(text)) / words


def _anaphora_rate(text: str) -> float:
    cleaned = re.sub(r"\bthis review\b", " ", text, flags=re.I)
    return _rate(ANAPHORA_RE, cleaned)


def _bool(x: bool) -> float:
    return 1.0 if x else 0.0


def document_from_front_matter(title: str, abstract: str, keywords: str = "") -> str:
    parts = [f"# {(title or 'Untitled').strip()}", "", "## Abstract", (abstract or "").strip()]
    if keywords.strip():
        parts += ["", "## Keywords", keywords.strip()]
    return "\n".join(parts) + "\n"


def _title_flags(title: str) -> dict[str, float]:
    words = re.findall(r"[A-Za-z0-9\-]+", title)
    flourish = 0.0
    for pat in ca.TITLE_FLOURISH:
        if re.search(pat, title, re.I):
            flourish = 1.0
            break
    return {
        "title_word_count": float(len(words)),
        "title_has_colon": _bool(":" in title),
        "title_flourish": flourish,
        "title_workflow": _bool(bool(TITLE_WORKFLOW_RE.search(title))),
        "title_kind_named": _bool(bool(KIND_RE.search(title))),
    }


def _abstract_flags(abstract: str) -> dict[str, float]:
    sents = ca.prose_sentences(abstract) or [
        s.strip() for s in ca.SENTENCE_SPLIT_RE.split(abstract) if len(s.split()) >= 4
    ]
    first = (sents[0] if sents else abstract[:240]).lower()
    ordinal = 0.0
    if len(ca.ORDINAL_OPENER.findall(abstract)) >= 2:
        ordinal = 1.0
    elif len(ca.ROMAN_ENUM.findall(abstract)) >= 2:
        ordinal = 1.0
    acq = 0.0
    for pat in ca.ABSTRACT_ACQUISITION:
        if re.search(pat, abstract, re.I):
            acq = 1.0
            break
    sigla = 0.0
    for m in ca.ABBR_PAREN.finditer(abstract):
        full = ca.expansion_for_abbr(abstract[: m.start()].rstrip(), m.group(1).strip())
        if full:
            sigla += 1.0
    return {
        "abstract_word_count": float(len(abstract.split())),
        "abstract_sentence_mean": ca._mean_words(sents) if sents else 0.0,
        "abstract_has_citation": _bool(bool(re.search(r"\[\d+\]", abstract))),
        "abstract_has_etal": _bool(bool(re.search(r"\bet al\.", abstract, re.I))),
        "abstract_ordinal": ordinal,
        "abstract_acquisition": acq,
        "abstract_contrast_per_100w": _rate(CONTRAST_RE, abstract),
        "abstract_anaphora_per_100w": _anaphora_rate(abstract),
        "abstract_catalog_per_100w": _rate(CATALOG_RE, abstract),
        "abstract_hedge_per_100w": _rate(HEDGE_RE, abstract),
        "abstract_slogan_per_100w": _rate(SLOGAN_RE, abstract),
        "abstract_evidence_rank_per_100w": _rate(EVIDENCE_RANK_RE, abstract),
        "abstract_this_review_first_sentence": _bool(first.startswith("this review")),
        "abstract_sigla_defined": sigla,
        "abstract_calibration_per_100w": _rate(CALIBRATION_RE, abstract),
    }


def extract_front_features(title: str, abstract: str) -> dict[str, float]:
    feats = {k: 0.0 for k in FRONT_FEATURES}
    feats.update(_title_flags(title or ""))
    feats.update(_abstract_flags(abstract or ""))
    return feats


def _claim_first_ratio(text: str) -> float:
    """Share of thematic paragraphs whose first sentence is not an author opener."""
    titles = ca.thematic_h2_titles(text)
    paras: list[str] = []
    for title in titles:
        sec = ca.section_after(text, title)
        paras.extend(ca.intro_paragraphs(sec))
    if not paras:
        body = ca.body_before_references(text)
        paras = ca.intro_paragraphs(body)
    if not paras:
        return 0.0
    claim = 0
    for para in paras:
        line = para.strip().split("\n", 1)[0].strip()
        if AUTHOR_OPENER_RE.match(line) or line.lower().startswith("according to "):
            continue
        claim += 1
    return claim / len(paras)


def extract_full_features(text: str) -> dict[str, float]:
    feats = {k: 0.0 for k in FULL_FEATURES}
    if not (text or "").strip():
        return feats
    body = ca.body_before_references(text)
    feats["coverage_fulltext"] = _bool(
        bool(ca.section_after(text, "Introduction"))
        or bool(ca.thematic_h2_titles(text))
        or bool(ca.section_after(text, "Discussion"))
    )
    kw = ca.section_after(text, "Keywords")
    feats["has_keywords"] = _bool(bool(kw.strip()))
    if kw.strip():
        body_kw = kw.strip().split("\n\n")[0]
        items = [x.strip() for x in re.split(r"[;,]", body_kw) if x.strip()]
        feats["keyword_count"] = float(len(items))
    intro = ca.section_after(text, "Introduction")
    intro_sents = ca.prose_sentences(intro)
    feats["intro_word_count"] = float(len(intro.split()))
    feats["intro_paragraphs"] = float(len(ca.intro_paragraphs(intro)))
    feats["intro_sentence_mean"] = ca._mean_words(intro_sents) if intro_sents else 0.0
    feats["intro_causal_per_100w"] = _rate(ca.CAUSAL_CONNECTOR_RE, intro)
    opener = ca.first_sentence(intro).lower()
    feats["intro_bad_opener"] = _bool(any(opener.startswith(b) for b in ca.INTRO_BAD_OPENERS))
    paras = ca.intro_paragraphs(intro)
    feats["intro_has_aim"] = _bool(bool(paras) and bool(ca.AIM_RE.search(paras[-1])))
    thematic = ca.thematic_h2_titles(text)
    feats["thematic_h2_count"] = float(len(thematic))
    feats["has_results_h2"] = _bool(
        any(ca.RESULTS_H2.match(re.sub(r"^\d+\.\s+", "", t).strip()) for t in ca.h2_titles(text))
    )
    feats["process_h2"] = _bool(any(ca.THEMATIC_PROCESS_H2.search(t) for t in thematic))
    results = body
    for stop in ("Discussion", "Conclusions"):
        chunk = ca.section_after(text, stop)
        if chunk:
            results = results.replace(chunk, "")
    feats["et_al_opener_count"] = float(ca.et_al_openers(results))
    feats["according_to_count"] = float(len(ca.AUTHOR_ACCORDING_RE.findall(body)))
    feats["has_markdown_table"] = _bool(ca.has_markdown_table(body))
    feats["has_table_callout"] = _bool(bool(ca.TABLE_CALLOUT.search(body)))
    disc = ca.section_after(text, "Discussion")
    feats["discussion_word_count"] = float(len(disc.split()))
    conc = ca.section_after(text, "Conclusions")
    feats["conclusions_ordinal"] = _bool(len(ca.ORDINAL_OPENER.findall(conc)) >= 2)
    feats["claim_first_ratio"] = _claim_first_ratio(text)
    feats["body_word_count"] = float(len(body.split()))
    feats["h3_outside_methods"] = float(ca.h3_outside_methods(text))
    feats["synthesis_per_100w"] = _rate(SYNTHESIS_RE, body)
    h2 = [re.sub(r"^\d+\.\s+", "", t).strip().lower() for t in ca.h2_titles(text)]
    if "methods" in h2 and thematic:
        try:
            methods_i = h2.index("methods")
            first_theme = None
            reserved = ca.RESERVED_H2
            for i, title in enumerate(h2):
                if title not in reserved:
                    first_theme = i
                    break
            feats["methods_before_themes"] = _bool(
                first_theme is not None and methods_i < first_theme
            )
        except ValueError:
            feats["methods_before_themes"] = 0.0
    outside = ca.text_outside_methods(text)
    proc = 0.0
    for pat in ca.ACQUISITION:
        if re.search(pat, outside, re.I):
            proc = 1.0
            break
    feats["process_outside_methods"] = proc
    all_sents = ca.prose_sentences(body)
    if all_sents:
        short = sum(1 for s in all_sents if len(s.split()) < ca.MECH_SHORT_SENTENCE)
        feats["short_sentence_frac"] = short / len(all_sents)
    return feats


def extract_features(text: str) -> dict[str, float]:
    title = ca.article_title(text)
    abstract = ca.section_after(text, "Abstract")
    feats = {k: 0.0 for k in FEATURE_NAMES}
    feats.update(extract_front_features(title, abstract))
    feats.update(extract_full_features(text))
    return feats


def vectorize(feats: dict[str, float], names: list[str] | None = None) -> list[float]:
    names = names or FEATURE_NAMES
    return [float(feats.get(n, 0.0)) for n in names]


def features_to_dict(values: list[float], names: list[str] | None = None) -> dict[str, float]:
    names = names or FEATURE_NAMES
    return {n: float(v) for n, v in zip(names, values)}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--article", default="")
    p.add_argument("--title", default="")
    p.add_argument("--abstract", default="")
    p.add_argument("--front-only", action="store_true")
    args = p.parse_args(argv)
    if args.article:
        text = Path(args.article).read_text(encoding="utf-8")
        feats = extract_features(text)
        if args.front_only:
            feats = {k: feats[k] for k in FRONT_FEATURES}
    elif args.title or args.abstract:
        feats = extract_front_features(args.title, args.abstract)
    else:
        print("need --article or --title/--abstract", file=sys.stderr)
        return 2
    print(json.dumps(feats, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
