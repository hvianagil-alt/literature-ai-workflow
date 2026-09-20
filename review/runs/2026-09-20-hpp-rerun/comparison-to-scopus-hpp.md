# Comparison: HPP rerun vs first HPP manuscript

Compared only after `python3 scripts/check_harness.py --run-dir review/runs/2026-09-20-hpp-rerun --full` exited 0.

| | First version (`2026-09-20-scopus-hpp`) | This rerun (`2026-09-20-hpp-rerun`) |
|---|---|---|
| File | `review/runs/2026-09-20-scopus-hpp/article.md` | `review/runs/2026-09-20-hpp-rerun/article.md` |
| Title | High-pressure processing of foods: a narrative review of lethality, injury, and quality when heat is not the kill step | High-pressure processing of foods: a narrative review of when a named cycle is not one outcome |
| Body words | 7327 | 8841 |
| Included full texts | 44 (43 export + 1 related review) | 43 (HPP-centred screen + 4 gap-fill papers) |
| `check_article.py` | OK | OK |
| Form model `p_published_form` | 0.999 | 1.000 |
| Food-science `field_z` | 0.778 | 0.541 |
| In-article tables | 3 | 4 |
| Gap retrieval that entered the article | 1 extra review (Houška already used as kinetics) | Wiśniewski *Listeria* overview; Szczepańska HPH apple juice; Heydenreich nisin/spore buffer; López 55 °C cream |

The first manuscript was not rewritten. This file is a comparison only.

## What improved

The central argument is sharper. Version 1 argues that HPP is a real vegetative hurdle whose log cannot be read from the gauge, and that quality and legal bars must be named. Version 2 keeps that and makes the unit of analysis the **named cycle**: ice, aW, agar, lactate, hold versus pulse, and heat assistance change the outcome of the same megapascal label. Neighbouring operations are there to refuse false equivalence, not to survey “nonthermal processing.”

Traceability is better on two rows that version 1 got wrong or incomplete:

- Rodríguez 2024 in version 1 Table 1 is labelled *Cronobacter sakazakii* (buffer). The included full text is *E. coli* DSM682 in already-pasteurised orange juice. Version 2 uses that matrix and organism.
- Serra-Castelló 2021 in version 1 Table 1 reports only the 1.4% lactate 10 min gap (0.5–1.46 log). Version 2 reports the 2.8% lactate 10 min differences from the PDF (1.75–2.51 log), after a critic FAIL on a mixed 1.29–2.35 cell.

Gap retrieval did more scientific work. Version 1’s extra retrieval added a plant-food review already in the conceptual spine. Version 2 added a primary HPH trial (≤1.4 log native kill at 200 MPa), a buffer spore–nisin mechanism paper, a 600 MPa/55 °C cream hurdle, and a *Listeria* overview, and it still leaves Gong 2024 and Torrents-Masoliver 2025 unread because no public PDF was available.

Screening is tighter. Version 1 kept neighbouring-only papers (plasma wash, irradiation mini-review, apple-juice sonicator) in §7. Version 2 excluded neighbouring-only full texts at eligibility and uses ultrasound, irradiation, and ohmic heating only where they sit on the same samples as pressure, plus HPH as the named false friend.

The critic gate ran. Version 2 failed once on two number/condition errors, was rewritten, and passed. That is a workflow improvement even though version 1 already passed `check_article.py`.

## What did not improve, or is not a fair A/B

The samples are not identical, so this is not a pure writing contest on the same 44 papers. Version 1 is longer on plasma, irradiation, and a dual-frequency sonicator because those papers were in. Version 2 is longer on HPH, PATP temperature, and HPTP-adjacent cream because those papers were added.

`field_z` against the food-science gold centroid is **lower** in version 2 (0.541 vs 0.778). `p_published_form` is saturated at 1.0 for both, so the form model does not decide a winner. The drop in `field_z` may reflect the tighter HPP spine and four tables rather than a worse Abstract. It is reported, not explained away.

Version 1 already taught in the Introduction, used colon-subtitle form, kept acquisition talk in Methods, and passed the machine gate. The rerun is not a rescue of a failing first draft. It is a second independent pass with a stricter HPP bar, more targeted extra papers, and an independent number check that caught two errors.

## Rank (1–5; 5 is better)

| Axis | Version 1 | Version 2 (deliverable) |
|---|---|---|
| Abstract as a topic map | 4 | 5 |
| Tables (design in cells; callouts) | 3 | 5 |
| Traceability of numbers to notes/PDF | 3 | 5 |
| Discussion (so-what, not a second Results) | 4 | 5 |
| Completeness for the HPP question | 4 | 5 |
| Coverage of neighbouring nonthermal fields | 5 | 3 |

**Deliverable for this request:** version 2, `review/runs/2026-09-20-hpp-rerun/article.md`. Version 1 remains the earlier manuscript and was not edited.
