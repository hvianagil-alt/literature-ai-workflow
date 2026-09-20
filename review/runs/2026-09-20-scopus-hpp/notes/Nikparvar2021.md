# A Diffusion Model to Quantify Membrane Repair Process in Listeria monocytogenes Exposed to High Pressure Processing Based on Fluorescence Microscopy Data

- **Citation (as given in the paper / filename):** Nikparvar, B., Subires, A., Capellas, M., Hernandez-Herrero, M., Crauwels, P., Riedel, C.U., Bar, N. (2021). Front. Microbiol. 12:598739. doi: 10.3389/fmicb.2021.598739
- **Source file:** papers/2026-09-20-scopus-hpp/Nikparvar2021.pdf
- **Extracted:** 2026-09-20

## Research question

After 400 MPa HPP, do *Listeria monocytogenes* Scott A cells that take up propidium iodide (PI) reseal pressure-made membrane pores over days, and can a diffusion model estimate pore radius from fluorescence time-lapse?

## Methods

Early-stationary *L. monocytogenes* Scott A (CIP 103575) in TSBYE was pressurised at 400 MPa for 8 min at 8 °C in an Alstom ACB 2 L press (come-up and decompression 2 min each), then stored at 8 °C. At 1 h (day 0) and days 1–4, cells were pelleted, resuspended in DPBS, immobilised under 2% low-gelling agarose, and overlaid with 1.25 µM PI during 30 min confocal time-lapse (1 fps, 63×). Heat-treated cells (80 °C, 40 min) set Imax; untreated cells were the negative control. Mean red fluorescence per cell was clustered with k-means. A mass-transfer model (adapted from Zarnitsyn et al. 2008) converted intensity to an effective pore radius R. Plate counts on TSAYE were taken before HPP and on days 0, 1, 2, 3 and 7 (LOD 1.00 log CFU/mL; LOQ 2.40 log CFU/mL). TEM images of pores were cited from the authors’ prior 400 MPa / 15 min work.

## Sample / data

318 PI-positive cells in 30 fields of view over 4 days (n per day 118, 49, 21, 44, 27 on days 0–4). Lowest-slope (least damaged) cluster sizes: 98, 12, 11, 10, 7 cells. Plate counts: three biological replicates. Model constants for Vcell, membrane thickness and viscosity were taken from *E. coli*/literature (Table 2), not measured on *Listeria*.

## Claim-ready facts

- **Design:** Single-cell fluorescence microscopy plus mechanistic diffusion model; parallel viable plate counts after one HPP condition.
- **Population / model:** *L. monocytogenes* Scott A in TSBYE (not a food matrix); PI as a pore probe.
- **n:** 318 imaged PI-positive cells; plate counts n = 3 biological replicates.
- **Intervention / comparator:** 400 MPa, 8 min, 8 °C vs untreated (no PI uptake) and heat-killed (maximum PI).
- **Primary endpoint:** Normalised PI fluorescence over 30 min; estimated pore radius (nm); viable log CFU/mL.
- **Primary result:** Mean pore radius in the least-damaged cluster fell from 1.338 nm on day 0 (CI 1.296–1.380) to 0.809 nm on day 4 (CI 0.702–0.915). HPP cut viable counts by 7.79 ± 0.82 log CFU/mL to below LOQ; counts stayed below LOQ through day 4 and exceeded LOQ only on day 7.
- **Cannot show:** That PI-positive cells are “dead”; food-matrix HPP; other pressures/times; individual pore counts (model uses one effective area); that repair is the only reason PI uptake slows.
- **PI-intensity trend:** Final normalised FI of the lowest-slope cluster fell from 0.14 on day 0 to 0.02 on day 4 (seven-fold).
- **Statistics:** Day-0 radius > later days (p < 10^-6); days 1–2 vs 3–4 also differed (p < 10^-6); day 3 vs 4 was not significant (small n on day 4).
- **Linear repair:** Weighted least squares on the lowest-slope cluster; authors treat repair of pores <5 nm as approximately linear in time.
- **Growth arrest:** Population lag of at least 4 days at 8 °C after this HPP; colony formation recovered by day 7.
- **Heterogeneity:** k-means produced low/mild/high slope clusters every day (Table 3), i.e. mixed damage in one treated population.
- **Sensitivity:** Local ±10% perturbation: model R was most sensitive to Vcell, η and h (relative |S| ≈ 0.38); predicted closure time was robust to those perturbations.

## Key findings

- HPP at 400 MPa / 8 min / 8 °C made membranes PI-permeable, consistent with pores (abstract; TEM from prior work).
- PI diffusion into the least-damaged PI-positive cells slowed over 4 days, which the calibrated model reads as shrinking effective pore radius (Figures 4–5).
- PI-positive cells are therefore treated as sub-lethally injured and capable of resealing, not as uniformly dead (abstract; Discussion).
- Plate counts stayed below LOQ during the repair window, so membrane resealing and colony formation are not the same process on the same clock.
- Authors propose using estimated resealing time to think about HPP strength/hold in industry, while warning the numbers are specific to this strain and this 400 MPa / 8 min / 8 °C treatment.

## Limitations (as stated by the authors, or evident from the methods)

- Broth, not food; 8 °C “abuse” storage, not a product chill chain.
- Effective single-pore-area assumption; pores smaller than PI are invisible.
- Vcell and membrane thickness borrowed from *E. coli*.
- FI–concentration linearity assumed; possible underestimation of large pores on days 0–2 if intensity nears saturation.
- Cell numbers drop over days (fewer red cells), which may mix true repair with loss of PI-positive cells.
- Microscopy protocol (agarose, PI delivery delay ~8 min) is specific.
- No independent physical measurement of pore size.

## Relevance to our research question

Mechanistic HPP paper: inactivation is not only immediate kill. After 400 MPa, some *L. monocytogenes* remain PI-permeable yet reseal pores over days while the population cannot form colonies, then grow later. That matters for how we interpret “inactivation” and for refrigerated foods where injured cells can recover.

## Open questions / things to verify

- Received/accepted dates on the Frontiers page look internally inconsistent (received 25 August 2021 vs 12 April 2021 accepted) — bibliographic only.
- TEM pores are from 400 MPa / 15 min, not the 8 min run used for PI.
- Whether the same linear resealing holds in ham, juice or milk.
- Day-1 to day-2 radius did not fall (1.191 vs 1.221 nm); authors note lag or variability.
