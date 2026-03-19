/**
 * slide-registry.js — Meta-análise
 * State machines for interactive slides (hook, checkpoints).
 * Pattern: cirrose slide-registry.js
 */
import { SplitText } from 'gsap/SplitText';

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
    const beat0 = slide.querySelector('.hook-beat-0');
    const beat1 = slide.querySelector('.hook-beat-1');
    const beat2 = slide.querySelector('.hook-beat-2');
    if (!beat0 || !beat1) return;

    let state = 0;
    const MAX = 2;
    let splitInstances = [];

    // Beat 0: ScrambleText "1.330" + SplitText words on description
    const volNumber = slide.querySelector('.hook-vol-number');
    const volText = slide.querySelector('.hook-vol-text');

    gsap.to(beat0, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' });

    // ScrambleText on "1.330" — information gap before reveal
    if (volNumber) {
      volNumber.textContent = '';
      gsap.to(volNumber, {
        scrambleText: {
          text: '1.330',
          chars: '0123456789.',
          speed: 0.6,
          revealDelay: 0.3
        },
        duration: 1.4,
        ease: 'power2.out'
      });
    }

    // SplitText on description — guided reading rhythm
    if (volText) {
      const splitVol = new SplitText(volText, { type: 'words' });
      splitInstances.push(splitVol);
      gsap.from(splitVol.words, {
        opacity: 0, y: 8,
        stagger: 0.04,
        duration: 0.5,
        ease: 'power3.out',
        delay: 1.2
      });
    }

    function advance() {
      if (state >= MAX) return false;
      state++;
      if (state === 1) {
        // Beat 1: ScrambleText "20%" — genuine suspense (replaces countUp)
        gsap.set(beat1, { visibility: 'visible' });
        gsap.to(beat1, { y: 0, opacity: 1, duration: 0.5, ease: 'power3.out' });
        const heroValue = beat1.querySelector('.hook-hero-value');
        if (heroValue) {
          gsap.set(heroValue, { opacity: 1 }); // override [data-animate] opacity:0
          heroValue.textContent = '';
          gsap.to(heroValue, {
            scrambleText: {
              text: '20%',
              chars: '0123456789%',
              speed: 0.7,
              revealDelay: 0.4
            },
            duration: 1.6,
            ease: 'power2.out',
            delay: 0.3
          });
        }
      }
      if (state === 2 && beat2) {
        // Beat 2: blackout upper (near-invisible) + SplitText verdict
        const upper = slide.querySelectorAll('.hook-question-text, .hook-data');
        gsap.to(upper, { opacity: 0.04, scale: 0.97, duration: 0.5, ease: 'power2.inOut' });

        gsap.set(beat2, { visibility: 'visible', opacity: 1, y: 0 });
        const splitVerdict = new SplitText(beat2, { type: 'words,chars' });
        splitInstances.push(splitVerdict);
        gsap.from(splitVerdict.chars, {
          opacity: 0,
          stagger: 0.025,
          duration: 0.3,
          ease: 'power2.out',
          delay: 0.6
        });
      }
      return true;
    }

    function retreat() {
      if (state <= 0) return false;
      if (state === 2 && beat2) {
        // Revert SplitText on verdict before hiding
        const lastSplit = splitInstances.pop();
        if (lastSplit) lastSplit.revert();
        gsap.killTweensOf(beat2);
        gsap.to(beat2, { opacity: 0, duration: 0.3 });
        gsap.set(beat2, { visibility: 'hidden', delay: 0.3 });
        // Restore upper content from blackout
        const upper = slide.querySelectorAll('.hook-question-text, .hook-data');
        gsap.to(upper, { opacity: 1, scale: 1, duration: 0.4, ease: 'power3.out' });
      }
      if (state === 1) {
        gsap.to(beat1, { opacity: 0, duration: 0.3 });
        gsap.set(beat1, { visibility: 'hidden', delay: 0.3 });
      }
      state--;
      return true;
    }

    slide.__hookAdvance = advance;
    slide.__hookRetreat = retreat;
    slide.__hookCurrentBeat = () => state;
    slide.__hookCleanup = () => {
      splitInstances.forEach(s => s.revert());
      splitInstances = [];
    };
  },

  's-checkpoint-1': (slide, gsap) => {
    const scenario = slide.querySelector('.checkpoint-scenario');
    const question = slide.querySelector('.checkpoint-question');
    const reveal = slide.querySelector('.checkpoint-reveal');
    if (!scenario || !question || !reveal) return;

    let state = 0;
    const MAX = 2;

    gsap.to(scenario, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' });

    function advance() {
      if (state >= MAX) return false;
      state++;
      if (state === 1) {
        gsap.to(question, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' });
      }
      if (state === 2) {
        gsap.to(reveal, { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out' });
      }
      return true;
    }

    function retreat() {
      if (state <= 0) return false;
      const target = state === 2 ? reveal : question;
      gsap.to(target, { opacity: 0, y: 20, duration: 0.3 });
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
