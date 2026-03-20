/**
 * slide-registry.js — Meta-análise
 * State machines for interactive slides (hook, checkpoints).
 * Pattern: cirrose slide-registry.js
 */
export const slideRegistry = {
  's-title': (slide, gsap) => {
    // Full choreography: h1 → subtitle → pillars (masking) → dots → identity
    const h1 = slide.querySelector('h1');
    const subtitle = slide.querySelector('.title-subtitle');
    const pillarSpans = slide.querySelectorAll('.pillar > span');
    const dots = slide.querySelectorAll('.pillar-dot');
    const identity = slide.querySelector('.title-identity');

    // h1: gentle fade+rise (0s)
    if (h1) {
      gsap.fromTo(h1,
        { opacity: 0, y: 12 },
        { opacity: 1, y: 0, duration: 0.7, ease: 'power3.out' }
      );
    }
    // subtitle: fade+rise (0.3s)
    if (subtitle) {
      gsap.fromTo(subtitle,
        { opacity: 0, y: 10 },
        { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out', delay: 0.3 }
      );
    }
    // pillars: masking reveal (0.6s) — overflow:hidden + yPercent
    gsap.fromTo(pillarSpans,
      { yPercent: 100 },
      { yPercent: 0, duration: 0.8, stagger: 0.2, ease: 'power3.out', delay: 0.6 }
    );
    // dots: fade in between pillars (0.8s)
    gsap.fromTo(dots,
      { opacity: 0 },
      { opacity: 1, duration: 0.4, stagger: 0.2, delay: 0.8, ease: 'power2.out' }
    );
    // identity: fade+rise last (1.4s)
    if (identity) {
      gsap.fromTo(identity,
        { opacity: 0, y: 8 },
        { opacity: 1, y: 0, duration: 0.6, ease: 'power2.out', delay: 1.4 }
      );
    }
  },

  's-hook': (slide, gsap) => {
    const volume = slide.querySelector('.hook-volume');
    const divider = slide.querySelector('.hook-divider');
    const facts = slide.querySelectorAll('.hook-fact');
    const nums = slide.querySelectorAll('.hook-num');

    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    // 1. Volume enters from left (hero moment)
    tl.to(volume, { opacity: 1, x: 0, duration: 0.9 });

    // 2. Divider scales in like a cut
    tl.to(divider, { scaleY: 1, duration: 0.6, ease: 'expo.inOut' }, '-=0.3');

    // 3. Reality facts enter from right, staggered
    tl.to(facts, { opacity: 1, x: 0, duration: 0.7, stagger: 0.25 }, '-=0.2');

    // 4. CountUp on all numbers (reset to 0 first — HTML has final values for no-js)
    nums.forEach((num) => {
      const decimals = parseInt(num.getAttribute('data-decimals') || '0', 10);
      const target = decimals > 0 ? parseFloat(num.getAttribute('data-val')) : parseInt(num.getAttribute('data-val'), 10);
      num.textContent = '0';
      const obj = { val: 0 };
      const isVolume = num.closest('.hook-volume');
      const delay = isVolume ? 0 : (num.closest('.hook-fact') === facts[0] ? 1.0 : 1.25);
      const snapVal = decimals > 0 ? Math.pow(10, -decimals) : 1;
      gsap.to(obj, {
        val: target,
        duration: 1.4,
        delay: delay,
        ease: 'power2.out',
        snap: { val: snapVal },
        onUpdate: () => {
          num.textContent = decimals > 0
            ? obj.val.toFixed(decimals).replace('.', ',')
            : Math.round(obj.val);
        }
      });
    });
  },

  's-contrato': (slide, gsap) => {
    const cards = slide.querySelectorAll('.contrato-card');
    const questions = slide.querySelectorAll('.contrato-question');
    const skills = slide.querySelectorAll('.contrato-skill');

    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    // 1. Cards rise + fade (architectural entrance — watermark numbers appear with card)
    tl.to(cards, {
      opacity: 1, y: 0, scale: 1,
      duration: 0.8, stagger: 0.2
    })
    // 2. Questions fade up
    .to(questions, {
      opacity: 1, y: 0,
      duration: 0.5, stagger: 0.2,
      ease: 'power2.out'
    }, '-=0.3')
    // 3. Skills fade up (cohesive with card entrance direction)
    .to(skills, {
      opacity: 1, y: 0,
      duration: 0.5, stagger: 0.15,
      ease: 'power2.out'
    }, '-=0.2');
  },

  's-checkpoint-1': (slide, gsap) => {
    const scenario = slide.querySelector('.checkpoint-scenario');
    const question = slide.querySelector('.checkpoint-question');
    const diamond = slide.querySelector('.ck1-diamond');
    const trials = slide.querySelectorAll('.ck1-trial');
    const accord = slide.querySelector('.ck1-trial--accord');
    const reveal = slide.querySelector('.ck1-reveal');
    if (!scenario || !question || !reveal) return;

    let state = 0;
    const MAX = 2;

    // Beat 0 (auto): scenario fades in — diamond + stats visible
    gsap.to(scenario, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' });

    function advance() {
      if (state >= MAX) return false;
      state++;
      if (state === 1) {
        // Beat 1: provocative question
        gsap.to(question, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' });
      }
      if (state === 2) {
        // Beat 2: "liquidificador" — diamond dissolves, trials appear
        // 1. Diamond fades to ghost
        gsap.to(diamond, { opacity: 0.15, duration: 0.8, ease: 'power2.inOut' });
        // 2. Non-ACCORD trials appear staggered
        const others = [trials[0], trials[1], trials[2]];
        gsap.to(others, { opacity: 1, duration: 0.5, stagger: 0.12, delay: 0.3, ease: 'power2.out' });
        // 3. ACCORD appears with emphasis (larger dot, danger color, slight scale)
        gsap.fromTo(accord,
          { opacity: 0, scale: 0.85 },
          { opacity: 1, scale: 1, duration: 0.6, delay: 0.8, ease: 'power2.out' }
        );
        // 4. Reveal text with ACCORD twist
        gsap.to(reveal, { y: 0, opacity: 1, duration: 0.8, delay: 1.0, ease: 'power3.out' });
      }
      return true;
    }

    function retreat() {
      if (state <= 0) return false;
      if (state === 2) {
        gsap.to(diamond, { opacity: 1, duration: 0.3 });
        gsap.to(trials, { opacity: 0, scale: 1, duration: 0.3 });
        gsap.to(reveal, { opacity: 0, y: 20, duration: 0.3 });
      }
      if (state === 1) {
        gsap.to(question, { opacity: 0, y: 20, duration: 0.3 });
      }
      state--;
      return true;
    }

    slide.__hookAdvance = advance;
    slide.__hookRetreat = retreat;
    slide.__hookCurrentBeat = () => state;
  },

  's-checkpoint-2': (slide, gsap) => {
    const scenario = slide.querySelector('.checkpoint-scenario');
    const question = slide.querySelector('.checkpoint-question');
    const steps = slide.querySelectorAll('.checkpoint-step');
    const verdict = slide.querySelector('.checkpoint-verdict');
    if (!scenario || !question) return;

    let state = 0;
    const MAX = 3;

    gsap.to(scenario, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' });
    gsap.to(question, { y: 0, opacity: 1, duration: 0.6, delay: 0.3, ease: 'power3.out' });

    function advance() {
      if (state >= MAX) return false;
      state++;
      if (state === 1 && steps[0]) {
        gsap.to(steps[0], { y: 0, opacity: 1, duration: 0.5, ease: 'power3.out' });
      }
      if (state === 2) {
        if (steps[1]) gsap.to(steps[1], { y: 0, opacity: 1, duration: 0.5, ease: 'power3.out' });
        if (steps[2]) gsap.to(steps[2], { y: 0, opacity: 1, duration: 0.5, delay: 0.3, ease: 'power3.out' });
      }
      if (state === 3 && verdict) {
        gsap.to(verdict, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' });
      }
      return true;
    }

    function retreat() {
      if (state <= 0) return false;
      if (state === 3 && verdict) {
        gsap.to(verdict, { opacity: 0, y: 12, duration: 0.3 });
      }
      if (state === 2) {
        gsap.to([steps[1], steps[2]].filter(Boolean), { opacity: 0, y: 12, duration: 0.3 });
      }
      if (state === 1 && steps[0]) {
        gsap.to(steps[0], { opacity: 0, y: 12, duration: 0.3 });
      }
      state--;
      return true;
    }

    slide.__hookAdvance = advance;
    slide.__hookRetreat = retreat;
    slide.__hookCurrentBeat = () => state;
  },
};
