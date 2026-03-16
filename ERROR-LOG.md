# ERROR-LOG — aulas-magnas (root)

> Erros de infraestrutura e governança cross-project. Erros de conteúdo de aula → `aulas/*/ERROR-LOG.md`.

## Erros corrigidos: 1 | Pendentes: 0

---

### ERRO-001 · CRITICAL · Governança
**Agente em main editou worktree via path absoluto — bypass total de travas**

**Sintoma:** Sessão no workspace `aulas-magnas` (branch main) escreveu diretamente em `C:\Dev\Projetos\wt-cirrose\` usando paths absolutos. Hooks (pre-commit, pre-push) não dispararam porque a escrita foi via ferramenta de edição, não via `git commit`.

**Root cause:** Nenhuma trava impedia escrita de arquivos fora do workspace root. Os hooks git só atuam no momento do commit/push, não na escrita em disco. O agente AI usou paths absolutos para editar arquivos da worktree sem perceber a violação de isolamento.

**Impacto:** Arquivos Classe A/B (`scripts/pre-commit.sh`, `tasks/lessons.md`) foram editados na worktree em vez de no main. Sem a correção, esses arquivos poderiam divergir ou ser perdidos em merge.

**Fix:**
1. Cherry-pick dos arquivos Classe A/B para main
2. `git merge main` em ambas worktrees
3. Regra "anti-crosspath" adicionada em `core-constraints.mdc` e `CLAUDE.md`

**Regra:** Agente em main NUNCA pode escrever em `../wt-*`. Para editar worktree, abrir sessão Cursor naquele diretório. Hooks não são suficientes — a trava é comportamental.

**Status:** ✅ Corrigido (2026-03-16).
