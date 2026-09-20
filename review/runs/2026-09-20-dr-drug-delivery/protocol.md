# Protocol — run `2026-09-20-dr-drug-delivery`

Written **before** PDF retrieval. The user asked for another test review, named the topic, and said to fetch the articles (empty `papers/` folder; no seed PDFs). Defaults below are the “just go” defaults from `AGENTS.md`.

## Defaults used (user said to fetch articles and run a test)

- Journal-style **narrative review**; teach in the Introduction; claim-first sentences; numbered Markdown results tables with in-text Table N callouts; all included full texts; no process talk in Discussion; quality-gate scripts before delivery.
- Related-paper search: **2021–2026** (current year minus 5 through current year), `--journal-quality journal` (peer-reviewed journal articles), `--sort relevance_score:desc`.
- Public OA PDFs only. Contact email for OpenAlex/Unpaywall: the run owner address (`hugogilcontas@gmail.com`).
- Output: Markdown article in this run folder. Word/PDF only if asked later.

## Review question

How do **ocular drug-delivery systems** (intravitreal implants and injectables, nanoparticles and other nanocarriers, hydrogels, microneedles, topical or periocular carriers) get **anti-VEGF agents, corticosteroids, and other drugs** to the **retina** in **diabetic retinopathy (DR)** and **diabetic macular edema (DME)**, and what still limits duration, targeting, and translation?

## Identification source

- Empty `papers/` tray (no user-dropped PDFs; two older Scopus exports in `papers/exports/` are from other topics and are **out of scope**).
- Database: OpenAlex topic search (`scripts/find_papers.py`), origin `topic_search`.
- Queries (ordinary words from the user’s topic; 1–3 searches):
  1. `drug delivery diabetic retinopathy`
  2. `nanoparticle diabetic retinopathy ocular`
  3. `intravitreal implant diabetic macular edema`
- Year window: 2021–2026. Venue bar: peer-reviewed journal articles.
- No pirate sites; no paywall bypass.

## Eligibility (inclusion)

A retrieved full text is **included** if it is about **drug delivery** (route, carrier, implant, formulation, or pharmacokinetic targeting) **to treat or experimentally model diabetic retinopathy or diabetic macular edema**.

Eligible designs: original research (clinical, in vivo, ex vivo, in vitro formulation with a DR/DME payload or model) **and** narrative/systematic reviews that synthesise ocular delivery for DR/DME, when the full text was retrieved.

## Eligibility (exclusion)

- No diabetic retinopathy / DME context (generic ocular delivery, AMD-only, glaucoma-only, dry eye, unless DR/DME is a measured indication).
- Systemic diabetes drugs with no ocular delivery or retinal endpoint.
- Full text not retrieved (no public `%PDF-`).
- Full text unreadable.
- Duplicate DOI already included.

Title-only exclusion is used only when the title is unambiguously off-topic. Borderline records go to full text.

## Emphasis

Balanced **methods + findings**: barriers that force a delivery system, what each carrier actually measured (release, vitreous half-life, retinal uptake, vision or OCT in patients, safety), and translational limits. Not a catalogue of every nanoparticle type.

## Accuracy rule

Numeric results, sample sizes, and mechanistic claims are taken from the PDF text (or marked “not stated” / “not retrieved”). Titles and DOIs come from the OpenAlex catalog. Nothing is filled in from memory.

## Token / usage logging

Cursor does not expose billed token counts to this workflow. Each phase writes `usage-log.jsonl` with character counts and a **characters/4 token estimate**. Token estimates belong only in `usage-log.md` / `usage-log.jsonl`, never in `article.md` or `synthesis-rationale.md`.

## Phases (this run)

1. `workflow` — protocol and run folder
2. `discovery` — OpenAlex topic search
3. `fetching` — public OA PDF retrieval
4. `screening` — title then full text
5. `extraction` — per-paper notes
6. `table` — comparison table
7. `rationale` — `synthesis-rationale.md` (mandatory before the article)
8. `gap_retrieval` — targeted OA searches for interpretation gaps
9. `synthesis` — article, following the rationale outline (after extra retrieval)
