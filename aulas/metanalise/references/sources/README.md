# Sources — Full-text Articles

Full-text PDFs for visual cropping (forest plots, GRADE tables, figures).

**Not tracked by git** — PDFs are gitignored. This README is the only tracked file.

## Naming convention

```
PMID-firstauthor-year-keyword.pdf
```

Examples:
- `40902613-valgimigli-2025-clopidogrel.pdf`
- `41065416-musini-2025-antihtn.pdf`
- `33782057-page-2021-prisma.pdf`

## Currently needed

| PMID | Author | Year | Purpose |
|------|--------|------|---------|
| 40902613 | Valgimigli | 2025 | Anchor article — forest plot, subgroup analysis |
| 41065416 | Musini | 2025 | Visual example — forest plot, GRADE SoF table |

## Usage

Agent crops relevant figures for slides via Playwright or manual screenshot.
Crops go to `aulas/metanalise/assets/` (tracked).
