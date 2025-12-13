# Clinical Consult Automation — Low-typing, pt-BR

Goal: minimal typing. Intake → audio (pt-BR) → transcript → auto-SOAP (JSON+Markdown) → humanized lifestyle message. Orchestrator: n8n.

Blueprint
1) Pre-visit: intake form → JSON
2) During: record audio → Whisper (pt-BR) → LLM → SOAP JSON + Markdown
3) Post-visit: pt-BR summary; store in Notion; queue tasks

Tools
- Speech-to-text: Whisper large-v3 / Faster-Whisper (local)
- LLMs: ChatGPT (core), Claude (long-context + humanized text)
- Forms: Typeform / SurveyJS; or SMART-on-FHIR
- Knowledge: Isabel Pro
- Orchestrator: n8n
- Storage: Notion DB; OneDrive files
- Messaging: Gmail API; Twilio WhatsApp/SMS (no PHI)

n8n workflows
A) Intake→Notion (Typeform webhook → Notion upsert)
B) Audio→SOAP (OneDrive trigger → Whisper → ChatGPT JSON Output → Notion + DOCX)
C) Patient message (Notion status trigger → Claude → Gmail/Twilio)

Schemas
Intake: {"patient_id":"","chief_complaint":"","onset":"","duration":"","modifiers":[],"red_flags":[],"meds":[],"allergies":[],"pmh":[]}
SOAP: {"subjective":"","objective":{"vitals":{"bp":"","hr":"","temp":"","spo2":""},"exam_key_points":[]},"assessment":{"problems":[{"label":"dx","icd10":"code","likelihood":0.0,"why":""}]},"plan":{"orders":[],"education_points_ptBR":[],"follow_up":""}}

Prompts
- SOAP (ChatGPT): “Extract a SOAP note in JSON per schema; concise; pt-BR; return JSON + Markdown.”
- Questionnaire chooser: “Top 3 validated questionnaires for CC/age/sex with links + time.”
- Patient message (Claude): “Warm pt-BR summary 120–180 words; 2 habits; disclaimer.”

Compliance: no PHI to third-party AIs unless compliant. Prefer local Whisper.
