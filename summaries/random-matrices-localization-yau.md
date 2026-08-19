---
title: "Random Matrices, Wigner–Dyson Universality, Localization and Beyond"
speaker: Horng-Tzer Yau (Harvard University)
source: https://www.youtube.com/watch?v=R_lDnWf9W3Y
video_id: R_lDnWf9W3Y
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: "none — companions: https://bookstore.ams.org/view?ProductCode=CLN/28 and https://arxiv.org/abs/2602.00975"
transcript: ../transcripts/R_lDnWf9W3Y_transcript.txt
difficulty_for_you: 2/5 (the physics and the objects) — 3/5 (the proof machinery)
reading_time: ~60 min
---

# Random Matrices, Universality, Localization and Beyond — Horng-Tzer Yau

**Field:** random matrix theory and mathematical physics. Specifically: the
localization–delocalization transition for random band matrices, and the spectral
statistics of random regular graphs.

**Difficulty against your background: 2 out of 5 for the physics and the objects,
3 out of 5 for the machinery.** This is one of the closest talks in the playlist to your
training and the header should say so plainly. The whole first third — Wigner's nuclei,
the semicircle law, level repulsion, Anderson's tight-binding model, universality classes,
a Schrödinger equation whose square modulus obeys a heat equation — is content you already
own under different names. Where the talk becomes genuinely new is the last third: a
hierarchy of coupled equations for traces of resolvents, closed by dropping terms, whose
truncation turns out to be **exactly solvable**. That closure is the whole 2024–2025
advance, and it gets the length.

So this tutorial is inverted in the way the spec describes. §3 is a calibration page you
can skim. The bridge (§4) is six definitions, not a chapter. §§5–7 — the walkthrough, the
central argument, and the exercises — are where the document lives.

**What this tutorial builds:** the dictionary between Anderson's coupling constant λ and a
band matrix's bandwidth W, and why it predicts a transition at W ≈ √N in one dimension;
what "complete delocalization" and "quantum unique ergodicity" mean as concrete ℓ^∞ and
ℓ² statements about eigenvectors; the three-step strategy and why it is a strange use of
dynamics; the G-loop, the loop hierarchy, and the primitive hierarchy that closes it; how
that closure produces a diffusion equation; and how a Tracy–Widom law turns into the
number 69%.

**A note on sources — read this one.** There is **no ICM 2026 proceedings paper for this
talk.** A sweep of arXiv found no preprint by Yau matching the lecture as a whole, and
nothing that covers both the band-matrix half and the regular-graph half.

What I used instead, in three visibly separate tiers:

- **Companion for the background half:** Erdős and Yau, *A Dynamical Approach to Random
  Matrix Theory*, Courant Lecture Notes 28, AMS (2017),
  [bookstore.ams.org/CLN/28](https://bookstore.ams.org/view?ProductCode=CLN/28). Yau's own
  book on the three-step strategy, the local semicircle law and Dyson Brownian motion —
  which is §§5.5–5.6 of this tutorial. **It predates every band-matrix result in the
  talk.** It is a companion, not the proceedings paper, and he does not name it from the
  podium.
- **Companion for the final section only:** Huang and Yau, *Lecture Notes on Edge
  Universality for Random Regular Graphs*,
  [arXiv:2602.00975](https://arxiv.org/abs/2602.00975), submitted 1 February 2026. My
  brief explicitly flagged this as *not* the proceedings paper — its comments field reads
  only "65 pages, 7 figures" and it makes no ICM reference — and asked me to decide from
  the transcript whether it is nevertheless a legitimate companion. **It is, for one
  section.** The talk devotes its last five minutes to random d-regular graphs, the
  Alon–Sarnak disagreement and the 69% figure, and Yau plugs the follow-up from the
  podium: "tomorrow Jiaoyang Huang will give a presentation of this." These notes are
  Yau's own exposition of exactly that result, co-written with exactly that speaker. So I
  label it a companion **for §5.9 and nothing else** — it covers perhaps 15% of the
  lecture and none of the band-matrix work.
- **Primary literature for the specific theorems**, which is not the same thing as a
  companion. Every rate, threshold and definition below that the auto-captions could not
  carry comes from the paper that proved it, named inline. The seven that matter are
  [arXiv:2501.01718](https://arxiv.org/abs/2501.01718) (one dimension),
  [arXiv:2503.07606](https://arxiv.org/abs/2503.07606) (two dimensions),
  [arXiv:2507.20274](https://arxiv.org/abs/2507.20274) (d ≥ 3),
  [arXiv:2412.20263](https://arxiv.org/abs/2412.20263) (the 69%),
  [arXiv:2508.05802](https://arxiv.org/abs/2508.05802) (the matching localization),
  [arXiv:2506.06441](https://arxiv.org/abs/2506.06441) (the non-Gaussian extension), and
  Erdős–Salmhofer–Yau, *Acta Mathematica* **200** (2008) 211–277 together with *Annales
  Henri Poincaré* **8** (2007) 621–685 (the twenty-year-old quantum diffusion result).

**The lecture's title.** The YouTube video is titled only "ICM 2026 Plenary Lecture -
Horng-Tzer Yau", and the ICM programme pages do not surface per-lecture titles. The title
in the front matter above is **his own, spoken from the podium** in the second minute:
"today I will talk about random matrices and Wigner[–Dyson] universality and localization
and beyond." I have not found an official printed title to check it against.

**Auto-captions and this talk.** They are bad even by the standards of this playlist. The
speaker's own name is rendered "HT H", "Yao" and "Dao"; "delocalization" is rendered
"deoization" and, four times, as its **opposite**, "localization"; "matrix Brownian
motion" becomes "magic brown emotions"; "BBGKY" becomes "BPGki" and then "musical"; the
martingale term becomes the "mole term". Three of these are meaning-inverting and I
correct them in the text and tabulate them in §11. Two names I could not verify and have
not guessed.

**Cross-references.** Otto's plenary (`geometric-concepts-pde-otto.md`) also derives
macroscopic behaviour from a noisy microscopic model, and also fights a divergent
perturbative expansion; where the comparison is instructive I point at it in §8.2 rather
than rewriting it.

---

## 1. What is at stake

Two questions, asked twenty-three years apart by two physicists who were not talking to
each other, which turned out to be the same question.

**Wigner, 1955.** You have a heavy nucleus — uranium, say. Fire neutrons at it and measure
the resonance energies. In principle those are eigenvalues of a many-body Schrödinger
operator with a few hundred strongly interacting nucleons, which nobody can write down,
let alone solve. Wigner's proposal was, in his own later phrase and Yau's from the podium,
"extremely bold" and "or you can call it crazy": *do not model the Hamiltonian at all.
Replace it by a random matrix.* Take an N×N matrix whose entries are independent random
numbers with the right symmetry, and predict that its eigenvalue **spacings** — not the
eigenvalues, the spacings — will match the measured resonance spacings.

It worked. And the striking part is not that it worked once. It is that the answer does
not depend on the distribution you chose for the entries. Yau's summary of Wigner's actual
claim: take any highly correlated system you do not understand, and in the large-system
limit its spectral statistics will be those of a random matrix. Only the **symmetry class**
survives — real symmetric or complex Hermitian. Everything else about the physics washes
out.

You already believe a version of this. It is a universality class, in exactly the sense of
critical phenomena, and the analogy is not decorative: the microscopic details are
irrelevant, the symmetry is not.

**Anderson, 1958.** You have a semiconductor with impurities. Model it as a discrete
Laplacian on ℤ^d plus a random on-site potential. Does an electron placed at the origin
spread out, or does it stay put? Anderson's answer, which won him the Nobel Prize, is that
for enough disorder it stays put — the eigenfunctions decay exponentially, the material is
an insulator. For weak disorder in three dimensions or more, it should spread — a
conductor. There is a phase transition between them.

**The connection, which took until about 1980 to see.** In the localized phase, the
eigenvalues do not repel each other; they behave like independent points, and the gap
statistics are **Poisson**. In the delocalized phase, the eigenvalues repel, and the gap
statistics are those of a **random matrix**. So Anderson's metal–insulator transition and
Wigner's universality are two faces of one object. The bridge between them is the **random
band matrix**, which Yau builds in §5.3: a matrix that is Wigner's when its bandwidth is
the full matrix size, and Anderson-like when its bandwidth is one.

**What was open until eighteen months ago.** For a one-dimensional band matrix of size N
and bandwidth W, physics predicted since 1991 that the transition sits at **W ≈ √N**.
Above it, delocalized and Wigner–Dyson. Below it, localized and Poisson. Yau's talk
reports that both halves are now proved: delocalization for W > N^{1/2+c} (Yau and Yin,
January 2025), and localization for W² ≪ N (Drogin, August 2025). The transition is
settled up to N^{ε}.

The tool that made the delocalization half possible is the actual content of the lecture,
and it is a closure of an infinite hierarchy — the same move you make when you close BBGKY
to get Boltzmann. Yau says so himself from the podium.

---

## 2. Your anchor, in the speaker's own words

The spec's best case is that the speaker hands you the anchor. He does, at minute 42,
while apologising for the complexity of an equation he declines to write down:

> "This is something similar to this BBGKY hierarchy in classical dynamics… you get the
> loop n will depend on loop n+1 and [the martingale] will depend on loop n+2, and the
> whole thing cannot be solved."

That is your kinetic theory, verbatim. The BBGKY hierarchy writes the evolution of the
1-particle distribution in terms of the 2-particle one, the 2 in terms of the 3, and so on
forever; the system is exact and useless. You close it by an ansatz — molecular chaos,
f₂ ≈ f₁⊗f₁ — and out drops the Boltzmann equation, and then a proof that the closure error
is small is the entire difficulty of the subject.

Yau's object is a hierarchy of traces of resolvents rather than particle correlations, and
his closure is "drop everything except the quadratic terms" rather than molecular chaos.
But the shape is identical, and so is the output: **the closed equation is a diffusion
equation.** Deriving a diffusion equation from a reversible microscopic dynamics, with
control on the closure error, is a hydrodynamic limit — which is the subject the introducer
credits Yau with founding, via the relative entropy method.

Three things you already own, then, and they cover the talk between them:

1. **Universality classes.** Microscopic detail irrelevant, symmetry class decisive. Same
   idea as critical exponents; here the "critical exponents" are the sine kernel and the
   Tracy–Widom law.
2. **Hydrodynamic limits.** Macroscopic PDE from microscopic stochastic dynamics. Quantum
   diffusion — |ψ_t|² solving a heat equation — is one, and the three-step strategy is the
   statement that local equilibrium is reached quickly.
3. **Hierarchy closure.** BBGKY and its truncation. This is the new mathematics of the
   talk, and it is the one you own most directly.

If you want a fourth, resist. The talk does not use one.

---

## 3. Calibration: what you can skip

Skim and go to §4. This exists only to fix notation and confirm we mean the same things.

**The random Schrödinger operator (Anderson, 1958).** On ℓ²(ℤ^d),

$$H = -\Delta + \lambda V,$$

where Δ is the discrete Laplacian (the kinetic energy) and V is a diagonal matrix of i.i.d.
random variables V(x) (the impurities). λ ≥ 0 is the coupling constant — the disorder
strength.

**Localized.** An eigenvector u is *localized with localization length ℓ* if it decays
exponentially away from some site x₀:

$$|u(x)| \lesssim e^{-|x-x_0|/\ell}.$$

If ℓ < ∞ the particle is trapped: insulator. If ℓ = ∞ it is not: conductor. Yau's captions
render "localization length" as "localization lens" throughout.

**The Anderson conjecture**, in the form he puts on the board:

| dimension | prediction |
|---|---|
| d = 1 | always localized, ℓ ~ λ^{−2} |
| d = 2 | always localized, ℓ ~ exp(cλ^{−2}) |
| d ≥ 3 | delocalized (ℓ = ∞) once λ is small enough |

The d = 2 entry is the one to notice: the localization length is *exponentially* large in
1/λ², so two dimensions is localized but only barely, and only asymptotically. Yau flags
this himself — "be careful, this is exponential."

Proof status, which he gives in one slide: d = 1 was done in the late 1970s; higher-d
localization at strong disorder is the famous multiscale analysis of Fröhlich and Spencer
(1983), later reproved by the fractional-moment method of Aizenman and Molchanov (1993);
Poisson statistics in the localized phase is Minami (1996). **Delocalization is proved
nowhere**, in any dimension, on ℤ^d. The only setting where it is known is the Bethe
lattice — an infinite regular tree — where the geometry is special.

**Wigner matrix.** H = (h_{ij}) is N×N Hermitian (or real symmetric) with independent
entries above the diagonal,

$$\mathbb{E}\, h_{ij} = 0, \qquad \mathbb{E}\,|h_{ij}|^2 = \frac{1}{N}.$$

The 1/N is a normalization that puts the spectrum in a fixed interval. If the entries are
real Gaussian this is the **Gaussian Orthogonal Ensemble** (GOE); complex Gaussian, the
**Gaussian Unitary Ensemble** (GUE); general distribution, a **Wigner ensemble**.

**Semicircle law** (Wigner). The empirical eigenvalue distribution converges to

$$\rho_{sc}(x) = \frac{1}{2\pi}\sqrt{4-x^2}\,\mathbf{1}_{[-2,2]}.$$

Yau's point about it: this is macroscopic and it is not what physics wanted. Physics wanted
the **gaps**.

**Local statistics.** In the bulk, N eigenvalues occupy an interval of length 4, so the
typical gap is of order 1/N. Rescale by N and the gap distribution has a limit — computed
by Gaudin and Mehta around 1960 and connected to a Painlevé transcendent by Jimbo, Miwa,
Môri and Sato (1980). At the spectral edge the scale is different: N^{−2/3}, and the limit
is the **Tracy–Widom** distribution (1993–94). Level repulsion — the vanishing of the gap
density at zero — is the visible signature.

**The Wigner–Dyson–Mehta conjecture.** Wigner's vision, restricted to the case where you
can actually ask a clean question: if you take a Wigner matrix with *non-Gaussian* entries,
are its local eigenvalue statistics the same as GOE's or GUE's, depending only on symmetry
class? Yau's own framing: "it is something like almost a central limit theorem" — the
distribution of a sum of random variables becomes Gaussian independently of the summands'
individual laws, and this is the same statement in the matrix setting.

**One piece of history worth keeping.** Yau tells it and it is not decoration. By about
1970 Dyson and his contemporaries had concluded that random matrix theory was "a beautiful
piece of pure mathematics having nothing to do with physics" and abandoned it. The reason,
as we now understand it, was that the nuclear data of the time was incomplete. The physics
was right and the evidence was not yet good enough to see it. Twenty years of the subject's
best people walked away from a correct theory because the measurements had gaps.

**Hydrodynamic limit.** You own this one; the sentence is here only to fix the phrase. A
microscopic stochastic particle system, rescaled in space and time, has a macroscopic
density that solves a PDE — typically diffusive. Yau's relative entropy method (1991) is
one of the standard routes to such theorems, and the introducer names it first among his
contributions.

That is the whole prerequisite for the physics. What follows is not standard.

---

## 4. The bridge: six things that are genuinely new

### 4.1 The random band matrix

This is the object the entire talk is about, and it is the interpolation between the two
stories in §1.

Stop labelling the matrix indices 1,…,N. Instead put them on a discrete torus
**ℤ_L^d** with N = L^d sites, so each index is a lattice site x. Fix a **bandwidth** W and
a profile function f, and set the variance of the entry connecting sites x and y to

$$S_{xy} := \mathbb{E}\,|h_{xy}|^2 = \frac{1}{W^{d}}\, f\!\left(\frac{x-y}{W}\right), \qquad S_{xy} = 0 \ \text{ if } |x-y| > W,$$

normalized so that ∑_y S_{xy} = 1 for every x.

Two limits:

- **W = L (in d = 1, so W = N).** Every entry has variance ≈ 1/N. This is exactly a Wigner
  matrix.
- **W = 1.** Only the diagonal and its immediate neighbours survive. This looks like the
  Anderson tight-binding model.

So a band matrix is a one-parameter family joining Wigner to Anderson, and W is the knob.
Yau credits **Wegner** with introducing the object, in the guise of the *orbital model*.
(The captions render both "Wigner" and "Wegner" as "wager"; the orbital model is Wegner's.)

Because the normalization is preserved, the semicircle law still holds for every W. The
macroscopic spectrum tells you nothing about the transition. Everything is in the local
statistics and the eigenvectors.

### 4.2 The dictionary λ ↔ 1/W, and the thresholds it predicts

Yau states the correspondence in one line: the Anderson coupling constant and the band
matrix bandwidth are related by

$$\lambda \;\longleftrightarrow\; W^{-1}.$$

Substituting into the Anderson table of §3 gives the band-matrix conjecture:

| dimension | localization length ℓ | transition at N = L^d |
|---|---|---|
| d = 1 | W² | W ≈ √N |
| d = 2 | exp(cW²) | W ≈ √(log N) |
| d ≥ 3 | ∞ | any W above a constant |

The d = 1 row is the famous one, and it is the one the talk closes. Its origin, on the
band-matrix side, is a supersymmetric-σ-model computation plus numerics; the standard
citation is Fyodorov and Mirlin, *Physical Review Letters* **67** (1991) 2405. *(Yau says
"supersymmetric method and numerics" from the podium without naming anyone; the attribution
is mine.)* On the Anderson side he credits the 1979 scaling theory of localization —
published by Abrahams, Anderson, Licciardello and Ramakrishnan, though he says only
"Anderson 1979" from the podium.

The transition condition is just "localization length ≳ system size": in d = 1, W² ≳ N.

### 4.3 Complete delocalization, as an inequality

"Delocalized" needs a quantitative form, and Yau gives the sharp one. Take an eigenvector u
normalized in ℓ², so ∑_x |u(x)|² = 1 over N sites. If the mass is spread evenly, each
|u(x)|² is about 1/N. So define:

$$\textbf{complete delocalization:}\qquad \|u\|_\infty^2 \;\le\; \frac{N^{\varepsilon}}{N} \quad\text{for every }\varepsilon>0,$$

with overwhelming probability, simultaneously for all eigenvectors. Equivalently
|u(x)| ≲ N^{−1/2+ε}. There is no room below this bound — an ℓ²-normalized vector on N sites
must have some coordinate at least N^{−1/2} — so it is not "spread out somewhat", it is
**as flat as an ℓ²-normalized vector can be**.

*(Caption correction: the transcript says "we also prove the complete **localization**…
[and] one way to say a vector is completely **localized** is that the ℓ^∞ norm squared is
less than 1/N up to N^ε." That is the definition of delocalization, and the inequality
proves it. The captions drop the "de-" repeatedly; see §11.)*

### 4.4 Quantum unique ergodicity, in the random-matrix sense

The name is borrowed. Rudnick and Sarnak's QUE conjecture concerns eigenfunctions of the
Laplacian on a compact negatively curved manifold: in the high-energy limit, |ψ|² should
become **flat** — equidistributed with respect to the volume measure. It is a statement
that a quantum system inherits the ergodicity of its classical counterpart.

Yau's version, proved for Wigner matrices with Bourgade and now for band matrices, is a
probabilistic analogue. Let E_A be the diagonal projection onto a deterministic subset A of
the index set, with |A| sites. Then for eigenvectors u_i, u_j,

$$\langle u_i, E_A u_j\rangle \;\approx\; \frac{|A|}{N}\,\delta_{ij},$$

with high probability. Read the two cases separately:

- **i = j:** the ℓ² mass of a single eigenvector inside any region A is proportional to the
  size of A. That is flatness — the manifold statement, transplanted.
- **i ≠ j:** two different eigenvectors, restricted to A and rescaled, remain
  *orthogonal*. This is what Yau means from the podium by "these two eigenvectors are still
  also orthonormal". It is strictly stronger than flatness of each one, and it is the part
  that does the work in §5.6.

The mnemonic to keep: **delocalization is an ℓ^∞ statement about one eigenvector; QUE is an
ℓ² statement about pairs of them on arbitrary sets.** QUE implies delocalization; the
converse is false and the gap between them is exactly what made band matrices hard.

### 4.5 The Green's function and the local law

$$G(z) := (H - z)^{-1}, \qquad z = E + i\eta, \quad \eta > 0,$$

and its normalized trace

$$m_N(z) := \frac{1}{N}\operatorname{Tr} G(z) = \frac{1}{N}\sum_{i=1}^N \frac{1}{\lambda_i - z}.$$

m_N is the Stieltjes transform of the empirical eigenvalue measure. The imaginary part η is
a **resolution**: Im G(E+iη) is the eigenvalue density smoothed on scale η. So the whole
game is to push η down.

The **local semicircle law** says m_N(z) is close to m_sc(z), the Stieltjes transform of the
semicircle law, for every η ≫ 1/N. And 1/N is not an artefact — it is the mean eigenvalue
spacing. Yau explains the choice from the podium: "when η becomes smaller and smaller you
are closer and closer to each individual eigenvalue, and each individual spacing is 1/N, so
you want η to be close to 1/N." Below that scale you would be resolving individual
eigenvalues and no deterministic law can hold.

m_sc satisfies a self-consistent equation you will derive in §7 as a warm-up:

$$m_{sc}(z) = \frac{1}{-z - m_{sc}(z)} \quad\Longleftrightarrow\quad m_{sc}^2 + z\,m_{sc} + 1 = 0, \qquad m_{sc}(z) = \frac{-z+\sqrt{z^2-4}}{2}.$$

The one fact to carry forward: for E strictly inside (−2,2) and η → 0, **|m_sc(E)| = 1**.
It will supply the small parameter in §6.

> *[Gap: the precise form of the local law — the error bound as a function of η and N, the
> constants, and the domain of z — was on the slide. The captions carry only "close to the
> semicircle law" and "η bigger than 1/N". The statement is Theorem 2.1 of the companion
> book (Erdős–Yau, CLN 28) for Wigner matrices, and Theorem 2.2 of arXiv:2501.01718 in the
> band case. Low impact: the shape carries the argument and the shape is stated.]*

### 4.6 Matrix Brownian motion

The dynamics that drives the whole proof strategy. Let the matrix entries perform
independent Brownian motions consistent with the symmetry:

$$dH_t = \frac{1}{\sqrt N}\,dB_t,$$

with B a matrix of standard Brownian motions (real or complex according to the symmetry
class). Then, in distribution,

$$H_t \;=\; H_0 + \sqrt{t}\cdot \text{GUE}.$$

Yau notes you can equally run an Ornstein–Uhlenbeck version that preserves the variance;
the choice does not matter. What matters is the reading:

> **H_t is your initial data plus a Gaussian noise of size √t.**

He pauses on this because of who is in the room: "this object also has a meaning in data
science — it talks about, if you take data which is H₀ and you add some noise, what is its
behaviour." Yes. It is exactly your denoising setup, and the theorem in §5.5 says something
strange about it.

The induced motion of the eigenvalues is **Dyson Brownian motion**: N particles on a line,
each doing Brownian motion, repelling each other with a 1/(λ_i − λ_j) force. The eigenvalues
are an interacting particle system. That is your statistical mechanics, and its equilibrium
measure is the GOE/GUE eigenvalue law.

---

## 5. The talk, rebuilt

I follow his order. He gave it as: Anderson → Wigner → the connection → band matrices →
quantum diffusion (old) → the three-step strategy → the new theorems → the loop hierarchy →
regular graphs → open problems.

### 5.1 Anderson, and where the proofs stop

Covered in §3 above. The line to carry into the rest of the talk is his summary of the
delocalized side:

> "Continuing with delocalization — there is not much result in [this] century, almost
> nothing, except on the Bethe lattice, which is a tree."

That is the state of the art on ℤ^d as of this lecture. **Nobody has proved delocalization
for the Anderson model in any dimension on a lattice.** The band matrix is the tractable
surrogate, and that is why the talk is about band matrices.

*(The Bethe-lattice attribution in the captions — "emana and ego" — I could not resolve.
The known results there are Klein (1998), on absolutely continuous spectrum for the
Anderson model on a regular tree at weak disorder, and Aizenman–Warzel. I name them as the
literature rather than as what he said; see §11.)*

### 5.2 Wigner, and the solution of the Wigner–Dyson–Mehta conjecture

Covered in §3 through the statement of the conjecture. The resolution is Yau's own, and he
gives it in two sentences and one slide:

> **Theorem (Erdős, Schlein, Yau, Yin, and independently in part Tao–Vu; roughly
> 2007–2012).** Bulk universality holds for Wigner matrices provided the matrix entries
> have bounded **2+ε moments**. Complete delocalization and probabilistic quantum unique
> ergodicity hold for all Wigner matrices.

Two footnotes he adds from the podium:

- The 2+ε moment condition can be pushed to **1+ε**. *(He names two collaborators; the
  captions render them "piggoa and lao" and I could not verify the sounds. The result I
  believe he means is Aggarwal, Lopatto and Yau, "GOE statistics for Lévy matrices",
  [arXiv:1806.07363](https://arxiv.org/abs/1806.07363), JEMS 2021 — α-stable entries with
  α ∈ (1,2) have exactly 1+ε moments and infinite variance, which is precisely the
  weakening described. **This identification is my reconstruction, not a verified reading
  of the captions**; see §11.)*
- Tao and Vu obtained a partial result under a **four-moment matching condition** — the
  entries must agree with a Gaussian in their first four moments — which he describes as
  partial progress on the same problem. (Captions: "territo and bamboo".)

The Steele Prize the introducer mentions is for this body of work. I have not verified the
introducer's award list and it is not talk content.

### 5.3 The connection, and the band matrix

Covered in §4.1–4.2. The historical claim worth repeating is his: **Wegner is the person who
built the bridge**, by introducing the orbital model, and the identification "Poisson ↔
localized, random-matrix ↔ delocalized" emerged in the early 1980s. Before that, the
semiconductor story and the neutron-scattering story were unrelated subjects.

### 5.4 Quantum diffusion, first attempt: perturbation theory, and the wall

Now the result from twenty years ago, and the reason it stalled.

**The statement.** Solve the Schrödinger equation with the Anderson Hamiltonian,

$$i\,\partial_t \psi = (-\Delta + \lambda V)\psi.$$

Quantum mechanics says the observable is |ψ_t(x)|². The conjecture is that this quantity,
suitably rescaled, solves a **heat equation**. Yau on how odd this is: "you take a
Schrödinger equation, with an *i* in it, and after you solve it you take the absolute value
squared and it becomes a diffusion equation."

It is odd, and it is the same oddness as any hydrodynamic limit: a time-reversible
microscopic evolution producing an irreversible macroscopic one. The reversibility is not
violated; it is buried in the fact that we averaged over the disorder and looked at a
squared amplitude.

**What was proved.** Erdős, Salmhofer and Yau, in the continuum (*Acta Mathematica* **200**
(2008) 211–277) and on the lattice ℤ^d (*Annales Henri Poincaré* **8** (2007) 621–685): in
dimension **d ≥ 3**, in the weak coupling limit λ → 0, with space and time rescaled as

$$x \sim \lambda^{-2-\kappa/2}, \qquad t \sim \lambda^{-2-\kappa}, \qquad 0 < \kappa < \kappa_0(d),$$

the expected Wigner distribution of ψ_t converges weakly to a solution of a heat equation
in x, for arbitrary L² initial data.

Read the exponent. The **kinetic** time scale — the mean free time between collisions with
impurities, by Fermi's golden rule — is λ^{−2}. The theorem reaches λ^{−2−κ} for a small
κ: **a few collisions past the first one**, which is exactly where a Boltzmann-type
description first becomes meaningful and exactly where the perturbative series first starts
to bite. It is a hard-won small step past the kinetic scale, not a result at the diffusive
scale.

**Why it stopped there.** The proof expands the resolvent (H₀ + λV − z)^{−1} in powers of
λV and controls the resulting sum. Because the time is long, the expansion must be carried
to very high order, and the terms are Feynman graphs. Yau's own account:

> "It's hundreds of graph computations and the classification is really a total nightmare…
> after this paper, we really didn't have the courage to continue. It was just so
> complicated."

So the group left the Anderson model and went to Wigner matrices instead — which is how
§5.2 happened. That detour lasted five or six years, produced the solution of the
Wigner–Dyson–Mehta conjecture, and then came back.

This is worth registering as a fact about how the subject moved: **the flagship theorem of
random matrix universality was a detour taken because a different problem was too hard.**

### 5.5 The three-step strategy, and why it is a strange use of dynamics

Yau's method for universality, and the content of the companion book. Three steps:

1. **A priori local law.** Prove a Green's function estimate for the initial matrix H₀ —
   the local semicircle law of §4.5, valid down to η ≫ 1/N.
2. **Universality after a small Gaussian noise.** For H_t = H₀ + √t·GUE, show that for
   t ≳ N^{−1+ε} the local eigenvalue statistics of H_t are exactly those of GUE/GOE. This
   is **Dyson's conjecture** — that Dyson Brownian motion reaches local equilibrium at time
   N^{−1} — and it is a theorem. (For the fixed-energy form: Landon, Sosoe and Yau, *Adv.
   Math.* **346** (2019) 1137–1332,
   [arXiv:1609.09011](https://arxiv.org/abs/1609.09011).) The hypothesis it needs on H₀ is
   supplied by step 1.
3. **Comparison.** Show that the local statistics of H_t agree with those of H₀ for
   t ≲ N^{−1/2}.

Now look at what the sandwich does. Choose t between N^{−1} and N^{−1/2} — both windows are
open at once. Step 2 says H_t has GUE statistics. Step 3 says H_t has H₀'s statistics.
Therefore **H₀ already had GUE statistics.**

Yau flags the strangeness explicitly and it is worth quoting because it is the reusable
part:

> "This is a very strange way of using dynamics. Typically we prove something by dynamics
> by flowing something into the ergodic theorem, into your solution, and we're very happy.
> But this idea is using dynamics to show the **initial data is already** the same as at
> time infinity."

Restated: you prove an ergodic theorem for a huge class of initial data, you show your
particular object is a member of that class *and* that it barely moves over the relevant
horizon, and you conclude it was sitting at equilibrium the whole time. The dynamics is a
measuring device, not a construction. §8.1 turns this into a method.

And note where the second step's hypothesis comes from: the class of admissible initial
data is defined by an *estimate* (the local law), not by a formula. That is what makes the
huge-class ergodic theorem provable.

> *[Gap: the mechanism of step 3 — how one actually compares the statistics of H₀ and H_t —
> is never given. He says "I will explain this later on in a minute" and does not return to
> it in the captions. The standard tool is the Green function comparison theorem
> (Erdős–Yau–Yin), a Lindeberg-type entry-by-entry swap. Moderate impact: step 3 is exactly
> the step that fails for band matrices, so the reader is told what breaks without being
> told what it is.]*

### 5.6 Why the strategy breaks for band matrices, and what fixes it

Two of the three steps get harder, and Yau names both:

- **Step 1** — the local law — is much harder for band matrices, because the variance
  profile is not constant.
- **Step 3** — the comparison — is the real obstruction, and the reason is structural.
  Comparison "requires the matrix to be quite fat", in his words: mean-field, with its
  variance spread over all N entries of a row. A band matrix has all its variance
  concentrated in W entries near the diagonal. **The mean-field structure that the whole
  comparison argument silently used is absent.**

He says this blocked the problem "for a long time". Then:

> **The observation that unblocks it: if you first prove that the eigenvectors are flat,
> the comparison goes through.**

More precisely, it is probabilistic QUE (§4.4) that is needed, not merely delocalization —
the pairwise, arbitrary-set statement. The logic then runs downhill:

$$\textbf{quantum diffusion}\;\Longrightarrow\;\textbf{QUE}\;\Longrightarrow\;\textbf{step 3 works}\;\Longrightarrow\;\textbf{bulk universality}.$$

That chain is the architecture of the whole talk, and §6 states it precisely.

Note what happened logically. The obstruction was "my object is not uniform enough for the
comparison to see it". The fix was not to weaken the comparison. It was to **prove a
stronger structural statement about the object first**, and hand the comparison what it
needed. That is a transferable move and §8.3 says so.

### 5.7 The theorems

> **Theorem (band matrix delocalization).** Let H be an N×N Hermitian random band matrix
> with complex Gaussian entries, indices on the discrete torus ℤ_L^d, N = L^d, bandwidth W
> and normalized variance profile as in §4.1. Suppose:
>
> - **d = 1:** W ≥ N^{1/2 + c} for some c > 0 — Yau and Yin,
>   [arXiv:2501.01718](https://arxiv.org/abs/2501.01718) (January 2025);
> - **d = 2:** W ≥ N^{c} for some c > 0 — Dubova, Kevin Yang, Yau and Yin,
>   [arXiv:2503.07606](https://arxiv.org/abs/2503.07606) (March 2025);
> - **d ≥ 3:** W ≥ N^{c} for some c > 0 — Dubova, Fan Yang, Yau and Yin,
>   [arXiv:2507.20274](https://arxiv.org/abs/2507.20274) (July 2025).
>
> Then, in the bulk of the spectrum and as N → ∞: the local semicircle law holds down to
> scale N^{−1+ε}; **all** eigenvectors are completely delocalized; probabilistic quantum
> unique ergodicity holds; the local eigenvalue statistics are those of GUE; and the
> quantum diffusion profile holds.

Yau's own summary: "essentially everything we were hoping to prove for the band matrix was
proved."

**Two honest caveats he states himself.**

1. **d = 2 is not sharp.** The conjecture says the threshold is W ≈ √(log N); the theorem
   proves W ≥ N^ε. That is an enormous gap in absolute terms — a power of N versus a power
   of a logarithm — even though both are "small". He says plainly: "you really want to do
   √(log N), but we only do N^ε. So there's something major one has to do."
2. **The entries are complex Gaussian.** This is a genuine restriction, removed
   independently: Erdős and Riabov, "The Zigzag Strategy for Random Band Matrices"
   ([arXiv:2506.06441](https://arxiv.org/abs/2506.06441), June 2025), prove delocalization,
   Wigner–Dyson statistics and QUE for W ≫ √N in one dimension for **general variance
   profiles, arbitrary entry distributions, and both symmetry classes**.

**And the matching lower half.** Yau credits **Drogin** (captions: "the dragon") with the
localization side:

> **Theorem (Drogin, [arXiv:2508.05802](https://arxiv.org/abs/2508.05802), August 2025).**
> For a general class of one-dimensional random band matrices with W² ≪ N, the eigenvectors
> are localized, with exponential decay at the sharp scale W².

*(Caption correction: the transcript reads "for W ≤ √N is **delocalized**". It must be
localized — otherwise there is no transition to prove. See §11.)*

Put the two together:

> **The one-dimensional localization–delocalization transition for random band matrices is
> now proved, at W = √N, up to N^{ε}.** A conjecture from 1991, closed in seven months of
> 2025, from opposite directions by different groups.

### 5.8 Quantum diffusion, second attempt: the loop hierarchy

Here is the new mathematics, and it is the reason the theorems above exist.

**The object.** Let E_a be the diagonal projection onto the block of indices at site a of
the torus. Define the **n-point G-loop**: for signs σ = (σ_1,…,σ_n) ∈ {+,−}^n and sites
a = (a_1,…,a_n),

$$\mathcal{L}_{t,\boldsymbol\sigma,\mathbf{a}} \;=\; \operatorname{Tr}\!\left[\prod_{i=1}^n G_t(\sigma_i)\, E_{a_i}\right],$$

where G(+) = G(z) = (H_t − z)^{−1} and G(−) = G(z̄) = G(z)^†. (Definition 2.9 and equation
(2.41) of [arXiv:2501.01718](https://arxiv.org/abs/2501.01718).)

It is a chain of resolvents alternately projected onto lattice sites, closed into a loop by
the trace — hence the name. The case that matters is **n = 2 with σ = (+,−)**:

$$\mathcal{L}_2 = \operatorname{Tr}\big[G(z)\,E_a\,G(z)^{\dagger}\,E_b\big] \;=\; \sum_{x \in a,\; y \in b} |G_{xy}(z)|^2 .$$

That is the average squared modulus of the Green's function between site a and site b —
the quantity whose diffusive behaviour *is* quantum diffusion.

**The dynamics.** Now let H_t run under matrix Brownian motion (§4.6) and apply Itô's rule
to L_n. Because G_t = (H_t − z)^{−1} depends on H_t, differentiating produces, in Yau's
words, "an extremely complicated expression" which he declines to write down. Its structure
has exactly three kinds of term:

$$d\mathcal{L}_n \;=\; \underbrace{\Big[\textstyle\sum \mathcal{L}_{k}\,S\,\mathcal{L}_{l}\Big]dt}_{\text{quadratic, } k+l \le n+\ldots}\;+\;\underbrace{\big[\ \cdot\ \mathcal{L}_{n+1}\ \big]dt}_{\text{one loop higher}}\;+\;\underbrace{d\mathcal{M}_n}_{\text{martingale}} .$$

(Schematic; the exact equation is Lemma 2.11, equation (2.45) of the same paper, where the
quadratic term carries an explicit factor W and the variance kernel S^{(B)}.) And the
martingale is no relief: computing its quadratic variation brings in a loop of order 2n+2.

**This is BBGKY.** L_n is driven by L_{n+1}; the noise is driven by something higher still;
the system never closes. Yau says so: "similar to the BBGKY hierarchy in classical
dynamics… the whole thing cannot be solved." (He also notes that another lecture at this
congress, the previous day, had discussed the trouble with BBGKY in classical dynamics. I
have not identified which and do not name it.)

**The closure.** Usually one truncates. Here the truncation is brutally simple:

> **Drop the L_{n+1} term. Drop the martingale. Keep only the quadratic terms.**

Call the solution of the resulting system K_n — the **primitive loops** — and the system
itself the **primitive hierarchy** (Definition 2.12, equation (2.48) of arXiv:2501.01718),
with initial condition K_{0,σ,a} = W^{−n+1}·∏_k m(σ_k)·**1**(a_1 = ⋯ = a_n).

And here is the payoff, which is the sentence Yau most wants you to leave with:

> **The primitive hierarchy can be solved exactly.**

Why it closes: the surviving quadratic term for K_n is a convolution of K_l's with l ≤ n.
So the system is *triangular* — K_1 first, then K_2 in terms of K_1, then K_3, and so on.
Each is an explicit computation. In particular K_2, the object of interest, has a closed
form.

Yau's framing of what this is: **"a new class of integrable fixed points."** Not a
perturbative approximation with an error series, but an exactly solvable model that happens
to sit next to the true dynamics.

**And then the work.** The claim is L_2 ≈ K_2, which gives quantum diffusion. But — and he
stresses this twice —

> "In order to show L_2 is close to K_2, you have to show that L_n is close to K_n **for
> all n**."

The dropped terms have to be error terms, uniformly in the hierarchy. That is where the 86
pages go.

**What replaced what.** The old proof (§5.4) expanded the resolvent in powers of λV and
classified Feynman graphs. The new one does not expand at all. Yau's closing assessment:

> "This idea [the expansion] completely disappears in the random band matrix case. We no
> longer do expansion; instead we use this loop hierarchy… If you were trained in physics
> you know that for the last century a lot of physics completely depended on perturbation
> theory. But what we find is, this primitive hierarchy is actually a new class of
> integrable fixed points."

That is a claim about method, made deliberately, at a plenary lecture. §8.2 takes it
seriously.

### 5.9 Random regular graphs, the Alon–Sarnak disagreement, and 69%

The last five minutes, and a different subject with the same toolkit. This is the section
for which Huang and Yau's lecture notes ([arXiv:2602.00975](https://arxiv.org/abs/2602.00975))
are the companion.

**The setup.** Pick a simple d-regular graph on N vertices uniformly at random, d ≥ 3
fixed. Let A be its adjacency matrix and normalize:

$$H := \frac{A}{\sqrt{d-1}}, \qquad \lambda_1 = \frac{d}{\sqrt{d-1}} \ge \lambda_2 \ge \cdots \ge \lambda_N.$$

λ₁ is deterministic (Perron–Frobenius, every vertex has degree d). The empirical
distribution of the rest converges to the **Kesten–McKay law**, the spectral measure of the
infinite d-regular tree:

$$\rho_d(x) = \mathbf{1}_{[-2,2]}\,\frac{1}{2\pi}\left(1 + \frac{1}{d-1} - \frac{x^2}{d}\right)^{-1}\sqrt{4-x^2}\,,$$

as written in equation (1.2) of [arXiv:2412.20263](https://arxiv.org/abs/2412.20263). It has
the same square-root edge behaviour as the semicircle law, with amplitude
A = d(d−1)/(d−2)².

**Ramanujan.** Lubotzky, Phillips and Sarnak called a d-regular graph *Ramanujan* if every
non-trivial eigenvalue lies in [−2, 2] — i.e. max{λ₂, |λ_N|} ≤ 2. The **Alon–Boppana**
bound says you cannot do better: for any infinite family, λ₂ ≥ 2 − o(1). So Ramanujan means
*optimal expander*, and 2 is the spectral radius of the adjacency operator on the infinite
tree.

Constructions: Lubotzky–Phillips–Sarnak and, independently, Margulis built infinite
families — but only for d−1 a prime (later, a prime power), and by algebraic means (Cayley
graphs). Marcus, Spielman and Srivastava settled the **bipartite** case for every d ≥ 3
using interlacing families of expected characteristic polynomials. The non-bipartite
existence question for general d stayed open.

**The disagreement.** Yau describes it as "the famous debate between Noga Alon and Peter
Sarnak", and the positions are:

- **Alon:** almost *all* random d-regular graphs are Ramanujan. Random objects usually have
  optimal properties.
- **Sarnak:** almost *none* are. Optimal expanders are rare and need number theory to build.

Alon's published conjecture — that random regular graphs are *almost* Ramanujan,
λ₂ ≤ 2 + o(1) — was proved by Friedman (2008), with later proofs by Bordenave and by
Chen–Garza-Vargas–Tropp–van Handel. That settles "almost". It does not settle the actual
question, which is about the sign of a vanishing quantity.

**The answer.**

> **Theorem (Huang, McKenzie and Yau, [arXiv:2412.20263](https://arxiv.org/abs/2412.20263),
> December 2024).** Fix d ≥ 3. Then
>
> $$(AN)^{2/3}(\lambda_2 - 2) \;\Longrightarrow\; \mathrm{TW}_1, \qquad A = \frac{d(d-1)}{(d-2)^2},$$
>
> the Tracy–Widom distribution of the GOE, with the analogous statement for −λ_N; and the
> two limits are **independent**. All eigenvalues are optimally rigid: bulk fluctuations
> N^{−1+o(1)}, edge fluctuations N^{−2/3+o(1)}.
>
> **Corollary 1.3.** For N large, approximately **69%** of d-regular graphs on N vertices
> are Ramanujan.

The arithmetic is three lines and you will do it in §7.2. TW₁ places about **83%** of its
mass on the negative half-line. λ₂ ≤ 2 is the event that its rescaled version is negative:
probability 0.83. Same for λ_N. Independent: 0.83² ≈ 0.69.

**Why 69% is the interesting number.** Not because of its value but because it is strictly
between 0 and 1. A probability that converges to a constant in (0,1) is invisible to every
standard tool of the probabilistic method: no concentration inequality can produce it, no
first- or second-moment argument, no union bound. You must know the **limiting
distribution**, exactly, which is why edge universality was the thing that had to be proved.
The paper's own remark is that this rules out the usual proof techniques.

It also settles the existence question that had been open since 1988: since 69% > 0, non-bipartite
Ramanujan graphs of every degree d ≥ 3 exist in infinite families.

**Who won the bet.** Neither. Alon's "almost all" is wrong; Sarnak's "almost none" is more
wrong. Alon's own comment, reported by *Quanta*: "Both of us were somewhat wrong. Still, I
was a little bit more correct, because the probability is bigger than half."

### 5.10 What he says is still open

He lists these in the last ninety seconds, and I keep his order.

1. **The d = 2 threshold.** Get from W ≥ N^ε to the conjectured W ≈ √(log N). He calls this
   "something major one has to do."
2. **Localization for the Anderson model.** He names this as "one key problem we cannot
   do". The captions are ambiguous about which half he means, and both halves are genuinely
   open, so I state both rather than guess: localization for weak disorder in **d = 2** is
   not proved, and **delocalization for weak disorder in d ≥ 3** is not proved in any
   dimension on ℤ^d. The band matrix results do not transfer, because the band matrix has
   randomness in W entries per row while the Anderson model has one.
3. **Many-body versions.** "We also don't know if there is any many-body system you can do
   that [for]." Open even to formulate cleanly.
4. **Band matrix plus Laplacian** — i.e. the block Anderson and Wegner orbital models. These
   are partially reached already: the d ≥ 3 paper
   ([arXiv:2507.20274](https://arxiv.org/abs/2507.20274)) treats them and locates the
   transition at coupling g = W^{−d/2}.
5. **The spectral edge**, as opposed to the bulk, for band matrices.
6. **Nonlinear settings**, where he explicitly names **artificial neural networks** as a
   place random matrices appear.

---

## 6. The one argument

The central claim of the lecture is not a single theorem but a chain, and stating the chain
precisely is the most useful thing this tutorial can do.

> **The architecture.**
>
> $$\text{primitive hierarchy solved exactly} \;\Rightarrow\; \mathcal{L}_2 \approx \mathcal{K}_2 \;\Rightarrow\; \textbf{quantum diffusion} \;\Rightarrow\; \textbf{QUE} \;\Rightarrow\; \text{step 3 of the three-step strategy} \;\Rightarrow\; \textbf{bulk universality}.$$

Every arrow is a theorem; the first is where the new idea lives. Take the middle link and
state it exactly.

**Quantum diffusion, precisely.** From Theorem 2.4, equations (2.8)–(2.9) of
[arXiv:2501.01718](https://arxiv.org/abs/2501.01718):

$$\max_{a,b}\left|\ \mathbb{E}\operatorname{Tr}\big[G E_a G^{\dagger} E_b\big] \;-\; \frac{1}{W}\left(\frac{|m|^2}{1 - |m|^2 S^{(B)}}\right)_{ab}\right| \;\le\; (W\ell\eta)^{-3}\,W^{\tau},$$

where m = m_sc(z) is the semicircle Stieltjes transform of §4.5 and S^{(B)} is the block
variance kernel of §4.1 — a symmetric stochastic matrix on the torus, i.e. **the transition
matrix of a random walk with step size W**.

**Now read the right-hand side.** Split the denominator:

$$1 - |m|^2 S^{(B)} \;=\; \underbrace{\big(1 - |m|^2\big)}_{\text{scalar}} \;+\; \underbrace{|m|^2\big(1 - S^{(B)}\big)}_{\text{operator}}.$$

Two facts finish it.

- In the bulk, |m_sc(E)| = 1 exactly when η = 0 (§4.5), so for small η, 1 − |m|² ≈ cη for a
  constant c depending on E.
- 1 − S^{(B)} is one minus a random-walk transition kernel. That is, by definition, the
  **generator of that random walk** — a discrete Laplacian. At long wavelengths
  1 − S^{(B)} ≈ −D·Δ with diffusion constant D ~ W², because the walk takes steps of size
  W.

So

$$\frac{|m|^2}{1-|m|^2 S^{(B)}} \;\approx\; \frac{1}{c\,\eta \;+\; D(-\Delta)} \;=\; \int_0^\infty e^{-c\eta t}\, e^{tD\Delta}\, dt .$$

**That is the resolvent of the heat semigroup.** The average of |G_{xy}(E+iη)|² is, up to
normalization, the Laplace transform in time of a diffusion kernel — which is exactly what
Yau states from the podium: "the Green's function absolute value squared becomes a random
walk… it's one over [η] minus the Laplace operator, and η is 1/N."

*Marked: the split of the denominator and its reading as a heat-semigroup resolvent is my
algebra, not the paper's presentation and not in the captions. The formula being read is
verbatim Theorem 2.4 of arXiv:2501.01718. What would verify it: the propagator estimates in
§3 of that paper, where the operator (1 − |m|²S^{(B)})^{−1} is analysed directly.*

**And now the threshold falls out.** η ≈ 1/N is a resolution in energy, and by the Laplace
transform above it is a **time horizon** t ≈ η^{−1} ≈ N. In that time a random walk with
diffusion constant W² spreads a distance √(W²·N) = W√N. Delocalization requires the walk to
cover the whole torus, of linear size L. In d = 1, L = N, so we need

$$W\sqrt{N} \;\gtrsim\; N \quad\Longleftrightarrow\quad W \gtrsim \sqrt{N}.$$

**The conjectured threshold is a statement about how far a diffusion travels before the
clock runs out.** You will redo this in §7.1, including the d = 2 case, where the same
computation shows the naive obstruction disappears — which is why two dimensions is
marginal and why its true threshold is only logarithmic.

---

## 7. Do this by hand

Two exercises. The first is the mechanism of the whole talk; the second is the number
everybody will remember from it.

### 7.1 Where √N comes from (25 minutes, pen)

Work in the band-matrix setting of §4.1: torus ℤ_L^d, N = L^d, bandwidth W, and take the
quantum-diffusion formula of §6 as given:

$$\mathbb{E}\operatorname{Tr}\big[G E_a G^\dagger E_b\big] \;\approx\; \frac{1}{W}\left(\frac{|m|^2}{1-|m|^2 S^{(B)}}\right)_{ab},\qquad z = E+i\eta .$$

1. Show that m = m_sc(z) satisfies m² + zm + 1 = 0, from the self-consistent equation
   m = 1/(−z − m). Deduce m_sc(z) = (−z + √(z²−4))/2 and verify that **|m_sc(E)| = 1** for
   E ∈ (−2,2) and η → 0. *(Hint: for real E in (−2,2), z²−4 < 0 so the square root is
   purely imaginary; compute |m|².)*
2. Conclude that 1 − |m|² = cη + O(η²), and identify c in terms of Im m_sc(E).
3. S^{(B)} is a symmetric stochastic matrix on the torus with range W. Argue that
   1 − S^{(B)}, acting on slowly varying functions, is approximately −DΔ, and that D ~ W².
   *(Hint: expand a smooth function to second order around x and use that the profile has
   variance ~ W².)*
4. Take the Laplace-transform reading of §6 and identify the time horizon corresponding to
   η. Set η = 1/N.
5. In d = 1 (so L = N), find the condition on W for a diffusion with constant D ~ W² to
   travel the linear size of the system within that horizon.
6. Repeat step 5 in d = 2 (so L = √N). What do you find, and what does it tell you about
   why the true two-dimensional threshold is only √(log N)?

<details>
<summary>Solution</summary>

**1.** The self-consistent equation is m(−z − m) = 1, i.e. m² + zm + 1 = 0, so
m = (−z ± √(z²−4))/2; the branch with Im m > 0 for Im z > 0 is the one with the +.
For real E ∈ (−2,2), E²−4 < 0, so √(E²−4) = i√(4−E²) and

m_sc(E) = (−E + i√(4−E²))/2, hence |m_sc(E)|² = (E² + 4 − E²)/4 = **1**.

Notice this is exactly the statement that the semicircle density is supported on [−2,2] and
non-zero inside — |m| = 1 is a property of the bulk, and it fails at the edge and outside.

**2.** Write z = E + iη. Differentiating the quadratic, or expanding m(E+iη) = m(E) + iη m′(E)
+ …, gives |m|² = 1 − cη + O(η²) with c = 2 Im(m′)… more simply: from m² + zm + 1 = 0 one
gets m′ = −m/(2m + z) = m/(m − 1/m) using z = −m − 1/m, and a short computation gives
1 − |m|² = cη with c = 2 Im m_sc(E)/√(4−E²) > 0 in the bulk. The only thing that matters
downstream is that **c > 0 and the leading term is linear in η**.

**3.** For φ slowly varying, (S^{(B)}φ)(x) = ∑_y S_{xy} φ(y). Expand
φ(y) = φ(x) + (y−x)·∇φ(x) + ½(y−x)ᵀ∇²φ(x)(y−x) + …. The zeroth-order term gives φ(x) by
the normalization ∑_y S_{xy} = 1; the first-order term vanishes because the profile is
symmetric; the second-order term gives ½ ∑_y S_{xy}|y−x|² · (Δφ)(x)/d. Since S is supported
on |y−x| ≤ W with profile f((x−y)/W), the second moment ∑_y S_{xy}|y−x|² is of order **W²**.
Hence

(1 − S^{(B)})φ ≈ −D Δφ, **D ~ W²**.

**4.** From §6,

(cη + D(−Δ))^{−1} = ∫₀^∞ e^{−cηt} e^{tDΔ} dt.

The exponential factor cuts the integral off at **t ≈ 1/η**. So the resolution η in energy
is a time horizon t ≈ η^{−1} in the diffusion. Setting η = 1/N, the horizon is **t ≈ N**.

**5.** In time t a diffusion with constant D spreads a distance √(Dt) = √(W² N) = W√N. The
torus has linear size L = N in one dimension. Requiring W√N ≳ N gives

**W ≳ √N.**

Which is Fyodorov and Mirlin's 1991 prediction, Yau and Yin's 2025 theorem, and Drogin's
2025 matching lower bound.

**6.** In two dimensions L = √N, and the same spread W√N must exceed √N:

W√N ≳ √N ⟺ **W ≳ 1.**

The obstruction disappears entirely. At this level of precision two dimensions is diffusive
for any bandwidth — which is exactly right, and exactly the point: **the two-dimensional
localization is not visible to a leading-order diffusion estimate.** It is a logarithmic
effect, coming from the marginal recurrence of two-dimensional random walk, and that is why
the conjectured threshold exp(cW²) ≳ N, i.e. W ≳ √(log N), involves a logarithm at all.
It is also why the theorem in d = 2 stops at W ≥ N^ε: proving the sharp result requires
resolving effects that this estimate cannot see.

**What to notice.** The famous √N is not a number that came out of a proof. It is a
statement about a race between a diffusion and a clock, and both the diffusion constant
(W², from the step size) and the clock (N, from the eigenvalue spacing) are things you could
have written down in five minutes. The theorem is the assertion that the heuristic is
exactly right — including the constant in the exponent.
</details>

### 7.2 Where 69% comes from (10 minutes)

Use the Huang–McKenzie–Yau theorem of §5.9 as given.

1. Write the Ramanujan condition max{λ₂, |λ_N|} ≤ 2 as two separate events.
2. Rewrite each in terms of the rescaled variables (AN)^{2/3}(λ₂ − 2) and
   (AN)^{2/3}(−λ_N − 2).
3. Given that the rescaled variables converge jointly to two **independent** TW₁ variables,
   and that TW₁ puts about 83% of its mass on (−∞, 0), compute the limiting probability.
4. Ask: could you have got this number from a concentration inequality?
5. Ask: what would have changed if λ₂ and λ_N were strongly positively correlated?

<details>
<summary>Solution</summary>

**1.** Ramanujan ⟺ {λ₂ ≤ 2} ∩ {−λ_N ≤ 2}.

**2.** λ₂ ≤ 2 ⟺ (AN)^{2/3}(λ₂ − 2) ≤ 0, and identically for −λ_N. Note that the centring
constant is exactly 2 and there is no shift: the paper records the constants as
C₁^d = (d(d−1)/(d−2)²)^{2/3} = A^{2/3} and **C₂^d = 0**. If C₂ had been non-zero the whole
computation would give a different number, and the fact that it is zero is a theorem, not a
convention.

**3.** By the theorem each rescaled variable converges to TW₁, and jointly they are
asymptotically independent. So

P(Ramanujan) → P(TW₁ ≤ 0)² ≈ (0.83)² ≈ **0.69.**

**4.** No — and this is the point of the exercise. A concentration inequality bounds the
probability that a quantity deviates from its typical value, and produces answers that go
to 0 or to 1. A limit strictly inside (0,1) means the event is decided by a fluctuation of
exactly the typical size. Nothing short of the **full limiting distribution** of that
fluctuation can produce the number. The first moment method, the second moment method,
Azuma, Talagrand — all give you the wrong shape of answer. That is why this problem waited
thirty-seven years for a proof and why the proof had to be an edge universality theorem.

**5.** If λ₂ and −λ_N were perfectly correlated the answer would be 0.83, not 0.69. If they
were strongly negatively correlated it could be as low as 0.66. So the independence claim is
load-bearing to two significant figures, and it is proved separately (Remarks 3.10 and 3.12
of arXiv:2412.20263), not assumed.

**A sanity check worth doing.** 0.83 is the value of the GOE Tracy–Widom distribution
function at 0 — i.e. the largest GOE eigenvalue is below its typical location about 83% of
the time. That asymmetry (83, not 50) is the left-skew of TW₁: the distribution has a thin
tail to the right and a thicker one to the left, so the median sits above the centring
point.
</details>

---

## 8. What is actually useful to you

### 8.1 The sandwich: use dynamics to prove your object was already at equilibrium

This is the most transferable single idea in the talk, and Yau flags its strangeness
himself (§5.5). The pattern:

1. Define a **class** by an estimate, not by a formula. ("All matrices satisfying the local
   law.")
2. Prove an **ergodic theorem for the whole class**: run any member forward under a noisy
   dynamics and after time t₁ it is at equilibrium.
3. Prove your **particular object barely moves** under that same dynamics up to a later
   time t₂ > t₁ — the statistics you care about are invariant.
4. Conclude your object was at equilibrium **at time zero**.

The dynamics never touched your object in any essential way. It was a probe. You get a
statement about the initial data out of a theorem about the flow.

Where this bites in your work: whenever you want to argue that a configuration you did not
design has a property you cannot check directly. Instead of inspecting it, find a
perturbation under which (a) *everything* in its rough class converges to a known reference
behaviour quickly, and (b) *your* configuration's measurable outputs are stable over a
longer window. If both windows are open at once, your configuration already had the
reference behaviour. Concretely: if injecting noise into a prompt/scaffold drives every
member of a broad class to a known behaviour within k perturbations, and your specific
scaffold's outputs are provably unchanged for 2k perturbations, then your scaffold was
already exhibiting that behaviour — without ever measuring it directly.

The precondition is the one worth remembering: **step 2 needs the class defined by an
estimate you can verify, not by a description.** That is what makes the huge-class theorem
provable at all.

### 8.2 Close the hierarchy where it is exactly solvable, not where it is small

The standard instinct with an unclosed hierarchy is to truncate where the neglected terms
are *small* — that is perturbation theory, and it is what the 2007 quantum diffusion proof
did, at the cost of "hundreds of graph computations" and a classification Yau calls "a
total nightmare".

The primitive hierarchy truncates somewhere else: at the point where **what remains can be
solved exactly**. The dropped terms are then shown to be errors afterwards, and the shape
of the answer is known in closed form from the start rather than assembled from a series.

Yau's own framing of the difference is a claim about physics as a whole: "for the last
century a lot of physics completely depended on perturbation theory… this primitive
hierarchy is actually a new class of integrable fixed points." Compare Otto's plenary
(`geometric-concepts-pde-otto.md`, §§4.5 and 9), which makes a structurally similar move in
singular SPDE — replacing Feynman-diagram bookkeeping with a diagram-free argument that
bounds variances directly. Two plenaries at one congress, in unrelated fields, both
reporting that the graph-expansion era of their subject has an exit.

The generalizable question when you face a coupled system you cannot close: **do not ask
"where are the terms small?" Ask "what is the largest sub-system that closes and solves?"**
Those are different questions with different answers, and only the second gives you an
object you can compute with.

### 8.3 When a comparison fails because your object is not uniform, prove uniformity first

§5.6 is a small masterclass in unblocking. The three-step strategy's comparison step
assumed, invisibly, that the matrix was mean-field. Band matrices are not, and the argument
died there "for a long time".

The fix was not to weaken the comparison, generalize it, or find a different route. It was
to prove a **stronger statement about the object** — quantum unique ergodicity, that the
eigenvectors are flat and pairwise orthogonal on every set — and hand the existing argument
the uniformity it had been assuming.

The diagnostic: when a general-purpose argument fails on your special case, check whether it
was silently relying on a regularity property. If so, the question is not "how do I fix the
argument" but "can I prove the regularity?" Often the regularity is a more interesting
theorem than the thing you originally wanted, which is what happened here — quantum
diffusion and QUE are more informative than the universality statement they were proved to
support.

### 8.4 A pass rate strictly between 0 and 1 needs a distribution, not a bound

§7.2, generalized. The 69% is the cleanest example in this playlist of a quantity that no
concentration argument can ever produce. Concentration inequalities answer "is this
overwhelmingly likely or overwhelmingly unlikely?"; they are silent on "is it 69%?".

For your evaluation work this is a direct constraint. If a benchmark's pass rate is near
0 or near 1, coarse arguments and small samples will characterise it. If it sits in the
middle, the pass rate is being decided by a fluctuation of exactly the typical size, and
nothing short of understanding the **distribution of that fluctuation** will tell you what
moves it. Adding samples reduces your error bar on 69%; it does not tell you why it is 69%
rather than 83%. The decomposition that explains the number here — two independent
one-sided events, each at 83% — is the kind of structural answer that a bound cannot give.

The check to run: when a rate sits mid-range and will not budge, look for the pair (or the
k-tuple) of near-independent binary events it factors into. Yau's answer is 0.83²; the
useful content is not the value, it is that there were **two** events and they were
**independent**.

### 8.5 Twenty years of the best people can be wrong about whether a theory is alive

§3's history is not decoration and Yau tells it deliberately. By 1970 Dyson and his
colleagues had concluded that random matrix theory had nothing to do with physics, and
walked away. They were wrong, and the reason they were wrong was that the nuclear data of
the period was incomplete. The theory was right; the measurements could not see it yet.

The generalizable observation is uncomfortable and worth holding: **a field's consensus that
an idea is dead is often a statement about instrumentation, not about the idea.** If you can
identify what measurement would have settled it and why it was unavailable, you have
identified the actual state of the question. Applied to your own domain: when a technique is
declared not to work, the first question is whether the evaluation could have detected it
working.

### 8.6 The honest limits of all of this for you

Two, both stated by the speaker.

**The band matrix is a surrogate.** Every theorem in this talk is about a matrix with W
random entries per row. The Anderson model has **one** — the diagonal potential. Yau names
delocalization for the Anderson model on ℤ^d as the problem they cannot do, and it has been
open since 1958. So the celebrated result is that the tractable interpolation is fully
understood; the physical model is not.

**Gaussian entries, mostly.** The band-matrix theorems assume complex Gaussian entries. The
non-Gaussian case in d = 1 is covered by Erdős and Riabov's independent work
([arXiv:2506.06441](https://arxiv.org/abs/2506.06441)); in higher dimensions it is not.
Universality theorems that assume Gaussianity are in a slightly odd position, and he does
not hide it.

He also names artificial neural networks as a place random matrices appear in nonlinear
settings, and moves on without a claim. I am not going to inflate one sentence into a
connection to your work that the talk does not make.

---

## 9. Where to read next

1. **Yau and Yin, *Delocalization of One-Dimensional Random Band Matrices*.**
   [arXiv:2501.01718](https://arxiv.org/abs/2501.01718) — 86 pages, 14 figures. The
   headline paper. §2 alone is worth the visit: it contains the definition of the G-loop
   (2.41), the loop hierarchy (2.45), the primitive hierarchy (2.48), and the quantum
   diffusion theorem (2.4) that §6 above unpacks. Start there and read only §2.
2. **Erdős and Yau, *A Dynamical Approach to Random Matrix Theory*,** Courant Lecture Notes
   28, AMS (2017). The companion for the background half — the local semicircle law, Dyson
   Brownian motion, and the three-step strategy in full, written for graduate students and
   deliberately light on technicalities. It predates every band-matrix result above, which
   is exactly why it is the right thing to read *first*.
3. **Huang, McKenzie and Yau, *Ramanujan Property and Edge Universality of Random Regular
   Graphs*.** [arXiv:2412.20263](https://arxiv.org/abs/2412.20263) — for §5.9. If the full
   paper is too much, Huang and Yau's exposition of it,
   [arXiv:2602.00975](https://arxiv.org/abs/2602.00975) (65 pages), explains the strategy
   and the microscopic loop equations without the full proof.

---

## 10. Self-test

<details>
<summary>1. What is a random band matrix, and what are its two limiting cases?</summary>

An N×N Hermitian random matrix whose indices sit on a discrete torus ℤ_L^d with N = L^d, and
whose entry variances are S_{xy} = W^{−d} f((x−y)/W), vanishing for |x−y| > W and normalized
so ∑_y S_{xy} = 1. With W = L in one dimension it is a Wigner matrix (every entry has
variance ≈ 1/N). With W = 1 only the diagonal and nearest neighbours survive and it
resembles the Anderson tight-binding model. Yau credits Wegner with introducing it, as the
orbital model. Because of the normalization the semicircle law holds for every W, so the
macroscopic spectrum says nothing about the transition.
</details>

<details>
<summary>2. State the dictionary between the Anderson coupling constant and the bandwidth, and the three thresholds it predicts.</summary>

λ ↔ W^{−1}. Anderson's localization lengths λ^{−2} (d=1), exp(cλ^{−2}) (d=2), ∞ (d≥3)
become W² (d=1), exp(cW²) (d=2), ∞ (d≥3). Setting localization length ≈ system size N = L^d
gives the transitions W ≈ √N in d=1, W ≈ √(log N) in d=2, and no threshold in d≥3. The d=1
prediction is Fyodorov–Mirlin (1991), from a supersymmetric σ-model plus numerics.
</details>

<details>
<summary>3. Define complete delocalization and probabilistic quantum unique ergodicity, and say how they differ.</summary>

Complete delocalization: every ℓ²-normalized eigenvector satisfies ‖u‖_∞² ≤ N^{−1+ε} with
overwhelming probability — the flattest an ℓ²-normalized vector on N sites can be. QUE: for
any deterministic diagonal projection E_A onto a set A, ⟨u_i, E_A u_j⟩ ≈ (|A|/N)δ_{ij}. The
i = j case is flatness on every set (the analogue of Rudnick–Sarnak's manifold statement);
the i ≠ j case says two eigenvectors restricted to A stay orthogonal. QUE is an ℓ² statement
about pairs on arbitrary sets, is strictly stronger, and is what step three of the
three-step strategy actually needs.
</details>

<details>
<summary>4. State the three-step strategy and explain why Yau calls it a strange use of dynamics.</summary>

(1) A priori local law for H₀ down to η ≫ 1/N. (2) For H_t = H₀ + √t·GUE with t ≳ N^{−1+ε},
the local statistics are GUE — Dyson's conjecture, that DBM reaches local equilibrium in
time N^{−1}. (3) For t ≲ N^{−1/2}, the local statistics of H_t agree with those of H₀. Both
windows are open for N^{−1} ≪ t ≪ N^{−1/2}, so H₀ already had GUE statistics. It is strange
because dynamics is normally used to flow *toward* a solution; here it is used to prove the
initial data was already at time-infinity equilibrium. The dynamics is a probe, not a
construction.
</details>

<details>
<summary>5. Why does the three-step strategy fail for band matrices, and what repairs it?</summary>

Step three — the comparison — requires the matrix to be mean-field, with variance spread over
all N entries of a row. A band matrix concentrates its variance in W entries near the
diagonal, so the comparison has nothing to grip. The repair is to prove probabilistic QUE
first: if the eigenvectors are flat and pairwise orthogonal on every set, the comparison goes
through. QUE in turn follows from quantum diffusion, which follows from the primitive
hierarchy. That chain — primitive hierarchy → L₂ ≈ K₂ → quantum diffusion → QUE → step three
→ universality — is the architecture of the talk.
</details>

<details>
<summary>6. Define the G-loop, and say what the loop hierarchy is and why it does not close.</summary>

The n-point G-loop is L_{t,σ,a} = Tr[∏_{i=1}^n G_t(σ_i)E_{a_i}] with σ_i ∈ {+,−} selecting
G(z) or G(z)^†, and E_a the projection onto the block at torus site a. The n=2, σ=(+,−) case
is Tr[G E_a G^† E_b] = ∑|G_{xy}|², the quantum-diffusion object. Applying Itô's rule under
matrix Brownian motion gives dL_n = (quadratic in lower loops) + (a term in L_{n+1}) +
(a martingale whose quadratic variation involves a loop of order 2n+2). L_n depends on
L_{n+1}, so the system never closes — exactly BBGKY, as Yau says from the podium.
</details>

<details>
<summary>7. What is the primitive hierarchy, why does it close, and what does it buy?</summary>

Drop the L_{n+1} term and the martingale, keeping only the quadratic terms. The resulting
system for the primitive loops K_n is triangular — the equation for K_n involves only
K_1,…,K_n through a convolution — so it can be solved **exactly**, K_1 first, then K_2, and
so on. K₂ has a closed form, and L₂ ≈ K₂ is quantum diffusion. Yau calls the primitive
hierarchy "a new class of integrable fixed points" and says it replaces perturbation theory.
The cost: proving L₂ ≈ K₂ requires proving L_n ≈ K_n for **all** n.
</details>

<details>
<summary>8. Write the quantum-diffusion formula and explain why it is a diffusion.</summary>

E Tr[G E_a G^† E_b] ≈ W^{−1}(|m|²/(1 − |m|²S^{(B)}))_{ab}, where m = m_sc and S^{(B)} is the
variance kernel, i.e. the transition matrix of a random walk with step W. Split the
denominator: (1 − |m|²) + |m|²(1 − S^{(B)}). In the bulk |m_sc(E)| = 1 at η = 0, so the first
piece is ≈ cη; the second is one minus a transition kernel, hence a discrete Laplacian, with
diffusion constant D ~ W². So the propagator is ≈ (cη + D(−Δ))^{−1} = ∫₀^∞ e^{−cηt}e^{tDΔ}dt
— the Laplace transform of the heat semigroup, cut off at time t ≈ 1/η.
</details>

<details>
<summary>9. Derive the √N threshold from the diffusion picture.</summary>

η ≈ 1/N is a time horizon t ≈ N. A diffusion with D ~ W² spreads √(Dt) = W√N in that time.
Delocalization requires covering the torus of linear size L. In d=1, L = N, so W√N ≳ N gives
W ≳ √N. In d=2, L = √N and the condition degenerates to W ≳ 1 — the leading-order estimate
cannot see the two-dimensional localization at all, which is why the true threshold there is
only logarithmic, √(log N), and why the proved result stops at W ≥ N^ε.
</details>

<details>
<summary>10. Where does 69% come from, and why could no concentration argument produce it?</summary>

Huang–McKenzie–Yau prove (AN)^{2/3}(λ₂ − 2) ⇒ TW₁ with A = d(d−1)/(d−2)² and no additive
shift, likewise for −λ_N, with the two limits independent. Ramanujan means both are ≤ 0. TW₁
puts ≈83% of its mass below 0, so the answer is 0.83² ≈ 0.69. No concentration inequality
can give it: a limit strictly inside (0,1) means the event is decided by a fluctuation of
exactly the typical size, so you need the full limiting distribution. The corollary also
settles the existence of infinite families of non-bipartite Ramanujan graphs for every
d ≥ 3, open since Lubotzky–Phillips–Sarnak.
</details>

<details>
<summary>11. What does Yau name as still open?</summary>

The sharp two-dimensional threshold (√(log N) rather than N^ε); localization/delocalization
for the genuine Anderson model on ℤ^d — he calls it "one key problem we cannot do", and both
d=2 localization at weak disorder and d≥3 delocalization are unproved; many-body analogues,
not even cleanly formulated; band matrix plus Laplacian, i.e. the block Anderson and Wegner
orbital models, partially reached in arXiv:2507.20274 with a transition at g = W^{−d/2}; the
spectral edge for band matrices; and nonlinear settings, where he names artificial neural
networks.
</details>

---

## 11. Note on the tutorial process

**Difficulty against reputation.** Yau's reputation is random matrix universality and
mathematical physics, and this talk is exactly that — no Kontorovich-style inversion. But the
brief predicted a Tier-0 inversion against *the reader*, and that prediction held: roughly
the first twenty minutes of the lecture are content the reader already owns under other names
(universality classes, kinetic theory, hydrodynamic limits, the semicircle law and level
repulsion, a Schrödinger equation whose modulus squared diffuses). So I compressed all of it
into §3, a calibration page, and spent the document on the loop hierarchy, the diffusion
computation, and the 2024–2025 results. Rated 2/5 for the physics and objects, 3/5 for the
machinery — the split is honest because the G-loop and its hierarchy are genuinely new
objects, even though the *move* (close a hierarchy) is one he knows cold.

**The anchor.** The speaker handed it over: "similar to this BBGKY hierarchy in classical
dynamics." I used his sentence and built §2 around the trio it belongs to — universality
classes, hydrodynamic limits, hierarchy closure. I did not add a fourth, and I did not
reach for the "random matrices were invented for nuclear physics" anchor as the *main* one:
it is true, it is in the talk, and it is §1 material, but it is background rather than the
structure of the mathematics. The BBGKY anchor is the one that actually explains the new
work.

**No proceedings paper; two companions, both partial.** I searched arXiv for a Yau preprint
matching this lecture and found none. Per the spec I fell back to surveys, and there are two,
neither of which covers the talk:

- Erdős–Yau, *A Dynamical Approach to Random Matrix Theory* (CLN 28, AMS 2017) — his own
  book, correct for §§5.5–5.6, and it **predates all the band-matrix work**.
- Huang–Yau, [arXiv:2602.00975](https://arxiv.org/abs/2602.00975) — correct for §5.9 and
  nothing else.

My brief explicitly ruled the second out as the proceedings paper (its comments field says
only "65 pages, 7 figures", no ICM reference) and asked me to judge whether it is a
legitimate labelled *companion*. It is, for one section: the talk really does spend its last
five minutes on random regular graphs and the 69%, and Yau plugs Huang's follow-up talk from
the podium. I have labelled it as covering §5.9 only, in the front matter, the header, and
§9, and I have not let it near any other section.

Everything else — the loop hierarchy, the primitive hierarchy, the quantum diffusion
formula, all six thresholds, the localization matching result — comes from the primary
papers, cited inline, in the Bartlett manner. That is the bulk of the mathematics here, and
the recovery is unusually complete for a caption-only talk, because all six results are
published.

**The lecture title.** The YouTube video is titled generically ("ICM 2026 Plenary Lecture -
Horng-Tzer Yau"; Simons Foundation; uploaded 2026-08-17; duration 53 minutes), and neither
mathunion.org nor the ICM programme pages surface per-lecture titles. The title in the front
matter is his own spoken one from minute two. I could not verify it against a printed
programme.

**Name corrections.** The captions destroy essentially every proper noun, including the
speaker's own name.

| Caption | Correct |
|---|---|
| HT H / HDL / Yao / Dao | Horng-Tzer Yau |
| Quran Institute | Courant Institute |
| nonlinear shinger equations | nonlinear Schrödinger equation |
| random sharing operator / shoring / showing equation | random Schrödinger operator / equation |
| vagner dy conjecture / wiggling universality | Wigner–Dyson(–Mehta); Wigner–Dyson universality |
| wiger / wager (spectral contexts) | Wigner |
| wager (orbital model context) | **Wegner** |
| opto models | orbital model (Wegner) |
| enderson | Anderson |
| laplas operator | Laplace (discrete Laplacian) |
| igon value / igon vector | eigenvalue / eigenvector |
| localization lens | localization length |
| deoization / deoized / dedizations / Docalization | delocalization / delocalized |
| proon statistic / person statistic | Poisson statistics |
| Frederick Spencer | Fröhlich and Spencer (1983) |
| Eisman Machanov | Aizenman and Molchanov (1993) |
| betalatis | Bethe lattice |
| Golden and Ma, 1962 | Gaudin and Mehta (the computation is 1960–61; see below) |
| penab equation by Jimboa Morris | Painlevé equation; Jimbo, Miwa, Môri and Sato (1980) |
| tracing with distribution | Tracy–Widom distribution |
| compress gaussian unit ensemble | complex Gaussian Unitary Ensemble |
| shy symmetric method | supersymmetric method |
| territo and bamboo | Tao and Vu |
| Erdish and Riabov | Erdős and Riabov |
| the dragon | Drogin (Reuben Drogin) |
| Lunik and Sonak | Rudnick and Sarnak |
| magic brown emotions / metric brown motion | matrix Brownian motion |
| on process / wooden back | Ornstein–Uhlenbeck process |
| dy conjecture | Dyson's conjecture |
| goddic / agodic / agoticity / quanticity | ergodic / ergodicity / quantum unique ergodicity |
| BPGki hierarchy / musical hierarchy | BBGKY hierarchy |
| mole term / module term | martingale term |
| etos rule | Itô's rule |
| predation theory | perturbation theory |
| deregular / dregular graph | d-regular graph |
| castm law | Kesten(–McKay) law |
| rajan / maluja / laud | Ramanujan |
| bubeski philips and sonak | Lubotzky, Phillips and Sarnak |
| along Sanak debate / no go along | the Alon–Sarnak disagreement; Noga Alon |
| Marcus Spielman the sastava | Marcus, Spielman and Srivastava |
| interlacing polinomial | interlacing polynomials (interlacing families) |
| Tracy Wen / Tracy Weden one | Tracy–Widom₁ |
| Joan Huang | Jiaoyang Huang |
| entering m 2/3 / entry minus one / n3 minus one | N^{−2/3} / N^{−1} |
| error infinity norm | ℓ^∞ norm |

**Substantive caption errors, corrected in the text.** Three, and all three invert a
meaning.

1. **"Complete localization" for "complete delocalization"**, twice — once in the statement
   of the Wigner-matrix theorem ("we also prove the complete localization and probabilistic
   QUE holds for all Wigner matrices") and once in the definition ("one way to say a vector
   is completely localized is that the ℓ^∞ norm squared is less than 1/N up to N^ε"). The
   inequality given is the definition of *de*localization, and the whole talk is about
   proving delocalization. Corrected in §4.3 and §5.2.
2. **Drogin's theorem stated backwards.** The captions read "for W ≤ √N is delocalized". His
   paper ([arXiv:2508.05802](https://arxiv.org/abs/2508.05802)) proves **localization** for
   W² ≪ N, with exponential decay at the sharp scale W². If it were delocalization there
   would be no transition and the sentence in which Yau declares the conjecture "completely
   solved" would be incoherent. Corrected in §5.7.
3. **"Each component should behave like 1/N".** For an ℓ²-normalized eigenvector on N sites
   it is |u(x)|² ≈ 1/N, i.e. |u(x)| ≈ N^{−1/2}. Stated correctly in §4.3.

**A date I did not silently fix.** Yau attributes the eigenvalue-gap computation to "1962".
The Gaudin–Mehta computations are usually dated 1960–61 (Mehta–Gaudin, *Nuclear Physics*
1960; Gaudin 1961). I have written "around 1960" and flagged the discrepancy here rather
than either repeating his date or quietly overwriting it, since the captions may have
mangled the number and I cannot tell which reference he had on the slide.

**Reconstructed, and labelled where it appears.**

- **§6, the reading of the quantum-diffusion propagator as a heat-semigroup resolvent.** The
  formula E Tr[G E_a G^† E_b] ≈ W^{−1}(|m|²/(1−|m|²S^{(B)}))_{ab} is verbatim Theorem 2.4,
  eqns (2.8)–(2.9) of [arXiv:2501.01718](https://arxiv.org/abs/2501.01718). The
  denominator split, the identification 1 − S^{(B)} ≈ −DΔ with D ~ W², and the Laplace
  transform are my algebra, marked in place. They reproduce exactly what Yau says verbally
  ("the Green's function squared is one over [η] minus the Laplace operator"). What would
  verify it: the propagator estimates in §3 of that paper.
- **§7.1, the derivation of the √N threshold.** Same status: standard folklore heuristic,
  written out; the captions carry only the statement of the threshold, not its origin.
- **The schematic loop hierarchy in §5.8.** Yau explicitly declines to write the equation
  ("I'm not going to give you all of them because it's so complicated"). I restored the
  three-term structure from Lemma 2.11/(2.45) and the primitive hierarchy from
  Definition 2.12/(2.48) of the same paper, and marked the display as schematic. The exact
  equation carries an explicit factor W and index sums that would not help here.
- **Fyodorov–Mirlin (1991) and Abrahams–Anderson–Licciardello–Ramakrishnan (1979)** are my
  attributions. Yau says "supersymmetric method and numerics" without a name, and
  "a famous paper of Anderson in 1979" — which is the four-author scaling-theory paper.

**Names I could not verify — not guessed.** Two.

- **"piggoa and lao"**, the collaborators on weakening the moment condition from 2+ε to
  1+ε (§5.2). I believe this is Aggarwal–Lopatto–Yau, "GOE statistics for Lévy matrices"
  ([arXiv:1806.07363](https://arxiv.org/abs/1806.07363), JEMS 2021), because α-stable entries
  with α ∈ (1,2) have exactly 1+ε moments and that is the only result of Yau's matching the
  described weakening. **The caption sounds do not support this reading and I have marked it
  a reconstruction in the text, not a fact.**
- **"emana and ego"**, the Bethe-lattice delocalization result (§5.1). I could not resolve
  either name. The known results there are Klein (1998) and Aizenman–Warzel; I cite those as
  *the literature*, explicitly not as what he said.

A third, minor: he refers to a lecture "yesterday" at the same congress that discussed the
trouble with the BBGKY hierarchy in classical dynamics. I could not identify which lecture
and have not named one.

**Gaps, and how bad they are.** Four, all marked in place.

1. **The exact local semicircle law** (§4.5) — error bound, constants, domain of z. On the
   slide. **Low impact:** the shape (valid down to η ≫ 1/N, m_N close to m_sc) is what the
   argument uses and is stated, and the precise statement is Theorem 2.1 of the companion
   book.
2. **The mechanism of step three, the comparison** (§5.5). He says "I will explain this
   later on in a minute" and never does. **Moderate impact** — this is the step that fails
   for band matrices and drives the entire second half, so the reader is told what breaks
   without being told what it is. I named the standard tool (Green function comparison) and
   did not reconstruct it.
3. **The exact loop hierarchy** (§5.8). He declines to state it. Restored schematically from
   the paper and labelled. **Low impact:** the structure — quadratic terms, one loop higher,
   a martingale — is exactly what makes the BBGKY analogy and the closure argument work, and
   that structure is recoverable.
4. **The proof that the dropped terms are errors** — i.e. L_n ≈ K_n for all n. This is the
   86 pages, and neither the captions nor a plenary lecture could contain it. **Low impact
   for this tutorial's purpose**, but it should be said clearly: everything above explains
   *why* the primitive hierarchy is the right object, and nothing above explains *why the
   truncation is legitimate*. That is the theorem.

**Length.** Comparable to the Bartlett tutorial and shorter than Otto's. The compression is
in §3 and §5.1–5.3, where the physics and history are told once and quickly; the length is
in §§5.7–5.9, §6 and §7, which are the parts that are less than two years old.
