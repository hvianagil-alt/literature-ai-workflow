---
name: graphical-abstract
description: "Build a BioRender-style journal graphical abstract after double-check: illustrated, catchy, short labels. Prefer Lovable; else GenerateImage. Never invent numbers. Never ship a four-box text table."
---

# Graphical abstract

Foods, CRFSFS, and many Elsevier food-science reviews print a **graphical abstract**: one landscape panel that a reader can understand in a few seconds.

This step is **after** `double-check.md`. It must not introduce claims that are not already in `article.md` / rationale (i).

## Visual standard (hard)

The figure must look like **BioRender / Nature Reviews**: illustrated objects (vessel, cell, spore, plate, product icons), a consistent palette, generous white space, a **catchy one-line title**, and **short labels**. Informative because the pictures carry the argument.

**Wrong (do not ship):** four HTML text boxes, a collapsed table, a paragraph in each cell, thin arrows that look like hyphens, a “flowchart of sentences.”

**Right:** isostatic vessel; membrane leaking; spore intact; ice / solute / injury as small icons; three visual readings (refrigerated hurdle; not legal heat; quality ≠ plate).

## When to use

- Automatically after double-check when the field uses graphical abstracts (`field-structure-benchmark`).
- When the user asks for a graphical abstract, BioRender-style figure, or Lovable visual.

## Brief

Write `review/runs/<run-id>/figures/graphical-abstract-brief.md`:

1. Catchy title (argument, not “Graphical abstract”).
2. Objects to draw (no new science).
3. Labels of **≤ five words** each.
4. Forbidden: new percentages, new logs, slogans (`unlocking`, `highly effective`).

## Path A — Lovable MCP

If `Lovable` is usable, build **one full-bleed 16:9 panel**, no website chrome. Prompt from the brief. Screenshot to `figures/graphical-abstract.png`. If `needsAuth`, ask once to connect Lovable; do not block the article.

## Path B — Illustrated image (default when Lovable is down)

The user asked for a picture. Use Cursor `GenerateImage`:

- `aspect_ratio`: `16:9`
- Style words: BioRender, Nature Reviews, flat 3D scientific icons, white background, no photographs, no watermarks.
- Put the catchy title **in the image**. Keep other text to short labels in empty space, never on top of drawings.
- If labels come out misspelled, regenerate once with the first image as `reference_image_paths`, or overlay **short** type with a real font (DejaVu) in empty margins only.

Save as `figures/graphical-abstract.png` and a PDF copy of that PNG. Copy PNG/PDF to `/opt/cursor/artifacts/` when delivering.

Do **not** fall back to a four-box HTML table.

## In the manuscript

Abstract stays text-only. After Keywords / Key Summary Points: `A one-panel graphical abstract is in figures/graphical-abstract.png.`

## Hard rules

- No new science.
- No Study A / B / C comic.
- Our figure may be committed; source-paper PDFs stay gitignored.
---
