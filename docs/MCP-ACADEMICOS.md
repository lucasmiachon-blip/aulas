# MCPs Academicos — Aulas Magnas

> Inventario completo de MCPs para pesquisa academica/clinica.
> Config local: `.mcp.json` (perfil ativo). Profiles: `.mcp-profiles/*.json`.
> Ultima revisao: 2026-03-17.

---

## MCPs Locais (self-hosted)

### Busca e Metadados

| MCP | Pacote | Runtime | Custo | Variavel .env |
|-----|--------|---------|-------|---------------|
| **pubmed** | `@cyanheads/pubmed-mcp-server` | npx | Gratis (key opcional — 10 req/s vs 3) | `NCBI_API_KEY` |
| **pubmed-simple** | `mcp-simple-pubmed` | uvx | Gratis | `PUBMED_EMAIL`, `NCBI_API_KEY` |
| **crossref** | `@botanicastudios/crossref-mcp` | npx | Gratis | — |
| **semantic-scholar** | `@jucikuo666/semanticscholar-mcp-server` | npx | Gratis (key opcional — limits maiores) | `SEMANTIC_SCHOLAR_API_KEY` |
| **arxiv** | `arxiv-paper-mcp-server` | uvx | Gratis | — |
| **google-scholar** | `@JackKuo666/google-scholar-mcp-server` | npx | Gratis (experimental) | — |
| **clinicaltrials** | `clinicaltrialsgov-mcp-server` | npx | Gratis | — |

### Biomedico Integrado

| MCP | Pacote | Runtime | Custo | Variavel .env |
|-----|--------|---------|-------|---------------|
| **biomcp** | `biomcp-python` | uvx | Gratis | — |

Funcoes: OpenFDA, clinical trials, gene info, variant data. Util para farmacovigilancia e busca de trials por droga.

### Gestao de Referencias

| MCP | Pacote | Runtime | Custo | Variavel .env |
|-----|--------|---------|-------|---------------|
| **zotero** | `zotero-mcp` | uvx | Gratis (Zotero local) | `ZOTERO_API_KEY`, `ZOTERO_LIBRARY_ID` |

### Q&A Grounded (PDFs completos)

| MCP | Pacote | Runtime | Custo | Variavel .env |
|-----|--------|---------|-------|---------------|
| **notebooklm** | `notebooklm-mcp-cli` (PyPI) | python -m | Gratis (consumer) | — (auth via cookies) |

NotebookLM MCP permite Q&A grounded nos PDFs completos dos artigos. Requer `nlm login` para autenticar via browser (cookies expiram ~20min). API nao oficial — reverse-engineered RPCs do Google.

Workflow: `nlm login` → `nlm notebook create` → `nlm source add` (PDFs) → `nlm notebook query` (Q&A com citacao).

CLI: `nlm` (instalado via `pip install notebooklm-mcp-cli`). Skill: `.claude/skills/nlm-skill/`.

### Analise e Citacoes

| MCP | Pacote | Runtime | Custo | Variavel .env |
|-----|--------|---------|-------|---------------|
| **scite** | streamableHttp `https://api.scite.ai/mcp` | — | Pago (Premium) | OAuth na 1a conexao |
| **perplexity** | `@perplexity-ai/mcp-server` | npx | Pago | `PERPLEXITY_API_KEY` |

---

## MCPs Claude.ai (nativos — sem config local)

Disponiveis automaticamente em claude.ai (Project Knowledge):

| MCP | Funcao | Custo |
|-----|--------|-------|
| **PubMed** (claude_ai) | Busca, metadados, full-text, citacoes | Incluso |
| **Scholar Gateway** | Semantic search academica | Incluso |
| **Consensus** | Busca com consenso cientifico | Incluso (limites por plano) |

---

## Profiles

| Profile | MCPs academicos incluidos | Uso |
|---------|--------------------------|-----|
| `dev` | 0 | Desenvolvimento de slides |
| `research` | pubmed, crossref, semantic-scholar, perplexity, notebooklm | Pesquisa de evidencias |
| `qa` | 0 | Quality assurance visual |
| `full` | Todos (12 academicos + QA + infra) | Sessoes intensivas |

Trocar profile: `npm run mcp:dev|research|qa|full`

---

## Pre-requisitos

- **Node/npx** — pubmed, crossref, semantic-scholar, perplexity, google-scholar, clinicaltrials, scite
- **uv/uvx** — biomcp, pubmed-simple, arxiv, zotero: `curl -LsSf https://astral.sh/uv/install.sh | sh`

---

## .env (variaveis academicas)

```env
# PubMed — opcional (gratis sem key, 3 req/s; com key 10 req/s)
NCBI_API_KEY=
PUBMED_EMAIL=

# Semantic Scholar — opcional (gratis sem key, com key limits maiores)
SEMANTIC_SCHOLAR_API_KEY=

# Perplexity — requer assinatura paga
PERPLEXITY_API_KEY=

# Zotero — biblioteca local de referencias
ZOTERO_API_KEY=
ZOTERO_LIBRARY_ID=
```

Todas as variaveis estao documentadas em `.env.example` (fonte canonica).
