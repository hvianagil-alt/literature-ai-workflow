# Synthesis rationale — 2026-09-20-scopus-hpp

**Research question:** How do nonthermal food-processing technologies — especially high-pressure processing (HPP / HHP), with ultrasound, PEF, plasma, irradiation, and hurdle combinations — inactivate microorganisms and change quality, enzymes, and related endpoints in human foods?

**Kind of review to write:** narrative journal review (not a systematic review or meta-analysis). Included evidence is 43 public full texts from a 2021–2026 Scopus export after title screening and OA retrieval. Designs are incommensurable (EFSA opinion, systematic/scoping reviews, laboratory challenges, storage trials). Do not pool log reductions.

**Not used as evidence:** title excludes (books, pet food, unnamed technology); 133 records without a public PDF/JATS body; six full-text excludes (seed-germination review; ML/digital-transformation review; PEF bibliometric; 591-page dump; unreadable 1-page PDF; alcoholic-beverage methods manual mis-fetched as a coconut-water PEF/HPP paper).

## (a) What each included study actually measured

Grouped; full cells are in `table/literature-table.md`.

**Regulatory / milk safety**

- **Koutsoumanis2022** — EFSA BIOHAZ opinion: modelled log10 reductions and serving contamination for HPP vs legal thermal pasteurisation of milk/colostrum; ALP as HPP indicator; Listeria isoreduction in RTE foods. Did not run a new milk challenge.
- **Sykora2026** — PRISMA review of HPP parameters in raw bovine milk for pathogens (65 papers) and bioactive proteins (24 papers); only four papers had both.
- **Agriopoulou20231**, **Ledina2023149** — narrative dairy HPP / nonthermal surveys; no pooled n.

**HPP microbiology, injury, matrix protection**

- **Guzel2026** — scoping review, 74 RTE-meat Listeria studies; HPP 29/74; 0–7 log reported; no meta-analysis.
- **Zhang2022** — HPP/HPTP kinetics in fruit/vegetable systems (reviews cited spore examples).
- **Xia2022** — mini-review of HHP plus nonthermal hurdles in plant foods.
- **Wu2025** — review of pathogen culture reductions vs sublethal injury / “hidden” hazards.
- **Nikparvar2021** — fluorescence + diffusion model of *L. monocytogenes* membrane pores after HPP; 7.79 log drop to below LOQ.
- **Serra-Castelló2021** — lactate piezo-protection of *L. monocytogenes* in cooked ham (dose-dependent less kill).
- **Torrents-Masoliver2024** — enumeration agar, acid, and sampling time change apparent HPP reductions in fruit purées (0.9- to 4.5-fold apple vs banana–apple).
- **Rodríguez2024** — US + HPP model for *C. sakazakii* in buffer; 400 MPa / 3 min: no colonies.
- **Bulut2021** — freeze-then-HHP of *E. coli* K12 in PBS and orange juice (up to 6.83 log in frozen PBS).
- **Scepankova2022** — *B. subtilis* spores in honey: undiluted honey, PATP 600 MPa / 85 °C / 15 min did not reduce TEL.

**HPP quality / shelf-life experiments**

- **Li2021** — Concord grape purée HPP vs heat; both ~5-log APC; HPP held Y&M longer in storage.
- **Le2023399** — celery juices; HPP kept TAC <2 log for 8 weeks vs spoil at 1 week untreated.
- **Eran Nagar2026** — semi-industrial grape juice: HPP vs ohmic vs thermal; HPP weak on PPO (~30%) vs >90% heat/ohmic.
- **Machado2023** — dairy cream 450 vs 600 MPa vs heat; 450 MPa spoiled like raw.
- **Koker2023292** — donkey milk TABC and lysozyme/lactoferrin vs 75 °C.
- **Castrica2021**, **Wang2025351**, **Nilsuwan2024**, **Pimsannil2025**, **Lian2023**, **González-Cantillo2026**, **Pérez Alcalá2023**, **Marçal2021**, **Jönsson2023**, **Rossi Ribeiro2026**, **Tsikrika2021**, **Zhang2026** — fish, squid, crab, prawn (HPCD), lamb burgers, sous-vide, algae sausages, kelp, pumpkin pulp, potatoes, fermented juice US+UHP: mixed APC/quality/sensory endpoints, not a shared pathogen.

**Other nonthermals**

- **Maghami2026** — flow-through sonicator apple juice; DF-4 2.7–3.6 log spoilage flora, not 5-log pathogens.
- **Seyedalangi2025** — gliding-arc plasma + phycocyanin on trout; delayed TVC/TVN spoilage.
- **Schnabel2021115** — plasma-functionalized water on lettuce; lab 4–5 log vs pilot ~2 log.
- **Hashemi Moosavi2021** — ultrasound vs mycotoxins/fungi (narrative, cited % degradations).
- **Bhatnagar2022** — irradiation of fruit/veg (narrative; FAO/WHO 10 kGy statement).
- **Mukhtar2022** — sugarcane juice survey of US/PEF/HPP/microfluidization vs heat.

**Hurdle / HPTP / matrices reviews**

- **Masilamani202519**, **Weihe2026**, **Jeevitha2023**, **Peng2023313**, **Knoerzer2025627**, **Braspaiboon2024** — hurdles, decontamination across matrices, beverages, aquatic UHP, HPTP commercialisation, protein allergenicity/function.

## (b) Themes the data support vs themes that would be forced

**Supported**

1. Industrial HPP (roughly 400–600 MPa, minutes, chilled or ambient) reliably reduces many vegetative bacteria in high-aw foods, but the log reduction is matrix-, strain-, and assay-dependent (Guzel; Torrents-Masoliver; Serra-Castelló; EFSA).
2. Bacterial spores and some barotolerant vegetative cells are not a solved ambient-HPP problem; heat-assisted pressure (HPTP) or other hurdles appear in the reviews and in honey spore work (Zhang2022; Knoerzer; Scepankova).
3. HPP milk is not interchangeable with legal thermal pasteurisation on the pathogen-reduction metric EFSA modelled (Koutsoumanis2022); bioactive-protein papers rarely share a protocol with pathogen papers (Sykora2026).
4. Quality is not uniformly “fresh-like”: PPO can survive HPP that already cuts APC (Eran Nagar); kelp hardness collapses at 600 MPa (Jönsson); cream at 450 MPa behaves like raw (Machado).
5. Combinations (freeze+HHP; US+HPP; plasma+pigment; mint extract+HPP; COS+HPP) can raise lethality or delay spoilage beyond either factor, but they change the process class (no longer “HPP only”).
6. Culture-based log reductions can overstate safety if injured cells recover or if enumeration is selective (Wu; Torrents-Masoliver; Nikparvar still below LOQ in that specific setup).

**Would be forced**

- “HPP always achieves a 5-log pasteurisation of juice pathogens.” Li2021’s 5-log is aerobic plate count of grape purée, not *E. coli* O157:H7; Maghami missed 5-log on native yeast/mould.
- “Nonthermal technologies are equivalent to each other.” Plasma, ultrasound, irradiation, HPCD, and HPP share a slogan, not a mechanism or TRL (Weihe; Schnabel lab vs pilot).
- A pooled mean log reduction for HPP of *L. monocytogenes* on RTE meat (Guzel explicitly could not meta-analyse).

## (c) Real disagreements and why

- **Milk HPP vs pasteurisation:** Agriopoulou’s narrative “400–600 MPa is sufficient” vs EFSA’s finding that 600 MPa / 6 min still underperforms legal HTST/LTLT on comparable milk pathogens. Reason: Agriopoulou compiles selected table rows; EFSA models a pasteurisation performance criterion across hazards including those with poor HPP data.
- **Donkey-milk numbers:** Koker abstract vs results disagree on heat log kill and enzyme %; the note prefers the results section. This is an internal inconsistency, not a cross-paper fight.
- **Apparent HPP lethality in purées:** Torrents-Masoliver shows the same process looking 0.9–4.5× different by fruit and by agar/acid/time — disagreement with any paper that reports a single log reduction without recovery methods.
- **Plasma scale-up:** Schnabel lab 4–5 log vs pilot ~2 log on lettuce — same technology, different process engineering (not a biological contradiction).
- **PPO vs microbes in grape juice:** Eran Nagar HPP ~30% PPO remaining vs ohmic/thermal >90% enzyme kill, while all cut aerobic counts ~3 log. Quality and safety endpoints diverge; not a microbial disagreement.

## (d) What this sample cannot answer

- Equivalence of HPP to FDA 5-log juice HACCP for *E. coli* O157:H7 / *Salmonella* / *Cryptosporidium* in the included primary juice papers.
- A validated industrial HPP schedule for bovine milk that jointly meets 5-log pathogen kill and preserves IgG/lactoferrin (Sykora: four overlap papers only).
- Spore commercial sterility without added heat (Scepankova undiluted honey failure; Zhang review).
- Head-to-head PEF vs HPP on the same coconut-water trial (intended paper not retrieved).
- Energy, LCA, or consumer-risk numbers except where a review asserts TRL (Weihe) without a shared inventory.
- Most of the 182 title-included records (133 not retrieved): any synthesis is OA-biased toward MDPI/Frontiers/PLOS/SpringerOpen/PMC JATS, not Elsevier/Wiley paywalled trials.

## (e) Outline of the review

**Kind:** narrative journal review.

**Title pattern:** High-pressure processing of foods: a narrative review of lethality, injury, and quality when heat is not the kill step.

**Introduction (teach, aim last):** Foodborne illness and why heat works (5–6 log vegetative targets; spore cook). What HPP physically is (isostatic pressure, 400–600 MPa, cold/ambient). Membrane/protein mechanism in one paragraph. Why quality arguments exist (vitamins, colour, “fresh-like”). Controversy: barotolerance, spores, milk pasteurisation law, injured cells. Last paragraph: *The aim of this review is…* / *The central argument of this review is that HPP is a reliable vegetative hurdle whose log reduction cannot be read off the pressure gauge, and that quality preservation is endpoint-specific rather than automatic.*

**2. Methods:** Scopus 20 Sep 2026 export; 2021–2026 journals; OA PDF or Europe PMC JATS; 43 included full texts. Point to prisma.md, not a flow-chart theatre in Discussion.

**3. What pressure does to cells and why matrices change the log reduction** — Nikparvar, Serra-Castelló, Torrents-Masoliver, Wu, Zhang kinetics, Guzel <400 vs 500–600 MPa. **Table 1:** microbial log reductions from primary HPP challenges (organism, matrix, P/t, log, assay).

**4. The pasteurisation problem: milk, juices, and performance criteria** — Koutsoumanis, Sykora, Agriopoulou, Machado, Koker, Li, Le, Eran Nagar, Maghami. **Table 2:** milk and juice processes vs a 5-log or legal-pasteurisation benchmark (met / not met / not tested).

**5. Spores, HPTP, and other ways to finish the kill** — Zhang2022, Knoerzer, Scepankova, Xia, Masilamani, Rodríguez US+HPP, Bulut freeze+HHP. **Table 3:** spore or hurdle outcomes.

**6. Quality is not one number** — PPO, colour, texture, enzymes, allergenicity (Braspaiboon), bioactive proteins, seafood (Castrica, Wang, Nilsuwan, Peng), kelp (Jönsson), cream, grape, celery, pumpkin.

**7. Other nonthermal fields in this set** — ultrasound (Maghami, Hashemi, Zhang2026), plasma (Schnabel, Seyedalangi), irradiation (Bhatnagar), HPCD (Lian), sugarcane survey (Mukhtar), Weihe/Jeevitha maps.

**Discussion:** two readings (HPP as commercial vegetative pasteurisation of RTE meat/juice vs HPP as incomplete milk pasteurisation); why logs cannot be pooled; OA bias; what to measure next (paired pathogen + enzyme/protein; recovery media; industrial scale).

**Conclusions:** numbered scientific next steps.

## (f) Interpretation gaps (must attempt retrieval)

1. **Paired HTST vs HPP in bovine milk** measuring the same pathogen cocktail and the same bioactive proteins (IgG, lactoferrin) — Sykora says this pairing is rare; EFSA did not run it.
2. **Primary HPTP or PATP data on bacterial spores in a juice or honey-like low-aw food** to sit beside Zhang’s review and Scepankova’s honey failure.
3. **Juice HPP validation against a named 5-log pathogen** (*E. coli* O157:H7 or *Salmonella*), because Li and Maghami used APC/spoilage flora.

## (g) Targeted extra retrieval log

OpenAlex searches (2021–2026, `journal` quality) are in `gap-retrieval/search-g1.json`–`search-g3.json`. Fetch log: `gap-retrieval/fetch-log.json`. PDFs/JATS: `papers/2026-09-20-scopus-hpp-gapfill/`.

1. **Paired HTST vs HPP bovine milk (pathogen + proteins):** Hits included the already-included EFSA opinion and human-milk HTST vs Holder work (`10.3389/fped.2021.798609`), plus bioactive-protein reviews that do not jointly challenge pathogens. No new public full text of a paired bovine-milk HTST/HPP trial was retrieved. **Sought / not retrieved as a new included paper.**
2. **Primary HPTP spore kinetics in plant foods:** Hits included reviews already in the export. **Found and retrieved:** Houška, Silva, Evelyn, Buckow, Terefe, Tonello 2022, *Foods* (`10.3390/foods11020223`) via Europe PMC JATS — now included as gap-fill `Huang2022plant` (D-values for *A. acidoterrestris* spores; 600 MPa equipment limit). Elsevier hits on juice sensory/HPP+PEF had **no public PDF/JATS**.
3. **Named 5-log juice pathogen HPP:** Hits included bacteriophage and tahini papers (wrong matrix) and `10.1016/j.foodres.2020.110091` (O157/Listeria/Salmonella pressure resistance). **Sought / not retrieved** (no public PDF/JATS). Gap remains: this sample still lacks a 5-log *E. coli* O157:H7 juice HPP validation.

## (h) Decision to write

Rationale + extra retrieval attempted. Table updated with one gap-fill review. Remaining open: paired milk HTST/HPP trial; juice 5-log pathogen HPP primary. The article may be written from the updated 44-row table. Do not treat Huang2022plant D-values as new experiments.
