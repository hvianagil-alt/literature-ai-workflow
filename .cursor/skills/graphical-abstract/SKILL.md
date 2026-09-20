---
name: graphical-abstract
description: "After the article exists: condense it for a non-specialist, write a Lovable prompt from that condensation (never paste the manuscript), then build a BioRender-style graphical abstract in Lovable. Give the user the Lovable URL."
---

# Graphical abstract

A graphical abstract is one landscape panel that lets a neighbour-field reader see **what the article will discuss** in a few seconds.

Do this **after** `article.md` and `double-check.md` exist. Never invent findings. Never paste the full article into Lovable.

## Workflow (mandatory order)

### 1. Condense the article (knowledge, not layout)

Read `article.md` (Abstract, Key Summary Points, Introduction aim, section headings, tables’ *meaning*, Discussion main finding). Write `figures/knowledge-condense.md` as if explaining the paper to an intelligent colleague **outside the field**.

Required sections:

- **What problem a non-specialist already knows** (one short paragraph).
- **What this paper is actually about** (the tension, in plain words).
- **How the process works** (physical picture, no jargon unless defined).
- **What changes the outcome** (the coefficients).
- **What people often mix up** (the false equivalences the article refuses).
- **What the reader will learn, in order** (the section spine as questions, not heading numbers).
- **What the paper does not claim.**
- **Words you may put on the figure** (title + labels ≤ five words). No new numbers.

This file is the science. It is **not** the Lovable prompt.

### 2. Decide the picture, then write the Lovable prompt

From the condensation only, choose **one visual story** (left-to-right or centre-and-satellites). Write `figures/lovable-prompt.md`:

- Role: “Build a single full-bleed 16:9 scientific graphical abstract. This is not a website, app, dashboard, or landing page.”
- Audience: neighbour-field scientist.
- Style: BioRender / Nature Reviews; white ground; teal–coral–navy; illustrated objects, not text boxes.
- Exact title and subtitle (from the condensation).
- Zones: what to draw in left / centre / right (objects, not paragraphs).
- Labels, copied verbatim from the allowed-words list.
- Hard no: navigation, footer, “Get started”, hamburger, paste of the article, four HTML boxes of prose, extra scientific claims.

Do **not** dump `article.md` into this prompt. If the prompt is longer than ~600 words, it is too long — cut objects, not explanations of the argument.

### 3. Send that prompt to Lovable (not the article)

1. `GetDynamicTools` on namespace `Lovable`.
2. If `needsAuth`, run `mcp_auth` and **stop**. Tell the user to connect Lovable in Cursor. Do not invent a `lovable.dev` URL. Keep the two markdown files ready.
3. If usable, inspect the create/edit tool schema, then create **one** project with **only** `lovable-prompt.md` as the instruction.
4. Iterate once if the result is a website chrome or a text table.
5. Write the project URL into `figures/lovable-url.md` and into the user message.
6. Screenshot the panel to `figures/graphical-abstract.png` if a screenshot tool exists.

### 4. Only if Lovable cannot run

Say so. Keep `knowledge-condense.md` and `lovable-prompt.md` as the deliverable for the next connected session. Do not replace step 3 with a four-box HTML table. An illustrated PNG is allowed as a **temporary** stand-in, labelled as not the Lovable link.

## Manuscript

Abstract stays text. After Key Summary Points you may point at the PNG. Put the Lovable URL in `lovable-url.md`, not inside the scientific Abstract.

## Hard rules

- Condense first. Prompt second. Lovable third.
- Never paste the manuscript into Lovable.
- No new science on the figure.
- The user asked for a **link**: that means the Lovable project URL when the MCP works.
---
