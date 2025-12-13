# Main Plan — ChatGPT core • Gemini + Claude secondary • n8n automation

**Time**: ~3 h/day. Heavy weight on AI/ML, APIs, automation. Next: biostats, probability, EBM.
**Goal by March**: intermediate‑to‑high biostatistics, advanced EBM, strong interactive classes, fluent daily AI.
**Long term**: top 0.01% conceptual grasp in math/biostats; broad AI fluency.

## Assistants priority
1) **ChatGPT** — core assistant for reasoning, code, stats, planning.
2) **Gemini Advanced** and **Claude** — secondary for Gmail/Drive summaries (Gemini) and long‑context second opinions (Claude).

## Automation choice
Single platform: **n8n** (open‑source, monthly cloud). No Make/Zapier unless n8n fails a requirement.

## Stack & roles
- **ChatGPT**: reasoning, coding, stats mentoring, planning.
- **Gemini Advanced**: Gmail/Drive/Docs summaries; quick drafting.
- **Claude**: second‑opinion reasoning; long‑context analysis and drafting.
- **Perplexity Pro**: fresh web answers with citations.
- **Elicit / Consensus**: paper discovery and evidence answers.
- **ChatPDF Pro**: Q&A on one PDF; extract structured takeaways.
- **Isabel Pro**: differential support; record rationale.
- **Zotero + Better BibTeX + scite**: capture, tag, cite; lock citekeys; smart citations.
- **Research Rabbit / Feedly**: explore networks; track journals; push to Zotero.
- **Canva Pro / Miro Pro**: visual style; diagrams; storyboards.
- **VS Code / GitHub Pro**: coding and version control.
- **n8n / rclone**: automations and bulk sync (test with `--dry-run`).
- **Orange Data Mining**: no‑code ML workflows.
- **Notion**: Tasks, Projects, Evidence hub.

## Daily flow (repeat)
1) Gmail triage → Gemini summary → apply labels **Action** / **Evidence**.
2) Discovery → Perplexity (Past 7 days) + Feedly → push 3 items to **Zotero ▸ To‑Read**.
3) Evidence pass → pick 1 PDF → ChatPDF summary → save *takeaway + link* to **Notion/Evidence**.
4) Teaching → ChatGPT outline → style in Canva → export PPTX/PDF.
5) Coding/versioning → work in VS Code → commit to GitHub.
6) Automation → n8n workflows run Action/Evidence/Drive‑drop → Notion.

## Security baseline
- 2FA on all services. No PHI to third‑party AIs.
- GitHub: use a fine‑scoped **PAT** for repo access.
- rclone: test with `--dry-run` before any sync or copy.

## Course tracks (two per topic)

### LLMs & Agents
- **Building Systems with the ChatGPT API — DeepLearning.AI**
  https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/
- **LangChain for LLM Application Development — DeepLearning.AI**
  https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/

### ML core
- **Machine Learning Specialization — Andrew Ng (Coursera)**
  https://www.coursera.org/specializations/machine-learning-introduction
- **Generative AI with Large Language Models — DeepLearning.AI + AWS (Coursera)**
  https://www.coursera.org/learn/generative-ai-with-llms

### APIs & Automation
- **Postman: The Complete Guide — REST API Testing (Udemy)**
  https://www.udemy.com/course/postman-the-complete-guide/
- **n8n docs and tutorials**
  https://docs.n8n.io/

### Biostatistics & Probability
- **Mathematical Biostatistics Boot Camp 1 — Johns Hopkins (Coursera)**
  https://www.coursera.org/learn/biostatistics
- **Data Analysis for Life Sciences (PH525x) — HarvardX**
  https://pll.harvard.edu/series/data-analysis-life-sciences

### Evidence‑Based Medicine
- **Introduction to Systematic Review and Meta‑Analysis — JHU (Coursera)**
  https://www.coursera.org/learn/systematic-review
- **Design and Interpretation of Clinical Trials — JHU (Coursera)**
  https://www.coursera.org/learn/clinical-trials

### Math foundations
- **Mathematics for Machine Learning — Imperial (Coursera)**
  https://www.coursera.org/specializations/mathematics-machine-learning
- **MITx Calculus 1A: Differentiation**
  https://mitxonline.mit.edu/courses/course-v1%3AMITxT%2B18.01.1x/

### Instructional design
- **Instructional Design Foundations and Applications — UIUC (Coursera)**
  https://www.coursera.org/learn/instructional-design-foundations-applications
- **e‑Learning Ecologies — UIUC (Coursera)**
  https://www.coursera.org/learn/elearning

### No‑code ML with Orange
- **Orange tutorials (YouTube)**
  https://www.youtube.com/@OrangeDataMining
- **Orange — Getting Started**
  https://orangedatamining.com/getting-started/

### Git & GitHub
- **Version Control with Git — Atlassian (Coursera)**
  https://www.coursera.org/learn/version-control-with-git
- **Introduction to Git and GitHub — Google (Coursera)**
  https://www.coursera.org/learn/introduction-git-github

## YouTube channels (math)
- **Professor Leonard** — Calculus I–III full lectures.
  https://www.youtube.com/@ProfessorLeonard
- **TrevTutor** — proofs, discrete math, linear algebra, probability.
  https://www.youtube.com/@TrevTutor

## Micro‑projects (first 4 weeks)
1. AI SOP: reusable prompts for clinic admin, teaching prep, literature work.
2. Assistants: small ChatGPT Assistants API runner that drafts lecture outlines and pushes to Notion.
3. APIs: Postman collection that calls an LLM API and writes CSV.
4. Automation: n8n workflow to send Gmail label **Action** → Notion/Tasks (key = MessageID).
5. Evidence: Consensus/Elicit search → capture 3 papers to Zotero; verify with scite.
6. Teaching: ship a 6–8 slide Canva‑styled deck; export PPTX and PDF.

## Folder structure
 ## tokens## 
 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
