# Agent instructions: Literature AI

This file tells any AI agent (Cursor, or another AGENTS.md-compatible tool) how to run the literature review workflow in this repo. If a user opens this repo and says something like **"review my papers"**, **"help me with my literature review"**, or **"read the PDFs in papers/"**, follow this file — don't default to generic chat.

## Who this is for

Researchers in **life sciences** (and neighbouring fields) who are not AI experts. They may only know ChatGPT, Claude, or Cursor chat. Assume they know their field deeply. Explain what you're about to do in plain language. Don't use ML/agent jargon unless they use it first. Write the repository, the article, and default replies in **English**.

## The workflow, in order

This is an opinionated, sequential workflow. Don't skip steps, and don't silently process everything the moment you see PDFs — **four hard gates** must complete before you tell the user the article is done: direction check (step 2), synthesis rationale + targeted extra retrieval (step 6), the machine quality gate (step 8), and the double-check (step 9).

**The article is not done when the file exists.** It is done when `scripts/check_extraction.py` and `scripts/check_article.py` exit 0. A previous run failed by delivering mechanical notes and catalog sentences. Do not repeat that. Do not rewrite an earlier sample's `article.md` unless the user asked to change that manuscript.

### 1. Intake

Look at what's in `papers/` (recursively, ignoring non-paper files). Tell the user what you found (count, filenames/titles if visible). Then ask, in a short list, **before any deep work**:

- **Who they are / research area** (e.g. nanomedicine, endocrinology, microbiology).
- **What the review is for** (thesis chapter, grant background, paper introduction, personal reading).
- **Do they already have literature?** If yes: they can drop PDFs in `papers/`, paste titles/DOIs in the chat, or attach files. If no: say you will search **free open-access** papers on the public web (OpenAlex) — not pirate sites, not paywalls.
- **Search filters they may want:** years (e.g. last 5–7 years) and journal quality (any OA; peer-reviewed journals; DOAJ; citation floor). Defaults if they say “just go”: last 6 years + peer-reviewed journals.
- **Output:** the article is always **Markdown** (`.md`). Ask whether they also want Word or PDF later (Times New Roman, justified). Do not delay the `.md` for that.

**If `papers/` is empty**, do not stop. They can still drop files by hand (`papers/README.md`), **or** you find free open-access papers for them. Use the `find-papers` skill: search OpenAlex for the topic they named, fetch public PDFs only, then continue. Ask once for a contact email if Unpaywall/OpenAlex need it. Do not ask them to buy an API. If the network fails or nothing is OA, say so and wait for PDFs.

If the user starts from a **Scopus/PubMed `.bib` export** rather than PDFs, do not skip intake: count the records, then use the `bib-import` skill into `review/runs/<run-id>/`. PDF retrieval is a separate, explicit step (`oa-fetch`) — only public open-access files, with failures logged. Document identification/screening with the `prisma-logging` skill.

### 2. Direction check (mandatory, do not skip)

Before extracting anything in depth, confirm with the user. **Do this for every new user and every new review**, even if a previous run already used filters:

- **Scope**: which papers (if any) are out of scope, and why (wrong population, wrong method, too old, off-topic)?
- **Inclusion/exclusion criteria**: is there a study design, date range, population, or venue that should be included/excluded?
- **Search filters (ask explicitly — do not assume):**
  - **Years**: from which year to which year should related-paper search run? (Example: last 5, 6, or 7 years.)
  - **Journal quality**: what venue bar should related-paper search use? Options the scripts support: no venue filter (`none`); peer-reviewed **journal** articles (default); **DOAJ**-listed journals; journal articles with a **citation** floor (`cited`, default floor 10).
- **Seeds vs filters**: papers the user dropped stay in the sample even if they are older than the year window, unless the user excludes them.
- **Emphasis**: should extraction lean toward methods (e.g. for a methods-focused thesis chapter), findings (e.g. for a grant background section), or something else?

Summarize back what you understood in 2-4 sentences and get explicit confirmation ("does that sound right?") before moving on. If the user says "just go", proceed with these defaults and write them into `protocol.md`: **journal-style narrative review**; teach in the Introduction; claim-first sentences; numbered Markdown results tables with in-text Table N callouts; all included full texts; no process talk in Discussion; run the quality-gate scripts before delivering; related-paper search uses the **last 6 years** (from-year = current year minus 5) through the current year; journal quality = peer-reviewed **journal** articles (`--journal-quality journal`). Pass those flags to `find_papers.py` / `search_oa_related.py`.

**Do not proceed past this step without user input.** This is a hard gate: scope cannot be guessed.

### 3. Find related papers (default when the folder is empty or they gave seeds)

If they dropped a seed set (for example ten PDFs on one topic), use `find-papers` in **related-to-seeds** mode: search free OpenAlex OA records on that shared topic and fetch public PDFs. Do this without waiting for a special opt-in — it is free and cheap. Tell them the titles the API returned. Confirm at the direction check which retrieved files to extract.

If they only want search strings and no downloads, use `related-paper-exploration` in **opt-in browse** mode instead. That step **never invents fake citations**.

Gap-driven extra retrieval after the table is **not** this step — that is step 6, and it is mandatory.

### 4. Extract

For each in-scope paper, use the `paper-extraction` skill to produce a note in `review/notes/` (and the run copy if you are in `review/runs/<run-id>/`). `scripts/notes_from_text.py` is a **stub**. Fill `## Claim-ready facts` from the PDF. Report progress as you go (e.g. "3 of 7 done, 1 unreadable — see below"). Surface unreadable-PDF failures immediately rather than silently skipping them.

Extraction is not finished until:

```bash
python3 scripts/check_extraction.py --notes-dir review/runs/<run-id>/notes \
  --screening review/runs/<run-id>/screening.json
```

exits 0.

### 5. Build the literature table

Use the `literature-table` skill to turn the **verified** notes into `review/table/literature-table.md`. `scripts/write_table.py` writes a DRAFT only. Run `scripts/table_from_notes.py --run-dir review/runs/<run-id>` so every cell comes from Claim-ready facts. Tell the user it's ready and suggest they skim it for obvious extraction errors before you go further.

**Do not write the journal article after this step.** The table is evidence, not interpretation.

### 6. Synthesis rationale + targeted extra retrieval (mandatory hard gate)

This is a sequencing gate like step 2: **do not skip it, and do not treat it as optional.** Unlike step 2, you do **not** wait for the user to confirm before doing it — you must complete it before any article.

Use the `synthesis-rationale` skill:

1. Write `review/runs/<run-id>/synthesis-rationale.md` (fallback `review/report/synthesis-rationale.md` or `review/notes/_synthesis-rationale.md`). Interpret the **whole sample**. The file **must** state: **(a)** what each included study actually measured; **(b)** themes the data support vs themes that would be forced; **(c)** real disagreements and why (methods / population / endpoint); **(d)** what this sample cannot answer; **(e)** the outline of the review. **No article yet.** If the user says “just write the review,” still write this file first, then the article, and tell them that you did.
2. In that rationale, list **interpretation gaps** (thin evidence; conflicting results; missing comparator, mechanism, or population; a striking finding that cannot be put in perspective from the current sample; an eligible paper that was not retrieved).
3. For **each** gap, attempt **targeted retrieval** of additional related papers **before** writing the article. Use the `related-paper-exploration` quality bar (**never invent citations**). Search with `scripts/search_oa_related.py` (OpenAlex; API hits only). Fetch **only public OA** via existing `oa-fetch` / `bib-import` / Unpaywall / OpenAlex / Europe PMC / publisher OA. **No paywall bypass.** Log sought / found / not retrieved.
4. Extract any newly included papers into notes and **update the table**.
5. If additional papers cannot be retrieved, say so explicitly in the rationale (and later in the article). **Do not fill gaps with speculation or invented citations.**

Only after the rationale, the retrieval attempts, and the updated table exist may you go to step 7.

### 7. Write the journal review (only after step 6)

Read `review-prose` **and** `report-writing` before drafting. Default output is a **journal-style narrative review**, not a lab report, unless the user asked for a short note. `review-prose` is the genre, architecture, and voice file (match the spine to the review kind; Introduction opens on the phenomenon and ends with the aim; claim-first sentences; human scientific prose; length). `report-writing` executes the outline from `synthesis-rationale.md` in that voice. If published reviews were read only to learn how to write, copy **form only** — do not import their findings into the article.

Produce a **PhD-quality, argument-driven journal review** of **all** in-scope evidence (original sample plus any successfully retrieved gap-fill papers), with thematic subsections and numbered citations from retrieved full texts.

- Run-based review: `review/runs/<run-id>/article.md`, also copied to `review/report/final-report.md` if useful.
- Folder-of-PDFs review: `review/report/final-report.md`.

The article is a **secondary** paper: it does not report a new experiment. It teaches the reader the physiology or technology later sections assume, then compares included results, names gaps, and says what to measure next.

**Introduction must teach, every time, without the user asking.** Open on the phenomenon in present tense (not “This review discusses…”). Write enough background that a reader expert in an **adjacent** field (not this subfield) can follow §§3–N: the clinical or biological problem, what current options already do and still fail, the compartments or tools later sections assume, and the live controversy. Put the aim or central argument in the **last** paragraph of the Introduction (`The aim of this review is…` / `The central argument of this review is…`). Headings name topics or arguments, not papers. **Do not use a generic `## Results` dump** and a stack of leftover `###` how-to fragments. Numbered thematic sections come from rationale (e). Do not dump screening theatre or “user-supplied seeds” into the Introduction. If the first draft would only make sense to someone who already knows the papers, **rewrite it before the user sees it** — that rewrite is part of the workflow, not a favour after a complaint.

`check_article.py` fails a too-short Introduction, a missing aim paragraph, a generic Results heading, or too few thematic `##` sections. Passing the 6,000-word floor is not enough. The double-check must record an adjacent-field reader test; if it fails, rewrite without asking the user.

**Title.** Prefer a colon subtitle that names the kind and the argument (`Topic: a narrative review of …`). The title is about the field, not about a list of papers or a database export.

**Abstract.** For a narrative review, the abstract is a map of the topic. Do **not** cite (`[1]`) and do **not** name included papers. Rank kinds of evidence. At most one hinge finding, still unnamed. Exact n, p, RR, and bioavailability belong in Results and in Table 1, not stacked in the Abstract. Structured abstracts (with pooled numbers, still without citations) are for systematic reviews and meta-analyses only.

**Length.** Unless the user asked for a short note, aim for at least ~6,000 words of body text (about 20 pages in a typical double-spaced Word document). Add length by teaching in the Introduction and by giving each included study its design and results — not by slogans or process talk.

**Tables in the article.** Put numbered Markdown results tables in `article.md` (Table 1, Table 2, …) with a caption, the paper, n, endpoint, and result in the cells. Mention the table from the Results: “Primary endpoints are summarised in Table 1 [1].” That is not the extraction worksheet in `literature-table.md`; curate comparable rows. `check_article.py` fails if the manuscript has no pipe table or no “Table N” callout.

**Abbreviations.** Terms that repeat (about five times or more) are written out once, then the short form: `type 2 diabetes (T2D)`, then `T2D`. Introduce the short form in a sentence that still teaches what the thing is. A first-time reader in an adjacent field must follow the Abstract and Introduction without a glossary — write the Abstract in words; at most four abbreviations, and only ones the Abstract reuses. See `review-prose`. Do not invent abbreviations, and do not keep spelling the long form after it has been defined.

Every included paper must be discussed with enough design and result detail to stand as a real review (not a citation dump). **Sentences must be constructed as in a scientific article:** the subject is the finding or the mechanism; the citation is evidence. Do not write a sequence of “Author et al. did X. This paper is a pilot.” file cards. **Discussion and Conclusions must read like a published scientific paper:** interpret mechanisms, clinical meaning, why studies cannot be pooled, and evidence limitations. Do **not** put screening counts, “OA export”, “PDFs we could open”, fetch logs, HTTP errors, token estimates, phase logs, or script names in the Abstract, Discussion, or Conclusions — those belong in `prisma.md` and `usage-log.md`. Methods may state search and eligibility briefly. Every claim must be traceable to the table/notes (including gap-fill rows). Open **scientific** gaps stay open in the prose. **Token estimates, phase logs, and script names must NEVER appear in the journal article.** Write in ordinary scientific English (`is`/`are`/`was`/`showed`); after drafting, grep the banned chatbot flourishes listed in `review-prose` and cut them.

### 8. Quality gate (mandatory, before you say it is done)

Use the `article-qa` skill. Do **not** skip this, and do not tell the user the article is ready while a script fails.

```bash
python3 scripts/check_extraction.py --notes-dir review/runs/<run-id>/notes \
  --screening review/runs/<run-id>/screening.json
python3 scripts/check_article.py \
  --article review/runs/<run-id>/article.md \
  --table review/runs/<run-id>/table/literature-table.md
```

If `check_article.py` fails, rewrite the draft (`review-prose`) and run it again. Repeat until exit 0. Use `--short` only if the user asked for a short note. A passing script is still not a passing story if you only noticed that after the user said the Introduction does not teach — treat that as a workflow bug and fix the draft **and** the skills so the next topic does not need the same complaint.

### 9. Double-check (mandatory, after the scripts)

Use the `double-check` skill. Scripts can pass while notes are still leads, the literature table is still a DRAFT, a number in the article does not match the PDF, **or the Introduction still does not teach**. Spot-check at least five numeric claims against notes (and the PDF if they disagree), confirm the Abstract has no citations, confirm in-article tables, apply the **adjacent-field reader test** to the Introduction and heading spine, and write `review/runs/<run-id>/double-check.md`. If the teaching test fails, rewrite `article.md` without waiting for the user. If this is a re-run of the same papers, keep the previous manuscript as `article-pass1.md`, rewrite `article.md`, and rank both passes in that log. **Do not tell the user the article is done until this log exists.**

### 10. Iterate

Always hand them the **Markdown** article first (`review/runs/<run-id>/article.md` and/or `review/report/final-report.md`). Then ask if they want to: add more papers (loop back to step 3/4 or 6), adjust scope (loop back to step 2), refine a section, **or export Word/PDF** (Times New Roman, justified) via the `export-manuscript` skill. Do not build Word/PDF unless they ask.

## Hard rules (apply throughout)

1. **Never fabricate a citation, quote, or finding.** If you're not sure a paper says something, say you're not sure. This applies most acutely when searching for extra papers, but holds everywhere.
2. **Never silently skip a paper.** If a PDF can't be read or a paper is deemed out of scope, say so explicitly and why.
3. **Talk to the user before going deep on scope.** Step 2 is not optional. Don't extract 20 papers before confirming direction.
4. **Understand the sample before writing the article.** Step 6 is not optional. Don't start `article.md` from the table alone.
5. **Ground the article in the table, notes, and rationale.** The article must not introduce claims that aren't backed by those files. Unfilled gaps are stated, not speculated away.
6. **No required external services for reading local PDFs.** Extraction and the rationale can run on files already in the repo. Targeted extra retrieval uses the same public OA path as `oa-fetch`. If the network fails or no OA PDF exists, document that and write the article with the gap left open — never treat a missing PDF as a reason to invent a citation, and never treat OA fetch as a paywall bypass.
7. **Keep outputs where they belong.** Per-paper notes → `review/notes/` (and run `notes/`). Table → `review/table/literature-table.md`. Rationale → `review/runs/<run-id>/synthesis-rationale.md` or `review/report/synthesis-rationale.md`. Article → `review/runs/<run-id>/article.md` and/or `review/report/final-report.md`. Usage/tokens → `usage-log.md` only.
8. **PDFs stay gitignored.** Do not commit downloaded PDFs.
9. **Do not deliver a failing first draft.** Notes must pass `check_extraction.py`. The article must pass `check_article.py` (including the teaching-Introduction and thematic-spine gates). Story quality is a default, not a user request. Do not rewrite a previous sample unless asked.

## Skills reference

| Step | Skill | Location |
|---|---|---|
| Reading/extracting a paper | `paper-extraction` | `.cursor/skills/paper-extraction/SKILL.md` |
| Building the comparison table | `literature-table` | `.cursor/skills/literature-table/SKILL.md` |
| Interpreting the sample + gap-fill retrieval | `synthesis-rationale` | `.cursor/skills/synthesis-rationale/SKILL.md` |
| Writing the journal review | `report-writing` | `.cursor/skills/report-writing/SKILL.md` |
| Review-article craft and human prose | `review-prose` | `.cursor/skills/review-prose/SKILL.md` |
| First-pass quality gate (scripts) | `article-qa` | `.cursor/skills/article-qa/SKILL.md` |
| Second look after the scripts | `double-check` | `.cursor/skills/double-check/SKILL.md` |
| Related papers (opt-in browse **or** gap-driven retrieval) | `related-paper-exploration` | `.cursor/skills/related-paper-exploration/SKILL.md` |
| Find OA papers when none (or few) were dropped | `find-papers` | `.cursor/skills/find-papers/SKILL.md` |
| Importing a Scopus/BibTeX export | `bib-import` | `.cursor/skills/bib-import/SKILL.md` |
| Fetching public OA PDFs | `oa-fetch` | `.cursor/skills/oa-fetch/SKILL.md` |
| PRISMA counts + phase/token log | `prisma-logging` | `.cursor/skills/prisma-logging/SKILL.md` |
| Optional Word/PDF/HTML (Times New Roman, justified) | `export-manuscript` | `.cursor/skills/export-manuscript/SKILL.md` |

## Worked examples

Before running this for real, you (the agent) and the user can both look at [`examples/`](examples/README.md) for a fully worked, clearly fictional literature table, synthesis rationale, and report — this shows the destination of the workflow without needing real papers first.
