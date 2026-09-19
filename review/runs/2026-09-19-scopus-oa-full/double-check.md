# Double-check — 2026-09-19-scopus-oa-full

Second look after `article-qa`. Same 44 included full texts (plus Pechenov 2021 gap-fill). Pass-1 manuscript kept as `article-pass1.md`. Pass-2 is `article.md`.

## Scripts

- `check_extraction.py --notes-dir review/runs/2026-09-19-scopus-oa-full/notes --screening …/screening.json`: **44/44 included notes claim-ready** (pass 1 was 0/44 stubs from `notes_from_text.py`).
- `check_article.py --article …/article.md --table …/table/literature-table.md`: pass 2 (see run log). Pass 1 would fail the Markdown-table and Table-N gates.

## Notes still stub?

No for included papers (0/44). Pass 1: yes (44/44 mechanical first-pass). Gap-fill `Pechenov2021-medi7219.md` now has Claim-ready facts (~6% dog oral-tablet bioavailability).

## Table still DRAFT/lead-paste?

No. Rewritten with `scripts/table_from_notes.py` (45 rows: 44 export + 1 gap-fill). Pass 1 pasted PDF leads and said “First-pass from extracted PDF text.”

## Claims spot-checked (paper, number, note/PDF agree?)

- Pasqua 2025: TIR +4.8 (SD 7.6) pp; 74.2% vs 69.4%; *P*=0.006; 28 randomised / 24 completers. Note and PDF (`Pasqua20251239.txt`) agree.
- Chen 2024: matched n=202; TIR 76.0% vs 65.7%; *p*<0.001. Note and PDF agree.
- Nielsen 2025: 222 / 201 / 123 in the three dose pairs; EMA/FDA/PMDA bioequivalence met. Note and PDF agree.
- Ma 2024: fed AUC/Cmax 23.7%/23.2% lower (3 mg) and 17.6%/20.9% lower (16 mg). Note and PDF agree.
- Sillassen 2025: 50 trials; 54,972 randomised; mortality RR 0.85 (0.79–0.91); MI RR 0.77 (0.69–0.85); nausea RR 3.00. Note and PDF agree.
- Jeong 2026: ZO-3 relative BA ~60% healthy rats, ~51% diabetic rats. Note and PDF agree.
- Woo 2025: 0.37 ± 0.020 N/needle. Note and PDF agree.
- Khater 2026: 225.1 ± 19.6 nm; EE 73.5 ± 4.2%; n=8 per group. Note and PDF agree.
- Hirotsu 2025: 74 enrolled; 44 reached HbA1c <7%; 17 did not. Note and PDF agree.
- Pechenov 2021: ~6% oral-tablet bioavailability in dogs. Note and PDF (`Niu2021_oralglp1.txt`, which is this paper) agree.

No number was invented to resolve a mismatch. Several notes still mark n as not reported where the PDF extract used for the article did not state it.

## Abstract: citations? named papers?

No `[n]`. No *et al.*. No MEDI7219. Topic map with one unnamed hinge (AID time-in-range). Same as pass 1; that part already met the craft rule.

## Abbreviations

Repeated terms are `Full term (ABBR)` at first use in a teaching sentence, then the short form. The Abstract now keeps GLP-1 and GIP (which it reuses) and writes the rest in words so a first-time reader does not need a glossary. The body still shortens T2D, T1D, GLP-1 RA, AID, TIR, CGM, SC, BA, PK, GI, MSC, EV after those teaching sentences. Headings, keywords, and reference titles stay expanded.

## Tables in article

- Table 1 (human glycaemia / tablet PK / pooled safety) mentioned in §3 and Discussion.
- Table 2 (delivery) mentioned in §4 and Discussion.
- Table 3 (extra-glycaemic / vesicle) mentioned in §5 and Discussion.
- Pass 1 had none.

## What the re-run showed about the workflow

Working:

- Teaching Introduction, claim-first sentences, topic-map Abstract, scientific Discussion (pass 1 already).
- `check_article.py` Abstract and catalog-voice gates.
- Direction check + synthesis rationale + gap-fill (Pechenov) already in the run trail.

Not working on pass 1 (fixed for pass 2 and encoded):

- Notes were stubs while the article cited PDF numbers. Scripts did not run, or ran only on the article. **Fix:** step 8 requires `check_extraction.py`; step 9 double-check stops if notes are stubs.
- Literature table was a lead-paste DRAFT. **Fix:** `scripts/table_from_notes.py` plus `check_article.py --table` failing on DRAFT markers.
- No in-article Markdown tables. **Fix:** `check_article.py` table + Table-N gates (already encoded); this pass inserted Tables 1–3.

## Ranks (1–5)

| Criterion | Pass 1 | Pass 2 |
|---|---|---|
| Abstract (topic map, no citations) | 5 | 5 |
| In-article tables | 1 | 5 |
| Traceability (notes → table → article) | 2 | 5 |
| Discussion (scientific, no process talk) | 5 | 5 |
| Completeness of the sample | 4 | 5 |
| **Mean** | **3.4** | **5.0** |

**Deliverable:** pass 2 (`article.md`). Pass 1 remains as `article-pass1.md` for comparison. Pass 1 is still readable science; it is not a finished extraction trail.
