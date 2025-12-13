# README — All‑Concepts Mode (Paragraph Style)

Date: 2025-10-13


Purpose: On every prompt, I will first correct your English, then teach one concept for every theme in your pack. Each theme appears as a four-to-five sentence paragraph in plain language at the current level, starting at Basic. You control pacing with the words “go” to advance all themes, “go [theme]” to advance one theme, “explain better [theme]” to expand the same level, and “repeat [theme]” or “skip [theme]” to revisit or omit. Mini steps follow as short imperative sentences that each take one to two minutes. No bullets are used in this README; everything is written as full lines.

Themes included every time: Adult education; Decision theory; Philosophy of mathematics and science; Design basics; Course and class design; Canva for teaching; Machine learning and AI updates; Automation (Gmail → Notion via n8n); Daily flow; LLM systems; APIs and Postman; Evidence‑based medicine; Biostatistics and probability; Research capture (Zotero + BBT + scite); Git and GitHub; Notion SOPs and databases; Orange Data Mining; Security; Roles by tool; Up‑to‑date AI/API routine.

Output rules: I will keep style minimalist and factual, avoid emojis and exclamation points, preserve provenance fields when relevant (such as SourceAccount or Message‑ID), and cite official documentation when providing factual claims. No protected health information will be processed.

Levels: I start at Basic for all themes. After you say “go,” I will move the included themes to Intermediate for the next reply, and another “go” will move them to Advanced. I will hold any theme at its current level if you do not advance it.

Mini steps template for daily execution: Label one email Action and one Evidence. Run your Gmail → Notion workflow once and confirm that a new Task appears. Capture one URL into Notion Evidence. Draft one slide in Canva and export to PPTX. Make one small Git commit that records today’s progress. These steps should take ten minutes or less in total and anchor learning to action.

---

## Basic concepts (all themes)



## Adult education (andragogy)

Adults are self‑directed and goal focused, so instruction should start with a clear outcome and immediate relevance to their tasks. Use learners’ prior experience as an asset through concrete examples, brief peer sharing, and problem‑centered activities. Keep cognitive load low by chunking content and interleaving short practice with fast feedback to stabilize learning. Space review over time and use retrieval practice to strengthen memory and transfer to new problems. Learn more: https://www.coursera.org/learn/instructional-design-foundations-applications


## Decision theory

A decision compares options under uncertainty by clarifying choices, possible outcomes, and the probabilities that link them. Expected value gives a baseline rule for ranking options, but human preferences and utilities matter when stakes differ. Sensitivity analysis shows how conclusions change when probabilities or utilities shift within plausible ranges. Watch for framing effects and loss aversion, then document assumptions so others can audit the choice. Learn more: https://plato.stanford.edu/entries/decision-theory/


## Philosophy of mathematics and science

Mathematics advances by deduction from axioms to theorems, while science advances by testing conjectures against observations. Models in both domains are tools with scope: they simplify reality to explain or predict, and they fail outside their domain of fit. Prefer simpler models that predict well and track error, because simplicity aids generalization and communication. Distinguish proof from evidence and remember that measurement, theory‑ladenness, and underdetermination limit certainty. Learn more: https://plato.stanford.edu/entries/scientific-method/


## Design basics (visual and information)

Hierarchy, alignment, contrast, and spacing guide the eye and create readable structure in documents and slides. Reduce clutter and make one idea per slide or section so the audience processes the message without distraction. Use consistent grids and typography to support scanning, and add captions to anchor figures and data displays. Validate design by quick user tests that measure comprehension and time‑to‑find, then iterate to improve. Learn more: https://www.canva.com/learn/design-principles/


## Course and class design

Write one clear learning objective per session in observable terms so activities and checks align directly to it. Plan practice opportunities and concise feedback moments that let learners calibrate effort and adjust strategies. Sequence modules so skills build from simple to complex while managing cognitive load through examples and scaffolds. Close with brief retrieval practice and a reflection prompt that captures what changed in understanding. Learn more: https://www.cmu.edu/teaching/designteach/design/index.html


## Canva for teaching

Start with an accessible template and a small brand kit for fonts, colors, and iconography to keep materials consistent. Write short lines, use ample whitespace, and prefer high‑contrast text for readability in varied lighting conditions. Export both PPTX and PDF versions and version file names by date or tag to support sharing and rollback. Build a small library of reusable layouts and diagrams so you assemble new decks quickly with consistent quality. Learn more: https://www.canva.com/education/


## Machine learning and AI updates

Follow a small set of high‑signal sources so you are informed without overload, and record updates in a dated log. Run weekly micro‑tests that check whether a change in a model or API alters accuracy, speed, or cost for your tasks. Note the provenance of data, prompts, and configurations so differences are traceable and you can reproduce results. Convert noteworthy changes into tiny next actions with due dates in Tasks or Evidence hubs. Learn more: https://www.bensbites.com/


## Automation (Gmail → Notion via n8n)

Label messages as Action or Evidence near the time of capture so routing rules stay simple and reliable. Ingest messages into Notion Tasks or Evidence with a SourceAccount field to preserve provenance for each item. Use the email Message‑ID as a deduplication key so later re‑runs do not create duplicates or inflate counts. Add a Drive “Teaching Drop” watcher that creates Tasks with file links, then measure throughput and error rates. Learn more: https://docs.n8n.io/


## Daily flow

Begin with Gmail triage, capture three items to track, and process one PDF into short notes so progress starts concrete. Draft a single slide in Canva and export to PPTX to keep forward motion on teaching assets every day. Commit small changes in Git so work is saved and traceable, then trigger automations for Action, Evidence, and Drive. Review SOP pages weekly so instructions match reality and the loop remains trustworthy. Learn more: https://www.notion.so/help/guides/manage-tasks-in-notion


## LLM systems

Use ChatGPT for core reasoning and planning with prompts that are modular, explicit, and testable. Introduce tool use or memory only when the task demands state or integration, keeping complexity low by default. Compare outputs across models for critical tasks and log assumptions, errors, and fixes so quality improves over time. Treat prompts and evaluations as versioned artifacts that you can roll back and audit. Learn more: https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/


## APIs and Postman

Understand endpoints, headers, authentication, and JSON schemas before you automate requests. Send a simple GET request, parse the body, and add basic error handling to make behavior predictable. Chain three requests with variables and tests so you can validate outputs end to end without manual checks. Keep environments and secrets separate from code and document how to reproduce calls. Learn more: https://learning.postman.com/docs/getting-started/introduction/


## Evidence‑based medicine

Start with a focused PICO question to constrain searches and reduce irrelevant results during screening. Track inclusion decisions transparently and appraise bias so summaries are explainable and defensible. Extract effect sizes in comparable forms and map a PRISMA flow to describe the evidence pipeline. State the strength of evidence and the limits so users understand where claims may not generalize. Learn more: https://training.cochrane.org/handbook


## Biostatistics and probability

Summarize data with clear tables and graphics and describe distributions before applying models. Quantify uncertainty using intervals and hypothesis tests that match design and assumptions. Check model assumptions and power, then prefer simpler models that meet goals and communicate well. Use small simulations to probe edge cases and to debug intuition when formulas feel opaque. Learn more: https://pll.harvard.edu/series/data-analysis-life-sciences


## Research capture (Zotero + BBT + scite)

Save sources with stable citekeys and descriptive tags so items are easy to retrieve and cite consistently. Use Smart Citations to see whether a claim is supported, contradicted, or merely mentioned in later work. Keep a focused to‑read queue and schedule short passes so literature review advances regularly. Export selected notes and links to Notion Evidence to integrate with tasks and teaching assets. Learn more: https://www.zotero.org/support/quick_start_guide


## Git and GitHub

Initialize a repository, add files, write concise commits, and push to a remote so work stays versioned and recoverable. Use branches and pull requests for changes, then review diffs to maintain quality and accountability. Adopt clear naming and tagging so weekly releases snapshot assets for classes or reports. Protect the repo with two‑factor authentication and scoped personal access tokens. Learn more: https://skills.github.com/


## Notion SOPs and databases

Define properties for Tasks, Projects, and Evidence so items carry the structure needed for views and automation. Store provenance fields such as SourceAccount and Message‑ID to deduplicate and audit your pipelines. Create views for today, this week, and review queues so work stays visible and prioritized. Build dashboards that show throughput, blockers, and a cadence of review to improve reliability. Learn more: https://www.notion.so/help/intro-to-databases


## Orange Data Mining

Load a CSV and inspect distributions to understand data before modeling in Orange’s visual workflow. Train a simple classifier or regressor with defaults and note accuracy on a holdout sample. Use widgets for feature scoring and model comparison to select a reasonable baseline. Export a short report or screenshot so results enter your Evidence hub. Learn more: https://orangedatamining.com/getting-started/


## Security

Enable two‑factor authentication on all critical accounts and store backup codes securely. Grant least‑privilege scopes to apps and integrations and review access quarterly to remove what you no longer need. Avoid placing protected health information in third‑party AI tools or public repositories unless contracts allow it. Run periodic audits and prefer dry‑runs for sync operations to avoid unintended changes. Learn more: https://myaccount.google.com/signinoptions/two-step-verification


## Roles by tool

Assign ChatGPT to core reasoning and planning, Gemini to Gmail and Drive triage, and Claude to long‑context analysis. Record outcomes and deltas in a Notion dashboard so tool choices are justified by results rather than habit. Swap tools only when a measurable improvement appears in speed, accuracy, or effort. Document which tool handles which class of task so collaborators can follow the same map. Learn more: https://www.notion.so/


## Up‑to‑date AI/API routine

Skim two newsletters daily and star one item to test so attention turns into action. Check vendor changelogs twice per week for breaking changes to assistants, models, and APIs. Read one Latent Space summary and watch one short demo weekly to refresh mental models. Add one micro‑test with a due date to Tasks so learning compounds. Learn more: https://www.latent.space/
