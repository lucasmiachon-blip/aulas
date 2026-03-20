# Narrativa — Meta-análise

> Fonte de verdade narrativa da aula. Toda decisão de slide deve ser rastreável até aqui.
> Derivado de: memo direcionado de conteúdo (mar/2026).
> Reestruturado: 2026-03-13 — de 4 atos para 3 fases + 2 interações.

---

## Título da aula

**Meta-análise — Leitura crítica para decisão clínica**

## Tese central

Uma boa leitura de meta-análise começa pela pergunta clínica, avalia a credibilidade da síntese, mede o tamanho e a precisão do efeito, e só se completa quando o leitor julga a certeza da evidência e traduz o efeito relativo em impacto absoluto para seu paciente.

## Público

Residentes de clínica médica (básico-intermediário).
**Papel do aluno:** residente-leitor clínico — não revisor, não produtor de RS.

## O que o aluno deve ser capaz de fazer ao final

1. Identificar a pergunta PICO de uma revisão sistemática com meta-análise
2. Ler um forest plot sem pânico: medida de efeito, direção, IC95%, peso
3. Distinguir benefício e dano no mesmo artigo
4. Interpretar níveis de certeza (GRADE) como linguagem clínica, não burocracia
5. Converter efeito relativo em efeito absoluto para decisão no ambulatório
6. Reconhecer limites de aplicabilidade (validade externa)

## O que esta aula NÃO é

- Não é curso de estatística
- Não é tutorial de software (RevMan, R)
- Não é como FAZER uma meta-análise
- Não é NMA, IPD, bayesiana, dose-response

---

## Arco narrativo — 3 fases + 2 interações

> Princípio: primeiro importância/curiosidade, depois metodologia, depois artigo.
> Artigo âncora entra APENAS na Fase 3. Fases 1-2 são genéricas.

### Fase 1 — Criar importância (por que o residente precisa ler MA?)

**Objetivo:** engajar antes de ensinar. O residente precisa QUERER aprender.

**Conteúdo:**
- Por que meta-análise importa para o residente clínico?
- Hook: 3 metric cards (tom sóbrio, sem escândalo):
  - ~80/dia: revisões sistemáticas publicadas (Hoffmann 2021, PMID 34091022)
  - 81%: qualidade criticamente baixa AMSTAR-2 (Bojcic 2024, PMID 37931822)
  - 33,8%: avaliaram certeza GRADE (Siedler 2025)
- h2 curto: "Por que isso importa" (não assertion longo)
- Speaker notes: Hoffmann contexto, Bojcic detalhes, Siedler gap GRADE, takeaway "diamante de verdade ou de vidro"
- Contrato com a audiência: o que a aula vai entregar (3 perguntas framework)

**Tensão narrativa:** "eu achava que sabia ler uma MA, mas talvez não saiba tanto"

**Slides:** 00-title, 01-hook, 02-contrato

### Interação 1 — Checkpoint de engajamento (entre Fase 1 e Fase 2)

**Momento:** após criar importância, antes de entrar em metodologia.
**Formato:** pergunta provocativa com dados reais (ACCORD como armadilha).

**Cenário (dados reais — Ray 2009 Lancet, PMID 19465231):**
MA de 5 RCTs, 33.040 pacientes. Controle glicêmico intensivo reduz infarto em 17% (OR 0,83, IC 0,75–0,93).
"Você aperta a meta de HbA1c do seu paciente?"
- A maioria dirá sim
- Twist: o ACCORD (PMID 18539917) — maior trial da MA (10.251 pts, 31%) — foi interrompido por aumento de mortalidade (HR 1,22, p=0,04)
- O diamante disse benefício, mas dentro dele, o maior pedaço apontava pro lado errado

**Visual:** diamante simplificado + linha de nulidade → "liquidificador" (diamond fades, trial markers appear, ACCORD em vermelho no lado do dano)

**Função pedagógica:** retrieval practice + criar tensão + ancorar o conceito de "olhar dentro do diamante". Prepara para forest plot (slide 07) e heterogeneidade (slide 10).

**Slide:** 03-checkpoint-1

### Fase 2 — Metodologia (conceitos-chave para leitura crítica)

**Objetivo:** ensinar os conceitos necessários — sem ancorar em artigo específico.

**Conteúdo (um conceito por slide):**
1. RS vs MA — diferença fundamental
2. PICO como porta de entrada (genérico, sem artigo)
3. Como ler um abstract de RS (PRISMA, genérico)
4. Forest plot: medida de efeito, direção, IC95%, peso, diamante
5. Benefício e dano no mesmo artigo
6. GRADE como linguagem clínica (alta, moderada, baixa)
7. Heterogeneidade (I²) — o que realmente importa
8. Efeito fixo vs aleatório (mínimo necessário para leitura)

**Credibility gap (convergência Gemini):** entre abstract (slide 06) e forest plot (slide 07), o residente pode assumir que PRISMA = qualidade. Não é: PRISMA é transparência de relato, não avaliação de risco de viés (RoB). O conceito de "posso confiar nesta síntese?" deve ser embutido nas speaker notes do abstract e reforçado no GRADE. Não requer slide adicional — é um fio condutor.

**Tensão narrativa:** cada conceito revela uma camada de complexidade que o residente não via

**Slides:** 04 a 11 (8 slides metodológicos)

### Interação 2 — Checkpoint de consolidação (entre Fase 2 e Fase 3)

**Momento:** após ensinar os conceitos, antes de aplicar no artigo real.
**Formato:** mini-caso com dados genéricos para o residente interpretar.

**Cenário (recalibrado — convergência Gemini):**
"Forest plot mostra RR 0.75 (IC 0.60–0.93), I²=72%, certeza GRADE baixa.
O diamante favorece o tratamento. Você muda sua conduta?"

**Twist (falso positivo):**
- O diamante diz benefício (RR < 1, IC não cruza 1)
- Mas I² alto + GRADE baixa = não confiar cegamente
- E o efeito absoluto? Risco basal de 5% → ARR = 1,25% → NNT = 80
- Resposta: "provavelmente NÃO muda conduta — efeito pequeno, certeza baixa, precisa de contexto"

**Função pedagógica:** consolidar antes de complexificar com artigo real. Testing effect. Expor o viés de confiança no diamante (mesmo residente que disse "sim" no checkpoint 1 agora hesita — crescimento).

**NOTA:** dados do mini-caso são ilustrativos/didáticos, não de artigo real. Sinalizar claramente no slide.

**Slide:** 12-checkpoint-2

### Fase 3 — Aplicação (Valgimigli 2025 — Lancet)

**Objetivo:** aplicar todos os conceitos em artigo real. Provar que o framework funciona.

**Artigo âncora:** Valgimigli M, et al. Clopidogrel versus aspirin for secondary prevention of coronary artery disease. Lancet 2025;406(10508):1091-1102. PMID 40902613.
- IPD-MA, 7 RCTs, 28.982 pacientes
- MACCE (5,5 anos): HR 0,86 (0,77–0,96)
- Sangramento maior: HR 0,94 (0,74–1,21) — NS
- GRADE: não avaliada pelos autores

**Tensões didáticas do artigo:**
- IPD (não pairwise clássica) — o residente aprende que o mundo real é mais sofisticado
- HR (não RR) — medida natural para tempo-até-evento; interpretação análoga (direção, IC, nulidade)
- Sem GRADE — valida a pergunta 2 do takehome ("certeza GRADE?") — mesmo Lancet pode omitir

**Conteúdo:**
1. Slide 13: O artigo âncora — apresentar PICO, design, números-chave
2. Slide 14: Aplicar framework — benefício vs dano com dados reais + expor lacuna GRADE
3. Slide 15: Validade externa / aplicabilidade — PICO do artigo vs seu paciente
4. Slide 16: Efeito relativo vs absoluto (genérico — já existente)
5. Slide 17: Take-home — as 3 perguntas que o residente leva (já existente)

**Tensão narrativa:** "agora que sei a teoria, os dados reais são mais complicados do que parecem — e mesmo o Lancet não responde todas as perguntas que eu deveria fazer"

**Slides:** 13 a 17 (3 novos + 2 existentes)

---

## Princípio pedagógico central

Uma meta-análise não é melhor do que os RCTs que a alimentam. A qualidade da síntese depende da qualidade da produção e da adjudicação das evidências individuais incluídas. O diamante do forest plot herda as fragilidades de cada quadrado que o compõe — e o residente precisa saber disso.

## Três perguntas que o residente leva para casa

1. **Qual é a pergunta — e posso confiar na síntese?** (PICO + credibilidade: PRISMA ≠ qualidade; RoB importa)
2. **Qual é o efeito, quão preciso, e qual o dano?** (forest plot + benefício-dano separados)
3. **Quão certa é a evidência — e o que isso significa para MEU paciente?** (GRADE por desfecho + efeito absoluto, não só relativo)

## Formato

- 45–60 min expositiva/interativa
- Pre-reading: 35–45 min (4 leituras obrigatórias)

---

## Revisão dos slides existentes (CONCLUÍDA)

> 6/6 slides revisados (2026-03-13). Detalhes: CHANGELOG.md.

---

## Changelog

| Data | Mudança |
|------|---------|
| 2026-03-11 | v0 — bootstrap a partir do memo direcionado |
| 2026-03-13 | v1 — reestruturado de 4 atos para 3 fases + 2 interações. Artigo desancorado das fases iniciais |
| 2026-03-13 | v1.1 — revisão de slides existentes concluída. Orphans deletados. Tabela de revisão atualizada |
| 2026-03-20 | v2.5 — I1 reescrito com ACCORD trap (Ray 2009/ACCORD 2008). Dados reais substituem cenário genérico. Visual liquidificador. |
| 2026-03-19 | v2.4 — Hook rewrite sober: VITALITY/NICE-SUGAR removidos do slide. Agora 3 metric cards (Hoffmann 80/dia, Bojcic 81% AMSTAR-2, Siedler 33.8% GRADE). h2 curto. Sem click-reveals. |
| 2026-03-19 | v2.3 — Fase 1 hook dados atualizados: VITALITY backbone (1.330 retratados → 3.902 MAs → 20% mudam → 157 guidelines). NICE-SUGAR como exemplo MA. Refs expandidas (INSPECT-SR, Possamai, Guyatt). |
| 2026-03-15g | v2.2 — Âncora decidida: Valgimigli 2025 Lancet (PMID 40902613). Fase 3 atualizada com tensões didáticas IPD/HR/GRADE. Slides 13-15 criados |
| 2026-03-15b | v2.1 — Nota: âncora em deliberação (Pitre PAC ou Abdul-Aziz β-lactam). Cochrane = exemplos visuais. Estrutura narrativa inalterada. Área do Lucas ≠ hepatologia |
| 2026-03-15 | v2 — convergências Gemini absorvidas: tese central (credibilidade + efeito absoluto), 3 perguntas reformuladas, credibility gap documentado, checkpoint-2 recalibrado para "falso positivo" |
