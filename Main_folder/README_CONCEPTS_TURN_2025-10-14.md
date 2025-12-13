# Concepts for this turn — Paragraph style

Date: 2025-10-14

Purpose: consolidate today’s requested concepts as short paragraphs of four to five sentences each, with one “learn more” link per concept. Style is minimalist and factual. No bullets. You control pacing later with “go”, “go [theme]”, and “explain better [theme]”.
## Biostatistics — Nonresponse bias and weighting adjustments

Nonresponse occurs when some sampled units fail to provide data, and bias appears when the probability of responding correlates with key outcomes. Analysts mitigate this by constructing response‑propensity or calibration weights using auxiliary variables like age, sex, or geography that are known for respondents and nonrespondents. Methods include raking (iterative proportional fitting), logistic response models, and post‑stratification; each relies on the assumption that, conditional on auxiliaries, nonresponders would resemble responders. Adjustments cannot recreate missing subpopulations with zero response, so sensitivity analysis and transparent nonresponse reporting remain essential. Learn more: https://www.aapor.org/


## Mathematics — Cardinality: countable vs uncountable

A set is countable if its elements can be placed in a one‑to‑one correspondence with the natural numbers, which includes the integers and even the rationals via clever listing tricks. Cantor’s diagonal argument proves that the real numbers are uncountable, meaning no sequence can list them all, so there are strictly more reals than rationals. This distinction underlies modern measure theory, probability, and analysis, where uncountable sets require limiting processes and sigma‑algebras. Thinking in terms of injections and bijections clarifies what it means for infinities to have different sizes. Learn more: https://richardhammack.github.io/BookOfProof/


## Philosophy — Theory‑ladenness of observation

Observations depend on concepts, instruments, and background assumptions, so data are never entirely theory‑free. When predictions fail, underdetermination means one can often adjust auxiliary assumptions instead of abandoning a core claim, which motivates safeguards. Preregistration, severe tests, and independent replications limit ad‑hoc immunizations and strengthen inference. Treat measurements as model‑based summaries and document assumptions that link signals to constructs. Learn more: https://plato.stanford.edu/


## Cognitive biases — Anchoring debiasing protocols

Anchoring occurs when an initial number pulls subsequent estimates, even when the anchor is irrelevant. Countermeasures include consider‑the‑opposite prompts, explicit generation of reasons the anchor should be ignored, and structured range estimates. Checklists that force an anchor challenge improve decisions in clinics, research planning, and forecasting. Teams should rehearse the protocol, record anchors encountered, and audit calibration over time. Learn more: https://www.ncbi.nlm.nih.gov/pmc/


## Evidence‑Based Medicine — Critical appraisal checklists

Appraisal checklists focus attention on internal validity (randomization, concealment, blinding, attrition), effect size and precision, and applicability to a local setting. They operationalize appraisal for randomized, cohort, case‑control, and diagnostic accuracy studies so notes remain transparent and consistent. Good practice pairs a filled checklist with a short narrative explaining the decision on trust and transportability. Using shared forms builds team memory and speeds future reviews on related questions. Learn more: https://www.cebm.ox.ac.uk/


## Decision theory — Value of Information (EVPI, EVPPI, EVSI)

Value of Information quantifies how much it is worth to reduce uncertainty before acting, turning research questions into economic choices. EVPI sets the upper bound by comparing the expected value with perfect information against current information. EVPPI targets the contribution of uncertainty in specific parameters, while EVSI estimates the value of a feasible study with a proposed sample size. VOI helps prioritize data collection and design trials where learning is expected to change the decision. Learn more: https://www.ispor.org/


## Adult education — Retrieval practice design

Testing is a learning event: low‑stakes quizzes, delayed recall, and spaced feedback strengthen retention and transfer. Interleave topics and vary contexts so retrieval becomes flexible, but keep task loads small to control cognitive strain. Explain that fluency illusions make rereading feel fast yet produce weak learning compared with retrieval. Close sessions with two or three targeted prompts and brief explanations keyed to upcoming use. Learn more: https://www.ncbi.nlm.nih.gov/pmc/


## Evaluation methods — Standard setting (Angoff and Hofstee)

Criterion‑referenced standard setting defines a performance cut as the minimum acceptable competence rather than a percentile of the cohort. In Angoff, trained judges estimate the probability that a minimally competent candidate answers each item correctly and those probabilities aggregate to a cut score. Hofstee blends acceptable failure rates with acceptable score ranges to produce a compromise cut anchored by policy constraints. Both methods require documentation of uncertainty and periodic review as items or cohorts change. Learn more: https://www.aomrc.org.uk/


## Class design — Backward design (Understanding by Design)

Backward design begins with the evidence of learning you want to see, then works backward to activities that produce that evidence. This ensures constructive alignment so time is spent on what will be assessed, not on attractive but off‑target topics. Outcomes should be observable and tied to specific artifacts, performances, or decisions. Rubrics and exemplars make expectations visible and speed feedback. Learn more: https://www.kent.edu/ctl/backward-design


## Programming — Data‑structure costs and Big‑O choices

Lists excel at ordered sequences with amortized O(1) append but have O(n) membership tests; linked lists differ in locality and insertion costs. Dictionaries (hash maps) provide average O(1) key lookup and update, while sets give O(1) membership and convenient algebra on keys. Choose structures to match operations; the wrong choice can dominate runtime more than constant‑factor optimizations. Measure with simple timings and profile before rewriting algorithms. Learn more: https://wiki.python.org/moin/TimeComplexity


## Machine learning — Nested cross‑validation to avoid leakage

Nested CV uses an outer loop for unbiased performance estimation and an inner loop for model selection and hyperparameter tuning. All preprocessing, feature selection, and scaling must be fit inside each training fold and applied only to its validation fold. Pipelines enforce this discipline and prevent information bleeding that inflates performance estimates. Report the outer‑loop score distribution and compare to a simple baseline to judge practical gain. Learn more: https://scikit-learn.org/stable/modules/cross_validation.html


## AI learning — Inter‑rater agreement for AI feedback (Cohen’s κ)

When multiple human or AI raters grade work, measure agreement beyond chance using Cohen’s kappa for nominal scales or weighted kappa for ordered categories. Before deployment, calibrate rubrics, hold a pilot rating session, and set κ thresholds that must be met. Low κ signals ambiguous criteria or rater drift and should trigger rubric revision and retraining. Agreement metrics complement accuracy by monitoring consistency across graders. Learn more: https://online.stat.psu.edu/stat509/lesson/1/1.3


## AI tools — Idempotency keys and exponential backoff

APIs should accept idempotency keys so clients can safely retry POST requests without duplicating work or creating inconsistent states. Clients implement exponential backoff with jitter to reduce thundering herd effects and congestion collapse under partial outages. Store responses keyed by the idempotency token to short‑circuit subsequent retries and support audit. Design retry budgets and error classification so only safe operations are retried automatically. Learn more: https://docs.stripe.com/idempotency


## Education theory — Dual‑coding theory (Paivio)

Learning improves when verbal and visual channels carry coordinated, relevant information that the learner can integrate. Pair concise text with meaningful diagrams; decorative images raise load and should be avoided. Narration plus graphics often beats dense on‑screen text plus graphics by reducing split attention. Test recall and transfer to ensure visuals are aiding comprehension rather than merely attracting attention. Learn more: https://en.wikipedia.org/wiki/Dual-coding_theory


## Computing theory — Reductions to SAT and NP‑completeness

To prove a problem is NP‑complete, show membership in NP and construct a polynomial‑time reduction from a known NP‑complete problem such as 3‑SAT. Reductions build gadgets that preserve yes/no answers, explaining why diverse problems share difficulty. This perspective guides practice: if your problem encodes SAT, exact algorithms will scale poorly in the worst case. Approximation, heuristics, or exploiting structure may be the only practical path for large instances. Learn more: https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/


## Logic theory — Soundness and completeness (first‑order logic)

Soundness states that anything provable in your calculus is semantically valid in all models, ensuring no false theorems arise from the rules of proof. Completeness states that every semantically valid statement is provable, tying truth in all models to derivability. Together they connect syntax and semantics and justify automated proof search methods in first‑order logic. Know the limits: stronger logics trade one or both properties for expressivity, and arithmetic adds incompleteness phenomena. Learn more: https://plato.stanford.edu/entries/logic-firstorder/


## Automation — Gmail → Notion via n8n

Label emails Action or Evidence at capture and route them to Notion Tasks or Evidence so triage becomes data. Store SourceAccount and Message‑ID to preserve provenance and enable idempotent upserts. Add a Drive ‘Teaching Drop’ watcher that creates tasks with file links and measure throughput. Keep logs and retry policies so runs are auditable and recover gracefully from errors. Learn more: https://docs.n8n.io/


## Daily flow

Start with Gmail triage, capture three items, process one PDF to notes, draft one slide, commit changes, and run automations. Treat this loop as a minimum viable cycle that keeps assets moving forward every day. Keep SOP pages current so future you can reproduce steps without friction. Review the loop weekly and cut steps that do not move outcomes. Learn more: https://www.notion.so/help/guides/manage-tasks-in-notion


## LLM systems

Build with modular prompts and explicit evaluation so changes are measurable and reversible. Add tools or memory only when required; complexity increases failure modes and audit cost. Cross‑check with a second model on high‑stakes outputs and log divergences for review. Version prompts, datasets, and scores so you can reproduce improvements and roll back when needed. Learn more: https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/


## APIs and Postman

Understand endpoints, headers, auth flows, and JSON schemas before chaining requests. Create a small collection with variables and tests that can run end‑to‑end without manual steps. Store secrets in environments, keep them out of version control, and document reproduction steps. Add a CI check that runs smoke tests after changes to detect breaking edits early. Learn more: https://learning.postman.com/docs/getting-started/introduction/


## Research capture — Zotero + BBT + scite

Capture sources with stable citekeys and descriptive tags so retrieval and citation stay reliable. Use Smart Citations to see whether later work supports or contradicts a claim and adjust summaries accordingly. Keep a constrained to‑read list and schedule short passes to convert reading into notes and actions. Export highlights and links to Notion Evidence to connect research with teaching and automation. Learn more: https://www.zotero.org/support/quick_start_guide


## Git and GitHub

Initialize a repository, make small atomic commits with clear messages, and push to a remote for backup and collaboration. Use branches and pull requests to isolate changes and invite review, which finds defects early. Tag weekly releases so teaching assets and SOPs are snapshot‑ready for reuse. Protect tokens, enable two‑factor authentication, and audit access periodically. Learn more: https://skills.github.com/


## Notion SOPs and databases

Define properties for Tasks, Projects, and Evidence so items can be filtered, sorted, and automated reliably. Store provenance fields like SourceAccount and Message‑ID so pipelines can deduplicate and audit items. Create focused views for today and this week so priorities remain visible. Build dashboards that track throughput, blockers, and review cadence to drive improvement. Learn more: https://www.notion.so/help/intro-to-databases


## Orange Data Mining

Load a CSV, inspect distributions, and visualize relationships before training models in Orange’s canvas. Start with default learners to set a baseline, then compare alternatives using cross‑validation widgets. Reserve a holdout sample to check generalization and avoid optimistic estimates. Export a concise report and place it in your Evidence hub to support decisions. Learn more: https://orangedatamining.com/getting-started/


## Security

Enable two‑factor authentication across services and store backup codes securely to reduce account‑takeover risk. Grant least‑privilege scopes to apps and rotate keys; remove stale access quarterly. Avoid sending protected health information to third‑party AI tools unless contracts explicitly allow it. Prefer dry‑runs and explicit confirmations in automation to prevent unintended changes. Learn more: https://myaccount.google.com/signinoptions/two-step-verification


## Roles by tool

Assign roles by strength: ChatGPT for reasoning and planning, Gemini for Gmail and Drive triage, Claude for long‑context second opinions. Record outcomes and deltas in a Notion dashboard so tool choices follow evidence rather than habit. Switch tools only when measurable improvements in speed, accuracy, or effort are observed. Document the map so collaborators can follow the same routes. Learn more: https://www.notion.so/


## Up‑to‑date AI/API routine

Skim two newsletters daily and star one item to test so attention becomes action. Check OpenAI, Anthropic, and Google changelogs twice per week to detect breaking changes early. Read one Latent Space summary and watch one short demo weekly to refresh mental models. Create one micro‑test with a due date in Tasks so learning compounds through small experiments. Learn more: https://www.latent.space/
