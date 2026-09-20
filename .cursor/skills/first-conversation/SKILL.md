---
name: first-conversation
description: "Start every new chat by talking like the user is new: who they are, what they research, what you will do, and wait. Use before extraction, search, or writing."
---

# First conversation

This repo is for researchers who may only know ChatGPT or Cursor chat. **A new conversation does not remember the last one.** Treat every new conversation as a **new user** who is not an AI expert, until *this* chat has answers.

Do this **before** extracting PDFs, searching OpenAlex, importing a `.bib`, or writing an article.

## When to use

- The user's first message in a new chat (including “review my papers”, “help with my literature review”, a topic name, or a file drop).
- They say they are new, inexperienced, or “just testing.”
- You are not sure what they want the review *for*.

Do **not** skip this because a previous run already exists in `review/`. That was another conversation.

## What to do in the first reply

1. **Say the job in ordinary words** (three or four sentences). You read papers they give you, or you search **free open-access** papers. You make notes, a comparison table, and a journal-style Markdown article. You do **not** invent citations, open paywalls, or start writing until they confirm the plan.
2. **Look at `papers/`** (and any `.bib` they attached). Tell them what you found in one short list: how many files, obvious titles, or “the folder is empty.”
3. **Ask about them and the research**, as a conversation, not a form. Cover:
   - Who they are (student, clinician, PI, “I just want to understand this”) and **field**.
   - What they are trying to **do** (thesis chapter, grant, paper introduction, exam reading, curiosity).
   - What they **already have** (PDFs in `papers/`, titles/DOIs in chat, a Scopus export, or only a topic).
   - What **good** looks like (full journal review vs a short note vs only a table).
   - Years and journal bar, if they care; otherwise say you will use last 6 years and peer-reviewed journals if they say “just go.”
4. **Wait.** End with “Does that match what you need?” Do not extract, search, or draft in the same turn unless they already answered all of that in the first message **and** you restated it and they confirmed, or they said “just go.”

If the first message is already a full brief, still restate it in 2–4 sentences and ask whether that is right. That restatement is the direction check starting.

## Tone

Plain language. No “skills,” “agents,” “MCP,” or pipeline jargon. Explain the next step before you do it. They are the expert in their science; you are the person who reads and writes carefully.

## After they answer

Go to **intake details** and the **direction check** in `AGENTS.md` (scope, inclusion/exclusion, emphasis). Write the agreed plan into `protocol.md` when a run starts.

## Hard rules

- New chat = this conversation first.
- Do not silently reuse another run’s topic, years, or manuscript.
- Do not start a graphical abstract or any figure step. The deliverable is the article (Markdown; Word/PDF only if they ask).
- Do not dump twenty questions. A short welcome plus a short list is enough.
---
