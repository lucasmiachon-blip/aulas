# Docs Audit — 2026-03-17

> Executado via skill `.cursor/skills/docs-audit/`. Batches 1–2 completos. Critérios: reference.md.

---

## Resumo por Domínio

| Domain | Status | Items |
|--------|--------|-------|
| Links | WARN | 1 link 404 (metanalise HANDOFF); grade/osteo sem links no README |
| Redundancy | PASS | Single source respeitado; overlap ECOSYSTEM↔KPIs em backlog |
| Verbosity | PASS | Tabelas para comparação; referência > duplicata |
| Tokens | WARN | 3 docs >200 linhas sem index; datas fixas em XREF/ECOSYSTEM |
| Structure | PASS | h1→h2→h3; listas para itens discretos |

---

## Batch 1: docs/README.md, RULES.md, SKILLS.md, SUBAGENTS.md, XREF.md

### Links
- **FAIL:** `docs/README.md` → `[aulas/metanalise/HANDOFF.md](../aulas/metanalise/HANDOFF.md)` — **arquivo não existe**. Metanalise tem apenas `CLAUDE.md`, `index.stage-*.html`.
- **WARN:** `docs/README.md` linhas 29–30: `aulas/grade/HANDOFF.md` e `aulas/osteoporose/HANDOFF.md` listados como texto, sem links (arquivos existem).
- **PASS:** Demais links internos verificados (SETUP, RULES, SKILLS, SUBAGENTS, XREF, ECOSYSTEM, KPIs, blueprint, biblia, prompts, archive, etc.).
- **PASS:** `biblia-narrativa.md` → `../aulas/cirrose/references/evidence-db.md` — path correto.
- **PASS:** `archive/AUDIT-BATCHES.md` → `../../tasks/todo.md` — existe.

### Redundancy
- **PASS:** docs-audit espelhado (.cursor + .claude) documentado em SKILLS.md.
- **PASS:** XREF.md canônico para dependências; RULES/SKILLS/SUBAGENTS referenciam-se sem duplicar.
- **PASS:** Context Window: regra em core-constraints.mdc; SUBAGENTS.md § Context Window como referência.

### Verbosity
- **PASS:** Tabelas usadas para comparação (RULES regras, SKILLS skills, XREF mapa).
- **PASS:** Prosa concisa; referências em vez de duplicata.

### Tokens
- **WARN:** `XREF.md` ~170 linhas — borderline; "Gerado: 2026-03-07" e "Última revisão: 2026-03-16" — dados sensíveis ao tempo.
- **PASS:** README, RULES, SKILLS, SUBAGENTS <200 linhas.

### Structure
- **PASS:** README: h1 (Docs) → h2 (Por propósito, HANDOFFs, MD Auditoria) → h3 (Onboarding, Boas práticas, etc.).
- **PASS:** Listas para itens discretos; tabelas alinhadas.

---

## Batch 2: SETUP.md, ECOSYSTEM.md, KPIs.md, HANDOFFs, MCP-*

### Links
- **PASS:** SETUP.md — sem links internos quebrados.
- **PASS:** ECOSYSTEM.md → SKILLS.md, RULES.md — existem.
- **PASS:** KPIs.md → arena.ai (externo).
- **PASS:** HANDOFF cirrose — referências internas corretas.
- **PASS:** MCP-ENV-VARS, MCP-ACADEMICOS — links externos (notion, ncbi, etc.).

### Redundancy
- **WARN:** HANDOFF cirrose (12/mar): "ECOSYSTEM.md routing overlap com KPIs.md" — backlog LOW, não corrigido.
- **PASS:** SYNC-NOTION-REPO canônico para IDs; .env.example referenciado.
- **PASS:** metanalise-scope, blueprint-cirrose — escopos distintos.

### Verbosity
- **PASS:** ECOSYSTEM, KPIs — tabelas para benchmarks e roteamento.
- **PASS:** SETUP — seções claras; sem filler.

### Tokens
- **WARN:** `ECOSYSTEM.md` ~131 linhas — OK.
- **WARN:** `KPIs.md` ~134 linhas — OK.
- **WARN:** `aulas/cirrose/HANDOFF.md` ~185 linhas — OK.
- **WARN:** Datas fixas em ECOSYSTEM ("Última atualização: 2026-03-16", "Gemini 3 Pro encerrado 9 mar 2026") — aceitável para benchmarks.

### Structure
- **PASS:** SETUP: h1 → h2 (1, 1b, 2, 3, 4, 5).
- **PASS:** ECOSYSTEM, KPIs — hierarquia correta.

---

## Batch 3 (amostra): MCP-*, SYNC-NOTION-REPO, blueprint, metanalise-scope

### Links
- **PASS:** blueprint-cirrose → HANDOFF.md, biblia-narrativa.md.
- **PASS:** metanalise-scope — sem links internos.
- **PASS:** SYNC-NOTION-REPO → .env.example.

### Redundancy
- **PASS:** blueprint vs biblia — blueprint = mapa; biblia = detalhe narrativo.
- **PASS:** metanalise-scope vs blueprint metanalise — escopo vs implementação.

### Tokens
- **WARN:** `blueprint-cirrose.md` ~178 linhas — borderline.
- **WARN:** `biblia-narrativa.md` ~340 linhas — **>200**. Considerar index ou reference.md para seções longas.
- **WARN:** `slide-pedagogy.md` ~302 linhas — **>200**. Já tem índice interno; OK.

### Structure
- **PASS:** blueprint — h1→h2→h3; tabelas para interações e cortes.
- **PASS:** metanalise-scope — seções objetivas.

---

## Batch 4 (amostra): prompts/, archive/

### Links
- **PASS:** prompts/* — referenciados no README.
- **PASS:** archive/README.md — lista arquivos; sem links quebrados.
- **PASS:** archive/AUDIT-BATCHES → tasks/todo.md.

### Tokens
- **WARN:** `archive/research-skills-ecosystem-2026-03-11.md` 550+ linhas — arquivado; referência, não operacional. OK manter.
- **PASS:** prompts curtos (<50 linhas).

### Structure
- **PASS:** archive/README — tabela Arquivo | Motivo.

---

## Recommended Actions

1. **Corrigir link 404:** `docs/README.md` — remover ou condicionar link para `aulas/metanalise/HANDOFF.md`. Opções:
   - Criar `aulas/metanalise/HANDOFF.md` stub (se projeto ativo).
   - Ou trocar por `aulas/metanalise/CLAUDE.md` e marcar "HANDOFF pendente".
   - Ou remover linha até HANDOFF existir.

2. **Adicionar links no README:** Linhas 29–30 — converter `aulas/grade/HANDOFF.md` e `aulas/osteoporose/HANDOFF.md` em links `[texto](../aulas/grade/HANDOFF.md)`.

3. **Atualizar XREF.md:** Seção `aulas/metanalise/` — HANDOFF.md listado como existente. Ajustar para refletir que não existe (ou marcar "pendente").

4. **Token economy (opcional):** `biblia-narrativa.md` >200 linhas — já tem índice interno. Considerar extrair "Números Práticos" para `biblia-numeros-reference.md` se carregado frequentemente.

5. **Datas em XREF:** "Gerado/Última revisão" — avaliar generalizar ("Revisar ao criar/mover docs") ou manter para rastreabilidade.

6. **Backlog LOW (HANDOFF):** ECOSYSTEM↔KPIs overlap — registrar em tasks/lessons.md ou criar issue para consolidar roteamento.

---

## Arquivos Auditados (por batch)

| Batch | Arquivos |
|-------|----------|
| 1 | README.md, RULES.md, SKILLS.md, SUBAGENTS.md, XREF.md |
| 2 | SETUP.md, ECOSYSTEM.md, KPIs.md, HANDOFF (cirrose), MCP-ENV-VARS.md, MCP-ACADEMICOS.md, SYNC-NOTION-REPO.md |
| 3 | blueprint-cirrose.md, metanalise-scope.md, biblia-narrativa.md, slide-pedagogy.md |
| 4 | prompts/weekly-updates.md, archive/README.md, archive/AUDIT-BATCHES.md |

---

*Relatório gerado conforme .cursor/skills/docs-audit/SKILL.md + reference.md.*
