Use one of these working mirrors or fallbacks. They are official or stable mirrors and include videos, notes, and downloads.

Primary OCW page (works now):
https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/
 
MIT OpenCourseWare

Open Learning Library copy (same course, free account optional; videos often load better from Brazil):
https://openlearninglibrary.mit.edu/courses/course-v1%3AOCW%2B6.042J%2B2T2019/about
 
openlearninglibrary.mit.edu

European OCW mirror (Croatia):
https://ocw.iti.hr/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/
 
ocw.iti.hr

Direct “Unit 1: Proofs” pages on international mirrors with MP4 downloads (use if the main page errors):
– Intro to Proofs hub (Ecuador mirror): https://mitocw.ups.edu.ec/.../tp1-1
 
mitocw.ups.edu.ec

– Part 1 video (Ecuador mirror): https://mitocw.ups.edu.ec/.../intro-to-proofs-part-1-video
 (has MP4 + SRT) 
mitocw.ups.edu.ec

– Same pages on the “aprende.org” mirror: https://opencw.aprende.org/.../tp1-1/
 
opencw.aprende.org

Full offline ZIP (desktop recommended). Download, unzip, then open index.html:
https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/download
 
MIT OpenCourseWare

If YouTube is easier, use these playlists or re-uploads (not official but complete):
– 2015 short-segment playlist referenced via bilibili: https://www.bilibili.com/video/BV1V741177d7/
 (description links to the YouTube list) 
bilibili.com

– 2010 long-lecture series (official OCW upload; excellent fallback): https://www.bilibili.com/video/BV1hq4y1W7w5/
 (desc links to YouTube playlist PLB7540DEDD482705B) 
 
 
 Module 1: Foundations of Mathematical Reasoning

Core goals: internalize axiomatic systems, proof logic, and classical geometry foundations.

A. Logic and Proof Theory

MIT 6.042J Mathematics for Computer Science (full OCW course):
▶ https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/

Focus: propositional logic, contraposition, contradiction, induction, invariants, set theory, relations.

Khan Academy — Proofs and Logic:
▶ https://www.khanacademy.org/math/geometry-home/geometry-foundations

Step-by-step drills on logical equivalence, contrapositives, and direct proofs.

Concept to master:
A statement P ⇒ Q is equivalent to ¬Q ⇒ ¬P (contrapositive).
Use in calculus: limit uniqueness proof — if limₓ→a f(x)=L₁ and L₂, assume L₁≠L₂, derive |L₁−L₂|<ε→contradiction.

B. Axioms → Theorems in Euclidean Geometry

Euclid’s Elements (Heath translation, public domain PDF):
▶ https://mathcs.clarku.edu/~djoyce/java/elements/

Gresham College Lecture “Here’s Looking at Euclid” by Robin Wilson (video):
▶ https://www.gresham.ac.uk/watch/euclids-elements

Axioms (Book I):

Draw a straight line between any two points.

Extend a finite straight line continuously.

Draw a circle with any center & radius.

All right angles are equal.

(Parallel Postulate) If a line intersects two others forming interior angles < 180°, the lines meet.

From these, prove congruence (I.4), parallels (I.29), and Pythagoras (I.47).

C. Archimedes and Exhaustion → Proto-Calculus

“The Method of Archimedes” (Gresham College lecture):
▶ https://www.gresham.ac.uk/watch/archimedes-method

MIT OCW 18.01 Single Variable Calculus — Week 1 (limits as areas):
▶ https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/

Example proof (Parabolic Segment):
Archimedes inscribes triangles under a curve; each new generation has 1/3 area of the last ⇒ infinite series

𝐴
=
𝑇
(
1
+
1
3
+
1
9
+
…
)
=
3
2
𝑇
.
A=T(1+
3
1
	​

+
9
1
	​

+…)=
2
3
	​

T.
This anticipates the integral 
∫
0
1
𝑥
2
𝑑
𝑥
=
1
3
.
∫
0
1
	​

x
2
dx=
3
1
	​

.

D. Limit Definition (ε–δ) and Continuity

3Blue1Brown – Epsilon Delta Visuals:
▶ https://www.3blue1brown.com/lessons/epsilon-delta

Professor Leonard Calculus 1 Lecture 6: Limits & Continuity:
▶ https://www.youtube.com/watch?v=JhE8KQgHLiw

Formal proof (for f(x)=x² at a):
Given ε>0, choose δ = min{1, ε/(2|a|+1)}.
Then if |x−a|<δ ⇒ |x²−a²|=|x−a||x+a| < ε.
This is the archetype of analysis reasoning.

Module 2: Calculus Core — Differentiation → Integration → Series

Primary course: MIT 18.01 + 3Blue1Brown visual series + Professor Leonard for worked proofs.

3Blue1Brown Playlist “Essence of Calculus”:
▶ https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr

MIT 18.01 videos and notes:
▶ https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/video-lectures/

Professor Leonard Calculus 1 & 2 series (YouTube, > 100 lectures):
▶ https://www.youtube.com/@ProfessorLeonard

Key proofs you’ll teach:

Derivative of xⁿ: limit of difference quotient → nxⁿ⁻¹ (by binomial expansion).

FTC: 
𝐹
(
𝑥
)
=
∫
𝑎
𝑥
𝑓
(
𝑡
)
 
𝑑
𝑡
⇒
𝐹
′
(
𝑥
)
=
𝑓
(
𝑥
)
F(x)=∫
a
x
	​

f(t)dt⇒F
′
(x)=f(x) via squeeze and mean-value theorem.

Taylor’s theorem: remainder 
𝑅
𝑛
(
𝑥
)
=
𝑓
(
𝑛
+
1
)
(
𝜉
)
(
𝑛
+
1
)
!
(
𝑥
−
𝑎
)
𝑛
+
1
R
n
	​

(x)=
(n+1)!
f
(n+1)
(ξ)
	​

(x−a)
n+1
.

Uniform convergence and termwise differentiation criteria.

Module 3: Probability & Inference

Harvard Stat 110 YouTube Full Course:
▶ https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo

MIT 6.041 Intro to Probability (OCW):
▶ https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/

Khan Academy Probability and Statistics:
▶ https://www.khanacademy.org/math/statistics-probability

Deep topics with derivations:

Kolmogorov axioms: 
𝑃
(
Ω
)
=
1
,
 
𝑃
(
𝐴
∪
𝐵
)
=
𝑃
(
𝐴
)
+
𝑃
(
𝐵
)
P(Ω)=1, P(A∪B)=P(A)+P(B) if disjoint.

Bayes theorem: derive from definition of conditional probability.

LLN and CLT: using characteristic functions: φₓ(t)=E[e^{itX}] → e^{−σ²t²/2}.

Expectation as integral: 
𝐸
[
𝑋
]
=
∫
𝑥
𝑓
(
𝑥
)
 
𝑑
𝑥
E[X]=∫xf(x)dx; variance via E[X²]−E[X]².

Module 4: Biostatistics and Applied Inference

Johns Hopkins Mathematical Biostatistics Boot Camp (Coursera):
▶ https://www.coursera.org/learn/biostatistics

Penn State STAT 504 (GEE and GLM tutorials):
▶ https://online.stat.psu.edu/stat504/

HarvardX PH525.1x Data Science and Biostatistics (EDX):
▶ https://online.hms.harvard.edu/course/data-science-biostatistics/

Analytic focus:

Likelihood & score equations 
𝑈
(
𝜃
)
=
∂
log
⁡
𝐿
/
∂
𝜃
U(θ)=∂logL/∂θ.

Fisher information 
𝐼
(
𝜃
)
=
𝐸
[
−
∂
2
log
⁡
𝐿
/
∂
𝜃
2
]
I(θ)=E[−∂
2
logL/∂θ
2
].

GLM derivation via canonical link & exponential family form.

Cox PH partial likelihood & score properties.

GEE vs. mixed models: marginal vs. conditional inference.

Module 5: Pedagogy — Teaching for Mathematicians

Harvard Derek Bok Center “Teaching Mathematics” seminars:
▶ https://bokcenter.harvard.edu/teaching-mathematics

MIT Open Learning Library “Teaching College-Level Science and Engineering”:
▶ https://openlearninglibrary.mit.edu/courses/course-v1:MITx+8.01F2016+type@spoc+block@SP

Book: Polya How to Solve It – teaches heuristics, questioning frameworks, and pattern recognition.
bilibili.com