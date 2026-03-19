# Archetypes — Meta-analise Layout Patterns

> 6 archetypes across 18 slides. Skeleton + constraints + animation contract per archetype.
> Source: extracted from slides/*.html + metanalise.css + slide-registry.js.
> Use: QA reference, Gemini prompt context, slide creation guard.

---

## 1. concept-evidence

**Slides:** s-rs-vs-ma, s-pico, s-abstract, s-grade, s-heterogeneity, s-fixed-random (6 slides)

### Skeleton

```html
<section id="s-{id}">
  <div class="slide-inner">
    <h2 class="slide-headline">{assertion}</h2>
    <div class="{evidence-container}" data-animate="stagger">
      <!-- 2-5 structured evidence children -->
    </div>
    <p class="source-tag">{source}</p>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Variants

| Sub-variant | Container class | Children | Used by |
|-------------|----------------|----------|---------|
| **compare** | `.compare-layout` | `.compare-col` (2 columns) + `.compare-footer` | s-rs-vs-ma |
| **stack** | `.grade-stack` | `.grade-level` (4 levels, semantic colors) | s-grade |
| **generic** | `.evidence` or custom | Flex children with stagger | s-pico, s-abstract, s-heterogeneity, s-fixed-random |

### Constraints

| Property | Rule |
|----------|------|
| Background | Light (stage-c creme). Exception: s-heterogeneity uses dark bg (#162032) |
| Animation | Declarative `data-animate="stagger"` only — no custom JS |
| Click-reveal | None (single-state slide) |
| h2 | Clinical assertion, not generic label |
| Max children | 5 (Cowan 4+-1) |
| Footer | Optional `.compare-footer` for connecting statement |

### Animation contract

- Engine `stagger`: children fade+translate sequentially (150ms default, override via `data-stagger`)
- Duration: 0.5s per element
- Total: <= 1.5s for full group
- Failsafe: `[data-animate] { opacity: 0 }`, `.no-js [data-animate] { opacity: 1 }`

---

## 2. data-hero

**Slides:** s-hook, s-absoluto (2 slides)

### Skeleton (s-hook — state machine)

```html
<section id="s-hook">
  <div class="slide-inner">
    <div class="hook-question">
      <div class="hook-question-text hook-beat-0">
        <span class="hook-vol-number">{big-number}</span>
        <p class="hook-vol-text">{context}<br>
        <span class="hook-vol-ask">{provocative-question}</span></p>
      </div>
      <div class="hook-data hook-beat-1">
        <div class="hook-hero">
          <span class="hook-hero-value" data-animate="countUp" data-target="{N}" data-suffix="{%}">0</span>
          <span class="hook-hero-label">{what-it-means}</span>
        </div>
      </div>
      <p class="hook-verdict hook-beat-2">{punchline}</p>
    </div>
    <p class="source-tag">{sources}</p>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Skeleton (s-absoluto — declarative)

```html
<section id="s-absoluto">
  <div class="slide-inner">
    <h2 class="slide-headline">{assertion}</h2>
    <div class="concept-card">
      <div class="conversion-hero" data-animate="fadeUp">
        <span class="conversion-hero-value">{common-value}</span>
        <span class="conversion-hero-label">{label}</span>
      </div>
      <div class="conversion-scenarios" data-animate="stagger" data-stagger="0.3">
        <div class="conversion-scenario conversion-impact">...</div>
        <div class="conversion-scenario conversion-negligible">...</div>
      </div>
    </div>
    <p class="source-tag">{source}</p>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Constraints

| Property | Rule |
|----------|------|
| Background | Light (s-hook), Dark (s-absoluto via shared dark-bg selector) |
| Animation | s-hook: custom state machine (slide-registry.js). s-absoluto: declarative fadeUp + stagger |
| Click-reveal | s-hook: 3 beats (auto → click → click). s-absoluto: none |
| Hero number | JetBrains Mono, large (72px+ for hook, hero-sized for absoluto) |
| Max beats | 3 (hook). Single state (absoluto) |
| Typography | Hero number mono, label sans, verdict serif italic (hook) |

### Animation contract (s-hook)

- Beat 0: auto fadeUp on `slide:entered` (0.8s power3.out)
- Beat 1 (click): hero appears + countUp (1.5s power2.out)
- Beat 2 (click): blackout upper content (opacity 0.12, scale 0.95) + verdict fadeUp
- Retreat: reverses each beat sequentially
- State machine: `slide.__hookAdvance()`, `slide.__hookRetreat()`, `slide.__hookCurrentBeat()`

---

## 3. forest-plot

**Slides:** s-forest-plot (1 slide)

### Skeleton

```html
<section id="s-forest-plot">
  <div class="slide-inner">
    <h2 class="slide-headline">{assertion about forest plot elements}</h2>
    <div class="anatomy-grid" data-animate="stagger">
      <div class="anatomy-item">
        <span class="anatomy-symbol">{visual-glyph}</span>
        <div class="anatomy-desc">
          <span class="anatomy-name">{element-name}</span>
          <span class="anatomy-what">{what-it-represents}</span>
        </div>
      </div>
      <!-- 4 more items (5 total: square, line, diamond, null line, direction) -->
    </div>
    <p class="source-tag">{sources}</p>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Constraints

| Property | Rule |
|----------|------|
| Background | Dark (#162032 via shared dark-bg selector) |
| Animation | Declarative stagger (5 items) |
| Click-reveal | None (single-state) |
| Items | Exactly 5 anatomy elements (square, line, diamond, null line, direction) |
| Symbols | Unicode glyphs (not SVG — design decision: placeholder for future cropped forest plot image) |
| Layout | Grid with symbol left, description right |

### Animation contract

- Stagger: 5 items, 150ms apart, total ~1s
- Each item: fadeUp (0.5s)
- Future QA visual may replace anatomy grid with cropped forest plot image from Valgimigli article

---

## 4. benefit-harm

**Slides:** s-benefit-harm (F2 generic), s-aplicacao (F3 with article data) (2 slides)

### Skeleton

```html
<section id="s-{id}">
  <div class="slide-inner">
    <h2 class="slide-headline">{assertion}</h2>
    <div class="compare-layout" data-animate="stagger">
      <div class="compare-col">
        <span class="compare-abbr symbol-safe">&#x2713;</span>
        <span class="compare-name">Beneficio</span>
        <p class="compare-desc">{benefit-data}</p>
      </div>
      <div class="compare-col">
        <span class="compare-abbr symbol-danger">&#x2715;</span>
        <span class="compare-name">Dano</span>
        <p class="compare-desc">{harm-data}</p>
      </div>
    </div>
    <p class="compare-footer">{connecting-statement}</p>
    <p class="source-tag">{source}</p>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Constraints

| Property | Rule |
|----------|------|
| Background | Light (stage-c creme) |
| Animation | Declarative stagger (2 columns) |
| Click-reveal | None |
| Columns | Exactly 2 (benefit left, harm right) |
| Symbols | Daltonism-safe: `symbol-safe` (checkmark/teal), `symbol-danger` (cross/red), `symbol-neutral` (circle/gray for NS) |
| Footer | Required — connects the two columns conceptually |

### Difference F2 vs F3

| Aspect | s-benefit-harm (F2) | s-aplicacao (F3) |
|--------|---------------------|------------------|
| Data | Generic/conceptual | Valgimigli HR values with CI |
| Symbol | safe/danger pair | safe/neutral (harm is NS) |
| Footer | GRADE principle | "GRADE: nao avaliada" |
| Source | Cochrane Handbook | PMID 40902613 |

---

## 5. checkpoint

**Slides:** s-checkpoint-1, s-checkpoint-2 (2 slides)

### Skeleton (checkpoint-1 — 2-beat)

```html
<section id="s-checkpoint-1">
  <div class="slide-inner slide-navy">
    <div class="checkpoint-layout">
      <div class="checkpoint-scenario checkpoint--hidden">
        <p class="checkpoint-context">{clinical-scenario-setup}</p>
        <div class="checkpoint-result">
          <span class="checkpoint-metric">{effect-measure}</span>
          <span class="checkpoint-ci">{confidence-interval}</span>
          <span class="checkpoint-grade">{GRADE-level}</span>
        </div>
        <p class="checkpoint-outcome">{outcome}</p>
      </div>
      <p class="checkpoint-question checkpoint--hidden">{provocative-question}</p>
      <div class="checkpoint-reveal checkpoint--hidden">
        <p class="checkpoint-twist">{the-twist}</p>
      </div>
      <p class="source-tag">{source}</p>
    </div>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Constraints

| Property | Rule |
|----------|------|
| Background | Dark — navy (#162032) via CSS `background-color` on `#s-checkpoint-N .slide-inner` |
| `.slide-navy` | Required on `.slide-inner` (dark bg = on-dark tokens) |
| Animation | Custom state machine in slide-registry.js |
| Click-reveal | CP1: 2 beats (scenario auto, question click, reveal click). CP2: 3 beats (scenario+question auto, steps click, more steps click, verdict click) |
| Initial state | `.checkpoint--hidden` = `opacity: 0; transform: translateY(20px)` |
| Content | Illustrative data (sinalizar em notes). NOT from anchor article |
| Fill ratio | 50-65% (breathing room for drama) |

### Animation contract (CP1)

- Beat 0 (auto): scenario fadeUp (0.8s power3.out)
- Beat 1 (click): question fadeUp (0.8s power3.out)
- Beat 2 (click): reveal fadeUp (0.8s power3.out)
- State machine: advance/retreat/currentBeat pattern (same interface as s-hook)

### Animation contract (CP2)

- Beat 0 (auto): scenario + question fadeUp (0.6s staggered)
- Beat 1 (click): step[0] fadeUp
- Beat 2 (click): step[1] + step[2] fadeUp (staggered 0.3s)
- Beat 3 (click): verdict fadeUp
- 4 total states (0 = initial, 3 = all revealed)

---

## 6. application

**Slides:** s-ancora, s-aplicabilidade (+ s-aplicacao uses benefit-harm archetype) (2-3 slides)

### Skeleton (s-ancora — article anchor)

```html
<section id="s-ancora">
  <div class="slide-inner">
    <h2 class="slide-headline">{assertion with article findings}</h2>
    <div class="anchor-card" data-animate="fadeUp">
      <p class="anchor-citation">{full AMA citation in prose}</p>
      <div class="metric-grid" data-animate="stagger" data-stagger="0.2">
        <div class="metric-item">
          <span class="metric-value">{value}</span>
          <span class="metric-label">{what}</span>
        </div>
        <!-- 3-4 metric items -->
      </div>
    </div>
    <p class="source-tag">{short-citation + PMID}</p>
  </div>
  <aside class="notes">...</aside>
</section>
```

### Constraints

| Property | Rule |
|----------|------|
| Background | Dark (#162032 — s-ancora). Light (s-aplicabilidade) |
| Animation | Declarative: anchor-card fadeUp, metric-grid stagger |
| Click-reveal | None |
| Citation | Full prose citation in `.anchor-citation` (italic journal name) |
| Metrics | 3-4 key numbers in `.metric-grid` (IPD, N RCTs, N patients, follow-up) |
| Data source | MUST be from anchor article (Valgimigli 2025 PMID 40902613) |

### Note on s-aplicacao

s-aplicacao uses the **benefit-harm** archetype (`.compare-layout` with 2 columns) but with article-specific data from Valgimigli. It belongs to F3 narratively but follows benefit-harm layout structurally.

---

## Cross-archetype rules

| Rule | Applies to |
|------|-----------|
| `h2` = clinical assertion (never generic label) | All except checkpoints (which use `.checkpoint-question`) |
| `<aside class="notes">` required with timing blocks | All |
| `data-animate` for declarative, slide-registry.js for state machines | All |
| Max body <= 30 words | All |
| `.source-tag` at bottom | All |
| `.slide-navy` on `.slide-inner` when dark bg | checkpoint, forest-plot, s-ancora, s-absoluto |
| State machine interface: `__hookAdvance`, `__hookRetreat`, `__hookCurrentBeat` | s-hook, s-checkpoint-1, s-checkpoint-2 |
| GSAP failsafe: `[data-animate] { opacity: 0 }`, `.no-js` override | All declarative |
| `.checkpoint--hidden` initial state: `opacity:0; translateY(20px)` | Checkpoints only |

---

## Archetype selection guide (for new slides)

| Content type | Archetype | Why |
|-------------|-----------|-----|
| Concept explanation with examples | concept-evidence | h2 assertion + visual evidence |
| Single impactful number | data-hero | Hero number dominates, context supports |
| Forest plot anatomy or real plot | forest-plot | Specialized grid layout |
| Benefit vs harm comparison | benefit-harm | 2-column with semantic symbols |
| Interactive decision point | checkpoint | State machine, dark bg, drama |
| Article-anchored data | application | Citation + metrics or benefit-harm with real data |
