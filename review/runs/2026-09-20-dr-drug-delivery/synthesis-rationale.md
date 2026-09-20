# Synthesis rationale — 2026-09-20-dr-drug-delivery

Written after the literature table and before any `article.md`. Extra retrieval for gaps is logged in (g).

## (i) Intellectual model

1. **Central question.** How do ocular delivery systems (bolus intravitreal injectables, biodegradable and non-biodegradable implants, and experimental nanocarriers) get anti-VEGF agents, corticosteroids, and other drugs to the diabetic retina, and what still limits duration, targeting, and translation in DR/DME?

2. **Variables.** Route (topical, periocular, intravitreal); carrier class (solution biologic, PLGA DEX implant, PVA/silicone FAc implant, polymer/lipid/protein nanoparticles, ocuserts); payload (anti-VEGF protein, dexamethasone, fluocinolone, apatinib, PEDF peptide, vildagliptin); duration of exposure; retinal/macular endpoint (histology, leakage, BCVA, CMT/CST); safety (IOP, cataract, nanoparticle toxicity).

3. **Mechanisms (as papers state them).** Anterior barriers (tear turnover, <5% topical bioavailability) make drops inadequate for the posterior segment (Ahmed, Wang 2024, Jacob). The inner limiting membrane and vitreous charge/size filters limit nanoparticle access after IVT (Swetledge). Licensed anti-VEGF proteins have short vitreous half-lives, forcing repeated injections (Kim, Liberski). DEX 0.7 mg in PLGA is labelled as ~6-month biphasic release; FAc 0.19 mg is labelled as ~36-month low-dose release (Tsung, Furino, Goñi). HA coating is **proposed** (not occupancy-measured) to use CD44 for topical retinal uptake of apatinib NPs (Radwan). PEDF34-NP is **proposed** to suppress VEGF/inflammation and leakage after one IVT (Qu). Faricimab’s Ang-2/VEGF-A bispecific design is **cited** as a durability strategy, not measured in this sample’s own experiment (Liberski).

4. **Heterogeneity.** Reviews of all ocular disease vs DR-specific nano reviews vs original rat NP studies vs retrospective DME implant cohorts vs expert consensus. Endpoints do not pool: rat retinal thickness is not ETDRS letters.

5. **Evidence types.** Narrative reviews (Kim, Wang 2024, Liu, Tsung, Ahmed, Cao, Jacob, Swetledge, Kartı, Spinetta, Furino, Liberski, Goñi); original preclinical (Radwan, Qu, Ramadan); original clinical observational (Taloni is a systematic narrative of DEX 1st vs 2nd line; Neves, Baillif, Mathis, Koç, Wang 2021). No new RCT enrolled by this sample. MEAD/FAME/Protocol T numbers appear only as **quoted** by included reviews.

6. **Established (in this sample).** Topical drops do not treat posterior DR at marketed bioavailability. Repeated IVT anti-VEGF is first-line DME therapy but incomplete. DEX implant reduces CMT; vision gains are modest and IOP/cataract are the clinical price. FAc extends duration after DEX in chronic DME with residual retreatment and IOP monitoring needs. After vitrectomy, a DEX implant can outperform PRN ranibizumab over 6 months in a small retrospective series (Wang 2021).

7. **Suggested / uncertain.** Topical HA-BSA apatinib NPs matching IVT histology in STZ rats (Radwan, n=5). Single IVT PEDF34-NP leakage reduction at 4 weeks (Qu). Vildagliptin SLNP ocuserts as a once-daily topical platform without a retinal DR endpoint (Ramadan). Faricimab extending injection interval vs aflibercept (Liberski, cited trials). DEX first-line vs switch: Taloni finds no systematic VA/CST difference; Koç finds no 6-month VA superiority of switch vs continue.

8. **Unknown.** Human PK of the experimental NPs; milligram apatinib dose per drop; whether nano toxicity scales to chronic human dosing; head-to-head RCT of DEX vs continued anti-VEGF after incomplete load in this sample (Koç is retrospective); 3-year FAc RCT full text (Singer not retrieved); microneedle/port-delivery original papers (mentioned in reviews, not retrieved as full texts here).

9. **Consequence.** The article must teach barriers and licensed implant kinetics first, then cluster clinical implant data separately from preclinical nanocarriers, and must not treat a rat histology win as a DME visual-acuity result. Translation limits (injection burden, IOP, incomplete drying, missing human nano trials) stay open.

Causal chain: diabetic inner BRB / macular edema → short-acting IVT drugs or impermeable drops → delivery system chosen for duration or route → measured CMT/BCVA or rat RT/leakage → interpretation that arrival and duration are not the same as function or safety.

## (a) What each included study actually measured

- **Kim 2021 (review):** intraocular PK and delivery platforms for retinal drugs (implants, particles, hydrogels, PDS). Did not enrol patients.
- **Wang 2024 (review):** DR pathophysiology plus treatment and nanocarrier delivery. Did not measure new PK.
- **Liu 2021 (review):** nanotechnology applications in DR. Did not run a new NP experiment.
- **Tsung 2023 (review):** biodegradable polymer ocular DDS, including Ozurdex vs Iluvien materials. No new formulation n.
- **Ahmed 2023 (review):** ocular anatomy, barriers, routes, nanocarriers across eye disease. DR is a minority of the text.
- **Radwan 2021 (preclinical):** Apa-HA-BSA-NP size/zeta/EE/release; STZ rat RT/BM after topical vs IVT (n=5); confocal fluorescence. No VA/OCT, no µg/eye dose.
- **Ramadan 2024 (formulation):** VLD-SLNP ocusert size/EE/24 h release in rabbits (n=24 release, n=5 irritation). No DR retinal efficacy.
- **Qu 2022 (preclinical):** PEDF34-PLGA NP in hypoxia cells, OIR mice, STZ rats (Evans blue n=5 at 4 weeks). Dose conflict 20 vs 5 µg/eye in text vs legends.
- **Cao 2022 (review):** ocular NP applications and toxicity (cornea/conjunctiva/retina). Animal toxicology cited, not a new tox study.
- **Jacob 2022 (review):** topical SLN/NLC for ocular therapy. DR mentions sparse; many examples are anterior segment.
- **Swetledge 2021 (review):** NP distribution vs ILM/vitreous charge/size. One DR mention; mechanism of filters.
- **Taloni 2023 (systematic narrative):** DEX implant 1st vs 2nd line in DME; quotes MEAD and real-world series; not a new meta-analysis statistic.
- **Neves 2021 (review):** real-world Ozurdex vs MEAD-type trials; duration ~4–6 months.
- **Kartı 2021 (mini-review):** DEX place in DME armamentarium; quotes MEAD, CHAMPLAIN, BEVORDEX, Protocol U.
- **Spinetta 2023 (review):** seven national DEX consensus documents (first-line situations, retreatment 3–6 months).
- **Liberski 2022 (review):** aflibercept vs faricimab molecular design and **cited** DME RCTs (YOSEMITE/RHINE, VIVID/VISTA). No new patients.
- **Baillif 2022 (observational):** DEX→FAc switch, 113 eyes, mean 7.6 months; BCVA, CMT, IOP, additional treatment 32.7%.
- **Furino 2021 (review):** IVT anti-VEGF and steroid devices in DME; quotes Protocol T, MEAD, FAME, switch series.
- **Mathis 2022 (observational):** REALFAc, 62 eyes, FAc after DEX, mean 13.9 months; BCVA, CMT, IOP, retreatment 37.1%.
- **Koç 2023 (retrospective):** 94 eyes, continue anti-VEGF vs switch to DEX after 3 loads; 6-month BCVA/CMT/IOP.
- **Wang 2021 (retrospective):** vitrectomized pseudophakic DME, DEX n=22 vs ranibizumab n=26, 6 months BCVA/CFT/injections/IOP.
- **Goñi 2022 (consensus):** IOP monitoring after corticosteroid implants; compiled cited IOP rates, no new cohort.

Not retrieved (not evidence): Singer 2022 Ophthalmology 3-year FAc; Vitiello 2024 Life DEX switch; Merrill 2022 AJO FAc burden; Roth 2023 ORET FAc.

## (b) Themes the data support vs themes that would be forced

**Supported.** (1) Posterior DR/DME cannot be treated by conventional drops at <5% bioavailability. (2) Bolus IVT anti-VEGF is effective but short-acting and incomplete. (3) PLGA DEX implants trade injection frequency for IOP/cataract and a ~2–3 month peak / ~4–6 month fade. (4) FAc extends the steroid interval in already-treated chronic DME; about one-third still need extra therapy in French real-world series. (5) Vitreous cavity status (vitrectomy) changes implant vs solution comparison (Wang 2021). (6) Experimental nanocarriers can put small molecules or peptides in rodent posterior segment; human DR nano efficacy is not in this sample. (7) NP ocular toxicity is condition-dependent (Cao).

**Forced (do not write).** That topical NPs are ready for DME clinic. That DEX is vision-superior to continued anti-VEGF after incomplete load (Koç: CMT yes, BCVA no). That faricimab’s dual target was measured here. That all ocular NP reviews are DR trials. That Ramadan’s ocusert treats retinopathy.

## (c) Real disagreements and why

- **DEX switch vs continue anti-VEGF:** Furino quotes a retrospective switch with +6.1 vs +0.4 letters; Koç’s four-arm 6-month series finds no significant BCVA change in any arm and no between-group VA difference (p=0.159). Different designs (quoted external series vs this sample’s own cohort), different baselines (Koç DEX arms had worse month-3 VA), 6 vs other follow-up.
- **DEX first vs second line:** Taloni’s synthesis: no systematic VA/CST advantage by line; Spinetta’s consensuses still list first-line niches (vitrectomized, inflammatory OCT, CV risk). Guideline vs pooled outcome.
- **Aflibercept MW:** Wang 2024 vs Kim (115 vs ~145 kDa) — review discrepancy; do not pick a third number from memory.
- **Radwan topical ≈ IVT histology** vs **Wang 2024 “topical nearly ineffective”:** different payloads (small-molecule NP vs free drug) and species (rat vs human bioavailability claim). Not a direct contradiction if the article names the condition cluster.
- **Qu dose 20 µg vs 5 µg:** internal text conflict; treat as uncertain.
- **FAc BCVA:** Baillif peak +5.3 letters at month 4 then attrition; Mathis +5.0 letters at 21 months from a better baseline (64 vs 54 letters) — different entry CMT (333 vs 455 µm) and prior control.

## (d) What this sample cannot answer

- Pooled RCT effect of DEX or FAc vs anti-VEGF (MEAD/FAME/Protocol I full texts not retrieved).
- 3-year FAc safety/efficacy from Singer 2022 (not retrieved).
- Human trial of topical or IVT nanocarriers for DR.
- Microneedles, iontophoresis, or Port Delivery System as primary evidence (only review mentions).
- Head-to-head randomised DEX vs continued anti-VEGF after incomplete load.
- Apatinib µg/eye and CD44 occupancy.
- Pediatric DR, type 1–only cohorts as a class, low-resource screening (out of protocol).
- Whether nano toxicity in rabbits predicts chronic human IVT.

## (e) Outline of the review

**Kind:** journal-style **narrative review** (not systematic meta-analysis). Teach in the Introduction; numbered thematic sections; separate Discussion.

**Title shape:** phenomenon first, colon subtitle (delivery constraint / DR-DME).

0. **Title, Abstract, Keywords** — topic map; no citations; no search theatre.
1. **Introduction** — DR/DME as a posterior-segment vascular problem; inner BRB and macular fluid; why marketed drops fail; what monthly anti-VEGF already does and still fails (injection burden, incomplete drying); implant vs nanoparticle as two answers to duration/route; live controversy (steroid IOP vs anti-VEGF frequency; animal nano vs clinic). Last paragraph: aim / central argument.
2. **Methods** — OpenAlex 2021–2026 journal OA; eligibility; only public full texts; 22 included. No token talk.
3. **Ocular barriers and routes that force a delivery system** — Ahmed, Kim, Wang 2024, Jacob, Swetledge. Nested: 3.1 tear/<5% drops; 3.2 ILM and vitreous as NP filters; 3.3 why IVT exists.
4. **Bolus anti-VEGF proteins, durability engineering, and a refillable port** — Furino, Liberski, Kim, Khanani 2025, Pieramici 2025. Nested: 4.1 short half-life and incomplete drying; 4.2 trap vs bispecific as injection-interval strategies (cited trials, labelled as cited); 4.3 Port Delivery System vs monthly ranibizumab (Pagoda) and vs monitoring in NPDR (Pavilion).
5. **Biodegradable dexamethasone implants in DME** — Taloni, Neves, Kartı, Spinetta, Koç, Wang 2021, Group 2015 (MEAD previously treated subgroup). Nested: 5.1 release kinetics and MEAD-quoted plus subgroup outcomes; 5.2 first-line vs switch and real-world duration; 5.3 vitrectomized eyes; 5.4 IOP and cataract as DEX constraints. **Table 1** clinical implant/injectable endpoints.
6. **Longer-acting fluocinolone implants and DEX-to-FAc switches** — Mathis, Baillif, Goñi, Tsung (material contrast), Augustin 2019 (Retro-IDEAL 3-year), Fusi-Rubiano 2018. Nested: 6.1 REALFAc / switch anatomy and letters; 6.2 three-year real-world FAc (Retro-IDEAL) and FAME as cited in Fusi-Rubiano; 6.3 IOP monitoring as the translational constraint; 6.4 vitrectomized FAc eyes. **Table 2** FAc/switch rows. Singer 2022 remains not retrieved.
7. **Experimental nanocarriers aimed at the diabetic retina** — Liu, Wang 2024, Radwan, Qu, Ramadan, Tsung, Cao. Nested: 7.1 topical HA-apatinib (hinge Radwan); 7.2 IVT peptide NP (Qu); 7.3 ocusert without retinal endpoint (Ramadan); 7.4 toxicity (Cao). **Table 3** preclinical/formulation.
8. **Discussion** — arrival ≠ drying ≠ vision; why CMT and BCVA split; why rat NP and human implant cannot be pooled; open gaps (no human nano RCT; Singer not retrieved).
9. **Conclusions** — one paragraph, continuous prose.
10. **References** — first-appearance order, blank line between entries.

## (j) Condition clusters

**Cluster 1 — Barrier/route reviews (same question: why free drug fails posteriorly).** Papers: Ahmed, Kim, Wang 2024, Jacob, Swetledge, Liu, Tsung. Same: narrative; human anatomy + cited animal PK. Differ: Ahmed/Jacob are all-eye; Wang/Liu are DR-titled; Swetledge is distribution physics. Jointly support: drops <5%; IVT is the default posterior route; size/charge/ILM matter for NPs. Cannot support: a ranked list of “best” nanocarrier for DME.

**Cluster 2 — Licensed bolus anti-VEGF and a refillable ranibizumab port (same question: protein delivery duration).** Papers: Furino, Liberski, Kim, Khanani 2025, Pieramici 2025. Same: ranibizumab/aflibercept/faricimab family. Differ: reviews citing trials vs Pagoda RCT (PDS Q24W vs monthly IVT in DME, n=634) vs Pavilion (PDS vs monitoring in NPDR without CI-DME). Jointly support: short intraocular activity of bolus protein; PDS can match monthly ranibizumab BCVA in DME at the cost of implant AESI (vitreous haemorrhage). Faricimab interval claims remain cited, not generated here.

**Cluster 3 — DEX 0.7 mg PLGA implant in human DME (same payload/device).** Papers: Taloni, Neves, Kartı, Spinetta, Koç, Wang 2021. Same: Ozurdex-class implant, DME, BCVA/CMT/IOP family. Differ: vitrectomized (Wang 2021) vs not; 1st vs 2nd line (Taloni/Spinetta) vs resistant after 3 anti-VEGF (Koç); review vs original n=94 and n=48. Jointly support: CMT falls; VA gains modest or null in resistant 6-month data; IOP rises more than continued anti-VEGF; duration months not years. Cannot support: DEX vision-superiority as a class.

**Cluster 4 — FAc 0.19 mg ~3-year implant after prior DEX (same device family, chronic DME).** Papers: Baillif, Mathis, Goñi (safety form), Tsung (polymer contrast), Augustin 2019, Fusi-Rubiano 2018. Same: Iluvien-class 0.19 mg. Differ: n=113 vs 62 vs 81; follow-up 7.6 vs 13.9 vs ~31 months; baseline CMT 455 vs 333 vs 502 µm. Jointly support: modest letter gain, CMT down, ~1/3 additional treatment, IOP protocols required. Singer 2022 still not retrieved; Retro-IDEAL is real-world 3-year, not the missing Ophthalmology RCT.

**Cluster 5 — Experimental posterior nanocarriers with a DR-relevant model.** Papers: Radwan (STZ rat, topical/IVT apatinib NP), Qu (OIR + STZ, IVT PEDF34-NP). Same: rodent, VEGF-related payload, histology/leakage not ETDRS. Differ: topical HA-BSA vs IVT PLGA; n=5 vs n=5–6; 14-day drops vs single IVT 4-week readout. Jointly support: a designed carrier can change rat posterior endpoints. Cannot support: human DME.

**Cluster 6 — Formulation without retinal efficacy.** Paper: Ramadan (single-study). Rabbit ocusert release/irritation. Cannot support DR treatment claims.

**Cluster 7 — Nano toxicity as a constraint.** Paper: Cao (review). Supports “arrival can still injure”; cannot give a pooled human AE rate for DR NPs.

## (f) Interpretation gaps (must attempt retrieval)

1. **MEAD/FAME (or equivalent) primary RCT full text** — hinge numbers for DEX/FAc are only quoted; cannot independently check n/p.
2. **Three-year FAc implant outcomes** — Singer 2022 not retrieved; Mathis/Baillif are <2 years.
3. **Human or large-animal topical/IVT nanocarrier DR trial** — Radwan/Qu are rodents.
4. **Microneedle, hydrogel depot, or Port Delivery System original paper for DR/DME** — named in Kim/Wang 2024 without a retrieved primary.
5. **Randomised DEX vs continued anti-VEGF after incomplete load** — Koç is retrospective; Protocol U is quoted not retrieved.

## (g) Targeted extra retrieval log

Searches: `gap-retrieval/search-g1.json` … `search-g5.json`. Selected catalog: `gap-retrieval/catalog.json`. Fetch: `gap-retrieval/fetch-log.json` into `papers/2026-09-20-dr-drug-delivery-gapfill/`.

1. **MEAD/FAME primary RCT.** Sought: Boyer 2014 MEAD 10.1016/j.ophtha.2014.04.024. **Not retrieved** (no public PDF). **Found:** Augustin et al. BMC 2015 MEAD previously treated subgroup 10.1186/s12886-015-0148-2 (`Group2015_01482`). FAME full text not in the selected hit list as a distinct OA PDF.
2. **Three-year FAc.** Sought: Singer 2022 (already failed at intake) and Wykoff 2017 10.1016/j.ophtha.2016.11.034. **Not retrieved.** **Found:** Augustin 2019 Retro-IDEAL 10.1177/1120672119834474; Fusi-Rubiano 2018 Iluvien review 10.1007/s40123-018-0145-7.
3. **Human topical/IVT nanocarrier DR trial.** Sought via G3. Hits were generic nano/pathogenesis or already included (Liu, Kim). **No eligible extra full text found.** Gap stays open.
4. **PDS / depot device.** **Found:** Khanani 2025 Pagoda PDS vs monthly ranibizumab DME 10.1001/jamaophthalmol.2025.0006; Pieramici 2025 Pavilion PDS vs monitoring NPDR 10.1001/jamaophthalmol.2025.0001 (Europe PMC XML).
5. **Randomised DEX add-on vs continued anti-VEGF.** Sought: Maturi 2017 Protocol U 10.1001/jamaophthalmol.2017.4914. **Not retrieved.** Koç 2023 remains the only original comparison in the sample.

## (h) Decision to write

Rationale, gap searches, and table update (27 rows) are done. The article may be written from the updated table. Open gaps: MEAD/FAME/Protocol U/Singer primary PDFs; human nano DR trial. Do not cite not-retrieved DOIs.
