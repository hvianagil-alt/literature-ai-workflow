# A Mathematical Model for the Combination of Power Ultrasound and High-Pressure Processing in the Inactivation of Inoculated E. coli in Orange Juice

- **Citation (as given in the paper / filename):** Rodríguez, Ó., Orlien, V., Amin, A., Salucci, E., Giannino, F., Torrieri, E. (2024). Foods 13(21):3463. doi: 10.3390/foods13213463
- **Source file:** papers/2026-09-20-scopus-hpp/Rodríguez2024.txt
- **Extracted:** 2026-09-20

## Research question

Can a system-dynamics inactivation model, calibrated on ultrasound (US) and HPP separately, predict *E. coli* DSM682 kill when the two nonthermal treatments are applied in sequence to orange juice, and do the combined processes act synergistically?

## Methods

Commercial pressed, pasteurized orange juice (Brähmults) was inoculated with *E. coli* DSM682 to about 5–6 log CFU mL^-1 and held 1 h at room temperature. US: Hielscher UP400St (400 W, 24 kHz), pulsed 10 s on / 10 s off, probes 46 µm and 99 µm, amplitudes 50–100%, jacket at 5 °C so juice stayed ≤20–22 °C; times from ~10 to 60 min (and 720, 1440, 2160 s for combinations). HPP: Avure QFP-6, 300 MPa for 1, 5, 10 min and 400 MPa for 1, 2, 3 min; 0.5% sodium benzoate water at 10 °C. Combination: US with probe B then HPP at the same pressure–time grid. Counts on agar after 24 h at 37 °C. Geeraerd-type ODEs for N and a “critical component” C_C, with k_i and N_i,min functions of intensity, pH and viscosity; calibrated on US and HPP then validated on US+HPP (MATLAB ode15s / Nelder–Mead). Microbial experiments in triplicate (combination table n = 2; HPP table n = 6). pH, °Brix and Brookfield viscosity measured.

## Sample / data

Pasteurized orange juice, pH 3.55–3.61, 10.70–12.43 °Brix, untreated viscosity 23.1 cP. Three juice batches (A, B, C) for HPP and US+HPP.

## Claim-ready facts

- **Design:** Inoculated kinetic challenge; separate US and HPP calibration; sequential US then HPP validation of an ODE model.
- **Population / model:** *E. coli* DSM682 in commercial pasteurized orange juice.
- **n:** Microbial runs in triplicate; HPP inactivation table n = 6; combined US+HPP table n = 2.
- **Intervention / comparator:** Pulsed US (46 or 99 µm) vs HPP 300–400 MPa vs US followed by HPP; untreated inoculated juice.
- **Primary endpoint:** *E. coli* log CFU mL^-1 and log reduction; model R^2.
- **Primary result:** HPP 300 MPa / 10 min: 4.0 ± 0.1 log reduction (from 6.2 ± 0.6 to 2.2 ± 0.2 log CFU mL^-1). HPP 400 MPa / 2 min: 3.9 ± 0.8 log; 400 MPa / 3 min: no colonies detected. Combined US + HPP produced no detectable CFU mL^-1 at 300 MPa / 10 min and at 400 MPa / 10 min for all US pretreatments tested. Combined-model validation R^2 = 0.82.
- **Cannot show:** Native (uninoculated) juice flora; *E. coli* O157:H7; simultaneous (not sequential) US+HPP in one vessel; shelf-life of treated juice; that synergy is more than additivity of two strong treatments at the longest holds.
- **US alone (Table 2):** From 5.1 log CFU mL^-1, probe A reached 3.82 log reduction after 3988 s; probe B 4.42 log after 4044 s, juice temperature 20 °C.
- **US amplitude (probe B):** After 720 s, 0.65 log (46 µm) vs 1.34 log (99 µm); after 60 min, 1.59 vs 3.59 log CFU mL^-1. Acoustic power 98 W vs 195 W. US model fit R^2 = 0.98.
- **HPP 300 MPa (Table 4):** 1 min 0.16 ± 0.02 log; 5 min 1.5 ± 0.1 log; 10 min 4.0 ± 0.1 log. HPP model R^2 = 0.88.
- **US+HPP examples (Table 6):** 400 MPa / 5 min after 1440 s US: 5.4 ± 0.5 log reduction (1.0 ± 0.1 log remaining); 1440 s US + 400 MPa / 2 min described in text as ~5 log, similar to 2160 s + same HPP.
- **Quality side-measurements:** pH and °Brix unchanged after HPP or US+HPP. US cut dynamic viscosity from 23.1 cP to 6.3–4.7 cP.
- **FDA framing:** Authors cite a 5-log *E. coli* O157 juice criterion; DSM682 is not that serotype.

## Key findings

- HPP kill in this juice is strongly time- and pressure-dependent; 400 MPa / 3 min cleared the inoculum, 300 MPa needed 10 min for 4 log (Section 3.2).
- US alone is slower: tens of minutes for 3–4 log at ≤22 °C (Section 3.1).
- Sequence US then HPP reached non-detectable counts at holds where HPP alone still left survivors (e.g. 300 MPa / 10 min after US) (Section 3.3; Table 6).
- The calibrated ODE model transferred to the combination with R^2 = 0.82; long US pretreatments were over-predicted (Section 3.3).
- Small molecules (pH, Brix) were stable; viscosity fell with acoustic energy (Section 3.4).

## Limitations (as stated by the authors, or evident from the methods)

- Juice was already pasteurized; experiment measures inoculated DSM682, not process validation of raw juice.
- Combination n = 2; ND cells in Table 6 have no log-reduction number.
- pH and viscosity terms in the ODE were not calibrated (no designed pH/viscosity grid).
- Probe C (164 µm) was abandoned because intensity >200 W cm^-2 overheated samples.
- Pressure-transmitting medium contained 0.5% sodium benzoate (not in the juice packs).
- No enzyme, vitamin C, colour or sensory data beyond pH/Brix/viscosity.
- Model uses a lumped “critical component” C_C, not a identified biomolecule.

## Relevance to our research question

HPP in orange juice inactivates *E. coli* at 300–400 MPa on a minutes scale; adding power ultrasound before HPP can push counts below detection and is modelled, not only tabulated. Quality endpoints here are limited to pH, Brix and viscosity. The organism is a laboratory *E. coli*, not O157:H7.

## Open questions / things to verify

- Table 6 400 MPa / 1 min after 2160 s US lists 4.1 ± 0.1 log reduction with 1.0 ± 0.1 log remaining — check arithmetic vs the 0 min US control of that block (4.9–5.5 log).
- Text “US 1440 s + HPP 400 MPa for 2 min showed a similar log reduction (5 log)” vs table 400 MPa / 1 min / 1440 s = 3.2 log — confirm which row is “2 min” in the published PDF table.
- Whether ND at 300 MPa / 10 min after US is true synergy or just crossing the detection limit after ~4 log from HPP plus residual US kill.
