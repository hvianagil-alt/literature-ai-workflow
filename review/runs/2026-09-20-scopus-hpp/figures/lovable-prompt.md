# Lovable prompt — HPP graphical abstract

Use **only** this prompt in Lovable. Do not paste the scientific article.

---

Build **one** full-viewport **graphical abstract**, landscape **16:9**. This is **not** a website, SaaS landing page, dashboard, blog, or app. **No** navigation bar, logo header, footer, hamburger, buttons, “Get started”, cards of paragraphs, or scrollable marketing layout. The browser window **is** the figure, as if BioRender or a Nature Reviews illustration were opened full screen.

**Audience:** a smart scientist who does **not** work in food microbiology. After three seconds they should know what the paper discusses: factories squeeze sealed food with water pressure instead of cooking it; that kills many living bacteria but not reliably spores or all enzymes; the **same pressure is not one safety number**.

**Style:** BioRender / Nature Reviews. White background. Flat 3D scientific icons, crisp outlines, soft shadows. Palette: navy `#123056`, teal `#0A7A84`, coral `#C44A4A`, gold `#C4A35A`, light grey. Generous whitespace. Very little text. **No photographs. No watermarks. No tables. No four text boxes filled with sentences.**

**Title** (top centre, large, navy, bold):  
Same squeeze. Three answers.

**Subtitle** (under title, smaller, teal):  
When heat is not the kill step

**Layout, left → centre → right, one row of meaning:**

**LEFT — the machine, not a cook.**  
Draw a cutaway steel high-pressure vessel filled with water. Inside: a juice pouch and a vacuum pack of ham. Teal arrows press **equally from all sides**. A small thermometer shows cool, not boiling. To the far left, a grey heat-exchanger coil with a clear **X** (this process is instead of cooking). Tiny caption under the vessel: `Isostatic pressure · not cooking`

**CENTRE — what happens to microbes.**  
One large rod-shaped bacterium in cross-section: membrane pores, purple cytoplasm leaking (membranes leak). Beside it, a smaller intact **endospore** with a thick coat (spores often survive). Below, a petri dish with mixed colonies and one faded/ghost colony (injury ≠ death). Three tiny icons under the dish, labelled: `Ice`  `Lactate protects`  `Injury ≠ death`

**RIGHT — three readings of the same cycle** (three circular badges, stacked, icon-first, five-word captions only):  
1. Juice bottle + ham + snowflake — `Refrigerated hurdle`  
2. Milk bottle ≠ heat-wave pasteurisation stamp — `Not legal milk heat`  
3. Brown apple/grapes beside an empty plate — `Quality ≠ plate count`  

A thin footer line, one sentence, small navy type:  
`Keep cold or add heat for spores. A plate count is not a pasteurisation law.`

**Do not add:** ultrasound, plasma, irradiation as equal heroes; any invented percentages; “HPP is safe and mild”; author names; journal logos.

Implement as a single HTML/CSS/SVG scene that fills the viewport (`100vw` × `100vh`, `overflow: hidden`). If you need React, still render **only** this poster.

---
