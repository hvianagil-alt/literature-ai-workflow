---
name: field-structure-benchmark
description: "Compare this review's outline to published reviews of the same kind and same field (headings and topics only). Use after synthesis-rationale (e) and before drafting article.md. Form only — never import their findings."
---

# Field-structure benchmark

A review can be scientifically honest and still **mis-shaped for its field**: missing the sections that journals and readers in that area expect, or copying a generic IMRaD dump that those journals never use.

This step checks **structure and topics**, not results. It is the same-area counterpart of the form-only style study in `review-prose`. It does **not** license new citations from memory.

## When to use

- Automatically after `synthesis-rationale.md` section **(e)** exists and **before** drafting `article.md`.
- When the user asks whether the structure or topics “make sense” compared with other reviews.

Do not skip this on a full journal manuscript. A short note (`--short`) may skip it.

## Same area, same style

Use **included review articles first** (already extracted; headings are in the XML/PDF/txt). Optionally add **two to five extra OA reviews** found with `search_oa_related.py` whose titles name both the **field** and the **kind** (narrative / systematic / scoping). Fetch public full texts only. If none are OA, benchmark from the included reviews alone and say so.

Match **kind to kind**:

- Narrative food-science review ↔ other narrative reviews in that matrix/technology.
- Scoping/systematic review ↔ other PRISMA papers, not a physiology essay.
- Do not treat a primary challenge trial as a structure model.

## What to extract (form only)

From each comparator, list:

- Title shape (colon subtitle? “recent advances”?)
- Front matter: unstructured vs structured abstract; keywords; highlights
- Heading spine (`##` / numbered 1. 2. 3.) — copy **titles**, not paragraphs
- Organising principle: by **mechanism**, by **matrix**, by **technology**, by **legal question**, or by **search batch**
- Where Methods sit (early / buried / absent)
- Whether Discussion is separate from Results
- Topics that recur in ≥2 comparators

**Forbidden:** copying their numbers, quoted findings, or example organisms into `article.md` unless that paper is already an included full text for **science**.

## Output

Write `review/runs/<run-id>/structure-benchmark.md` (fallback `review/report/structure-benchmark.md`):

```markdown
# Structure benchmark — <run-id>

**Our kind:** narrative / systematic / …
**Our organising principle:** …
**Comparators (n=):** citation or included citekey, kind, OA yes/no

## Heading inventory
| Topic the field uses | In comparators | In our outline (e) | Decision |
|---|---|---|---|
| … | Zhang §3; Wu §2 | §3 membranes | keep / add / omit (why) |

## What matches
## What we omit on purpose
<Field-standard sections we will not write because this sample has no primary evidence.>
## What we should add before drafting
<Only if the sample already supports it.>
## Verdict
<One paragraph: the outline is field-typical, or it is a justified departure, or it must change.>
```

Then **update rationale (e)** if the verdict says add/split/drop a heading. Do not add a section whose only job is “other reviews have this chapter.”

## Decisions

| Situation | Do |
|---|---|
| Field reviews organise by matrix (milk / juice / meat) and our sample can support that | Allowed, but a **question-driven** spine is also valid for a narrative argument. Record the choice. |
| Field reviews always include equipment, energy, packaging, or consumer acceptance and we have no measurements | Name them in rationale **(d)**. One Discussion sentence that they are neighbouring topics without evidence here. Do not invent a chapter. |
| Field reviews are technology catalogues (HPP, then PEF, then plasma) | Do **not** copy that catalogue if the research question is about one process and its coefficients. |
| Systematic comparators use IMRaD Results | Use IMRaD only if **our** review is systematic/meta. |
| Extra OA reviews were read only for headings | Do not cite them for scientific claims in `article.md`. |

## Hard rules

- Never fabricate a comparator. Headings come from a file you opened.
- Never import findings from a form-only comparator.
- Do not reorganise around search batches (“papers from group A”).
- Do not add a graphical abstract or figure step. The article is text (Markdown; Word/PDF only if asked).
---
