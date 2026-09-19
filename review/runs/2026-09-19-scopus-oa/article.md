# GLP-1 receptor agonists, cell-derived vesicles, and delivery systems in a 2026 Scopus open-access slice: a documented mini-review

## Abstract

**Background.** This article reports a pre-specified, fully documented review of a 10-record Scopus open-access BibTeX export (export date 19 September 2026), assembled to test an end-to-end literature workflow (catalog → public PDF fetch → PRISMA → extraction → synthesis). The review question was: what do these records report about GLP-1 receptor agonists (GLP-1 RAs), stem-cell/exosome products, and drug-delivery systems in metabolic disease and closely related settings?

**Methods.** Records were parsed from the user-supplied BibTeX file. Public PDFs were requested only from open-access endpoints (OpenAlex, Unpaywall, Europe PMC, publisher PDFs). Eligibility and exclusions were logged. Findings were taken from retrieved full texts; titles were not used as evidence.

**Results.** Ten records were identified; 0 duplicates. One was excluded as off-topic (yeast genetics). Nine full texts were sought; one gold-OA Elsevier article could not be downloaded. Eight full texts were assessed; one digital weight-management evaluation was excluded because GLP-1 drugs were not the intervention. Seven studies were included. They do not form a single comparable evidence body: three are preclinical delivery/formulation papers (liraglutide–ZnO inhalation; GLP-1 RA microneedle nanoparticles in arthritis; *Phyllanthus* niosomes vs semaglutide in fatty liver), one is an AD-MSC exosome hydrogel for diabetic wounds, one is a 55-trial Bayesian network meta-analysis in prediabetes (16,610 participants), one links semaglutide to PCSK5-dependent angiogenesis after myocardial infarction, and one develops a diabetes medication-satisfaction questionnaire that included GLP-1 users.

**Conclusions.** In this slice, the only human comparative efficacy data for GLP-1/GIP–GLP-1 drugs are from Wu et al.’s prediabetes network meta-analysis. Delivery papers are animal or in-vitro. This is not a field-wide systematic review; it is an auditable reading of seven retrieved papers plus a PRISMA trail for the export.

## Keywords

GLP-1 receptor agonists; drug delivery; extracellular vesicles; PRISMA; open access; Scopus

## 1. Introduction

GLP-1 RAs, vesicle-based biologics, and enabling delivery systems are often discussed together in metabolic-disease research, but a small database export will usually mix those themes with off-topic OA hits. The present paper does not claim comprehensive coverage of those fields. It answers a narrower, checkable question: **what is actually in this 10-paper Scopus OA export, after public PDFs are fetched and eligibility is applied?**

The protocol was written before retrieval (`review/runs/2026-09-19-scopus-oa/protocol.md`). Defaults were used because the user asked to fetch PDFs, keep a PRISMA table, log effort per phase, and write a citation-backed article.

## 2. Methods

### 2.1 Search and sources

No new database search was run. Identification is the user-uploaded Scopus BibTeX file (`identification.bib`; header “EXPORT DATE: 19 September 2026”). All 10 entries are 2026 articles tagged by Scopus as gold open access.

### 2.2 Eligibility

**Include** if the full text addresses at least one of: (i) GLP-1 / GLP-1 RA / liraglutide / semaglutide / related incretin drugs; (ii) stem cells, MSCs, or exosomes/EVs as therapy or carrier; (iii) a delivery system (nanoparticles, microneedles, niosomes, hydrogels, inhalation carriers), **and** the setting is metabolic disease or a closely related inflammatory/repair context.

**Exclude** if there is no such link, if the PDF is missing, or if the PDF is unreadable. Title-only exclusion was used only when the topic was unambiguous.

### 2.3 Retrieval

`scripts/fetch_oa_pdfs.py` requested public PDFs (OpenAlex → Unpaywall → Europe PMC → publisher conventions → doi.org). Files were kept only if the body started with `%PDF-`. Paywalled or pirate sources were not used. Unpaywall queries used the run owner’s contact email.

### 2.4 Extraction and synthesis

Each included PDF was converted locally with pypdf; structured notes follow the paper-extraction template. The comparison table was built from notes, not from memory. The narrative below only uses facts that appear in those notes/table. If a number was not in the extractable text, it is marked **not stated**.

### 2.5 Usage logging (token estimates)

Cursor does not expose billed model-token counts to this workflow. `usage-log.jsonl` stores **character counts / 4** as a token *estimate*, plus HTTP call counts for fetching. Screening/extraction estimates use the size of locally extracted PDF text and are **upper bounds** on model-facing tokens (the model did not necessarily ingest every page in one prompt). Do not treat these figures as an invoice.

| Phase | Items | HTTP calls | Est. total tokens (chars/4) | What was measured |
|---|---|---|---|---|
| workflow | — | 0 | 0 | Skills/scripts committed before fetch |
| discovery | 10 records | 0 | 3,899 | BibTeX parse |
| fetching | 10 DOIs | 48 | 2,224 | OA PDF requests |
| screening | 10 | 0 | 210,434 | Upper bound on extracted PDF text |
| extraction | 7 included | 0 | 214,677 | Upper bound + notes |
| table | 7 | 0 | 5,744 | Notes → table |
| synthesis | 1 article | 0 | (this file; logged after write) | Article |

## 3. Results

### 3.1 Study selection (PRISMA)

| Step | n |
|---|---|
| Records from Scopus export | 10 |
| Additional records | 0 |
| Duplicates removed | 0 |
| Records screened | 10 |
| Excluded at title | 1 (Li 2026: yeast plasmids) |
| Sought for retrieval | 9 |
| Not retrieved | 1 (Huang 2026: IJPX gold OA, no public PDF body) |
| Full text assessed | 8 |
| Excluded at full text | 1 (Barrett 2026: digital weight-management programme) |
| **Included** | **7** |

Full reasons: `prisma.md` and `screening.json`.

### 3.2 Study characteristics

Included studies are heterogeneous (see `table/literature-table.md`).

**Delivery / formulation (preclinical).** Jeong et al. engineered zinc-oxide carriers for **liraglutide** inhalation; after intratracheal LG@ZO-3 they report relative bioavailability of about 60% versus subcutaneous injection in healthy rats and 51% in alloxan-diabetic rats (PK n=4/group) [1]. They contrast that with marketed oral semaglutide bioavailability below 2%; that comparison is to the product literature, not an oral arm in their rats [1]. Zhang et al. loaded GLP-1 RAs into silk-fibroin nanoparticles (encapsulation ~28–33%; ~60% released by day 14) inside dissolving microneedles aimed at arthritic joints; disease model is CIA rats, not diabetes [2]. Khater et al. gave *Phyllanthus niruri* niosomes (225.1 ± 19.6 nm; EE 73.5 ± 4.2%; n=8/group) in high-fat-diet rats and report GLP-1R-dependent benefit that was reversed by exendin 9–39, with semaglutide as a comparator [3].

**Exosome hydrogel (preclinical).** Chen et al. report an adipose-MSC exosome / *Spirulina* hydrogel ± laser in a diabetic rat wound model, with in-vitro antimicrobial and M2/angiogenesis effects [4]. Exact animal n per group is **not stated** in the extracted text [4].

**Clinical synthesis.** Wu et al. included 55 RCTs (16,610 participants; 37 interventions) of anti-prediabetic drugs [5]. Versus placebo they report HbA1c MD −0.94 to −0.27%, FPG MD −26.42 to −0.15 mg/dL, and weight MD −13.59 to −5.99 kg [5]. Highlighted: semaglutide 2.4 mg SC weight MD −13.59 kg (95% CI −17.30 to −9.91) and HbA1c MD −0.39% (−0.55 to −0.25); tirzepatide 15 mg FPG MD −9.58 mg/dL (−12.00 to −7.15) [5]. They conclude GLP-1 RAs, GIP/GLP-1 RAs, and TZDs looked favorable, with 2.4 mg semaglutide SC and 15 mg tirzepatide as their preferred pair for glucose and BMI among included interventions [5]. Limitations they state include few trials per class, heterogeneity, and incomplete safety data [5].

**Mechanism / PRO.** Guo et al. show PCSK5 up-regulation after MI and state that semaglutide’s angiogenic/repair effects were partly PCSK5-dependent [6]. Boye et al. developed the PSMD satisfaction questionnaire (concept elicitation T1D n=10, T2D n=20; cognitive T1D n=5, T2D n=10); among cognitive T2D participants, 30% used an injectable GLP-1 RA with orals and 10% a GIP/GLP-1 RA [7]. That paper does not estimate drug efficacy [7].

**Not used as evidence.** Huang et al. (SRT1720 exosome-mimetic nanovesicles in diabetic cerebral infarction) would likely have been eligible on title but is **not retrieved**. Barrett et al. retrieved but excluded (behavioural digital programme). Li et al. retrieved and off-topic.

### 3.3 Synthesis

There is **no shared primary endpoint** across the seven papers. What can be said without stretching:

1. **Human drug-effect estimates for incretins in this set come from one NMA** (Wu et al.), in **prediabetes**, not from the delivery papers [5].
2. **Non-injectable GLP-1 RA delivery is only preclinical here:** pulmonary liraglutide–ZnO [1], transdermal microneedle-NP GLP-1 RAs in RA [2], and oral niosomes of a plant extract acting through GLP-1R [3].
3. **Vesicle products** appear as AD-MSC exosomes in a diabetic-wound hydrogel [4], not as a GLP-1 formulation.
4. **Semaglutide** is used as a comparator or mechanism probe (Khater; Guo) as well as an NMA node (Wu) [3,5,6].
5. **Patient-facing GLP-1 experience** is represented only by a qualitative PRO development sample [7].

Disagreement is mostly **non-comparable designs**, not conflicting point estimates. Zhang studies RA joints [2]; Jeong studies lung PK [1]; Wu pools RCTs in prediabetes [5]. Treating them as one “effect of GLP-1 delivery” would be incorrect.

## 4. Discussion

This export was too small and mixed to support a state-of-the-art survey of GLP-1 RAs, stem cells, or drug delivery. Several 2026 OA papers that Scopus returned are only loosely related (questionnaire; MI biology; a weight-management service). That is expected from a simple keyword search and is why PRISMA reasons are listed rather than smoothed over.

Accuracy limits: PDF text extraction was imperfect (column breaks, missing n in Chen et al. [4]). We did not guess those numbers. Huang et al. remains a hole: Unpaywall lists gold OA without `url_for_pdf`.

For a next iteration, re-run Scopus with a tighter query (e.g. GLP-1 AND (nanoparticle OR microneedle OR niosome OR “pulmonary delivery”)) and download the Huang PDF from a browser session if the publisher allows.

## 5. Conclusions

From this 10-record OA export, seven papers can be cited. Only Wu et al. provide pooled human efficacy/safety numbers for GLP-1/GIP–GLP-1 drugs [5]. Delivery and exosome papers are animal or in-vitro [1–4]. Claims in this article are limited to those sources; nothing was filled in from memory.

## References

1. Jeong J-H, Han C-S, Kang J-H, Kim D-W, Park C-W. Morphology-driven zinc oxide biointeractive carriers with biological barrier modulating effects for pulmonary delivery of liraglutide. *J Nanobiotechnology*. 2026;24:446. doi:10.1186/s12951-026-04085-y
2. Zhang H, liu Y, Zhang S, Wang Z, Zhang X, Zhang Y, Zhang J, Liang S, Li C, Su M, Tian Z, Luo L. Microneedle patches deliver targeted GLP-1RAs-loaded nanoparticles for the treatment of rheumatoid arthritis. *J Nanobiotechnology*. 2026;24:265. doi:10.1186/s12951-026-04261-0
3. Khater SI, Hussein MMA, Abdel-Magied SS, Lotfy MM, khamis T, Abdelaziz S, Mostafa M, El-Shaer NO, El-Emam MMA. Phyllanthus niruri niosomes ameliorate obesity-induced hepatic steatosis in rats via modulating MALAT1/miR-206/GLP-1R signaling and hepatic lipid metabolism. *Biol Res*. 2026;59:27. doi:10.1186/s40659-026-00682-1
4. Chen W, Hong J, Wei Y, Ye J, Wu Q. Novel approach for diabetic wound healing: adipose-derived mesenchymal stromal cells Exo@SPHydrogel combined with laser therapy. *npj Regen Med*. 2026;11:15. doi:10.1038/s41536-026-00459-w
5. Wu Y, Wang Z, Tuersun A, et al. Efficacy and safety of anti-prediabetic drugs in patients with prediabetes: a Bayesian network meta-analysis. *BMC Med*. 2026;24:174. doi:10.1186/s12916-026-04705-2
6. Guo J, Ma S, Ma J, et al. PCSK5 promotes angiogenesis and cardiac repair after myocardial infarction. *Nat Commun*. 2026. doi:10.1038/s41467-026-72148-7
7. Boye KS, Stewart KD, Matza LS, Soucier-Ernst D, Houle C, Goetz I, Patel H, Kanu C. Development of the Patient Satisfaction with Medication for Diabetes (PSMD) questionnaire. *J Patient-Rep Outcomes*. 2026;10:73. doi:10.1186/s41687-026-01037-w

### Identified but not included (not cited as evidence)

- Li A, Zhao Q, Yang Z, et al. A hybrid system enables plasmid copy number control in yeast. *Nat Commun*. 2026. doi:10.1038/s41467-026-75973-y — excluded, off-topic.
- Barrett S, et al. Evaluation of the experience of people referred under the NHS enhanced service incentive for obesity to the NHS digital weight management programme. *BMC Public Health*. 2026;26:638. doi:10.1186/s12889-026-26203-z — excluded, wrong intervention.
- Huang Q, Zhao F, Sun B, Yang X, Chen M. SRT1720-loaded exosome-mimetic nanovesicles promote mitophagy via SIRT1/PARKIN activation to ameliorate diabetic cerebral infarction in a preclinical rat model. *Int J Pharm X*. 2026;12:100639. doi:10.1016/j.ijpx.2026.100639 — not retrieved.

## Supplementary files (this run)

- Protocol: `review/runs/2026-09-19-scopus-oa/protocol.md`
- PRISMA: `review/runs/2026-09-19-scopus-oa/prisma.md`
- Usage log: `review/runs/2026-09-19-scopus-oa/usage-log.jsonl`
- Table: `review/runs/2026-09-19-scopus-oa/table/literature-table.md`
- Notes: `review/runs/2026-09-19-scopus-oa/notes/`
