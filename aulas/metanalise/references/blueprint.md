# Blueprint — Meta-análise

> Espinha de slides. Cada entrada = 1 slide-núcleo.
> Assertion-evidence: h2 = afirmação verificável, nunca rótulo genérico.
> Derivado de: narrative.md v2.4 (3 fases + 2 interações).
> Reestruturado: 2026-03-13. Atualizado: 2026-03-19 (v1.9 — Siedler PMID, framing corrigido).

---

## Convenções

- **Fase:** em qual das 3 fases da narrativa ele vive
- **Função:** papel didático do slide no arco
- **Assertion:** a frase que vai no h2 (rascunho, será refinada)
- **Risco cognitivo:** qual erro de interpretação esse slide previne
- **Evidência:** de onde vem o dado central
- **Status:** slide existente / novo / reescrever / generalizar

---

## FASE 1 — Criar importância

### Slide 00 — Título

- **Fase:** 1
- **Função:** enquadramento + expectativa
- **Assertion:** "Meta-análise sem terror: como ler um forest plot e decidir se isso muda sua prática"
- **Risco cognitivo:** —
- **Evidência:** —
- **Status:** EXISTENTE (00-title.html) — manter

### Slide 01 — Por que meta-análise importa

- **Fase:** 1
- **Função:** hook — criar importância, gerar curiosidade
- **Assertion:** "Por que isso importa" (h2 curto — archetype hook, não assertion longo)
- **Risco cognitivo:** aula parecer estatística pura → desmotivação imediata
- **Evidência:** ~80/dia SRs publicadas (Hoffmann 2021, PMID 34091022), 81% qualidade criticamente baixa AMSTAR-2 (Bojcic 2024, PMID 37931822), 33,8% sequer avaliaram certeza da evidência (Siedler 2025, PMID 40969451). Detalhes: evidence-db.md §s-hook
- **Status:** ✅ FEITO (01-hook.html) — sober 3-card metrics layout, asymmetric grid, countUp GSAP. DONE (QA.0-QA.4 PASS, avg 9.36)

### Slide 02 — Contrato com a audiência

- **Fase:** 1
- **Função:** definir o que a aula entrega — criar expectativa
- **Assertion:** "3 perguntas que você faz a toda meta-análise"
- **Risco cognitivo:** residente não saber o que esperar → atenção dispersa
- **Evidência:** —
- **Status:** ✅ DONE (02-contrato.html) — 3 cards: "Posso confiar na síntese?" / "Qual o efeito — e qual o dano?" / "O que isso significa para meu paciente?". Watermark-only design, grid+subgrid, GSAP choreography. QA.0-QA.4 PASS.

---

## INTERAÇÃO 1 — Checkpoint de engajamento

### Slide 03 — Você mudaria sua conduta? (ACCORD trap)

- **Fase:** Interação 1
- **Função:** provocar a audiência — expor viés de confiança no diamante com dados reais
- **Assertion:** "Controle glicêmico intensivo reduziu infarto — mas o maior trial da MA aumentou mortalidade"
- **Risco cognitivo:** residente aceitar resultado da MA sem olhar os estudos individuais
- **Evidência:** Ray 2009 Lancet (PMID 19465231) — OR 0,83 IAM; ACCORD 2008 NEJM (PMID 18539917) — HR 1,22 mortalidade
- **Status:** ✅ FEITO (03-checkpoint-1.html) — diamond liquidificador visual + 3-beat click-reveal: cenário → pergunta → ACCORD twist
- **Nota:** dados REAIS (não ilustrativos). ACCORD como armadilha antes de ensinar forest plot.

---

## FASE 2 — Metodologia

### Slide 04 — Revisão sistemática =/= meta-análise

- **Fase:** 2
- **Função:** desfazer a confusão mais comum
- **Assertion:** "RS é o método de busca e seleção; MA é o cálculo estatístico — e são separáveis"
- **Risco cognitivo:** tratar RS e MA como sinônimos → perda da estrutura lógica
- **Evidência:** Cochrane Handbook v6.5, cap. 1
- **Status:** ✅ FEITO (04-rs-vs-ma.html) — renumerado, assertion atualizada

### Slide 05 — O PICO como porta de entrada

- **Fase:** 2
- **Função:** ensinar que toda MA começa por uma pergunta estruturada
- **Assertion:** "PICO define a validade externa: se a população ou o comparador não batem, o resultado não se aplica"
- **Risco cognitivo:** pular direto para resultados sem entender elegibilidade
- **Evidência:** Cochrane Handbook v6.5, cap. 3
- **Status:** ✅ FEITO (04-pico.html) — generalizado, sem dados Musini

### Slide 06 — O que o abstract já entrega

- **Fase:** 2
- **Função:** mostrar que o abstract de boa RS é denso e ensinável
- **Assertion:** "Abstract PRISMA entrega busca, elegibilidade, N de estudos e resultado — triagem em 2 min antes do PDF"
- **Risco cognitivo:** ler abstract superficialmente → perder metadados estruturais
- **Evidência:** PRISMA 2020 for Abstracts (Page et al. BMJ 2021;372:n160)
- **Status:** ✅ FEITO (05-abstract.html) — generalizado, pipeline flow layout

### Slide 07 — Como ler o forest plot

- **Fase:** 2
- **Função:** alfabetização no forest plot — medida, direção, nulidade, IC95%, peso
- **Assertion:** "Forest plot codifica efeito, precisão e peso de cada estudo em 5 elementos — quadrado, linha, diamante, eixo e direção"
- **Risco cognitivo:** confundir significância estatística com importância clínica
- **Evidência:** Dettori et al. Global Spine J 2021, PMID 33939533 · Baruah et al. Indian J Anaesth 2025, PMC11878362 · Cochrane Handbook v6.5, cap. 10
- **Status:** ✅ FEITO (06-forest-plot.html) — anatomy grid, 5 elementos com símbolos

### Slide 08 — Benefício e dano no mesmo artigo

- **Fase:** 2
- **Função:** mostrar que MA séria reporta dano, não só benefício
- **Assertion:** "Benefício e dano podem ter certeza GRADE diferente na mesma MA — avaliar ambos separadamente"
- **Risco cognitivo:** ignorar dano porque o benefício é significativo
- **Evidência:** Cochrane Handbook v6.5, cap. 15
- **Status:** ✅ FEITO (07-benefit-harm.html) — compare layout com ícones ✓/✕

### Slide 09 — Certeza da evidência (GRADE)

- **Fase:** 2
- **Função:** introduzir GRADE como linguagem clínica
- **Assertion:** "Certeza GRADE expressa confiança no efeito estimado — avalia por desfecho, não por artigo"
- **Risco cognitivo:** tratar GRADE como burocracia metodológica → não usar na prática
- **Evidência:** GRADE Working Group · Cochrane Handbook v6.5, cap. 14
- **Status:** ✅ FEITO (08-grade.html) — 4 níveis com ícones daltonismo (✓ ○ ⚠ ✕)

### Slide 10 — Heterogeneidade

- **Fase:** 2
- **Função:** desfazer o mito de que I² alto = MA inválida
- **Assertion:** "I² alto não invalida a MA — importa se a heterogeneidade é explicável e clinicamente relevante"
- **Risco cognitivo:** I² alto → descartar a MA automaticamente
- **Evidência:** Higgins & Thompson BMJ 2003, PMID 12958120 · Borenstein 2017, PMID 28058794 · Cochrane Handbook v6.5, cap. 10
- **Status:** ✅ FEITO (09-heterogeneity.html) — concept card com I² hero + question box

### Slide 11 — Efeito fixo vs. aleatório

- **Fase:** 2
- **Função:** dar ao residente o mínimo para leitura madura
- **Assertion:** "Random-effects alarga o IC quando há heterogeneidade — resultado significativo em fixed-effect pode desaparecer"
- **Risco cognitivo:** ignorar que o modelo afeta a interpretação
- **Evidência:** Cochrane Handbook v6.5, cap. 10
- **Status:** ✅ FEITO (10-fixed-random.html) — compare layout FE vs RE

---

## INTERAÇÃO 2 — Checkpoint de consolidação

### Slide 12 — Falso positivo: o diamante mente?

- **Fase:** Interação 2
- **Função:** consolidar conceitos + expor viés de confiança no diamante
- **Assertion:** "RR 0.75 (IC 0.60–0.93), I²=72%, certeza GRADE baixa — o diamante favorece. Você muda sua conduta?"
- **Risco cognitivo:** confiar no diamante sem avaliar certeza e efeito absoluto
- **Evidência:** dados ilustrativos/didáticos (NÃO de artigo real — sinalizar claramente)
- **Status:** ✅ FEITO (12-checkpoint-2.html) — click-reveal 4-beat: cenário+pergunta → ✓safe → ⚠warning+✕danger → verdict (via slide-registry.js)
- **Twist:** diamante favorece tratamento (IC não cruza 1) MAS I²=72% + GRADE baixa + efeito absoluto pequeno (ARR ~1,25%, NNT ~80 com baseline risk 5%) → "provavelmente NÃO muda conduta"
- **Arco com CP1:** no checkpoint-1 a maioria disse "sim" (RR 0.91, IC significativo). Aqui, mesmo com RR mais impressionante (0.75), a resposta correta é "não" — crescimento do residente.

---

## FASE 3 — Aplicação (Valgimigli 2025)

> Artigo âncora: **Valgimigli 2025 — Clopidogrel vs Aspirina (Lancet, PMID 40902613)**. IPD-MA, 7 RCTs, 28.982 pts.
> Cochrane reviews reservados para exemplos visuais nas Fases 1-2.
> Slides 13-17 criados com dados reais.

### Slide 13 — O artigo âncora (Valgimigli 2025)

- **Fase:** 3
- **Função:** ancorar aplicação em artigo real — primeiro slide que nomeia artigo específico
- **Assertion:** "Clopidogrel reduziu eventos cardiovasculares vs aspirina em prevenção secundária — 7 RCTs e 28.982 pacientes com dados individuais"
- **Risco cognitivo:** discutir MA no vácuo → desconexão clínica
- **Evidência:** Valgimigli et al. Lancet 2025;406(10508):1091-1102. PMID 40902613
- **Layout:** anchor-card (citação AMA) + metric-grid (IPD, 7 RCTs, 28.982 pts, 2,3a follow-up)
- **Nota didática:** IPD ≠ pairwise — explicar em notes que os princípios de leitura são os mesmos
- **Status:** ✅ FEITO (13-ancora.html) — anchor-card + metric-grid, notes explicam IPD e HR

### Slide 14 — Resultados + framework aplicado

- **Fase:** 3
- **Função:** aplicar framework (benefício-dano, GRADE) ao artigo real — expor lacuna GRADE
- **Assertion:** "MACCE caiu 14% com clopidogrel, sem aumento de sangramento — mas certeza GRADE não foi avaliada"
- **Risco cognitivo:** aceitar resultado sem avaliar certeza; confiar no diamante porque é Lancet
- **Evidência:** Valgimigli et al. Lancet 2025. PMID 40902613. MACCE HR 0,86 (0,77–0,96). Sangramento HR 0,94 (0,74–1,21) NS
- **Layout:** compare-layout (benefício ✓ vs dano ○) + compare-footer--gap (GRADE warning)
- **Nota didática:** "Mesmo o Lancet pode omitir GRADE" — valida pergunta 2 do takehome
- **Status:** ✅ FEITO (14-aplicacao.html) — compare-layout com dados reais + gap callout

### Slide 15 — Aplicabilidade

- **Fase:** 3
- **Função:** o salto de "funciona?" para "funciona para meu paciente?" — callback ao PICO (slide 05)
- **Assertion:** "Prevenção secundária de DAC, seguimento mediano 2,3 anos — antes de adotar, verifique se seu paciente se encaixa"
- **Risco cognitivo:** aplicar resultado de MA sem questionar validade externa
- **Evidência:** Valgimigli et al. Lancet 2025. PMID 40902613
- **Layout:** pico-grid (callback ao slide 05) com conteúdo aplicado ao artigo
- **Nota didática:** cada letra PICO agora tem dados reais + pergunta de aplicabilidade
- **Status:** ✅ FEITO (15-aplicabilidade.html) — pico-grid com dados Valgimigli + perguntas de validade externa

### Slide 16 — Efeito relativo vs. absoluto

- **Fase:** 3
- **Função:** converter RR em NNT / efeito absoluto legível
- **Assertion:** "Mesmo RR pode significar NNT 25 ou NNT 250 — sem risco basal, efeito relativo não informa decisão"
- **Risco cognitivo:** tomar decisão clínica com efeito relativo sem baseline risk
- **Evidência:** Cochrane Handbook v6.5, cap. 15 — dados ilustrativos
- **Status:** ✅ FEITO (16-absoluto.html) — conversion layout: RR 0.80 → NNT 25 (baseline 20%) vs NNT 250 (baseline 2%)

### Slide 17 — Take-home

- **Fase:** 3
- **Função:** fechamento — as 3 perguntas que o residente leva
- **Assertion:** "Três perguntas que você faz a toda MA antes de mudar sua conduta"
- **Risco cognitivo:** sair da aula sem framework operacional reutilizável
- **Evidência:** síntese narrativa — Cochrane Handbook, PRISMA 2020, GRADE
- **Status:** ✅ FEITO (17-takehome.html) — 3 takehome cards com perguntas reformuladas, alinhado com contrato (slide 02)

---

## Historico (CONCLUIDO)

> Migração 18/18 ✅. Âncora: Valgimigli 2025 (PMID 40902613). Dossiês Gemini absorvidos em narrative v2.
> Detalhes: CHANGELOG.md + HANDOFF-ARCHIVE.md.

---

## Status: BLUEPRINT v2.0 — 18 slides (deck completo). F1 DONE (3/18); I1 reescrito com ACCORD; F2-F3 LINT-PASS (15/18).
