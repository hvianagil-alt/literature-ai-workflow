# A Diffusion Model to Quantify Membrane Repair Process in *Listeria monocytogenes* Exposed to High Pressure Processing Based on Fluorescence Microscopy Data

- **Citation (as given in the paper / filename):** Nikparvar B, Subires A, Capellas M, Hernandez-Herrero M, Crauwels P, Riedel CU, Bar N. Front Microbiol. 2021;12:598739. doi:10.3389/fmicb.2021.598739. PMID: not printed in the extracted header; article ID 598739.
- **Source file:** papers/2026-09-20-hpp-rerun/Nikparvar2021.txt
- **Extracted:** 2026-09-20
- **Screening:** Included (experimental HPP of *L. monocytogenes*: membrane pores, PI uptake, repair, plate counts)

## Research question
Does HPP at 400 MPa for 8 min at 8 °C create plasma-membrane pores in *Listeria monocytogenes* Scott A, and can a diffusion model of propidium iodide (PI) uptake quantify pore shrinkage (repair) over subsequent refrigerated days while colony counts remain suppressed?

## Methods
Early-stationary *L. monocytogenes* Scott A (CIP 103575) grown in TSBYE at 37 °C. HPP in a 2 L Alstom ACB isostatic press: 400 MPa, 8 min, 8 °C; come-up and decompression each 2 min; samples precooled to 8 °C. After treatment, cells stored at 8 °C. PI (1.25 µM) time-lapse confocal microscopy (30 min, 1 fps) on days 0 (1 h post-HPP), 1, 2, 3, and 4. Untreated negative control; heat-killed positive control (80 °C, 40 min). k-means clustering of PI intensity curves. Mass-transfer model (modified Zarnitsyn et al. 2008) to estimate effective pore radius R. Spread-plate counts on non-selective TSA-YE before HPP and on days 0, 1, 2, 3, and 7; LOD 1.00 log CFU/mL, LOQ 2.40 log CFU/mL. Plate-count n = three biological replicates.

## Sample / data
Microscopy: 318 bacteria in 30 fields of view; PI-positive n = 118, 49, 21, 44, and 27 on days 0–4 (lowest and average per day 20 and 45 cells). Untreated n = 20; heat-treated n = 39 (Table 3). Model constants include V_cell = 0.7 × 10^−18 m³ taken from *E. coli* literature (Table 2).

## Claim-ready facts
- **Design:** laboratory challenge study: HPP of broth-grown *L. monocytogenes* plus single-cell PI microscopy, diffusion modeling, and plate counts during 8 °C storage
- **Population / model:** *Listeria monocytogenes* Scott A (CIP 103575), early stationary phase in TSBYE; not a food matrix
- **n:** 318 pressure-treated cells imaged over 4 days (cluster counts in Table 3); viable counts in three biologically independent replicates (Figure 8)
- **Intervention / comparator:** 400 MPa / 8 min / 8 °C versus untreated cells and versus heat-killed cells (80 °C / 40 min)
- **Primary endpoint:** PI fluorescence intensity over 30 min (proxy for membrane pore size); modeled effective pore radius (nm); viable plate counts (log CFU/mL)
- **Primary result:** HPP produced PI-permeable membrane pores. Lowest-slope (least-damaged) cluster: normalized FI at 30 min fell from 0.14 on day 0 to 0.02 on day 4 (seven-fold) (Figure 3). Modeled mean pore radius declined from 1.338 nm on day 0 (95% Bonferroni CI 1.296–1.380) to 0.809 nm on day 4 (0.702–0.915) (Table 4). Day 0 radius (mean 1.338, SD 0.0014) was higher than later days (p < 10^−6); days 1–2 differed from days 3–4 (p < 10^−6) (Section 3.2). Weighted linear regression described pore-size decay; authors extrapolate closure when R < PI molecular radius (0.6 nm; Table 2). Plate counts: 400 MPa / 8 min / 8 °C reduced viable cells by 7.79 ± 0.82 log CFU/mL to below LOQ; counts stayed below LOQ through day 4 and exceeded LOQ only on day 7 (Section 3.3; Figure 8). Untreated cells remained PI-negative; heat-killed cells reached maximum FI by 30 min (Section 3.1).
- **Cannot show:** inactivation or repair in a real food; spore kill; that PI-positive cells are dead (authors argue the opposite: sub-lethal injury with repair); exact number of physical pores (model uses one effective area); generalization to other HPP cycles or species (Discussion).

## Key findings
- TEM from the authors’ prior work is cited as showing membrane perforation after 400 MPa, 15 min (Figure 1); the present HPP cycle is 400 MPa, 8 min, 8 °C. Pore morphology is **previously measured (TEM)** plus **modeled** from PI diffusion, not newly TEM-imaged at 8 min.
- Cell-to-cell damage was heterogeneous (three slope clusters); total PI-positive cells declined over days, interpreted as repair rather than outgrowth because plates remained below LOQ (Discussion).
- Mechanism **proposed**: HPP-linked membrane-protein denaturation and phospholipid liquid-crystalline-to-gel transition (cited Pagán and Mackey, Winter and Jeworrek, etc.), creating pores that then reseal approximately linearly on a days scale (Discussion).
- Industry implication stated: estimated resealing time could inform pressure strength and holding time so that injured cells cannot recover (Introduction; Conclusion).

## Limitations (as stated by the authors, or evident from the methods)
- Broth system, one strain, one cycle (400 MPa, 8 min, 8 °C).
- V_cell, membrane thickness, and viscosity constants borrowed from *E. coli*/literature (Table 2); local sensitivity identified V_cell, η, and h as influential, though predicted closure time was robust to ±10–50% V_cell (Section 3.2).
- Single-pore-area assumption; PI-only probe cannot resolve pores smaller than PI.
- Small PI-positive n on day 4 (n = 27 total; 7 in lowest-slope cluster) limited day 3 versus day 4 significance.
- Possible underestimation of pore size on days 0–2 if FI approached saturation (Discussion).

## Relevance to our research question
Direct evidence that 400 MPa / 8 min / 8 °C is not an instantaneous complete kill: ~7.8 log plate reduction with a PI-permeable injured subpopulation whose pores shrink over 4 days while population growth is arrested—so a named cycle’s “safety” depends on whether repair is allowed during cold storage.

## Open questions / things to verify
- Figure 8 raw CFU values other than the 7.79 ± 0.82 log drop and LOQ/day-7 qualitative pattern are in Supplementary File 2, not in the extracted body text.
- TEM cycle (400 MPa, 15 min) is not identical to the microscopy cycle (8 min).
