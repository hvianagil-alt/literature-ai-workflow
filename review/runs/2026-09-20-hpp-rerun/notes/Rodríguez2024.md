# A Mathematical Model for the Combination of Power Ultrasound and High-Pressure Processing in the Inactivation of Inoculated *E. coli* in Orange Juice

- **Citation (as given in the paper / filename):** Rodríguez Ó, Orlien V, Amin A, Salucci E, Giannino F, Torrieri E (2024). Foods 13:3463. doi:10.3390/foods13213463
- **Source file:** papers/2026-09-20-hpp-rerun/Rodríguez2024.txt
- **Extracted:** 2026-09-20

## Research question
How do power ultrasound (US), HPP, and sequential US then HPP inactivate inoculated *Escherichia coli* DSM682 in commercial orange juice, and can a System Dynamics ODE model predict combined inactivation from the single-technology kinetics?

## Methods
Commercial pressed, pasteurized orange juice (Brähmults) inoculated to ~5–6 log CFU mL^−1. US: Hielscher UP400St, 400 W, 24 kHz, pulsed 10 s on/10 s off, probes 46/99/164 µm amplitude, jacket 5 °C, juice <22 °C in combination runs, 10–60 min or 720/1440/2160 s. HPP: Avure QFP-6, 300 MPa for 1, 5, 10 min and 400 MPa for 1, 2, 3 min; 0.5% sodium benzoate water at 10 °C. Combination: US probe B (99 µm) then the same HPP matrix. Geeraerd-type ODEs for N and critical component Cc; intensity H_US = acoustic power (W), H_HPP = P (MPa). Quality: pH, °Brix, viscosity. Plate counts. HPP table n = 6; combination table n = 2.

## Sample / data
Three juice batches A, B, C prepared in duplicate for HPP and US+HPP. Initial HPP controls 6.2 ± 0.6 (300 MPa series) and 6.2 ± 0.5 log CFU mL^−1 (400 MPa series). US kinetic series started at 5.1 log CFU mL^−1.

## Claim-ready facts

- **Design:** Inoculated laboratory inactivation kinetics plus ODE model calibration/validation; sequential US then HPP.
- **Population / model:** *E. coli* DSM682 in commercial pasteurized orange juice.
- **n:** HPP inactivation Table 4 n = 6; combined US+HPP Table 6 n = 2; three batches.
- **Intervention / comparator:** US alone (amplitude/time) vs HPP 300 or 400 MPa vs US (720–2160 s) followed by those HPP cycles; untreated inoculated juice.
- **Primary endpoint:** *E. coli* log CFU mL^−1 and log reduction; model R^2; pH, °Brix, viscosity (cP).
- **Primary result:** US from 5.1 log: 1.67–1.71 log reduction after 22.1 min (residual 3.4 log); residual 1.3 log after 66.5 min. At 60 min, 99 µm amplitude gave 3.59 log reduction vs 1.59 log at 46 µm; after 720 s, 0.65 vs 1.34 log at 46 vs 99 µm. HPP 300 MPa: 1 min 0.16 ± 0.02 log reduction (6.0 ± 0.5 remaining); 5 min 1.5 ± 0.1; 10 min 4.0 ± 0.1 (2.2 ± 0.2 remaining). HPP 400 MPa: 1 min 1.9 ± 0.8; 2 min 3.9 ± 0.8 (2.5 ± 0.2 remaining); 3 min no colonies detected. US 1440 s + HPP 400 MPa/2 min ≈ 5 log reduction, similar to US 2160 s + same HPP; combined US+HPP yielded no detectable CFU/mL (authors call this synergistic). US model fit R^2 = 0.98; HPP R^2 = 0.88; combination prediction R^2 = 0.82 (abstract). Control juice 10.70–12.43 °Brix, pH 3.55–3.61; HPP and US+HPP did not change pH/Brix. US lowered viscosity from 23.1 cP to 6.3–4.7 cP.
- **Cannot show:** Enzyme inactivation or sensory quality beyond pH/Brix/viscosity. Spoilage flora or pathogens other than this *E. coli* strain. Simultaneous (not sequential) US+HPP. Shelf life of treated juice. FDA 5-log is discussed as a target; combination 5 log is for DSM682 in already-pasteurized juice, not O157:H7.

## Key findings
- Named HPP cycles are not equivalent: 300 MPa/1 min ≈ 0.16 log vs 300 MPa/10 min = 4.0 log vs 400 MPa/3 min = ND. (Table 4)
- Measurement: 400 MPa/2 min ≈ 3.9 log, not complete; 400 MPa/3 min complete for this inoculum. (Table 4)
- Sequential US then 400 MPa/2 min reached ~5 log / ND, whereas 400 MPa/2 min alone left 2.5 log. (Section 3.3)
- Author interpretation: combined treatment is synergistic; model can optimize US time vs HPP. (Abstract, Section 3.3)
- Mechanism grade: cavitation, free radicals, and pressure damage to intracellular components are proposed from literature, not imaged here.

## Limitations (as stated by the authors, or evident from the methods)
- Juice was already commercially pasteurized then re-inoculated.
- Combination n = 2.
- pH and viscosity terms were excluded from calibration for lack of experimental range.
- Temperature rose from 10 to ~20–22 °C under US despite cooling; not isothermal.
- No storage or enzyme data.

## Relevance to our research question
Clear demonstration that pressure–time identity matters: 400 MPa for 2 vs 3 min changes surviving *E. coli* from ~2.5 log to ND, and adding a prior US dose changes 400 MPa/2 min from incomplete to ~5 log/ND. Heat is not the kill step.

## Open questions / things to verify
- Abstract “no detectable CFU” for the combination vs conclusion “5 log CFU mL^−1 reduction” for US 1440 s + 400 MPa/2 min; Table 6 has ND rows—use ND where tabulated, 5 log where stated as reduction.
- US-alone initial 5.1 log vs HPP-alone 6.2 log: do not pool those series as one N0.
