---
name: sync-evidence
description: |
  Persiste achados do medical-researcher em evidence-db.md e opcionalmente no Notion References DB. Ponte entre pesquisa e persistencia. Rodar APOS /medical-researcher quando quiser salvar os achados. Ativar com "sincronizar evidencias", "sync evidence", "salvar pesquisa", "persistir no notion", "gravar evidencias".
version: 1.0.0
context: fork
agent: general-purpose
allowed-tools: Read, Write, Grep, Glob, Agent
argument-hint: "[aula=auto-detect] [--notion]"
---

# Sync Evidence — Pesquisa → Persistencia

Persiste achados de pesquisa: `$ARGUMENTS`

## Quando usar

APOS uma rodada de `/medical-researcher` ou `@medical-researcher` quando o usuario quiser:
1. Salvar achados no `evidence-db.md` local (sempre)
2. Sincronizar com Notion References DB (opcional, flag `--notion`)

NAO e um pesquisador — e uma ponte. Se nao houver pesquisa recente, avisar e sugerir rodar `/medical-researcher` primeiro.

## Step 0 — Localizar achados

1. Detectar aula: `git branch --show-current` → `feat/{aula}-*` ou pedir
2. Checar `.claude/agent-memory/medical-researcher/` por arquivos recentes (memory do agent)
3. Se nao encontrar memory → pedir ao usuario que cole o report ou rode `/medical-researcher` primeiro
4. Ler `aulas/{aula}/references/evidence-db.md` (estado atual)

## Step 1 — Apresentar para aprovacao

Mostrar ao usuario:

```
## Achados prontos para persistir

### Novos (nao existem em evidence-db.md)
1. [PMID] — [titulo abreviado] — [effect size]
2. ...

### Atualizacoes (ja existem, dados mais recentes)
1. [PMID] — campo X: [antigo] → [novo]
2. ...

### Conflitos (dados divergem do evidence-db atual)
1. [PMID] — evidence-db diz X, pesquisa encontrou Y

Aprovar quais? (all / numeros / none)
```

NUNCA gravar sem aprovacao explicita do usuario.

## Step 2 — Escrever em evidence-db.md

Para cada entrada aprovada, append/update em `aulas/{aula}/references/evidence-db.md`:

```markdown
## [slide-id]

### [Trial/Guideline Name] ([Year])
- **Citation:** [AMA format]
- **PMID:** [verificado] | **DOI:** [verificado]
- **Design:** [tipo] | **n:** [X]
- **Population:** [descricao]
- **Primary endpoint:** [descricao]
- **Result:** [effect size] (95% CI: [a]-[b])
- **NNT:** [X] (CI: [a]-[b]) em [tempo]
- **GRADE:** [certeza]
- **Verified:** [YYYY-MM-DD]
- **Source:** medical-researcher session [date]
```

Se slide-id nao fornecido → usar header `## Unassigned` (usuario associa depois).

## Step 3 — Notion sync (opcional, flag --notion)

So executar se usuario pediu explicitamente (flag `--notion` ou "salvar no notion").

1. Verificar restricao: reference-manager tem STOP gate para aulas fora de Cirrose
   - Se aula != cirrose → avisar: "Notion References DB nao tem filtro por aula. Sync bloqueado para {aula}. Ver docs/SYNC-NOTION-REPO.md"
   - Se aula == cirrose → prosseguir
2. Delegar ao agent `reference-manager` via Agent tool:
   - Input: lista de PMIDs/DOIs aprovados no Step 1
   - reference-manager valida via MCP, formata AMA, cria entries no Notion
3. Reportar resultado: N entries criadas, N atualizadas, N falhas

## Step 4 — Confirmar

```
## Sync concluido

- evidence-db.md: [N] entries adicionadas, [M] atualizadas
- Notion: [synced/skipped/blocked] ([motivo])
- Proximos passos: [sugestoes]
```

## Regras

- NUNCA gravar sem aprovacao — usuario escolhe quais entries salvar
- NUNCA modificar dados clinicos — copiar exatamente como vieram da pesquisa
- Se PMID nao verificado (status CANDIDATE) → marcar como `[CANDIDATE]` no evidence-db
- evidence-db.md e append-only para novos. Update permitido para campos que mudaram.
- Notion sync so para Cirrose (STOP gate do reference-manager). Outras aulas = evidence-db local only.
- Hook guard-evidence-db.sh protege evidence-db — edits devem passar pela validacao
