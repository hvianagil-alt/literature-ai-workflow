# Structure benchmark — 2026-09-20-dr-drug-delivery

**Our kind:** journal-style **narrative** review (not systematic/meta; not a short note).  
**Our organising principle:** **delivery constraint** for DR/DME (ocular barriers and routes → bolus anti-VEGF duration and a refillable port → biodegradable DEX implants → longer-acting FAc implants → experimental posterior nanocarriers), not a catalogue of nanoparticle chemistries, not a catalogue of every DR treatment (laser, vitrectomy, gene therapy), not search-batch order.  
**Memory consulted:** review/memory/nanomedicine.md; review/memory/endocrinology.md; review/memory/generic-narrative.md  
**Application overlay:** review/memory/applications.md — journal article / “just go” row (full narrative length; findings and methods in extraction; brief Methods; teach in the Introduction).  
**Comparators (n=14):** included review/consensus full texts in this sample only. Headings opened in `papers/2026-09-20-dr-drug-delivery-found/` and `papers/2026-09-20-dr-drug-delivery-gapfill/`. No extra OA form-only reviews were fetched; the sample already supplies same-field, same-kind spines. **Form only** — do not import their numbers, quoted trials, or organisms into `article.md` except where that paper is already included science.

| Comparator | Kind (as labelled) | Title shape | Methods? | Organising principle (headings) |
|---|---|---|---|---|
| Kim2021_010108 | narrative review | colon subtitle; no “narrative review” | absent | intraocular PK → strategies to extend IVT duration (implants, micro/nano, hydrogels, port) → non-IVT routes |
| Wang2024_347864 | narrative review | “Recent advances in …” (avoid this flourish) | absent | DR pathophysiology → laser/surgery/drugs/gene → drug-delivery system (by nano platform) |
| Liu2021_294807 | narrative review | “Progress of …” (avoid) | absent | traditional DR therapies then nanotech by use (prevention, treatment, delivery/monitoring, regeneration) |
| Tsung2023_612976 | narrative review | topic name, no colon-kind | absent | polymer class → formulation class → anterior vs posterior **disease** |
| Ahmed2023_25169 | comprehensive narrative | colon; “a Comprehensive Review” | absent | anatomy → all ocular diseases → barriers → routes → dosage forms → nano platforms |
| Cao2022_931759 | narrative review | topic name (NPs + toxicity) | absent | NP chemistry (organic/inorganic) → function → toxicity by particle type |
| Jacob2022_030533 | narrative review | em-dash; “Recent Advances” (avoid) | absent | eye anatomy/barriers → lipid platforms (SLN, NLC, NE, liposomes) |
| Swetledge2021_07459 | narrative review | colon subtitle | absent (Background) | **tissue** (cornea → iris/ciliary → lens → choroid → retina), each with biodistribution then applications |
| Kartı2021_81220 | invited mini-review | topic sentence (DEX place in DME) | absent | major DEX trials → meta-analyses → expert recommendations → **safety** |
| Spinetta2023_102461 | narrative / consensus review | colon; “A Review of …” | absent | **country guidelines** then Discussion nested on clinical questions (first-line, switch, IOP, cataract) |
| Furino2021_654168 | narrative update | colon; “An Update” | absent | pathophysiology → **drug class** (anti-VEGF agents then steroids then emerging) |
| Liberski2022_169424 | comparative review | colon; “A Review” | absent | pathogenesis → two molecules → **trial-by-trial** phase I/II/III |
| Goñi2022_04271 | consensus commentary | topic (IOP after DME implants) | meeting described in body, not a Methods heading | key IOP data → pre-implantation → post-implantation algorithms |
| FusiRubiano2018_01457 | narrative review | colon; “A Review” | absent (explicitly no new studies) | FAc implant → FAME → real-world → **vitrectomized eyes** → regimens/guidelines → cost |

Front matter in comparators (form only): unstructured abstracts are the default; Goñi adds a plain-language summary, Key Summary Points, and a graphical abstract. Keywords are common. Structured IMRaD abstracts are not used. **Our article:** unstructured Abstract; keywords; optional Key Summary Points allowed; no graphical abstract.

## Heading inventory

| Topic the field uses | In comparators | In our outline (e) | Decision |
|---|---|---|---|
| Phenomenon-first title; colon subtitle | Kim; Ahmed; Swetledge; Furino; Liberski; Spinetta; Fusi-Rubiano. Wang/Jacob use “recent advances” (banned flourish). | Title: phenomenon first, colon (delivery constraint / DR–DME) | **keep.** Naming “a narrative review” is a justified extra (endocrinology + generic-narrative cards), not required by Kim-style nanomedicine titles. |
| Unstructured Abstract; keywords; no citations in Abstract | All 14 | Front matter | **keep** |
| Teach DR/DME physiology, BRB, why drops fail | Wang §2 Pathophysiology; Furino §2; Liberski §§2–4; Ahmed Anatomy/Obstacles; Jacob §§2–3; Kim §1; Liu diabetes/complications | Introduction (not a numbered Pathophysiology chapter) | **keep in Introduction.** Endocrinology + generic-narrative: teach in the Introduction; Methods occupies §2. |
| Brief Methods (search/eligibility) | Almost all comparators **omit** Methods | §2 Methods | **keep** as a justified departure (generic-narrative + applications “just go”). How papers were found lives only here. |
| Ocular barriers and administration routes | Ahmed Obstacles + Routes; Kim §4 non-IVT routes; Jacob §§2–3; Wang §4 opening; Swetledge by tissue | §3 barriers/routes (3.1 tears/<5% drops; 3.2 ILM/vitreous as NP filters; 3.3 why IVT exists) | **keep** |
| Licensed bolus anti-VEGF / injection burden / durability | Furino §3.1 by agent; Liberski by molecule and trial; Wang §3.3.1; Kim §2 PK + §3.1–3.2 dose/MW; Liu Anti-VEGF Drugs | §4 bolus anti-VEGF, durability engineering, refillable port | **keep.** Do **not** copy Liberski’s phase-I/II/III file-card spine or Furino’s one-heading-per-antibody catalogue. Nest by duration problem (4.1 half-life/incomplete drying; 4.2 trap vs bispecific as interval strategies, labelled as cited; 4.3 Port Delivery System). |
| Port / refillable delivery | Kim §3.7 Port Delivery Systems | §4.3 | **keep** (sample now has primary Pagoda/Pavilion full texts) |
| Biodegradable DEX implant as its own topic | Furino §3.2.1; Kartı whole paper; Spinetta whole paper; Wang §3.3.2 (steroids, mixed) | §5 DEX implants | **keep** (split DEX from FAc — Furino 3.2.1 vs 3.2.2; Kartı vs Fusi-Rubiano) |
| First-line vs switch / real-world DEX | Kartı Expert recommendations; Spinetta Discussion 9.1–9.6 | §5.2 | **keep** |
| Vitrectomized eyes (DEX) | Kartı trials narrative (CHAMPLAIN); Spinetta nested in discussion | §5.3 | **keep** |
| DEX safety (IOP, cataract) as a **named** heading | Kartı **SAFETY OF DEX IMPLANT ADMINISTRATIONS**; Spinetta 9.7–9.10 IOP/cataract; Goñi (both implants) | previously only implied inside §5.1 | **add nest 5.4** IOP and cataract as DEX constraints. Sample already measured/compiled this; endocrinology card splits safety when the sample has it. |
| Longer-acting FAc implant | Furino §3.2.2; Fusi-Rubiano whole paper; Tsung implants as material contrast; Kartı intro contrast | §6 FAc + DEX-to-FAc switches | **keep** |
| FAME / three-year FAc and real-world | Fusi-Rubiano FAME + REAL WORLD; Goñi collates FAc IOP series | §6.1–6.2 | **keep** (cite Fusi-Rubiano as secondary for FAME; Singer still not retrieved) |
| IOP monitoring as translational constraint (both implants) | Goñi whole paper (pre/post implantation); Spinetta 9.8; Fusi-Rubiano Adverse Effects | §6.3 | **keep** for FAc; DEX IOP also named in new 5.4. Do not invent a third peer `##` that only repeats Goñi. |
| Vitrectomized FAc eyes | Fusi-Rubiano **VITRECTOMIZED EYES** | previously missing as a nest under §6 | **add nest 6.4.** Fusi-Rubiano is already assigned to §6; sample supports the heading. |
| Experimental nanocarriers aimed at diabetic retina | Wang §4 by platform; Liu nanotech-in-DR; Kim §3.4 by particle type; Cao by chemistry; Jacob lipid platforms; Tsung formulation classes; Swetledge by tissue | §7 by **route and whether a retinal endpoint was measured** (topical HA-apatinib; IVT peptide NP; ocusert without retinal endpoint; toxicity) | **keep this question-driven split.** Do **not** copy Kim/Cao/Jacob/Tsung/Ahmed one-heading-per-platform catalogues (nanomedicine card: not an encyclopaedia of materials). |
| Nano toxicity as constraint (arrival ≠ safe function) | Cao §§4–5 toxicity + assessment challenges | §7.4 + Discussion | **keep** nested under experimental carriers; Cao’s particle-by-particle toxicity encyclopaedia is omitted |
| Separate Discussion | Spinetta §9 (best clinical-review model); others often jump to Conclusions only | §8 Discussion | **keep** separate (generic-narrative; endocrinology: what cannot be pooled; nanomedicine: arrival ≠ function) |
| Conclusions in running prose | all | §9 | **keep** |
| Laser photocoagulation as a treatment chapter | Wang §3.1; Liu Laser Therapy | — | **omit.** Sample has no primary laser measurements. Neighbouring topic; one Discussion sentence if needed. |
| Vitrectomy as a DR treatment chapter | Wang §3.2; Liu Vitrectomy | only as a **modifier** of implant PK (§5.3, new 6.4) | **omit** as a peer treatment chapter |
| Gene therapy / senolytics / “other drugs” | Wang §3.3.3–3.4; Liu gene nanocarriers for regeneration | — | **omit.** No primary gene/senolytic full texts in this sample. |
| Anterior-segment disease encyclopaedia | Ahmed diseases; Tsung §4.1 glaucoma/uveitis/dry eye; Jacob topical lipid focus | — | **omit.** Question is posterior DR/DME delivery. |
| National-guideline-by-country spine | Spinetta §§2–8 | — | **omit.** Copy Spinetta’s **Discussion nests** (first-line, switch, IOP), not the country catalogue. |
| Trial-by-trial phase I/II/III | Liberski §§7.1–7.2 | — | **omit.** Hinge trials get design+result; supporting papers grouped. |
| Cost-effectiveness chapter | Fusi-Rubiano “WILL IT BE COST EFFECTIVE…” | — | **omit.** No primary cost study in the sample. Neighbouring topic in (d). |
| Diagnostic NP / imaging / organoids | Cao §2.2 diagnosis; Liu prevention/imaging; Cao §5.2 human 3D model | — | **omit.** No primary imaging-NP or organoid measurements here. |
| Microneedles, iontophoresis, suprachoroidal as peer chapters | Tsung §3.8; Ahmed Iontophoresis/Juxtascleral; Kim §4.3–4.5 | — | **omit** as chapters (rationale (d): only review mentions). May appear as a Discussion clause. |
| Generic `## Results` dump | none of these narratives | — | **omit** |
| Equipment / energy / consumer acceptance | none | — | **omit** (no measurements) |
| Graphical abstract | Goñi only | — | **omit** (workflow: text Markdown) |

## What matches

Same-field ocular-delivery and DME-implant reviews teach anatomy and barriers, then split **clinical payloads** (anti-VEGF proteins vs DEX vs FAc) from **experimental carriers**, and they treat **IOP/cataract** as a named constraint rather than a footnote. Kim-type nanomedicine reviews open on why free/short-acting drug fails, then on the constraint actually tested (duration, route, size/charge), not on a list of every nanoparticle. Endocrinology-shaped DME papers (Kartı, Furino, Fusi-Rubiano, Spinetta) keep utilisation/consensus from being written as a new outcomes trial. That is the spine we already chose.

A **question-driven** spine is a justified departure from technology catalogues (Kim 3.4.1–3.4.8; Cao organic/inorganic; Jacob SLN/NLC/NE/liposome; Ahmed cubosomes/bilosomes). The research question is how delivery systems get drug to the diabetic retina and what still limits duration and translation — not “progress of nanotechnology” by material.

## Result-presentation craft (form only)

Copy **clustering**, not findings.

- **Do cluster (models to copy):** Swetledge gathers polymeric NP experiments by tissue and then names why distribution differs (size, charge, coating, route) in one stretch, with tables of comparable rows. Kartı groups DEX RCTs together, then meta-analyses, then consensus, and says why first-line, switch, and vitrectomized series are not one efficacy class. Goñi compiles IOP rates but **forbids pooling** because baseline, drug, and follow-up differ — that “name why they cannot be pooled” sentence is the craft. Fusi-Rubiano clusters FAME, then real-world cohorts, then vitrectomized eyes as a separate condition. Spinetta’s **Discussion** nests clinical questions (first-line, switch, IOP, cataract) after a country dump we will not copy. Kim clusters intraocular half-lives of current IVT proteins before introducing implants/particles.
- **Do not catalogue:** Liberski’s one subsection per named trial; Furino’s one heading per antibody; Cao/Jacob/Ahmed/Tsung one heading per chemistry; Spinetta one section per national consensus; Liu one cited nanomaterial after another without a shared endpoint.
- **Article rule:** follow rationale **(j)** condition clusters. Same endpoint family in one paragraph; name population, cells/strain, dose/device, endpoint, geography, statistics. Hinge studies (Radwan topical HA-apatinib; Pagoda PDS; MEAD as cited; REALFAc/Retro-IDEAL) get design and result; supporting papers are grouped. Rank design in the sentence (RCT vs observational vs rodent vs review). Do not write one study, one percentage, next study.

## What we omit on purpose

Field-standard chapters we will **not** write because this sample has no primary evidence, or because they are a technology encyclopaedia rather than our question: laser; vitrectomy-as-treatment; gene therapy; senolytics; anterior-segment diseases; NP-type catalogues; diagnostic nanoparticles; microneedles/iontophoresis/suprachoroidal as peer `##`; cost-effectiveness; equipment/energy/consumer; graphical abstract. Neighbouring topics may take **one Discussion sentence** that they sit outside the evidence here (rationale (d)).

## What we should add before drafting

Only nests the sample already supports:

1. **§5.4 IOP and cataract as DEX constraints** — Kartı SAFETY; Spinetta 9.7–9.10; Goñi applies to DEX as well as FAc. Endocrinology card: safety as its own subsection when measured. Previously dumped into 5.1 kinetics.
2. **§6.4 Vitrectomized FAc eyes** — Fusi-Rubiano has this heading and is already listed under §6.

Do **not** add empty laser, gene, or polymer-class chapters.

## Verdict

The outline is **field-typical** for a mixed nanomedicine–endocrinology narrative on ocular delivery in DR/DME: teach barriers in the Introduction, brief Methods, then constraint-driven thematic sections, separate Discussion. It is a **justified departure** from same-field technology catalogues (one heading per nanoparticle or per anti-VEGF brand) and from “Recent advances” titles. It **must change (e) only to nest DEX safety and FAc vitrectomy**, which included reviews treat as named topics and which this sample already supports. After that nest, keep (e). Do not import comparator numbers into the article.
