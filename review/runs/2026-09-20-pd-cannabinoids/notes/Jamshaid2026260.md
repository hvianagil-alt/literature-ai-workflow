# Exploring the Therapeutic Potential of Cannabis Constituents in Parkinson’s Disease: Insights from Molecular Docking Simulations

- **Citation:** Jamshaid A, Aziz M, Raza U, Mazhar R, Shakil MAU, Sajid M, Tang L, Sehgal SA. Medinformatics. 2026;3(3):260–274. DOI: 10.47852/bonviewMEDIN62029324
- **Source file:** papers/2026-09-20-pd-cannabinoids/Jamshaid2026260.txt
- **Extracted:** 2026-09-20

## Research question
Which Cannabis sativa phytochemicals dock most strongly to MAO-B, and is the top complex (Cannabicyclol–MAO-B) stable in molecular dynamics—i.e., a computational screen for PD-relevant MAO-B inhibition?

## Methods
In silico only: ligand structures from public databases; MAO-B PDB 2C65 Chain A; PyRx-v0.8 docking (grid x = 53.9113, y = 149.558, z = 17.1728). Redock of co-crystallized 4CR: RMSD = 1.382 Å. References: Deprenyl −7.3, Rasagiline −7.9, Selegiline −7.3 kcal/mol. Physicochemical/drug-likeness/ADMET/toxicity and PASS bioactivity for Cannabicyclol. Desmond MD 100 ns, 310 K, OPLS-3e, NPT, 53,853 atoms. No wet-lab enzyme assay, cell, or animal experiment.

## Sample / data
Computational: docking affinities of cannabis ligands from −6.1 to −10.8 kcal/mol (Table 5). MD of one complex. Authors state no animal-derived experimental data were used.

## Claim-ready facts
- **Design:** computational (molecular docking + 100 ns MD + ADMET); no experimental biology
- **Population / model:** human MAO-B crystal structure PDB 2C65 (Chain A + FAD)
- **n:** not applicable (in silico); 14 listed cannabis compounds in physicochemical Table 2; docking panel in Table 5
- **Intervention / comparator:** cannabis ligands vs Deprenyl, Rasagiline, Selegiline docking scores
- **Primary endpoint:** docking score (kcal/mol) to MAO-B; MD RMSD of Cannabicyclol complex
- **Primary result:** Cannabicyclol docking score −10.8 kcal/mol vs Deprenyl/Selegiline −7.3 kcal/mol and Rasagiline −7.9 kcal/mol. Other scores include cannabinol −9.6, cannabidiol −8.4, cannabigerol −9.1, cannabielsoin −5.8 kcal/mol (Table 5). MD: ligand RMSD relatively stable to ~23 ns then ~2.8 Å over the remaining trajectory (Section 3.7.1). Redock RMSD 1.382 Å.
- **Cannot show:** actual MAO-B enzyme inhibition, dopamine sparing, neuroprotection, or PD clinical effect; docking is not a Ki/IC50.

## Key findings
- Cannabicyclol contacts listed include Cys172, Tyr435 and Gly58, Ser59, Tyr188, Ile199, Gln206, Lys296 (interaction table).
- Cannabicyclol MW 314.5; predicted BBB logPS = 0.589; Lipinski compliant (text/Table).
- Authors explicitly call for in vitro MAO-B assays and in vivo PD models (Discussion/limitations).
- Graphic abstract claims Cannabicyclol “outperforming” selegiline/rasagiline on docking only.

## Limitations
- Purely computational; no experimental confirmation (authors).
- Single protein target (MAO-B), not α-synuclein, DAT, or cannabinoid receptors as the docking campaign.
- Docking score ≠ inhibitory potency; tautomer/protonation and induced fit not fully captured.
- Selegiline and Deprenyl listed as separate references with identical −7.3 kcal/mol scores.

## Relevance to our research question
Hypothesis-generating only: a cannabis constituent (cannabicyclol, not CBD) may bind MAO-B tighter than some licensed MAO-B inhibitors *in silico*. Does not constitute PD toxin-model evidence.

## Open questions / things to verify
- Table 5 full ligand list vs “top four” narrative (cannabitriol −7.7 is not stronger than several others).
- Whether 2.8 Å ligand RMSD is interpreted as stable enough by a structural biologist.
- No experimental IC50 exists in this paper to compare with selegiline.
