# Slide Identity — Regra de Integridade

> Erro mais recorrente do projeto. Qualquer operacao em ID de slide
> que nao toque TODAS as 9 superficies = drift garantido.
> Relacionados: [slide-editing](slide-editing.md) · [reveal-patterns](reveal-patterns.md)

## 1. Anatomia de um Slide ID

```
s-{act}-{slug}

Exemplos:
  s-a1-damico    → Act 1, slide D'Amico
  s-a2-05        → Act 2, slide 05
  s-cp1          → Checkpoint 1
  s-app-alb      → Apendice, albumina
  s-hook          → Pre-ato (sem act prefix)
  s-title         → Pre-ato (sem act prefix)
  s-close         → Fechamento
```

Regras do formato:
- Prefixo `s-` obrigatorio
- Act: `a1`, `a2`, `a3`, `cp`, `app`, ou vazio (pre/close)
- Slug: lowercase, hifens, sem acentos, max 12 chars
- ID e IMUTAVEL apos primeiro commit — renomear so com protocolo completo

## 2. As 9 Superficies de Identidade

Toda operacao de criacao/rename/split/delete DEVE tocar TODAS:

| # | Arquivo | Campo | Exemplo |
|---|---------|-------|---------|
| 1 | `slides/_manifest.js` | `id` no objeto do slide | `{ id: 's-a1-damico', ... }` |
| 2 | `slides/NN-slug.html` | `<section id="...">` | `<section id="s-a1-damico">` |
| 3 | `slide-registry.js` | chave em `customAnimations` | `'s-a1-damico': (slide, gsap) => {` |
| 4 | `{aula}.css` | seletores `#s-xxx` | `#s-a1-damico .source-tag { }` |
| 5 | `references/narrative.md` | coluna Slide na tabela | `| s-a1-damico |` |
| 6 | `references/evidence-db.md` | referencias a slide ID | `## s-a1-damico` ou inline |
| 7 | `AUDIT-VISUAL.md` | header de scorecard | `### s-a1-damico (02b-a1-damico.html)` |
| 8 | `HANDOFF.md` | mencoes em backlog/status | `- h2 assertivo fib4: ...` |
| 9 | `index.html` | GERADO — `npm run build:{aula}` | nao editar manualmente |

**Superficie 3 (slide-registry.js):** so se o slide TEM customAnimation.
**Superficie 9 (index.html):** NUNCA editar. Rodar build apos qualquer mudanca.

## 3. Protocolo de CRIACAO de Slide

### Checklist (ordem obrigatoria)

1. Escolher ID seguindo convencao `s-{act}-{slug}`
2. Criar arquivo `slides/NN-slug.html` com `<section id="s-{act}-{slug}">`
3. Adicionar entrada em `_manifest.js` na posicao correta (ordem = ordem de apresentacao)
4. Se slide tem animacao custom → adicionar em `slide-registry.js`
5. Se slide tem CSS especifico → adicionar em `{aula}.css` com seletor `#s-{slug}` (ou `#s-{act}-{slug}` se a aula usa acts)
6. Adicionar linha em `narrative.md` na tabela do ato correspondente
7. `npm run build:{aula}` → verificar que `index.html` inclui o slide
8. `npm run lint:slides` → PASS
9. Registrar em `CHANGELOG.md`

### Numero do arquivo (NN)

O prefixo numerico `NN-` no nome do arquivo HTML e APENAS para ordenacao no filesystem.
NAO precisa corresponder a posicao no manifest (que define a ordem real).
Ao criar, usar proximo numero disponivel no ato.

## 4. Protocolo de RENAME de Slide

> RENAME = operacao de ALTO RISCO. So executar com aprovacao explicita.

### Pre-flight

```bash
grep -rn "ID_ANTIGO" aulas/{aula}/ --include="*.html" --include="*.js" --include="*.css" --include="*.md"
```

### Checklist atomico (TODAS as 9 superficies)

- [ ] `_manifest.js`: trocar `id` no objeto
- [ ] `slides/NN-slug.html`: trocar `<section id="...">`
- [ ] `slide-registry.js`: trocar chave em `customAnimations` (se existir)
- [ ] `{aula}.css`: trocar TODOS os seletores `#ID_ANTIGO` → `#ID_NOVO`
- [ ] `narrative.md`: trocar na tabela do ato
- [ ] `evidence-db.md`: trocar referencias
- [ ] `AUDIT-VISUAL.md`: trocar header do scorecard
- [ ] `HANDOFF.md`: trocar mencoes
- [ ] `npm run build:{aula}` → rebuild index.html
- [ ] `npm run lint:slides` → PASS
- [ ] Verificacao final: `grep -rn "ID_ANTIGO" aulas/{aula}/` retorna ZERO

### NUNCA renomear arquivo HTML junto com ID

Rename de ID e rename de filename sao operacoes SEPARADAS.
Executar em commits separados para facilitar rollback.

## 5. Protocolo de SPLIT (1 slide → 2)

1. **NAO deletar o slide original.** Manter como slide A.
2. Criar slide B com novo ID (seguindo convencao).
3. Redistribuir conteudo entre A e B.
4. Atualizar `_manifest.js`: slide B APOS slide A na sequencia.
5. Se slide A tinha customAnimation → ajustar para novo conteudo.
6. Criar customAnimation para slide B se necessario.
7. Atualizar `narrative.md`: nova linha para slide B.
8. Atualizar contagens em HANDOFF/CLAUDE.md (N+1 slides total).
9. `npm run build:{aula}` + `npm run lint:slides`.
10. Re-auditar ambos slides em AUDIT-VISUAL.md.

## 6. Protocolo de DELETE

1. Remover de `_manifest.js`.
2. NAO deletar o arquivo HTML (mover para `slides/_archive/` se quiser).
3. Remover de `slide-registry.js` (se tinha customAnimation).
4. Remover seletores CSS em `{aula}.css`.
5. Marcar como removido em `narrative.md` (~~riscado~~ ou removido).
6. Atualizar contagens em HANDOFF/CLAUDE.md (N-1).
7. `npm run build:{aula}` + `npm run lint:slides`.

## 7. Verificacao Automatizada

### Comando de auditoria (rodar antes de QUALQUER commit que toque slides)

```bash
node -e "
// Usage: node -e "..." -- {aula}  (ex: node -e "..." -- cirrose)
var aula=process.argv.pop()||'cirrose';
var m=require('./aulas/'+aula+'/slides/_manifest.js');
var fs=require('fs');var p=require('path');
var ok=0,fail=0;
m.slides.forEach(function(s){
  var fp=p.join('aulas',aula,'slides',s.file);
  if(!fs.existsSync(fp)){console.log('MISSING|'+s.id+'|'+s.file);fail++;return}
  var html=fs.readFileSync(fp,'utf8');
  var r=html.match(/id=\x22([^\x22]+)\x22/);
  var hid=r?r[1]:'NONE';
  if(hid===s.id){ok++}else{console.log('MISMATCH|manifest:'+s.id+'|html:'+hid);fail++}
});
console.log('Result: '+ok+' OK, '+fail+' FAIL');
if(fail>0)process.exit(1);
"
```

Se FAIL > 0: **NAO COMMITAR.** Corrigir primeiro.

## 8. Anti-patterns (erros reais do projeto)

| Anti-pattern | Exemplo | Consequencia |
|-------------|---------|-------------|
| Renomear arquivo sem atualizar manifest | `05-a1-infeccao.html` tem ID `s-a2-04` | Nome enganoso, confunde agentes |
| Mudar `<section id>` sem atualizar CSS | ID novo, CSS antigo nunca casa | Estilos quebram silenciosamente |
| Mudar headline no HTML sem atualizar manifest | h2 diz X, manifest.headline diz Y | lint:narrative-sync FAIL |
| Criar slide sem entrada no manifest | HTML existe, nao aparece no build | Slide fantasma |
| Split sem atualizar contagens | HANDOFF diz 44, manifest tem 45 | Drift documental |
| Editar `index.html` diretamente | Mudanca sobrescrita no proximo build | Trabalho perdido |

## 9. Nomes de arquivo enganosos (debt conhecida)

> **Nota:** Esta tabela e especifica da aula `cirrose` (migracao historica de acts).
> Outras aulas podem ter debt similar — documentar aqui ou no HANDOFF da aula.

Estes arquivos tem nomes que NAO correspondem ao ID atual (migracao historica, aula cirrose):

| Arquivo | ID atual | Porque |
|---------|----------|--------|
| `05-a1-infeccao.html` | `s-a2-04` | Migrou de Act 1 para Act 2 |
| `24-app-ccc.html` | `s-a2-13` | Migrou de appendice para Act 2 |
| `25-app-pulm.html` | `s-a2-14` | Migrou de appendice para Act 2 |
| `10-a2-albumina.html` | `s-app-alb` | Migrou de Act 2 para appendice |
| `06-a1-etiologias.html` | `s-app-etio` | Migrou de Act 1 para appendice |
| `15-a3-recompensacao.html` | `s-a3-02` | Renumerado dentro do Act 3 |
| `16-a3-svr.html` | `s-a3-05` | Renumerado dentro do Act 3 |
| `17-a3-vigilancia.html` | `s-a3-06` | Renumerado dentro do Act 3 |

Renomear estes arquivos e backlog de baixa prioridade.
O ID no `<section>` e no `_manifest.js` e o que importa — nome do arquivo e cosmetic.
