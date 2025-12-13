# 🔥 IGNIS ANIMA - EXECUTION STRATEGY & ACTION PLAN

**Owner:** Lucas Miachon
**Last Updated:** November 5, 2025
**Objective:** Execute the Project Roadmap with maximum AI leverage and full automation.

---

## 1. THE IGNIS ANIMA PHILOSOPHY

"Ignis Anima" (Fire of the Soul) dictates how we execute. We prioritize intellectual fire (synthesis, validation, teaching) over manual labor.

1.  **Leverage Over Labor:** Never perform tasks manually that technology can automate.
2.  **AI as Primary Workforce:** You are the Director and Validator; AI (Claude, Elicit, Gamma, n8n) handles the execution.
3.  **Ruthless Velocity:** Prioritize Minimum Viable Products (MVPs). Perfectionism is the enemy of this aggressive timeline.
4.  **Automation First:** If a task is repeated more than twice, automate it immediately.

---

## 2. PRIORITIZATION & STRATEGIC PIVOTS

### Execution Priority:
1.  🥇 **Classes (3)** (Osteoporosis, Hypothyroidism, GRADE) - Due Nov 25
2.  🥈 **Automation of Everything** - Enabling infrastructure
3.  🥉 **Systematic Review** - Starts mid-Nov
4.  🌟 **Mini Interface** - Lowest priority

### Critical Pivots (Changes to the Original Plan):
-   **NO CUSTOM CODING:** The Mini Interface will be built using No-Code tools (e.g., Glide or Fillout). This saves 2 months.
-   **AI BLITZ WORKFLOW:** Classes will be created using rapid AI synthesis (Elicit/Consensus/NotebookLM), not slow manual review (Covidence).
-   **N8N CLOUD FIRST:** Use your premium n8n cloud account immediately; do not waste time setting up self-hosting on Oracle yet.

---

## 3. PHASE 0: THE ENABLING INFRASTRUCTURE (Today, Nov 5)

**Duration:** 4 Hours
**Goal:** Activate the foundational automation required to accelerate class creation. Automation (Priority 2) enables the Classes (Priority 1).

| Task | Description | Tools | Status |
| :--- | :--- | :--- | :--- |
| **Workspace Setup** | Create dedicated dashboards for the 3 classes and a central "Research Inbox" database. | Notion Pro | [ ] |
| **Zotero Setup** | Create collections for Osteoporosis, Hypothyroidism, and GRADE. | Zotero | [ ] |
| **Literature Pipeline v1**| Build the core automation: RSS feeds → AI Summary → Notion Research Inbox. | n8n Cloud, Feedly/PubMed, AI (Claude/OpenAI) | [ ] |

**Automation Implementation Note (The Non-Coder Way):**
Do not build the n8n workflow manually. Ask Claude/ChatGPT for the JSON structure:
> **Prompt:** "Generate the JSON code for an n8n workflow. 1. Trigger daily. 2. Read from a PubMed RSS feed (placeholder URL). 3. Extract the abstract. 4. Use an 'OpenAI' or 'Anthropic' node to summarize the abstract and rate its relevance to Osteoporosis. 5. Insert the Title, URL, AI Summary, and Score into a Notion database (placeholder ID)."

Paste the generated JSON into your n8n Cloud canvas and configure the credentials (API keys) and placeholders.

---

## 4. PHASE 1: THE 20-DAY CLASS SPRINT (Nov 6 - Nov 25)

**Goal:** Complete all 3 classes using the "AI Blitz" workflow. Run these in parallel.

### The AI Blitz Workflow:
`Elicit/Consensus → NotebookLM → Claude Ultra → Gamma`

#### WEEKS 1 & 2: Synthesis and Creation (Nov 6 - Nov 18)

| Step | Timeline | Description | Tools |
| :--- | :--- | :--- | :--- |
| **1. AI Synthesis** | Days 1-4 | Ask direct clinical questions (e.g., "What are the 2025 guidelines?"). Let AI synthesize evidence and identify the 5-10 key papers/guidelines. | Elicit Pro, Consensus Pro, Perplexity |
| **2. Deep Dive** | Days 5-7 | Upload the key documents into NotebookLM. Prompt it to create a Study Guide, FAQ, and Clinical Pearls based *only* on these sources. Save references to Zotero. | NotebookLM, Zotero |
| **3. Structuring** | Days 8-10 | Feed NotebookLM output into Claude. Prompt it to structure a 1-hour teaching presentation outline, including objectives and case studies. | Claude Ultra |
| **4. Slide Generation**| Days 11-13 | Paste the Claude outline directly into Gamma to instantly generate visual slides. | Gamma |

#### WEEK 3: Refinement (Nov 19 - Nov 25)

| Step | Timeline | Description | Tools |
| :--- | :--- | :--- | :--- |
| **5. Validation & Polish**| Days 14-20 | **High-Value Human Work:** Review for accuracy, nuance, and relevance. Add graphics and visual models (especially for GRADE). | Expertise, Canva Pro AI, Miro AI |
| **6. Delivery** | Nov 25 | Final review and delivery of classes. | - |

---

## 5. PHASE 2: SCALING AUTOMATION & STARTING RESEARCH

**Goal:** Expand automation infrastructure (Priority 2) and begin the Systematic Review (Priority 3).

### Automation Expansion (Starts Week 2)

1.  **Zotero to Notion Sync (n8n):**
    -   Automate the synchronization of saved papers in Zotero collections to relevant Notion databases, linking citations to notes.
2.  **Automated Draft Generation (The "Content Button"):**
    -   Build an n8n workflow triggered by a Notion status change.
    -   *Workflow:* Pulls notes from Notion → Sends to Claude (e.g., "Create a 1-page handout") → Saves output back to Notion.

### Systematic Review (Starts Week 3 - Nov 18)

1.  **Protocol Development (Week 3):** Define PICO, develop search strategy (use Elicit/Claude for keywords/MeSH terms), define criteria, and register on PROSPERO.
2.  **Infrastructure Setup (Week 3/4):** Set up the project in **Covidence** (necessary for formal systematic reviews). Execute searches and import results.
3.  **Screening (Week 4 onwards):** Begin Title/Abstract screening in Covidence.

---

## 6. PHASE 3: THE MINI INTERFACE (The 1-Hour Solution)

**Goal:** A fancy interface for data entry into an Excel-like format (Priority 4, Non-Research).
**Timeline:** Week 3 or 4.

**Choose ONE option. Do not code.**

1.  **Option 1 (Recommended - Best Integration): Fillout + Notion Pro**
    -   Creates a highly polished, sophisticated form that feeds directly into your existing Notion database.
    -   *Time:* 1 hour.
2.  **Option 2 (Recommended - Best App Experience): Glide + Google Sheets**
    -   Turns a spreadsheet into a beautiful, modern web application instantly.
    -   *Time:* 1-2 hours.

---

## 7. IMMEDIATE ACTION PLAN: THE NEXT 72 HOURS

*   **TODAY (Nov 5):**
    *   Complete Phase 0: Set up Notion Workspace and Zotero collections.
    *   Build the n8n Literature Alert Pipeline using the AI JSON generation hack.
*   **TOMORROW (Nov 6):**
    *   Start the AI Blitz (Phase 1, Step 1). Run Elicit and Consensus searches for all three class topics (Osteoporosis, Hypothyroidism, GRADE).
*   **DAY 3 (Nov 7):**
    *   Begin the Deep Dive (Phase 1, Step 2). Identify key papers, upload them to NotebookLM, and generate initial summaries and clinical pearls.

---

## 8. TIMELINE VISUALIZATION (NOVEMBER)