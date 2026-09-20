# Structure benchmark — 2026-09-20-scopus-hpp

**Our kind:** narrative journal review (not a systematic review or meta-analysis).  
**Our organising principle:** scientific **questions** (why the same MPa is not the same kill; legal pasteurisation vs what was measured; spores and heat under pressure; quality endpoints that do not track plate counts; other nonthermal unit operations as supporting technologies).  
**Comparators (n = 12):** included OA review full texts already in this run (headings from JATS/XML or extracted text). No extra OA reviews were fetched for this benchmark. Form only.

| Comparator | Kind | Organising principle (headings) |
|---|---|---|
| Zhang 2022 [1] | Narrative (fruit/veg HPP–HPTP kinetics) | Kinetics models → factors (species, P mode, T, composition, aw/pH) |
| Houška / Silva 2022 [4] | Narrative (plant foods) | Matrix (juices/smoothies) → inactivation modelling → endogenous enzymes |
| Wu 2025 [5] | Narrative (nonthermal + VBNC) | **By technology** (HPP, PEF, CAP, HPCD, US), each with kill / mechanism / VBNC, then regulation |
| Braspaiboon 2024 [6] | Narrative (proteins) | Principle of HHP → protein effects **by source** (plant / animal / alternative) |
| Guzel 2026 [7] | Scoping (RTE meat *Listeria*) | Methods → Results and Discussion: thermal, then **nonthermal technologies** (HPP, pulsed light, UV, irradiation, plasma), then heterogeneity |
| Sykora 2026 [25] | Systematic (bovine milk) | IMRaD-like Methods → Results and Discussion by **organism** then **protein** |
| Agriopoulou 2023 [26] | Narrative dairy | **By dairy product** (milk compounds, cheese, yogurt) |
| Ledina 2023 [27] | Narrative dairy nonthermals | Application of nonthermal technologies **in dairy** |
| Xia 2022 [14] | Mini-review | HHP combinations (hurdles), not a legal-criteria paper |
| Knoerzer 2025 [16] | Engineering narrative | HPTP physics → history → adiabatic heating → applications/commercialisation → **equipment** |
| Weihe 2026 [43] | Broad decontamination map | Technologies × matrices (readiness / typical logs) |
| Jeevitha 2023 [44] | Beverage nonthermals | **By technology** (US, plasma, scCO2, HHP, pulsed light, membranes, PMF) |
| Mukhtar 2022 [41] | Sugarcane juice survey | Thermal options then nonthermal options; has a **graphical abstract** |
| Bhatnagar 2022 [42] | Irradiation mini-review | Mechanisms → process parameters → nutrition → **consumer acceptance** |
| Hashemi Moosavi 2021 [40] | Ultrasound fungi | Overview → inactivation → factors → structure → combinations |

## Heading inventory

| Topic the field uses | In comparators | In our outline | Decision |
|---|---|---|---|
| Teach what the process is | Zhang, Braspaiboon, Knoerzer, Agriopoulou intros | Introduction | keep |
| Brief Methods on a screened corpus | Guzel, Sykora | §2 Methods | keep (narrative-short, not PRISMA theatre in Discussion) |
| Microbial inactivation + coefficients (P, T, matrix, aw, pH, species) | Zhang §3; Houška modelling | §3 + Table 1 | keep |
| Injury / VBNC / assay ≠ death | Wu (own sections per technology) | §3.3 | keep (folded into lethality, not a parallel PEF/CAP encyclopaedia) |
| Legal pasteurisation / 5-log / named pathogen | EFSA opinion is evidence; most narratives skip or assert “sufficient” | §4 + Table 2 | keep — this is the distinctive spine, not a missing chapter |
| Spores / HPTP / adiabatic heat | Zhang; Knoerzer whole paper | §5.1 | keep (physics in the spore argument, not an equipment monograph) |
| Hurdles / combinations | Xia; Masilamani; Hashemi §7 | §5.2 | keep |
| Quality: enzymes, proteins, texture | Houška enzymes; Braspaiboon proteins; Agriopoulou dairy chemistry | §6 | keep (endpoint-first, not matrix-first) |
| Matrix catalogues (milk / juice / meat / seafood as peer `##`) | Agriopoulou; Houška; Guzel; Peng aquatic | nested under questions (§4 milk/juice, §6.3 seafood) | omit as peer `##` — would turn the paper into a search-batch handbook |
| Other nonthermals as equal chapters | Wu; Jeevitha; Guzel; Mukhtar | §7 supporting technologies | keep as **supporting**, not a balanced field map (rationale already forbids equivalence) |
| Equipment / vessels / intensifiers | Knoerzer | mentioned in Intro/§5.1 | omit as a section — no primary equipment trial in the sample |
| Energy / LCA / TRL tables | Weihe | not a section | omit — rationale (d) |
| Packaging | Knoerzer (HPTP 120 °C) | one constraint in §5.1 | omit as a section |
| Consumer acceptance | Bhatnagar (irradiation) | none | omit — no data here |
| Kinetics model zoo (primary/secondary/polynomial) | Zhang §2 | D-values and Weibull tails inside §5.1 | omit as a section — would be a methods textbook |
| Graphical abstract | Mukhtar (and many *Foods* articles) | not in pass 2 | **add** as a one-panel figure after double-check, not as Abstract text |

## What matches

Same-area narrative reviews teach the process, then split **inactivation**, **quality**, and often **combinations**. Scoping/systematic papers in the sample (Guzel, Sykora) use Methods plus a Results-and-Discussion hybrid. Our numbered thematic `##` after a short Methods matches the **narrative** Foods / Food Eng Rev pattern better than IMRaD “study characteristics.” Injury as a first-class limit matches Wu’s emphasis without copying Wu’s technology-by-technology encyclopaedia. Tables that separate **what was measured** from a legal benchmark (our Table 2) are rarer in the narratives, which more often compile selected 5-log rows (Agriopoulou). That difference is a feature of this argument.

## What we omit on purpose

Vessel design, energy, packaging, and consumer acceptance recur as **peer headings** in engineering or irradiation reviews. This sample does not measure them. They stay in rationale (d). Organising `##` by milk vs meat vs juice would match Agriopoulou/Houška/Guzel, but it would hide the claim that a megapascal is not a pasteurisation number. Technology-equal chapters (Wu, Jeevitha) would contradict the evidence density (HPP rows vs one sonicator, one plasma pilot).

## What we should add before drafting

Nothing in the scientific spine. Add a **graphical abstract** (field-typical in this journal class) from the intellectual model. One Discussion sentence may name neighbouring topics that lack measurements here.

## Verdict

The outline is a **justified departure** from matrix-by-matrix and technology-by-technology catalogues, and it is **field-typical** in the topics it does treat (lethality coefficients, spores/HPTP, enzymes/proteins/texture, hurdles). It should not be rewritten as “§3 milk, §4 juice, §5 meat.” The legal-criteria section is more prominent than in most included narratives; that matches the included EFSA opinion and should stay. Graphical abstracts are common enough in this area that the workflow should produce one.
