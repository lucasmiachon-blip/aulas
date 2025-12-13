# 🎯 PROJECT ROADMAP - LUCAS MIACHON

**Last Updated:** November 5, 2025  
**Status:** Active Development  
**Completion Target:** Q1 2026

---

## 📋 TABLE OF CONTENTS

1. [Overview](#overview)
2. [Active Projects (Next 20 Days)](#active-projects-next-20-days)
3. [Short-Term Projects (1-2 Months)](#short-term-projects-1-2-months)
4. [Timeline Visualization](#timeline-visualization)
5. [Tech Stack Per Project](#tech-stack-per-project)
6. [Automation Opportunities](#automation-opportunities)
7. [Success Metrics](#success-metrics)

---

## 🎯 OVERVIEW

**Mission:** Develop comprehensive EBM teaching materials and tools while building automation infrastructure for clinical research.

**Total Projects:** 6  
**Urgent Projects (≤20 days):** 3  
**Medium-Term Projects (1-2 months):** 3

---

## ⚡ ACTIVE PROJECTS (NEXT 20 DAYS)

### 1. 🦴 OSTEOPOROSIS REVIEW + CLASS

**Timeline:** 20 days  
**Deadline:** November 25, 2025  
**Status:** 🔴 Not Started

#### Deliverables:
- [ ] Complete literature review
- [ ] Systematic review document
- [ ] Teaching presentation (slides)
- [ ] Class handouts/materials
- [ ] References organized in Zotero

#### Workflow:
```
Literature Search (Consensus/Elicit)
  ↓
Screen Papers (Covidence)
  ↓
Extract Data (Zotero)
  ↓
Synthesize (NotebookLM + Claude)
  ↓
Create Slides (Gamma/SlideSpeak)
  ↓
Design (Canva)
  ↓
Final Review
```

#### Tech Stack:
- **Research:** Consensus, Elicit, Scite, Covidence
- **Organization:** Zotero, Notion
- **Analysis:** NotebookLM, Claude
- **Creation:** Gamma, SlideSpeak, Canva

#### Automation:
- n8n workflow: PubMed alerts → Notion database
- Daily research digest from Feedly
- Auto-citation formatting

---

### 2. 🦋 HYPOTHYROIDISM REVIEW + CLASS

**Timeline:** 20 days  
**Deadline:** November 25, 2025  
**Status:** 🔴 Not Started

#### Deliverables:
- [ ] Complete literature review
- [ ] Clinical guidelines synthesis
- [ ] Teaching presentation (slides)
- [ ] Case studies for class
- [ ] References organized in Zotero

#### Workflow:
```
Guidelines Review (UpToDate/Dynamed)
  ↓
Literature Search (Consensus/Elicit)
  ↓
Case Development (ChatGPT/Claude)
  ↓
Slides Creation (Gamma)
  ↓
Clinical Pearls Summary (NotebookLM)
```

#### Tech Stack:
- **Research:** Consensus, Elicit, Perplexity
- **Guidelines:** Clinical databases
- **Case Creation:** ChatGPT Pro, Claude
- **Slides:** Gamma, Presentation AI

#### Automation:
- Guideline updates → Notion
- Case template generation (ChatGPT)
- Auto-summary of new papers

---

### 3. 📊 GRADE SYSTEM REVIEW + CLASS

**Timeline:** 20 days  
**Deadline:** November 25, 2025  
**Status:** 🔴 Not Started

#### Deliverables:
- [ ] GRADE methodology review
- [ ] Evidence quality assessment framework
- [ ] Interactive teaching presentation
- [ ] Practice exercises
- [ ] GRADE templates/tools

#### Workflow:
```
GRADE Official Resources
  ↓
Practical Examples (Literature)
  ↓
Teaching Framework (Claude)
  ↓
Interactive Slides (Gamma)
  ↓
Practice Tools (Mini Interface)
```

#### Tech Stack:
- **Research:** Consensus, Scite
- **Framework:** Miro AI (visual mapping)
- **Teaching:** Gamma, SlideSpeak
- **Practice:** Custom web tool (Cursor)

#### Automation:
- GRADE checklist generator
- Evidence table auto-population
- Quality assessment templates

---

## 🚀 SHORT-TERM PROJECTS (1-2 MONTHS)

### 4. 📚 SYSTEMATIC REVIEW OF EBM

**Timeline:** 2 months  
**Start:** November 5, 2025  
**Deadline:** January 5, 2026  
**Status:** 🟡 Planning Phase

#### Objectives:
- Conduct comprehensive systematic review
- Meta-analysis (if applicable)
- Publication-ready manuscript
- Teaching materials derived from review

#### Phases:

**Phase 1: Protocol (Week 1-2)**
- [ ] PICO/PECO question definition
- [ ] Search strategy development
- [ ] Inclusion/exclusion criteria
- [ ] Data extraction forms
- [ ] Risk of bias tools selection
- [ ] PROSPERO registration

**Phase 2: Search & Screen (Week 3-4)**
- [ ] Database searches (PubMed, Embase, Cochrane)
- [ ] Citation management (Zotero)
- [ ] Title/abstract screening (Covidence)
- [ ] Full-text screening
- [ ] Reference list screening

**Phase 3: Data Extraction (Week 5-6)**
- [ ] Extract study characteristics
- [ ] Extract outcomes data
- [ ] Risk of bias assessment
- [ ] Quality of evidence (GRADE)

**Phase 4: Analysis & Writing (Week 7-8)**
- [ ] Meta-analysis (Orange Data Mining/R)
- [ ] Evidence synthesis (NotebookLM)
- [ ] Manuscript drafting (Claude + Grammarly)
- [ ] Figure/table creation (Orange/Canva)

#### Tech Stack:
- **Protocol:** Covidence, Notion
- **Search:** PubMed, Embase (via institution)
- **Screening:** Covidence
- **Data:** Zotero, Excel, Notion
- **Analysis:** Orange Data Mining, R (optional)
- **Writing:** Claude, ChatGPT, Grammarly
- **Visualization:** Canva, Orange

#### Automation:
- Search alerts → Notion
- Citation auto-import (Zotero + n8n)
- Data extraction templates
- PRISMA diagram auto-generation
- Reference formatting automation

---

### 5. 🖥️ MINI "REDCAP" INTERFACE

**Timeline:** 2 months  
**Start:** November 5, 2025  
**Deadline:** January 5, 2026  
**Status:** 🟡 Planning Phase

#### Objectives:
Create a simple, beginner-friendly web form interface for data collection and organization.

#### Features:

**Core Functionality:**
- ✅ Simple form builder (drag & drop)
- ✅ Field types: Text, Number, Date, Dropdown, Checkbox
- ✅ Data validation
- ✅ Real-time table view (Excel-like)
- ✅ Export to CSV/Excel
- ✅ Import existing data
- ✅ Basic user authentication

**Advanced Features (Optional):**
- 📋 Calculated fields
- 📋 Conditional logic (show/hide fields)
- 📋 Data visualization (charts)
- 📋 Multi-user collaboration
- 📋 Version control

#### Tech Stack:

**Frontend:**
- HTML/CSS/JavaScript
- React (or simple vanilla JS)
- TailwindCSS for styling

**Backend:**
- Node.js + Express
- SQLite database (simple, file-based)
- OR: Google Sheets API (no backend needed!)

**Hosting:**
- Oracle Free Tier
- OR: Vercel/Netlify (free tier)

**Development:**
- **Cursor** - AI-assisted coding
- **Claude/ChatGPT** - Code generation
- **GitHub** - Version control

#### Development Phases:

**Phase 1: MVP (Week 1-2)**
```
Simple form with 5 field types
  ↓
Save to local storage / Google Sheets
  ↓
Display in table view
  ↓
Export to CSV
```

**Phase 2: Enhancement (Week 3-4)**
```
Form builder interface
  ↓
Multiple forms
  ↓
Data validation
  ↓
Better UI/UX
```

**Phase 3: Advanced (Week 5-8)**
```
User authentication
  ↓
Database integration
  ↓
Conditional logic
  ↓
Charts/visualizations
```

#### Cursor Prompts to Use:
```
"Create a simple web form that saves data to Google Sheets"
"Build a form builder interface with drag & drop"
"Add data validation to form fields"
"Create Excel-like table view for form data"
"Add export to CSV functionality"
```

---

### 6. 📖 EBM 2-YEAR RESIDENCY PROGRAM

**Timeline:** 1 month  
**Start:** November 5, 2025  
**Deadline:** December 5, 2025  
**Status:** 🟡 Planning Phase

#### Objective:
Develop comprehensive Evidence-Based Medicine curriculum for 2-year residency program.

#### Deliverables:

**1. Curriculum Framework**
- [ ] Learning objectives (by year/rotation)
- [ ] Core competencies
- [ ] Assessment methods
- [ ] Milestones

**2. Year 1 Content**
- [ ] EBM fundamentals
- [ ] Critical appraisal skills
- [ ] Search strategies
- [ ] Study design understanding
- [ ] Statistics basics

**3. Year 2 Content**
- [ ] Advanced critical appraisal
- [ ] Systematic reviews
- [ ] Meta-analysis
- [ ] Guideline development
- [ ] Teaching EBM to others

**4. Teaching Materials**
- [ ] Lecture slides (all topics)
- [ ] Journal club templates
- [ ] Case studies
- [ ] Assessment tools
- [ ] Reading lists

**5. Implementation Plan**
- [ ] Schedule/calendar
- [ ] Faculty requirements
- [ ] Resources needed
- [ ] Evaluation strategy

#### Content Outline:

**YEAR 1: FOUNDATIONS**

**Quarter 1: Introduction to EBM**
- What is EBM? History and principles
- Formulating clinical questions (PICO)
- Information sources (databases)
- Search strategies
- Study designs overview

**Quarter 2: Critical Appraisal Basics**
- Therapy studies (RCTs)
- Diagnostic studies
- Prognostic studies
- Understanding statistics I
- Risk, odds, NNT/NNH

**Quarter 3: Harm & Systematic Reviews**
- Harm studies
- Cohort studies
- Case-control studies
- Introduction to systematic reviews
- Understanding meta-analysis

**Quarter 4: Guidelines & Application**
- Clinical practice guidelines
- GRADE system
- Applying evidence to patients
- Shared decision making
- Quality improvement

**YEAR 2: ADVANCED SKILLS**

**Quarter 1: Advanced Critical Appraisal**
- Bias assessment (Cochrane Risk of Bias)
- Precision and confidence intervals
- Subgroup analysis
- Heterogeneity
- Publication bias

**Quarter 2: Conducting Reviews**
- Systematic review protocol
- Search strategies (advanced)
- Screening & data extraction
- Risk of bias assessment
- GRADE quality assessment

**Quarter 3: Meta-Analysis**
- Introduction to meta-analysis
- Fixed vs random effects
- Forest plots interpretation
- Sensitivity analysis
- Software tools (RevMan, R)

**Quarter 4: Teaching & Leadership**
- Teaching EBM to medical students
- Leading journal clubs
- Guideline development
- Quality improvement projects
- Disseminating evidence

#### Tech Stack:
- **Curriculum Design:** Notion, Miro AI
- **Content Creation:** Claude, ChatGPT
- **Slides:** Gamma, SlideSpeak, Presentation AI
- **Assessment:** Custom form tool (Mini Interface)
- **Resources:** Zotero library

#### Automation:
- Auto-generate lesson plans
- Reading list automation
- Assessment tracking (Notion)
- Progress dashboard
- Certificate generation

---

## 📅 TIMELINE VISUALIZATION

```
NOVEMBER 2025
├── Week 1 (Nov 5-11)
│   ├── Start: Osteoporosis review
│   ├── Start: Hypothyroidism review
│   ├── Start: GRADE review
│   ├── Start: EBM Residency planning
│   ├── Start: Systematic Review protocol
│   └── Start: Mini Interface planning
│
├── Week 2 (Nov 12-18)
│   ├── Continue: All 3 classes (research phase)
│   ├── EBM Program: Curriculum outline
│   ├── Systematic Review: Protocol complete
│   └── Mini Interface: MVP design
│
├── Week 3 (Nov 19-25)
│   ├── DUE: Osteoporosis class ✅
│   ├── DUE: Hypothyroidism class ✅
│   ├── DUE: GRADE class ✅
│   ├── Systematic Review: Begin screening
│   └── Mini Interface: Begin coding
│
└── Week 4 (Nov 26-30)
    ├── EBM Program: Year 1 content draft
    ├── Systematic Review: Continue screening
    └── Mini Interface: MVP development

DECEMBER 2025
├── Week 1 (Dec 1-7)
│   ├── DUE: EBM Residency Program ✅
│   ├── Systematic Review: Data extraction
│   └── Mini Interface: MVP testing
│
├── Week 2-4 (Dec 8-31)
│   ├── Systematic Review: Analysis begins
│   └── Mini Interface: Feature additions

JANUARY 2026
└── Week 1 (Jan 1-5)
    ├── DUE: Systematic Review ✅
    └── DUE: Mini Interface ✅
```

---

## 🛠️ TECH STACK PER PROJECT

| Project | Research | Writing | Creation | Automation |
|---------|----------|---------|----------|------------|
| **Osteoporosis** | Consensus, Elicit, Covidence | Claude, Grammarly | Gamma, Canva | n8n → Notion |
| **Hypothyroidism** | Perplexity, Consensus | ChatGPT, Claude | Gamma, SlideSpeak | n8n alerts |
| **GRADE** | Scite, Consensus | Claude | Gamma, Miro | Template gen |
| **Systematic Review** | Covidence, Zotero | Claude, NotebookLM | Orange, Canva | Citation sync |
| **Mini Interface** | - | - | Cursor, Claude | - |
| **EBM Program** | Notion | Claude, ChatGPT | Gamma, Miro | Content gen |

---

## 🤖 AUTOMATION OPPORTUNITIES

### Priority 1 (Build Now):
1. **Literature Alerts → Notion**
   - PubMed/Embase alerts → n8n → Notion database
   - Daily digest of new papers

2. **Citation Manager Sync**
   - Zotero → n8n → Notion
   - Automated reference formatting

3. **Class Content Pipeline**
   - Research notes → AI summary → Slide generation
   - Feedly → Notion → Gamma

### Priority 2 (Build After):
4. **Assessment Tracking**
   - Student progress → Notion → Dashboard
   - Auto-generated reports

5. **Content Scheduler**
   - Curriculum calendar → Notion
   - Automated reminders

---

## 📊 SUCCESS METRICS

### Academic Deliverables:
- ✅ 3 teaching presentations completed (by Nov 25)
- ✅ 1 systematic review in progress (protocol by Nov 18)
- ✅ 1 EBM curriculum document (by Dec 5)
- ✅ 1 functional data collection tool (by Jan 5)

### Automation Metrics:
- 📈 50% reduction in manual literature screening
- 📈 80% faster slide creation (vs manual)
- 📈 100% automated citation management
- 📈 Daily automated research updates

### Learning Metrics:
- 📚 Proficiency in systematic review methodology
- 📚 Comfortable with n8n automation
- 📚 Basic coding skills (via Cursor + AI)
- 📚 GRADE system expert

---

## 🚨 CRITICAL PATH

**Must Complete First (Dependencies):**

1. **Week 1-2: Research Infrastructure**
   - Set up Covidence
   - Organize Zotero libraries
   - Create Notion databases
   - Build n8n literature alert workflow

2. **Week 2-3: Content Creation**
   - Complete all 3 class reviews
   - Create teaching materials
   - Deliver classes

3. **Week 3-4: EBM Curriculum**
   - Draft program outline
   - Finalize Year 1 content
   - Get stakeholder approval

4. **Month 2: Parallel Development**
   - Systematic review (continuous)
   - Mini interface (MVP → full)

---

## 💡 TIPS FOR SUCCESS

### Time Management:
- 🎯 **Block time daily:** 2h morning (research), 2h afternoon (creation)
- 🎯 **Batch similar tasks:** All literature searches same day
- 🎯 **Use AI maximally:** Don't write from scratch, edit AI output
- 🎯 **Automate repetitive:** Set up workflows once, reuse forever

### AI Leverage:
- 💪 **Claude:** Deep analysis, writing, curriculum design
- 💪 **ChatGPT:** Quick summaries, case studies, creative
- 💪 **Cursor:** All coding, tool development
- 💪 **NotebookLM:** Document synthesis, podcast summaries
- 💪 **Gamma:** Instant slide decks from outlines

### Don't Get Stuck:
- ⚡ **Perfect is enemy of done** - Ship MVPs
- ⚡ **Use templates** - Don't reinvent wheels
- ⚡ **Ask AI first** - Before Googling or struggling
- ⚡ **Time-box tasks** - 2 hours max per subtask

---

## 📞 SUPPORT RESOURCES

### Communities:
- **r/EvidenceBasedMedicine** - EBM discussions
- **Cochrane Training** - Systematic review help
- **n8n Community** - Automation support
- **Cursor Discord** - Coding help

### Key References:
- **Cochrane Handbook** - Systematic reviews
- **GRADE Guidelines** - Evidence assessment
- **PRISMA Statement** - Review reporting
- **Users' Guides to Medical Literature** - EBM fundamentals

---

## 🎯 QUARTERLY GOALS

**Q4 2025 (Oct-Dec):**
- ✅ Complete 3 teaching classes
- ✅ EBM curriculum finalized
- 🔄 Systematic review in progress
- 🔄 Mini interface MVP

**Q1 2026 (Jan-Mar):**
- ✅ Systematic review completed
- ✅ Mini interface launched
- 🎯 Teach first EBM curriculum session
- 🎯 Publish systematic review

---

## 📝 NOTES

**Key Principles:**
1. **Automation First** - Build once, use forever
2. **AI Everywhere** - Never work without AI assistance
3. **Iterate Fast** - MVP → feedback → improve
4. **Document Everything** - Future-you will thank you

**Remember:**
- You have 21+ premium tools - USE THEM ALL
- Cursor + Claude = unstoppable coding duo
- n8n = your automation backbone
- Don't spend 6 hours on email sync! 😅

---

**Last Updated:** November 5, 2025  
**Next Review:** November 12, 2025  
**Status:** 🟢 On Track

---

*This is a living document. Update weekly with progress and learnings.*
