---
title: "Hamilton's Ricci Flow"
speaker: Simon Brendle (Columbia University)
source: https://www.youtube.com/watch?v=tKObU5yKXdk
video_id: tKObU5yKXdk
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: proceedings chapter exists but is inaccessible — https://doi.org/10.1137/25M1799052 — companion: https://arxiv.org/abs/2201.02522
transcript: ../transcripts/tKObU5yKXdk_transcript.txt
difficulty_for_you: 3/5
reading_time: ~65 min
---

# Hamilton's Ricci Flow — Simon Brendle

**Field:** geometric analysis. Specifically: singularity formation in a nonlinear parabolic
system, and the complete classification of the objects that describe it. Brendle opens by
dedicating the lecture to the memory of Richard Hamilton, and says in his second minute
that he will "focus exclusively on the Ricci flow."

**Difficulty against your background: 3/5, and the number hides a useful asymmetry.**

The *architecture* of this talk is your own material and you will recognise it inside
thirty seconds. A nonlinear parabolic equation blows up in finite time. Rescale at the
blow-up point using the equation's own parabolic scaling. Take a limit. The limit is an
object that has existed for infinite backward time. Classify those objects, and you have
classified the singularities. That is blow-up analysis, and it is a 1 or a 2 for you.

The *objects* are the gap. The unknown in this parabolic equation is the Riemannian metric
itself, so there is no fixed background to blow up *on*; curvature is a four-index tensor
you have probably only met contracted into Einstein's equations; and the classification is
stated in a vocabulary — soliton, neck, cap, κ-noncollapsed, ancient κ-solution — none of
which you own. That is a real 3, and it is where this document spends its length.

I have not split the rating, because the talk does not split. It is one continuous arc from
"what is a Riemannian metric" to "here are the only three singularity models in dimension
three," and the geometric vocabulary runs through all of it.

**What this tutorial builds.** Riemannian metric and curvature, in the minimum that the
talk actually uses; why −2 Ric is the Laplacian of the metric and why that makes Ricci flow
a heat equation; why that heat equation is only *weakly* parabolic and what is done about
it; solitons as fixed points modulo coordinate change; parabolic rescaling and ancient
solutions; κ-noncollapsing as a scale-invariant non-degeneracy condition; ε-necks; and then
the classification theorems and the mechanism — the Neck Improvement Theorem — that proves
them.

**A note on sources — read this before you trust any formula below.**

- **The ICM proceedings chapter exists.** Simon Brendle, *Hamilton's Ricci Flow*, in
  *Proceedings of the International Congress of Mathematicians 2026, Volume 2: Plenary
  Lectures*, SIAM, pp. 25–34, published online 13 July 2026,
  [doi:10.1137/25M1799052](https://doi.org/10.1137/25M1799052). This is the first talk in
  this folder for which a real proceedings chapter is known to exist. **I could not read
  it.** SIAM's site returns HTTP 403 to automated fetching, and no abstract is carried by
  Crossref, Semantic Scholar or OpenAlex. Crossref does confirm the title, the author, the
  volume, the page range (10 pages) and that it carries 35 references. Nothing below is
  taken from it.
- **A title discrepancy, and it is worth knowing about.** The proceedings chapter is called
  *Hamilton's Ricci Flow*. From the podium, the introducer announces the lecture as
  **"singularity models in three-dimensional Ricci flow."** I have used the proceedings
  title in the front matter because that is the ICM's own record of the lecture; the
  spoken title is what the content actually is.
- **The companion is Brendle's own survey, and it carries the spoken title exactly.**
  [arXiv:2201.02522](https://arxiv.org/abs/2201.02522), Simon Brendle, ***Singularity models
  in the three-dimensional Ricci flow*** (v1 January 2022, v2 October 2022; 30 pages;
  comments field reads "To appear in KIAS Springer Series in Mathematics, vol 1").
  **This is a companion, not the ICM chapter**, and I label it as such everywhere below. It
  earns the label as strongly as a companion can: it is by the speaker, its title is the
  title the introducer read out, and its section order is very nearly the talk's order. It
  is the source for every numbered theorem and every explicit metric in this document.
- **I scanned the transcript for a podium self-citation and found none.** The talk names no
  survey, no book and no arXiv number. Brendle names his own results by year only ("I
  proved this back in 2012"; "this is a theorem from 2018"; "in a joint work with … in
  2020"). Those years match arXiv posting dates for the three papers, which is how I
  matched them.
- **Individual results are restored from their own primary papers**, cited inline by name
  and journal, and kept visibly distinct from the companion. The companion's bibliography
  is the source of those citations.
- **No formulas survive in the captions.** Everything Brendle wrote was on slides. Every
  displayed equation below is either (i) quoted from the companion survey and cited by its
  numbered statement, (ii) standard textbook material that I label as such, or (iii) marked
  as a gap. I have filled nothing by guessing.

**Names.** The auto-captions destroy nearly every proper noun, including Perelman's, the
speaker's own, and the introducer's. Full correction table in §10.

---

## 1. What is at stake

Brendle's opening frame is Hamilton's, and it is one sentence:

> Start with a geometric object. Evolve it by a nonlinear heat equation. Deform it toward a
> standard geometry that you understand.

That is the whole programme. Heat equations smooth things out; the bet is that if you write
the right heat equation for a geometric object, it will smooth the object into one of a
short list of models you can recognise. Brendle traces the idea to Eells and Sampson's
paper on harmonic maps, and says it "really took off in 1982 with the work of Richard
Hamilton."

He lists the family:

| object being evolved | the flow | first paper |
|---|---|---|
| a Riemannian metric | **Ricci flow** | Hamilton 1982 |
| a curve in the plane | curve shortening flow | Gage and Hamilton *(see §10 on the date)* |
| a submanifold of Euclidean space | mean curvature flow | — |

"Depending on what geometric object you want to study, you would look at a different heat
equation that's tailored to that geometric object." Among them, he says, Ricci flow "has
turned out to be the most useful," and he names why: Perelman's proof of the Poincaré
conjecture, and the differentiable sphere theorem.

**And then the bet fails, on purpose.** The flow does not always smooth things out. It can
blow up in finite time. In PDE this is normally the bad case — Brendle says so explicitly:

> "In PDE, usually singularities are thought of as undesirable. Singularities are something
> we want to avoid. In Ricci flow the situation is different, in that often we cannot avoid
> singularities, and furthermore singularities often encode important geometric
> information. So the point is not to avoid singularities but to understand them."

That is the thesis of the lecture, and the next sentence is the payoff:

> "As the curvature gets large a hidden structure emerges, and understanding that hidden
> structure — this is the ultimate goal in the study of the Ricci flow."

The concrete question the talk answers is: **what does a three-dimensional Ricci flow look
like just before it blows up?** Perelman answered it qualitatively in 2002, and that was
enough for the Poincaré conjecture. The talk's news is that the answer is now *complete*:
there are exactly three models in dimension three, plus one extra in the compact case, and
nothing else can happen.

---

## 2. Your anchor

The talk hands you two anchors from the podium and the companion hands you a third. Take
all three; the first is the load-bearing one.

### 2.1 Blow-up analysis for a nonlinear heat equation — this is the whole talk

You have done this. Take the model semilinear heat equation on ℝⁿ,

$$\partial_t u = \Delta u + u^p$$

with p > 1. Solutions blow up in finite time T. You do not study the blow-up directly. You
pick a sequence of space-time points (x_j, t_j) with t_j → T where |u| → ∞, rescale using
the equation's own scaling symmetry so that the rescaled solution has size 1 at the base
point, and take a limit. What you get is a solution defined on all of ℝⁿ × (−∞, 0] — the
rescaling stretched a finite backward history into an infinite one. Then you classify
*those*, and every possible singularity is on your list.

Brendle's talk is exactly that programme, for a system where the unknown is the metric.
Here is the correspondence, item by item. The left column is yours; the right column is
what the talk spends fifty minutes on.

| semilinear heat equation ∂ₜu = Δu + uᵖ | Ricci flow ∂ₜg = −2 Ric |
|---|---|
| unknown: a scalar function on a fixed domain | unknown: **the metric itself**; there is no fixed background |
| blow-up criterion: ‖u‖<sub>∞</sub> → ∞ as t → T | blow-up criterion: curvature unbounded as t → T (Hamilton, Thm 1.4 below) |
| parabolic scaling: û(x,t) = λ<sup>2/(p−1)</sup> u(λx, λ²t) | parabolic scaling: ĝ(t) = λ² g(λ⁻²t) |
| normalise so \|u\| = 1 at the base point | normalise so scalar curvature R = 1 at the base point |
| limits taken in C<sup>∞</sup><sub>loc</sub> on a fixed ℝⁿ | limits taken in the **Cheeger–Gromov** sense — see §3.7 |
| the limit is an entire/ancient solution | the limit is an **ancient solution**: defined on (−∞, T] |
| self-similar profiles u = (T−t)<sup>−1/(p−1)</sup>φ | **solitons**: fixed points modulo coordinate change |
| extra ingredient making the list finite: a monotone functional (Giga–Kohn) | extra ingredient: Perelman's monotone 𝒲-functional ⇒ **κ-noncollapsing** |
| type I vs type II blow-up rates | shrinking cylinder (type I) vs Bryant soliton (type II) |

*(The left column and the type I/II row are mine, built to give you a handle; the talk
never mentions the semilinear heat equation or Giga–Kohn. Everything in the right column is
in the talk or the companion and is sourced below.)*

Brendle makes the parabolic-scaling point himself, and he makes it by appealing to the
linear heat equation, which tells you exactly how much background he assumes:

> "The Ricci flow is invariant under simultaneous scaling of space and time … this is a
> basic feature of many parabolic equations. So even for the standard linear heat equation
> you have this behaviour that it is invariant under simultaneous rescaling in space and
> time, and for time you have to use lambda squared if you dilate by lambda in space."

And he places the whole enterprise inside PDE, out loud:

> "Of course in PDE theory we study similar questions for any PDE. You can ask, does it
> have a global solution, or does it form a singularity in finite time?"

The companion adds one line that is worth memorising, because it tells you what kind of
object you are hunting:

> "The concept of an ancient solution to a parabolic PDE is analogous to the concept of an
> **entire solution** to an elliptic PDE." *(companion, §2)*

So: ancient solutions are the Liouville objects of parabolic theory. Classifying them is a
Liouville theorem. Every classification result in this talk is, structurally, a Liouville
theorem — and the punchline at the end of the talk is exactly that reading:

> "The property that the solution exists infinitely far back in time — this is a very rigid
> property, and these ancient solutions are much more rare than you would expect."

### 2.2 The Ricci tensor is the one from Einstein's equations

Brendle stops to say this, unprompted:

> "Let me also mention that the Ricci tensor plays a very important role not just in
> Riemannian geometry but also in relativity. So the Einstein field equations, they take
> [the Ricci tensor] equal to [the stress-energy source] for a Lorentzian metric. So the
> only difference is that in general relativity you look at Lorentzian metrics instead of
> Riemannian metrics."

So the central object is not new to you. What is new is the *use*: in general relativity
Ric is constrained algebraically by matter at each instant; here it is the right-hand side
of an evolution equation, and the metric chases it.

There is a second, sharper version of this anchor, and I flag immediately that **it is in
the companion and not in the talk.** Einstein's equations in a general coordinate system
are not hyperbolic — the diffeomorphism invariance of the theory eats one derivative's
worth of ellipticity — and you fix that by choosing harmonic (de Donder) gauge, after which
the equations become honestly hyperbolic. Ricci flow has the identical disease and the
identical cure. See §3.5.

### 2.3 Where the anchor stops

Be clear about what does **not** transfer. In the semilinear problem the domain is fixed
and only the function changes, so "rescale and take a limit" means what it usually means.
Here the metric *is* the unknown, so:

- rescaling changes what "distance" means, which is why the scaling is a scaling of *g*, not
  of coordinates;
- "the limit exists" needs an entirely new definition (Cheeger–Gromov, §3.7), because the
  underlying manifolds in the sequence need not even be the same manifold;
- and the equation is invariant under all coordinate changes, so the solution is never
  unique as a metric — only unique up to diffeomorphism. Fixed points are therefore fixed
  points *modulo the symmetry group*, which is what a soliton is.

Those three are the tax. §3 pays it.

---

## 3. The bridge

Everything here is the minimum needed to follow §4 and §5. Brendle himself spends the first
eight minutes on §3.1–§3.3, and he pitches it at exactly this level.

### 3.1 A Riemannian metric

Fix an n-dimensional manifold M and local coordinates x¹,…,xⁿ near a point. A **Riemannian
metric** is written

$$g \;=\; \sum_{i,j} g_{ij}(x)\, dx^i \, dx^j$$

where at each point the coefficients g_ij(x) form a **symmetric positive definite matrix**.
Brendle's own gloss: "you can think of this as a smooth function that takes values in the
space of positive definite matrices."

What is it for? It measures lengths of curves, and hence distances between points. For a
curve α with coordinate functions α¹,…,αⁿ,

$$L(\alpha) \;=\; \int \sqrt{\textstyle\sum_{i,j} g_{ij}(\alpha(s))\, \dot\alpha^i(s)\, \dot\alpha^j(s)} \;\, ds$$

and Brendle emphasises the one subtle bit: you evaluate g **at the point α(s)**, the point
you are currently standing on. *(This display is a transcription of what he describes in
words; the formula was on the slide.)*

The consequence he draws is the one to keep:

> On small scales near any point, a Riemannian manifold behaves approximately like Euclidean
> space, because on small scales g_ij is approximately constant. On large scales it can
> behave completely differently.

**The three model spaces.** Brendle gives the constant-curvature metrics as the simplest
examples: Euclidean space (g_ij = δ_ij on ℝⁿ), the sphere, and hyperbolic space. He says the
last two are the Euclidean metric multiplied by a point-dependent stretching factor, in
stereographic coordinates, and that hyperbolic space is obtained by "flipping a sign" and
lives on the unit ball in ℝⁿ. The standard formulas that match that description exactly are

$$g^{\text{sph}} \;=\; \frac{4}{(1+|x|^2)^2}\,\delta_{ij} \quad\text{on } \mathbb{R}^n, \qquad
g^{\text{hyp}} \;=\; \frac{4}{(1-|x|^2)^2}\,\delta_{ij} \quad\text{on } \{|x|<1\}$$

*(Restored from standard references, not from the captions. The talk's verbal description —
stereographic coordinates, flip a sign, unit ball — pins these down, and the sign flip in
the denominator is exactly the difference. I label them restored because the slide is
unreadable.)*

### 3.2 Curvature, and why it has four indices

Brendle motivates curvature from the only honest starting point:

> "Curvature was invented to detect whether or not a given metric is locally isometric to
> the Euclidean metric."

The problem is that the Euclidean metric written in spherical or otherwise curved
coordinates does not look like δ_ij. So: given g, can you change coordinates to make it
δ_ij? The **Riemann curvature tensor** R_ijkl is the object designed to answer that.

Three facts, all from the podium:

1. It is a complicated expression in the **first and second derivatives** of the metric.
   "To leading order it looks like a linear expression in the second derivatives of the
   metric, plus additional quadratic terms in the first derivatives, but let me not write
   them down."
2. It **transforms tensorially** under coordinate change. That is the whole point of the
   construction.
3. **R ≡ 0 near a point ⟺ there are coordinates in which g_ij = δ_ij near that point.** Both
   directions. Euclidean ⇒ tensor vanishes is easy; the converse is the substance.

*[Gap: the explicit formula for R_ijkl was on the slide and Brendle deliberately declined to
write out the quadratic terms. **Impact: low.** He does not use the formula anywhere in the
talk; he uses only the three facts above. The standard leading-order form —
R_ijkl = ½(∂ᵢ∂ₖg_jl + ∂ⱼ∂ₗg_ik − ∂ᵢ∂ₗg_jk − ∂ⱼ∂ₖg_il) + (quadratic in ∂g) — is in any
textbook, including the speaker's own book [Brendle, *Ricci Flow and the Sphere Theorem*,
AMS GSM 111, 2010].]*

**Contracting down.** Four indices is a lot. Trace two of them away, using g^{kl}, the
inverse matrix of g_kl:

$$\mathrm{Ric}_{ij} \;=\; g^{kl}\, R_{ikjl}, \qquad\qquad R \;=\; g^{ij}\, \mathrm{Ric}_{ij}$$

The first is the **Ricci tensor** (two indices), the second the **scalar curvature** (one
number per point). Brendle: "the Ricci and scalar curvature, they contain less information
but they're easier objects."

**And here is the analogy that unlocks the entire lecture for you.** It is his, verbatim in
substance:

> In calculus, the **Hessian** of a function is analogous to the **Riemann tensor**. Take a
> contraction of the Hessian and you get the **Laplacian**; the Laplacian of a function is
> analogous to the **Ricci tensor**. Specifically, **−2 Ric can be thought of as the
> Laplacian of the metric.**

Hold onto that. It is the reason the next equation is a heat equation.

### 3.3 Ricci flow

A one-parameter family of Riemannian metrics g(t) on M evolves by the **Ricci flow** if

$$\frac{\partial}{\partial t}\, g_{ij}(t) \;=\; -2\,\mathrm{Ric}_{g(t)}$$

*(Companion, Definition 1.1, attributed to R. Hamilton, J. Diff. Geom. **17** (1982)
255–306. Brendle states the same equation from the podium.)*

His two-sentence reading, which is the one you want:

> "You can think of this in some abstract sense as a dynamical system on the space of all
> Riemannian metrics. But what this really is, is a **nonlinear heat equation for Riemannian
> metrics.** … Keep in mind that this is nonlinear, because the Ricci tensor is nonlinear in
> the metric, and that in turn is dictated by the invariance properties that we want the
> curvature to have — that we want it to transform nicely under coordinate changes."

That last clause is not decoration. **The nonlinearity is the price of coordinate
invariance.** You cannot have a curvature that transforms tensorially and is linear in g.

### 3.4 Short-time existence, and the one dichotomy that matters

> **Theorem (Hamilton 1982; DeTurck 1983).** Let g₀ be a Riemannian metric on a compact
> manifold M. Then there exists a unique solution g(t), t ∈ [0,T), to the Ricci flow with
> g(0) = g₀, for some T > 0 depending on the initial data.
>
> *(Companion, Theorem 1.2.)*

> **Theorem (Hamilton 1982).** Let g(t), t ∈ [0,T), be the unique maximal solution. **If
> T < ∞, then the curvature of g(t) is unbounded as t → T.**
>
> *(Companion, Theorem 1.4. Brendle states this from the podium: "the solution either exists
> for all time, or it has to become singular at some finite time T, and in the latter case
> the curvature is unbounded as you approach the singular time.")*

This is precisely the alternative you know from semilinear heat equations: continue until
the norm blows up. What is different is that "the norm" is the curvature of the unknown
itself.

### 3.5 Why the heat equation is only weakly parabolic — and DeTurck's fix

**This subsection is companion-only. The talk does not mention it.** I include it because if
you take "nonlinear heat equation" seriously — and you should — you will immediately ask
where the short-time existence theorem comes from, and the honest answer is that it is not
routine.

The companion, §1, states the difficulty:

> "The main difficulty in proving Theorem 1.2 is that the Ricci flow is **weakly, but not
> strictly, parabolic**. This is due to the fact that the Ricci flow is invariant under the
> diffeomorphism group of M."

Read that as a gauge problem, because that is what it is. If g(t) solves the flow and φ is
any fixed diffeomorphism, φ*g(t) solves it too. So the symbol of the operator has a kernel
in the directions generated by the symmetry, and standard parabolic theory does not apply.

**DeTurck's trick** is to break the gauge. Fix a background family h(t) — the companion notes
the choice does not matter and can be taken t-independent. Define ξ_t := Δ_{g̃(t),h(t)} id and
run the **Ricci–DeTurck flow**

$$\frac{\partial}{\partial t}\,\tilde g(t) \;=\; -2\,\mathrm{Ric}_{\tilde g(t)} \;-\; \mathcal{L}_{\xi_t}\big(\tilde g(t)\big)$$

*(Companion, Definition 1.3.)* The extra Lie-derivative term is exactly a gauge-fixing term,
and the companion then gives the payoff in one display:

$$\frac{\partial}{\partial t}\, \tilde g_{ij} \;=\; \tilde g^{kl}\, \partial_k \partial_l\, \tilde g_{ij} \;+\; \text{lower order terms}$$

**That is a strictly parabolic quasilinear system, and it is written in a form you can read
on sight.** The principal part is g̃^{kl}∂_k∂_l — a Laplacian in the metric's own coefficients,
applied to the metric. So the slogan "Ricci flow is a heat equation for the metric" is
literally true, but only after gauge fixing; before that it is degenerate.

The dictionary back to your own background is exact:

| general relativity | Ricci flow |
|---|---|
| Einstein's equations are diffeomorphism-invariant, hence not hyperbolic as written | Ricci flow is diffeomorphism-invariant, hence not strictly parabolic as written |
| choose harmonic / de Donder gauge | run harmonic map heat flow, i.e. DeTurck's trick |
| reduced Einstein equations are honestly hyperbolic | Ricci–DeTurck flow is honestly parabolic |
| solutions correspond after applying the gauge diffeomorphism | solutions correspond via φ_t with ∂ₜφ_t = ξ_t∘φ_t |

The companion spells out both directions of that last row: given a Ricci–DeTurck solution
you integrate the vector field ξ_t to get diffeomorphisms φ_t and set g(t) = φ_t*(g̃(t));
given a Ricci flow solution you solve the harmonic map heat flow ∂ₜφ_t = Δ_{g(t),h(t)}φ_t
from φ₀ = id and set φ_t*(g̃(t)) = g(t).

**Keep the gauge idea. It reappears in §4 as the definition of a soliton and again in §6 as
the reason the linearised flow is a Lichnerowicz equation.**

### 3.6 Solitons: fixed points modulo coordinate change

A genuine fixed point of Ricci flow is a metric with Ric ≡ 0 — then ∂ₜg = 0. Brendle points
out that this is the wrong notion:

> "It turns out you should take the point of view that metrics are equivalent if they differ
> by a coordinate change. And in that sense the cigar soliton is a fixed point of Ricci flow,
> because as you evolve it, the metric changes, but it only changes by a coordinate change.
> And so geometrically it's the same."

A solution that "moves by diffeomorphisms" — g(t) is a reparameterisation of g(0) for every
t — is called a **soliton**. In gradient form the companion gives the algebraic
characterisation:

> **Definition (companion, Definition 1.5).** (M, g, f) is a **steady** gradient Ricci
> soliton if Ric = D²f. It is **shrinking** if Ric = D²f + μg with μ > 0, and **expanding**
> if Ric = D²f + μg with μ < 0.

D²f is the Hessian of the scalar function f. Read it against §3.2's analogy: Ric is the
Laplacian of the metric, and a soliton says the Laplacian of the metric equals the Hessian
of a potential, up to a constant multiple of g. The vector field ∇f is the gauge direction
along which the metric slides.

Note the direct payoff for §2.1: a soliton is a self-similar solution, and self-similar
solutions are exactly the classification targets in blow-up analysis. Solitons are also
automatically ancient, and Brendle makes the point explicitly — since they only move by
reparameterisation, they can be extended infinitely far back in time.

### 3.7 What "the limit exists" means: Cheeger–Gromov convergence

You cannot compare metrics on different manifolds, and blow-up limits will in general not
live on the manifold you started with. The companion works throughout "in the
Cheeger–Gromov sense." Unpacked:

> A pointed sequence (M_j, g_j, p_j) converges in the Cheeger–Gromov sense to (M_∞, g_∞, p_∞)
> if for every compact K ⊂ M_∞ containing p_∞, for all j large there are embeddings
> ψ_j : K → M_j with ψ_j(p_∞) = p_j such that ψ_j*(g_j) → g_∞ in C^∞ on K.

So: you do not compare the manifolds; you compare *pullbacks onto a fixed limit chart*, on
larger and larger pieces, and only up to diffeomorphism. Brendle observes from the podium
that the limits typically come out **noncompact even when the original flow was compact** —
which is exactly what you expect if you have zoomed in by an unbounded factor.

*(The definition above is standard and is my unpacking of the phrase the companion uses; the
companion states results "in the Cheeger–Gromov sense" without restating the definition.)*

### 3.8 κ-noncollapsing: the scale-invariant non-degeneracy condition

This is the one genuinely new idea in the bridge, and it is the one that makes the
classification finite. Perelman's definition, quoted exactly:

> **Definition (Perelman 2002; companion, Definition 2.2).** An ancient solution to the
> Ricci flow in dimension n is **κ-noncollapsed** if
>
> $$\mathrm{vol}_{g(t)}\big(B_{g(t)}(p,r)\big) \;\ge\; \kappa\, r^n \qquad \text{whenever} \qquad \sup_{x \in B_{g(t)}(p,r)} R(x,t) \;\le\; r^{-2}.$$

Brendle's own informal gloss, from the podium:

> "In a very informal way, non-collapsing tells us that **curvature controls volume.** If you
> have a ball of radius r such that in this ball the curvature is at most 1/r², then the
> volume is at least κ·rⁿ. And informally that says that the manifold looks n-dimensional in
> a kind of global sense, and it doesn't collapse to something lower-dimensional."

**Read the two sides as a scale-invariant pair, because that is the design.** Under
g ↦ λ²g, curvature scales like λ⁻² and volume of an r-ball like λⁿ·(r-ball at the old
scale). Both "R ≤ r⁻²" and "vol ≥ κrⁿ" are therefore unchanged by rescaling. That is not
decoration: the condition has to be scale-invariant, or it would not survive the blow-up
limit, and surviving the blow-up limit is its entire job.

*(One definitional delta worth having: the companion's Definition 2.2 uses **scalar
curvature R**; from the podium Brendle says "the maximum curvature." For nonnegatively
curved metrics — which is where it gets used, see §4.6 — the two are equivalent up to a
dimensional constant, so this is a compression rather than an error. I flag it in §10.)*

---

## 4. The talk, rebuilt

From here I follow Brendle's order.

### 4.1 The simplest solutions, and what they look like

**The shrinking sphere.** Start from a round sphere. It has positive curvature, so it
contracts. Brendle: "it just shrinks homothetically and it collapses to a point in finite
time." Explicitly, on S² with the standard metric g_{S²}:

$$g(t) \;=\; (-2t)\, g_{S^2}, \qquad t \in (-\infty, 0)$$

and on S³ with the standard metric g_{S³}:

$$g(t) \;=\; (-4t)\, g_{S^3}, \qquad t \in (-\infty, 0)$$

*(Companion, Examples 2.6 and 2.9. Both are κ-noncollapsed.)* You verify these in §6.1. Note
that they are already written as **ancient** solutions: they exist for all t < 0 and go
extinct at t = 0.

Brendle adds a caveat that is exactly the kind of thing you want to notice: "this picture is
valid in dimension greater or equal to two. A one-dimensional sphere doesn't have curvature
and therefore it doesn't shrink." A circle is flat. Keep that fact; it decides the cigar's
fate in §4.6.

**The shrinking cylinder.** On S² × ℝ,

$$g(t) \;=\; (-2t)\, g_{S^2} \;+\; dz \otimes dz, \qquad t \in (-\infty, 0)$$

*(Companion, Example 2.10; κ-noncollapsed.)* Brendle's intuition, which is the right one:
"think of this cylinder as being made up of spheres. Then these spheres shrink to points,
and in the axial direction there's no curvature, and therefore nothing happens." The
cylinder collapses to a **line**.

### 4.2 Two solitons: the cigar and the Bryant soliton

**The cigar (dimension 2, Hamilton).** Completely explicit, a conformal factor times the
Euclidean metric on ℝ²:

$$g_{ij}(t) \;=\; \frac{4}{e^{t} + |x|^{2}}\; \delta_{ij}, \qquad t \in (-\infty,\infty)$$

*(Companion, Example 2.7.)* It is rotationally symmetric, has positive curvature, moves by
diffeomorphisms, and — Brendle's picture — **opens up like a cylinder**: foliate it by
circles, and as you go to infinity the radius of the cross-sectional circles approaches a
constant.

**The Bryant soliton (dimension 3, Robert Bryant).** The higher-dimensional analogue. It
also moves by diffeomorphisms and is rotationally symmetric, but Brendle stresses that you
**cannot write it down in closed form**, and that its asymptotics are different, "because S²
has curvature while S¹ has not." Instead of opening like a cylinder, it **opens up like a
paraboloid**: at distance s from the tip, the cross-sectional radius grows like √s rather
than approaching a constant.

*(Companion, Example 2.11, citing R.L. Bryant, "Ricci flow solitons in dimension three with
SO(3)-symmetries." The √s growth rate is Brendle's own statement from the podium: "the
cross-sectional radius doesn't approach a constant, but instead it grows at a rate
proportional to square root of s approximately." The companion says only "opens up like a
paraboloid," which is the same fact.)*

That one difference — constant radius versus √s — decides everything in §4.6. It is the
single most consequential number in the talk, and you compute its consequence yourself in
§6.2.

### 4.3 The first two theorems: when the flow does smooth everything out

**Dimension 3, positive Ricci curvature.**

> **Theorem (Hamilton 1982).** Let g₀ be a metric on a compact three-manifold M with
> **positive Ricci curvature**. Then the maximal solution has T < ∞, and as t → T the
> rescaled metrics
>
> $$\frac{1}{4(T-t)}\, g(t)$$
>
> converge in C^∞ to a metric of **constant sectional curvature 1**.
>
> *(Companion, Theorem 1.7. Brendle states the qualitative version from the podium: "the
> manifold collapses to a point and it becomes round after rescaling.")*

Brendle then draws the topological consequence, and this is the template for everything
that follows: M admits a constant-curvature metric, hence M is diffeomorphic to a quotient
of S³ by standard isometries. He is careful about which half is hard: "this latter part is
easy to prove, because we completely understand constant-curvature metrics." **The analysis
is the hard part; the topology is a corollary.**

*The mechanism, restored from the companion (Brendle does not give it in the talk).* Let
λ₁ ≤ λ₂ ≤ λ₃ be the eigenvalues of the tensor R g_ij − 2 Ric_ij. Then the scalar curvature
is λ₁+λ₂+λ₃, the Ricci eigenvalues are ½(λ₂+λ₃), ½(λ₃+λ₁), ½(λ₁+λ₂), and **Ric > 0 ⟺
λ₁ + λ₂ > 0**. Hamilton proved the differential inequalities

$$\frac{\partial}{\partial t}\lambda_1 \;\ge\; \Delta \lambda_1 + \lambda_1^2 + \lambda_2\lambda_3, \qquad\qquad \frac{\partial}{\partial t}\lambda_3 \;\le\; \Delta \lambda_3 + \lambda_3^2 + \lambda_1\lambda_2$$

(both in the barrier sense) and deduced from the maximum principle a **pinching estimate**
λ₃ − λ₁ ≤ C(λ₁+λ₂)^{1−δ} for constants δ > 0 small and C large depending on the initial
data. *(Companion, §1, equations (3)–(4).)* That is a pure maximum-principle argument on a
reaction–diffusion system, and you can read every line of it with the background you have.
This is the moment to notice that the technique underneath all of geometric analysis here
is the parabolic maximum principle.

**Dimension 2, any initial metric.**

> **Theorem (Hamilton 1988; Chow 1991).** Let g₀ be any metric on S². Then T < ∞, and as
> t → T the rescaled metrics
>
> $$\frac{1}{2(T-t)}\, g(t)$$
>
> converge in C^∞ to a metric of **constant Gauss curvature 1**.
>
> *(Companion, Theorem 1.6. Hamilton proved it assuming positive scalar curvature; Chow
> removed the assumption.)*

Brendle adds two things from the podium that the companion's theorem statement does not
carry. First, **in dimension two the Ricci flow preserves the conformal structure** — "lengths
will change, areas of regions will change, but angles will not change in dimension two. But
this is not true in higher dimensions." Second, the consequence: this gives an **alternative
proof of the classical uniformization theorem**.

Notice the historical inversion Brendle flags: the two-dimensional case "historically was
understood quite a bit after the 3D case." Lower dimension, later proof.

*(A bonus from the companion, because it is a lovely object and it is exactly your kind of
mathematics. Hamilton's proof runs on a monotone entropy: for a metric on S² with positive
scalar curvature and area A,*

$$E(g) \;=\; \int_{S^2} R \,\log\!\Big(\frac{AR}{8\pi}\Big)\, d\mu$$

*is scale-invariant, is nonnegative by Gauss–Bonnet (∫R dμ = 8π) plus Jensen's inequality,
is strictly positive unless R is constant, and is **monotone decreasing under the flow**.
Companion, equation (2). A Lyapunov functional whose zero set is exactly the target.)*

### 4.4 Where it stops working: the neck pinch

Now take a **generic** metric on a compact 3-manifold. No positivity assumption. Brendle:
"then Ricci flow can develop more complicated singularities. So you can no longer expect
singularities to be modelled on round spheres."

**The neck pinch.** Take two three-spheres and join them by a thin neck. The neck looks like
S² × interval. On the neck, the cross-sectional two-spheres are small, so their curvature is
large. Brendle's account of the mechanism:

> "Because there's a lot of curvature on this neck, the neck will pinch off, and it will
> pinch off in a short time — before these big three-spheres have a chance to shrink much."

So the manifold does *not* shrink to a point. The two large spheres shrink a little; the
neck pinches; the curvature there goes to infinity; the solution ceases to exist. **The
singularity is local, and it is modelled on a family of shrinking cylinders.**

**The degenerate neck pinch.** Brendle names a second type and declines to give details:

> "The degenerate neck pinch is modelled on the Bryant soliton, in the same way that the
> ordinary neck pinch is modelled on shrinking cylinders."

*[Gap: no details on the degenerate neck pinch. **Impact: low.** He explicitly says he is
skipping them, and the classification theorem in §5 tells you everything you need about the
model — it is the Bryant soliton, and that is one of the three items on the final list.]*

### 4.5 Parabolic rescaling and the birth of an ancient solution

Here is the construction that the whole talk turns on. I give it in Brendle's own steps.

**The scaling symmetry.** If g(t) solves Ricci flow, then so does

$$\hat g(t) \;:=\; \lambda^{2}\, g(\lambda^{-2}\,t)$$

for any λ > 0. Distances are stretched by λ, times by λ². Taking λ large **zooms in**. You
verify this in §6.1; it is three lines and it turns on Ric being scale-invariant as a
(0,2)-tensor.

**The blow-up.** Suppose the flow becomes singular at finite time T. Then the curvature is
unbounded, so choose:

- times t_j ↗ T, and points p_j, with curvature at (p_j, t_j) tending to infinity;
- for each j, the rescaling factor that makes the curvature at that base point exactly **1**.

Concretely, set r_j⁻² := R(p_j, t_j) and consider g^{(j)}(t) := r_j⁻² g(r_j² t). *(Companion,
proof of Corollary 4.4.)*

**Why the limit is ancient.** This is Brendle's punchline and it is worth reading twice:

> "The important point is that in doing so we have increased distances in space by a massive
> amount, and because we have to scale time together with the rescaling in space, that means
> we also have to dilate time by a huge factor. And so then this previous flow, which had a
> back history going back by time t_j — so some finite number, but not a small number —
> after rescaling this flow has a **huge back history**. And so now if you take the limit,
> assuming that the limit exists, then in the limit you expect to get what is called an
> **ancient solution**."

That is the mechanism in one paragraph. A finite backward history, divided by a factor
going to zero, becomes an infinite one.

> **Definition (Hamilton, early 1990s; companion, Definition 2.1).** An **ancient solution**
> to the Ricci flow is a solution defined on the time interval (−∞, T] for some T.

Brendle credits Hamilton with recognising the importance of these: "he was the first to
recognize the importance of ancient solutions, and he simply defined a solution to the Ricci
flow to be ancient if it has a back history extending infinitely far back in time. So we
don't really care so much here about the future; we care that it comes from infinitely far
back in time."

### 4.6 Perelman's non-collapsing estimate, and the table it produces

Definition 3.8 was just a definition. Here is why it is the right one.

> **Theorem (Perelman 2002; companion, Theorem 2.3).** Let M be compact of dimension n and
> let g(t), t ∈ [0,T), be a solution with T < ∞. Take times t_j → T, a bounded sequence of
> radii r_j, and points p_j with
>
> $$r_j^2 \sup_{x \in B_{g(t_j)}(p_j, r_j)} R(x, t_j) \;<\; \infty.$$
>
> Then
>
> $$\liminf_{j\to\infty}\; r_j^{-n}\,\mathrm{vol}_{g(t_j)}\big(B_{g(t_j)}(p_j,r_j)\big) \;>\; 0.$$
>
> Consequently **every blow-up limit at a finite-time singularity is κ-noncollapsed.**

The companion notes that this "is a consequence of Perelman's monotonicity formula for the
𝒲-functional." Brendle states the conclusion from the podium and calls it universal: "this
is a universal property of any finite-time singularity, that it has to be κ-non-collapsed."

**Now the table.** Brendle walks through every example and asks whether it is collapsed. This
is the most useful five minutes of the talk, because it shows the condition doing work.

| solution | dimension | collapsed? | can it be a singularity model? |
|---|---|---|---|
| shrinking spheres | n ≥ 2 | **non-collapsed** | yes — and it does occur |
| "shrinking" cylinders S¹ × ℝ | 2 | **collapsed** | **no** |
| shrinking cylinders S^{n−1} × ℝ | n ≥ 3 | **non-collapsed** | yes — the neck pinch |
| cigar soliton | 2 | **collapsed** | **no** — Perelman's theorem rules it out |
| Bryant soliton | 3 | **non-collapsed** | yes — the degenerate neck pinch |

Two entries deserve comment.

**The cigar.** Brendle's reason: it "is asymptotic to a cylinder, to a 2D cylinder." Since the
2D cylinder is collapsed, so is the cigar, and Perelman's theorem eliminates it. This
matters historically — before Perelman, the cigar was the standing worry in dimension two,
and the non-collapsing estimate is what killed it.

**The 2D cylinder, and a wrinkle in the phrasing.** Brendle says "the shrinking cylinders in
2D, they happen to be collapsed." Taken literally the phrase is a compression: S¹ × ℝ is
**flat** — the circle has no curvature, as he himself said in §4.1 — so it does not shrink at
all, and it is excluded from Definition 2.5 below by the non-flatness requirement anyway.
What is true, and is the content, is that it is collapsed: a ball of radius r in a cylinder
of fixed circumference has area growing **linearly** in r, not quadratically, so no κ works.
You compute this in §6.2. *(Flagged in §10 as podium shorthand, not a caption error.)*

**Why Bryant survives and the cigar does not** is the √s versus constant asymptotics of §4.2,
and it is Brendle's own explanation: "the S² has curvature whereas S¹ does not." §6.2 turns
that sentence into arithmetic.

### 4.7 The Hamilton–Ivey estimate, and the assembled picture

One more ingredient, and it is the only genuinely three-dimensional one.

> **Theorem (Hamilton 1995; Ivey 1993; companion, Theorem 2.4).** Let g(t) be a solution on a
> compact three-manifold, and let λ₁ be the smallest eigenvalue of R g_ij − 2 Ric_ij. Then
> λ₁ satisfies a pointwise inequality λ₁ ≥ −f(R), where f satisfies lim_{s→∞} f(s)/s = 0.
>
> Consequently **every blow-up limit of the Ricci flow in dimension 3 has nonnegative
> sectional curvature.**

Read the shape of it: any negative curvature present is *sublinear* in the scalar curvature.
So when you blow up — driving R to infinity and dividing everything by it — the negative
part washes out. That is a beautiful and very PDE-flavoured argument: the estimate is proved
by the maximum principle, and its meaning is entirely about which term wins under rescaling.

Brendle assembles the three facts from the podium:

> The big picture about singularity formation in 3D:
> **(a)** singularities are modelled on ancient solutions;
> **(b)** singularity models have to be κ-noncollapsed, by Perelman's estimate;
> **(c)** singularity models in 3D have no negative curvature, by the Hamilton–Ivey pinching
> estimate.
>
> "The only part of this picture that's specific to three dimensions is the Hamilton–Ivey
> pinching estimate."

Which is exactly the definition you now want:

> **Definition (companion, Definition 2.5).** An **ancient κ-solution** to the Ricci flow in
> dimension n ∈ {2,3} is a **complete, non-flat, κ-noncollapsed ancient solution with bounded
> and nonnegative curvature**.

Every hypothesis in that definition is earned by one of (a), (b), (c). Nothing is assumed
for convenience.

### 4.8 Perelman's canonical neighbourhood theorem

Brendle notes that making the blow-up rigorous "is quite challenging from a technical point
of view," and that Perelman succeeded. The statement, in his own quantifiers:

> **Theorem (Perelman 2002).** Let (M, g(t)) be a solution to the Ricci flow on a compact
> three-manifold which forms a singularity in finite time. Then near each point where the
> curvature is large, one can approximate the solution **to any desired degree of accuracy**
> by an ancient κ-solution. Precisely: given ε > 0 there is a constant C(ε) such that the
> approximation property holds at every point where the curvature exceeds C(ε).
>
> *(Podium statement. The companion, §2, states it as: "if a solution to the Ricci flow in
> dimension 3 forms a singularity in finite time, then the high curvature regions can be
> approximated by ancient κ-solutions," citing Perelman, "The entropy formula for the Ricci
> flow and its geometric applications," arXiv:math/0211159, §12. I have not seen §12 itself
> and have not reproduced its exact hypotheses.)*

This is the reduction. **The problem is now entirely about ancient κ-solutions in dimension
3.** Everything after this point is a classification problem.

### 4.9 The two supporting estimates Brendle names and skips

He lists four ingredients underlying Perelman's proof, and says two of them he had no time
for. I restore them from the companion, flagged, because they are the reason the limits
exist at all.

1. **The Hamilton–Ivey pinching estimate** — §4.7 above.
2. **Hamilton's matrix Harnack inequality.** *[Gap: named from the podium, never stated.
   **Impact: low** — Brendle says outright "unfortunately I didn't have time to talk about"
   it, and nothing later in the talk uses it. Reference: R. Hamilton, "The formation of
   singularities in the Ricci flow," Surveys in Differential Geometry II (1995) 7–136.]*
3. **Perelman's non-collapsing estimate** — §4.6 above.
4. **Perelman's long-range curvature estimate.** Brendle: "informally, this is what lets you
   take limits." The companion gives it:

> **Theorem (Perelman; companion, Theorem 4.2).** Let (M, g(t)), t ∈ (−∞,0], be an ancient
> κ-solution in dimension 3. Then there is a function ω : [0,∞) → [0,∞), depending on κ,
> with
>
> $$R(y,t) \;\le\; R(x,t)\,\omega\big(R(x,t)\, d_{g(t)}(x,y)^2\big)$$
>
> for all x, y ∈ M and all t ≤ 0.

Stare at the argument of ω: R(x,t)·d(x,y)² is the **scale-invariant** distance from x to y,
measured in units set by the curvature at x. So the estimate says the curvature anywhere is
controlled by the curvature at your base point, times a universal function of how far away
you are in curvature units. That is precisely what you need to prevent a blow-up sequence
from losing control at large distances — and it is what gives compactness:

> **Theorem (Perelman; companion, Theorem 4.3).** Let (M^{(j)}, g^{(j)}(t)), t ∈ (−∞,0], be a
> sequence of ancient κ-solutions in dimension 3 with points p_j satisfying R(p_j, 0) = 1.
> Then after passing to a subsequence, the flows converge in the Cheeger–Gromov sense to a
> limit which is again an ancient κ-solution.

**The space of ancient κ-solutions is compact.** That is the technical heart, and everything
in §5 is an argument on a compact space.

There is also a pointwise derivative estimate that makes the C^∞ convergence go through:

> **Theorem (Perelman; companion, Theorem 4.1).** For an ancient κ-solution in dimension 3
> and each m ≥ 1, |D^m Rm| ≤ C R^{(m+2)/2}, with C depending only on m and κ.

Again scale-invariant: both sides scale like λ^{−(m+2)} under g ↦ λ²g. That is the pattern
of the entire subject — every usable estimate is scale-invariant, because the estimates have
to survive the blow-up.

### 4.10 Perelman's structure theorem: necks and caps

Now the qualitative picture of a noncompact ancient κ-solution. First, the object you need:

> **Definition (ε-neck; companion, Definition 4.5; introduced by Hamilton).** Let (x̄, t̄) be a
> point in space-time with R(x̄, t̄) = r⁻². Then (x̄, t̄) **lies at the centre of an evolving
> ε-neck** if, after rescaling by the factor r⁻¹, the parabolic neighbourhood
>
> $$B_{g(\bar t)}(\bar x,\, \varepsilon^{-1} r) \;\times\; [\,\bar t - \varepsilon^{-1}r^2,\; \bar t\,]$$
>
> is ε-close in C^{[ε⁻¹]} to a family of shrinking cylinders.

Brendle's plain reading of it: "think of a very long cylinder, and then we're allowed to
perturb that slightly. So it can be ε-close to an actual cylinder, and then we can scale it
to make it bigger or smaller." A ball of radius ε⁻¹r rescales to an interval of length 2/ε,
which is exactly the length the talk quotes.

Notice the two roles of the single parameter ε: it is simultaneously how *close* to a
cylinder (the ε in ε-close), how *long* the cylinder is (2/ε), how *many derivatives* you
control (C^{[1/ε]}), and how far *back in time* you go (ε⁻¹r²). Making ε smaller makes every
demand stricter at once.

> **Structure theorem (Perelman; companion, Corollary 4.6).** Let (M, g(t)), t ∈ (−∞,0], be a
> noncompact ancient κ-solution in dimension 3 with positive sectional curvature. Fix ε > 0
> and let M_ε be the set of points x with (x,0) **not** at the centre of an evolving ε-neck.
> Then M_ε has **finite diameter**, and
>
> $$\sup_{M_\varepsilon} R \;\le\; C(\kappa,\varepsilon)\, \inf_{M_\varepsilon} R, \qquad\qquad \sup_{M_\varepsilon} R \;\le\; C(\kappa,\varepsilon)\, \mathrm{diam}_{g(0)}(M_\varepsilon)^{-2}.$$

Brendle's podium version says the same thing in pictures: the solution "has to look like a
half-infinite **tube** with a **cap** attached on one side; in the tube part every point lies
on an ε-neck; and in the cap part the curvature is positive, the cap has controlled geometry
— there is one length scale r, the maximum curvature is between a small constant times 1/r²
and a big constant times 1/r², and the diameter is at most a constant times r."

Those are the same statement: put r = diam(M_ε) and the companion's two inequalities say the
curvature on the cap is comparable to r⁻² from both sides.

*(Two deltas between talk and paper. First, the companion assumes **positive sectional
curvature** where the talk instead excludes "a family of shrinking cylinders or a quotient of
that." These are compatible: a noncompact ancient κ-solution has nonnegative curvature by
Hamilton–Ivey, and if the curvature is not strictly positive the flow splits off a line and
you are in the cylinder case. Second, Brendle adds a remark the paper does not: the constants
degrade as ε shrinks — "the more picky you are about ε, the bigger the region you have to
exclude, and the worse these estimates are going to be.")*

The companion also supplies the fact that drives the proof, and it is worth having because
it is what "asymptotically cylindrical" means precisely:

> **Corollary (Perelman; companion, Corollary 4.4).** For a noncompact ancient κ-solution in
> dimension 3 with positive sectional curvature, take points p_j with d(p₀, p_j) → ∞ and set
> r_j⁻² := R(p_j, 0). Rescale around (p_j, 0) by r_j⁻¹. Then a subsequence converges in the
> Cheeger–Gromov sense to **a family of shrinking cylinders**.

So: far out, every such solution looks like a cylinder. That is what makes "tube plus cap"
the right picture.

### 4.11 Surgery, and the Poincaré conjecture

Brendle covers this quickly, because it is not the news.

Perelman showed that a singularity can be continued past the singular time by a **surgery
procedure** — "that was envisioned by Hamilton and then successfully carried out by
Perelman." You flow to the first singularity, cut and paste, obtain new initial data, flow
again, and repeat. The process terminates: the flow becomes **extinct** in finite time, and
for any potential counterexample to the Poincaré conjecture it must do so, which is how the
topology is reconstructed.

His summary line about the whole enterprise is worth keeping:

> "Perelman's monumental proof built on many brilliant ideas developed by Hamilton and
> Perelman over the course of several decades."

And the sentence that sets up the rest of the lecture:

> "The bottom line is that to prove the Poincaré conjecture, this **qualitative** picture is
> enough."

**Cross-reference.** The Poincaré conjecture is settled in dimension 3 by exactly this
machinery. In dimension 4 it is open — the smooth four-dimensional Poincaré conjecture is one
of the central problems of Ciprian Manolescu's plenary at this same congress. See
`summaries/knots-four-manifolds-manolescu.md`, especially its §1 and its discussion of
S⁴. Two plenaries at one congress on the same conjecture in adjacent dimensions, and the
methods have nothing in common.

---

## 5. The one argument

The talk's own news is the following theorem and its compact counterpart. Brendle introduces
it as "today we know a lot more … and in particular we can give a complete classification."

### 5.1 The theorem

> **Theorem (Brendle, 2018/2020).** Assume (M, g(t)) is a **noncompact ancient κ-solution of
> dimension 3**. Then either (M, g(t)) is isometric to a family of **shrinking cylinders**
> (or a quotient thereof), or (M, g(t)) is isometric to the **Bryant soliton**, up to scaling.
>
> *(Companion, Theorem 5.2. Primary source: S. Brendle, "Ancient solutions to the Ricci flow
> in dimension 3," Acta Math. **225** (2020) 1–102; arXiv:1811.02559, posted November 2018,
> which is the "2018" Brendle quotes from the podium. The companion notes: "Theorem 5.2
> confirms a conjecture of Perelman.")*

Brendle underlines what makes it a real theorem rather than a catalogue: "there are very few
examples of ancient κ-solutions that were known before, and the theorem says these are the
only ones."

And the compact case:

> **Theorem (Brendle, Daskalopoulos, Šešum, 2020/2021).** Assume (M, g(t)) is a **compact
> ancient κ-solution of dimension 3**. Then, up to parabolic rescaling, translation in time,
> and diffeomorphisms, (M, g(t)) is either a family of **shrinking spheres** or **Perelman's
> ancient solution**, or a quotient of these.
>
> *(Companion, Theorem 5.3. Primary source: S. Brendle, P. Daskalopoulos, N. Šešum,
> "Uniqueness of compact ancient solutions to three-dimensional Ricci flow," Invent. Math.
> **226** (2021) 579–651.)*

**Perelman's ancient solution** is the extra object in the compact case, and Brendle describes
it carefully because there is no formula for it. It is a rotationally symmetric ancient
solution on S³, defined for t ∈ (−∞, 0], not self-similar. As t → −∞ it "approximately looks
like two Bryant solitons stuck together"; as t → 0 it looks like a family of shrinking
spheres. So it **interpolates** between a long nearly-cylindrical piece capped at both ends by
Bryant-like caps, and a round shrinking sphere. *(Companion, Example 2.12; the precise
asymptotics are Angenent–Brendle–Daskalopoulos–Šešum, Comm. Pure Appl. Math. **75** (2022)
1032–1073.)*

### 5.2 The corollary — the three models

Combine Perelman's canonical neighbourhood theorem (§4.8) with Theorem 5.1, and you get the
statement the lecture exists to deliver:

> **Corollary.** Let (M, g(t)) be a solution on a compact three-manifold which forms a
> finite-time singularity. Then near each point where the curvature is large, the solution
> can be approximated **to any desired degree of accuracy** by one of exactly three models:
>
> 1. a **round sphere**, or a quotient;
> 2. a **cylinder**, or a quotient;
> 3. the **Bryant soliton**.
>
> All three do occur, and nothing else can.

Brendle's own emphasis: "all of these models do in fact occur — and even in the rotationally
symmetric setting you can get these models — and in the general case you cannot get anything
else."

### 5.3 The proof, in three steps — and the structure of the proof is the interesting part

Brendle breaks the classification into three steps and then says something about how they
fit that is more instructive than the theorem.

**Step 1 — classify the self-similar solutions that are κ-noncollapsed.**

> **Theorem (Brendle 2012/2013).** Let (M, g) be a three-dimensional complete steady gradient
> Ricci soliton which is non-flat and κ-noncollapsed. Then (M, g) is rotationally symmetric,
> and therefore isometric to the **Bryant soliton** up to scaling.
>
> *(Companion, Theorem 5.1. Primary source: S. Brendle, "Rotational symmetry of self-similar
> solutions to the Ricci flow," Invent. Math. **194** (2013) 731–764; arXiv:1202.1264, posted
> February 2012, which is the "2012" Brendle quotes.)*

Why this is the easy case, in his words: solitons "move by diffeomorphisms, so they're really
fixed points of the Ricci flow modulo reparameterisation, and as such they have a back
history going back infinitely far in time." Self-similarity collapses a parabolic problem to
an elliptic one.

**Step 2 — classify noncompact ancient κ-solutions that are rotationally symmetric.** Drop
self-similarity, impose SO(3) symmetry — "basically a warped product over a one-dimensional
object with S² fibre." Brendle's account of why this is tractable:

> "In general the Ricci flow is a very complicated nonlinear system, but in this special case
> with rotational symmetry it boils down to just a **scalar equation**, and that's easier to
> analyse."

Conclusion: the Bryant soliton is the only example.

**Step 3 — show that every noncompact ancient κ-solution is rotationally symmetric.**

**And here is the point Brendle stops to make.** Step 3 is not proved from scratch; it *uses*
Steps 1 and 2:

> "The interesting part that makes the classification possible is that **step three uses step
> one and step two**. So classifying these special examples — the subcategories of ancient
> solutions — allows you to prove the classification in general."

His sketch of the mechanism, in words, because no formula reached the captions:

1. Take an ancient solution. Go very far back in time.
2. Find a sequence of times at which the solution looks **approximately self-similar**.
3. By Step 1, at those times the solution therefore looks approximately like the **Bryant
   soliton** — hence approximately rotationally symmetric. (The times may be far apart.)
4. Propagate **forward** from those very early times and show the symmetry cannot be lost.
5. Step 2 is what closes the loop: as long as you are close to the Bryant soliton you do not
   lose rotational symmetry, and as long as you are close to rotationally symmetric you
   remain close to the Bryant soliton.

Brendle's takeaway: "these special cases are very useful to tackle the general case."

The compact theorem is proved the same way. Companion, §5: first show every compact ancient
κ-solution is rotationally symmetric — using the *noncompact* classification (Theorem 5.1
above) plus the Neck Improvement Theorem — then classify the rotationally symmetric compact
ones using the precise asymptotics.

### 5.4 The engine: why symmetry improves

Step 4 above — "propagate forward and show the symmetry cannot get lost" — is the technical
core, and it is the one thing in the talk that Brendle names but does not explain. He calls
it the **symmetry improvement principle**. The companion calls it the **Neck Improvement
Theorem** and gives the mechanism in full.

**Everything in this subsection is companion-restored. The talk contains none of it.** I
include it because it is the most transferable idea in the whole lecture (§7.1) and because
you can read every step of it.

**Why a linear parabolic equation appears.** Symmetry of a metric means Killing vector fields:
V is Killing exactly when h := 𝓛_V(g) = 0. So "approximately symmetric" should mean "there
exist vector fields V with 𝓛_V(g) small." The question is what h does under the flow. The
answer:

> **Definition (companion, Definition 6.1).** The **Lichnerowicz Laplacian** of a symmetric
> (0,2)-tensor h is
>
> $$\Delta_L h_{ik} \;:=\; \Delta h_{ik} \;+\; 2R_{ijkl}h^{jl} \;-\; \mathrm{Ric}^l_{\;i} h_{kl} \;-\; \mathrm{Ric}^l_{\;k} h_{il}.$$

> **Proposition (Brendle 2020; companion, Proposition 6.3).** Let (M, g(t)) be a Ricci flow.
> Let V(t) be a time-dependent vector field evolving by
>
> $$\frac{\partial}{\partial t} V(t) \;=\; \Delta_{g(t)} V(t) \;+\; \mathrm{Ric}_{g(t)}\big(V(t)\big)$$
>
> and set h(t) := 𝓛_{V(t)}(g(t)). Then
>
> $$\frac{\partial}{\partial t} h(t) \;=\; \Delta_{L,g(t)}\, h(t).$$

So: evolve a candidate almost-Killing field by its own heat equation, and its failure to be
Killing obeys a **linear parabolic equation** — the parabolic Lichnerowicz equation. The
companion notes that both equations are exactly the linearisations of §3.5's gauge fixing:
the V-equation is the linearised harmonic map heat flow around the identity, and the
h-equation is the linearised Ricci–DeTurck flow around g(t). The gauge machinery from the
existence theory comes back as the machinery for the classification.

**Why the maximum principle applies.** In dimension 3, with positive scalar curvature:

> **Proposition (Anderson–Chow 2005; companion, Proposition 6.5).** If h solves the parabolic
> Lichnerowicz equation, then
>
> $$\frac{\partial}{\partial t}\Big(\frac{|h|^2}{R^2}\Big) \;\le\; \Delta\Big(\frac{|h|^2}{R^2}\Big) \;+\; \frac{2}{R}\Big\langle \nabla R, \nabla \Big(\frac{|h|^2}{R^2}\Big)\Big\rangle.$$

That is a scalar drift–diffusion inequality with no zeroth-order term, so the maximum
principle applies directly to |h|²/R² — a **scale-invariant** measure of the failure of
symmetry. Same design rule as everywhere else in the subject.

**The contraction.** With a quantitative definition of "ε-symmetric" (companion, Definition
7.2: there exist three vector fields U^(1), U^(2), U^(3) on a ball of radius 100r whose Lie
derivatives are ε-small in a weighted C² norm, which are ε-nearly tangent to the CMC foliation
of the neck, and whose Gram matrix is ε-close to the identity), the payoff is:

> **Neck Improvement Theorem (Brendle 2020; companion, Theorem 7.3).** There are a large
> constant L and a small ε₁ > 0 such that the following holds. Let (x₀, t₀) lie at the centre
> of an evolving ε₁-neck with R(x₀,t₀) = r⁻². Suppose **every** point in the parabolic
> neighbourhood B_{g(t₀)}(x₀, Lr) × [t₀ − Lr², t₀) is ε-symmetric, with ε ≤ ε₁. **Then (x₀,t₀)
> is ε/2-symmetric.**

**That factor of ½ is the whole proof.** It is a strict contraction, so you iterate it: a neck
that has existed for a long time is ε/2^k-symmetric for every k, hence exactly symmetric. An
ancient solution has existed for infinite time, so on the neck the symmetry is exact.

The reason it works is Proposition 7.1 in the companion: on an exact shrinking-cylinder
background, decompose h in spherical harmonics on the S² factor. The system becomes a family
of linear heat equations in one space variable. All modes decay except the ones that are
themselves Lie derivatives of the metric — i.e. except the modes that correspond to genuine
symmetries. Given long enough, only the symmetries survive.

*[Gap: the talk states only that a "symmetry improvement principle" exists and is used. Every
formula in §5.4 is from the companion. **Impact: low for understanding the theorem, high for
understanding the proof** — without the companion, Step 4 of §5.3 is an unexplained black box,
and with it, it is a contraction argument you could have invented.]*

### 5.5 What the theorem is not

Two honest limits.

- **This is dimension 3.** The whole picture leans on Hamilton–Ivey, which Brendle explicitly
  says is the only three-dimensional ingredient. In dimension 4 and up there is no such
  pinching estimate and the classification is far less complete. The companion notes partial
  higher-dimensional results (Brendle–Naff, Geom. Topol.; Brendle–Daskalopoulos–Naff–Šešum,
  arXiv:2102.07180) but that is not this talk.
- **The talk announces no new theorem.** Everything in §5 is published: 2013, 2020, 2021. The
  lecture is a synthesis — the field's account of itself now that Perelman's conjectured
  classification is a theorem.

---

## 6. Do this by hand

Both exercises are fully recoverable: every formula comes from the companion's Examples
2.6–2.11, so **nothing in this section is reconstructed from captions.** Pen and paper, no
computer.

### 6.1 Verify the explicit solutions and the scaling symmetry (25 minutes)

You will need exactly one fact, and it is the one that makes everything work:

> **Ric is scale-invariant as a (0,2)-tensor.** For any constant c > 0, Ric(cg) = Ric(g).

*(Reason: the Christoffel symbols Γ = ½g⁻¹(∂g) are unchanged when g ↦ cg, because the c
cancels between g⁻¹ and ∂g; the Riemann tensor with all indices down scales like c, and Ric
is a contraction of it with one factor of g⁻¹, so the c cancels again. You do not need to
verify this; take it and use it.)*

You will also need: the standard round metric on Sⁿ of radius 1 has **Ric = (n−1) g_{Sⁿ}**.

**(a)** Show that g(t) = (−2t) g_{S²} on S², t ∈ (−∞,0), solves ∂ₜg = −2 Ric.

**(b)** Show that g(t) = (−4t) g_{S³} on S³, t ∈ (−∞,0), solves it.

**(c)** Generalise: start from a round Sⁿ of radius r₀ at time 0. Find the metric at time t
and the extinction time T. Check your answer against (a) and (b).

**(d)** Show that g(t) = (−2t) g_{S²} + dz ⊗ dz on S² × ℝ solves it, and say in one sentence
why the z-direction does nothing.

**(e)** Show that if g(t) solves Ricci flow then so does ĝ(t) := λ² g(λ⁻²t), for any λ > 0.

<details>
<summary>Solutions</summary>

**(a)** Write g(t) = λ(t) g_{S²} with λ(t) = −2t. By scale invariance, Ric_{g(t)} = Ric_{g_{S²}}
= (2−1) g_{S²} = g_{S²}. And ∂ₜg = λ′(t) g_{S²} = −2 g_{S²}. So

$$\partial_t g \;=\; -2\, g_{S^2} \;=\; -2\, \mathrm{Ric}_{g(t)}. \qquad \checkmark$$

**(b)** Same computation with n = 3: Ric_{g(t)} = 2 g_{S³}, and ∂ₜg = −4 g_{S³} = −2·(2 g_{S³}).
✓ Note the coefficient changed from 2 to 4 purely because Ric of the unit sphere is (n−1)g.

**(c)** Put g(t) = λ(t) g_{Sⁿ} with λ(0) = r₀². Then Ric_{g(t)} = (n−1) g_{Sⁿ} always, so
λ′(t) = −2(n−1), giving

$$\lambda(t) \;=\; r_0^2 \;-\; 2(n-1)\,t, \qquad\qquad T \;=\; \frac{r_0^2}{2(n-1)}.$$

Check against (a): n = 2 gives λ(t) = r₀² − 2t, which is (−2t) shifted so that λ(0) = r₀²;
the extinction time is r₀²/2. Against (b): n = 3 gives λ(t) = r₀² − 4t and T = r₀²/4. ✓

**Two things to take from (c).** First, the **area/volume goes to zero but the shape never
changes** — this is the purest possible instance of a self-similar singularity, and it is why
"round sphere" is one of the three models. Second, the extinction time is smaller in higher
dimension for the same radius: more curvature, faster collapse.

**(d)** The metric splits as a product, and Ricci of a product is the direct sum of the
Riccis. The ℝ factor is flat, so it contributes nothing: Ric_{g(t)} = g_{S²} ⊕ 0. Meanwhile
∂ₜg = −2 g_{S²} ⊕ 0. ✓ The z-direction does nothing because **a line has no curvature**, so
Ricci flow has no reason to move it — which is exactly Brendle's spoken intuition, that the
cylinder is made of spheres which shrink while the axis stays put.

**(e)** Write ĝ(t) = c⁻¹g(ct) with c := λ⁻². Then by the chain rule

$$\partial_t \hat g(t) \;=\; c^{-1}\cdot c\cdot (\partial_s g)(ct) \;=\; (\partial_s g)(ct) \;=\; -2\,\mathrm{Ric}_{g(ct)}$$

and by scale invariance Ric_{g(ct)} = Ric_{c⁻¹g(ct)} = Ric_{ĝ(t)}. So ∂ₜĝ = −2 Ric_{ĝ}. ✓

**The one thing to notice.** The computation works *only* because Ric is scale-invariant while
∂ₜg is not — the mismatch is what forces time to scale as the square of space. That is the
same λ² you know from the linear heat equation, arriving here for a slightly different
reason.

</details>

### 6.2 Why the Bryant soliton survives and the cigar does not (25 minutes)

This is the exercise. It converts Brendle's one-sentence explanation — "the S² has curvature
whereas S¹ does not" — into the arithmetic that decides which objects can be singularity
models. Everything you need is in §4.2 and Definition 3.8.

Recall the two asymptotic shapes, both stated by Brendle from the podium:

- the **cigar** (n = 2) opens like a **cylinder**: at large distance s from the tip, the
  cross-sectional circle has a **constant** radius;
- the **Bryant soliton** (n = 3) opens like a **paraboloid**: at large distance s from the tip,
  the cross-sectional 2-sphere has radius ≈ **√s**.

And recall the test: κ-noncollapsed means vol(B(p,r)) ≥ κ rⁿ **whenever** sup_{B(p,r)} R ≤ r⁻².

**(a)** Start with the cigar's asymptotic geometry from the explicit formula. At t = 0 the
cigar is g = 4/(1+|x|²) δ_ij on ℝ². Write δ in polar coordinates, take |x| = ρ large, and show
that the metric becomes a **flat cylinder**. What is its circumference?

**(b)** Take a point p at large arclength s from the cigar's tip, and a ball B(p, r) with
r ≤ s/2. Estimate the area of B(p,r) for large r, and estimate sup_{B(p,r)} R. Now test the
κ-noncollapsing inequality as r → ∞. What happens?

**(c)** Now the Bryant soliton. At distance s from the tip the cross-sectional sphere has
radius √s, so its scalar curvature contribution is ≈ 2/s. Take p at distance s and find the
**largest** r for which the hypothesis sup_{B(p,r)} R ≤ r⁻² still holds.

**(d)** With that r, estimate vol(B(p,r)) and test the conclusion vol ≥ κ r³. What κ do you
get?

**(e)** In one sentence: what exactly is the exponent that separates the two cases?

<details>
<summary>Solutions</summary>

**(a)** In polar coordinates δ = dρ² + ρ²dθ², so

$$g \;=\; \frac{4}{1+\rho^2}\big(d\rho^2 + \rho^2 d\theta^2\big) \;\approx\; \frac{4}{\rho^2}\,d\rho^2 \;+\; 4\,d\theta^2 \qquad (\rho \to \infty).$$

Set s := 2 log ρ, so that ds = 2 dρ/ρ and the first term becomes ds². Then

$$g \;\approx\; ds^2 \;+\; 4\, d\theta^2$$

a **flat** cylinder with cross-sectional circle of radius 2, hence circumference **4π**. This
is Brendle's "it opens up like a cylinder," made explicit. Note also that the scalar curvature
R ≈ 4/ρ² = 4e^{−s} decays **exponentially** in arclength.

**(b)** On the asymptotic cylinder, a ball of radius r around p has area

$$\mathrm{area}\big(B(p,r)\big) \;\approx\; 4\pi \cdot 2r \;=\; 8\pi\, r$$

— circumference times length, **linear in r**. Meanwhile sup_{B(p,r)} R ≈ 4e^{−(s−r)}, which
for r ≤ s/2 is ≈ 4e^{−s/2}: exponentially small. So the hypothesis R ≤ r⁻² holds for **every**
r up to s/2, once s is large. Test the conclusion:

$$\frac{\mathrm{area}(B(p,r))}{r^{2}} \;\approx\; \frac{8\pi r}{r^{2}} \;=\; \frac{8\pi}{r} \;\longrightarrow\; 0.$$

Since s is unbounded, r is unbounded, so **no κ > 0 works. The cigar is collapsed.** ∎

The same computation with n = 2 and a fixed circle radius ρ₀ shows that the 2D cylinder
S¹ × ℝ itself is collapsed — area grows like 2πρ₀·2r, linearly, against a required r². That is
the entry in Brendle's table, and note that it needs no shrinking: S¹ × ℝ is flat and static.

**(c)** On the Bryant soliton at distance s, the cross-sectional S² has radius √s, so its
scalar curvature is 2/(√s)² = 2/s. Take the curvature scale to be R ≈ c/s. The hypothesis
R ≤ r⁻² requires

$$\frac{c}{s} \;\le\; \frac{1}{r^{2}} \qquad\Longleftrightarrow\qquad r \;\le\; \sqrt{\frac{s}{c}}.$$

Take the largest admissible radius, r ≈ √(s/c) — i.e. **r grows like √s**, exactly the same
rate as the cross-sectional radius. (Take c = 1 to keep the arithmetic clean.)

**(d)** With r ≈ √s and r ≪ s, the ball B(p, r) is approximately (cross-sectional S² of radius
√s) × (interval of length 2r), so

$$\mathrm{vol}\big(B(p,r)\big) \;\approx\; 4\pi\,(\sqrt{s})^{2}\cdot 2r \;=\; 8\pi\, s\, r \;=\; 8\pi\, r^{2}\cdot r \;=\; 8\pi\, r^{3}$$

using s = r². So vol(B(p,r)) ≈ 8π r³ ≥ κ r³ with **κ ≈ 8π**. Non-collapsed. ∎

**(e)** **Whether the cross-section keeps growing at all.** Suppose the cross-sectional sphere
has radius ≈ s^a at distance s from the tip, in dimension n.

- **If a > 0**, the cross-section has curvature ≈ s^{−2a}, so the largest admissible ball radius
  is r ≈ s^a — the same rate. Then vol(B(p,r)) ≈ (s^a)^{n−1}·2r ≈ s^{a(n−1)}·s^a = s^{an}, and
  the requirement κrⁿ ≈ κ s^{an} is met with room to spare. **Non-collapsed, and the two rates
  balance exactly.** The Bryant soliton is the case a = ½.
- **If a = 0** — the cross-section stops growing — the curvature does not merely stay bounded, it
  decays to zero, so *r is no longer capped at all* and may be taken as large as you like. But
  the volume then grows in only **one** direction, linearly in r, while κrⁿ demands growth in
  **n**. **Collapsed.** The cigar is the case a = 0.

So the dividing line is not the value of the exponent but whether it is positive. The clean
summary is the one you just computed twice:

| | cross-section radius | admissible r | vol(B(p,r)) | required | verdict |
|---|---|---|---|---|---|
| cigar (n=2) | constant | unbounded | ~ 8π r | κ r² | **fails** |
| Bryant (n=3) | √s | ~ √s | ~ 8π r³ | κ r³ | **holds** |

The cigar's cross-section stops growing, so the ball can grow in only *one* direction while
the volume needed grows in *two*. The Bryant soliton's cross-section keeps growing at exactly
the rate that keeps the ball genuinely three-dimensional. **That is Brendle's "S² has curvature
whereas S¹ does not," in numbers** — a curved cross-section shrinks under the flow, and the
soliton's steady state has to open up to compensate; a flat cross-section does not, so the
soliton stays a tube.

**And this is the whole reason the classification is finite.** Without κ-noncollapsing, the
cigar (and in the compact case the King–Rosenau solution, companion Example 2.8) are perfectly
good ancient solutions and the list is longer. The condition is what prunes it.

</details>

---

## 7. What is actually useful to you

Four items, in order of how often you will reach for them. The first two are transferable
method; the third is a modelling habit; the fourth is a caution.

### 7.1 Quantitative rigidity with a contraction factor beats qualitative rigidity

The Neck Improvement Theorem (§5.4) is the single best idea in the lecture to steal.

The qualitative fact — Ricci flow preserves symmetry, because isometries of g(0) are
isometries of g(t) — is trivial and useless: it applies only to *exact* symmetry, and nothing
in a blow-up argument is ever exact. The theorem replaces it with a statement of the form

> if the neighbourhood is ε-good, the centre is **ε/2**-good

and that single factor of ½ changes everything, because **it iterates**. Run it k times and you
get ε/2^k. Run it over an infinite backward history — which you have, precisely because the
object is *ancient* — and you get zero. Approximate symmetry becomes exact symmetry.

The pattern, stated generally: *when you have a qualitative rigidity statement, look for the
quantitative version with a factor strictly less than one, and then find the structure that
lets you iterate it.* The qualitative version is a fact; the quantitative version is a tool.

The reason this is worth carrying into your own work is that it is exactly the shape of a
convergence guarantee for any iterative loop. A self-improvement claim of the form "the output
is at least as good as the input" is worth almost nothing — it permits stalling forever. A
claim of the form "the defect shrinks by a factor bounded away from 1 per round" composes, and
composing is what you actually need. If you are designing an evaluate-and-revise loop, the
question to ask about it is not "does this step help?" but "**what is the contraction factor,
and what supplies the unbounded number of rounds?**" In Brendle's proof the answer to the
second half is the infinite backward history, and it is not an accident that the theorem is
about *ancient* solutions.

*(This paragraph's application is mine. The talk says nothing about iterative systems of any
kind.)*

### 7.2 Solve the special cases and then *use them as hypotheses*

Brendle stops the lecture to point this out, which means he thinks it is the interesting
part of the proof:

> "The interesting part that makes the classification possible is that step three uses step
> one and step two."

The naive picture of a three-step proof is three independent lemmas. That is not what happens
here. Step 1 (self-similar) and Step 2 (rotationally symmetric) are each strictly easier than
the general problem — one collapses a parabolic problem to an elliptic one, the other collapses
a nonlinear system to a scalar equation. And then Step 3 does not re-prove them: it **takes a
limit into their hypotheses**. Go far enough back in time, and the general object *becomes*
approximately self-similar; now Step 1 applies; now you know it is approximately Bryant; now
Step 2 applies to keep it there.

The reusable form: *a special case is not a warm-up, it is a lemma you are going to invoke.
Choose which special cases to solve based on which ones the general object will asymptotically
fall into*, not on which ones are easiest to state. Brendle's two special cases were chosen
because the two limits available to him — t → −∞ and blow-up — deliver exactly those
hypotheses.

### 7.3 Make the invariant scale-invariant, or it will not survive the limit

Notice how many of the estimates in this talk are ratios rather than quantities:

| estimate | scale-invariant combination |
|---|---|
| κ-noncollapsing | vol(B(p,r)) / rⁿ and R·r² |
| long-range curvature (Thm 4.2) | R(x,t)·d(x,y)² |
| derivative bounds (Thm 4.1) | \|D^m Rm\| / R^{(m+2)/2} |
| Anderson–Chow (Prop 6.5) | \|h\|² / R² |
| Hamilton's 2D entropy | ∫R log(AR/8π) dμ |

**Every single one.** This is not stylistic. The entire method is "rescale by an unbounded
factor and take a limit," so any quantity that is not scale-invariant has a limit of 0 or ∞ and
tells you nothing. The design rule is: *if your argument's central move is a change of scale,
then every quantity you plan to control must be dimensionless with respect to that scale.*

That is a habit worth generalising past this subject. Any time your analysis involves taking
a limit along a family of transformations — refining a mesh, growing a dataset, shrinking a
step size — the invariants worth tracking are the ones that the transformation fixes. The
others are bookkeeping.

### 7.4 The nonlinearity was the price of a symmetry, and so was the degeneracy

Two of Brendle's remarks are the same remark, and together they are a useful caution.

- Why is Ricci flow nonlinear? Because we insisted the curvature transform correctly under
  coordinate change. Brendle: the nonlinearity "is dictated by the invariance properties that
  we want the curvature to have."
- Why is Ricci flow not strictly parabolic? Because the equation is invariant under the whole
  diffeomorphism group. *(Companion, §1.)*

So: **the symmetry you built in on purpose is also the thing that broke your standard
theory**, and the fix (DeTurck's trick / harmonic gauge) is to quotient the symmetry out,
solve, and map back. The same trilogy — invariance, degeneracy, gauge fixing — is what you
know from general relativity and from Yang–Mills, and the same trilogy is why "fixed point" had
to be replaced by "fixed point modulo the group" to get solitons.

The engineering version, which you will recognise: any system with a genuine redundancy in its
representation has no canonical solution, only an equivalence class, and comparisons only make
sense after canonicalisation. If you find yourself unable to say whether two states are the
same, check whether you forgot to fix the gauge.

*(The DeTurck half of this is companion-only; the talk covers the nonlinearity remark but never
mentions DeTurck or weak parabolicity.)*

### 7.5 A cross-reference rather than a repetition

Felix Otto's plenary at the same congress is the mirror image of this one, and the pair is
worth holding together. **Brendle uses PDE to answer questions about geometry**; **Otto uses
geometry to make sense of PDE that are otherwise ill-posed.** Both talks turn on
scale-invariance, on what survives a blow-up, and on classifying limit objects. Otto's
treatment of scale invariance in law, subcriticality, and what "zooming in" does to an
exponent is at `summaries/geometric-concepts-pde-otto.md` §4.2, and I have not duplicated it
here.

---

## 8. Where to read next

1. **Simon Brendle, *Singularity models in the three-dimensional Ricci flow*,**
   [arXiv:2201.02522](https://arxiv.org/abs/2201.02522) — the companion, 30 pages, and the
   right first stop. It is the talk with the slides restored: every theorem numbered, every
   example given by an explicit metric, and §§6–9 supply the symmetry-improvement mechanism
   the talk names but skips. Sections 1–5 are readable in an evening with what you now have.
2. **Simon Brendle, *Ancient solutions to the Ricci flow in dimension 3*,** Acta Math. **225**
   (2020) 1–102; [arXiv:1811.02559](https://arxiv.org/abs/1811.02559) — the main theorem of
   §5.1, in full. Go here if you want the Neck Improvement Theorem proved rather than
   described. It is 100 pages and it is the real thing.
3. **Peter Topping, *Lectures on the Ricci Flow*,** LMS Lecture Note Series **325**, Cambridge
   University Press, 2006 — the companion's own reference for background. Free from the
   author's page, and the shortest route to a working command of the Riemannian geometry that
   §3 compressed into six pages. Read this instead of a general Riemannian geometry text: it
   teaches only what Ricci flow uses.

*(A fourth, if you want the primary source for the qualitative theory rather than the
classification: G. Perelman, "The entropy formula for the Ricci flow and its geometric
applications," [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§11–12. That is where
Theorems 4.1–4.3 and the canonical neighbourhood theorem live.)*

---

## 9. Self-test

<details>
<summary>1. Why is ∂ₜg = −2 Ric a heat equation, and why is it nonlinear?</summary>

Because −2 Ric plays the role of the Laplacian of the metric: the Riemann tensor is analogous
to the Hessian of a function, and Ricci is the contraction of it, analogous to the Laplacian.
It is nonlinear because Ric is a nonlinear function of g — and Brendle's point is that this is
forced: you cannot have a curvature that transforms correctly under coordinate change and is
linear in the metric. The nonlinearity is the price of coordinate invariance.
</details>

<details>
<summary>2. Explain, in the speaker's own logic, why a blow-up limit is an <em>ancient</em> solution.</summary>

You rescale around points (p_j, t_j) with curvature tending to infinity, by exactly the factor
that brings the curvature at the base point back to 1. That factor is unbounded. Because the
scaling is parabolic, time must be dilated by the square of the spatial factor. So the finite
backward history t_j that the original flow had becomes, after rescaling, an enormous one — and
in the limit, infinite. A solution with an infinite backward history is called ancient
(Hamilton, early 1990s). The companion adds the right analogy: ancient is to parabolic what
entire is to elliptic, so classifying ancient solutions is a Liouville theorem.
</details>

<details>
<summary>3. State the κ-noncollapsing condition and say why both of its sides had to be scale-invariant.</summary>

vol_{g(t)}(B(p,r)) ≥ κ rⁿ whenever sup_{B(p,r)} R ≤ r⁻² (Perelman; companion Definition 2.2).
Under g ↦ λ²g the scalar curvature scales like λ⁻² and volumes like λⁿ, so both "R ≤ r⁻²" and
"vol ≥ κrⁿ" are unchanged. That is mandatory: the condition's entire job is to be inherited by
blow-up limits, and a condition that is not scale-invariant would be destroyed by the very
rescaling it has to survive. Brendle's informal gloss: curvature controls volume, and the
manifold does not collapse to something lower-dimensional.
</details>

<details>
<summary>4. Why is the cigar soliton not a singularity model, but the Bryant soliton is?</summary>

Asymptotics. The cigar opens like a cylinder, so its cross-sectional circle has constant
radius; a ball of radius r therefore has area growing linearly in r, against the r² that
noncollapsing demands, and no κ works — it is collapsed, and Perelman's theorem rules it out.
The Bryant soliton opens like a paraboloid, cross-sectional radius ≈ √s at distance s, and the
largest admissible ball radius is also ≈ √s, giving volume ≈ 8πr³ against the required κr³ — it
is non-collapsed, and it does occur, as the model for the degenerate neck pinch. Brendle's
one-line reason: S² has curvature, S¹ does not.
</details>

<details>
<summary>5. What is an ancient κ-solution, and where does each hypothesis come from?</summary>

A complete, non-flat, κ-noncollapsed ancient solution with bounded and nonnegative curvature,
in dimension 2 or 3 (companion, Definition 2.5). "Ancient" comes from the blow-up construction;
"κ-noncollapsed" comes from Perelman's noncollapsing theorem, which says every finite-time
singularity model has it; "nonnegative curvature" comes from the Hamilton–Ivey pinching
estimate, which is the only three-dimension-specific ingredient in the picture.
</details>

<details>
<summary>6. State the classification theorem in the noncompact case and its corollary for singularities.</summary>

Every noncompact ancient κ-solution in dimension 3 is, up to scaling, either a family of
shrinking cylinders (or a quotient) or the Bryant soliton (Brendle, Acta Math. 225 (2020)
1–102; confirming a conjecture of Perelman). Combined with Perelman's canonical neighbourhood
theorem, the corollary is that near every high-curvature point of a finite-time singularity in
dimension 3, the solution is approximated to any desired accuracy by one of exactly three
models: a round sphere or quotient, a cylinder or quotient, or the Bryant soliton. All three
occur; nothing else can. In the compact case there is one extra ancient κ-solution — Perelman's
solution on S³ — and Brendle–Daskalopoulos–Šešum (Invent. Math. 226 (2021) 579–651) show
shrinking spheres and Perelman's solution are the only ones.
</details>

<details>
<summary>7. Why does step three of the proof use steps one and two, rather than standing alone?</summary>

Because the general object falls into the special cases in the limit. Go very far back in time
and you find times at which the solution looks approximately self-similar; step one then says it
looks approximately like the Bryant soliton, hence approximately rotationally symmetric; and
step two supplies the stability that lets you propagate that symmetry forward without losing it
— close to Bryant means you do not lose rotational symmetry, and close to rotationally symmetric
means you stay close to Bryant. The special cases are not warm-ups; they are the hypotheses that
the limiting argument delivers.
</details>

<details>
<summary>8. What is the Neck Improvement Theorem and why does the factor ½ matter?</summary>

If every point of a parabolic neighbourhood B(x₀, Lr) × [t₀ − Lr², t₀) of the centre of an
ε₁-neck is ε-symmetric (ε ≤ ε₁), then (x₀, t₀) is ε/2-symmetric (companion, Theorem 7.3). The
½ matters because it is a strict contraction and therefore iterates: an ancient solution has
infinite backward time, so applying it repeatedly drives the asymmetry to zero and the neck is
exactly rotationally symmetric. The underlying mechanism is that h = 𝓛_V(g) obeys the linear
parabolic Lichnerowicz equation, and |h|²/R² obeys a maximum principle (Anderson–Chow); on a
cylinder background, decomposing in spherical harmonics kills every mode except the ones that
are genuine symmetries.
</details>

<details>
<summary>9. Why is Ricci flow only weakly parabolic, and what is done about it?</summary>

Because it is invariant under the entire diffeomorphism group of M, so the linearisation has a
kernel in the gauge directions and standard parabolic theory does not apply. DeTurck's trick
adds a Lie-derivative term along ξ_t = Δ_{g̃,h} id, producing the Ricci–DeTurck flow, whose
principal part is g̃^{kl}∂_k∂_l g̃_ij — strictly parabolic. Solutions of the two flows correspond
via a family of diffeomorphisms solving the harmonic map heat flow. This is the exact analogue
of choosing harmonic gauge to make Einstein's equations hyperbolic. *(Companion §1; the talk
does not cover this.)*
</details>

<details>
<summary>10. Which part of the three-dimensional picture is genuinely three-dimensional?</summary>

Only the Hamilton–Ivey pinching estimate, which forces blow-up limits to have nonnegative
sectional curvature. Brendle says this explicitly. The rest — singularities are modelled on
ancient solutions, and singularity models are κ-noncollapsed — holds in any dimension. That is
why the classification is complete in dimension 3 and far less complete above it.
</details>

---

## 10. Note on the tutorial process

**Difficulty versus reputation.** Reputation would have got this badly wrong in one direction
and mildly wrong in the other. Brendle's most-cited recent work is on scalar curvature and the
positive mass theorem — the introduction names his proof of the positive mass theorem in all
dimensions with his student Yipeng Wang as a headline result — and none of that appears in the
lecture. He announces in his second minute that he will "focus exclusively on the Ricci flow,"
and he keeps to it. The brief for this tutorial flagged the narrowing in advance and the
transcript confirms it. In the other direction, reputation would have predicted difficulty 4 or
5 for a geometric-analysis plenary; the actual talk is a 3, because Brendle spends eight minutes
building Riemannian geometry from zero and because the argument's skeleton is blow-up analysis
for a parabolic equation, which is home ground for this reader.

**What earned the difficulty 3.** Not the strategy — the strategy is standard PDE. The
vocabulary: metric-as-unknown, curvature tensors, Cheeger–Gromov convergence, solitons, necks,
noncollapsing. §3 is six sections long because that is what the gap actually costs.

**Name corrections.** The auto-captions destroy nearly every proper noun. Each correction below
is verified against the companion's bibliography, the speaker's publication record, or a primary
source; none is a phonetic guess.

| Caption | Correct |
|---|---|
| Simon Brandler | **Simon Brendle** |
| Colombia University | **Columbia** University |
| Mich / Mikail Aishmire | **Michael Eichmair** (introducer; Chair of Global Analysis and Differential Geometry, University of Vienna) |
| Gahatus | **Gerhard Huisken** (Brendle's doctoral adviser, Tübingen 2001) |
| Richard Shane | Richard **Schoen** |
| the loss and conjecture | the **Lawson** conjecture |
| sharp isoparametric inequality | sharp **isoperimetric** inequality |
| his PhD student Wang | **Yipeng Wang** (Columbia; Brendle–Wang, arXiv:2604.08473) |
| Yels and Samson | **Eells and Sampson** |
| rei flow / reichi flow / richy flow / rich flow / reie flow / rey flow / rii flow | **Ricci flow** |
| richi tensor / reachy / richy curvature | **Ricci** tensor / Ricci curvature |
| remmanion / Romanian / ramanian metric | **Riemannian** metric |
| reman tensor / reman curvature | **Riemann** curvature tensor |
| uklidian / ukidian / ukadian / uklitian | **Euclidean** |
| lorenian / lorenzian matrix | **Lorentzian** metrics |
| Einstein bhome equations | Einstein **field** equations |
| hession | **Hessian** |
| llassian / llian / llasian | **Laplacian** |
| conical delta / chronic delta / kronic delta | **Kronecker delta** |
| Paramman / Pelman / Palman / perman | **Perelman** (Grigori Perelman) |
| poner / ponare / fun conjecture | **Poincaré** conjecture |
| Hamilton and Chao | Hamilton and **Chow** (Bennett Chow) |
| Hamilton IV pinching estimate | **Hamilton–Ivey** pinching estimate |
| hornac inequality | **Harnack** inequality |
| cigal / cigaral soliton | **cigar** soliton |
| Brian Soliton / Brian Solitron / autorian soliton | **Bryant** soliton (Robert Bryant) |
| ka / kapa / copper / kanon / capon non-collapsed | **κ (kappa)** non-collapsed |
| ipsilon neck / ipssilla neck | **ε-neck** |
| deomorphisms / theomorphisms / fomorphisms / difforphisms | **diffeomorphisms** |
| difforphic | **diffeomorphic** |
| homothetically | homothetically *(correct as spoken)* |
| propolite / paraboid asatics | **paraboloid** asymptotics |
| asimatics / asmtoics / asytoic | **asymptotics** / asymptotic |
| a wall product over a one-dimensional object | a **warped product** over a one-dimensional object |
| panayota dcalopulus | **Panagiota Daskalopoulos** |
| natasha sesum | **Natasa Šešum** |
| copper solutions / ancient copper solution | ancient **κ-solutions** |
| the / this thumb / this therm / this film / these two films | the **theorem** / these two **theorems** |
| PTE / PBE theory | **PDE** theory |
| corary | **corollary** |
| gig j / gigj | **g_ij** |

**Substantive corrections and compressions, not just spellings.**

- **"Shrinking cylinders in 2D."** Brendle's table entry says the 2D shrinking cylinders are
  collapsed. S¹ × ℝ is flat — as he himself said two minutes earlier, a circle has no curvature
  — so it does not shrink at all, and it is excluded from the definition of an ancient
  κ-solution by the non-flatness requirement in any case. The *content* of his entry is correct
  and is what I verified in §6.2: a ball in a cylinder of fixed circumference has area growing
  linearly, so no κ works. I have treated this as podium shorthand rather than an error, and
  said so in §4.6.
- **κ-noncollapsing uses scalar curvature.** The companion's Definition 2.2 has
  sup_{B(p,r)} **R**(x,t) ≤ r⁻², with R the scalar curvature; from the podium Brendle says "the
  maximum curvature." Where the definition is applied — to solutions with nonnegative curvature
  — these differ only by a dimensional constant, so this is a compression, not a discrepancy. I
  have used the companion's version and flagged the difference in §3.8.
- **Perelman's structure theorem hypotheses differ between talk and paper.** The companion's
  Corollary 4.6 assumes positive sectional curvature; the talk instead excludes shrinking
  cylinders and their quotients. Compatible, via the splitting that occurs when the curvature
  fails to be strictly positive. Noted in §4.10.
- **The curve shortening flow date.** Brendle attributes curve shortening flow to "a paper by
  Gage and Hamilton in 1983." The Gage–Hamilton paper, *The heat equation shrinking convex
  plane curves*, is J. Diff. Geom. **23** (1986) 69–96; Gage's own earlier paper on curve
  shortening is from 1983. The companion does not cite either. **I have not corrected the date
  in the text** — I have written "Gage and Hamilton" without a year in §1's table and pointed
  here, since I cannot tell whether Brendle's slide said 1983 or whether the caption garbled a
  different number. Impact: nil for the mathematics.
- **"Theorem from 2018" and "back in 2012."** These are arXiv posting dates, not publication
  dates. The 2018 theorem is Acta Math. **225** (2020); the 2012 theorem is Invent. Math. **194**
  (2013). I give both in §5.

**One erratum in the companion.** The survey's Example 2.9 reads "Let us define a family of
metrics g(t) **on S²** by g(t) = (−4t) g_{S³}" — it plainly means **on S³**, since the metric
being scaled is the round metric on the three-sphere and the coefficient −4t is the one that
Ricci flow forces in dimension 3 (see §6.1(c)). Example 2.10 repeats the same slip, writing "a
family of metrics g(t) **on S²**" for the metric (−2t) g_{S²} + dz ⊗ dz, which lives on
**S² × ℝ**. I have used the corrected manifolds in §4.1 and note the source's wording here.
Neither affects any statement in the survey.

**What I reconstructed.**

- The **spherical and hyperbolic conformal factors** in §3.1. Brendle describes them precisely
  in words (stereographic coordinates, a point-dependent stretching factor, flip a sign,
  defined on the unit ball) but the formulas were on the slide. The two displayed metrics are
  the standard ones matching that description exactly. **Verify by**: computing the sectional
  curvature of each, which comes out +1 and −1.
- The **length functional** display in §3.1 is a transcription of his spoken formula, which he
  gives completely ("integrating the square root of the sum of g_ij α̇ⁱ α̇ʲ ... you use the metric
  at the point α(s)"). Nothing is added.
- The **Cheeger–Gromov convergence definition** in §3.7 is my unpacking of a phrase the
  companion uses without restating. It is standard and appears in Topping's lectures.
- The **anchor table in §2.1** is entirely mine — the left column, the type I/II row, and the
  Giga–Kohn reference are constructions for this reader, not claims about the talk. Labelled in
  place.

**Where the mathematics is unrecoverable, and how bad it is.**

- **The Riemann tensor formula (§3.2). Impact: low.** Brendle explicitly declines to write the
  quadratic terms from the podium, and the talk never uses the formula. Restorable from any
  textbook including his own.
- **Hamilton's matrix Harnack inequality (§4.9). Impact: low.** Named as one of four
  ingredients, then skipped, with Brendle saying so. Nothing later in the talk depends on it.
- **The degenerate neck pinch (§4.4). Impact: low.** He says "let me not go into details" and
  gives the one fact that matters — it is modelled on the Bryant soliton.
- **The symmetry improvement mechanism (§5.4). Impact: moderate, and it is the biggest hole in
  the talk itself rather than in the captions.** Brendle names the "symmetry improvement
  principle" as the crux of Step 3 and gives no mechanism at all. I have restored the whole
  chain — Lichnerowicz Laplacian, the parabolic equation for h = 𝓛_V(g), the Anderson–Chow
  maximum principle, the ε/2 contraction — from the companion's §§6–7, and labelled it. Without
  the companion this section would have been a paragraph saying "a principle exists."
- **Every slide with a picture.** The neck pinch diagram, the shrinking sphere, the cigar's
  profile, the tube-and-cap picture, and Perelman's ancient solution interpolating between two
  Bryant solitons and a round sphere were all drawn, and the caption track sees none of it.
  Where §4 reads thinner than it should, a picture was doing the work.

**Names I could not verify: none.** Every proper noun in the correction table above is anchored
to a located publication, an institutional page, or the companion's bibliography.

**One thing I could not get.** The ICM proceedings chapter itself. It exists
([doi:10.1137/25M1799052](https://doi.org/10.1137/25M1799052), SIAM, pp. 25–34, 35 references),
and it is the one document that would tell me exactly which of the above Brendle considers the
lecture's spine. SIAM returns 403 to automated fetching and no abstract is exposed by Crossref,
Semantic Scholar or OpenAlex. If you have institutional access, ten pages by this author on this
material is worth the download — and its 35 references will be a better reading list than my §8.
