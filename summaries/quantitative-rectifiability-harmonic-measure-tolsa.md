---
title: "Quantitative Rectifiability and Harmonic Measure"
speaker: Xavier Tolsa (ICREA / Universitat Autònoma de Barcelona / Centre de Recerca Matemàtica)
source: https://www.youtube.com/watch?v=hyZsD4UWy1o
video_id: hyZsD4UWy1o
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2607.16457
transcript: ../transcripts/hyZsD4UWy1o_transcript.txt
difficulty_for_you: 2/5 (the PDE half) — 3/5 (the geometric measure theory)
reading_time: ~60 min
---

# Quantitative Rectifiability and Harmonic Measure — Xavier Tolsa

**Field:** the intersection of geometric measure theory, harmonic analysis, and elliptic
PDE. Concretely: how rough can the boundary of a domain be before the classical theory of
the Dirichlet problem stops working, and what exactly is the geometric condition that
draws the line.

**Difficulty against your background: split, and the split is the useful part.**

The PDE half of this talk is yours already. Harmonic measure, the Green function, the
fundamental solution, layer potentials, non-tangential maximal functions, the Dirichlet
and Neumann problems, Brownian motion — you have all of it. That half rates **2/5**: a
handful of definitions to fix, not a subject to learn.

The other half is a genuine gap. Rectifiability, pure unrectifiability, Hausdorff measure
and density, Ahlfors–David regularity, uniform rectifiability, the β-coefficients, and
Calderón–Zygmund operators taken with respect to a *general measure* rather than Lebesgue
measure — none of this is in your training. That half rates **3/5**: real, and crossable
in one sitting if the definitions are built by deforming things you know.

So this tutorial compresses the PDE background into a calibration section you can skim,
and spends its length building the geometric measure theory. Then it walks the talk.

**What this tutorial builds.** The single chain that the whole hour is about:

> mutual absolute continuity of harmonic measure and surface measure
> → boundedness of a Riesz transform
> → rectifiability of the boundary

and the reverse implications, and the price paid at each arrow.

**Note on sources.** This one is unusually clean. There *is* a proceedings paper:
[arXiv:2607.16457](https://arxiv.org/abs/2607.16457), Tolsa, *Interactions between
quantitative rectifiability, singular integrals, and boundary value problems for harmonic
functions*, submitted 17 July 2026, revised 21 July 2026, whose arXiv comment field reads
verbatim "Survey paper for the ICM 2026 plenary lecture of the author." Every theorem the
speaker stated is in it, with the formulas the auto-captions could not carry. I use the
paper to restore the mathematics and the transcript to fix the order and the emphasis.

They are not identical, and I flag every divergence. Three matter:

- The paper contains three large topics the talk skipped entirely: Jones' traveling
  salesman theorem, Carleson's ε²-conjecture, and the Painlevé problem stated as a
  characterization of *capacity*. Each gets a clearly labelled paper-only block below.
- The talk contains one thing the paper never mentions: **Kakutani's theorem**, and
  therefore Brownian motion. The paper has no probability in it at all. That absence is
  interesting, because Kakutani is the best anchor in the talk.
- The talk poses Kenig's 1991 question and then stops. The paper answers it, with the
  speaker's own theorem. I include the answer, labelled as paper-not-podium.

**Names.** The auto-captions destroy essentially every proper noun in this lecture,
including the speaker's. Corrections are in a table in §11, verified against the survey's
bibliography except where marked.

---

## 1. What is at stake

Here is the question with no jargon in it.

You have a region of space. You hold its boundary at a prescribed temperature — hotter
here, colder there. You wait. The interior settles into equilibrium. What is the
temperature at a point inside?

That is the Dirichlet problem for the Laplacian, and you have solved it a thousand times.
For a nice region the answer is an integral: the interior temperature at a point *p* is a
weighted average of the boundary temperatures, and the weight is a probability measure on
the boundary. That measure is called **harmonic measure with pole at p**, written ω^p.
Everything about the problem is encoded in it.

Now make the boundary ugly. Not merely non-smooth — genuinely fractal. Infinitely many
corners at infinitely many scales. Does the averaging formula survive? Does the weight
measure still behave like surface area, so that a set of zero area on the boundary
receives zero weight and vice versa? Does the solution still converge to its boundary
values in any useful sense?

The classical answer, from the 1970s and 1980s, is: yes, if the boundary is a Lipschitz
graph. That is already a big class — corners allowed, cusps not. But it is a *smoothness*
condition, and it is not the right one. It is sufficient, not necessary, and it is stated
in coordinates.

The discovery this talk is about is that **the right condition is not smoothness at all.
It is a measure-theoretic notion of "n-dimensional-ness" called rectifiability**, and the
correspondence between the PDE behaviour and the geometry is not one-way. It is an
equivalence. Harmonic measure behaving well *forces* the boundary to be rectifiable. There
is no topological assumption anywhere in the modern statements — no simple connectivity,
no connectivity at all in the strongest one-phase theorem.

And the tool that proves it is a singular integral operator, the Riesz transform, whose
L² boundedness turns out to be *exactly equivalent* to rectifiability in the two
dimensions where anyone can prove it. That equivalence is a theorem from 2014 and it is
the load-bearing wall of the entire subject.

Three fields, one chain. That is the talk.

---

## 2. Your anchor

The speaker hands you the first one from the podium, which is always the best case.

### 2.1 Harmonic measure is where Brownian motion exits

Tolsa states it plainly, calling it "the classical theorem from Kakutani from 1944":

> If Ω is a bounded open set, x₀ ∈ Ω, and E ⊂ ∂Ω, then ω^{x₀}(E) equals the probability
> that Brownian motion started at x₀ first exits Ω through E.

That is the whole of harmonic measure, and it is a probabilistic object you already own.
Release a particle at x₀. Let it diffuse. Record where it first touches the boundary.
Repeat. The histogram you accumulate on ∂Ω *is* ω^{x₀}. The averaging formula
u(x₀) = ∫ f dω^{x₀} is then the statement that the equilibrium temperature at x₀ is the
expected boundary temperature at the exit point — the Feynman–Kac representation for the
Laplacian with no potential and no killing.

The speaker immediately extracts the intuition that carries the rest of the talk:

> "The more visible is some part of the boundary for Brownian motion, the larger will be
> harmonic measure."

At an outward-pointing vertex, a diffusing particle hits early and often, so harmonic
measure is large there. Down in a deep fjord, the particle has to thread a narrow channel
without escaping first, so harmonic measure is small. On a fractal boundary this
visibility varies wildly across scales, and the question of whether ω is comparable to
surface measure becomes a question about whether the boundary is, in a quantitative sense,
*flat enough at most scales at most points that visibility does not collapse*.

Hold onto that sentence. Rectifiability is the rigorous version of it.

**Divergence to note:** the survey never mentions Kakutani, Brownian motion, or
probability. It builds harmonic measure the functional-analytic way — the map
f ↦ u_f(x₀) is a positive bounded linear functional of norm one on C(∂Ω) by the maximum
principle, so the Riesz representation theorem hands you a probability measure. That is a
cleaner derivation and a worse picture. The speaker chose the picture. So do I.

### 2.2 The Riesz transform is the field of a surface charge

The second anchor is not decoration either — the speaker states the identity it rests on.

The **n-dimensional Riesz transform** of a measure ν in ℝ^d is

$$\mathcal{R}^n\nu(x) = \int \frac{x-y}{|x-y|^{n+1}}\, d\nu(y).$$

Tolsa's own justification for why this object has anything to do with harmonic functions
is one sentence: "the Riesz kernel is the gradient of the fundamental solution of the
Laplacian modulo some constant."

In codimension one — n = d−1, the case that matters — that is literally true. The
fundamental solution of −Δ in ℝ^d is E(x) = |x|^{2−d}/((d−2)κ_d) for d ≥ 3, and
∇E(x) = −c·x/|x|^d. The kernel x/|x|^d *is* the Coulomb field of a unit point charge in d
dimensions, up to sign and constant.

So read the Riesz transform as electrostatics. Put a charge distribution ν on a surface.
𝓡^{d−1}ν(x) is the electric field it produces at x. The truncated version 𝓡_ε^{d−1}ν
ignores charge within distance ε of the observation point — it is the field with the
self-interaction cut out. Asking whether the operator is bounded on L²(μ) is asking
whether the field of a charge density in L²(μ) has finite energy in the same norm.

And the speaker's explanation of why boundedness should force flatness is a physics
argument dressed as an analysis argument:

> "The naive idea why there is a connection between the Riesz transform and
> rectifiability is that the existence and finiteness of this integral only occurs when
> there are many cancellations among the positive part of the integral and the negative
> part. That's the naive idea, and the precise statement is that the naive idea is
> correct."

The kernel is **odd**. On a flat sheet, the in-plane components of the field cancel by
reflection symmetry and the integral converges. On a set that fails to be flat at
infinitely many scales, the symmetry that produced the cancellation is gone, and the
integral has no reason to converge — and the theorems below say it does not.

That is the content. Bounded field ⟺ flat surface, where "flat" is the quantitative
measure-theoretic version.

### 2.3 The square function is Littlewood–Paley

The third anchor is structural rather than physical, and it is the one that makes the
central definitions readable at a glance instead of intimidating.

Every characterization in this talk has the shape

$$\int_0^R \big(\text{a defect measured at scale } r\big)^2\, \frac{dr}{r} < \infty .$$

You have seen exactly this object. It is a **square function**. The defect at scale r
plays the role of the Littlewood–Paley piece Δ_j f; the measure dr/r is the Haar measure
of the multiplicative group of scales, the continuous version of "sum over dyadic j"; and
finiteness of the L² sum over scales is the statement that the total defect, counted once
per octave, is summable.

Once you see that, "β-coefficient" stops being a new idea and becomes: *the L² distance,
at scale r around x, from the measure to the nearest n-plane, normalized to be scale
invariant.* And "the square function is finite almost everywhere" becomes: *the set is
close to flat at almost every point, in a summable sense, across all scales.*

The dr/r is not cosmetic. It is what makes the criterion invariant under dilation, which
is what allows a purely local, scale-by-scale condition to force a *global* conclusion
about the set. The speaker singles this out as the remarkable feature of the David–Semmes
theorem:

> "What is interesting and remarkable, I think, from this result is that from some local
> behaviour of these coefficients one can derive global information of the set."

### 2.4 Calibration: the PDE half you can skip

Skim this. It exists so we agree on words. All of it appears in the talk, and it is all
standard.

**The Dirichlet problem.** Ω ⊂ ℝ^{n+1} bounded open, f ∈ C(∂Ω). Find u ∈ C(Ω̄), harmonic
in Ω, with u|_{∂Ω} = f. Tolsa's own gloss: "one has a domain, one can think of f as a
distribution of temperatures on the boundary, and u(x) is the temperature in equilibrium
inside at the point x."

**Dimension convention, which matters throughout.** The ambient space is ℝ^{n+1} (or
ℝ^d), and **n is reserved for the dimension of the boundary and of the measures on it**.
So a hypersurface boundary in ℝ^d is (d−1)-dimensional, and the relevant Riesz transform
is 𝓡^{d−1}. The talk and the paper use both letterings; I follow whichever source I am
quoting and say which.

**Harmonic measure.** ω^p is the probability measure on ∂Ω with u_f(p) = ∫_{∂Ω} f dω^p for
every f ∈ C(∂Ω). For a Borel set E ⊂ ∂Ω, ω^p(E) is the value at p of the harmonic
extension of χ_E. It depends on the pole p, but **if Ω is connected, harmonic measures
with different poles are mutually absolutely continuous** — one is a positive finite
density times the other — so qualitative questions do not depend on the pole.

**Mutual absolute continuity**, written ω ≪≫ σ, means each measure is a positive finite
density times the other: they have the same null sets. This is the property the whole talk
is about. It is the precise version of "harmonic measure behaves like surface area."

**Surface measure.** σ = ℋ^{d−1}|_{∂Ω}, the (d−1)-dimensional Hausdorff measure on the
boundary. For a smooth boundary this is ordinary surface area. For a rough one it is the
only thing that still makes sense.

**Green function.** G(x,p) for Ω is the fundamental solution corrected to vanish on the
boundary:

$$G(x,p) = \mathcal{E}(x-p) - \int_{\partial\Omega} \mathcal{E}(x-z)\, d\omega^{p}(z).$$

Read the correction term as the potential of the induced surface charge on a grounded
conductor. That is not an analogy; it is the same equation. **This identity is the hinge
of the entire talk** and we differentiate it in §5.7.

**Non-tangential maximal function.** For a fixed aperture a > 0 and ξ ∈ ∂Ω, the
non-tangential region is Γ_a(ξ) = {y ∈ Ω : |ξ−y| < (1+a) dist(y,∂Ω)} — a cone with vertex
at ξ that stays away from the rest of the boundary. Then 𝒩(u)(ξ) = sup_{y∈Γ_a(ξ)} |u(y)|.

**The three L^p problems.** With σ = ℋ^{d−1}|_{∂Ω}:

| | statement | reads as |
|---|---|---|
| (D_p) | ‖𝒩(u)‖_{L^p(σ)} ≤ C‖f‖_{L^p(σ)} | Dirichlet data in L^p controls the solution |
| (R_p) | ‖𝒩(∇u)‖_{L^p(σ)} ≤ C‖∇_t f‖_{L^p(σ)} | tangential gradient of the data controls the gradient |
| (N_p) | ‖𝒩(∇u)‖_{L^p(σ)} ≤ C‖∂_ν u‖_{L^p(σ)} | Neumann data controls the gradient |

The point of the non-tangential maximal function, as the speaker puts it, is that this
estimate "determines the convergence of u to the values at the boundary for functions that
are in L^p." Without it you have a harmonic function with no boundary trace worth the
name.

That is the whole prerequisite from your side. Everything from here is the part you do not
have.

---

## 3. The bridge — geometric measure theory in six definitions

Each definition below is built by deforming something you already use. Each comes with a
concrete instance. This section is the main event of the tutorial.

### 3.1 Hausdorff measure ℋ^s — box counting, done honestly

You know how to define the length of a curve and the area of a surface when they are
parameterized. Hausdorff measure is how you do it when they are not — when you have an
arbitrary set and no chart.

For E ⊂ ℝ^d and ε ∈ (0,∞],

$$\mathcal{H}^n_{\varepsilon}(E) = c_n \inf\Big\{\sum_i \operatorname{diam}(A_i)^n : E \subset \bigcup_i A_i,\ \operatorname{diam}(A_i)\le \varepsilon\Big\},$$

and then ℋ^n(E) = lim_{ε→0} ℋ^n_ε(E), which exists because the infimum only increases as
you shrink ε. The constant c_n is chosen so that ℋ^n agrees with Lebesgue measure on ℝ^n.

Three things to internalize:

1. **The limit ε → 0 is essential.** With ε = ∞ you get the *Hausdorff content* ℋ^n_∞,
   which is a genuinely different and coarser object; it appears in the talk's cone-point
   theorem. Forcing the covering sets to be small is what makes the measure see fine
   structure.
2. **ℋ^1 is arclength and ℋ^n on a smooth n-manifold is its volume.** The speaker says
   exactly this. So this is not a new measure; it is the old one with the parameterization
   removed.
3. **The exponent is a dial, not a fact about the set.** For any E there is a critical
   exponent — the Hausdorff dimension — below which ℋ^s(E) = ∞ and above which it is 0.
   The interesting sets are the ones where ℋ^n(E) is positive and finite *at* the critical
   exponent.

### 3.2 Rectifiable and purely unrectifiable

Here is the definition. It is short, and its content is entirely in the words "countable"
and "up to a null set."

> **E ⊂ ℝ^d is n-rectifiable** if there is a countable family of Lipschitz maps
> g_i : ℝ^n → ℝ^d with ℋ^n(E ∖ ⋃_i g_i(ℝ^n)) = 0.

Deform from "manifold" in two steps. First replace *smooth chart* by *Lipschitz map*: you
allow corners, you allow the image to be a horrible non-injective mess, you only forbid
infinite stretching. Second, allow *countably many* pieces and throw away a set of measure
zero. What survives is not a shape. It is a measure-theoretic statement: **almost all of
the set, in the ℋ^n sense, can be covered by countably many Lipschitz images of ℝ^n.**

Rectifiability is stable under countable unions — that is immediate from the definition
and the speaker notes it. Curves of finite length are 1-rectifiable; smooth n-manifolds
are n-rectifiable. Both are elementary.

The opposite notion is the interesting one:

> **E is purely n-unrectifiable** if ℋ^n(E ∩ Γ) = 0 for every n-rectifiable set Γ.

Equivalently: no subset of E of positive ℋ^n measure is rectifiable. A curve of finite
length can be threaded through such a set as carefully as you like and it will still catch
zero length.

These are not complementary — a general set splits into a rectifiable part and a purely
unrectifiable part — but the dichotomy is the right one, and every theorem in the talk is
a statement about which side of it something falls on.

### 3.3 The example that carries the whole talk: the four-corner Cantor set

The speaker builds it on a slide and returns to it three times. It is the standard
counterexample of the subject and it is worth having in your hands.

Start with the unit square in the plane. Replace it by four squares of side 1/4 sitting in
its four corners. Replace each of those by four squares of side 1/16 in *their* corners.
Iterate forever. E is the intersection of the nested unions.

At generation k there are **4^k squares Q_{k,i} of side 4^{−k}**. Now compute the sum of
diameters at generation k:

$$\sum_i \operatorname{diam}(Q_{k,i}) = 4^k \cdot \sqrt{2}\cdot 4^{-k} = \sqrt{2},$$

**independent of k.** So the natural covering at every generation gives the same answer,
and this is the numerical signature of a set that is exactly one-dimensional. With more
work — the speaker says so and does not do it — one shows

$$\mathcal{H}^1(E) = \sqrt{2}.$$

Positive and finite. This set has honest one-dimensional length.

And it is **purely 1-unrectifiable.** No rectifiable curve captures positive length of it.
The speaker's picture is a curve drawn through the set, intersecting it, and the caption
that the intersection has at most zero length.

Sit with the contradiction between those two sentences for a moment, because it is where
the whole subject lives. The set has the *measure* of a curve and none of the *structure*
of one. It is one-dimensional in size and zero-dimensional in coherence. Every quantity
that only sees size — Hausdorff measure, dimension, density — cannot tell it from a
circle. Every quantity in this talk can.

We will use it again for removability in §5.10 and as an exercise in §7.2.

### 3.4 Ahlfors–David regularity — dimension n at every point and every scale

Rectifiability is qualitative. Everything from here is its quantitative counterpart, and
the first step is to demand that the set has the right dimension *uniformly*, not just in
the limit.

> A Radon measure μ in ℝ^d is **n-Ahlfors regular** (equivalently n-AD-regular) if there
> is C₀ > 0 with
> $$C_0^{-1} r^n \le \mu(B(x,r)) \le C_0\, r^n \quad\text{for all } x\in\operatorname{supp}\mu,\ 0<r\le\operatorname{diam}(\operatorname{supp}\mu).$$
> If only the upper bound holds, μ is said to have **n-polynomial growth**. A closed set E
> is n-AD-regular if ℋ^n|_E is.

Read it as: the measure of a ball behaves like r^n with constants, at every centre and
every scale. It is exactly the doubling condition you know, sharpened from "μ(2B) ≲ μ(B)"
to the specific power n.

The density ratio the speaker writes on the board is the same object,

$$\Theta_\mu^n(x,r) = \frac{\mu(B(x,r))}{r^n},$$

and AD-regularity says Θ is bounded above and below.

The four-corner Cantor set is 1-AD-regular. So is every Lipschitz graph. So is every
smooth hypersurface, away from the boundary scale.

### 3.5 Uniform rectifiability — rectifiable, with constants

The speaker deliberately declines to define this precisely from the podium — "I will not
define precisely what is uniform n-rectifiability, but I will say something" — and his
"something" is the right thing to remember. Here is the full definition from the survey
(§3.2), followed by his gloss.

> μ is **uniformly n-rectifiable** if it is n-AD-regular and there exist θ, M > 0 such
> that for every x ∈ supp μ and 0 < r ≤ diam(supp μ) there is a Lipschitz map
> g : B_n(0,r) ⊂ ℝ^n → ℝ^d with Lip(g) ≤ M and
> $$\mu\big(B(x,r)\cap g(B_n(0,r))\big) \ge \theta\, r^n.$$

The phrase for this is **big pieces of Lipschitz images**: inside every ball, at every
scale, a fixed fraction of the measure sits on a single Lipschitz image with a *uniform*
Lipschitz constant.

Compare with plain rectifiability, which allows countably many pieces with unbounded
Lipschitz constants and permits an exceptional null set. Uniform rectifiability
quantifies both: finitely much of the measure, uniformly good pieces, at every scale.

It implies rectifiability. It is strictly stronger.

The reason it is the right notion, and the reason David and Semmes invented it, is stated
in the survey: uniformly rectifiable measures are precisely the class on which every
singular integral operator with an odd Calderón–Zygmund kernel is L²-bounded. It was
designed backwards, from the operator theory. We come to that in §5.8.

### 3.6 The β-coefficients — flatness defect at one point and one scale

Now the central quantitative object, and the speaker defines it fully.

> For a Radon measure μ, 1 ≤ p < ∞, x ∈ ℝ^d, r > 0:
> $$\beta_{p,\mu}^n(x,r) = \inf_L \left(\frac{1}{r^n}\int_{B(x,r)} \left(\frac{\operatorname{dist}(y,L)}{r}\right)^p d\mu(y)\right)^{1/p},$$
> the infimum over all n-planes L ⊂ ℝ^d. For p = ∞, replace the integral by a supremum
> over supp μ.

Take it apart:

- **dist(y,L)/r** — how far the point y is from the candidate plane, measured in units of
  the ball's own radius. Dimensionless.
- **∫ ... dμ(y)** — averaged against the measure itself, not against Lebesgue measure.
  This is what makes it see the set rather than the ambient space.
- **1/r^n** — the normalization. If μ is n-AD-regular then μ(B(x,r)) ≈ r^n, so this factor
  turns the integral into an average.
- **inf over L** — you get to pick the best plane. β measures the residual after the best
  linear fit.

So β^n_{2,μ}(x,r) is the **root-mean-square residual of the best n-plane fit to μ inside
B(x,r), in units of r**. It is a least-squares regression coefficient. If μ inside the
ball is supported on an n-plane, β = 0 exactly — the speaker says so. If the measure lives
in a slab of thickness h around a plane, β ≲ h/r.

The whole construction is scale invariant when μ is n-AD-regular: dilating the picture
leaves β unchanged. That is what makes the dr/r integration in the next definition the
correct one and not an arbitrary weighting.

**Why p = 2 and not p = ∞.** The p = ∞ version, β_∞, is Peter Jones' original coefficient
and is the natural one for the traveling salesman theorem. The p = 2 version is the one
that works in the theorems below, and the survey records something sharp about this: for
sets of finite ℋ^n measure the characterization in §5.5 is **true for p = 2 and false for
every p ≠ 2** (Tolsa, *Publ. Mat.* 63 (2019)). That is not a technical preference. It is
the Hilbert-space exponent doing what Hilbert-space exponents do, and it is why the
subject reads like harmonic analysis rather than like geometry.

### 3.7 Carleson conditions — the square function, and what it forces

Two ways to assemble the β's over scales, and the difference between them is the whole
distinction between qualitative and quantitative.

**Pointwise (qualitative).** Fix x and integrate over scales with the invariant measure:

$$\int_0^1 \beta_{2,E}^n(x,r)^2\, \frac{dr}{r} < \infty \quad \text{for } \mathcal{H}^n\text{-a.e. } x\in E.$$

Read: at almost every point, the flatness defect is square-summable across octaves.

**Carleson (quantitative).** Integrate over scales *and* over points, and demand the
result be controlled by the measure of the ball:

$$\int_{B(x,r)}\!\int_0^r \beta_{p,\mu}^n(y,t)^2\, \frac{dt}{t}\, d\mu(y) \le C\,\mu(B(x,r)).$$

Read: the defect, integrated over the whole Carleson box above a ball, is bounded by the
*base* of the box. This is the same shape as every Carleson-measure condition you have
seen in H^p theory or in the Littlewood–Paley characterization of BMO. The measure
β² (dt/t) dμ on the "space × scale" upper half space is a Carleson measure.

The distinction is exactly the distinction between rectifiable and uniformly rectifiable.
The pointwise condition characterizes the first; the Carleson condition characterizes the
second. Both theorems are in §5.

That is the bridge. Six definitions, all of which now have a picture attached. Everything
from here is the talk.

---

## 4. A one-paragraph map before the walkthrough

The talk runs in three movements and one coda.

**Movement one (§5.1–5.5): geometry.** Rectifiability, its quantitative version, and the
characterization of both by square functions of β-coefficients. Pure geometric measure
theory and harmonic analysis; no PDE.

**Movement two (§5.6–5.10): the operator.** The Riesz transform, its identity with the
gradient of the fundamental solution, the theorem that its L² boundedness is equivalent to
rectifiability, and the payoff for removable singularities — the Painlevé problem.

**Movement three (§5.11–5.13): the PDE.** Harmonic measure, the one-phase and two-phase
free boundary theorems, and the L^p solvability of the boundary value problems.

**Coda (§5.14–5.15):** what the paper does that the talk did not.

---

## 5. The talk, rebuilt

### 5.1 Why rectifiability matters in analysis

Tolsa opens with the motivation, and it is a two-column slide: rectifiability appears in
**boundary value problems for elliptic PDE** and in **removable singularities** for
bounded holomorphic functions in the plane and for Lipschitz harmonic functions in higher
dimensions.

And he draws the distinction that organizes everything:

> "Broadly speaking there are two types of questions. The first one is [assuming]
> rectifiability, where one is usually interested in obtaining regularity results for
> solutions of elliptic PDEs such as harmonic functions. And in the other direction, we
> could assume good behaviour of certain PDE solutions and then we would like to
> characterize, or obtain, or prove rectifiability under this assumption."

Direction one is classical: nice geometry gives nice analysis. Direction two — analysis
forcing geometry — is the *free boundary* direction, and it is where all the recent work
is. Keep the two directions separate as you read; almost every theorem below is a
statement about one arrow or the other, and the two arrows have completely different
proofs.

He also states which domains he cares about, which is a useful filter: "we are interested
in open sets whose boundaries may be very rough, because if we have an open set whose
boundary is smooth then this is always true, and these domains are not interesting for
us." His running example of a suitable domain is **the complement of the four-corner
Cantor set**.

### 5.2 Two classical theorems, and the higher-dimensional collapse

Two results frame the subject.

**F. and M. Riesz, 1916.** If Ω is a **simply connected** domain in the plane with
ℋ^1(∂Ω) < ∞, then harmonic measure and arclength measure on ∂Ω are mutually absolutely
continuous.

Note the hypotheses. Finite length in particular implies the boundary is 1-rectifiable —
that is not obvious but it is true, and the speaker says so. And simple connectivity is
doing real work: this is a theorem about conformal maps in disguise.

**What happens in higher dimensions: it fails.** The speaker is blunt — "the analogous
statement is false. There are counterexamples in both directions." His diagnosis is the
right one: "topology in higher dimensions is not so determined." In the plane, simple
connectivity plus finite length is a rigid combination because the Riemann map exists. In
ℝ^3 it buys you nothing.

**Dahlberg, 1977.** The replacement. If Ω ⊂ ℝ^{n+1} is a **Lipschitz domain** — locally
the region on one side of a rotated Lipschitz graph — then harmonic measure and surface
measure are mutually absolutely continuous, and quantitatively so.

The speaker skips the quantitative statement. The survey gives it, and it is worth having
because it is the form all the later generalizations take. Writing ω^{x₀} for harmonic
measure with a pole at corkscrew distance from a ball B centred on ∂Ω:

$$\left(\fint_{B\cap\partial\Omega}\Big(\frac{d\omega^{x_0}}{d\sigma}\Big)^2 d\sigma\right)^{1/2} \le C \fint_{B\cap\partial\Omega}\frac{d\omega^{x_0}}{d\sigma}\, d\sigma = C\,\frac{\omega^{x_0}(B)}{\sigma(B)},$$

and moreover ω^{x₀} is a doubling measure. The constants depend only on the dimension, the
Lipschitz character, and the corkscrew constant.

That display is an **L² reverse Hölder inequality** for the Poisson kernel dω/dσ. Reverse
Hölder is the wrong-way inequality — the L² average controlled by the L¹ average — and it
holds only for weights that do not concentrate. Its presence here is the statement that
harmonic measure on a Lipschitz boundary is an A_∞ weight with respect to surface measure.
That is a much stronger and much more usable statement than mutual absolute continuity,
and it is the reason Dahlberg's theorem is the foundation of everything in §5.13.

### 5.3 The David–Semmes characterization

Now the geometry. This is Theorem 3.2 of the survey, and the speaker states it in the
AD-regular case.

> **Theorem (David–Semmes, 1991/1993).** Let μ be n-AD-regular in ℝ^d and 1 ≤ p < 2n/(n−2)
> (in particular any 1 ≤ p ≤ 2 works for every n). Then μ is **uniformly n-rectifiable**
> if and only if for all x ∈ supp μ and 0 < r ≤ diam(supp μ),
> $$\int_{B(x,r)}\int_0^r \beta_{\mu,p}^n(y,t)^2\, \frac{dt}{t}\, d\mu(y) \le C\, \mu(B(x,r)).$$

The speaker states the right-hand side as C·r^n and notes it is comparable to
μ(B(x,r)) by AD-regularity. Same thing.

He credits the inspiration to Peter Jones' earlier work and to techniques from harmonic
analysis — "multiscale arguments" — which is exactly right: the proof is a corona
decomposition, the same stopping-time architecture as in the Carleson corona theorem.

Then he makes the observation quoted in §2.3, that a purely *local* condition on the
coefficients yields *global* structure, and gives the sharpest instance: in the plane, for
a 1-AD-regular set E, this estimate holding for all x and r forces E to be contained in an
AD-regular **curve**, because in the plane uniform 1-rectifiability is exactly containment
in an AD-regular curve.

That is worth pausing on. You verify an inequality about least-squares residuals at every
location and scale, and out comes a single connected curve through the whole set.

### 5.4 Dropping Ahlfors regularity

AD-regularity is a strong hypothesis — it forbids the measure from being thin anywhere,
at any scale. Can it be removed?

> **Theorem (Tolsa 2015; Azzam–Tolsa 2015).** Let E ⊂ ℝ^d be ℋ^n-measurable with
> ℋ^n(E) < ∞. Then E is **n-rectifiable** if and only if
> $$\int_0^1 \beta_{2,E}^n(x,r)^2\, \frac{dr}{r} < \infty \quad\text{for } \mathcal{H}^n\text{-a.e. } x\in E.$$

The speaker attributes it to "Jonas [Azzam] and myself in 2015." The two halves are in two
papers: the forward implication in Tolsa, *Characterization of n-rectifiability in terms
of Jones' square function: part I*, Calc. Var. PDE 54 (2015) 3643–3665; the converse in
Azzam–Tolsa, *Part II*, GAFA 25 (2015) 1371–1412.

Two remarks he makes and one he does not.

**The pointwise version is the right generalization.** With AD-regularity gone, the
Carleson condition has nothing to be compared against, so you drop to a pointwise
statement — finiteness of the square function at almost every point — and you get plain
rectifiability rather than uniform rectifiability. Qualitative hypothesis, qualitative
conclusion. Note the integral now has only dr/r and no dμ: "so notice again that this
quantity is essentially scale invariant."

**The density-weighted version is equivalent.** The speaker adds: "the finiteness of this
condition is equivalent to the finiteness of the same integral but here putting the
density of this measure," meaning β² can be replaced by β²·Θ^n_{ℋ^n|_E}(x,r) without
changing the truth of the statement.

*Reconstructed reasoning, not stated by either source:* this is believable because for a
set of finite ℋ^n measure the upper density satisfies 2^{−n} ≤ θ^{*n}(x,E) ≤ 1 for
ℋ^n-a.e. x ∈ E — the standard density theorem. So the weight Θ is bounded above and below
by absolute constants at almost every point at small scales, and the two integrals are
comparable there. **What would verify it:** checking that the density theorem's bounds
apply at the relevant scales uniformly enough. I have not done that; I flag the reasoning
as mine, not the speaker's.

**Why this matters for later:** the weighted form β²·Θ (dr/r) is exactly the integrand in
the Dąbrowski–Tolsa theorem of §5.9 and in the Jones–Wolff potential of §5.15. The
speaker himself points forward: "the fact that this factor appears should not be so
surprising if we remember [this theorem]."

**The offshoot the speaker singles out.** Naber and Valtorta proved a discrete,
quantitative version of this theorem, with effective bounds on Hausdorff measure and
Minkowski content, and applied it to bound the size of the **singular sets of stationary
and minimizing harmonic maps**. Their techniques have since been used on the singular sets
of many free boundary problems. (The talk says "elliptic PDEs" generally; the survey says
harmonic maps and free boundary problems specifically. I quote the survey.)

This is the escape hatch from the subject into geometric analysis, and it is why this
machinery shows up in papers that look nothing like this talk.

### 5.5 The Riesz transform, defined properly

Definitions from §2.2, made precise, following the speaker.

The n-dimensional Riesz transform of a signed Radon measure ν is
𝓡^n ν(x) = ∫ (x−y)/|x−y|^{n+1} dν(y). The kernel has **homogeneity −n**, which is exactly
critical against an n-dimensional measure: the integral is not absolutely convergent. The
speaker's example is the one to keep: if μ is n-dimensional Lebesgue measure on an
n-plane, the kernel is not locally integrable against it. "I think that you should know
this," he says, and you do — it is the same divergence as the Hilbert transform on the
line.

The standard fix, and the same one you use for the Hilbert transform: **truncate**.

$$\mathcal{R}^n_{\varepsilon}\nu(x) = \int_{|x-y|>\varepsilon} \frac{x-y}{|x-y|^{n+1}}\, d\nu(y),$$

and then the principal value pv 𝓡^n ν(x) = lim_{ε→0} 𝓡^n_ε ν(x) when it exists, and the
maximal transform 𝓡^n_* ν(x) = sup_{ε>0} |𝓡^n_ε ν(x)|.

Notation used throughout: 𝓡^n_μ f = 𝓡^n(fμ), and **𝓡^n μ means 𝓡^n applied to the
constant function 1** — the field of the measure itself, with no density.

And the definition that matters:

> **𝓡^n_μ is bounded in L²(μ)** means the truncated operators 𝓡^n_{μ,ε} are bounded on
> L²(μ) **uniformly in ε**.

The survey is explicit that this formulation is chosen to sidestep the existence question
for principal values. Uniform-in-ε boundedness is a statement you can verify; existence of
the pointwise limit is a conclusion you hope to derive.

**Here is the thing that makes this hard, and that I want to state loudly because it is
the piece of the talk furthest from your training.** You know Calderón–Zygmund theory with
respect to Lebesgue measure. The measures here are *not* Lebesgue measure and need not be
doubling. They live on fractals. They may have polynomial growth and nothing else. The
entire classical CZ toolkit — the Calderón–Zygmund decomposition, the good-λ inequality,
the standard T1 theorem — has to be rebuilt in the non-homogeneous setting. That rebuild
is a body of work in its own right (Nazarov–Treil–Volberg, Tolsa, Volberg's CBMS
monograph), and it is the technical substrate under every theorem in §5.8 and §5.9. The
talk does not mention it. The survey mentions it only through its bibliography. It is the
reason these theorems took twenty years.

### 5.6 The bridge: from harmonic measure to the Riesz transform

This is the hinge, and the speaker walks it slowly. Start from the Green function identity
of §2.4:

$$G(x,y_0) = \mathcal{E}(x-y_0) - \int_{\partial\Omega} \mathcal{E}(x-z)\, d\omega^{y_0}(z).$$

Differentiate in x, and move the derivative under the integral:

$$\nabla_x G(x,y_0) = \nabla\mathcal{E}(x-y_0) - c_d\, \mathcal{R}^{d-1}\omega^{y_0}(x).$$

**That is the whole bridge.** Up to a constant, ∇E is the Riesz kernel, so differentiating
the correction term in the Green function produces exactly the Riesz transform of harmonic
measure.

Now the asymptotics that make it useful, in the speaker's own framing. When you study
harmonic measure you take **x near the boundary** and **y₀ deep inside** Ω. Then
|x − y₀| is bounded away from zero, so the term ∇E(x−y₀) is *bounded* — it is the harmless
one. He calls it the error term explicitly and gives the reason: "this is bounded because
the denominator of x − y₀ is bounded away from zero."

So, up to a bounded error,

$$\mathcal{R}^{d-1}\omega^{y_0}(x) \approx -c_d^{-1}\,\nabla_x G(x,y_0).$$

The Riesz transform of harmonic measure *is* the gradient of the Green function. In
electrostatic terms: harmonic measure is the induced surface charge on a grounded
conductor, and its Riesz transform is the field that charge produces, which is the field
of the Green function.

Then the estimate that converts this into something checkable. The survey states it as a
consequence of (6.4) plus "standard estimates relating the Green function and harmonic
measure": if Ω satisfies the capacity density condition,

$$\mathcal{R}_*^{d-1}\omega^{y_0}(x) \lesssim \sup_{r>0} \frac{\omega^{y_0}(B(x,r))}{r^{d-1}}.$$

**Read this line carefully, because it is the payoff.** The left side is an analytic
quantity — the maximal Riesz transform, the thing whose finiteness will force
rectifiability. The right side is a purely *metric* quantity — the supremum of the density
ratio of harmonic measure. So:

> **If harmonic measure has bounded (d−1)-density ratios at a point, the maximal Riesz
> transform is finite there.**

And bounded density ratios is precisely what mutual absolute continuity with ℋ^{d−1} gives
you, almost everywhere. That is how the hypothesis of the one-phase theorem turns into the
hypothesis of the rectifiability theorem.

> *[Gap, moderate impact: neither source proves the estimate |∇_x G(x,y₀)| ≲
> ω^{y₀}(B(x,r))/r^{d−1}. The speaker calls it "standard estimates from harmonic measure";
> the survey calls it "some standard estimates." It is the single most load-bearing
> unproved step in the talk. It is genuinely standard — it is the Caffarelli–Fabes–Mortola–
> Salsa type comparison between the Green function and harmonic measure — but you will not
> reconstruct it from either document.]*
>
> *[Gap, low impact: the speaker's on-the-fly derivation introduces the truncation
> parameter ε informally and says so — "I am cheating a little because I have introduced
> for free this epsilon." The survey's version is clean and I have followed it.]*

### 5.7 NToV: the black box

Now the theorem the speaker himself calls "the main black box."

> **Theorem (Nazarov–Tolsa–Volberg, 2014).** Let n = 1 or n = d−1.
>
> **(a) Qualitative version.** Let E ⊂ ℝ^d be Borel with ℋ^n(E) < ∞ and μ = ℋ^n|_E. If
> 𝓡^n_μ is bounded in L²(μ), then E is n-rectifiable.
>
> **(b) Quantitative version.** Let μ be n-AD-regular with 𝓡^n_μ bounded in L²(μ). Then
> μ is **uniformly** n-rectifiable.
>
> **(c) The form the speaker used.** If E is Borel with ℋ^n(E) < ∞ and μ is mutually
> absolutely continuous with ℋ^n on E, then E is n-rectifiable **if and only if**
> 𝓡^n_* μ(x) < ∞ for μ-a.e. x ∈ E.

References: (b) for n = d−1, d > 2 is Nazarov–Tolsa–Volberg, *Acta Math.* 213 (2014)
237–321; (a) for n = d−1, d > 2 is Nazarov–Tolsa–Volberg, *Publ. Mat.* 58 (2014) 517–532;
the n = 1 cases are earlier — Mattila–Melnikov–Verdera, *Ann. of Math.* 144 (1996) 127–136
for (b) and Léger, *Ann. of Math.* 149 (1999) 831–869 for (a), the latter also proved in
an unpublished manuscript of Guy David.

**The easy direction and the hard direction.** The speaker separates them and the
distinction is instructive.

*Rectifiable ⟹ bounded* was known: David and Semmes, resting on the Calderón–
Coifman–McIntosh–Meyer theory of the Cauchy integral on Lipschitz graphs. This is the
classical direction. Once you know the Cauchy integral is bounded on a Lipschitz graph,
you build the general case by decomposing a rectifiable set into graph pieces.

*Bounded ⟹ rectifiable* is the **David–Semmes problem**, posed in the early 1990s, and it
is much harder because it is a free boundary problem: you are given analytic information
and asked to produce geometry. The speaker says so directly — "the other implications,
that go from Riesz transform to rectifiability, are more like free boundary problems, are
more difficult."

**Why the plane was solved first, and why it did not generalize.** For n = 1 the tool is
**Menger curvature**: for three points x, y, z in the plane, c(x,y,z) is the reciprocal of
the radius of the circle through them, and Melnikov's identity expresses the L² norm of
the Cauchy transform in terms of a triple integral of c². Positivity of c² turns the
problem into a geometric one about how much the measure bends. The speaker: "their methods
used the so-called curvature of measures, and this is a notion that is useful in the plane
but not in higher dimensions." There is no positive curvature-like quantity for the Riesz
kernel in higher dimensions. The whole approach dies.

**What replaced it, and I state these as facts, not as a proof.** The speaker gives the
one honest sentence about the difficulty:

> "In order to prove this theorem what we have to do is to estimate the β₂ coefficients in
> terms of the L² norm of the Riesz transform — that is, in particular, we have to
> estimate from below the Riesz transform of μ. And this is difficult because the Riesz
> transform involves a kernel that has cancellations, and these cancellations we don't
> know where they are. It's like when we wish to sum positive and negative numbers: we can
> bound from above, maybe with difficulty, but from below, if we want to show this is
> bounded away from zero, this could be more difficult."

That is the entire conceptual obstacle in three sentences. **Upper bounds on an
oscillating integral are routine; lower bounds are not**, because you cannot rule out
cancellation you cannot locate.

The ingredients, from the survey: the David–Semmes **BAUP criterion** for uniform
rectifiability; **quasiorthogonality** arguments; a variational argument rooted in
Eiderman–Nazarov–Volberg, who showed that vanishing lower density forces the Riesz
transform to be *unbounded*; the **maximum principle** for harmonic functions, used to
transfer L^∞ bounds on 𝓡^{d−1}(ℋ^{d−1}|_E) from E to the ambient space; and then the
**Fourier transform** in the ambient space to produce the lower bounds.

**I am declaring this a black box and stopping.** Following the precedent of the Gaitsgory
tutorial in this series (`langlands-function-fields-gaitsgory.md`), which declines to teach
two objects and says so: this proof is a 90-page *Acta* paper resting on a rebuilt
non-homogeneous Calderón–Zygmund theory. Neither the talk nor the survey attempts a sketch
beyond the paragraph above. A tutorial that manufactured one would be manufacturing
fiction. What you should take away is: the statement, the reason the plane was easy, the
reason higher dimensions were not, and the fact that the maximum principle is what makes
codimension one work.

**Which is exactly why the general case is open.**

> **Question (David–Semmes problem, still open).** For an integer n with 1 < n < d−1: if μ
> is n-AD-regular and 𝓡^n_μ is bounded in L²(μ), is μ uniformly n-rectifiable?

The survey names the obstruction precisely: "the absence of a suitable maximum principle
for functions of the form 𝓡^n η for n < d−1." In codimension one the Riesz transform is
the gradient of a harmonic potential and inherits the maximum principle. In intermediate
dimensions it is not, and there is nothing to inherit. That is a clean statement of why a
proof does not generalize, and it is the kind of statement worth collecting.

### 5.8 General measures: the Dąbrowski–Tolsa characterization

The theorem the speaker presents as the most recent piece of this story, joint with a
former student.

> **Theorem (Dąbrowski–Tolsa).** Let μ be a Radon measure in ℝ^d with **no point masses**.
> Then 𝓡^{d−1}_μ is bounded in L²(μ) **if and only if** both
>
> $$\mu(B(x,r)) \le C\, r^{d-1} \quad \text{for all } x\in\operatorname{supp}\mu,\ r>0 \tag{growth}$$
>
> and
>
> $$\int_B \int_0^{\operatorname{rad}(B)} \beta_{2,\mu}^{d-1}(x,r)^2\, \Theta_\mu^{d-1}(x,r)\, \frac{dr}{r}\, d\mu(x) \le C^2\, \mu(B) \quad\text{for every ball } B. \tag{Carleson}$$
>
> Moreover the optimal constant C is comparable to ‖𝓡^{d−1}_μ‖_{L²(μ)→L²(μ)}.

(*Mem. Amer. Math. Soc.*, to appear. The d = 2 case was known from Azzam–Tolsa via Menger
curvature.)

This is the completion of the programme. Compare the three levels:

| hypothesis on μ | geometric condition | conclusion |
|---|---|---|
| n-AD-regular | Carleson condition on β² | uniformly rectifiable (David–Semmes) |
| ℋ^n(E) < ∞ | pointwise square function finite | rectifiable (Tolsa; Azzam–Tolsa) |
| any Radon, no atoms | growth + Carleson on β²·Θ | 𝓡^{d−1}_μ bounded on L² (Dąbrowski–Tolsa) |

Note the **density weight Θ** in the third row — the same weight the speaker flagged in
§5.4. With AD-regularity gone, Θ is no longer ≈ 1 and has to be carried explicitly. The
speaker points this out and says it "should not be so surprising."

Also note that the third row characterizes *L² boundedness of the operator* directly, not
rectifiability. That is the right target once the measure is arbitrary, because an
arbitrary measure with polynomial growth need not be rectifiable in any sense — it might
have fractional dimension. The theorem says the operator does not care about
rectifiability per se; it cares about the weighted Carleson condition.

**A corollary the speaker did not mention and that is startling.** From the survey: the
condition (Carleson) is stable under bilipschitz maps, so **L² boundedness of 𝓡^{d−1}_μ is
a bilipschitz invariant**, with the operator norm controlled by the bilipschitz constant.
The survey adds: "up to now, the preceding result was not known even for the case of
invertible affine maps such as φ(x₁,…,x_d) = (2x₁, x₂,…,x_d)."

Sit with that. Until this theorem, nobody knew whether stretching a set by a factor of two
in one direction preserved the L² boundedness of the Riesz transform on it. The kernel is
not affine-invariant, and there was no way to track what a linear map does to it. Getting
a *geometric* characterization — one phrased entirely in terms of β's and densities, which
are visibly bilipschitz-stable — turns an intractable analytic question into a triviality.

That is a general lesson worth extracting, and I return to it in §9.2.

### 5.9 Removable singularities and the Painlevé problem

The speaker calls this "essentially just one slide," and says something worth noting about
motivation:

> "The initial motivation for the proof of the NTV theorem was not the application to
> harmonic measure, but the application to the study of removable singularities."

**The definitions.** A compact E ⊂ ℂ is **removable for bounded holomorphic functions** if
for every open Ω ⊃ E, every function holomorphic and bounded on Ω ∖ E extends
holomorphically to Ω. A compact E ⊂ ℝ^d is **removable for Lipschitz harmonic functions**
if for every open Ω ⊃ E, every function Lipschitz on Ω and harmonic on Ω ∖ E extends
harmonically to Ω.

The speaker's calibration point: **a single point is removable**, by Riemann's removable
singularity theorem. The question is how large a set can be and still be invisible to the
function class.

The **Painlevé problem**, from around 1900: give a metric-geometric description of the
removable sets. And the speaker's framing of the dimensional analogy is exactly right:
"the role of holomorphic functions in the plane is taken by Lipschitz harmonic functions
in higher dimensions."

**The theorem.**

> **Theorem (Nazarov–Tolsa–Volberg, 2014).** Let E ⊂ ℝ^d be compact with ℋ^{d−1}(E) < ∞.
> Then E is removable for Lipschitz harmonic functions **if and only if** E is purely
> (d−1)-unrectifiable.

The plane case for Lipschitz harmonic functions is David–Mattila, *Rev. Mat.
Iberoamericana* 16 (2000) 137–215. The plane case for **bounded holomorphic** functions is
David's celebrated 1998 theorem, which resolved **Vitushkin's conjecture** for sets of
finite length. So the theorem above is the extension of Vitushkin's conjecture to higher
dimensions — the speaker says so.

**And the four-corner Cantor set is the example.** It has finite length in the plane, it is
purely 1-unrectifiable, and therefore it is removable both for Lipschitz harmonic functions
and for bounded holomorphic functions.

Read what that means concretely. Take a bounded holomorphic function on the complement of
the four-corner set. It extends across. The set is a genuinely one-dimensional obstacle —
positive finite length — and bounded holomorphic functions cannot see it at all. Meanwhile
a circle, with the *same* one-dimensional measure, is completely opaque: 1/z on the
complement of a circle does not extend.

Length is not what determines removability. **Coherence** is.

The mechanism, once you have §5.7, is straightforward: removability is characterized by
the non-existence of measures on E with polynomial growth and bounded Riesz transform;
NToV says such a measure forces rectifiability; so removability ⟺ pure unrectifiability.

### 5.10 The one-phase problem

Back to harmonic measure, and the first of the two free boundary theorems. This is the
converse direction to the Riesz brothers and to Dahlberg: **analysis forcing geometry.**

> **Theorem (Azzam, Hofmann, Martell, Mayboroda, Mourgoglou, Tolsa, Volberg, 2016).** Let
> Ω ⊂ ℝ^d be an **arbitrary open set** and y₀ ∈ Ω. Suppose there is E ⊂ ∂Ω with
> 0 < ℋ^{d−1}(E) < ∞ such that ω^{y₀}|_E and ℋ^{d−1}|_E are mutually absolutely
> continuous. Then **E is (d−1)-rectifiable**.

(*Geom. Funct. Anal.* 26 (2016) 703–728. It solves a question of Christopher Bishop.)

The speaker emphasizes the hypothesis that is *not* there: "one interesting feature of
this theorem is that here we don't have any topological assumption on Ω. This holds for
arbitrary open sets Ω."

That is the whole distance travelled since 1916. F. and M. Riesz needed simple
connectivity in the plane. Dahlberg needed a Lipschitz graph. This needs **nothing** — not
connectivity, not a corkscrew condition, not AD-regularity of the boundary. Just: on some
piece of the boundary of finite positive measure, harmonic measure and surface measure
have the same null sets. Geometry follows.

**The proof chain, which the speaker gives in full and which is the centrepiece of the
talk.** See §6.

### 5.11 The two-phase problem, and the frozen snowflake

Now two domains instead of one.

> **Theorem (Azzam, Mourgoglou, Tolsa, Volberg, 2019).** For d ≥ 3, let Ω₁, Ω₂ ⊂ ℝ^d be
> two **disjoint** domains with harmonic measures ω₁, ω₂. Let E ⊂ ∂Ω₁ ∩ ∂Ω₂ be Borel with
> ω₁|_E and ω₂|_E mutually absolutely continuous. Then E contains a (d−1)-rectifiable
> subset F with ω₁(E ∖ F) = 0, such that ω₁|_F and ω₂|_F are both mutually absolutely
> continuous with ℋ^{d−1}|_F.

(*Amer. J. Math.* 141 (2019) 1259–1279; the planar case is Bishop's; a version under the
capacity density condition is Azzam–Mourgoglou–Tolsa, *Comm. Pure Appl. Math.* 70 (2017)
2121–2163, which additionally yields tangents ω_i-a.e.)

Two disjoint domains sharing part of their boundary. Probe the shared boundary from inside
Ω₁ with Brownian motion, then from inside Ω₂. If the two exit distributions see the same
null sets, then almost all of the harmonic measure is concentrated on a rectifiable piece,
and there it is comparable to surface measure.

**Why it is hard.** The speaker names the difficulty and it is the right one: "we don't
assume a priori the boundary to have finite ℋ^{d−1} measure. It could be very rough,
although this picture seems everything to be smooth." So there is no ambient
finite-measure hypothesis to work inside — you must *produce* σ-finiteness as part of the
conclusion.

**The frozen snowflake.** The example the speaker draws to show what the theorem is
actually saying, and it is a good one. Build a von Koch snowflake, but at each stage,
**freeze one of the segments** — leave it alone instead of replacing it with the bumped
pattern. Take Ω₁ to be the interior and Ω₂ the exterior.

Then the boundary has two parts:

- a **countable union of line segments** — the frozen ones, one per stage per location —
  which is 1-rectifiable;
- a **fractal remainder**, which has infinite length and is purely 1-unrectifiable.

One can check that interior and exterior harmonic measures are mutually absolutely
continuous on the *whole* boundary. So the theorem applies, and its conclusion is:
harmonic measure is concentrated on the rectifiable part. **All of it lives on the frozen
segments. The fractal part, despite being infinitely long, carries essentially none.**

That is exactly Kakutani's visibility intuition from §2.1, made into a theorem. The
diffusing particle overwhelmingly exits through the flat pieces. The fractal part is
infinitely long and effectively invisible.

> *[Gap, low impact: the speaker gives no precise construction of the frozen snowflake and
> no formula — "if you don't remember the precise construction, don't worry." The survey
> does not contain this example. The description above is faithful to what he said and is
> qualitative because his was.]*

**The proof route**, from the survey, because it names the tools:

1. Reduce to showing 0 < θ^{*,d−1}(x, ω₁) := limsup_{r→0} ω₁(B(x,r))/(2r)^{d−1} < ∞ for
   ω₁-a.e. x ∈ E. Given that, rectifiability of F follows from the one-phase theorem.
2. The **upper** bound is standard. The **lower** bound is the difficulty.
3. For the lower bound: suppose there is F ⊂ ∂Ω₁ ∩ ∂Ω₂ with positive ω₁ measure on which
   the density vanishes. Apply the rectifiability criterion below in a small ball at a
   density point of F. It produces a uniformly rectifiable set carrying a non-negligible
   portion of the measure, on which the density is positive — contradiction.
4. Getting the criterion's hypotheses to hold requires the **Alt–Caffarelli–Friedman
   monotonicity formula** and a delicate blowup argument in the style of Kenig–Preiss–Toro,
   plus the Green-function identity of §5.6.

**The rectifiability criterion.** The speaker explicitly declines to state it precisely —
"I will not state the precise criterion for rectifiability, but instead roughly speaking"
— and then gives the shape: a ball B, a measure μ, β small so most of the measure is near
a plane, and the **L² oscillation of 𝓡^{d−1}μ about its mean on B small**; conclusion, a
big piece of μ inside B sits on a rectifiable set, which forces that piece to be
absolutely continuous with respect to ℋ^{d−1}.

Here is the survey's precise version (Girela-Sarrión–Tolsa, *Calc. Var. PDE* 57 (2018);
the variant stated is from the CPAM two-phase paper). Write Θ^n_μ(B) = μ(B)/rad(B)^n and
P^n_μ(B) = Σ_{j≥0} 2^{−j} Θ^n_μ(2^j B).

> **Theorem.** Let μ be Radon in ℝ^d and B a ball with μ(B) > 0 such that:
> **(a)** P^{d−1}_μ(B) ≤ C₀ Θ^{d−1}_μ(B);
> **(b)** there is a (d−1)-plane L through the centre of B with
> β^{d−1,L}_{μ,1}(B) ≤ δ Θ^{d−1}_μ(B);
> **(c)** there is G_B ⊂ B with
> sup_{0<r≤2rad(B)} Θ^{d−1}_μ(x,r) + 𝓡^{d−1}_*(χ_{2B}μ)(x) ≤ C₁ Θ^{d−1}_μ(B) for x ∈ G_B,
> and μ(B ∖ G_B) ≤ δ μ(B);
> **(d)** ∫_{G_B} |𝓡^{d−1}μ − m_{μ,G_B}(𝓡^{d−1}μ)|² dμ ≤ τ Θ^{d−1}_μ(B)² μ(B).
>
> Then for δ, τ small enough (depending on C₀, C₁) there is θ > 0 and a uniformly
> (d−1)-rectifiable set Γ with μ(G_B ∩ Γ) ≥ θ μ(B).

Reading the hypotheses in the survey's own gloss: (a) is a doubling-type condition on B;
(b) says the measure in B is concentrated near a hyperplane through the centre; (c) says
that on most of B, both the density ratios and the maximal Riesz transform are controlled;
(d) is the key one — the Riesz transform has **small oscillation about its mean**.

The survey adds a candid line: "It is not clear to the author whether the assumptions in
the theorem are sharp. For example, it is natural to wonder if the assumption (b) can be
eliminated."

> *[Correction, moderate impact: the speaker says the smallness hypothesis is on the
> **β_{μ,2}** coefficient. The survey's stated version uses **β_{μ,1}**. I have quoted the
> survey. The distinction matters if you go to the source.]*

### 5.12 The quantitative boundary value problems, and where the talk stops

The last movement, which the speaker compresses into a single slide and then ends.

The setting: Ω a domain with (d−1)-AD-regular boundary, σ = ℋ^{d−1}|_{∂Ω}, cones and
non-tangential maximal function as in §2.4, and the three solvability statements (D_p),
(R_p), (N_p).

The classical results the speaker names: these problems are solvable in **L²** in Lipschitz
domains, by "deep results and very important results due to Dahlberg, Verchota, and
Dahlberg and Kenig from the 80s." Restoring the attributions from the survey:

- **Dahlberg, 1977:** (D_2) in Lipschitz domains, via the reverse Hölder inequality of
  §5.2.
- **Verchota, 1984:** (R_2) in Lipschitz domains, *J. Funct. Anal.* 59 (1984) 572–611.
- **Dahlberg and Kenig, 1987:** (R_p) and (N_p) for p ∈ (1, 2+ε) in Lipschitz domains,
  *Ann. of Math.* 125 (1987) 437–465.
- Earlier, **Fabes, Jodeit, and Rivière:** both problems for all p ∈ (1,∞) in C¹ domains.

The survey notes that all of these rest on proving the **invertibility of the double layer
potential** in L^p — which is a method you know, and which is exactly why C¹ and Lipschitz
are the natural classes for it.

And then the question that ends the talk:

> **Kenig's question (posed in his 1991 CBMS lectures; published as Problem 3.2.2 in
> *Harmonic analysis techniques for second order elliptic boundary value problems*, AMS
> 1994).** In a bounded **chord-arc** domain Ω ⊂ ℝ^d, does there exist p > 1 such that the
> regularity and Neumann problems for the Laplacian are solvable in L^p?

The speaker's closing sentence: "in the last years the introduction of these techniques
from quantitative rectifiability and other ideas have allowed to obtain many results in
this area. So I finish here."

He names none of them. That is the largest gap in the talk.

> *[Gap in the talk, structural — but low net impact on this tutorial, because the survey's
> §7 covers it in full and I restore it below. The talk poses the field's central open
> question of the 1990s and stops without saying that it has been answered, in part by the
> speaker.]*

### 5.13 The slide after the talk ended (paper, not podium)

Everything in this section is from the survey. None of it was spoken.

**First, the vocabulary of rough domains**, which is the taxonomy the field runs on:

- **Corkscrew:** for every x ∈ ∂Ω and r ∈ (0, 2diam Ω), there is a ball B ⊂ B(x,r) ∩ Ω
  with rad(B) ≥ c₁ r. *There is always room inside, at every scale.* **Two-sided
  corkscrew** demands it of the exterior too.
- **Harnack chain condition:** any two points of Ω are joined by a chain of balls staying
  in Ω, of length logarithmic in the ratio of their separation to their distance from the
  boundary. *You can get from anywhere to anywhere without squeezing.*
- **Uniform** = corkscrew + Harnack chain. **NTA** (non-tangentially accessible, from
  Jerison–Kenig) = uniform + two-sided corkscrew. **Chord-arc** = NTA + (d−1)-AD-regular
  boundary. **Two-sided chord-arc** = Ω and its exterior both chord-arc.

Note that these are *quantitative topology* conditions, and that they replace simple
connectivity. That is the higher-dimensional substitute the speaker said was missing in
§5.2.

**Second, the geometric characterization of L^p solvability of the Dirichlet problem.**
This is the headline of the survey's §7, and it is the direct answer to the question in
§1 of this tutorial.

> **Theorem (Azzam, Hofmann, Martell, Mourgoglou, Tolsa, *Invent. Math.* 222 (2020)
> 881–993).** Let Ω ⊂ ℝ^d, d ≥ 3, be open with (d−1)-AD-regular boundary satisfying the
> corkscrew condition. The following are equivalent:
> **(a)** Ω has big pieces of chord-arc subdomains;
> **(b)** harmonic measure for Ω is in local weak-A_∞.
>
> And both are equivalent to: **∂Ω is uniformly (d−1)-rectifiable and Ω satisfies the weak
> local John condition.**

Local weak-A_∞ is exactly the reverse Hölder condition of §5.2 holding for some p > 1,
which by the survey's Theorem 7.1 is exactly the L^p solvability of the Dirichlet problem.

So, in one line: **the Dirichlet problem is L^p-solvable if and only if the boundary is
uniformly rectifiable and the domain is quantitatively connected.** Geometry and
connectivity, separately necessary, jointly sufficient. That is the answer to "how rough
can the boundary be," and it is a complete answer.

**Third, a characterization that will interest you specifically**, because it is a
Littlewood–Paley statement:

> **Theorem (Hofmann–Martell–Mayboroda, and the converse by Garnett–Mourgoglou–Tolsa,
> *Duke Math. J.* 167 (2018) 1473–1524).** Let Ω ⊂ ℝ^d, d ≥ 2, be a corkscrew domain with
> (d−1)-AD-regular boundary. Then **∂Ω is uniformly (d−1)-rectifiable if and only if**
> there is C > 0 such that for every bounded harmonic u on Ω and every ball B centred on
> ∂Ω,
> $$\int_B |\nabla u(x)|^2\, \operatorname{dist}(x,\partial\Omega)\, dx \le C\, \|u\|_{L^\infty(\Omega)}^2\, \operatorname{rad}(B)^{d-1}.$$

That left-hand side is the classical Carleson measure estimate for harmonic functions —
the one that gives you Littlewood–Paley theory and the H¹–BMO duality on the half space.
The theorem says: **that estimate holds if and only if the boundary is uniformly
rectifiable.** The analytic tool and the geometric hypothesis are the same statement.

**Fourth, Kenig's question, answered.**

> **Theorem (Mourgoglou–Tolsa, *Duke Math. J.* 173 (2024) 1731–1837).** Let Ω ⊂ ℝ^d be a
> bounded corkscrew domain with (d−1)-AD-regular boundary. For p ∈ (1,∞), the Dirichlet
> problem (D_{p′}) is solvable **if and only if** the regularity problem (R̃_p) is
> solvable, where R̃ is the regularity problem stated with the Hajłasz–Sobolev norm
> ‖f‖_{Ẇ^{1,p}(∂Ω)} in place of ‖∇_t f‖_{L^p}.

Consequences the survey draws: for chord-arc domains (D_{p′}) holds for p′ large, hence
(R̃_p) holds for p small; and for **two-sided chord-arc** domains the boundary supports a
weak q-Poincaré inequality for every q ≥ 1, so ‖∇_t f‖_{L^p} ≈ ‖f‖_{Ẇ^{1,p}} and the
genuine (R_p) is solvable for p > 1 small. **Kenig's regularity question: yes.**

The Hajłasz–Sobolev detour is worth a sentence, because it is a nice piece of engineering.
On a rough boundary there may be no tangential gradient to speak of. Hajłasz's definition
sidesteps it: g is an upper gradient of f if |f(x) − f(y)| ≤ |x−y|(g(x) + g(y)) for
σ-a.e. x, y, and ‖f‖_{Ẇ^{1,p}} is the infimum of ‖g‖_{L^p} over such g. No derivative, no
chart, no smoothness — just a metric-space substitute for the mean value theorem. The
survey notes that in the absence of a connectivity condition (D_{p′}) ⟹ (R_p) can *fail*,
so the switch to R̃ is not cosmetic.

The proof strategy, one sentence from the survey, because it is a nice construction: build
an "almost harmonic extension" v of the boundary data whose distributional Laplacian
satisfies an L^p-Carleson condition and whose normal derivative is controlled by the
Hajłasz gradient, using a corona decomposition of Ω into interior Lipschitz subdomains
plus a buffer region; then a duality argument gives a one-sided Rellich inequality
‖∂_ν u‖_{L^p} ≤ C‖f‖_{Ẇ^{1,p}}; then layer potentials finish it.

**Fifth, the Neumann problem is still open.**

> **Question (survey 7.5).** Is there p > 1 such that the Neumann problem is L^p-solvable
> in chord-arc domains?

Best known: Hofmann–Mitrea–Taylor proved (N_p) for all p ∈ (1,∞) in **SKT domains** —
chord-arc with outer unit normal in VMO, which forces Reifenberg flatness,
lim_{r→0} β^{d−1}_{∞,∂Ω}(x,r) = 0 uniformly. And Mourgoglou–Tolsa (2024) get it for
chord-arc domains where (R_p) is solvable and which have **very big pieces** of Lipschitz
subdomains — the γ in the big-pieces definition taken close to 1.

The survey's own assessment: "there has been little progress since the proof of the
solvability for p ∈ (1, 2+ε) in Lipschitz domains by Dahlberg and Kenig." Forty years.
Note the asymmetry — Dirichlet is characterized completely, regularity is characterized
completely relative to Dirichlet, and Neumann is essentially where it was in 1987.

### 5.14 What else is in the paper and not in the talk

Three more topics, listed briefly so you know they exist and know they are not what the
talk did.

**Jones' analyst's traveling salesman theorem** (survey §3.1). A set E ⊂ ℝ^d is contained
in a curve of finite length if and only if Σ_{Q dyadic} β^1_{∞,E}(3Q)² ℓ(Q) < ∞, and the
length of the shortest such curve is comparable to diam(E) plus that sum. Jones for the
plane; Okikiolu for one implication in higher dimensions. This is the origin of the whole
β-coefficient enterprise and the speaker credits Jones in passing without stating it.

**Carleson's ε²-conjecture** (survey §3.4–3.5). *This is in the brief for this tutorial and
in the paper's abstract, and the talk does not mention it at all.* Stating it briefly,
labelled as paper-only: for a Jordan domain Ω₁ ⊂ ℝ² with Γ = ∂Ω₁ and Ω₂ the exterior, let
I_i(x,r) be the longest open arc of ∂B(x,r) inside Ω_i, and

$$\varepsilon(x,r) = \frac{1}{r}\max\big(|\pi r - \mathcal{H}^1(I_1(x,r))|,\ |\pi r - \mathcal{H}^1(I_2(x,r))|\big),$$

so ε(x,r) = 0 exactly when both arcs are semicircles. Then Carleson's conjecture, now a
theorem (Jaye, Tolsa, Villa, *Ann. of Math.* 194 (2021) 97–161), says
∫₀¹ ε(x,r)² dr/r < ∞ if and only if Γ has a tangent at x, up to ℋ^1-null sets; in
particular the set where the square function is finite is 1-rectifiable. Fleschler, Tolsa
and Villa extended it to ℝ^d, where the sharp coefficient involves the **Dirichlet
eigenvalues** of the two spherical caps cut out by Ω₁ and Ω₂ and the Friedland–Hayman
inequality α₁ + α₂ ≥ 2 — which is the engine of the Alt–Caffarelli–Friedman monotonicity
formula.

Following the precedent set by the Gaitsgory tutorial in this series with
Kapustin–Witten: **a suggested topic that the talk does not support gets named as absent,
not woven in.** The ε²-conjecture is real, important, and the speaker's own work. He did
not talk about it. Now you know it exists and know it is not what you heard.

**The Painlevé problem as a capacity statement** (survey §5). The talk gives removability
for sets of finite measure. The survey gives the full solution, which is about *capacity*.
Define the Lipschitz harmonic capacity κ(E) = sup |⟨Δf, 1⟩| over Lipschitz
f : ℝ^d → ℝ harmonic off E with ‖∇f‖_∞ ≤ 1 — the higher-dimensional analogue of Ahlfors'
analytic capacity γ. Then κ(E) ≈ sup{μ(E) : U_μ ≤ 1 on E}, where

$$U_\mu(x) = \sup_{r>0}\Theta^{d-1}_\mu(x,r) + \left(\int_0^\infty \beta^{d-1}_{2,\mu}(x,r)^2\, \Theta^{d-1}_\mu(x,r)\, \frac{dr}{r}\right)^{1/2}$$

is the **Jones–Wolff potential**. The survey calls this "a possible solution of the
Painlevé problem for Lipschitz harmonic functions" — a metric-geometric characterization
of an analytic capacity, which is what Painlevé asked for in 1900. Note that the integrand
is exactly the Dąbrowski–Tolsa integrand of §5.8. Everything in this subject is the same
square function.

**Two open problems worth knowing**, both from the survey and neither in the talk:

- **Vitushkin's Favard length conjecture.** Fav(E) = ∫₀^π ℋ^1(P_θ(E)) dθ, the average
  length of the shadows. For sets of finite length, positive Favard length ⟺ positive
  analytic capacity, by David's theorem plus Besicovitch. For general sets it is open in
  one direction: Jones and Murai built a set with zero Favard length and positive analytic
  capacity, so one implication is false; **whether positive Favard length implies positive
  analytic capacity is open**. Dąbrowski proved a quantitative Besicovitch projection
  theorem in 2024, which was the missing tool, but the survey says it is not yet clear
  whether it applies.
- **The dimension of harmonic measure.** Jones and Wolff: dim_H ω ≤ 1 for *any* planar
  domain. Bourgain, 1987: dim_H ω ≤ d − ε_d in ℝ^d, for some ε_d > 0 depending only on d.
  The natural guess ε_d = 1 is **false** — Wolff built a snowflake domain in ℝ^d, d ≥ 3,
  with dim_H ω > d − 1. Bishop and Jones conjecture ε_d = 1/(d−1); the survey says "at
  present there is not much evidence supporting this conjecture."

That second one is worth carrying around. In the plane, harmonic measure never has
dimension above 1 no matter how bad the domain — Brownian motion cannot spread its exit
distribution across more than a curve's worth of boundary. In three dimensions, that fails,
and nobody knows by how much.

---

## 6. The one argument

The centrepiece of the talk is the proof of the one-phase theorem (§5.10), and the speaker
gives it in full at the level of the chain of implications. It is short, it uses everything
above, and it is worth having exactly.

**Claim.** Ω ⊂ ℝ^d arbitrary open, y₀ ∈ Ω, E ⊂ ∂Ω with 0 < ℋ^{d−1}(E) < ∞, and
ω^{y₀}|_E ≪≫ ℋ^{d−1}|_E. Then E is (d−1)-rectifiable.

**Step 1 — the hypothesis gives bounded density ratios.** Mutual absolute continuity means
ω^{y₀}|_E = h·ℋ^{d−1}|_E with h positive and finite a.e. Since ℋ^{d−1}(E) < ∞, the
standard density theorem bounds the density ratios of ℋ^{d−1}|_E, and hence of ω^{y₀},
above at a.e. point of E — with a bound that may depend on the point but not on the scale.

The speaker states the outcome exactly: the quantity is "bounded uniformly in ε for almost
all points. Perhaps the bound will depend on x, but not on ε."

**Step 2 — bounded density ratios give a finite maximal Riesz transform.** Apply the Green
function estimate of §5.6:

$$\mathcal{R}_*^{d-1}\omega^{y_0}(x) \lesssim \sup_{r>0}\frac{\omega^{y_0}(B(x,r))}{r^{d-1}} < \infty \quad \text{for } \omega^{y_0}\text{-a.e. } x\in E.$$

This is the only place the PDE enters. Everything before it is measure theory and
everything after it is harmonic analysis. **The Green function identity is the entire
bridge**, and it is one differentiation of one representation formula.

**Step 3 — from a.e.-finiteness to L² boundedness on a subset.** A.e. finiteness is
qualitative; NToV wants an operator bound. The passage is standard harmonic analysis:
since 𝓡^{d−1}_* ω is finite a.e. on E, by Chebyshev it is *uniformly* bounded on a subset
of positive measure, and a T1/good-λ argument upgrades uniform pointwise bounds on a big
piece to L² boundedness there. The speaker: "using this fact and some tools from harmonic
analysis, one deduces that E contains some subset F with positive ℋ^{d−1} measure such
that the Riesz transform operator with respect to this measure is bounded in L²."

**Step 4 — NToV.** By the theorem of §5.7, F is (d−1)-rectifiable.

**Step 5 — exhaustion.** F is one subset of positive measure. Repeat on E ∖ F, which
satisfies the same hypotheses; iterate. Since rectifiability is stable under countable
unions, and the residual has measure zero by a maximality argument, **E itself is
rectifiable**. The speaker: "then by an exhaustion argument, considering many other
subsets, we deduce that E itself is n-rectifiable."

∎

**What to notice about the shape of this argument.** Steps 1, 3 and 5 are soft — measure
theory and standard harmonic analysis. Step 2 is a single identity. **All the difficulty
is concentrated in step 4**, which is the black box, and the speaker says so in as many
words: "putting all together is the main difficulty of this theory, but of course here the
main black box is this array."

That is a good architecture to recognize. The theorem looks like it is about PDE. Almost
none of the work is about PDE. The PDE contributes one differentiation, and the rest of
the labour has been exported to a statement about singular integrals on general measures
that was proved for entirely different reasons — removable singularities — eighteen years
after the problem was posed.

---

## 7. Do this by hand

Two exercises. The first is in your own field and takes ten minutes. The second is the
talk's own example and takes twenty.

### 7.1 Differentiate the Green function (10 minutes)

Start from the representation

$$G(x,y_0) = \mathcal{E}(x-y_0) - \int_{\partial\Omega}\mathcal{E}(x-z)\, d\omega^{y_0}(z),$$

where E is the fundamental solution of −Δ in ℝ^d, so that for d ≥ 3,
E(x) = |x|^{2−d}/((d−2)κ_d).

(a) Compute ∇E(x) explicitly and confirm it is a constant multiple of the Riesz kernel
x/|x|^d.

(b) Differentiate the identity in x and identify the resulting integral as a Riesz
transform. Which measure is it the Riesz transform of?

(c) Now put x near ∂Ω and y₀ deep inside. Explain in one sentence why the term
∇E(x − y₀) is harmless.

(d) Finally: what would go wrong if you tried to run the same argument with x and y₀
*both* near the boundary?

<details>
<summary>Solutions</summary>

**(a)** ∇(|x|^{2−d}) = (2−d)|x|^{1−d}·(x/|x|) = (2−d) x/|x|^d. So

$$\nabla\mathcal{E}(x) = \frac{(2-d)}{(d-2)\kappa_d}\cdot\frac{x}{|x|^{d}} = -\frac{1}{\kappa_d}\cdot\frac{x}{|x|^{d}}.$$

The Riesz kernel in codimension one is x/|x|^{(d−1)+1} = x/|x|^d. Identical up to the
constant −1/κ_d. This is the statement the speaker makes verbally and it is a one-line
check.

**(b)** Differentiating under the integral,

$$\nabla_x G(x,y_0) = \nabla\mathcal{E}(x-y_0) - \int_{\partial\Omega}\nabla\mathcal{E}(x-z)\,d\omega^{y_0}(z) = \nabla\mathcal{E}(x-y_0) - c_d\,\mathcal{R}^{d-1}\omega^{y_0}(x),$$

with c_d = −1/κ_d. It is the Riesz transform of **harmonic measure itself** — the measure
with no density, 𝓡^{d−1}ω^{y₀} in the notation of §5.5.

**(c)** If x ∈ ∂Ω (or within a small distance of it) and y₀ is deep inside Ω, then
|x − y₀| ≥ dist(y₀, ∂Ω) > 0, bounded below independently of x. The kernel |x−y₀|^{1−d} is
therefore bounded. All the singular behaviour lives in the integral term, which is exactly
the Riesz transform. That is why the identity is useful: it isolates the singular part.

**(d)** The bound in (c) fails — you can have x → y₀ and ∇E(x−y₀) blows up like
|x−y₀|^{1−d}. You would then have two singular objects and no way to attribute the
behaviour of ∇G to the Riesz transform alone. The asymmetry of the setup (pole deep,
observation point at the boundary) is load-bearing, not incidental. This is also why
harmonic measure's independence of the pole (§2.4) matters: you get to *choose* the pole
deep inside without losing generality.

**The transferable observation.** A representation formula plus one differentiation turned
a PDE object (the Green function's gradient) into a singular integral operator applied to
a measure. That move — differentiate the potential, get the operator — is available
whenever you have a fundamental solution. It is why the codimension-one Riesz transform,
and not some other operator, is *the* operator of this subject.

</details>

### 7.2 The four-corner Cantor set (20 minutes, pen and paper)

Let E be the set from §3.3. Generation k has 4^k squares Q_{k,i} of side ℓ_k = 4^{−k},
sitting at the four corners of each generation-(k−1) square.

(a) Verify Σ_i diam(Q_{k,i}) = √2 for every k. What does the k-independence tell you about
the dimension of E?

(b) Granting ℋ^1(E) = √2, compute ℋ^1(E ∩ Q) for a generation-k square Q.

(c) **The main estimate.** Fix a generation-k square Q of side ℓ = 4^{−k}, take x ∈ E ∩ Q,
and consider the ball B = B(x, 2ℓ) ⊃ Q. Show that for **every** line L there is an
absolute constant c > 0 with

$$\int_{B}\left(\frac{\operatorname{dist}(y,L)}{2\ell}\right)^2 d\mathcal{H}^1|_E(y) \ \ge\ c\,\ell,$$

and deduce β^1_{2,E}(x, 2ℓ) ≥ β₀ for an absolute β₀ > 0.

(d) Conclude that ∫₀¹ β^1_{2,E}(x,r)² dr/r = ∞ for every x ∈ E, and say which theorem of
§5.4 this is consistent with.

<details>
<summary>Solutions</summary>

**(a)** Each Q_{k,i} is a square of side 4^{−k}, so diam(Q_{k,i}) = √2·4^{−k}. There are
4^k of them. The sum is 4^k · √2 · 4^{−k} = √2.

The k-independence is the signature of dimension exactly 1 at the critical exponent. Try
the same computation with exponent s: Σ diam^s = 4^k (√2·4^{−k})^s = 2^{s/2} 4^{k(1−s)},
which → 0 for s > 1 and → ∞ for s < 1. So the Hausdorff dimension is 1, and only at s = 1
is the covering sum bounded and bounded away from zero. The scaling was *designed* to make
this happen: four pieces each scaled by 1/4 gives dimension log 4 / log 4 = 1.

**(b)** By self-similarity, E ∩ Q is a scaled copy of E by the factor 4^{−k}, and ℋ^1
scales linearly. So ℋ^1(E ∩ Q_{k,i}) = √2 · 4^{−k} = √2 ℓ. (Consistency check: 4^k pieces
× √2·4^{−k} = √2 = ℋ^1(E). ✓)

**(c)** E ∩ Q consists of four pieces, one in each of the four corner sub-squares
Q', Q'', Q''', Q'''' of side ℓ/4, sitting at the four corners of Q. Each carries ℋ^1
measure √2 ℓ/4, by (b) applied one generation down.

The four corner sub-squares are, up to their own diameter ℓ√2/4, located at the four
corners of Q. **A line cannot be close to all four corners of a square.** Concretely: let
L be any line. If L is within distance ℓ/8 of three of the four corner regions, it would
have to be within ℓ/8 of three non-collinear points separated by distance ≥ ℓ, which for a
line means those three points are within ℓ/4 of a common line — impossible for three
corners of a square of side ℓ, since the third corner is at distance ℓ/√2 ≈ 0.707ℓ from
the diagonal through the other two. So **at least two** of the four corner regions are at
distance ≥ cℓ from L, with c an absolute constant (c = 1/8 works comfortably).

Therefore

$$\int_B \left(\frac{\operatorname{dist}(y,L)}{2\ell}\right)^2 d\mathcal{H}^1|_E(y) \ \ge\ 2\cdot\frac{\sqrt{2}\,\ell}{4}\cdot\left(\frac{c\ell}{2\ell}\right)^2 = \frac{\sqrt{2}\,c^2}{8}\,\ell.$$

Since this holds for every L, taking the infimum and dividing by the normalization
r = 2ℓ gives

$$\beta^1_{2,E}(x,2\ell)^2 = \inf_L \frac{1}{2\ell}\int_B\left(\frac{\operatorname{dist}(y,L)}{2\ell}\right)^2 d\mathcal{H}^1|_E \ \ge\ \frac{\sqrt{2}\,c^2}{16} =: \beta_0^2 > 0,$$

an absolute constant independent of k and of x.

**(d)** The estimate in (c) holds at r = 2·4^{−k} for every k, and by the same argument
(with slightly worse constants) for every r in the range [4^{−k}, 4^{−k+1}] — the geometry
inside a ball of any such radius still sees four corner clusters. So β^1_{2,E}(x,r)² ≥ β₀²
on a set of scales covering (0,1] up to constants. Hence

$$\int_0^1 \beta^1_{2,E}(x,r)^2\,\frac{dr}{r} \ \ge\ \sum_{k=0}^{\infty}\beta_0^2\int_{4^{-k-1}}^{4^{-k}}\frac{dr}{r} = \sum_{k=0}^{\infty}\beta_0^2 \log 4 = \infty.$$

The square function diverges at **every** point of E, not merely almost every point.

By the theorem of §5.4 (Tolsa; Azzam–Tolsa 2015), a set of finite ℋ^1 measure is
1-rectifiable if and only if the square function is finite ℋ^1-a.e. Divergence everywhere
is therefore consistent with — and, given the theorem, equivalent to the statement that —
**no subset of positive measure is rectifiable.** That is pure 1-unrectifiability, which is
what §3.3 asserted without proof.

*Marked as reconstruction:* part (c)'s constant-chasing is mine, not the speaker's and not
the survey's. The geometric fact — four corners, no line close to more than two — is
elementary and I have given the argument. What would tighten it: a careful treatment of
the boundary case where B(x,2ℓ) straddles two generation-k squares, which changes constants
but not the conclusion, since the straddling ball contains a full generation-k square.

**The thing to carry away.** The divergence came entirely from **self-similarity**: the
same flatness defect at every scale, and Σ 1 over infinitely many octaves diverges. That
is why the dr/r measure is the right one. A set that is flat-ish but with defect decaying
like 1/k across octaves would still be rectifiable; a set with constant defect never is.
Rectifiability is not about being flat. It is about the *defect being summable*.

</details>

---

## 8. What is actually useful to you

Four transferable things, in decreasing order of how portable they are.

### 8.1 A characterization is worth more than the theorem it replaces

The pattern repeats four times in this talk and it is the same pattern each time.

- Uniform rectifiability was **defined** geometrically. David–Semmes gave it a
  **characterization** as a Carleson condition on β's. Now you can *check* it.
- L² boundedness of the Riesz transform is an **operator** statement. Dąbrowski–Tolsa gave
  it a **characterization** in terms of growth plus a weighted Carleson condition. Now you
  can check it, and — the corollary from §5.8 — you can immediately see it is a bilipschitz
  invariant, which nobody could prove before, not even for the map (x₁,…,x_d) ↦ (2x₁,…,x_d).
- L^p solvability of the Dirichlet problem is a **PDE estimate**. Azzam–Hofmann–Martell–
  Mourgoglou–Tolsa gave it a **characterization** as uniform rectifiability plus weak local
  John. Now you know exactly which domains it holds in.
- Removability is a **function-theoretic** property. NToV gave it a **characterization** as
  pure unrectifiability. Now you can decide it for a given set.

In each case the characterization does something the original definition could not: it is
*stable under operations you care about*. The bilipschitz case is the sharpest instance.
The operator-theoretic definition gave no handle on what a stretch does to it. The
geometric characterization is visibly stable under stretching, because β's and densities
are. Same theorem, and one form is usable and the other is not.

**The version for your work:** when you have a property defined by "the system behaves well
under this test," push hard for an equivalent condition stated on the *structure* rather
than on the *behaviour*. The structural form is what survives refactoring, composition, and
transport into a new setting. The behavioural form only tells you about the instance in
front of you.

### 8.2 Find the one place the hard part is concentrated, and name it a black box

Look at §6 again. Five steps. Four of them are soft. One of them is a 90-page *Acta*
paper. The speaker says so from the podium — "the main black box is this array" — and this
is a mature research habit, not a rhetorical flourish.

Being able to say *which single step carries the difficulty* is what lets you:

- reuse the argument in a new setting by checking only whether the black box still applies;
- know exactly what would break if a hypothesis changed (here: drop to 1 < n < d−1, and
  only step 4 fails, because only step 4 needed the maximum principle);
- state honestly what you have and have not proved.

The survey does this too, and precisely: the David–Semmes problem is open in intermediate
codimension for exactly one identified reason — "the absence of a suitable maximum
principle for functions of the form 𝓡^n η for n < d−1." Not "it is hard." A named
missing tool.

That is the standard to hold your own dependency analysis to. "This works because of X"
and "this would break if X went away" are the same sentence, and if you cannot write it,
you do not know why your system works.

### 8.3 Two lower-bound problems are harder than two upper-bound problems

The speaker's clearest methodological remark, from §5.7:

> "It's like when we wish to sum positive and negative numbers: we can bound from above,
> maybe with difficulty, but from below, if we want to show this is bounded away from
> zero, this could be more difficult."

The asymmetry: to bound an oscillating sum from above you may discard cancellation and use
the triangle inequality — crude, but it works. To bound it from below you must **locate**
the cancellation and show it is incomplete. There is no crude method.

This is why "rectifiable ⟹ Riesz transform bounded" was known in the 1980s and the converse
took until 2014. It is the same asymmetry that makes lower bounds hard in complexity
theory, and — from the sibling tutorial `optimization-theory-practice-wright.md` §7 — it is
why Wright reports that AI systems have been most useful in optimization for constructing
**lower bounds**, which are counterexample constructions.

Two ICM plenaries, two fields, same structural observation: the hard direction is always
the one where you must exhibit something rather than estimate something. When you are
planning work, that is where the schedule risk is.

### 8.4 The right invariant is often a square function over scales

Every characterization in this talk has the same form: a defect measured at one point and
one scale, squared, integrated dr/r, and either finite pointwise (qualitative) or
Carleson-bounded (quantitative).

That is a template, and it is more general than this subject. When you have a
multi-scale object and want a single condition that decides its global behaviour:

1. Define a **scale-invariant, dimensionless defect** at each (location, scale). Here:
   the normalized least-squares residual from the best plane.
2. **Square it and integrate against dr/r** — the invariant measure on scales, so that
   every octave counts equally.
3. Distinguish two strengths: **finite at almost every point** gives the qualitative
   conclusion; **Carleson-bounded over every box** gives the quantitative one.

The gap between those two strengths is exactly the gap between rectifiable and *uniformly*
rectifiable. And that distinction — "works a.e." versus "works with uniform constants at
every location and scale" — is the same distinction as between a property holding in the
limit and a property holding with a budget you can spend. If you have ever had a system
that was correct in the limit and useless under load, you already know which one you
actually needed.

The p = 2 detail is worth keeping too: the theorem in §5.4 is **true for p = 2 and false
for every other p**. The Hilbert-space exponent is not a convenience. It is where
orthogonality lives, and orthogonality across scales is what makes the sum converge.

---

## 9. Where to read next

1. **Tolsa, *Interactions between quantitative rectifiability, singular integrals, and
   boundary value problems for harmonic functions*.**
   [arXiv:2607.16457](https://arxiv.org/abs/2607.16457) — the proceedings paper for this
   talk. Roughly 25 pages of statements with essentially no proofs, and a 111-item
   bibliography that is the map of the field. Read §3 and §4 for the geometry and the
   operator, §6 and §7 for the PDE.
2. **Prats and Tolsa, *Notes on harmonic measure*** (to appear, 2025), at
   <https://mat.uab.es/~xtolsa/mesuraharmonica.pdf> — the speaker's own lecture notes on
   harmonic measure, cited in the survey's bibliography. This is where to go for the
   "standard estimates relating the Green function and harmonic measure" that both the
   talk and the survey wave at, and that are the one genuine gap in §5.6.
3. **Nazarov, Tolsa, and Volberg, *On the uniform rectifiability of AD-regular measures
   with bounded Riesz transform operator: the case of codimension 1*,** *Acta Math.* 213
   (2014) 237–321 — the black box. Read it only if you want the black box opened; the
   statement plus §5.7's ingredient list is enough for everything else.

---

## 10. Self-test

<details>
<summary>1. State Kakutani's theorem and say what it buys you.</summary>

For Ω bounded open, x₀ ∈ Ω, E ⊂ ∂Ω, harmonic measure ω^{x₀}(E) equals the probability
that Brownian motion started at x₀ first exits Ω through E (Kakutani, 1944).

It buys the visibility intuition that runs the whole talk: parts of the boundary that a
diffusing particle reaches easily carry large harmonic measure; parts buried in deep
recesses carry little. The frozen-snowflake example of §5.11 is that intuition as a
theorem — harmonic measure concentrates entirely on the flat segments and essentially
ignores the infinitely long fractal part.

Note: this is in the talk and **not** in the survey, which builds harmonic measure via the
maximum principle and Riesz representation instead.
</details>

<details>
<summary>2. Define n-rectifiable and purely n-unrectifiable, and give the example that separates them from Hausdorff measure.</summary>

E ⊂ ℝ^d is n-rectifiable if there are countably many Lipschitz maps g_i : ℝ^n → ℝ^d with
ℋ^n(E ∖ ⋃ g_i(ℝ^n)) = 0. E is purely n-unrectifiable if ℋ^n(E ∩ Γ) = 0 for every
n-rectifiable Γ.

The example: the four-corner Cantor set. Start with the unit square, replace by four
squares of side 1/4 at the corners, iterate. At generation k there are 4^k squares of side
4^{−k}, the diameter sum is √2 at every generation, and ℋ^1(E) = √2 — positive and finite.
Yet it is purely 1-unrectifiable. Same one-dimensional measure as a circle, none of the
structure.
</details>

<details>
<summary>3. Write down β^n_{p,μ}(x,r) and say what each factor is doing.</summary>

β^n_{p,μ}(x,r) = inf over n-planes L of ( (1/r^n) ∫_{B(x,r)} (dist(y,L)/r)^p dμ(y) )^{1/p}.

dist(y,L)/r is the distance to the candidate plane in units of the ball's radius —
dimensionless. The integral is against μ, so it sees the measure rather than the ambient
space. The 1/r^n normalizes: if μ is n-AD-regular then μ(B(x,r)) ≈ r^n, so the whole thing
is an average. The infimum over L means β measures the residual after the best plane fit.
It is a scale-invariant least-squares regression coefficient.
</details>

<details>
<summary>4. State the difference between the pointwise and Carleson forms of the square-function condition, and which notion each characterizes.</summary>

Pointwise: ∫₀¹ β^n_{2,E}(x,r)² dr/r < ∞ for ℋ^n-a.e. x ∈ E. For sets with ℋ^n(E) < ∞ this
characterizes **rectifiability** (Tolsa Part I; Azzam–Tolsa Part II, both 2015). True for
p = 2 and false for every p ≠ 2.

Carleson: ∫_{B(x,r)} ∫₀^r β^n_{p,μ}(y,t)² (dt/t) dμ(y) ≤ C μ(B(x,r)) for every ball. For
n-AD-regular μ this characterizes **uniform rectifiability** (David–Semmes), valid for
1 ≤ p ≤ 2 in every dimension.

Qualitative hypothesis gives qualitative conclusion; a uniform Carleson budget gives
uniform constants.
</details>

<details>
<summary>5. Why is the Riesz transform the operator of this subject and not some other singular integral?</summary>

Because in codimension one the Riesz kernel *is* the gradient of the fundamental solution:
x/|x|^d = −κ_d ∇E(x). So differentiating the Green function representation
G(x,y₀) = E(x−y₀) − ∫ E(x−z) dω^{y₀}(z) produces
∇_x G(x,y₀) = ∇E(x−y₀) − c_d 𝓡^{d−1}ω^{y₀}(x). The Riesz transform of harmonic measure is
the gradient of the Green function, up to a term that is bounded whenever the pole is deep
inside and the observation point near the boundary.

That single differentiation is the entire bridge between the PDE and the harmonic
analysis. In ℝ², the Riesz kernel z/|z|² is the conjugate of the Cauchy kernel 1/z, which
is why the plane case connects to complex analysis.
</details>

<details>
<summary>6. State NToV and explain why the plane was solved eighteen years earlier.</summary>

For n = 1 or n = d−1: if μ = ℋ^n|_E with ℋ^n(E) < ∞ and 𝓡^n_μ is L²(μ)-bounded, then E is
n-rectifiable; and if μ is n-AD-regular with 𝓡^n_μ L²(μ)-bounded, then μ is uniformly
n-rectifiable. (Nazarov–Tolsa–Volberg 2014 for n = d−1, d > 2; Mattila–Melnikov–Verdera
1996 and Léger 1999 for n = 1.)

The plane fell first because of **Menger curvature**: Melnikov's identity expresses the L²
norm of the Cauchy transform as a triple integral of c(x,y,z)², a manifestly *positive*
quantity, turning an oscillating-integral problem into a geometric one. There is no
positive curvature-like quantity for the Riesz kernel in higher dimensions, so the whole
method dies and one needs the maximum principle, quasiorthogonality, and Fourier estimates
instead.
</details>

<details>
<summary>7. Why is the David–Semmes problem still open for 1 < n < d−1?</summary>

Because the proof in codimension one uses the **maximum principle** to transfer L^∞ bounds
on 𝓡^{d−1}(ℋ^{d−1}|_E) from the set to the ambient space, where the Fourier transform
gives lower bounds. That works because in codimension one the Riesz transform is the
gradient of a harmonic potential. For 1 < n < d−1 it is not, and the survey names this
exactly: "the absence of a suitable maximum principle for functions of the form 𝓡^n η for
n < d−1."

An alternative route is Jaye and Nazarov's programme on **reflectionless measures**: if
every n-AD-regular reflectionless measure for 𝓡^n is n-flat (of the form c ℋ^n|_L), then
David–Semmes has a positive answer. Known only for n = 1.
</details>

<details>
<summary>8. State the one-phase theorem and give its five-step proof chain.</summary>

Theorem (Azzam–Hofmann–Martell–Mayboroda–Mourgoglou–Tolsa–Volberg, GAFA 2016): Ω ⊂ ℝ^d an
**arbitrary open set**, y₀ ∈ Ω, E ⊂ ∂Ω with 0 < ℋ^{d−1}(E) < ∞ and ω^{y₀}|_E ≪≫
ℋ^{d−1}|_E. Then E is (d−1)-rectifiable. No topological hypothesis on Ω.

Chain: (1) mutual absolute continuity plus finiteness of ℋ^{d−1}(E) gives bounded density
ratios for ω a.e. on E, uniformly in scale; (2) the Green-function estimate
𝓡_*^{d−1}ω(x) ≲ sup_r ω(B(x,r))/r^{d−1} turns that into finiteness of the maximal Riesz
transform a.e.; (3) Chebyshev plus standard harmonic analysis upgrades this to L²(μ)
boundedness on a subset F of positive measure; (4) NToV gives F rectifiable; (5) exhaust E
by such subsets and use stability of rectifiability under countable unions.

All the difficulty is in step (4).
</details>

<details>
<summary>9. What does the two-phase theorem say, and what does the frozen snowflake illustrate?</summary>

Theorem (Azzam–Mourgoglou–Tolsa–Volberg, Amer. J. Math. 2019): for d ≥ 3, Ω₁ and Ω₂
disjoint domains with harmonic measures ω₁, ω₂, and E ⊂ ∂Ω₁ ∩ ∂Ω₂ Borel with ω₁|_E ≪≫
ω₂|_E. Then E contains a (d−1)-rectifiable F with ω₁(E ∖ F) = 0 on which both ω₁ and ω₂
are mutually absolutely continuous with ℋ^{d−1}|_F.

The frozen snowflake: build a von Koch snowflake but freeze one segment at each stage. The
boundary is a countable union of segments (rectifiable) plus a fractal remainder of
infinite length that is purely 1-unrectifiable. Interior and exterior harmonic measures are
mutually absolutely continuous on the whole boundary, so the theorem applies, and its
conclusion is that harmonic measure lives entirely on the segments. The infinitely long
fractal part carries essentially none of it.
</details>

<details>
<summary>10. What is the complete geometric characterization of L^p-solvability of the Dirichlet problem, and where does it come from?</summary>

For Ω ⊂ ℝ^d, d ≥ 3, open with (d−1)-AD-regular boundary satisfying the corkscrew
condition: harmonic measure is in local weak-A_∞ (equivalently, (D_p) is solvable for some
p > 1) **if and only if** Ω has big pieces of chord-arc subdomains, equivalently **∂Ω is
uniformly (d−1)-rectifiable and Ω satisfies the weak local John condition**
(Azzam–Hofmann–Martell–Mourgoglou–Tolsa, *Invent. Math.* 222 (2020) 881–993).

Geometry of the boundary plus quantitative connectivity of the interior, both necessary,
jointly sufficient. This is **in the survey and not in the talk** — the speaker's last
slide poses Kenig's question and stops.
</details>

<details>
<summary>11. Name three things in the paper that were not in the talk.</summary>

(i) **Jones' analyst's traveling salesman theorem** — E lies on a curve of finite length
iff Σ_Q β^1_{∞,E}(3Q)² ℓ(Q) < ∞, with the shortest length comparable to that sum.

(ii) **Carleson's ε²-conjecture**, now a theorem (Jaye–Tolsa–Villa, *Ann. of Math.* 194
(2021)), and its higher-dimensional extension via Dirichlet eigenvalues on spherical caps
and the Friedland–Hayman inequality — the engine of the ACF monotonicity formula.

(iii) **The Painlevé problem as a capacity statement**: κ(E) ≈ sup{μ(E) : U_μ ≤ 1 on E}
where U_μ is the Jones–Wolff potential, built from the same β²·Θ (dr/r) integrand as
everything else.

Also: the answer to Kenig's regularity question (Mourgoglou–Tolsa, *Duke* 2024), the
bilipschitz invariance corollary, Vitushkin's Favard length conjecture, and the open
problem on the dimension of harmonic measure.
</details>

---

## 11. Note on the tutorial process

**Difficulty versus reputation.** Tolsa's reputation is geometric measure theory and the
semiadditivity of analytic capacity, and the talk is exactly what that reputation predicts
— unlike Kontorovich, whose talk was about Lean and formal verification. So Rule 1 of the
template did not bite here. What *did* bite is that the reputation predicted the wrong
**difficulty**. A geometric-measure-theory plenary sounds like a 4; against this reader's
background half of it is a 2, because harmonic measure, the Green function, layer
potentials, non-tangential maximal functions, and Brownian motion are all his. The split
rating is the honest one, and the compression of §2.4 relative to §3 follows from it.

**Anchor selection.** The speaker handed over Kakutani from the podium, which the template
identifies as the best case, and I tested it against the transcript rather than assuming
it: he states the theorem, gives the visibility intuition, and returns to it implicitly in
the snowflake example. The brief also proposed "how rough can a boundary be before the
classical PDE theory fails" as an anchor from numerical PDE; the transcript supports it
directly ("we are interested in open sets whose boundaries may be very rough, because if
the boundary is smooth then this is always true, and these domains are not interesting for
us"), so it became §1. The electrostatic reading of the Riesz transform is supported by the
speaker's own sentence that the Riesz kernel is the gradient of the fundamental solution.
The Littlewood–Paley reading of ∫β²dr/r is mine, added because it converts the talk's
central object into something the reader recognizes on sight; it is a structural
correspondence, not a decoration, since dt/t is literally the continuous dyadic sum.

**Talk/paper divergences, all flagged in place.**

| | talk | paper |
|---|---|---|
| Kakutani / Brownian motion | central to the exposition | absent entirely |
| Carleson ε²-conjecture | absent entirely | §3.4–3.5, in the abstract |
| Jones' traveling salesman theorem | Jones credited in passing | §3.1, stated in full |
| Painlevé as capacity (κ, γ, Jones–Wolff potential) | absent; removability only | §5, the paper's own framing |
| §7 boundary value problems | one slide, no results named | full section, seven theorems |
| Bishop's one-phase question | "1990" | "1992" |
| Kenig's regularity question | "early '90s" | "1991" citing a 1994 book |
| rectifiability criterion smallness hypothesis | β_{μ,**2**} | β_{μ,**1**} |

On the two date discrepancies, both sources are defensible and neither is an error.
Bishop's *Some questions concerning harmonic measure* appeared in the proceedings of a
**1990** conference in Chicago, published as an IMA volume in **1992**. Kenig's *Harmonic
analysis techniques for second order elliptic boundary value problems* is a CBMS volume of
lectures delivered in **1991** and published in **1994**. Talk and paper each picked one
end.

**Name corrections.** The auto-captions destroy every proper noun in this lecture,
beginning with the speaker's, whom the introducer's captions render as "Shabiel Tulsa."
All corrections below are verified against the survey's bibliography except where noted.

| Caption | Correct |
|---|---|
| Shabiel Tulsa / Shavier Tulsa / Shertosa | Xavier Tolsa |
| the re brothers | F. and M. Riesz (the Riesz brothers) |
| bronial motion / abonian motion / bron motion / baron trajectory | Brownian motion |
| Dalberg | Björn E. J. Dahlberg |
| lich's graph / le's domain / leis domain / lipis harmonic | Lipschitz graph / Lipschitz domain / Lipschitz harmonic |
| David Sims / David SS | Guy David and Stephen Semmes |
| Jonasa Sam / Jonas Moru | Jonas Azzam / Jonas Azzam and Mihalis Mourgoglou |
| near of myself and Borick / Nazar of myself and Warberg / Borber / Bulberg / lbert | Fedor Nazarov, Xavier Tolsa, Alexander Volberg |
| Danielski | Damian Dąbrowski |
| matila and vertera | Pertti Mattila, Mark Melnikov and Joan Verdera |
| Cadron Kman Mintosh and meer | Calderón, Coifman, McIntosh and Meyer *(see note)* |
| the nature | Jean-Christophe Léger |
| Hman Martu | Steve Hofmann, José María Martell, Mihalis Mourgoglou |
| bishop Chris Bishop | Christopher J. Bishop |
| Alafar Friedman | Alt, Caffarelli and Friedman |
| kenik presenter | Kenig, Preiss and Toro |
| Berota | Gregory Verchota |
| Carlos Kenik | Carlos Kenig |
| neighbor | Aaron Naber (with Daniele Valtorta) |
| Shul | Raanan Schul |
| vuskin conjecture / B2K conjecture | Vitushkin's conjecture |
| pale problem | Painlevé problem |
| Freeman | Riemann (removable singularity theorem) |
| vonok snowflake | von Koch snowflake |
| one quarter planner tantor set | the four-corner (one-quarter) planar Cantor set |
| alpha regular / al for regularity / AD regularity | Ahlfors regular / Ahlfors–David regularity |
| half of measure / hard measure / hers measure / heart of measure | Hausdorff measure |
| restra form / reser form / risk transform / ris transform | Riesz transform |
| direct problem / dular problem | Dirichlet problem |
| regality problem | regularity problem |
| norman problem | Neumann problem |
| llashian / llian | Laplacian |
| homorphic / holorphic / colomorphic | holomorphic |
| richest images | Lipschitz images |
| subjectivity of the analytic capacity *(introducer)* | **semiadditivity** of analytic capacity |

*Note on Calderón–Coifman–McIntosh–Meyer:* this attribution is **not** in the survey's
bibliography. The caption "Cadron Kman Mintosh and meer" in the context "works on the
Cauchy transform" is unambiguous against the standard literature — Calderón's 1977 result
for small Lipschitz constant and Coifman–McIntosh–Meyer's 1982 result in general — and I
state it, but the reader should know the companion document does not corroborate it.

*Note on Kakutani:* the survey contains no probability at all, so this attribution rests on
the talk plus general knowledge (Kakutani, *Two-dimensional Brownian motion and harmonic
functions*, Proc. Imp. Acad. Tokyo, 1944). It is entirely standard, but it is not
corroborated by the companion.

**Names I could not verify, and did not guess.**

- **"Pot"** — in "there were in fact previous results by Pot, others by Schul," describing
  earlier work on β-coefficients for non-AD-regular sets. Schul is Raanan Schul, confirmed
  from the bibliography (Azzam–Schul; Badger–Schul). "Pot" has no plausible match in the
  survey's 111-item bibliography. A reader might guess Hervé Pajot, whose work is on
  exactly this topic, but the survey does not cite him and I will not assert it.
- **"hung ... although she called [it] a regularity"** — a reference to another ICM 2026
  speaker who used Ahlfors–David regularity in her talk. Two plenary speakers at this
  congress fit the pronoun and the caption phonetics; the captions cannot discriminate and
  I have not guessed.

**Substantive caption errors corrected, not merely spellings.** Three sign-flips, of the
same kind as the "last n−k components nonzero" error flagged in
`optimization-theory-practice-wright.md`:

1. "E is **uniformly unrectifiable** if and only if the Riesz transform is bounded in L²" —
   the correct statement is **uniformly rectifiable**. As captioned it says the exact
   opposite of the theorem.
2. "then this implies that F is **unrectifiable**" in the one-phase proof sketch — should be
   **rectifiable**; the whole chain collapses otherwise.
3. "the set is **invertifiable** if and only if this integral is finite" — caption garble
   for **n-rectifiable**.

All three are corrected silently in the body text above and flagged here.

**Gaps, rated.**

- **Moderate.** The estimate |∇_x G(x,y₀)| ≲ ω^{y₀}(B(x,r))/r^{d−1}, which converts the
  Green-function identity into the density-ratio bound and is the hinge of §6 step 2. Both
  sources call it "standard estimates" and neither proves or cites it precisely. This is the
  one place a reader working from these two documents alone cannot reconstruct the argument.
  Item 2 of §9 is where to go.
- **Moderate.** The precise rectifiability criterion behind the two-phase theorem. The
  speaker explicitly declined to state it; restored from the survey's Theorem 4.6, with the
  β_1/β_2 discrepancy flagged. The survey itself says it does not know whether the
  hypotheses are sharp.
- **Low, and deliberate.** The proof of NToV. Neither source attempts a sketch beyond a
  list of ingredients. I have declared it a black box, following the Gaitsgory precedent in
  this series — stated with its motivation, its consequence, and the reason the plane was
  easier, and no manufactured proof. The speaker calls it a black box himself.
- **Low.** The frozen snowflake construction. Qualitative in the talk, absent from the
  survey, qualitative here.
- **Structural in the talk, low net here.** The final section on quantitative boundary
  value problems is one slide ending in "many results have been obtained," with none named.
  The survey's §7 restores all of it, and §5.13 above is that restoration, labelled
  paper-not-podium throughout. The single most consequential item: the talk poses Kenig's
  1991 question and does not say that the speaker himself answered the regularity half of
  it in *Duke Math. J.* 173 (2024).

**Reconstructed and marked as such.** (i) The density-theorem justification in §5.4 for
why the weighted and unweighted square functions are equivalent — my reasoning, not stated
by either source. (ii) The constants in exercise 7.2(c) — the geometric fact is elementary
and I give the argument, but the constant-chasing and the treatment of straddling balls are
mine.

**Cross-references rather than rewrites.** Two sibling tutorials in `summaries/` cover
shared material and are cited in place rather than reproduced:
`optimization-theory-practice-wright.md` §7 for the upper-bound/lower-bound asymmetry and
the counterexample-construction observation (§8.3 above), and
`langlands-function-fields-gaitsgory.md` for the precedent of declaring an object
un-teachable and saying so (§5.7 above).
