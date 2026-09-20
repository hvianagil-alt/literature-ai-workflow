# Structure benchmark — 2026-09-20-hpp-rerun

**Our kind:** journal-style **narrative** process review (not systematic, not scoping, not an EFSA opinion).  
**Our organising principle:** by **question** (when a named hydrostatic cycle is not the same safety or quality outcome), with brief Methods early; matrix and neighbouring technologies appear as evidence, not as equal catalogue chapters.  
**Application overlay:** journal paper (`review/memory/applications.md`) — full-length narrative; findings and methods; brief Methods; teach in the Introduction.  
Memory consulted: review/memory/food-science.md  
**Also read (length/Methods only):** `review/memory/applications.md`. Generic narrative spine used only as the default journal overlay (Introduction → brief Methods → thematic sections → separate Discussion → Conclusions).  
**Comparators (n=14 narrative/mini reviews in this run, plus 3 kind-contrast papers):** all public OA full texts already in `papers/2026-09-20-hpp-rerun/` (opened for **headings/front matter only**). No extra OA reviews were fetched; included same-field reviews were enough. **Do not import their numbers, log reductions, organisms, or conclusions into `article.md`.** Do not use `review/runs/2026-09-20-scopus-hpp/article.md`.

Narrative / mini-review spines (form models):

| Citekey | Kind | Title shape | Methods sit | Organising principle |
|---|---|---|---|---|
| Zhang2022 | narrative | *Recent Progress in … and Related Kinetics* (flourish) | absent | coefficients / kinetics, then factors (species, pulse, temperature, composition, aW/pH) |
| Braspaiboon2024 | narrative | colon: *Influences on Allergenicity, Bioactivities, …* | absent | protein **source / matrix** |
| Agriopoulou20231 | narrative | *Recent Advances in … — A Review* (flourish) | absent | **dairy matrix** then product type |
| Xia2022 | mini-review | colon: *The Cases of Emerging Combination Patterns* | absent | **combination technologies** (thermal, US, UV, antimicrobials, PEF, CO2) |
| Wu2025 | narrative | phenomenon first, no colon | absent | **technology catalogue** (HPP, then PEF, CAP, HPCD, US) + VBNC |
| Knoerzer2025627 | narrative | colon: *Unlocking the Potential of High-Pressure Thermal Processing* | absent | HPTP mechanism → applications → **equipment / packaging / parameters** |
| Peng2023313 | narrative | colon: *A review* | early `METHODOLOGY` (search years only) | **aquatic matrix** + principles/equipment |
| Houška2022_020223 | narrative | no colon: *Applications in Plant Foods* | absent | plant **matrix** (juices) → HPTP microbes → enzymes → **industrial equipment** |
| LomelíMartín2021_040878 | narrative | colon: *A Review* | absent | aroma **compound class** |
| NavarroBaez2022_051502 | narrative | colon: *A Review* | absent | phenolics: biosynthesis vs extraction |
| SernaHernandez2021_081867 | narrative | colon: *A Review* | absent | milk **components** then dairy products |
| Almoselhy2022_000243 | short narrative | *… for Optimization of Food Processing, Quality, and Safety* | absent | HSH vs **HPH** (shear machine, not hydrostatic) |
| Mukhtar2022 | narrative | long list of technologies *regarding sugarcane juice* | absent | **technology catalogue** on one juice; highlights + graphical abstract (we do not produce a GA) |
| Wiśniewski2023_010014 | narrative overview | em-dash: *An Overview of Challenges and Responses* | absent | pathogen background → HPP parameters / matrix / strain / recovery |

Kind contrast only (not the narrative spine):

| Citekey | Kind | Why not the spine |
|---|---|---|
| Sykora2026 | PRISMA **systematic** review | IMRaD (`2. Methods` → `3. Results and Discussion`); structured search theatre; pooled-parameter analysis |
| Guzel2026 | PRISMA-ScR **scoping** review | IMRaD; maps thermal vs nonthermal in RTE meats; HPP is one technology among many |
| Koutsoumanis2022 | EFSA BIOHAZ **scientific opinion** | Terms of Reference, questionnaires, legal performance criteria — use as the **legal-question** form, not as numbered IMRaD Results |

Front matter pattern among narrative comparators: unstructured abstract + keywords is the majority (Braspaiboon, Wu, Houška, Lomelí, Navarro, Serna, Agriopoulou, Wiśniewski, Knoerzer, Peng, Almoselhy). Zhang uses a *Background / Scope and approach / Key findings* block. Mukhtar adds Highlights and a graphical abstract. **Our kind:** unstructured Abstract (topic map; no citations; no named papers) + ≥4 keywords; no Highlights required; no graphical abstract.

## Heading inventory

| Topic the field uses | In comparators | In our outline (e) | Decision |
|---|---|---|---|
| Title: phenomenon first; often a colon subtitle; avoid *Recent Advances* / *Recent Progress* | Braspaiboon, Xia, Peng, Lomelí, Navarro, Serna, Knoerzer (colon); Zhang & Agriopoulou use flourish titles this workflow fails | (e) starts at Abstract; title kind not yet named in (e) but implied by food-science card | **keep** spine; draft title as colon subtitle naming the phenomenon (named cycle ≠ same outcome). Do not copy flourish titles |
| Unstructured Abstract + keywords | Most MDPI/journal narratives above | (e) §Abstract, §Keywords | **keep** |
| Teach HPP (isostatic liquid, pressure–time–temperature) vs heat in the Introduction | Zhang §1; Braspaiboon §2; Agriopoulou §1; Peng Principles; Xia Introduction | (e) §1 Introduction | **keep** |
| Brief Methods after Introduction | Peng `METHODOLOGY`; Sykora/Guzel IMRaD Methods (wrong kind); most narratives **omit** Methods | (e) §2 Methods early | **keep** as our journal overlay. Do not copy systematic Results. How papers were found lives only here |
| Coefficients: why the same MPa is not the same kill (ice, solute/aW, pH, pulse vs hold, injury assay) | Zhang §3–3.5; Wiśniewski §3.1; Houška modelling subsections | (e) §3 | **keep** (matches food-science card heading *shape*) |
| Injury / VBNC / recovery after HPP | Wu §2.3 (under HPP); Wiśniewski §3.2 recovery | nested in (e) §3 (injury assay: Torrents, Nikparvar, Wu) | **keep nested** in §3. Sample measured injury/VBNC; not a new `##` |
| Legal / 5-log / milk pasteurisation performance criteria | Koutsoumanis (opinion ToRs); Agriopoulou §1 EU novel-food language; Peng intro cites legal milk contrast as a neighbouring topic | (e) §4 | **keep** (sample has the opinion + milk systematic + juice bars) |
| Spores / HPTP / adiabatic heating / hurdles | Zhang §3.3; Houška §3; Xia thermal-combination; Knoerzer whole spine; Peng elevated-temperature UHP | (e) §5 | **keep** |
| Quality endpoints that do not track plate counts (enzymes, colour, texture, proteins, aroma, phenolics) | Houška §4 enzymes; Braspaiboon proteins; Lomelí aroma; Navarro phenolics; Serna/Agriopoulou milk components | (e) §6 | **keep** (fold matrix-quality reviews here; do not split into one chapter per commodity) |
| Neighbouring unit operations only to refuse false equivalence (US, PEF, irradiation, HPH shear) | Xia combination chapters; Mukhtar §3–4 catalogue; Almoselhy HSH/HPH; Wu PEF/plasma/US as **equal** heroes | (e) §7 | **keep as refusal chapter**, not a Wu/Mukhtar technology catalogue |
| Separate Discussion (commercial chilled HPP ≠ legal pasteurisation) | Rare in these narratives (they often jump to Conclusions); food-science card requires it | (e) §8 Discussion | **keep** (journal overlay + memory card). Not IMRaD Results |
| Conclusions | Zhang §4; Braspaiboon §4; Agriopoulou §6; Xia concluding remarks; Wu §9; Houška §6; Peng conclusions | (e) §9 | **keep** |
| One chapter per food (milk / juice / meat / aquatic) | Agriopoulou; Serna; Peng; Houška §2; Braspaiboon by protein source | not in (e) | **omit on purpose** — field-typical but hides shared coefficients; memory card allows question-driven departure |
| Equal-time PEF / plasma / ultrasound / HPCD chapters | Wu §§3–6; Mukhtar §3 | not in (e) | **omit on purpose** — protocol: other nonthermals only where measured beside pressure |
| Industrial equipment, cost, installation, canisters | Houška §5; Knoerzer Equipment/Canister; Peng Principles/equipment; Almoselhy lab vs industrial | not in (e) | **omit** — no primary equipment measurements in this sample; name in (d) / one Discussion sentence |
| Energy, packaging integrity, consumer acceptance | Mukhtar intro energy slogans; Knoerzer packaging materials; Agriopoulou consumer-demand intro | not in (e) | **omit** — (d) already lists them as unmeasured |
| Graphical abstract / Highlights | Mukhtar | not in (e) | **omit** (workflow is Markdown text) |

## What matches

Rationale (e) already follows the **food-science** card’s example heading *shapes*: coefficients first; legal performance criteria in their own section; spores / HPTP / cold-chain hurdles; quality that moves against plate counts; neighbouring operations only to refuse false equivalence; Discussion that commercial chilled HPP is not legal pasteurisation. That is the same argument spine the card records as a **justified departure** from commodity or technology catalogues.

Included narrative reviews that organise by **question or coefficient** rather than by grocery aisle are the closest form models: Zhang (factors that change a named cycle), Wiśniewski (parameters, matrix, strain, recovery — under one pathogen), Xia (why single HHP is not enough, then combinations), Navarro (two pressure jobs: biosynthesis vs extraction). Quality-only reviews (Braspaiboon, Lomelí, Houška enzymes) support a dedicated quality heading, which (e) already has as §6 rather than as milk-then-juice-then-meat.

Methods sit **early and brief**, matching the generic-narrative / journal-paper overlay, not the IMRaD of Sykora or Guzel. Peng is the only included narrative with an early search `METHODOLOGY`; copying that depth of screening theatre into Results or Discussion would be the wrong kind.

## What we omit on purpose

Field-standard sections we will **not** write because this sample has no primary evidence, or because they would force a catalogue:

- **Equipment / cost / installation / canister hardware** (Houška §5; Knoerzer Equipment; Peng equipment types). Neighbouring gap only.
- **Energy, packaging integrity, consumer willingness-to-pay.** Named in rationale (d). One Discussion sentence at most.
- **One `##` per matrix** (milk, juice, meat, aquatic). The sample could fill those chapters, but that organisation hides the shared coefficients the review is arguing.
- **Equal-time chapters for PEF, cold plasma, ultrasound, HPCD, ozone, membranes.** Wu and Mukhtar use that catalogue; this run’s question is hydrostatic pressure and when a named cycle is not one outcome.
- **Graphical abstract.** Mukhtar has one; this workflow does not.
- **IMRaD Results** from Sykora/Guzel. Wrong kind.
- **EFSA questionnaire / ToR appendices** as the article spine. Koutsoumanis informs §4’s *legal-question* form, not the heading list.

## What we should add before drafting

**Nothing at `##` level.** Injury/VBNC is already a bullet under §3 and is measured in this sample; leaving it nested is enough. HPH belongs in §7 (Almoselhy + Szczepańska), not as a co-equal process chapter. Title should be a **colon subtitle** (phenomenon first, then narrative angle); that is front-matter form, not a new section.

Do not invent equipment, energy, or consumer chapters.

## Verdict

**Keep (e).** The outline is a field-typical *question-driven* food-process narrative, not a mis-shaped IMRaD dump. It matches `review/memory/food-science.md` heading shapes and the journal-paper overlay (teach in the Introduction; brief Methods early; separate Discussion). Matrix catalogues (Agriopoulou, Serna, Peng, Houška) and technology catalogues (Wu, Mukhtar) are common in this field; refusing them is the departure the memory card already licenses when the argument is that one set-point is not one safety number. Sykora (systematic) and Guzel (scoping) stay kind contrast. Koutsoumanis stays the legal-criteria form for §4. No heading that this sample measured is missing; no empty equipment/energy/consumer chapter should be added. Draft the title as a colon subtitle and do not copy *Recent Advances* / *Recent Progress* from Zhang or Agriopoulou.
