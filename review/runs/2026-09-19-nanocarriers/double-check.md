# Double-check — 2026-09-19-nanocarriers

Second look after `article-qa`. One manuscript (`article.md`); this is not a rewrite of a previous nanocarrier sample.

## Scripts

- `check_extraction.py --notes-dir review/runs/2026-09-19-nanocarriers/notes --screening review/runs/2026-09-19-nanocarriers/screening.json`: **19/19 included notes claim-ready** (exit 0).
- `check_article.py --article review/runs/2026-09-19-nanocarriers/article.md --table review/runs/2026-09-19-nanocarriers/table/literature-table.md`: **exit 0**. Body before References is 6018 words (floor is 6000). Earlier drafts failed only on that floor (5986, then 5997).

## Notes still stub?

No (0/19). Each included note has `## Claim-ready facts` without stub markers.

## Table still DRAFT/lead-paste?

No. `review/runs/2026-09-19-nanocarriers/table/literature-table.md` is rewritten from Claim-ready facts (19 rows). No “mechanical first-pass” / extracted-lead cells.

## Claims spot-checked (paper, number, note/PDF agree?)

- Lutta 2025: LM-pectin 965 ± 178 nm; uncoated ~220 nm; ratio 0.7 and flow 2:1. Note, Table 1 in the article, and `Lutta2025_pectin.txt` (Table 2 line “LM-pectin liposomes 965 ± 178”) agree.
- Muenraya 2022: F3 loading 11.55 ± 0.93%; free colistin MIC 1 µg/mL. Note, article, and `Muenraya2022_colistin.txt` (Abstract and Results) agree. The article’s caution that conjugation does not beat free colistin on MIC is the same comparison as the PDF.
- Valkova 2025: VRE AgNP MIC 13.5 mg L−1, vancomycin 512 mg L−1, combination 3.38 + 2 mg L−1, FIC 0.25. Note, article Table 1, and PDF Table 1 in `Valkova2025_vancomycin.txt` agree.
- Nunes 2022: Lip-DOX tumour-growth inhibition 60.4%; size ~140 nm / 139.4 ± 3.8 nm; EE >90% / 93.1 ± 1.2%; n=7/group. Note, article, and `Nunes2022_140272.txt` agree.
- Chauhan 2020 (AJP OA): 154.10 nm; 69.46% ± 1 entrapment. Note, article, and `Chauhan2020_sertraline.txt` agree. Group n remains unstated in the extract.
- Aloss 2023: LTLD 50 mg/m2 15 min before ablation; HEAT missed PFS; OS similar in the main analysis; ≥45 min ablation subgroup; phase I n=24. Note, article, and `Makwana2023_030893.txt` (HEAT paragraph) agree. Filename is a download tag; the paper is Aloss & Hamar, *Pharmaceutics* 2023.
- Azimzadeh 2025: colistin MIC 8–128 µg/mL (min 8, max 128 in the extract); AgNP MIC 0.07–37.5 µg/mL; L929 IC50 75 µg/mL; >50% viability at 37.5 µg/mL. Note, article, and `Azimzadeh2025_00056.txt` agree.
- Mahmoudzadeh 2021: cited calcein 55% / 24% / 10% at 0 / 0.6 / 3 mol% PEG-lipid, pH 5.5. Note and article both label these as **cited experiments**, not new MD output.

No number was invented to resolve a mismatch.

## Abstract: citations? named papers?

No `[n]`. No *et al.*. Topic map (emptying problem, PEG vs pH trigger, AgNP–antibiotic combinations, nasal inlet, HEAT miss, unread polymersome). Readable without a glossary: PEG, AgNP, and MIC are defined in words on first use.

## Abbreviations

PEG, AgNP, MIC, DOPE, FIC, AINI, LTLD, HEAT are introduced in teaching sentences, then shortened. Headings and reference titles stay expanded. The Abstract defines PEG, AgNPs, and MIC and reuses them.

## Tables in article

- Table 1 (experimental full texts) called in Results and Discussion.
- Table 2 (reviews / clinical secondary literature) called in Results and Discussion.
- Table 3 (AgNP–antibiotic metrics) called in Results.

Cells match the notes for the spot-checked numbers above.

## Discussion

Interprets PEG vs acid-trigger vs thermosensitive clinical failure, pectin coats vs stimulus, AgNP synergy vs liposomes, and inlet constraints. No fetch-log, PRISMA, or token meters. Andresen 2026 is not used as a results source (no `%PDF-` full text).

## Gaps left explicit

- Andresen 2026 polymersome full text: not retrieved; not cited as findings.
- JDDST 2020 sertraline: paywalled; AJP 2020 OA used instead and labelled.
- Related search: 2021–2026 open-access journal articles, relevance-sorted; older seeds kept.

## Ranks

Single pass. Deliverable is `article.md` (also copied to `review/report/final-report.md`).
