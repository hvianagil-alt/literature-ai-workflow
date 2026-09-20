# Modelling the piezo-protection effect exerted by lactate on the high pressure resistance of Listeria monocytogenes in cooked ham

- **Citation (as given in the paper / filename):** Serra-Castelló, C., Jofré, A., Belletti, N., Garriga, M., Bover-Cid, S. (2021). Modelling the piezo-protection effect exerted by lactate on the high pressure resistance of Listeria monocytogenes in cooked ham. Food Research International. doi: 10.1016/j.foodres.2020.110003 (postprint; published volume 140).
- **Source file:** papers/2026-09-20-scopus-hpp/Serra-Castelló2021.pdf
- **Extracted:** 2026-09-20

## Research question

How do potassium lactate and sodium diacetate change the 400 MPa inactivation kinetics of three *Listeria monocytogenes* strains on sliced cooked ham, and can the lactate “piezo-protection” be quantified with Weibull models?

## Methods

Five cooked-ham batters (pork shoulder, salt 20.7 g/kg, nitrite 0.1 g/kg, etc.): control (no organic acids); 1.4% or 2.8% potassium lactate; 0.1% sodium diacetate; 1.4% lactate + 0.1% diacetate. Product pH 6.04 ± 0.04, a_w 0.974 ± 0.003. Slices 12–14 g were surface-inoculated independently with stationary-phase *L. monocytogenes* CTC1011 (1/2c), CTC1034 (4b) or Scott A (4b) at about 10^7 CFU/g from thawed −80 °C cultures, vacuum packed, and treated at 400 MPa in a Hiperbaric Wave 6000/120 (come-up 2.0 min, release <2 s, water at 13 °C) for holding times 0, 2.5, 3.75, 5, 6.25, 7.5, 8.5, 9.5 and 10 min. Counts on Chromogenic Listeria Agar after 2 h at room temperature; presence below quantification treated as 1 CFU/g and absence as 0.1 CFU/g for modelling. Primary Weibull model on log N/N0; secondary polynomials and a one-step global regression (n = 225 inactivation values for lactate series) in R. Duplicate or triplicate analyses per batch and strain.

## Sample / data

Sliced cooked ham as a ready-to-eat meat model. n = 25 log N/N0 points per strain × formulation for each Weibull fit (Table 2). Global lactate model used 75 points per strain.

## Claim-ready facts

- **Design:** Inoculated challenge on formulated cooked ham; primary Weibull plus secondary/global regression of holding-time kinetics at a single pressure.
- **Population / model:** *L. monocytogenes* CTC1011, CTC1034 and Scott A on vacuum-packed sliced cooked ham.
- **n:** About 10^7 CFU/g inoculum; duplicate/triplicate plates; 25 points per Weibull fit; 225 points in the lactate global regression.
- **Intervention / comparator:** 400 MPa, 0–10 min hold, 13 °C start; formulations with 0 / 1.4 / 2.8% potassium lactate and/or 0.1% sodium diacetate vs acid-free control.
- **Primary endpoint:** Inactivation as log N/N0; Weibull δ (min for first log reduction) and shape p.
- **Primary result:** Lactate reduced HPP kill in a dose-dependent way for all three strains. At 10 min, inactivation was 0.5, 1.46 and 1.29 log lower with 1.4% lactate than control for CTC1011, CTC1034 and Scott A; with 2.8% lactate the gaps were 2.51, 1.75 and 2.35 log. Diacetate alone cut δ by 13%, 31% and 20% vs control. Lactate + diacetate was not statistically different from control (p > 0.05).
- **Cannot show:** Storage growth after HPP (a related “piezo-stimulation” paper is cited separately); other pressures or temperatures; sensory scores (authors say industrial lactate/diacetate levels are accepted, but they only checked appearance); molecular mechanism of piezo-protection.
- **Control Weibull parameters (Table 2):** CTC1011 δ = 5.98 min, p = 3.62 (convex/shoulder); CTC1034 δ = 3.89 min, p = 1.29 (near linear); Scott A δ = 0.70 min, p = 0.47 (concave/tail).
- **2.8% lactate Weibull (Table 2):** CTC1011 δ = 7.39 min, p = 4.48; CTC1034 δ = 7.48 min, p = 1.17; Scott A δ = 2.48 min, p = 0.41.
- **Time for 2-log reduction at 400 MPa (Table 4, global model):** 0% lactate — 7.51, 6.24 and 2.10 min for CTC1011, CTC1034 and Scott A; 2.8% lactate — 8.49, 11.14 and 11.22 min (CTC1034 and Scott A need >11 min).
- **Physicochemical:** Adding lactate/diacetate did not change ham pH or a_w vs control, so piezo-protection is not explained by a_w drop in this matrix.
- **FSIS context:** Authors frame 1-log as the minimum validated post-lethality treatment and 2-log as “increased control.”

## Key findings

- Inactivation curve *shape* is strain-specific and lactate does not change that shape; it lengthens δ (Figure 1; Figure 2).
- Scott A is easiest to drop 1 log (short δ) but tails at long holds; CTC1011 has a long shoulder then a steep drop, and at >6 min was about 3 log more inactivated than the other two strains in control ham (Section 3.1).
- Diacetate sensitised all strains to 400 MPa; combining 1.4% lactate with 0.1% diacetate cancelled the opposing effects (Section 3.2).
- Global models (Table 3) are offered to pick holding time at 400 MPa as a function of added lactate (Table 4).
- Authors recommend a strain pool covering convex, linear and concave kinetics for HPP validation of cooked meats with or without organic acids (conclusions).

## Limitations (as stated by the authors, or evident from the methods)

- Only 400 MPa and ≤10 min; come-up inactivation is absorbed into (log N/N0)_i, not separated.
- Inocula were frozen then thawed (osmotic/cold stress) and exposed to acids only ~30 min before HPP, so this is short-term exposure, not acid-adapted growth.
- Presence/absence coded as 1 and 0.1 CFU/g for fitting.
- Scott A control RMSE was 0.946 with RSS 19.669 — noisier than the meat isolates.
- No independent industrial validation dataset in this paper.
- Sensory impact of acids was not measured here.

## Relevance to our research question

Highly relevant to HPP microbiology in a human RTE meat: shows that a common clean-label antimicrobial (lactate) can *protect* *L. monocytogenes* from 400 MPa, so hurdle combinations are not automatically synergistic. Diacetate went the other way. Kinetics are strain-dependent, which matters for any synthesis of “how HPP inactivates *Listeria*.”

## Open questions / things to verify

- Table 1 literature gaps (control minus lactate) are cited studies, not this experiment.
- Whether piezo-protection holds at 600 MPa commercial cycles.
- Molecular basis (membrane ion transport vs general stress) is hypothesized, not tested.
