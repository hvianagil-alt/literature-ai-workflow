---
name: scientific-synthesis
description: "Write a review as evidence synthesis, not a paper catalogue: intellectual model first, four statement layers, claim-evidence-contrast-explanation-synthesis paragraphs, mechanism strength grading, and logic audits. Read with review-prose before drafting or rewriting article.md."
---

# Scientific synthesis (publication-ready review)

Read this **with** `review-prose` before drafting or rewriting `article.md`. This file is the reasoning workflow. `review-prose` remains genre, spine, title, keywords, and banned chatbot diction. It is **not** a license to invent citations.

A scientific review is **not** a collection of papers.

Wrong objective: *Study A found X. Study B found Y. Study C found Z.*

Right objective: what the literature **collectively** shows, **why** results differ, **how strong** the evidence is, **which mechanisms** explain the differences, and **which conclusions** the measurements actually support.

Optimize for:

**evidence → comparison → explanation → synthesis → implication**

not:

**paper → result → paper → result → conclusion**

## Phase 1 — Intellectual model (before any article prose)

Do this in `synthesis-rationale.md`, not in your head. If you cannot fill the nine items, you are not ready to write.

1. Central scientific question.
2. Main variables that change the outcome.
3. Main mechanisms linking those variables to the outcome (only as the papers state them).
4. Major sources of disagreement or heterogeneity.
5. Types of evidence (primary experiment, storage trial, model, systematic/scoping review, regulatory opinion).
6. What is well established (multiple independent sources or a designated authority on that question).
7. What is suggested but uncertain.
8. What remains unknown.
9. What practical or scientific consequence follows from that uncertainty.

Express the review as a causal chain:

**condition → mechanism → observed effect → interpretation → consequence**

Example shape (replace with this sample’s facts):

experimental condition → changes a physical/biological mechanism → produces a measured response → the response depends on another variable → therefore an apparent contradiction is explained by that variable, not by “the literature disagrees.”

Add this as **`(i) Intellectual model`** in `synthesis-rationale.md` **before** outlining `(e)` and **before** any `article.md`.

## Phase 2–3 — Evidence map (already the notes + table)

Every included paper is a structured record, not a remembered abstract. Claim-ready facts must keep **what was measured** separate from **what it means** and from **what you think might explain it**.

In notes, when the PDF allows, record:

| Field | Meaning |
|---|---|
| System | Organism / matrix / population |
| Conditions | Independent variables that matter |
| Comparator | Control or reference |
| Outcome | What was actually assayed |
| Magnitude | Number with units, or “not reported” |
| Mechanism | Directly tested, proposed by authors, or not stated |
| Evidence type | Primary / review / model / regulatory |
| Confidence | High / moderate / low, tied to design |
| Relevance | Which review question it addresses |

Never silently merge measurement, interpretation, and speculation in one cell.

Do **not** pool numbers that share a unit. Two log reductions are comparable only if outcome, system, conditions, comparator, method, time point, and biological meaning match. Otherwise write **contextually comparable, not interchangeable**.

## Four layers of statement (hard rule)

Every scientific sentence is primarily one of:

**A. Observation** — what was measured. *Treatment X reduced Y by ~3 log under the stated conditions.*

**B. Interpretation** — what that measurement means. *X can substantially reduce Y in that system.*

**C. Mechanism** — why it may have happened, graded (below).

**D. Implication** — why it matters. *Those conditions must be named when comparing studies.*

Do not jump from A to D. Preferred order: **observation → interpretation → mechanism → implication**. Not every paragraph needs all four. Know which layer you are on.

## Mechanism strength (hard rule)

Never present a mechanism as stronger than the evidence.

| Grade | Allowed wording |
|---|---|
| Directly demonstrated | The study **measured** membrane permeability / pores / enzyme activity and observed… |
| Supported by multiple studies | Findings are **consistent with** … as a contributing mechanism |
| Plausible | **One possible explanation** is… |
| Speculative | This **could** reflect… (only if the papers themselves speculate) |

Never convert “the authors proposed that X may explain Y” into “X causes Y.”

Use **associated with** for observational evidence; **consistent with** for a mechanism not proven; **suggests** when uncertainty remains; **demonstrated** only when the design establishes the claim; **caused** only when the experiment supports causal inference.

The assay is not the phenomenon: no colonies ≠ dead; lower activity ≠ structural destruction; a blank plate ≠ sterility.

## Paragraph function (every body paragraph)

One paragraph, one intellectual job. Template:

1. **Topic sentence** — the scientific idea or question (not an isolated number, not “Author et al. found”).
2. **Evidence** — representative measurements, with comparator and units.
3. **Contrast** — studies that differ, or a limitation of the assay.
4. **Explanation** — which variable changed (matrix, strain, recovery, scale), not “the papers disagree.”
5. **Synthesis** — what can reasonably be concluded, no broader than the evidence.

Before keeping a paragraph, answer: **what question does this paragraph answer?** If the answer is only “it contains information about X,” rewrite.

Do not load one paragraph with results + mechanism + regulation + industrial implication + a new technology. Split.

Do not open with an orphan result (*At 500 MPa, counts fell 4.2 log*) unless that number **is** the point. Introduce the variable, then the number.

Do not announce the conclusion in sentence one and only then show the data (*HPP is highly matrix-dependent. For example…*). Introduce the variable, present evidence, compare, explain, then conclude.

Do not hide the point under six sentences of throat-clearing. **Topic sentence → evidence → explanation → synthesis.**

## Sentence logic

Make cause, support, and uncertainty evaluable. If one sentence contains several independent scientific relationships, split it.

Use **because**, **however**, **therefore**, and **although** only when the preceding evidence supports that relation.

Every **therefore / thus / consequently / indicating that / suggesting that / demonstrating that / implying that** must rest on evidence immediately above it. If it does not, weaken or delete.

When studies differ, name the variables that changed (system, organism, strain, P/T/t, pH, aw, composition, scale, recovery medium, endpoint, storage). Heterogeneity is information. Do not pick the convenient row.

## Three synthesis levels

1. Study: this experiment measured X.
2. Cross-study: across included studies, X was generally associated with Y, with stated spread.
3. Conceptual: Y is not determined by X alone; it emerges from X interacting with A, B, and C.

Reach level 3 in section closings and in the Discussion. Do not end a subsection on another citation dump.

## Section architecture

Organize around **questions**, not search batches. Each major section:

**question → evidence → comparison → explanation → synthesis**

The last subsection integrates; it does not repeat. Transitions must say **why this section exists now** (*Because lethality depends on the physical state of the pack, ice and solute are not optional footnotes*).

Discussion answers **so what?**, not a second Results:

1. Main finding  
2. Explanation of the pattern  
3. How parts of the evidence fit  
4. What cannot be concluded  
5. Why that matters  
6. What measurement would resolve it  

If a Discussion paragraph could be pasted into the body unchanged, it is not doing enough synthesis.

Conclusions must be **narrower** than the evidence, not broader. Trace each major conclusion: conclusion → synthesis → studies → measurements.

Cite for **coverage of the argument** (foundational, representative, contradictory, primary numbers). Do not make papers the grammatical subject of three consecutive sentences (*According to Smith et al.… According to Jones et al.…*). Place citations at the claim they support, not once at the end of five claims.

Tone: **simple + precise + qualified**. Not conversational metaphor (*the plate invents a disagreement*) and not bureaucratic fog. Prefer a number to *remarkable / dramatic / striking / highly effective*. Every *higher / lower / more effective* needs an explicit comparator. Default hedge for local evidence: **under the conditions studied**.

## Tables and evidence hierarchy

In-article tables must reveal a relationship (direction, exceptions, what was measured vs the legal benchmark). They are not a paste of the extraction worksheet.

Do not treat as interchangeable: primary experiment, several independent experiments, systematic review, narrative review, model, regulatory opinion, expert interpretation. Do not let a secondary sentence replace a primary number for a core claim when the primary full text is in the sample.

## Audits (mandatory in `double-check.md`)

After `check_article.py` exits 0, do a **reasoning pass** (not a second catalogue):

**Logic (per paragraph):** main claim; evidence; counterevidence; explanation; interpretation; implication. Flag unsupported, overextended, hidden assumption, mechanistic leap, premature conclusion, missing comparator, missing uncertainty, redundant synthesis.

**Sentence:** clear subject and verb; supported; one main logical relation; qualification next to the claim; number or condition if it would reduce ambiguity.

**Paragraph:** question in sentence 1; evidence in the middle; difference or mechanism later; takeaway last.

**Section:** question; why it belongs; multi-study synthesis; differences explained; evidence vs interpretation; synthesis ending; handoff to the next section.

**Whole paper, five steps:** (1) unresolved problem; (2) what the literature shows; (3) why that pattern; (4) what blocks a stronger conclusion; (5) what synthesis this review adds. If you cannot write those five steps, the argument is still dispersed.

## Machine gate

`check_article.py` still cannot judge every inference. It **does** fail conversational review-metaphor, stacked *According to Author et al.*, and the usual flourish/process bans. The double-check must catch the rest. Do not tell the user the article is done while either fails.

## Handoff

`report-writing` executes rationale `(e)` **in this reasoning**, in the voice of `review-prose`. Then `article-qa`, then this audit inside `double-check`.
