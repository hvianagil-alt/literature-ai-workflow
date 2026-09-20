---
name: graphical-abstract
description: "Build a journal graphical abstract from the intellectual model after double-check. Prefer the Lovable MCP for a designed figure; fall back to a local HTML/PDF figure. Never invent numbers."
---

# Graphical abstract

Foods, CRFSFS, and many Elsevier food-science reviews print a **graphical abstract**: one landscape panel that states the argument without replacing the Abstract.

This step is **after** `double-check.md` exists. It must not introduce claims that are not already in `article.md` / rationale (i).

## When to use

- Automatically after the double-check for a full journal manuscript in fields where comparators used a graphical abstract (`field-structure-benchmark`).
- When the user asks for a graphical abstract, figure, or “Lovable” visual.

Skip on a short note unless they asked.

## Content (the brief)

Write `review/runs/<run-id>/figures/graphical-abstract-brief.md` first:

1. One-line argument (from rationale (i) causal chain).
2. Three to six boxes or arrows: **condition → mechanism (graded) → measured endpoint → interpretation**.
3. One contrast (e.g. legal criterion vs plate count).
4. Words allowed: only terms and magnitudes already in the article.
5. Words forbidden: new percentages, new log reductions, slogans (`highly effective`, `unlocking`).

Example shape (replace with this sample’s facts):

`P/t + matrix coefficients → vegetative log / enzyme / texture → three readings that are not interchangeable`

## Path A — Lovable MCP (preferred)

Lovable is the design tool. Use it when the `Lovable` MCP namespace is usable (`GetDynamicTools`; if `needsAuth`, run `mcp_auth` and **ask the user once** to connect Lovable in Cursor). Do not invent a login.

Then:

1. Inspect the Lovable tools (`GetDynamicTools` on that namespace) and follow their schemas.
2. Create **one** project: a **single full-bleed panel**, landscape (~16:9 or journal 180×90 mm), no website chrome (no nav, no footer, no “Get started”).
3. Typography: serif or clean sans; dark text on white or very light ground; arrows with captions.
4. Prompt Lovable with the **brief**, not with a new scientific story.
5. Export or screenshot the panel to `review/runs/<run-id>/figures/graphical-abstract.png` (and HTML if the tool returns it).
6. Record the Lovable project URL in the brief file.

If authentication fails, say so in the brief and use Path B. Do not block the article.

## Path B — Local figure (always available)

When Lovable is unavailable, write `figures/graphical-abstract.html` (Times / Liberation Serif, landscape page) from the same brief and print it:

```bash
python3 -c "
from weasyprint import HTML
HTML('review/runs/<run-id>/figures/graphical-abstract.html').write_pdf(
    'review/runs/<run-id>/figures/graphical-abstract.pdf')
"
```

Copy the PDF/HTML to `/opt/cursor/artifacts/` when delivering. Optional PNG if a rasteriser exists.

## In the manuscript

Do **not** put the figure inside the Abstract (Abstract stays text-only; `check_article.py` forbids citations there). After Keywords / Key Summary Points, one sentence may point to the file:

`A one-panel graphical abstract is in figures/graphical-abstract.pdf.`

Do not add claims in that sentence. Do not add a generic `## Graphical abstract` Results dump.

## Hard rules

- No new science in the figure.
- No decorative food photography that implies a product claim.
- No “Study A / Study B / Study C” comic.
- Source papers’ PDFs stay gitignored; **our** figure may be committed.
---
