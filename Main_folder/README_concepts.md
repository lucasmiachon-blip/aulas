# MetaVida — Concept Teaching Prompt and Modules

Date: 2025-10-13

This README gives you a reusable teaching prompt plus concise 3–4 line 
summaries for each topic at three levels: Basic, Intermediate, Advanced.
It follows your Master prompt, weekly plan, and AI/API routine.
fileciteturn0file1turn0file0turn0file2
Every prompt i type u give me the 3-4 line concept and reference

---

## Master prompt to paste into ChatGPT

**Role**: You are a synthetic assistant. Explain one concept at a time with tight 3–4 line chunks per level: **Basic → Intermediate → Advanced**. Wait for my signal “next” before moving to the next level or topic. Keep style minimalist and factual. No emojis, no exclamation points.

**Method**
1) Start with a plain-language definition and one concrete example.
2) Add mechanics and a second example at Intermediate.
3) Add edge cases, trade‑offs, or math at Advanced.
4) Close each topic with a short “Next actions (10–15 min)” checklist tied to my tools.
5) Preserve **provenance** when relevant (SourceAccount, dataset, link). Cite official docs if you reference facts.
6) Do not include PHI. Follow my weekly AI/API routine for updates.” fileciteturn0file1turn0file2

**Tools and outputs to reference when useful**: Notion (Tasks, Evidence), Gmail and Drive, n8n, Git/GitHub, Zotero+BBT+scite, Canva/Miro, Orange, Postman, LLM APIs. Use small checklists and upsert semantics. fileciteturn0file1turn0file0

---

## Concept modules (3 tiers each)

### 1) Adult education (andragogy)
**Basic**: Adults are goal‑driven and self‑directed. Start with clear outcomes, immediate relevance, and problem‑centered tasks. Use prior experience as an asset through examples and peer sharing.  
**Intermediate**: Chunk content, interleave practice, and give timely feedback. Use retrieval practice and spaced repetition. Support autonomy and choice while keeping cognitive load low.  
**Advanced**: Design mastery paths with formative checks and reflection prompts. Use data on completion and error patterns to adapt instruction and close skill gaps.

### 2) Decision theory
**Basic**: Decisions balance benefits, harms, and uncertainty. Frame choices, list options, and define outcomes. Use expected value to compare simple options.  
**Intermediate**: Incorporate probabilities from data. Use sensitivity analysis to see how conclusions change. Watch for loss aversion and framing effects.  
**Advanced**: Model with Bayesian updates and utility functions. Include constraints, priors, and value of information. Document assumptions and choose robust options.

### 3) Philosophy of mathematics and science
**Basic**: Math builds abstract structures; science tests claims against observations. Both seek reliable knowledge with different methods.  
**Intermediate**: Distinguish proof (deductive) from evidence (inductive). Note limits: underdetermination, measurement error, and theory‑ladenness.  
**Advanced**: Use falsifiability, model selection, and simplicity criteria. Treat models as tools with scopes, not mirrors of reality; track where they fail.

### 4) Design basics (visual and information)
**Basic**: Use hierarchy, alignment, contrast, and spacing. Reduce clutter and make one idea per slide or section.  
**Intermediate**: Apply grids, consistent typography, and color used sparingly. Support scanning with headings and captions.  
**Advanced**: Prototype fast, test with users, and iterate on comprehension and time‑to‑find metrics. Measure readability and error rates.

### 5) Course and class design
**Basic**: Set one clear learning objective per session. Align activities and checks with the objective.  
**Intermediate**: Map a course with modules, outcomes, assessments, and feedback cycles. Build weekly cadence and office hours.  
**Advanced**: Add authentic assessments, rubrics, and analytics. Use item analysis and revision logs to improve reliability.

### 6) Canva for teaching
**Basic**: Start from a simple template. Use brand kit for fonts and logo. Keep slides light and readable.  
**Intermediate**: Build reusable layouts, add alt text, and export PPTX/PDF. Version files with dates.  
**Advanced**: Create a slide library and components. Standardize diagrams and automate export to OneDrive/Git. fileciteturn0file0

### 7) Machine learning and AI updates
**Basic**: ML learns patterns from data to make predictions. Track only a few core metrics and document data sources.  
**Intermediate**: Use train/validation/test splits and sanity checks. Maintain an update log for models and APIs.  
**Advanced**: Add monitoring, drift alerts, and evaluation suites. Follow your weekly AI/API routine to test vendor changes. fileciteturn0file2

### 8) Automation: Gmail → Notion via n8n
**Basic**: Label emails as **Action** or **Evidence**. Ingest to Notion Tasks/Evidence. Keep **SourceAccount** to preserve origin.  
**Intermediate**: Upsert by Message‑ID. Extract first URL for Evidence. Test each node and log runs.  
**Advanced**: Add Drive “Teaching Drop”, retries, and idempotent flows. Publish dashboards for throughput and errors. fileciteturn0file0

### 9) Daily flow (teaching prep)
**Basic**: Scan Gmail, pick 3 items, process one PDF, draft slides, commit changes.  
**Intermediate**: Keep SOP pages current and tie tasks to outcomes. Use small time boxes.  
**Advanced**: Track throughput and hit rate from scans to shipped assets. Tighten the loop weekly. fileciteturn0file1

### 10) LLM systems
**Basic**: Use ChatGPT for reasoning and planning. Keep prompts modular.  
**Intermediate**: Add tool use and memory via frameworks. Compare outputs across models.  
**Advanced**: Orchestrate multiple models with guardrails and tests. Log assumptions and errors. fileciteturn0file1

### 11) APIs and Postman
**Basic**: Know endpoints, headers, auth, and JSON. Send a GET and parse the body.  
**Intermediate**: Build a 3‑request chain with variables and tests. Handle rate limits and errors.  
**Advanced**: OAuth flows, environments for dev/prod, and CI checks for collections. fileciteturn0file0

### 12) Evidence‑based medicine
**Basic**: Form a PICO question, search, and screen studies. Track inclusion decisions.  
**Intermediate**: Appraise bias and extract effect sizes. Draw a PRISMA flow.  
**Advanced**: Plan meta‑analysis, explore heterogeneity, and state limits clearly. fileciteturn0file0

### 13) Biostatistics and probability
**Basic**: Summaries, samples, and distributions. Define uncertainty with intervals.  
**Intermediate**: Hypothesis tests and simple regression. Power and assumptions.  
**Advanced**: Bayesian updates, survival ideas, and simulation to check reasoning. fileciteturn0file0

### 14) Research capture (Zotero + BBT + scite)
**Basic**: Save sources with citekeys and tags. Keep to‑read lists focused.  
**Intermediate**: Use Smart Citations and discovery feeds into Zotero.  
**Advanced**: Template notes and export to Notion Evidence. fileciteturn0file0

### 15) Git and GitHub
**Basic**: init, add, commit, push. Clear repo layout.  
**Intermediate**: Branches, PRs, and tags. Write meaningful messages.  
**Advanced**: Releases, PAT use, and scheduled publishing. fileciteturn0file0

### 16) Notion SOPs and databases
**Basic**: Tasks, Projects, Evidence with clear properties and views.  
**Intermediate**: Upsert semantics, dedupe keys, provenance fields.  
**Advanced**: Dashboards for throughput and review cadence. fileciteturn0file1

### 17) Orange Data Mining
**Basic**: Load CSV, visualize, train a simple model.  
**Intermediate**: Build small pipelines with validation.  
**Advanced**: Use reports and pair with EBM examples. fileciteturn0file0

### 18) Security
**Basic**: 2FA everywhere. Avoid PHI in third‑party AIs.  
**Intermediate**: Minimal scopes and dry‑run syncs.  
**Advanced**: Regular audits and access reviews. fileciteturn0file0

### 19) Roles by tool
**Basic**: ChatGPT core reasoning. Gemini triage. Claude long context.  
**Intermediate**: Cross‑check outputs; select per task.  
**Advanced**: Track deltas and outcomes in Notion dashboards. fileciteturn0file1

### 20) Up‑to‑date AI/API routine
**Basic**: Daily skim of key newsletters. Star one item to test.  
**Intermediate**: Twice‑weekly vendor checks and short notes.  
**Advanced**: Weekly deep dive and one micro‑test added to Tasks. fileciteturn0file2

---

## How to use this file
1) Paste the **Master prompt** into ChatGPT.  
2) Tell the assistant the **topic**. It will output Basic first. Say “next” to get Intermediate, then Advanced.  
3) After Advanced, it will print **Next actions (10–15 min)** tied to your stack. fileciteturn0file1
