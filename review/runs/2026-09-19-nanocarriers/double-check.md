# Double-check — 2026-09-19-nanocarriers

Second look after rewriting `article.md` for structure and Introduction. Pass 1 kept as `article-pass1.md`. Pass 2 is `article.md`.

## Scripts

- `check_extraction.py --notes-dir review/runs/2026-09-19-nanocarriers/notes --screening review/runs/2026-09-19-nanocarriers/screening.json`: **19/19 included notes claim-ready** (unchanged).
- `check_article.py --article …/article.md --table …/table/literature-table.md`: **exit 0**. Body before References is 6176 words.

## Notes still stub?

No (0/19).

## Table still DRAFT/lead-paste?

No. Same 19-row table from Claim-ready facts.

## Claims spot-checked (paper, number, note/PDF agree?)

Unchanged from the pass-1 log; pass 2 reuses the same numbers:

- Lutta 2025: 965 ± 178 nm; ~220 nm uncoated; ratio 0.7 / FRR 2:1. Note and `Lutta2025_pectin.txt` agree.
- Muenraya 2022: 11.55 ± 0.93% loading; free colistin MIC 1 µg/mL; 11.61 ± 0.84% hemolysis at 32 µg/mL. Note and `Muenraya2022_colistin.txt` agree.
- Valkova 2025: VRE 13.5 / 512 / 3.38+2 mg L−1, FIC 0.25. Note and PDF Table 1 agree.
- Nunes 2022: 60.4% growth inhibition; ~140 nm; n=7/group. Note and `Nunes2022_140272.txt` agree.
- Chauhan 2020: 154.10 nm; 69.46% ± 1. Note and `Chauhan2020_sertraline.txt` agree.
- Aloss 2023: 50 mg/m2; HEAT missed PFS; ≥45 min subgroup; phase I n=24. Note and `Makwana2023_030893.txt` agree.
- Azimzadeh 2025: colistin MIC 8–128 µg/mL; AgNP 0.07–37.5; IC50 75 µg/mL. Note and PDF extract agree.

No number was invented.

## Abstract: citations? named papers?

No `[n]`. No *et al.*. Topic map: emptying problem, PEG vs pH trigger, AgNPs as a different tactic, nasal inlet, HEAT miss. Abbreviations in the Abstract: PEG and AgNPs only, each reused.

## Abbreviations

PEG, EPR, DOPE, CHEMS, MIC, AgNPs, FIC, LTLD, AINI introduced in teaching sentences, then shortened. Headings stay expanded.

## Tables in article

- Table 2 (review maps) in §3, pointed from Methods and §3.
- Table 1 (experimental) in §4, pointed from Methods and §4.
- Table 3 (antimicrobial metrics) in §7.
- Discussion points back to Table 1 and Table 2.

## Discussion

Interprets knobs (PEG vs heat vs coat vs FIC vs inlet). No fetch-log, PRISMA, or token meters. Polymersome full text treated as an unmeasured comparison, not as findings.

## What pass 2 changed

Pass 1 taught lipid physics early, then used a generic Results heading and many fragment subsections (pH definitions, calcein vs doxorubicin, charge signs) after the story had already jumped. Pass 2 opens on the clinical packaging problem, teaches compartments and cues before DOPE shape, then walks trigger → PEG/acid → HEAT → coats → AgNPs → mucosa in numbered thematic sections.

## Ranks (1–5)

| Criterion | Pass 1 | Pass 2 |
|---|---|---|
| Abstract (topic map, no citations) | 4 | 5 |
| Introduction (teaches later sections) | 2 | 5 |
| In-article tables | 5 | 5 |
| Traceability (notes → table → article) | 5 | 5 |
| Discussion (scientific, no process talk) | 4 | 5 |
| Story / section architecture | 2 | 5 |
| Completeness of the sample | 5 | 5 |
| **Mean** | **3.9** | **5.0** |

**Deliverable:** pass 2 (`article.md`). Pass 1 remains as `article-pass1.md`.
