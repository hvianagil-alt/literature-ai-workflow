# Double-check — 2026-09-20-hpp-rerun

- Scripts: check_extraction.py 43/43 OK (prior critic pass, exit 0); check_article.py OK after the two number fixes (writer/orchestrator report); score_review_form.py food-science p_published_form=1.000 (orchestrator report)
- Notes still stub? no (0). `check_extraction.py` reports 43/43 claim-ready. Extra files `Baek2026.md` (pet-food, excluded by protocol) and `Bhanu Prakash Reddy2026.md` (wrong/unretrieved full text) are logged in Methods, not treated as included evidence.
- Table still DRAFT/lead-paste? no (`review/runs/2026-09-20-hpp-rerun/table/literature-table.md` states rewritten from Claim-ready facts; no “mechanical first-pass” / “extracted lead”)
- Claims spot-checked (paper, number, note/PDF agree?):
  - Bulut 2021, 400 MPa/9 min/4 °C unfrozen PBS 1.83 vs frozen −24 °C 5.63 / −80 °C 6.83 log — note agree
  - Sykora 2026, ~450/500/600 MPa; F = 171.12; *S. aureus* time P = 0.06139; β-Lg 20.1% / LF 39.0%; *E. coli* 1.6 vs 3.0 log (3.6% fat vs skim) — note agree
  - Li 2021, PPO 75.2% vs 22.6%; POD 80.7% vs 10.2%; sensory n = 101; day-1 APC/Y&M 6.33/6.31 — note agree (SDs omitted in prose, not contradictory)
  - Jönsson 2023, hardness −67.7% (200 MPa) to −87.7% (600 MPa), 180 s — note agree
  - Szczepańska 2021, max 1.4 log TMC at 200 MPa; TMC 5.36; Dv(50) 308 → 15.8 µm — note agree
  - Nikparvar 2021, 7.79 ± 0.82 log; 1.338 → 0.809 nm; n = 318 cells — note agree
  - Serra-Castelló 2021, δ Scott A 0.70 vs 2.48 min; second-log 2.10 vs 11.22 min — note/PDF agree
  - Serra-Castelló 2021, Table 1 and §3 “1.75–2.51 log with 2.8% lactate” — note/PDF agree after rewrite (PDF 2.51, 1.75, 2.35 at 2.8%; 1.29–2.35 removed)
  - Scepankova 2022, 5.65 log undiluted at 85 °C — note agree; PATP 600 MPa/15 min/75 °C to 1.30 log LOD at aW 0.85–0.90 in Table 1, §3, and Table 3 — note agree after rewrite
  - Eran Nagar 2026, PPO 41 ± 8 vs 58 ± 13; ΔE ~6.4–6.5 — note agree
  - Koker 2023, TABC 4.04; 200 MPa 0.85 log; heat 0.72–1.34 log — note agree
  - Koutsoumanis 2022, 600 MPa/6 min ~6 log *S. aureus*; RTE 5-log *Listeria* 4.7 min at 600 MPa — note agree
  - Heydenreich 2024, −2.1 / −5.7 / nisin −5.3 log — note agree
  - Tsikrika 2021, Rooster ΔE 8.06 / 21.23 / 18.03 — note agree
  - Torrents-Masoliver 2024, 0.3 ± 0.2 log; Scott A 6.2 log — note agree
  - Zhang 2022, D 2.12 vs 5.32 min; 4.88 vs 0.42 log; D 4.17 → 13.71 min — note agree
- Abstract: citations? no. named papers? no. search/OA/year-window language (must be Methods only)? no in Abstract/Introduction/Discussion/Conclusions. Scopus, OpenAlex, 2021–2026, public PDF, paywall, and screening counts sit only in §2 Methods. No *First, Second, Third* or (i)(ii)(iii) spine. Title is a colon subtitle naming the phenomenon. Keywords follow the Abstract.
- Citation order: first-appearance [1]…[43]? yes ([1] Koutsoumanis in the Introduction). References each in their own paragraph? yes (blank line between entries).
- Abbreviations: repeated terms defined once then shortened? yes (HPP, HPTP, HPH, EFSA, VBNC, PPO, RTE, aW). Abstract still readable without a glossary? yes (Abstract stays in words; HPP/HPH not required there).
- Adjacent-field reader test (Introduction teaches later sections?): yes. Heat as the default verifiable kill step, legal milk 72 °C/15 s and juice five-log as performance criteria, isostatic HPP vs adiabatic HPTP vs valve HPH, vegetative vs spore physiology, injury/VBNC, and PPO as a quality enzyme that need not track plates are all taught before §3. A neighbour-field food scientist can follow coefficients, legal bars, spores, quality, and false-equivalence chapters.
- Mechanism articulation (condition → effect → measurement; grade not upgraded?): yes. Ice, aW, agar/time, pores, lactate, and pulse are joined to log reductions; pores and nucleic-acid leak are treated as demonstrated, lactate piezo-protection and Ice I–III as proposed/compiled.
- Paragraph function (claim → evidence → contrast → explanation → synthesis): yes. Thematic sections open on the coefficient or bar, then name designs, then contrast matrices, then close on what the section cannot show.
- Whole-paper argument (problem / evidence / explanation / limitation / contribution): a labelled megapascal hold is treated as if it were pasteurisation; included opinion, milk mixed-model, and primary challenges show vegetative kill in high-moisture foods with matrix- and assay-dependent logs; ice, solute, injury, heat assistance, and shear vs hydrostatic explain why the same number is not one outcome; no retrieved paired 72 °C/15 s *S. aureus* milk trial, no industrial 600 MPa named-pathogen juice five-log, no proteolytic *C. botulinum* food curve; process specifications must name matrix, assay, and whether heat was part of the kill.
- Field-structure benchmark (`structure-benchmark.md`): done; verdict keep. Heading spine matches rationale (e) and the food-science card’s question-driven shapes (coefficients; legal criteria; spores/HPTP; quality vs plates; neighbouring operations as refusal; separate Discussion). No empty equipment/energy/consumer chapter. No graphical abstract.
- Field memory card: `review/memory/food-science.md`
- Critic verdict: PASS
- Heading spine: thematic `##` sections, not generic Results? yes (§1–9 as in rationale (e))
- Tables in article: Table 1–4 present, captioned, and called from prose. Table 1 Serra-Castelló cell now matches the PDF (1.75–2.51 log at 2.8% lactate). Table 1 and Table 3 Scepankova cells name 75 °C PATP for the diluted-honey LOD.
- If two passes: rank pass 1 vs pass 2 on abstract, tables, traceability, Discussion, completeness (1–5 each) and say which is the deliverable. Not ranked. Comparison to `review/runs/2026-09-20-scopus-hpp/article.md` is forbidden until this run’s harness is green.
- Graphical abstract present: no
- Catalogue voice remaining: no
- Acquisition language outside Methods: no

Re-critic after writer fixes: both prior FAIL items are gone. No new number, teaching, catalogue, or acquisition failures. Article.md was not edited by the critic.
