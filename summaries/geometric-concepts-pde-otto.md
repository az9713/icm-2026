---
title: "Geometric Concepts in Partial Differential Equations"
speaker: Felix Otto (Max Planck Institute for Mathematics in the Sciences, Leipzig)
source: https://www.youtube.com/watch?v=K8-O-FdUzGs
video_id: K8-O-FdUzGs
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: none — companion: https://arxiv.org/abs/2401.05935
transcript: ../transcripts/K8-O-FdUzGs_transcript.txt
difficulty_for_you: 1/5 (part one) — 3/5 (part two)
reading_time: ~70 min
---

# Geometric Concepts in Partial Differential Equations — Felix Otto

**Field:** applied analysis. Nonlinear PDE, calculus of variations, and PDE driven by
randomness. Otto describes the talk himself as "kind of a personal tour" of one habit:
applying *elementary* concepts from differential and Riemannian geometry in the
infinite-dimensional setting of models from the applied sciences.

**Difficulty against your background: split, and the split is large.** The talk is two
vignettes with almost nothing in common except the method.

- **Part one is your own material.** It is the origin story of what the introducer calls
  "Otto calculus." Overdamped two-phase flow in a porous medium, treated as a gradient
  flow in a Wasserstein-type metric. Everything in it is built from calculus of
  variations, classical mechanics, and statistical mechanics. **Difficulty 1.** It gets
  the Tier-0 treatment: a compressed calibration, then the parts you almost certainly do
  not know.
- **Part two is a real gap.** Quasi-linear PDE driven by white noise, renormalization,
  and a geometric reconstruction of Martin Hairer's regularity structures.
  **Difficulty 3.** It would be a 4 in the standard tree-and-Feynman-diagram
  presentation. Otto's whole point is that a geometric framing removes most of the
  combinatorics — and that is exactly what pulls it down to a 3 for someone with your
  background. Part two gets the full bridge, and it is the longer half, as it was in the
  talk.

**What this tutorial builds.** For part one: nothing — it recalibrates and then goes to
the delta. For part two: white-noise scaling and subcriticality; the Cameron–Martin
space; the Malliavin derivative and the spectral gap inequality; the solution manifold
with charts and transition maps; germs, coherence, and Hairer's reconstruction theorem;
counterterms; multi-indices.

**A note on sources — read this before you trust any formula below.**

- **There is no ICM proceedings paper.** I searched arXiv and Otto's MPI MIS publication
  list. Nothing with this title exists. The announced title
  ("Geometric Concepts in Partial Differential Equations") is confirmed twice inside the
  talk itself — the introducer states it, and Otto repeats it in his first sentence — so
  the title is not announcement-level guesswork.
- **The companion I use for part two is
  [arXiv:2401.05935](https://arxiv.org/abs/2401.05935), Broux–Otto–Tempelmayr, *Lecture
  notes on Malliavin calculus in regularity structures*** (v1 January 2024, v3 October
  2025; 76 pages; published in *Stochastics and PDE: Analysis and Computations*, 2025).
  **This is a companion, not the ICM paper.** It earns the label: its abstract states
  the talk's exact thesis — a notion of model "indexed by multi-indices rather than
  trees," motivated "as charts and transition maps, respectively, of the nonlinear
  solution manifold," with the Malliavin derivative "assimilated to a tangent vector of
  the solution manifold." One real difference: the lecture notes work a *semilinear*
  equation (heat operator, cubic nonlinearity, additive noise — φ⁴-like), whereas the
  talk's model problem is *quasi-linear*. Where that matters I say so.
- **The talk's own named source for part two** is a paper with "Pablo, Markus and
  Pavlos" — Linares, Otto, Tempelmayr and Tsatsoulis,
  [arXiv:2112.10739](https://arxiv.org/abs/2112.10739), *A diagram-free approach to the
  stochastic estimates in regularity structures*, Invent. Math. **237** (2024)
  1469–1565. Otto says he is following an exposition sketched "with Luca and Marcus in a
  recent Oberwolfach report" — Lucas Broux and Markus Tempelmayr, *A geometric view upon
  regularity structures, charts and transition maps for the solution manifold*,
  Oberwolfach Report 33/2025. I could not retrieve the full text of that report (the
  MFO PDF endpoint returned 404), so I have not quoted it.
- **One nearby candidate is not used.** arXiv:2505.10175, *From Combinatorics to Partial
  Differential Equations* (Otto–Mattesini), is IMPRS lecture notes, not the proceedings
  paper. The talk itself says nothing about it. Since a better-matched companion exists,
  I do not use it.
- **No formulas survive in the captions.** Everything Otto wrote was on slides. Every
  displayed equation below is either (i) reconstructed from his spoken description and
  labelled, (ii) taken from a published source and cited, or (iii) marked as a gap. I
  have not filled a single hole by guessing.

**Names.** The auto-captions destroy essentially every proper noun in this talk,
including the speaker's own. Full correction table in §11.

---

## 1. What is at stake

Otto's thesis is one sentence, and both vignettes are evidence for it:

> Geometry — ordinary, elementary differential and Riemannian geometry, used informally
> in infinite dimensions — lets you **robustly encode a PDE problem that is ill-posed as
> stated**, and bypass the ill-posedness rather than fight it.

The two instances are as far apart as two problems in one field can be.

**Vignette one.** Two immiscible fluids of different density sit in the pore space of a
rock, heavy above light. The interface between them is unstable — it fingers, it breaks
up, it mixes. As a free boundary problem it is *ill-posed*: the equation for the
interface has no solution once fingering starts. Otto's move is to notice that the whole
system is a gradient flow, discretize the gradient flow variationally, relax the
discretized variational problem, and read off the mixing behaviour from what the relaxed
minimizers do. The ill-defined free boundary is never used. It is bypassed.

**Vignette two.** A quasi-linear elliptic PDE is driven by white noise. The noise is so
rough that the solution is not differentiable, so the differential operator on the left
side — which involves a coefficient evaluated *at the solution* multiplied against second
derivatives *of the solution* — has no meaning as a distribution. As written the equation
is *ill-defined*. Otto's move is to build a family of parameterizations of the solution
set, characterize them by how the operator acts on smooth functions only, and then throw
the operator away. The ill-defined operator is never used. It is bypassed.

His own image for the second move is the one to keep:

> "The mental image you should have is that we want to take a **cast** of the
> differential operator, take the impressions — which are the charts — and then discard
> the differential operator."

Same method, twice: replace the broken object with the geometry of the set of solutions.

The talk's framing is deliberately genealogical. Part one descends from Vladimir Arnold's
observation about the Euler equations and Yann Brenier's work on optimal transportation.
Part two is what Otto calls "a personal appropriation" of Martin Hairer's regularity
structures — "much less combinatorial and more geometric than the common approach." Otto
is candid about the maturity of each: part one is "fairly ancient" and "fully clear by
now"; part two is recent and "probably still has to unfold its merit."

---

## 2. Your anchor, and the calibration you can skip

You do not need an analogy for part one. Part one **is** your statistical mechanics,
restated in a different geometry, and the man restating it is the man the restatement is
named after.

The correspondence is exact and it is the canonical one:

> The Fokker–Planck equation **is** the gradient flow of the free energy (relative
> entropy) with respect to the Wasserstein-2 metric on probability densities.

That is Jordan–Kinderlehrer–Otto, 1998. Otto tells its origin story in the talk: it came
out of conversations at Carnegie Mellon with **Richard Jordan** and **David
Kinderlehrer**. And he tells it as the *sequel*, not the original — see §3.6, which is
the part you probably do not know.

Here is the calibration. Skim it, confirm we are using the same words, and go to §3.

**Gradient flow needs a metric, not just an energy.** This is the point Otto stops to
make explicitly, because everything hangs on it. Given a function E on a differentiable
manifold M, the derivative dE at a point is a **linear form** — a cotangent vector. A
flow needs a **tangent** vector, a direction to move in. The object that converts one
into the other is the metric tensor. So a "gradient flow" is not determined by E alone.
Change the metric and you change the dynamics, with the same energy. Both ingredients
matter, always.

**The Wasserstein-2 distance.** For two probability densities ρ₀, ρ₁ on ℝᵈ,

$$W_2^2(\rho_0,\rho_1) \;=\; \inf_{T_\# \rho_0 = \rho_1} \int |T(x)-x|^2 \,\rho_0(x)\,dx$$

the infimum over maps T pushing ρ₀ forward to ρ₁. Otto describes exactly this in the
talk — "minimizing over all maps that push forward the first measure into the second."
It is a genuine metric on densities of fixed mass.

**Otto's Riemannian picture of it.** Tangent vectors at ρ are infinitesimal mass
displacements δρ, and the metric is

$$\|\delta\rho\|_\rho^2 \;=\; \inf\Big\{ \int \rho |v|^2 : \ \delta\rho + \nabla\!\cdot\!(\rho v) = 0 \Big\}$$

— the cheapest kinetic energy of a velocity field that produces δρ. *(Standard; this
formula is not in the captions, it is the published Otto/Benamou–Brenier form. I state it
because §7.1 uses it.)*

**The JKO / minimizing-movement scheme.** Implicit Euler for a gradient flow acquires a
variational characterization. Given a time step τ and the current state ρᵏ,

$$\rho^{k+1} \;=\; \arg\min_{\rho} \Big[\, E(\rho) \;+\; \frac{1}{2\tau} W_2^2(\rho,\rho^k) \,\Big]$$

De Giorgi's name for schemes of this shape is **minimizing movements**. The standard
reference Otto names from the podium is the Ambrosio–Gigli–Savaré book.

**The one-line payoff.** With E(ρ) = ∫ρ log ρ + ∫Vρ, this scheme converges as τ → 0 to

$$\partial_t \rho \;=\; \Delta\rho + \nabla\!\cdot\!(\rho\nabla V)$$

the Fokker–Planck equation for the overdamped Langevin dynamics with potential V. You
derive it by hand in §7.1.

**Vocabulary for what "overdamped" buys you.** In conservative mechanics, force equals
rate of change of momentum — Newton. In an overdamped system, momentum is destroyed
instantly by viscosity, and the motion law becomes **force proportional to velocity**,
with a constant of proportionality Otto calls the inverse mobility. Nothing moves unless
a potential energy drives it. That is why overdamped dynamics are gradient flows and
conservative dynamics are not.

That is the whole prerequisite for part one. Everything in §3 is what is new.

---

## 3. Part one, rebuilt: from Euler to a mixing zone

### 3.1 Arnold: the Euler equations are a geodesic equation

Euler wrote down, a long time ago, the first PDE for the motion of an inviscid
incompressible fluid. Otto's reading of it in words: a fluid particle would move
**completely unaccelerated** — straight lines, constant speed — were it not for the
collective constraint that the flow map be volume preserving. Incompressibility is the
constraint; the **pressure** is the Lagrange multiplier enforcing it; and the gradient of
that pressure potential is the force that bends the particles onto their actual paths.

Arnold reinterpreted that sentence geometrically. Let X(t, x) be the time-dependent
diffeomorphism sending each initial position x ∈ ℝ³ to its position at time t; the
constraint says X(t, ·) lives in the group of volume-preserving diffeomorphisms. Then
"unaccelerated subject to the constraint" reads:

> **X(t, ·) is a geodesic in the group of volume-preserving diffeomorphisms.**

A geodesic needs a metric tensor. Arnold's is the plainest available: the **L² inner
product** on velocity fields. Where it comes from is worth having, because the same trick
recurs in part two. The ambient space of *all* transformations X of Euclidean space
carries a Hilbert (L²) structure; the volume-preserving ones form a submanifold, of
infinite codimension; the metric is **inherited by restriction** — exactly as a surface in
ℝ³ gets its first fundamental form from the ambient dot product.

Arnold did not stop there. **Sectional curvature** controls the exponential rate at which
nearby geodesics diverge, and for an embedded submanifold Gauss's theorem computes it from
the extrinsic curvature. Arnold did that computation, found many sectional curvatures
**strongly negative**, and read the resulting fast divergence as a geometric account of
the fact that these flows are **effectively unpredictable**.

### 3.2 Shnirelman and Brenier: the first relaxation

Geodesics are stationary points of an action; the action is the energy of a curve. So it
is natural to ask the variational question: can one *minimize* the action? Is the problem
well posed? Do shortest geodesics always exist?

**Alexander Shnirelman** showed that in **three space dimensions and higher**, generically
they do not. Otto calls this surprising, and gives the reason it is surprising: the action
functional is benign-looking. You can even write it **without any derivative at all**, as
a supremum over partitions of the time axis of a sum of L² distances between points on
the manifold:

$$\text{Action}(X) \;=\; \sup_{\text{partitions } t_0<\cdots<t_N} \ \sum_{i} \frac{\|X(t_{i+1})-X(t_i)\|_{L^2}^2}{t_{i+1}-t_i}$$

*(Reconstructed in form from "you can write the action as a supremum over partitions of a
sum of the L² distances between points on this manifold." The captions carry no formula.
The shape is forced — this is the standard metric-space definition of the energy of a
curve — but the exact normalization is a gap.)*

**Yann Brenier** was emboldened by exactly that derivative-free formulation to **relax**
the problem: give up the requirement that the flow map be one-to-one, keep only that it
push Lebesgue measure forward to Lebesgue measure. Giving up injectivity is precisely
allowing effective mixing. In that larger class, shortest curves exist.

Otto flags this explicitly as the template for everything that follows: *when the
variational problem has no minimizer, enlarge the class of competitors until it does, and
read the physics off the enlarged minimizers.*

### 3.3 Darcy and Muskat: switching from conservative to overdamped

Arnold's least-action principle is for an inviscid fluid — all dissipation neglected.
Now put the fluid in a rock.

**Henry Darcy** observed that flow in the pore space of a porous medium is highly
overdamped. The pores are tiny; the no-slip condition holds on the pore walls; momentum
that would be conserved in free flow is **instantly dissipated by viscosity**. So Newton's
law is replaced: force is no longer proportional to acceleration, it is proportional to
**velocity**, with constant of proportionality one over the mobility.

**Morris Muskat** looked at what happens with two immiscible components — say oil and
water — of different densities and different mobilities, driven by gravity. When they do
not mix, you get an **interface evolution**: a free boundary problem for the surface
between the heavy and the light phase.

And that free boundary problem is **ill-posed**, because of the fingering instability
Otto names from the podium. *(Caption: "suffment or fingering instability." The intended
name is almost certainly the **Saffman–Taylor** fingering instability; in this
gravity-driven porous-medium setting the same phenomenon is also called the
Rayleigh–Taylor instability. I flag this as reconstructed.)* Heavy above light in a porous
medium fingers immediately, and the fingers finger.

His question is the good one, and it is not "how do I fix the free boundary problem":

> Are there **rational** ways to quantify this effective mixing, given that the starting
> point is an ill-posed mathematical problem?

### 3.4 The gradient flow structure, and the surprise inside it

The Lyapunov functional is handed to you by physics: it is the potential energy with
respect to gravity. Write χ for the characteristic function of the heavy phase, ρ₁ and ρ₀
for the two mass densities, and let the last coordinate be height. Then

$$E(\chi) \;=\; g\!\int \big(\rho_1 \chi + \rho_0 (1-\chi)\big)\, x_d \; dx$$

*(Reconstructed from "the potential energy with respect to gravity, which I can represent
in terms of the characteristic function of the phase distribution — χ is the
characteristic function of the heavy phase — and in terms of the two mass densities ρ₁
and ρ₀ and the vertical height function, as this integral." The functional form is forced;
the constant g and any normalization are not in the captions.)*

That E decreases is trivial. Otto's claim is much stronger:

> The overdamped dynamics are a **gradient flow** of E — and with respect to **the same
> metric tensor** that governs Arnold's conservative dynamics.

He is careful about how far the coincidence goes. Mathematically it is "almost the same"
metric. Physically it is completely different, and you can see the difference in one
slot: where Arnold's metric carries the **density**, this one carries **one over the
mobility** — and if the two phases have different mobilities, the characteristic function
appears in the metric too.

*[Gap: the explicit metric tensor was on the slide. The captions give only the
substitution — density replaced by inverse mobility, with χ appearing when mobilities
differ — and no formula. I have not reconstructed it.]*

Sit with the structural claim for a second, because it is the reusable one. Two systems
with completely different physics — one conservative and time-reversible, one overdamped
and dissipative — share a Riemannian structure. What distinguishes them is not the
geometry but *what you do with it*: Arnold takes geodesics of the metric, Otto takes
gradient flow of an energy in the same metric.

### 3.5 Relaxation inside the time step, and the mixing zone

Now the machinery pays. Once you know you have a gradient flow, the **implicit Euler
scheme acquires a variational characterization** — and variational problems can be
relaxed.

Discretize time. At step k+1, minimize

$$E(\chi) \;+\; \frac{1}{2\tau}\, d^2\big(X, X^k\big)$$

over configurations, where τ is the time step and d is the distance from the metric of
§3.4 expressed through the flow map. That is the variational time discretization of the
gradient flow.

**Ill-posedness is still there, and now it is visible in the right place.** Minimizers do
not exist. But — in Brenier's sense — minimizing *sequences* converge to something no
longer one-to-one. On the level of characteristic functions: they converge **weakly** to
functions taking all values in [0, 1], and such a function has an unambiguous physical
meaning. It is the **volume fraction** of the first phase relative to the second. That is
the whole trick: weak limits of characteristic functions are volume fractions, and volume
fractions are the language in which "these two fluids mixed" is a statement rather than a
failure.

The relaxed problem persists at the limit level: the volume fraction φ at step k+1
minimizes

$$E(\varphi) \;+\; \frac{1}{2\tau}\Big[\, w_1\, W_2^2(\varphi, \varphi^k) \;+\; w_0\, W_2^2(1-\varphi,\, 1-\varphi^k) \Big]$$

and each of the two terms is an honest **Wasserstein** distance — the object from
statistics and optimal transportation, the infimum over maps pushing one measure to the
other. Both phases have to be moved, and moving each costs dissipation, which is why both
φ and 1−φ appear. *(The two weights w₁, w₀ are determined by the mobilities. Otto says the
relaxed dissipation "is the sum of the square of two metrics, weighted by the mobilities."
The captions do not give the weights, so I have labelled them rather than invented them.)*

Otto's own historical note, delivered in passing: this is an instance of what De Giorgi
later called **minimizing movements**, and the scheme had been used before it acquired
that name, in a *perfectly well-posed* interfacial motion — motion by mean curvature — by
**Almgren** and by Otto's own PhD advisor **Stephan Luckhaus**.

**Now take τ → 0.** Start from stratified initial data — specifically, the unstable
configuration, heavy above light. Then you can write down a very explicit solution, and it
shows:

- a **mixing zone** that opens **linearly in time**;
- a **profile** across that zone, and an **opening speed**, both of which depend in a
  characteristic way on the two mobilities.

That is the answer to the question in §3.3. The ill-posed free boundary problem has been
replaced by an explicit, quantitative, mobility-dependent description of how the mixing
region grows. And it was obtained without ever writing an equation for the interface.

*(A detail I keep because it is characteristic of the man: Otto points at his own slide
and says "there's a minus sign missing here." I have not reproduced the formula, so I
cannot say where.)*

### 3.6 The paradox that makes this interesting — and the link to Bartlett

Here is the part that should stop you, and it is the reason I said §3 is the delta rather
than the calibration.

**A gradient flow trajectory exits an unstable stationary point.**

The stratified unstable configuration — heavy above light — is a stationary point of E.
Gradient flows do not spontaneously leave stationary points. Yet this one does, in finite
time, with an explicit profile.

Otto's explanation is a statement about geometry, not about the energy:

> The energy functional "looks completely benign" — it is **linear** in χ. But in the
> intrinsic geometry, in the right geometry, in the geometry of this two-phase Wasserstein
> flow, it is **highly non-convex. It is not even semiconvex.** And that is what makes it
> possible to lead out of the stationary point.

Read that as a general warning. *Convexity is not a property of a functional. It is a
property of a functional with respect to a metric.* A functional that is literally linear
in its natural coordinate can fail even semiconvexity in the geometry that actually
governs its dynamics. All of the uniqueness and stability theory you would reach for
depends on semiconvexity along geodesics, and here there is none.

And the mechanism by which the trajectory escapes is an **order of limits**:

> "We have inverted the order of relaxation. We first relax, and then we let the time step
> size go to zero."

Relax-then-refine, not refine-then-relax. If you took τ → 0 first you would be solving the
ill-posed interface problem and you would get nothing. Taking the relaxation first, at
fixed τ, lets the minimizing sequence discover the mixing, and only then does the time
step shrink.

Otto ties this directly to another plenary at the same congress:

> "If you want, you can see a connection to **Peter Bartlett's** talk, where he said that
> with these kinds of steepest descent algorithms it's not always best to choose the
> smallest time step size. In fact sometimes it's good to choose a larger time step size.
> And this is what's happening here on a qualitative level."

That is worth holding next to §4.1 of the Wright tutorial in this same folder, where
Altschuler and Parrilo's silver step sizes buy a provably better rate by occasionally
taking a step so long it goes *uphill*, giving up monotone decrease. Three talks at one
congress, in three different fields, all reporting the same thing: **a finite step size is
not an approximation to an infinitesimal one. It is a different object, and sometimes the
better one.**

### 3.7 And only now, Fokker–Planck

Otto's chronology is the reverse of the one you would guess:

> "So that was the first Wasserstein gradient flow. Something much better known came about
> when I was at CMU and discussing with Rich Jordan and David Kinderlehrer... where we
> realized that in a much simpler case — single Wasserstein phase, and taking as the energy
> functional the Kullback–Leibler divergence — you can in fact recover the overdamped
> Langevin equation in the form of its Fokker–Planck equation."

So: the two-phase porous-medium mixing problem came first, in his own account, and the
famous statement — the one your statistical mechanics owns — is the **simplification**.
One phase instead of two. Relative entropy instead of gravitational potential energy.

*(Publication dates are close and run the other way: JKO appeared in SIAM J. Math. Anal.
29 (1998) 1–17, Otto's porous-medium paper in Comm. Pure Appl. Math. 52 (1999) 873–915. I
have not verified submission order. I report the ordering as Otto tells it, which is about
when the ideas happened, not when they printed.)*

He closes part one by noting where the idea landed: "in Stephen Wright's talk he was
briefly mentioning that this point of view is used to understand learning mechanisms in
neural networks." That is the mean-field / Wasserstein-gradient-flow analysis of training
dynamics — Wright's §6.4, citing Chizat and Bach, and Weinan E.

---

## 4. The bridge: what you need for part two

Otto changes register here and says so: no physics intuition, more mathematical detail,
and this half is the longer one. Read §4 slowly; §5 goes fast once you have it.

### 4.1 The problem, and exactly where it breaks

Take functions u : ℝᵈ → ℝ (Otto says three-dimensional affine domain, finite-dimensional
affine target; think d = 3 and scalar u), a constant positive-definite tensor a₀, and
contract:

$$a_0 : \nabla^2 u \;=\; \sum_{ij} (a_0)_{ij}\, \partial_i\partial_j u$$

A constant-coefficient elliptic operator — the Laplacian, or a sheared variant. Crucially,
**it makes sense on non-differentiable u**: test against a smooth ζ and integrate by parts
twice, moving both derivatives from u onto ζ, which you may do precisely because a₀ is
constant. So a₀ : ∇²u is a perfectly good Schwartz distribution however rough u is.

But media are nonlinear — the constitutive relation depends on the state. Let a be a
function of the *target* variable, mapping ℝ into positive-definite tensors, and write the
quasi-linear operator

$$a(u) : \nabla^2 u$$

Now try the same integration by parts. Move one derivative off u and onto the test
function. Fine. Try to move the second, and you cannot: differentiating the product
produces a term with ∇(a(u)) = a′(u)∇u in it, and you are stuck with a genuine derivative
of u again.

> **The barrier.** If u is not differentiable, there is no reasonable way to give a(u) :
> ∇²u a meaning. The equation as written is not merely hard. It is undefined.

Why would u fail to be differentiable? Because of the right-hand side:

$$a(u):\nabla^2 u \;=\; f$$

with f so rough it is not a function, and not even the derivative of a function.

**And why would f be that rough? Because thermal forces are.** Thermal forcing at
different points of the domain is statistically independent — the parts "don't speak to
each other." That independence *is* the roughness; in the limit it is the definition of
**white noise**. And it is the pivot the whole second half turns on:

> The independence is bad news and good news at once. It makes f rough. But it also means
> **you are not interested in a single f. You are interested in an entire probability
> measure over right-hand sides** — an *ensemble*, in physics language. That extra
> structure is what lets you get past the barrier.

Two properties of the ensemble do the work: **scale invariance** (§4.2) and the fact that
a Gaussian ensemble has a **thin Hilbertian tangent space** (§4.3).

### 4.2 Scale invariance in law, and subcriticality

Zoom in on the noise at a point. For a scale-invariant ensemble,

$$f(x_0 + \lambda\, \hat{x}) \;\overset{\text{law}}{=}\; \lambda^{\alpha-2} f(x_0 + \hat{x})$$

*(Reconstructed in form from "if you take your right-hand side and you take some center and
you zoom in, then it's statistically the same as magnifying the amplitude," with the
exponent written α−2. The exponent naming is verbatim from the talk; the display is my
transcription of it.)*

Note the direction. Otto contrasts this with **Jeremy Quastel's** plenary at the same
congress, where you saw Brownian motion's scale invariance with your own eyes — but there
you zoom *out* to see it. Here you zoom *in*, and the amplitude **grows**.

So α − 2 < 0. Two consequences fix the working range:

- **α < 1 is the interesting case.** By the scaling, α is the Hölder exponent of the
  solution. α < 1 means u is not differentiable — the singular case, the one that needs
  all this machinery.
- **α > 0 is required by subcriticality.** Subcritical means: *as you zoom in, the problem
  becomes more linear* — the constitutive law a(·) should look constant at small scales.
  That is what α > 0 buys.

So the theory lives at **0 < α < 1**.

**Where white noise sits.** For white noise the scaling exponent is −d/2, so α − 2 = −d/2
and

$$\alpha = 2 - \tfrac{d}{2}$$

In d = 3 that gives α = 1/2 — inside the window. And α − 2 = −3/2 < −1, which is Otto's
remark that in three dimensions f is "more negative than minus one even, and therefore not
even the derivative of a function." In d = 4, α = 0: critical. The theory stops.

**The change of perspective this forces.** To use scale invariance you have to enlarge
what you are studying. The dilation groups act on **both** the domain (centred at some
x ∈ ℝᵈ, ratio λ) and the target (centred at some v, ratio μ). Under the joint action, an
easy computation shows the nonlinear operator picks up a factor μ/λ². *(The λ² is the two
derivatives. This is stated in the talk and I reproduce it as stated.)*

To make the solution set invariant you have to **slave** the two ratios together through
α — pick the subgroup where μ and λ are linked by the exponent α — and then postulate that
*that* subgroup leaves the solution manifold invariant in law.

But invariance under target dilations moves a(·) around. So you cannot study one
constitutive law. You must study **all constitutive laws at once**, and the object that is
invariant is the set of *triplets* (a, u, f).

If that feels familiar it should: it is exactly what you do for ODEs when you study all
driving vector fields simultaneously rather than one, and it is the organizing idea of
Lyons's rough path theory.

### 4.3 The Cameron–Martin space: the thin tangent space

This is the single most important idea in part two, and it is pure Gaussian measure theory
— nothing about PDE in it at all.

Take a Gaussian ensemble. Ask: **which perturbations δf can I add to a sample without
leaving the measure class?** Formally, consider the shift map

$$f \;\longmapsto\; f + \delta f$$

and require that it map null sets to null sets. Otto calls this an exponential map, which
is the right instinct: it is the geometric statement that δf is an admissible direction of
motion.

The set of such δf turns out to be a **Hilbert space** — the **Cameron–Martin space**, the
tangent space to the ensemble.

**And here is the phenomenon.** For an infinite-dimensional Gaussian, the Cameron–Martin
space is **much smaller** than the smallest Banach space in which the realizations live.
The white-noise case makes it concrete:

| object | regularity |
|---|---|
| realizations of white noise | Schwartz distributions of order −d/2 |
| Cameron–Martin space of white noise | plain **L²**, order 0 |

**A gain of d/2 derivatives** in passing from the sample to the tangent direction. Otto
calls this a *sparsity* of the tangent space, and it holds for general dilation-invariant
ensembles too, not only white noise.

If you have seen this before it was as the classical statement that a Cameron–Martin shift
is the only translation under which a Gaussian measure stays equivalent to itself; the
regularity gain is the same fact wearing analysis clothes.

**The whole strategy of part two is to spend that d/2.** You cannot control the solution
by differentiating in a direction as rough as the noise itself. You *can* control it by
differentiating in the Cameron–Martin directions, which are d/2 derivatives smoother.

### 4.4 Malliavin derivative and the spectral gap

Differentiating a random object in a Cameron–Martin direction is exactly the **Malliavin
derivative** — an infinite-dimensional Fréchet derivative with respect to the noise, in
the direction of an element δf of the Cameron–Martin space.

The obvious worry is that a derivative restricted to such a thin space of directions might
not see anything. It does not happen, and the reason is the **spectral gap inequality**,
also called an infinite-dimensional **Poincaré inequality**:

> The Malliavin derivative **controls the variance** of a random variable.

Schematically, Var(F) ≲ 𝔼‖DF‖², with the norm taken in the Cameron–Martin space. *(Otto
states the control in words; the captions carry no constants. The shape is the standard
spectral gap statement.)*

That is the technical engine: you lose nothing by restricting to the thin tangent space,
and you gain d/2 derivatives.

**And it has a pedigree in Otto's other field.** He tells you where he got it — this is
what he and **Antoine Gloria** used when they started on *quantitative stochastic
homogenization*, and they found the idea in an **unpublished paper by Naddaf and
Spencer**, a 1998 preprint on variance estimates in homogenization built on a spectral gap
inequality. One of the more consequential unpublished papers in modern analysis.

### 4.5 The other randomness problem, and why it is the same problem

Otto pauses to place part two next to stochastic homogenization, and the comparison is
genuinely clarifying.

|  | singular SPDE (this talk) | stochastic homogenization |
|---|---|---|
| where the randomness sits | the **right-hand side** f | the **coefficient field** a |
| what is modelled | a nonlinear medium driven by thermal noise | a heterogeneous medium known only statistically |
| the enemy | small-scale **oscillations** | needing large-scale **cancellations** |
| what you want | tame the roughness | replace the medium by a homogeneous one on large scales |

They look opposite: one fights the noise at small scales, the other exploits it at large
ones. Otto's claim is that they are the same problem twice:

1. Both produce a **scaling law** out of a dilation invariance in law, and the scaling laws
   are similar.
2. Both are attacked by **monitoring the derivative of the solution with respect to the
   noise**, whatever the noise is attached to, and controlling it through the spectral gap.
3. Both need a **new kind of regularity theory** — one that decouples the *low regularity
   of the solution* from the fact that you can nevertheless approximate it to *high order*
   in a Taylor-type sense. He credits learning this from a paper of **Armstrong and Smart**
   and the work following it.

Point 3 is not a technicality. It is the definition of what a "model" is in this whole
field, and §4.7 makes it precise.

### 4.6 The solution manifold, its charts, and its transition maps

To take a derivative with respect to f you must hold something else fixed. So you need a
**parameterization** of the solution set: a parameter space P, held fixed, and then a
derivative in f. For a PDE, P has to be infinite dimensional (in d > 1). What should it be?

**Look at the constant-coefficient case.** If a ≡ a₀, the solution set of a₀ : ∇²u = f is
**affine over the linear space of a₀-harmonic functions**, and by ellipticity those are
**analytic**. So in the linear case the natural parameter space is a space of analytic
functions from domain to target.

Otto's bet is that this survives deformation to the nonlinear case:

$$u \;=\; u[p, f], \qquad p \ \text{analytic}$$

with the parameterization pinned down by requiring that u agrees with p when f vanishes.
*(He notes a second term added to the right-hand side of the defining equation to enforce
exactly that. The term itself was on the slide and is not in the captions.)*

The astonishing part, and he says so: **the solutions are far from analytic, and yet
analytic functions parameterize them.** The roughness lives entirely in the map p ↦ u,
not in the parameters.

**A uniqueness problem, and a broken symmetry.** On the whole domain, with no growth
conditions, the defining PDE does not pin down u[p, f] uniquely. The natural fix is to
demand **equivariance** under the dilation group actions of §4.2 — but full equivariance is
too much to ask, and the piece you must give up is equivariance under **translations of the
domain**.

A broken symmetry means the object you want is bigger than you thought. So you do not get
one parameterization. You get a **family of them, indexed by the homothety centre x**:

$$u_x[\,p,\,f\,], \qquad x \in \mathbb{R}^d$$

Otto invokes **Felix Klein's** philosophy here — once you have a family of objects related
by a group, look at how they transform. So the second object of the theory is the family
of **transition maps** between parameterizations at different centres:

$$p_{xy}: \quad u_x[\,p\,] \;=\; u_y[\,p_{xy}(p)\,]$$

*(Reconstructed composition, from "it's convenient to reintroduce our transition map and
to write u of x as the composition of u of y with the transition map." Otto says: "I think
retaining the picture is all you need." I have kept the picture and marked the formula.)*

**This is the punchline of the geometric reframing, so say it plainly.** In Hairer's
regularity structures, the pair (Π, Γ) is called a **model**: Π is the family of abstract
symbols realized as actual distributions, Γ is the recentering group element. Otto's claim
— and the companion lecture notes' abstract says it in as many words — is that

> **Π is a chart of the solution manifold, and Γ is a transition map between charts.**

You have met that structure before. It is the definition of a manifold. What is unusual is
only that the manifold is the solution set of a singular PDE, and the charts are indexed
by points of physical space.

### 4.7 Germs, coherence, and Hairer's reconstruction theorem

One more piece of vocabulary, and it is the one that does the analysis.

You will end up with a **family of distributions indexed by a base point y** — an object
that is a good local description of your solution *near y*, for each y separately. Such a
family is called a **germ**.

The question is whether the local descriptions can be **glued** into one global
distribution. That obviously requires the family to vary continuously in y in some
quantitative sense. That property is called **coherence**.

> **Reconstruction (Hairer).** A coherent germ determines a single distribution that it
> locally approximates, and the correspondence is bounded.

The condition, in this problem, is an inequality on exponents, and Otto states it
explicitly:

> Coherence holds **provided the sum of two exponents is positive**. One exponent is the
> Hölder continuity of the coefficient field, which is just **α**. The other is the order
> of the Taylor-type remainder, which is **α + d/2 − 2**.

So the condition is

$$\alpha \;+\; \Big(\alpha + \tfrac{d}{2} - 2\Big) \;>\; 0 \qquad \Longleftrightarrow \qquad \alpha \;>\; 1 - \tfrac{d}{4}$$

Otto's comment on it: it "gives rise to a new condition in low dimensions, not in high
dimensions, and is well known in the field." Check that against the inequality and it is
exactly right — in d ≥ 4 the right-hand side is ≤ 0 and the condition is implied by α > 0,
while in d = 3 it demands α > 1/4, in d = 2 it demands α > 1/2. You verify this in §7.2.

### 4.8 Counterterms

The last piece of vocabulary is one you already own from a different room.

A **counterterm** is a quantity you subtract to cancel a divergence produced by a
regularization, chosen so that the limit exists as the regularization is removed. That is
renormalization in quantum field theory, and Otto says so — "well known from quantum field
theory."

What is worth noticing is the *style* of the argument here, because it is a nice one. The
counterterm is not chosen by a computation. It is **pinned down by postulates**, and Otto
lists them: the counterterm should be

1. **deterministic** — not random,
2. **independent of the centre x**,
3. **independent of the parameter p**,
4. **compatible with the dilation group on the target**.

Those requirements make it unique. Renormalization by symmetry, rather than by
subtraction bookkeeping.

---

## 5. Part two, rebuilt: the construction in Otto's order

You now have every word. Here is the argument.

**Goal.** Characterize the family of parameterizations {u_x[p, f]} **without ever
referring to** the ill-defined operator a(u) : ∇²u on rough functions. Retain only how
that operator acts on smooth (analytic) functions, then discard it — the cast image
from §1.

**Step 1 — control the chart by its Malliavin derivative.** Fix a centre x. By the
spectral gap inequality (§4.4), controlling the Malliavin derivative of the chart controls
its fluctuations. So the chart's Malliavin derivative is the object to estimate.

**Step 2 — the two derivatives you can compare.** Look at the defining relation for
u_x[p, f]. Two things appear on the right: **f** and **p**. So there are two natural
derivatives:

- the **noise derivative** — Malliavin, in the direction of δf in the Cameron–Martin space;
- the **parameter derivative** — in the direction of some analytic δp.

The image of the parameter derivative, as δp ranges over all analytic functions, is by
definition the **tangent space to the solution manifold** at that point.

The question becomes: **can the noise derivative be represented by a parameter
derivative?**

**Step 3 — why it almost works, and exactly how it fails.** If Cameron–Martin elements
were analytic, the answer would be yes, essentially by Cauchy–Kovalevskaya. They are not,
so the inclusion fails. But it does not fail badly: we have d/2 derivatives in hand
(§4.3).

The failure is quantitative, and Otto is precise about it in a way that matters. Despite
the d/2 gain going from f to δf, **the Malliavin derivative of the chart is stuck at the
low regularity of the chart itself** — Hölder continuity of degree α. The gain does not
propagate to the derivative's regularity.

What *is* true is the approximation statement:

> The Malliavin derivative of the chart can be **locally approximated by an element of the
> tangent space to the solution manifold, to order α + d/2**.

"Locally" means: relative to a **second** centre y. Which is exactly why the transition
maps of §4.6 come back — you write u_x as u_y composed with the transition map, and
approximate the noise derivative at x by the parameter derivative at y.

For this you need only **polynomials of degree at most α + d/2**. Finitely many. That
finiteness is the whole reason the theory is computable.

**Otto's caution, and take it seriously:** this is *not* a Taylor approximation. Both sides
are rough functions; there is nothing to Taylor-expand. It is a **Taylor-type**
approximation — it has the same *complexity* as a Taylor expansion because the right-hand
side is parameterized by polynomials, but it is a statement comparing two rough objects.

He names the connections: in Gubinelli's work this is what would be called a **controlled
rough path**, and it is connected to the notion of **modelled distribution**.

**Step 4 — freeze the coefficients, once.** This is standard Schauder theory and Otto says
so. Rewrite the defining equation as a **constant-coefficient** operator on the left plus
everything else on the right:

$$a_0 : \nabla^2 u \;=\; \underbrace{f \;+\; \big(a_0 - a(u)\big):\nabla^2 u}_{\text{"where all the music is"}}$$

*(Reconstructed splitting. Otto describes exactly this: "we rewrite our defining equation
in terms of a constant coefficient operator with a right-hand side where all the music is,
which can be expressed in terms of the old right-hand side and the error we make by
freezing in the coefficients." The sign convention is mine.)*

You have split a nonlinear PDE into

- a **benign, constant-coefficient, linear** relation (harmless — see §4.1), and
- a **singular, pointwise, nonlinear** relation between the right-hand side and ∇²u.

The goal is now to make that second relation robust.

**Step 5 — pass to Taylor-type remainders.** Apply Malliavin derivatives, and work at the
level of the Taylor-type *remainders* of those derivatives. Two derivatives were consumed
by the Hessian, so the order drops by two:

$$\alpha + \tfrac{d}{2} \quad\longrightarrow\quad \alpha + \tfrac{d}{2} - 2$$

That is the exponent that reappears in the coherence condition of §4.7.

**But this is still informal**, and Otto flags it himself. The expression still contains a
genuine product — a(u_x) times the second derivative of u_y — of two rough objects.
Nothing has been gained yet.

**Step 6 — freeze the coefficients a second time.** Use the same trick again: freeze the
coefficient at the *secondary* base point y. Now a(u_y(y)) is a **constant** with respect
to the active variable, so the product is a distribution times a constant, and the whole
expression is at last **well defined**.

That is the crux. One freezing turns the operator into a constant-coefficient operator
plus an error. A second freezing, at the auxiliary centre, turns the error into something
that can be written down.

**Step 7 — glue with reconstruction.** What Step 6 produces is a **germ**: a family of
well-defined distributions indexed by y. To recover the actual Malliavin derivative you
must glue them, and gluing needs coherence. Coherence holds when α + (α + d/2 − 2) > 0
(§4.7). Hairer's **reconstruction theorem** does the gluing.

**Step 8 — the trade-off, and the counterterm that resolves it.** Here is the subtlety
Otto says he finds most attractive, because it has a geometric flavour.

The germs produced by freezing are **not individually Malliavin derivatives** of anything.
Being a Malliavin derivative — Otto calls it *integrability*, in analogy with integrability
of a distribution of tangent planes — emerges only *after* reconstruction. So there is a
**trade-off between coherence** (needed to glue) **and integrability** (needed for the
result to be a noise derivative).

His own analogy: this is like the fundamental theorem of surface theory, where you need
compatibility conditions (Gauss–Codazzi) before a candidate first and second fundamental
form actually come from a surface. And after all, he points out, the thing being built
here *is* a manifold.

The fix is to build an **approximating family of germs that genuinely are Malliavin
derivatives**. You do it the same way as before, but for a **modified right-hand side**:
apply a **smoothing (convolution) operator** to the second derivative, so that the product
is defined by fiat.

That is too intrusive — you have changed the equation. So you must **counter the effect of
the smoothing**, and the object that does it is the **counterterm** of §4.8, made unique by
its four postulates.

> The counterterm is what reconciles the trade-off between coherence and integrability.

**Step 9 — buckle it together.** Two relations now connect the same two objects, from
opposite directions:

- **Reconstruction** (made possible by the two freezings) relates the Taylor-type remainder
  of the Malliavin derivative of the *right-hand side* to that of the *parameterization*.
- **Integration** — applying the inverse of the constant-coefficient operator — relates
  them the other way.

Otto's assessment: "That was subtle. That's easy." Reconstruction was the hard part;
Schauder estimates for a constant-coefficient operator are routine.

**Step 10 — the last obstacle, and where the algebra finally enters.** To close the loop
you must **disentangle the Malliavin derivative from its Taylor remainder** — extract the
function itself out of the remainder statement. That works because of a **hidden strict
triangularity**, and the triangularity becomes visible only at the *perturbative* level.

Concretely, you expand twice:

1. expand the parameterizing function p in **monomials**, whose degree gives a grading;
2. expand the constitutive function a around the constant one a₀, in the direction of
   suitable monomials.

The grading is what makes the system strictly triangular, so it can be solved order by
order. Otto's comparison: "very analogous to expansion methods in quantum field theory."

And he adds a line worth quoting, because it is unusual for a talk of this technical
density:

> "These are the main ideas. In terms of ideas, I didn't really hide much."

---

## 6. The one claim, stated precisely

The talk is not built around a theorem, so here is the claim it argues, in the sharpest
form the sources support.

> **Claim.** For the quasi-linear equation a(u) : ∇²u = f driven by a scale-invariant
> Gaussian ensemble in the subcritical range 0 < α < 1, one can construct an object
> satisfying every axiom of Hairer's **centered model**, where
>
> - the index set is **multi-indices**, not **trees**;
> - the model components are **charts** (Π) and **transition maps** (Γ) of the solution
>   manifold;
> - the construction is driven by **Leibniz's rule** applied to derivatives in the
>   constitutive function a, the parameter p, and the noise f — rather than by
>   combinatorics on trees;
> - the stochastic estimates come from the **spectral gap inequality** applied to
>   Malliavin derivatives — rather than from **Feynman diagrams**.
>
> The construction is **more parsimonious** than the standard one, because it works only
> on the solution space.

Otto's own phrasing of the verification, which I keep because it is his: what they build
"satisfies all the axioms to the last iota of what is called a centered model." *(Caption:
"to the last Yoda.")*

**How to read the three substitutions.** Each replaces a combinatorial device with a
calculus device.

| standard theory | Otto's version | why |
|---|---|---|
| index set = **trees** | index set = **multi-indices** | you are differentiating in a, p, f, so what indexes your terms is *how many times you differentiated in each*, which is a multi-index |
| algebra from **tree combinatorics** | algebra from **Leibniz's rule** | if every object arises by differentiation, the product rule generates the algebra |
| stochastic estimates via **Feynman diagrams** | estimates via **spectral gap** on Malliavin derivatives | you never expand a moment into a diagram sum; you bound variance directly |

"There are no trees in the ansatz," Otto says, "but a similar algebraic structure
emerges." The multi-index structure group is worked out in Linares–Otto–Tempelmayr, *The
structure group for quasi-linear equations via universal enveloping algebras*
([arXiv:2103.04187](https://arxiv.org/abs/2103.04187)); the diagram-free stochastic
estimates in the full subcritical range are Linares–Otto–Tempelmayr–Tsatsoulis, *Invent.
Math.* 237 (2024) 1469–1565.

**Honest limits.** This is a *reconstruction of the machinery*, not a new well-posedness
theorem announced at the podium. Otto says so: he wants a "proof of concept," to "develop
the full theory and apply it in interesting situations," and this half of the talk
"probably still has to unfold its merit." He also states the comparison with the
foundational **Chandra–Hairer** paper ([arXiv:1612.08138](https://arxiv.org/abs/1612.08138))
as a difference of construction, not a claim of greater generality.

*[Gap: the talk gives no theorem statement, no hypotheses list, and no convergence rate.
Every displayed exponent above is one Otto spoke aloud. Everything else was on slides that
the caption track cannot see. For an actual theorem with hypotheses, go to the companion
lecture notes.]*

---

## 7. Do this by hand

### 7.1 Derive Fokker–Planck from the JKO scheme (25 minutes, pen)

This is the anchor, so build it once yourself. It is standard published mathematics — JKO
1998 — not something reconstructed from captions.

Take the free energy on probability densities

$$E(\rho) \;=\; \int \rho \log \rho \;+\; \int V \rho$$

and the Otto metric of §2. Show, formally, that the Wasserstein gradient flow of E is the
Fokker–Planck equation.

Two facts you may use. First, the first variation: δE/δρ = log ρ + 1 + V. Second, the
Wasserstein gradient of a functional E at ρ is

$$\operatorname{grad}_{W_2} E \;=\; -\,\nabla\!\cdot\!\Big(\rho\, \nabla \frac{\delta E}{\delta \rho}\Big)$$

<details>
<summary>Solution</summary>

Compute the inner gradient:

$$\nabla\frac{\delta E}{\delta\rho} \;=\; \nabla\big(\log\rho + 1 + V\big) \;=\; \frac{\nabla\rho}{\rho} + \nabla V$$

Multiply by ρ. The 1/ρ cancels:

$$\rho\,\nabla\frac{\delta E}{\delta\rho} \;=\; \nabla\rho + \rho\nabla V$$

So the gradient flow ∂_t ρ = −grad E is

$$\partial_t \rho \;=\; \nabla\!\cdot\!\big(\nabla\rho + \rho\nabla V\big) \;=\; \Delta\rho \;+\; \nabla\!\cdot\!(\rho\nabla V)$$

which is the Fokker–Planck equation for overdamped Langevin dynamics in the potential V. ∎

**The two things to take away.** First, the cancellation of ρ against 1/ρ is where the
diffusion term comes from — the **entropy** produces the **Laplacian**, and it produces it
only because the metric supplied the factor ρ. Second, run the argument with the flat L²
metric instead: you get ∂_t ρ = −(log ρ + 1 + V), which is not a PDE anyone wants. The
equation is in the metric, not in the energy.

Now connect it back to §3.6. Here E is convex along Wasserstein geodesics whenever V is
(that is McCann displacement convexity), which is why this flow is stable and does what you
expect. Otto's two-phase energy in §3.4 is **linear in χ** and yet **not even semiconvex**
in its geometry, which is why that flow does something you do not expect. Same framework,
opposite behaviour, and the difference is entirely in the interaction between the energy
and the metric.

</details>

### 7.2 The exponent bookkeeping of part two (15 minutes, pen)

Every exponent in §4 and §5 was spoken aloud, so this is fully recoverable. Do all four
parts; part (d) is the one with a surprise.

**(a)** White noise on ℝᵈ scales with exponent −d/2. Given Otto's convention that the
noise scales as λ^{α−2}, what is α? Evaluate at d = 3 and d = 4.

**(b)** The theory requires 0 < α < 1. What does each end mean, in words?

**(c)** The Malliavin derivative of a chart is approximated by a tangent vector to order
α + d/2. After passing to second derivatives, what order does the remainder have?

**(d)** Coherence requires the sum of the Hölder exponent α of the coefficient field and
the remainder order from (c) to be positive. Write the condition on α. For which dimensions
does it bite?

<details>
<summary>Solutions</summary>

**(a)** α − 2 = −d/2, so **α = 2 − d/2**. In d = 3, α = 1/2 — comfortably inside (0,1). In
d = 4, α = 0 — the theory's boundary. This is why d = 3 is *the* case in the talk and d ≥ 4
is out of reach for white noise.

**(b)** α is the Hölder exponent of the solution. **α < 1** means u is not differentiable —
this is the singular, interesting case; if α > 1 there is no problem to solve. **α > 0** is
subcriticality: zooming in makes the problem *more linear*, i.e. the constitutive law a(·)
looks constant at small scales. Without it the nonlinearity is as strong at every scale and
no perturbative construction can close.

**(c)** Two derivatives cost two units of order: **α + d/2 − 2**.

**(d)** The condition is

$$\alpha + \Big(\alpha + \tfrac{d}{2} - 2\Big) > 0 \quad\Longleftrightarrow\quad 2\alpha > 2 - \tfrac{d}{2} \quad\Longleftrightarrow\quad \boxed{\ \alpha > 1 - \tfrac{d}{4}\ }$$

Now tabulate the threshold against the standing assumption α > 0:

| d | 1 − d/4 | does it bite? |
|---|---|---|
| 1 | 3/4 | yes, hard |
| 2 | 1/2 | yes |
| 3 | 1/4 | yes |
| 4 | 0 | no — implied by α > 0 |
| ≥ 5 | < 0 | no |

Which is exactly Otto's remark that it "gives rise to a new condition in low dimensions,
not in high dimensions." **Check the arithmetic yourself** — this is one of the few places
where the captions give you enough to verify a claim in the talk independently, and it
comes out right. That is a useful signal about the rest of the exponent bookkeeping.

One more check worth doing. Substitute the white-noise value α = 2 − d/2 from (a) into the
remainder order in (c): α + d/2 − 2 = 0 exactly, for every d. The Taylor-type remainder for
white noise sits precisely at order zero. That is not an accident; it is the same
subcriticality balance seen from a different side.

</details>

---

## 8. What is actually useful to you

Five items, in order of how often you will reach for them.

### 8.1 A gradient flow is an energy **and** a metric — and everything interesting lives in the metric

Otto stops the talk to make this point, and it is the load-bearing idea in both his career
and your day job. The derivative of an energy is a *cotangent* vector — a linear form. A
direction to move in is a *tangent* vector. Converting one to the other requires a metric,
and there is no canonical choice.

The consequences are concrete:

- **The same energy in two metrics is two different dynamical systems.** §7.1 shows this
  in three lines: relative entropy in the Wasserstein metric gives diffusion; relative
  entropy in flat L² gives nonsense.
- **The same metric with two different uses is two different theories.** Arnold takes
  geodesics; Otto takes gradient flow of an energy. Same metric tensor, one conservative
  system and one dissipative one (§3.4).
- **Convexity is a statement about the pair, never about the energy alone.** The two-phase
  gravitational energy is *linear* in the phase indicator and *not even semiconvex* in the
  transport geometry (§3.6).

For your work the translation is direct. Every optimizer you configure has an implicit
metric hiding in how it measures "distance moved" — Adam's diagonal preconditioner and
Muon's spectral-norm trust region, both in Wright's talk, are exactly that. The energy is
the part you thought about; the metric is the part you inherited by accident, and it is
the part that decides the behaviour.

### 8.2 The coarse step is a different object, not a worse one

§3.6 has the full argument: relax at fixed τ, *then* send τ → 0, and a gradient flow
leaves an unstable stationary point. Otto ties it to Bartlett's step-size remark, and it
agrees with the silver-step-size result in the Wright tutorial in this folder, where
giving up monotone decrease over a horizon provably improves the rate. Three talks at one
congress: **a discretization is not an approximation to a continuum.**

Applied to agent systems: forcing every step of a loop to be locally optimal is a
*constraint*, and constraints cost. A loop allowed to hold a mixed, undecided state — the
volume fraction, strictly between 0 and 1 — can reach outcomes a strictly greedy loop
cannot.

### 8.3 When an object is undefined, characterize it by how it acts on the things where it *is* defined

This is the single most transferable move in the talk.

You already know one version of it: a distribution is defined by what it does to test
functions. What is new is the ambition. Otto applies it to a *nonlinear* operator, and the
impressions he keeps are not numbers but a family of parameterizations of the whole
solution set, **plus transition maps between them**.

The engineering analogue is exact, and the second half is the part usually missing: when a
component's behaviour is unspecifiable directly, specify it by its **observable interface**
on inputs you can construct, *plus* **consistency conditions between overlapping
observations**. The transition maps are the consistency conditions, and they are what make
the family an object rather than a pile.

### 8.4 Uniqueness by postulate

The counterterm (§4.8) is not computed. It is **pinned down by four requirements** — be
deterministic, be independent of x, be independent of p, be compatible with the target
dilation group — and those requirements make it unique.

That is a very economical way to specify something. You do not describe the object; you
describe what it must commute with, and the symmetry does the rest. Where you can express
a requirement as an invariance rather than as a formula, do it — invariances compose and
formulas do not.

### 8.5 Two hard problems that look opposite are often one problem

§4.5 is a small masterclass. Singular SPDE fights small-scale oscillations; stochastic
homogenization exploits large-scale cancellations. They look like opposites. They share:
scale invariance in law, differentiation with respect to the noise, spectral gap control,
and the need for a regularity theory that separates *low regularity of the object* from
*high-order approximability of it*.

The transferable diagnostic: **when you are stuck, ask what your problem shares with the
one that looks like its opposite.** Otto's own path — the spectral gap technique came out
of homogenization, learned in turn from an unpublished Naddaf–Spencer preprint, and was
carried across into renormalization — is a worked example of the payoff.

And the last line of his talk is the same lesson at the level of a career:

> "This confrontation of partial differential equations with randomness is very fruitful,
> no matter whether it's thermal noise — where your focus is on working against the
> detrimental effects of noise on small scales — or quenched noise in stochastic
> homogenization, where you try to benefit from large-scale cancellations. Always you need
> to develop a new type of regularity theory, and for both we find that using noise
> derivatives is a powerful tool."

---

## 9. Where to read next

1. **Broux, Otto, Tempelmayr, *Lecture notes on Malliavin calculus in regularity
   structures*.** [arXiv:2401.05935](https://arxiv.org/abs/2401.05935) — 76 pages, and the
   companion to part two. Start here: it is written as lectures, it develops exactly the
   charts-and-transition-maps picture the talk sketches, and it treats a semilinear
   equation, which is strictly easier than the talk's quasi-linear one.
2. **Linares, Otto, Tempelmayr, Tsatsoulis, *A diagram-free approach to the stochastic
   estimates in regularity structures*.**
   [arXiv:2112.10739](https://arxiv.org/abs/2112.10739), *Invent. Math.* 237 (2024)
   1469–1565 — the paper the talk names, for the quasi-linear case in the full subcritical
   range. This is where "no Feynman diagrams" is a theorem rather than a slogan.
3. **Jordan, Kinderlehrer, Otto, *The variational formulation of the Fokker–Planck
   equation*,** SIAM J. Math. Anal. **29** (1998) 1–17 — the paper behind §7.1 and the
   anchor. Sixteen pages. If you have somehow never read it end to end, this is the one
   evening in the list that pays back fastest.

---

## 10. Self-test

<details>
<summary>1. Why does a gradient flow need more than an energy?</summary>

Because dE at a point is a linear form — a cotangent vector — and a flow needs a tangent
vector to move along. The metric tensor supplies the isomorphism between them. So the same
energy in two different metrics gives two different dynamics, and the choice of metric is
part of the model, not a technicality.
</details>

<details>
<summary>2. What is Arnold's observation about the Euler equations, and what did he deduce from it?</summary>

The flow map of an inviscid incompressible fluid is a **geodesic** in the group of
volume-preserving diffeomorphisms, with the metric inherited by restriction from the
ambient L² structure on all transformations — exactly as a surface inherits its metric from
ℝ³. He computed sectional curvatures via Gauss's theorem, found many strongly negative, and
read the resulting fast divergence of geodesics as the geometric content of the fact that
these flows are effectively unpredictable.
</details>

<details>
<summary>3. What did Shnirelman show, and what was Brenier's response?</summary>

Shnirelman showed that in three space dimensions and higher, shortest geodesics
(minimizers of the action) generically do not exist. Brenier **relaxed** the problem: give
up injectivity of the flow map — allowing effective mixing — while keeping the requirement
that Lebesgue measure be pushed forward to Lebesgue measure. Minimizers exist in the
enlarged class.
</details>

<details>
<summary>4. Why is the Muskat free boundary problem ill-posed, and what does Otto do instead of fixing it?</summary>

Heavy fluid above light in a porous medium is unstable to fingering, so the interface
evolution has no solution once fingering starts. Otto never writes an interface equation.
He uses that the overdamped dynamics are a gradient flow of gravitational potential energy,
takes the variational (implicit Euler) time discretization, and **relaxes** it. Minimizing
sequences of characteristic functions converge weakly to functions valued in [0,1], which
are volume fractions — the correct language for "these two fluids mixed."
</details>

<details>
<summary>5. Otto's energy is linear in the phase indicator, yet the flow escapes an unstable stationary point. Explain.</summary>

Linearity is a statement in the flat coordinate. In the intrinsic geometry — the two-phase
Wasserstein metric that actually governs the flow — the same functional is **highly
non-convex, and not even semiconvex**. That is what permits a gradient-flow trajectory to
leave a stationary point. The mechanism is the inverted order of limits: relax first at
fixed time step, then send the time step to zero. Otto links this to Bartlett's remark that
the smallest step size is not always the best one.
</details>

<details>
<summary>6. Where exactly does a(u) : ∇²u fail to be a distribution, and why does randomness help?</summary>

For **constant** a₀ you integrate by parts twice, moving both derivatives onto the test
function — so a₀ : ∇²u makes sense for any rough u. For a(u), the first integration by
parts works; the second produces ∇(a(u)) = a′(u)∇u, so you need u differentiable and you do
not have it. Randomness helps because you are not handed one f, you are handed an
**ensemble** — a probability measure — whose scale invariance and Gaussian tangent-space
structure provide the extra information the single equation lacks.
</details>

<details>
<summary>7. What is the Cameron–Martin space, and what is the number d/2 doing?</summary>

It is the set of shifts δf such that f ↦ f + δf maps null sets to null sets — the tangent
space to a Gaussian ensemble, and a Hilbert space. For white noise it is plain L² (order
0), while realizations are distributions of order −d/2. So Cameron–Martin directions are
**d/2 derivatives smoother** than samples. The entire construction is built on spending
that gain: differentiate the solution in Cameron–Martin directions (the Malliavin
derivative), and use the spectral gap inequality to convert that derivative into control on
the variance.
</details>

<details>
<summary>8. What are the charts and transition maps, and what do they correspond to in Hairer's language?</summary>

The charts are the family of parameterizations u_x[p, f] of the solution manifold by
**analytic** functions p, indexed by a homothety centre x — the indexing is forced because
you must break equivariance under domain translations. The transition maps relate the
parameterizations at two different centres. In regularity structures these are exactly the
model (Π, Γ): Π is a chart, Γ is a transition map. The solutions are far from analytic even
though the parameters are.
</details>

<details>
<summary>9. State the coherence condition and say when it bites.</summary>

Coherence of the germ requires the sum of two exponents to be positive: the Hölder exponent
α of the coefficient field, and the Taylor-type remainder order α + d/2 − 2 (the −2 from
passing to second derivatives). So α + (α + d/2 − 2) > 0, i.e. **α > 1 − d/4**. In d ≥ 4
this is implied by subcriticality (α > 0) and is vacuous; in d = 3 it demands α > 1/4, and
in d = 2, α > 1/2. A genuine extra condition in low dimensions only.
</details>

<details>
<summary>10. Name the three substitutions Otto's construction makes relative to the standard one, and what buys each.</summary>

(1) **Multi-indices replace trees** as the index set — because every object arises by
differentiating in a, p and f, so what labels a term is how many times you differentiated
in each. (2) **Leibniz's rule replaces tree combinatorics** as the source of the algebraic
structure — same reason. (3) **The spectral gap inequality on Malliavin derivatives
replaces Feynman diagrams** for the stochastic estimates — you bound variance directly
instead of expanding moments into diagram sums. The result satisfies every axiom of a
centered model and is more parsimonious, because it works only on the solution space.
</details>

---

## 11. Note on the tutorial process

**Difficulty versus reputation.** Reputation would have predicted this talk correctly, but
only by accident, and only for half of it. Otto is famous for optimal transport and
gradient flows, and part one *is* optimal transport and gradient flows — so Rule 1 came out
even. But part two, which is the longer half and the reason the talk exists now rather than
twenty years ago, is singular SPDE and renormalization, and reputation would not have
predicted it. The team brief flagged the Otto-calculus anchor in advance; the transcript
confirms it, and also shows that anchoring the *whole* talk there would have been wrong.
The split rating (1 for part one, 3 for part two) is the honest one.

**The Tier-0 inversion, applied to half a document.** Part one gets a one-page calibration
(§2) and then goes straight to the delta — the two-phase Muskat problem as the *first*
Wasserstein gradient flow in Otto's telling, the non-convexity that lets a gradient flow
escape a stationary point, and the inverted order of limits. Part two gets the full bridge
(§4), which is what the template prescribes at difficulty 3.

**Name corrections.** The auto-captions mangle nearly every proper noun, including the
speaker's. All corrections below are verified against the talk's own named papers, the
speaker's publication list, or the primary literature.

| Caption | Correct |
|---|---|
| Phelix Sto / Felix Sto | **Felix Otto** |
| Maxplank Institute … Leipig | Max Planck Institute for Mathematics in the Sciences, Leipzig |
| Irene / Irene Fona | Irene Fonseca (introducer; Kinderlehrer was her adviser) |
| Leonard Oiler | Leonhard Euler |
| autocalculus | Otto calculus |
| Alexander Schneerman | Alexander **Shnirelman** |
| Bernier / bun / "Yandon's work" | Yann **Brenier** |
| Muscat | **Muskat** (Morris Muskat) |
| suffment … instability | **Saffman–Taylor** fingering *(reconstructed — see below)* |
| leapono functional | **Lyapunov** functional |
| vasstein / Vasachines / vasachstein | **Wasserstein** |
| the Georgie | Ennio **De Giorgi** |
| Ambro Sar | **Ambrosio** (Ambrosio–Gigli–Savaré) |
| Angrin | **Almgren** |
| Stefan Lucaus | **Stephan Luckhaus** (Otto's PhD adviser) |
| Rich Jordan and David Kinderelia | Richard Jordan and David **Kinderlehrer** |
| Kulbach L divergence | **Kullback–Leibler** divergence |
| focal plank | **Fokker–Planck** |
| nonj equation | **Langevin** equation |
| Martin Hyra / Hayra | Martin **Hairer** |
| lion's rough path | **Lyons**'s rough paths |
| kubinelli | **Gubinelli** |
| Chandra Hyra | **Chandra–Hairer** |
| "Pablo, Marcos and Pablo" | **Linares, Tempelmayr, Tsatsoulis** *(see below)* |
| "Luca and Marcus" | **Lucas Broux, Markus Tempelmayr** |
| Uba report | **Oberwolfach** report |
| Naf Spencer | **Naddaf and Spencer** |
| Antoan Gloria | **Antoine Gloria** |
| Armstrong and smart | **Armstrong and Smart** |
| maravan / malavan / Mayavan derivative | **Malliavin** derivative |
| Camron margin / kron mian | **Cameron–Martin** space |
| pankare inequality | **Poincaré** inequality |
| Koshi Coleskaya | **Cauchy–Kovalevskaya** |
| shaer theory | **Schauder** theory |
| helder | **Hölder** |
| lightnets's rule | **Leibniz**'s rule |
| fineman diagrams | **Feynman** diagrams |
| Jeremy Questell | Jeremy **Quastel** |
| Steven Wright | Stephen **Wright** |
| Terrence Tao | Terence **Tao** |
| "to the last Yoda" | to the last **iota** |
| SNZAT | **ansatz** |
| judici | **geodesic** |
| Gaus theorem | **Gauss**'s theorem |
| lrange parameter | **Lagrange** multiplier |

**Collaborator names — how they were resolved.** Otto says the second part is "based on a
paper with Pablo, Marcos and Pablo" (captions). Searching his publication list for a
four-author paper in this exact area returns Linares, Otto, Tempelmayr and Tsatsoulis,
*Invent. Math.* 237 (2024). The three coauthors are **Pablo** Linares, **Markus**
Tempelmayr and **Pavlos** Tsatsoulis — which is what "Pablo, Marcos and Pablo" is. Likewise
"Luca and Marcus" resolves to **Lucas** Broux and **Markus** Tempelmayr, confirmed by the
existence of an Oberwolfach Report 33/2025 contribution by Broux–Otto–Tempelmayr titled *A
geometric view upon regularity structures, charts and transition maps for the solution
manifold*. I did not guess any of these; each is anchored to a located publication.

**Reconstructed, not verified.** "suffment or fingering instability" → **Saffman–Taylor**.
The setting Otto describes is gravity-driven and would usually be called Rayleigh–Taylor in
a porous medium; "Saffman–Taylor" is the standard name for viscous fingering in the same
geometry and is the closest phonetic match. I have marked it as reconstructed in §3.3
rather than asserting it.

**Where the mathematics is unrecoverable, and how bad it is.** This is the honest ledger.

- **Part one, the metric tensor (§3.4).** Slide-only. The captions give just the
  substitution — density replaced by inverse mobility, characteristic function present when
  mobilities differ. **Marked as a gap; the most substantive hole in the document.**
- **Part one, the explicit mixing solution.** Otto shows a formula and notes a missing minus
  sign in it. **The formula is entirely lost.** The conclusion he states aloud — mixing zone
  opening linearly in time, profile and speed depending characteristically on the
  mobilities — is reported and is safe.
- **Part one, the relaxed variational problem (§3.5).** Structure fully described in words;
  the **mobility weights are not in the captions**, so I wrote them as symbols w₁, w₀.
- **Part one, the energy (§3.4) and the action (§3.2).** Reconstructed and labelled. The
  functional forms are forced by the verbal description; normalizations are not.
- **Part two, every displayed equation.** The scaling law, the Step 4 splitting, and the
  transition-map composition in §4.6 are labelled reconstructions. The **exponents are not
  reconstructions** — α, α−2, d/2, α+d/2, α+d/2−2 and the coherence condition are all spoken
  aloud, and §7.2 verifies they are mutually consistent and reproduce Otto's own remark
  about low dimensions. That internal check is the strongest evidence here that the exponent
  bookkeeping came through intact.
- **Part two, the theorem.** There is none in the talk — no hypotheses, no rate. Marked as a
  gap in §6; go to the two papers in §9 for statements.

**Length.** This runs longer than the two model tutorials because the talk is two disjoint
half-talks with a split difficulty rating, so §3 carries a Tier-0 delta treatment and §4–§5
carry a full difficulty-3 bridge. The name table alone is forty rows.

**Sources I could not retrieve.** The Oberwolfach Report 33/2025 PDF returned HTTP 404 from
the MFO repository, so although I could confirm the existence, authorship and exact title of
Otto's contribution to it, I have not quoted its content anywhere.

**One thing the talk does that the write-up cannot.** Otto's closing remark is that
geometry's real gift is "these mental pictures, which hopefully help people to save their
precious memory space and trigger fruitful associations." A large part of this talk was
pictures on slides — the fingering diagram, the charts-and-transition-maps figure, the
mixing zone. None of that reaches the caption track. If any section here feels thinner than
it should, that section is where a picture was doing the work.
