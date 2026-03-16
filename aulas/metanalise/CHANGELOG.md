# CHANGELOG — Meta-analise

> Historico de batches. Append-only (novos no topo). Estado → HANDOFF.md

---

## 2026-03-16j — QA full-deck + housekeeping

Branch: `feat/metanalise-mvp`

### Mudancas

- **Hook (01):** 80/dia → 146/dia (Hoffmann 2021, dado atualizado de 2019→2021). countUp target, label, notes atualizados
- **CP1 (03):** Musini PMID atualizado nas notes (pendente → 41065416 verificado)
- **Evidence-db v4.2:** autores corrigidos — G3 Yin→Greenwood H (PMID 38588546), G5 Bosco→El-Taji O (PMID 38842801). Todos 5 PMIDs verificados via PubMed
- **Reading-list:** item 4 atualizado — Musini→Valgimigli 2025 (PMID 40902613). Lacuna de acesso atualizada
- **CSS:** `.checkpoint-teaser` removido (dead selector — nenhum HTML o referenciava)
- **CLAUDE.md aula:** merge ref corrigido 6889ff7→733eb2e
- **CHANGELOG.md:** criado (referenciado por ERROR-LOG/HANDOFF mas nunca existiu)

### QA slide-a-slide (18/18)

| Status | Slides |
|--------|--------|
| PASS | 00, 01, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| Pendente decisao | 02 (contrato) — titulo + word count |

### Repo janitor

- 0 orphan HTML, 0 orphan MDs, 0 broken links, 0 temp files
- 1 dead CSS class removida (.checkpoint-teaser)
- QA screenshots: 5 dirs stale (manter post-fix-scan/ como current)

---

## 2026-03-16i — Notion sync completo

Branch: `feat/metanalise-mvp`

- 18/18 slides sincronizados com Notion Slides DB
- 25 refs adicionadas ao Notion References DB
- ALLOW_AB_ON_WT=1 usado para este CHANGELOG

---

## 2026-03-16h — Hook layout centering

Branch: `feat/metanalise-mvp`

- `.hook-data` flex container + `.hook-data-item { flex: 1 }` = 3 colunas iguais
- `.hook-verdict` margin-top 80px
- Revertido override `.stage-c .slide-navy` erroneo

---

## 2026-03-16 — CSS layout fixes (ERRO-005/006/008)

Branch: `feat/metanalise-mvp`

- ERRO-005: base.css pseudo-elements → override `justify-content: center` + `::before/::after { display: none }`
- ERRO-006: checkpoint centering safe pattern
- ERRO-008: CSS zoom REMOVIDO — deck.js scale() e o mecanismo correto

---

## 2026-03-15g — _manifest.js + QA batch 1

Branch: `feat/metanalise-mvp`

- `_manifest.js` criado: 18 slides, fases F1/I1/F2/I2/F3
- QA visual batch 1 (slides 00-02): PASS
- 8 classes CSS orfas removidas
- `references/sources/` criado com .gitignore

---

## 2026-03-15e — Fase 3 completa (slides 13-15)

Branch: `feat/metanalise-mvp`

- 13-ancora.html: anchor-card + metric-grid (Valgimigli 2025)
- 14-aplicacao.html: beneficio vs dano (MACCE HR 0,86 vs sangramento NS)
- 15-aplicabilidade.html: PICO callback com dados Valgimigli

---

## 2026-03-15 — Notion sync + slides independentes

Branch: `feat/metanalise-mvp`

- 12-checkpoint-2.html: "falso positivo" do diamante
- 16-absoluto.html: RR→NNT conversion
- 17-takehome.html: 3 perguntas reformuladas
- narrative.md v2, blueprint.md v1.4

---

## 2026-03-13 — Deck completo (18 slides)

Branch: `feat/metanalise-mvp`

- 12 slides Fase 2 criados (04-rs-vs-ma ate 10-fixed-random)
- 01-hook.html reescrito: 2-beat state machine, 3 countUp
- 02-contrato.html: 3 cards framework
- 03-checkpoint-1.html: cenario MA ilustrativo
- h2 rewrite: 9 headlines → assertions tecnicas
- evidence-db.md v2: 12 refs tier 1
