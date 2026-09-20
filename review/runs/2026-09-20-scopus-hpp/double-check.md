# Double-check — 2026-09-20-scopus-hpp

- Scripts: `check_extraction.py` 44/44 OK (exit 0); `check_article.py` OK (exit 0) on `review/runs/2026-09-20-scopus-hpp/article.md` with `table/literature-table.md`.
- Notes still stub? no (0 of 44 included notes contained stub markers).
- Table still DRAFT/lead-paste? no (`table_from_notes.py` rewrite; no DRAFT header).
- Claims spot-checked (paper, number, note/PDF agree?):
  - Bulut 2021: 1.83 vs 5.63 vs 6.83 log CFU·ml−1 at 400 MPa / 9 min (4 °C vs −24 °C vs −80 °C hold) — note `Bulut2021.md` Primary result.
  - Maghami 2026: DF-4 yeast >3.6 log, mould 2.7, aerobic 2.8 — note `Maghami2026.md`.
  - Koutsoumanis 2022: industrial 600 MPa / 6 min fewer log10 than legal milk pasteurisation — note `Koutsoumanis2022.md`.
  - Guzel 2026: HPP 29/74 studies; 1–7 log at 500–600 MPa; <1 log below 400 MPa — note `Guzel2026.md`.
  - Scepankova 2022: undiluted honey, 600 MPa / 85 °C / 15 min, no TEL reduction — note `Scepankova2022.md`.
  - Houska/Silva 2022 gap-fill: *A. acidoterrestris* D 8.6 min at 600 MPa / 45 °C in apple juice — note `Huang2022plant.md`.
  - Jönsson 2023: hardness 312.3 g untreated vs 38.3 g at 600 MPa — note `Jönsson2023.md`.
  - Sykora 2026: 65 pathogen papers, 24 protein papers, 4 overlap; pressure strongest contributor; *L. monocytogenes* >551 MPa and >5 min at 20–30 °C for >5 log in papers that got there — note `Sykora2026.md`.
  - Wu 2025: Ritz et al. as cited, 8-log culture drop vs ~4-log still viable; Karamova et al. >7-log culture vs 0.72-log PI-excluding FCM — note `Wu2025.md`.
- Abstract: citations? no. named papers? no. *et al.*? no. search/OA/year-window language? no (Methods only).
- Citation order: first-appearance [1]…[44] (Zhang 2022 is [1]; Wu 2025 is [5] because the membrane/ribosome mechanism is taught in the Introduction). References are separate paragraphs.
- Abbreviations: HPP, HPTP, RTE, PPO, APC, EFSA, CFU defined in running text; Abstract uses HPP and names polyphenol oxidase in words. HTST written out (high-temperature short-time) in the body.
- Adjacent-field reader test (Introduction teaches later sections?): yes. Opens on foodborne illness and legal heat specs, then HPP cycle physics, then non-covalent membrane/protein mechanism (graded as compiled reviews, not a single primary proof), then quality counterexamples, milk/juice law, injury/VBNC, HPTP, aim last.
- Mechanism articulation: yes. Condition → physical/molecular effect → measured endpoint. Ice extra-kill graded as **consistent with** SEM/leakage, not a complete phase map. Membrane routes **compiled by reviews**. Lactate piezo-protection is a measured dose effect without a molecular assay. Assay ≠ death (selective agar; pore repair while counts stay below LOQ).
- Paragraph function (claim → evidence → contrast → explanation → synthesis): yes after the scientific-synthesis rewrite. Topic sentences name the variable or question (not an isolated log). Contrast is a changed coefficient or assay, not “papers disagree.” Subsection endings state what can reasonably be concluded. Conversational metaphor (“the plate invents a disagreement”) is gone; §3.3 is `Injury that culture methods miss`.
- Whole-paper argument:
  1. **Problem:** when heat is not the kill step, vegetative logs, legal pasteurisation, spores, and quality are still written as if they were one HPP claim.
  2. **Evidence:** 500–600 MPa repeatedly reduces vegetative flora in high-aw foods, but reported logs span about 1–7; EFSA modelled industrial 600 MPa / 6 min as not equivalent to legal milk heat; juice 5-log rows here are APC; ambient commercial HPP leaves spores; enzymes and texture often move against plate counts.
  3. **Explanation:** the measured effect is P/t interacting with ice, solute, pH, water activity, strain, recovery medium, and the endpoint that was actually assayed.
  4. **Limitation:** public-OA sample; no included paired bovine HTST vs HPP trial on the same batches; no included inoculated *E. coli* O157:H7 or *Salmonella* juice HPP 5-log; no human disease trial.
  5. **Contribution:** a working rule that a megapascal set-point is not a pasteurisation number, and that legal, microbial, and quality specifications have to be named separately.
- Field-structure benchmark: `structure-benchmark.md` vs 12 included same-area reviews. Verdict: question-driven spine is a justified departure from matrix/technology catalogues; keep §4 legal criteria; omit equipment/energy/consumer chapters. No graphical abstract.
- Heading spine: thematic `##` 3–7 with nested `###` on their own lines. §4.1 `HPP milk versus legal heat pasteurisation`; §5.1 `Spores, adiabatic heat, and refrigeration`. No glued heading+paragraph; no generic Results.
- Tables in article: Table 1 (microbial primary), Table 2 (pasteurisation benchmarks vs what was measured), Table 3 (spores/hurdles); each called in prose. Rows are not pooled.
- Discussion: commercial versus legal readings; heterogeneity as coefficients; quality as a separate specification; pH class; what cannot be concluded; next measurements. Not a second Results and not a First/Second spine.
- If two passes: pass 2 is the scientific-synthesis rewrite (intellectual model in the rationale; claim–evidence–contrast–explanation–synthesis paragraphs; mechanism grading). Deliverable is `article.md` (pass 1 kept as `article-pass1.md`).
