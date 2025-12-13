# Lucas Miachon — Start Here

**Last updated:** November 05, 2025

This repo bundles (1) your *project plans*, (2) your *tech stack*, and (3) a small app you’ll build: **Mini‑REDCap** (a simple data‑entry interface). This page is the one‑pager that orients you and anyone helping you.

---

## What’s inside

- **/docs/ROADMAP.md** — detailed project roadmap (now → Q1 2026)
- **/docs/TECH-STACK.md** — your current tools and how you use them
- **/apps/mini-redcap/** — the “fancy interface” for forms + data table

> TL;DR focus (next 20 days): ship three teaching classes (osteoporosis, hypothyroidism, GRADE), and keep the Mini‑REDCap moving to MVP.

---

## Quick start for you (daily)

- 90 mins research → 90 mins slides (per class)
- 45 mins Mini‑REDCap (MVP features only)
- 15 mins update ROADMAP checkboxes

---

## Working rules

- **Automation first.** If it repeats, template or automate.
- **MVP mindset.** Done > perfect. Ship small, iterate.
- **Data safety.** No PHI/PII in test data. Treat Mini‑REDCap as a teaching tool, not a clinical system.

---

## How to run the Mini‑REDCap (when code exists)

- Option A (no backend): open `/apps/mini-redcap/index.html` in a browser. Data goes to Google Sheets via a tiny script.
- Option B (Node + SQLite): `npm i`, then `npm run dev`. Data persisted locally for demos.

---

## Contact & license

- Owner: **Lucas Miachon**
- License: MIT (doc + sample code)
