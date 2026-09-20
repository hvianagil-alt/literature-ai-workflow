#!/usr/bin/env python3
"""Measurable writing-craft features for a narrative review.

These are form-only proxies distilled from published guides (Pautasso 2013;
Gopen & Swan 1990; Swales CARS; SANRA; Snyder 2019) and from same-field
published reviews (for example Houška 2022 and Zhang 2022 in *Foods*).
They do not import scientific findings into a manuscript.
"""

from __future__ import annotations

import re
from pathlib import Path

META_REVIEWER = [
    r"\bthis sample\b",
    r"\bin this set\b",
    r"\bincluded evidence jointly\b",
    r"\bintellectual model\b",
    r"\bnamed cycle is not one\b",
    r"\bthe literature table\b",
    r"\bclaim-ready\b",
    r"\bharness\b",
]

THESIS_SLOGANS = [
    r"named cycle is not one outcome",
    r"the same megapascal number is not",
    r"a labelled hydrostatic cycle is",
]

CARS_NICHE = re.compile(
    r"\b(however|yet|although|gap|unresolved|poorly mapped|"
    r"live controversy|still fail|does not inactivate|"
    r"there is a need|remains unsettled|not interchangeable)\b",
    re.I,
)

AIM_RE = re.compile(
    r"(the aim of this review|the central argument of this review|"
    r"this review is divided|this paper is an initiative|"
    r"the aim of this paper)",
    re.I,
)

SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9*])")
MD_H3 = re.compile(r"^###\s+(?!(?:\d+\.\d+\s+)?(?:Search|Eligibility|Study selection|Sources)\b)", re.I | re.M)
MD_H3_ANY = re.compile(r"^###\s+", re.M)
MD_METHODS = re.compile(r"^##\s+(?:\d+\.\s+)?Methods\s*$", re.I | re.M)
NUMBERED_SUB = re.compile(r"(?m)^\s*(\d+)\.(\d+)(?:\.\d+)?\.?\s+[A-Z]")
AUTHOR_OPEN = re.compile(
    r"(?m)^(?:[-*]\s+)?[A-Z][A-Za-z\-]+(?:\s+[A-Z][a-z]+)?(?:\s+et al)?\.?\s+(?:19|20)\d{2}\b"
)
SINGLE_CITE = re.compile(r"\[(\d+)\]")
MULTI_CITE = re.compile(r"\[\d+\s*[,;–—-]")
SYNTH_CLOSE = re.compile(
    r"\b(taken together|concluding remarks|these data suggest|"
    r"in summary|overall,|the practical implication|"
    r"this section cannot show|what cannot currently)\b",
    re.I,
)
MD_H2 = re.compile(r"(?im)^(?:##\s+(?:\d+\.\s+)?|\s*\d+\.\s+)(.+?)\s*$")


def body_before_references(text: str) -> str:
    parts = re.split(r"(?im)^(?:##\s+)?References\s*$", text, maxsplit=1)
    return parts[0]


def section_after(text: str, heading: str) -> str:
    m = re.search(rf"(?im)^(?:##\s+(?:\d+\.\s+)?)?{re.escape(heading)}\s*$", text)
    if not m:
        # PMC/plaintext reviews often use "1. Introduction"
        m = re.search(rf"(?im)^\s*\d+\.\s+{re.escape(heading)}\s*$", text)
    if not m:
        return ""
    rest = text[m.end() :]
    nxt = re.search(r"(?im)^(?:##\s+|\s*\d+\.\s+)[^\n]+$", rest)
    return rest[: nxt.start()] if nxt else rest


def sentences(text: str) -> list[str]:
    chunk = re.sub(r"\s+", " ", text).strip()
    if not chunk:
        return []
    return [s.strip() for s in SENTENCE_RE.split(chunk) if s.strip()]


def mean_sentence_words(text: str) -> float:
    sents = sentences(text)
    if not sents:
        return 0.0
    return sum(len(s.split()) for s in sents) / len(sents)


def nested_thematic_count(text: str) -> int:
    """Count 3.1-style nests that are not Methods 2.1 Search/Eligibility."""
    md = 0
    methods_span = None
    m = MD_METHODS.search(text)
    if m:
        nxt = re.search(r"^##\s+", text[m.end() :], re.M)
        methods_span = (m.start(), m.end() + (nxt.start() if nxt else len(text) - m.end()))
    for hit in MD_H3_ANY.finditer(text):
        if methods_span and methods_span[0] <= hit.start() < methods_span[1]:
            continue
        md += 1
    numbered = 0
    for hit in NUMBERED_SUB.finditer(text):
        major, minor = hit.group(1), hit.group(2)
        heading_line = text[hit.start() : text.find("\n", hit.start())]
        if re.search(r"Search|Eligibility|Study selection|Sources", heading_line, re.I):
            continue
        if major == "2" and re.search(r"Method", text[max(0, hit.start() - 400) : hit.start()], re.I):
            continue
        numbered += 1
    return max(md, numbered)


def meta_hits(text: str) -> int:
    body = body_before_references(text)
    # Methods may mention the sample; strip a Methods block if present.
    methods = section_after(body, "Methods")
    if methods:
        body = body.replace(methods, "\n")
    n = 0
    for pat in META_REVIEWER:
        n += len(re.findall(pat, body, re.I))
    return n


def slogan_hits(text: str) -> int:
    body = body_before_references(text).lower()
    n = 0
    for pat in THESIS_SLOGANS:
        n += len(re.findall(pat, body))
    return n


def single_study_paragraphs(text: str) -> tuple[int, int]:
    """Paragraphs that look like one-paper file cards vs all body paragraphs."""
    body = body_before_references(text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if len(p.split()) >= 40]
    singles = 0
    for para in paras:
        cites = SINGLE_CITE.findall(para)
        if not cites:
            continue
        unique = set(cites)
        if len(unique) != 1:
            continue
        if MULTI_CITE.search(para):
            continue
        if re.search(r"\b(n\s*=|MPa|log CFU|P\s*<)\b", para):
            singles += 1
    return singles, len(paras)


def cars_has_niche_before_aim(text: str) -> bool:
    intro = section_after(text, "Introduction")
    if not intro:
        return False
    aim = AIM_RE.search(intro)
    head = intro[: aim.start()] if aim else intro
    return bool(CARS_NICHE.search(head))


def author_year_openers(text: str) -> int:
    body = body_before_references(text)
    return len(AUTHOR_OPEN.findall(body))


def thematic_synthesis_frac(text: str) -> float:
    """Share of thematic H2 sections whose last block synthesises."""
    body = body_before_references(text)
    hits = list(MD_H2.finditer(body))
    scored = 0
    closed = 0
    skip = re.compile(
        r"abstract|keywords|key summary|introduction|methods|references", re.I
    )
    for i, hit in enumerate(hits):
        title = hit.group(1)
        if skip.search(title):
            continue
        start = hit.end()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        chunk = body[start:end].strip()
        if len(chunk.split()) < 80:
            continue
        scored += 1
        last = chunk.strip().split("\n\n")[-1]
        heading_close = re.search(
            r"(?im)^\s*(?:#{2,3}\s+)?(?:\d+\.\d+\.?\s+)?concluding remarks\b",
            chunk,
        )
        if SYNTH_CLOSE.search(last) or SYNTH_CLOSE.search(title) or heading_close:
            closed += 1
    if scored == 0:
        return 0.0
    return closed / scored


def extract_craft_features(text: str) -> dict[str, float]:
    body = body_before_references(text)
    singles, paras = single_study_paragraphs(text)
    return {
        "nested_thematic_h3": float(nested_thematic_count(text)),
        "meta_reviewer_hits": float(meta_hits(text)),
        "slogan_hits": float(slogan_hits(text)),
        "single_study_paragraphs": float(singles),
        "body_paragraphs": float(paras),
        "single_study_frac": (singles / paras) if paras else 0.0,
        "intro_mean_sentence_words": mean_sentence_words(section_after(text, "Introduction")),
        "body_mean_sentence_words": mean_sentence_words(body),
        "cars_niche_before_aim": 1.0 if cars_has_niche_before_aim(text) else 0.0,
        "author_year_openers": float(author_year_openers(text)),
        "thematic_synthesis_frac": thematic_synthesis_frac(text),
        "body_words": float(len(body.split())),
    }


def extract_from_path(path: str | Path) -> dict[str, float]:
    return extract_craft_features(Path(path).read_text(encoding="utf-8", errors="replace"))
