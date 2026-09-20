# Form notes (style only) — 2026-09-20 OA review sample

This run is **not** a scientific review of the 2,000 Scopus records. It is a craft study: titles, manuscript spine, headings, and how sentences join. **Copy form only.** Do not import findings, doses, diseases, or quotes from these papers into any other `article.md`.

## What was sampled

- Source: Scopus Review + open-access export, 20 September 2026 (`identification.bib`, ~2,000 records).
- Plan: stratified draw across journals/titles, then a small OA fetch; stop if the pattern is stable.
- Fetched batch 1: 40 public full texts (`batch1.json`). Usable reviews: 39. **Caselli 2026 was skipped** — the retrieved file was not that paper.
- Confirmation batch 2: 50 further records, stratified across fields (`review/runs/2026-09-20-style-study-batch2/`). **47 public full texts** were opened. Three DOIs had no public PDF (Di Cosimo 2026; Rukmindar 2026; Li 2026) and were not used. Pattern held: **42/50 titles use a colon**; median ~14 words; opening prose used anaphora/contrast (`this`, `yet`, `however`) and **not** First/Second or (i)/(ii). A few journals still print “comprehensive review” in the title; this workflow still bans that as an LLM default. No extra fetch after batch 2.

Full texts stay local and gitignored. These notes do not reproduce article bodies.

## Titles (batch 1 = 40 records; batch 2 = 50 titles)

Most titles use a **colon** (34/40 then 42/50). Typical length is about 14–15 words (range about 6–28). The left side names the object; the right side names the kind or the angle.

Shapes that recur:

- `Phenomenon: a narrative review of <map>` (diet indices; bile-duct access; tobacco policy).
- `Phenomenon: how / implications for / a framework for …`
- `X as a <role> in A, B, and C`
- `From A to B: a conceptual framework for …`
- Kind in the subtitle (`narrative review`, `systematic review`, `scoping review`), not as a slogan wrapper.

Rare: a short question after a colon. Weak: `A Review of X` with no angle; `Recent Advances` / `Comprehensive Overview` (LLM habit, uncommon in this sample).

## Manuscript spine

Two families, chosen by **kind**:

**Narrative / physiology (majority here).** Title → Abstract → Keywords → optional Highlights → Introduction that teaches → brief Methods (sometimes titled scope/evidence selection) → numbered thematic sections with nested 3.1 / 3.1.1 → Discussion (known vs inferential) → optional Limitations → Conclusions / perspectives. Headings are topics, mechanisms, or questions (`Why do identical meals produce different glucose responses?`, `Evidence map: what is known and what remains inferential`). Not `Results` as a catalogue. Not `Overview of included papers`.

**Systematic / scoping.** Structured abstract. IMRaD Methods (eligibility, selection, extraction, quality) → Results (flow, characteristics, then the scientific split) → Discussion with principal interpretation, comparison with previous reviews, strengths and limitations.

This workflow keeps Methods **before** the science when a bibliographic export was screened, even if a few journals bury the search.

## Joinery

Abstracts open on the phenomenon, then a tension (`yet`, `however`), then organisation around that tension, then a rank of evidence, then what the rank does not imply. Introductions stay on one problem; the next sentence is a consequence or limit (`this`, `these`, `that`). Conclusions restate the calibrated claim and name the next measurement as ordinary sentences.

Do not spine Abstract or Conclusions with *First, Second, Third* or *(i)(ii)(iii)*.

## Encoded where

- `.cursor/skills/review-prose/SKILL.md` — Title, Keywords, Key Summary Points, Headings, Continuous prose
- `scripts/check_article.py` — title, keywords, front-matter order, process headings, ordinal scaffold
- `AGENTS.md`, `report-writing`, `article-qa`, `double-check`, literature-review agent

The HPP manuscript uses a colon title, Keywords, Key Summary Points, nested thematic headings, and continuous Abstract/Discussion/Conclusions. Science in that article comes only from the HPP notes and table, not from the style-study papers.
