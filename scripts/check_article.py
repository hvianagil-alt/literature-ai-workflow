#!/usr/bin/env python3
"""Fail a journal-review draft that would not survive a first-pass referee.

Run this after writing article.md. Exit 0 only if the draft is deliverable.
Do not tell the user the article is done while this script fails.

Usage:
    python3 scripts/check_article.py --article review/runs/<id>/article.md \\
        --table review/runs/<id>/table/literature-table.md
    python3 scripts/check_article.py --article path.md --short

Fails when the body has no Markdown pipe table or no in-text "Table N" callout.
Fails when the Abstract contains a numbered citation ([n]) or "et al."
Fails when ``--table`` still looks like a ``write_table.py`` DRAFT (lead paste).
Fails when a defined abbreviation is still followed by many leftover expanded forms.
Fails when the Abstract defines more than four abbreviations, or defines one it never uses again.
Fails a narrative spine that dumps science under a generic Results heading, or an
Introduction too short to teach an adjacent-field reader (pass-1 failure mode).
Fails when the Abstract or any section other than Methods describes how papers
were found or opened (Scopus, open full texts, year windows of the export,
Unpaywall, paywalls). Those facts belong only in Methods.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ACQUISITION = [
    r"\bscopus\b",
    r"\bbibtex\b",
    r"\bunpaywall\b",
    r"\bopenalex\b",
    r"\beurope pmc\b",
    r"open full texts?",
    r"\bopen access\b",
    r"open-access",
    r"without a subscription",
    r"public full texts?",
    r"\bgap-fill\b",
    r"\bgap fill\b",
    r"title screening",
    r"bibliographic records",
    r"database export",
    r"\bthis export\b",
    r"full texts? from",
    r"could not be opened",
    r"not retrieved",
    r"sought for retrieval",
    r"\bfetch-log\b",
    r"public files were",
    r"\bpaywall",
    r"\boa export\b",
    r"user-supplied seeds",
    r"pdfs we could",
]

ABSTRACT_ACQUISITION = ACQUISITION + [
    r"20\d{2}\s*[–\-]\s*20\d{2}",
    r"\bfull texts?\b",
    r"\bwe searched\b",
    r"\brecords were\b",
    r"\bincluded \(n\s*=",
]

PROCESS = [
    r"\bunpaywall\b",
    r"\boa export\b",
    r"\btoken estimate\b",
    r"\busage-log\b",
    r"\bextracted lead\b",
    r"\bin this set\b",
    r"pdfs we could",
    r"this introduction is that map",
    r"the paper's job",
    r"extracts used here",
    r"mechanical first-pass",
    r"\bhttp_calls\b",
    r"est_input_tokens",
    r"\buser-supplied\b",
    r"papers in this sample were assembled",
]

FLOURISH = [
    r"stands as a testament",
    r"evolving landscape",
    r"rich tapestry",
    r"\bdelve\b",
    r"indelible mark",
    r"setting the stage",
]

INTRO_BAD_OPENERS = (
    "this review discusses",
    "this review aims",
    "this paper reviews",
    "in recent years",
    "in today's world",
    "it is well known that",
)

REQUIRED_HEADINGS = ("abstract", "introduction", "discussion", "conclusions", "references")
RESERVED_H2 = {
    "abstract",
    "keywords",
    "introduction",
    "methods",
    "discussion",
    "conclusions",
    "references",
    "key summary points",
    "highlights",
}
RESULTS_H2 = re.compile(r"^(?:\d+\.\s+)?results$", re.I)
AIM_RE = re.compile(
    r"\b(aim of this review|central argument of this review|this review is to)\b",
    re.I,
)
INTRO_MIN_WORDS_FULL = 400
INTRO_MIN_WORDS_SHORT = 40
INTRO_MIN_PARAS_FULL = 5
INTRO_MIN_PARAS_SHORT = 3
THEMATIC_H2_FULL = 3
THEMATIC_H2_SHORT = 2
H3_OUTSIDE_METHODS_MAX_FULL = 8

TABLE_CALLOUT = re.compile(r"\bTable\s+\d+\b", re.I)
TABLE_ROW = re.compile(r"^\s*\|.+\|\s*$")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
TABLE_STUB = (
    "mechanical first-pass",
    "extracted lead",
    "first-pass from extracted pdf",
    "not the final table",
    "literature table — draft",
    "not stated in extracted lead",
)


def body_before_references(text: str) -> str:
    parts = re.split(r"^##\s+References\s*$", text, maxsplit=1, flags=re.I | re.M)
    return parts[0]


def references_section(text: str) -> str:
    parts = re.split(r"^##\s+References\s*$", text, maxsplit=1, flags=re.I | re.M)
    return parts[1] if len(parts) > 1 else ""


CITE_BRACKET = re.compile(r"\[(\d+(?:\s*[,;]\s*\d+|\s*[–—−\-]\s*\d+)*)\]")
REF_START = re.compile(r"^\[(\d+)\]\s+|^(\d+)\.\s+", re.M)


def expand_cite_inner(inner: str) -> list[int]:
    nums: list[int] = []
    for part in re.split(r"[,;]", inner):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"(\d+)\s*[–—−\-]\s*(\d+)$", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            step = 1 if b >= a else -1
            nums.extend(range(a, b + step, step))
        elif part.isdigit():
            nums.append(int(part))
    return nums


def citation_scan_text(text: str) -> str:
    """Body citations only: skip Abstract/Keywords so numbering starts in the article."""
    body = body_before_references(text)
    for heading in ("Abstract", "Keywords"):
        span = section_span(body, heading)
        if span:
            body = body[: span[0]] + "\n" + body[span[1] :]
    return body


def first_appearance_numbers(text: str) -> list[int]:
    seen: list[int] = []
    for m in CITE_BRACKET.finditer(citation_scan_text(text)):
        for n in expand_cite_inner(m.group(1)):
            if n not in seen:
                seen.append(n)
    return seen


def parse_reference_entries(ref_text: str) -> dict[int, str]:
    starts = list(REF_START.finditer(ref_text))
    entries: dict[int, str] = {}
    for i, m in enumerate(starts):
        num = int(m.group(1) or m.group(2))
        end = starts[i + 1].start() if i + 1 < len(starts) else len(ref_text)
        body = re.sub(r"\s+", " ", ref_text[m.end() : end].strip())
        entries[num] = body
    return entries


def references_paragraph_separated(ref_text: str) -> bool:
    starts = list(REF_START.finditer(ref_text))
    if len(starts) < 2:
        return True
    for i in range(len(starts) - 1):
        between = ref_text[starts[i].end() : starts[i + 1].start()]
        if "\n\n" not in between:
            return False
    return True


def format_cite_cluster(nums: list[int]) -> str:
    compact: list[int] = []
    for n in nums:
        if n not in compact:
            compact.append(n)
    compact.sort()
    return "[" + ",".join(str(n) for n in compact) + "]"


def citation_order_problems(text: str) -> list[str]:
    problems: list[str] = []
    order = first_appearance_numbers(text)
    if not order:
        return problems
    if order != list(range(1, len(order) + 1)):
        problems.append(
            "numbered citations must follow first-appearance order "
            "(first cited paper is [1], next new paper is [2], …); "
            f"in-text first-appearance sequence is {order[:12]}"
            + ("…" if len(order) > 12 else "")
        )
    refs = parse_reference_entries(references_section(text))
    if not refs:
        problems.append("References list has no numbered entries matching in-text [n]")
        return problems
    expected_keys = list(range(1, len(order) + 1))
    actual_keys = sorted(refs)
    if actual_keys != expected_keys:
        problems.append(
            "References numbering must be [1]…[n] in first-appearance order "
            f"(cited n={len(order)}, listed n={len(refs)})"
        )
    unused = sorted(set(refs) - set(order))
    missing = sorted(set(order) - set(refs))
    if missing:
        problems.append("in-text citations with no References entry: " + ",".join(map(str, missing[:12])))
    if unused:
        problems.append("References never cited in the body: " + ",".join(map(str, unused[:12])))
    if not references_paragraph_separated(references_section(text)):
        problems.append(
            "each References entry must be its own paragraph (blank line between [n] items)"
        )
    return problems


def _replace_cites_outside_abstract(front: str, repl) -> str:
    spans: list[tuple[int, int]] = []
    for heading in ("Abstract", "Keywords"):
        span = section_span(front, heading)
        if span:
            spans.append(span)
    spans.sort()
    if not spans:
        return CITE_BRACKET.sub(repl, front)
    out: list[str] = []
    pos = 0
    for start, end in spans:
        out.append(CITE_BRACKET.sub(repl, front[pos:start]))
        out.append(front[start:end])
        pos = end
    out.append(CITE_BRACKET.sub(repl, front[pos:]))
    return "".join(out)


def renumber_vancouver(text: str) -> str:
    """Rewrite [n] and the References list into first-appearance Vancouver order."""
    parts = re.split(r"^(##\s+References\s*)$", text, maxsplit=1, flags=re.I | re.M)
    front = parts[0]
    heading = parts[1] if len(parts) > 1 else "## References"
    ref_text = parts[2] if len(parts) > 2 else ""
    old_order = first_appearance_numbers(text)
    if not old_order:
        return text
    mapping = {old: i for i, old in enumerate(old_order, start=1)}
    refs = parse_reference_entries(ref_text)

    def replace_cluster(m: re.Match[str]) -> str:
        nums = [mapping.get(n, n) for n in expand_cite_inner(m.group(1))]
        return format_cite_cluster(nums)

    new_front = _replace_cites_outside_abstract(front, replace_cluster)
    lines = []
    for i, old in enumerate(old_order, start=1):
        entry = refs.get(old, "")
        if not entry:
            entry = f"(missing original reference [{old}])"
        lines.append(f"[{i}] {entry}")
    new_refs = "\n\n".join(lines)
    return new_front.rstrip() + "\n\n" + heading + "\n\n" + new_refs + "\n"


def section_after(text: str, heading: str) -> str:
    m = re.search(rf"^##\s+(?:\d+\.\s+)?{heading}\s*$", text, re.I | re.M)
    if not m:
        return ""
    rest = text[m.end() :]
    nxt = re.search(r"^##\s+", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def first_sentence(section: str) -> str:
    cleaned = re.sub(r"^#+\s+.*$", "", section, flags=re.M).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        return ""
    m = re.search(r"(.+?[.!?])\s", cleaned + " ")
    return (m.group(1) if m else cleaned[:240]).strip()


def heading_lines(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^#{1,4}\s+(.+)$", text, re.M)]


def h2_titles(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.M)]


def thematic_h2_titles(text: str) -> list[str]:
    out = []
    for raw in h2_titles(text):
        title = re.sub(r"^\d+\.\s+", "", raw).strip()
        if title.lower() in RESERVED_H2:
            continue
        out.append(title)
    return out


def intro_paragraphs(intro: str) -> list[str]:
    cleaned = re.sub(r"^#+\s+.*$", "", intro, flags=re.M).strip()
    return [p.strip() for p in re.split(r"\n\s*\n", cleaned) if p.strip()]


def section_span(text: str, heading: str) -> tuple[int, int] | None:
    m = re.search(rf"^##\s+(?:\d+\.\s+)?{heading}\s*$", text, re.I | re.M)
    if not m:
        return None
    nxt = re.search(r"^##\s+", text[m.end() :], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return m.start(), end


def h3_outside_methods(text: str) -> int:
    span = section_span(text, "Methods")
    n = 0
    for m in re.finditer(r"^###\s+", text, re.M):
        if span and span[0] <= m.start() < span[1]:
            continue
        n += 1
    return n


def story_problems(text: str, short: bool) -> list[str]:
    """Narrative reviews must teach, then argue in thematic sections — not dump Results."""
    problems: list[str] = []
    intro = section_after(text, "Introduction")
    words = intro.split()
    paras = intro_paragraphs(intro)
    min_words = INTRO_MIN_WORDS_SHORT if short else INTRO_MIN_WORDS_FULL
    min_paras = INTRO_MIN_PARAS_SHORT if short else INTRO_MIN_PARAS_FULL
    if len(words) < min_words:
        problems.append(
            f"Introduction word count {len(words)} < {min_words} "
            "(teach the field so an adjacent-field reader can follow later sections; "
            "see review-prose, Introduction)"
        )
    if len(paras) < min_paras:
        problems.append(
            f"Introduction has {len(paras)} paragraphs; need at least {min_paras} "
            "(phenomenon, background, why current options fail, controversy, aim last)"
        )
    if paras and not AIM_RE.search(paras[-1]):
        problems.append(
            "Introduction last paragraph must state the aim or central argument "
            "('The aim of this review is' / 'The central argument of this review is')"
        )
    for raw in h2_titles(text):
        title = re.sub(r"^\d+\.\s+", "", raw).strip()
        if RESULTS_H2.match(title):
            problems.append(
                "generic Results heading; use numbered thematic sections from "
                "synthesis-rationale (e), not a Results dump (see review-prose, "
                "Match the spine)"
            )
            break
    need = THEMATIC_H2_SHORT if short else THEMATIC_H2_FULL
    thematic = thematic_h2_titles(text)
    if len(thematic) < need:
        problems.append(
            f"{len(thematic)} thematic ## sections; need at least {need} "
            "topic/argument headings between Methods and Discussion"
        )
    if not short:
        n_h3 = h3_outside_methods(text)
        if n_h3 > H3_OUTSIDE_METHODS_MAX_FULL:
            problems.append(
                f"{n_h3} ### headings outside Methods (max {H3_OUTSIDE_METHODS_MAX_FULL}); "
                "fold fragment subsections into the numbered thematic story"
            )
    lowered_intro = intro.lower()
    if "user-supplied" in lowered_intro or "were assembled from" in lowered_intro:
        problems.append(
            "Introduction contains intake/process talk; teach the field, not how papers were gathered"
        )
    return problems


def et_al_openers(text: str) -> int:
    n = 0
    for para in re.split(r"\n\s*\n", text):
        line = para.strip().split("\n", 1)[0].strip()
        if re.match(r"^[A-Z][A-Za-z\-]+ et al\.", line):
            n += 1
    return n


def has_markdown_table(text: str) -> bool:
    """True if the text contains a GitHub-flavoured Markdown table (header, sep, row)."""
    lines = text.splitlines()
    for i in range(len(lines) - 2):
        if (
            TABLE_ROW.match(lines[i])
            and TABLE_SEP.match(lines[i + 1])
            and TABLE_ROW.match(lines[i + 2])
        ):
            return True
    return False


SKIP_WORDS = {"and", "or", "of", "the", "in", "a", "an", "to", "for", "with"}
TOKEN_RE = re.compile(r"[A-Za-z][-A-Za-z0-9]*|[0-9]+")
ABBR_PAREN = re.compile(
    r"\(([A-Z][A-Z0-9]{1,6}(?:[- ][A-Z0-9][A-Z0-9]{0,6}){0,2}s?)\)"
)


def _initials_from(tokens: list[str]) -> str:
    sig = [t for t in tokens if t.lower() not in SKIP_WORDS]
    return "".join(t[0].upper() if t[0].isalpha() else t for t in sig)


def _sig_tokens(full: str) -> list[str]:
    return [t for t in re.findall(r"[A-Za-z0-9]+", full) if t.lower() not in SKIP_WORDS]


def _initials_variants(full: str) -> set[str]:
    """Hyphenated compounds count as one token or as split words (GLP-1 vs GIP)."""
    kept = [t for t in TOKEN_RE.findall(full) if t.lower() not in SKIP_WORDS]
    split = _sig_tokens(full)
    return {_initials_from(kept), _initials_from(split)}


def looks_like_sigla(full: str, abbr: str) -> bool:
    """True if ABBR is a conventional short form of the expanded phrase."""
    abbr_n = re.sub(r"[^A-Z0-9]", "", abbr.upper())
    if len(abbr_n) < 2 or len(abbr_n) > 8:
        return False
    variants = _initials_variants(full)
    if abbr_n in variants:
        return True
    sig = _sig_tokens(full)
    if len(sig) >= 2:
        first = sig[0][0].upper() if sig[0][0].isalpha() else ""
        tail = "".join(t[0].upper() for t in sig[-2:] if t[0].isalpha())
        if first and tail and abbr_n.startswith(first) and abbr_n.endswith(tail):
            return True
    return False


def expansion_for_abbr(before: str, abbr: str) -> str | None:
    """Right-aligned phrase immediately before ``(ABBR)``, not a longer clause."""
    cut = before.rfind(")")
    if cut != -1:
        before = before[cut + 1 :]
    window = before[-160:]
    tokens = list(TOKEN_RE.finditer(window))[-8:]
    if not tokens:
        return None
    exact = None
    tail = None
    abbr_n = re.sub(r"[^A-Z0-9]", "", abbr.upper())
    for n in range(1, len(tokens) + 1):
        full = window[tokens[-n].start() :].strip().rstrip(" ,;:")
        if "(" in full or not looks_like_sigla(full, abbr):
            continue
        if abbr_n in _initials_variants(full):
            if exact is None:
                exact = full
        elif n <= 4:
            tail = full
    return exact or tail


def leftover_expanded_terms(body: str) -> list[str]:
    """After 'Full term (ABBR)', the long form should not keep flooding the prose."""
    problems: list[str] = []
    seen: set[str] = set()
    for m in ABBR_PAREN.finditer(body):
        abbr = m.group(1).strip()
        full = expansion_for_abbr(body[: m.start()].rstrip(), abbr)
        if not full:
            continue
        key = (full.lower(), abbr.upper())
        if key in seen:
            continue
        seen.add(key)
        leftover = 0
        after = body[m.end() :]
        for line in after.splitlines():
            if re.match(r"^#{1,4}\s", line):
                continue
            leftover += len(
                re.findall(rf"{re.escape(full)}(?![A-Za-z])", line, re.I)
            )
        if leftover >= 4:
            problems.append(
                f"after defining {abbr}, '{full}' still appears {leftover} times; "
                "use the abbreviation (see review-prose, Abbreviations)"
            )
    return problems


ABSTRACT_ABBR_MAX = 4


def abstract_sigla_problems(abstract: str) -> list[str]:
    """A first-time reader should not need a glossary to finish the Abstract."""
    problems: list[str] = []
    defined: list[tuple[str, int]] = []
    for m in ABBR_PAREN.finditer(abstract):
        abbr = m.group(1).strip()
        full = expansion_for_abbr(abstract[: m.start()].rstrip(), abbr)
        if not full:
            continue
        defined.append((abbr, m.end()))
    if len(defined) > ABSTRACT_ABBR_MAX:
        problems.append(
            f"Abstract defines {len(defined)} abbreviations; "
            f"a first-time reader cannot hold that many (max {ABSTRACT_ABBR_MAX}; "
            "see review-prose, Abbreviations)"
        )
    for abbr, end in defined:
        after = abstract[end:]
        n = len(re.findall(rf"\b{re.escape(abbr)}s?\b", after))
        if n == 0:
            problems.append(
                f"Abstract defines {abbr} but never uses it again; "
                "write the term out in the Abstract (see review-prose)"
            )
    return problems


def papers_from_table(table_md: str) -> list[tuple[str, str]]:
    papers: list[tuple[str, str]] = []
    for line in table_md.splitlines():
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s:\-|]+\|$", line.replace(" ", "")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0].lower() in {"paper", "-----"}:
            continue
        if "research question" in cells[0].lower():
            continue
        raw = re.sub(r"\*+", "", cells[0])
        m = re.match(r"(?:Fictional\s+)?(.+?)[,\s]+(\d{4})\b", raw)
        if not m:
            continue
        name = m.group(1).strip().rstrip(",")
        year = m.group(2)
        surname = name.split()[-1]
        papers.append((surname, year))
    return papers


def text_outside_methods(text: str) -> str:
    """Everything before References except the Methods section."""
    body = body_before_references(text)
    span = section_span(body, "Methods")
    if not span:
        return body
    return body[: span[0]] + "\n" + body[span[1] :]


def acquisition_outside_methods_problems(text: str) -> list[str]:
    """How the papers were found or opened belongs only in Methods."""
    problems: list[str] = []
    abstract = section_after(text, "Abstract")
    for pat in ABSTRACT_ACQUISITION:
        if re.search(pat, abstract, re.I):
            problems.append(
                f"Abstract describes how papers were acquired ({pat}); "
                "put search, dates, and open full texts only in Methods"
            )
            break
    outside = text_outside_methods(text)
    for heading in ("Abstract", "Keywords"):
        span = section_span(outside, heading)
        if span:
            outside = outside[: span[0]] + "\n" + outside[span[1] :]
    for pat in ACQUISITION:
        if re.search(pat, outside, re.I):
            problems.append(
                f"search/retrieval language outside Methods ({pat}); "
                "Scopus, OA, paywalls, and screening counts belong only in Methods"
            )
            break
    return problems


def check(text: str, table: str | None, short: bool) -> list[str]:
    problems: list[str] = []
    lowered = text.lower()
    body = body_before_references(text)
    for h in REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+(?:\d+\.\s+)?{h}\s*$", text, re.I | re.M):
            problems.append(f"missing heading: {h}")
    words = body.split()
    if not short and len(words) < 6000:
        problems.append(f"body word count {len(words)} < 6000 (use --short only if the user asked for a short note)")
    for pat in PROCESS + FLOURISH:
        if re.search(pat, body, re.I):
            problems.append(f"banned phrase: {pat}")
    if re.search(r"^Additionally,", body, re.M):
        problems.append("sentence opener Additionally,")
    intro = section_after(text, "Introduction")
    opener = first_sentence(intro).lower()
    for bad in INTRO_BAD_OPENERS:
        if opener.startswith(bad):
            problems.append(f"Introduction opens with '{bad}'")
    for h in heading_lines(text):
        if re.search(r"\bet al\.", h, re.I) or re.match(r"paper\s+\d+", h, re.I):
            problems.append(f"heading names a paper: {h}")
    results = body
    for stop in ("Discussion", "Conclusions"):
        chunk = section_after(text, stop)
        if chunk:
            results = results.replace(chunk, "")
    intro_full = section_after(text, "Introduction")
    methods = section_after(text, "Methods")
    results = results.replace(intro_full, "").replace(methods, "")
    n_open = et_al_openers(results)
    if n_open >= 4:
        problems.append(f"{n_open} results paragraphs open with 'Author et al.' (max 3)")
    if table:
        lowered_table = table.lower()
        for marker in TABLE_STUB:
            if marker in lowered_table:
                problems.append(
                    f"literature table still looks like a DRAFT (found '{marker}'); "
                    "rewrite from Claim-ready facts (scripts/table_from_notes.py)"
                )
                break
        missing = []
        for surname, year in papers_from_table(table):
            if surname not in text or year not in text:
                missing.append(f"{surname} {year}")
        if missing:
            problems.append("included papers not named in article: " + ", ".join(missing[:12]))
            if len(missing) > 12:
                problems.append(f"...and {len(missing) - 12} more")
    disc = section_after(text, "Discussion") + "\n" + section_after(text, "Conclusions")
    for pat in (r"\bprisma\.md\b", r"\bfetch-log\b", r"\bnot retrieved\b"):
        if re.search(pat, disc, re.I):
            problems.append(f"Discussion/Conclusions contains process talk: {pat}")
    if not has_markdown_table(body):
        problems.append(
            "missing Markdown results table (put a |header| table in the article body)"
        )
    if not TABLE_CALLOUT.search(body):
        problems.append(
            "missing in-text Table N callout (e.g. 'Table 1 summarises…')"
        )
    abstract = section_after(text, "Abstract")
    if re.search(r"\[\d+\]", abstract):
        problems.append("Abstract contains a citation ([n]); narrative abstracts do not cite")
    if re.search(r"\bet al\.", abstract, re.I):
        problems.append("Abstract names a paper (et al.)")
    problems.extend(abstract_sigla_problems(abstract))
    problems.extend(leftover_expanded_terms(body))
    problems.extend(story_problems(text, short))
    problems.extend(citation_order_problems(text))
    problems.extend(acquisition_outside_methods_problems(text))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article", required=True)
    parser.add_argument("--table", default="")
    parser.add_argument(
        "--short",
        action="store_true",
        help="skip the 6,000-word floor (only if the user asked for a short note)",
    )
    args = parser.parse_args()
    path = Path(args.article)
    if not path.is_file():
        print(f"FAIL article missing: {path}", file=sys.stderr)
        return 2
    table = Path(args.table).read_text(encoding="utf-8") if args.table else None
    problems = check(path.read_text(encoding="utf-8"), table, args.short)
    if problems:
        print("FAIL article is not deliverable:")
        for p in problems:
            print(f"  - {p}")
        print(
            "Rewrite before telling the user it is done. See review-prose and report-writing.",
            file=sys.stderr,
        )
        return 1
    print(f"OK {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
