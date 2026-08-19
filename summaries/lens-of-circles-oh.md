---
title: "Dynamics and Rigidity through the Lens of Circles"
speaker: Hee Oh (Yale)
source: https://www.youtube.com/watch?v=clMjIGdpVMw
video_id: clMjIGdpVMw
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2510.10771
transcript: ../transcripts/clMjIGdpVMw_transcript.txt
difficulty_for_you: 3/5 (questions 1–2) — 4/5 (questions 3–4)
reading_time: ~70 min
---

# Dynamics and Rigidity through the Lens of Circles — Hee Oh

**Field:** homogeneous dynamics in *infinite volume*. Concretely: what happens to counting,
equidistribution and orbit-classification theorems when the invariant measure of the system
is infinite, so that Poincaré recurrence and the Birkhoff ergodic theorem are both
unavailable.

**Difficulty against your background: split, 3 and 4.**

- **Questions 1 and 2 — circle counting and orbit closures — are a 3.** Everything in them
  is geometry you can draw plus ergodic theory you already own. There is exactly one
  genuinely new object, the Patterson–Sullivan measure, and it is definable in one line in
  language you have. This half is the main event of this tutorial and gets the space.
- **Questions 3 and 4 — representation rigidity and torus counting — are a 4.** The
  *statements* are elementary; question 3's final form is "a map that preserves the property
  *this cross-ratio is real* must be a Möbius transformation", which you can read on sight.
  The machinery underneath is not elementary: it runs on a rank-2 homogeneous space, where a
  single growth exponent is replaced by a concave function on a cone of directions, and the
  vocabulary (Weyl chamber, Cartan projection, limit cone, Anosov subgroup) is Lie theory you
  have none of. I state those results, name the mechanism, and decline to teach the Lie
  theory. That is deliberate; see §10.

Note the difference from the Kontorovich case. **This talk is squarely the speaker's famous
field**, and the reputation prediction was correct: Peter Sarnak's introduction says she
"has shaped the modern subject" of infinite-volume homogeneous dynamics, and that is exactly
the lecture she gives. Nothing inverted.

**Prerequisites this tutorial builds:** Möbius transformations as circle-preserving maps;
Kleinian groups and limit sets; the upper half-space model of hyperbolic 3-space and the
dictionary circle ↔ geodesic plane; quotient manifolds, convex cores, and the three
size-classes (lattice / convex cocompact / geometrically finite); the critical exponent and
why it equals a Hausdorff dimension; the Patterson–Sullivan measure as a Gibbs state; the
geodesic, frame and unipotent flows as right translations on Γ\PSL₂(ℂ); the Bowen–Margulis–
Sullivan and Burger–Roblin measures and what distinguishes them; *local mixing* as a
renormalized correlation function; thick recurrence.

**A note on sources.** This is the good case, and then some.

There is a genuine ICM proceedings paper: [arXiv:2510.10771](https://arxiv.org/abs/2510.10771),
Hee Oh, *"Dynamics and Rigidity through the Lens of Circles"*, submitted 12 October 2025,
revised 13 April 2026 (v2), whose arXiv comment reads "To appear in the Proceedings of the
ICM 2026, 33 pages, 24 figures". Its abstract is almost verbatim the talk's opening
paragraph. It follows the talk's order closely for the first six sections and then continues
past where the talk stops.

**The auto-captions carry not one formula.** This was a slide talk, and an unusually visual
one — 24 figures in the written version, most of them pictures of fractals. The caption track
contains the narration and nothing else. Every displayed formula, every theorem statement,
every constant and every exponent below comes from the paper. Where the talk and paper differ
I say which one I am quoting; there are six such places and they are listed in §10.

The talk also stops earlier than the paper. Sections 7 and 8 of the paper — the mixing
machinery in rank one and higher rank — are the analytic engine underneath everything, and
the talk gestures at them in about four sentences. I have compressed those two sections to
what the talk actually used, with one clearly-labelled exception in §4.11 that is too good to
leave out.

**Cross-link, one line.** Alex Kontorovich appears here as a collaborator: Theorem 2.1, the
original Apollonian circle-counting theorem, is Kontorovich–Oh 2011. His own ICM talk was
about AI and formal verification, so
[`shape-of-math-kontorovich.md`](shape-of-math-kontorovich.md) will not help you with any of
the mathematics below.

---

## 1. What is at stake

Draw three circles in the plane, each tangent to the other two. Apollonius of Perga
(262–190 BC) proved there are then exactly **two** more circles tangent to all three: one
tucked into the curved triangle between them, one wrapped around the outside.

That is a construction rule, so iterate it. Start with four mutually tangent circles. They
leave four curvilinear triangles between them; drop the unique inscribed circle into each.
Now you have more triangles; repeat. Forever. What you get is the **Apollonian circle
packing** — one of the most-drawn objects in mathematics, and the first picture in Oh's talk
after the sesame-oil photograph.

> *[Figure 1.1 in the paper shows the first few generations, with each circle labelled by
> the reciprocal of its radius — its **curvature**. Those labels matter later: start from the
> right four circles and every curvature in the infinite packing is an integer.]*

She opens with a second picture that looks nothing like it: a **Sierpiński-type circle
packing** (Figure 1.2), where the circles do *not* touch. Remove all the open white discs
from the plane and the fractal that remains is homeomorphic to the Sierpiński carpet.

Two pictures, no obvious relation, no obvious construction rule for the second one. The
unifying fact is the first move of the talk:

> **Both are limit sets of Kleinian groups.**

A **Kleinian group** Γ is a discrete group of Möbius transformations of the Riemann sphere
Ĉ = ℂ ∪ {∞}. Möbius transformations send circles to circles (with lines counted as circles
through ∞). Its **limit set** Λ is where the orbit Γ(z) of any point piles up — the set of
accumulation points, independent of which z you started from. For each of her two packings
there is a Kleinian group Γ with Γ𝒫 = 𝒫, and

> **closure of the union of all circles in 𝒫  =  Λ.**

The packing has countably many circles; its closure is a fractal of non-integer Hausdorff
dimension, because it contains the limit points of the ever-smaller circles.

Now Oh asks four questions about circle packings. All four are stated in the language of a
high-school geometry problem. All four turn out to be questions about the dynamics of flows
on an infinite-volume space.

> **Q1 — Circle counting.** How many circles in 𝒫 have radius at least t, as t → 0?
>
> **Q2 — Orbit closures.** Take any circle C. Its Γ-translates ΓC are countably many circles.
> What is the closure of ΓC in the space of all circles? Dense? Closed? Something in between?
>
> **Q3 — Rigidity.** Suppose f is a homeomorphism between the limit sets of two such
> packings. It need not send circles to circles — in her picture it sends a green circle to
> a circle but a yellow circle to a wobbly Jordan curve, so it is not Möbius. **How many
> circles can such an f send to circles before it is forced to be Möbius?**
>
> **Q4 — Torus counting.** When f *does* send some circle C to a circle f(C), the pair
> (C, f(C)) is a torus in ℂ², with volume rad(C)·rad(f(C)). How many such tori have volume
> at least t, as t → 0?

Her closing sentence is the thesis:

> "So, I have discussed all these four questions... They were formulated in plain language
> in terms of circles in the plane, but they led us naturally to homogeneous spaces of
> infinite volume."

**Why "infinite volume" is the whole difficulty.** Here is the shape of the subject before
any details. A Kleinian group Γ acts on hyperbolic 3-space ℍ³, and the quotient
ℳ = Γ\ℍ³ is a hyperbolic 3-manifold. If ℳ has *finite* volume, everything above is known
and has been for decades: counting is Duke–Rudnick–Sarnak and Eskin–McMullen, orbit closures
are Ratner and Shah, rigidity is Mostow–Prasad. The paper says this explicitly in §1.2 and
lists those four as the finite-volume ancestors of the four questions.

But a Γ whose limit set is an interesting fractal is *never* a finite-volume group. A finite
volume quotient forces Λ = Ĉ, the whole sphere — no fractal, no packing. So the moment the
picture is interesting, **the volume is infinite**, and every finite-volume tool is gone.

That is the entire subject, and it is also your way in.

---

## 2. Your anchor: this is statistical mechanics on an orbit, with the finite-measure hypothesis removed

You do not need a decorative analogy here. Two of them are structural, and the speaker hands
you the second one from the podium.

### 2.1 The failure: no Poincaré recurrence

Take the most basic theorem in ergodic theory. If T preserves a measure μ on a space X and
**μ(X) < ∞**, then Poincaré recurrence holds: almost every point of any positive-measure set
returns to that set, infinitely often. Birkhoff then gives you time averages = space
averages. Every classification statement in dynamics is downstream of these two.

Both need the *same* hypothesis, and it is a finiteness hypothesis. Delete it and both fail
immediately. In infinite measure, a typical orbit spends **zero fraction** of its time in any
fixed compact set, so time averages converge to zero and tell you nothing.

Oh says exactly this, and gives the picture:

> "So, think of this traveler moving along a unipotent trajectory in infinite volume
> hyperbolic manifolds. So, she might come back to some compact subset, and then she goes
> out, and then she might come back to some compact subset, and then she goes out again. And
> in the end, in infinite volume, in any fixed compact subset, the time she spends in a
> compact subset will be 0%. So, this means that it is very hard to capture where the
> accumulation happens in infinite volume."

To understand where an orbit accumulates you have to know where it comes back. In infinite
volume nothing gives you that for free. **The whole talk is: what you must build by hand to
replace the finite-measure hypothesis.** Two things get built, and you own the shape of both.

### 2.2 Repair one: the finite measure hiding inside the infinite one

The manifold ℳ has infinite Riemannian volume. But the interesting dynamics does not happen
on all of ℳ. Consider the set of unit tangent vectors *both* of whose geodesic endpoints
(forward and backward) lie in the limit set Λ. Those are exactly the directions along which
the geodesic stays bounded forever, in both time directions. Everything else escapes to an
end and never comes back.

On that set there is a natural measure — the **Bowen–Margulis–Sullivan measure** m^BMS — and
Sullivan proved (paper, [80]):

> **If Γ is geometrically finite, |m^BMS| < ∞.**

The paper's comment on this is the load-bearing sentence of the subject:

> "This finiteness is crucial: although ℳ has infinite Riemannian volume, the essential
> dynamics of flows is captured by this finite BMS measure. This explains why many central
> theorems in dynamics for hyperbolic manifolds are formulated for geometrically finite
> quotients."

You know this move. An infinite phase space whose recurrent dynamics is confined to a
finite-measure invariant set is the ordinary situation in dissipative mechanics: the
attractor carries a finite invariant measure even though the ambient space does not. The
technical content here is that the "attractor" is a fractal set of *directions*, and that its
natural measure is finite exactly when the group is geometrically finite.

### 2.3 Repair two: renormalization — and the partition function

Here is the second half, and it is the one the speaker states out loud.

Take a bounded set B in the quotient, push it forward by the geodesic flow for time t, and
ask how much of it comes back to a fixed compact region. In finite volume, mixing says the
answer converges to a nonzero constant. In infinite volume it converges to **zero**. Oh, on
the equidistribution step of her own proof:

> "So, in any fixed compact region, the mass seen will go to zero as t goes to infinity. So,
> what do we do? So, we renormalize it by multiplying the inverse of the rate... It turns out
> the correct [rate] is e to the 2 minus delta t where delta is the Hausdorff dimension of
> the limit set."

That is renormalization in the sense you use it. The raw quantity dies; you do not conclude
"no signal", you find the exact exponential rate at which it dies and divide it out, and the
limit is a genuine measure. Formally (paper, Theorem 7.2, specialised to ℍ³ so d = 3):

> lim_{t→∞} e^{(2−δ)t} ⟨a_t·f₁, f₂⟩ = (1/|m^BMS|) · m^BR(f₁) · m^BR*(f₂)

Read the left side as a **correlation function** of two observables separated by time t under
the geodesic flow a_t; read the right side as a product of two spatial averages against
specific measures. In finite volume with δ = 2 this is exactly the usual statement "the
correlation function tends to the product of the means", i.e. mixing. In infinite volume the
correlation decays like e^{−(2−δ)t} and (2 − δ) is the decay exponent. The paper calls the
renormalized version **local mixing**; the word *local* means only that you test against
compactly supported observables, so the integrals against infinite measures make sense.

**Now the anchor proper.** The exponent δ, the measures, and the constants all come from one
construction, and it is a Gibbs construction. Fix a base point o ∈ ℍ³ and form the series

> **P(s) = Σ_{γ ∈ Γ} e^{−s·d(o, γo)}**

*(This series is standard background that I am supplying; neither the talk nor the paper
writes it down. The paper gives instead the quantity it controls — see below.)* This is a
partition function: a sum over the states of a system (elements of the group), each weighted
by e^{−β·energy}, with the energy of γ being the hyperbolic displacement d(o, γo) and s
playing the role of inverse temperature. Then:

| Statistical mechanics | Here | Where it is in the sources |
|---|---|---|
| Partition function | Σ_γ e^{−s d(o,γo)} | supplied by me |
| Critical inverse temperature (abscissa of convergence) | **the critical exponent δ** | paper, Thm 2.6: δ = limsup_T (1/T) log #{x ∈ Γo : d(x,o) ≤ T} |
| Free energy / entropy | δ again — it *is* the exponential orbit growth rate | Thm 2.6 |
| Gibbs state at the critical point | **the Patterson–Sullivan measure ν_o** on Λ | paper, Thm 2.8 |
| DLR / Gibbs consistency condition | dγ*ν/dν(ξ) = e^{sβ_ξ(o,γo)} — "Γ-conformal of dimension s" | paper, eq. (2.2) |
| Equilibrium state on phase space | **the BMS measure** on (past, future, time) coordinates | paper, §2.4.1 |

And the theorem tying it together, which is genuinely startling the first time (Patterson,
Sullivan; paper Theorem 2.6):

> **δ = dim(Λ).**

The exponential growth rate of the orbit *inside* hyperbolic space equals the Hausdorff
dimension of where the orbit piles up *on the boundary*. A thermodynamic quantity equals a
geometric one. The fractal, which lives on the sphere at infinity, remembers how fast the
group grew in the interior.

**Why this anchor keeps paying.** Every constant in the talk is a ratio of masses of these
Gibbs-type measures. The circle-counting constant is (paper, §2.4.2):

> **c_𝒫 = sk_Γ(𝒫) / |m^BMS|**

— a "skinning" mass divided by the total equilibrium mass. And when the talk moves to the
hard half (rank two, §4.10), the single number δ is replaced by Quint's **growth indicator**
ψ_ρ, defined in the paper as an abscissa of convergence *computed separately in each
direction* of a cone. That is a direction-dependent free energy. The anchor survives the
transition intact; you just go from one thermodynamic variable to a concave function on a
cone.

### 2.4 The KAM contrast — mine, and absent from the talk

You might expect the following comparison, and it is a fair one, so I am naming it and then
setting it aside.

The answer to Q2 is a **dichotomy**: an orbit is either closed or dense, with nothing in
between. Your instinct from classical mechanics says this should be false. In a
near-integrable Hamiltonian system, KAM theory says invariant tori and chaotic regions
*coexist* in the same phase space at the same energy — the phase portrait is a mixture, and
the mixture is the whole content of the theory. Nothing there is a dichotomy.

The reason the dichotomy holds here and not there is that the flows in question are
**unipotent** — algebraic, with polynomial rather than exponential divergence of nearby
orbits — and unipotent flows on homogeneous spaces are rigid in a way generic Hamiltonian
flows are not. That is Ratner's theorem, and its whole point is that the KAM picture does not
occur.

**The talk never mentions KAM, Hamiltonian mechanics, or integrability.** This comparison is
mine. I include it because it is the right calibration for you — it tells you that "closed or
dense" is a surprising conclusion, not a boring one — and I am labelling it so you do not
attribute it to her. The rigidity theorems below are also not universal: §4.6 gives her own
counterexamples, geodesic planes with genuinely chaotic closures, which is as close as this
subject comes to a KAM-like mixed picture.

---

## 3. The bridge

Eight ideas. Each defined by deforming something you have. Nothing else is needed.

### 3.1 Möbius transformations, and why circles are the right object

The group PSL₂(ℂ) acts on Ĉ = ℂ ∪ {∞} by

> [[a, b], [c, d]] · z = (az + b)/(cz + d),  ad − bc = 1.

You know these as fractional linear transformations from complex analysis. The one property
that runs the whole talk:

> **A Möbius transformation sends circles to circles**, where a straight line counts as a
> circle through ∞.

And the converse, which the paper states as a classical characterisation: a homeomorphism of
Ĉ is Möbius **if and only if** it preserves the family of circles. That biconditional is why
Q3 is a sensible question at all — "how many circles must f preserve before f is Möbius"
interpolates between "none" and "all".

The Möbius group is generated by **inversions in circles**: reflect each point through a
circle, i.e. z ↦ centre + r²/(z̄ − centre‾). Hold that; it is the mechanism for §3.3.

### 3.2 Kleinian groups, limit sets, and the snow

A **Kleinian group** is a *discrete* subgroup Γ < PSL₂(ℂ) — every point of Γ is isolated in
the matrix topology, so Γ is countable. Discreteness is the entire hypothesis; everything
interesting is a consequence of it.

Fix z ∈ Ĉ and look at the orbit Γ(z), a countable set of points. The **limit set** Λ is the
set of accumulation points of that orbit. It does not depend on z. Its complement
Ω = Ĉ − Λ is the **domain of discontinuity**.

Oh's picture for this is Figure 2.3 of the paper, and she narrates it:

> "Think of an orbit as snow falling in hyperbolic 3-space. Then, the snow does not
> accumulate in the air. It can only accumulate on the ground. And wherever it accumulates,
> it becomes the limit set."

The snow falls in the interior of hyperbolic space; discreteness forbids it from piling up
anywhere in the interior; so it can only pile up on the boundary sphere, and where it piles
up *is* Λ. In the paper's own gloss: for a lattice "the snow covers the entire ground",
Λ = Ĉ. For everything else you get fractals.

Figure 2.4 shows four of them, and her narration names them: a **Jordan curve** (homeomorphic
to a circle, though it does not look like one); the **Sierpiński-type packing**; the
**Apollonian packing**; and **Schottky dust**, totally disconnected, homeomorphic to a Cantor
set. All four have non-integer Hausdorff dimension, all four have dimension strictly less
than 2.

### 3.3 Hyperbolic 3-space, and the dictionary circle ↔ geodesic plane

This is where the dynamics enters, and it is one page of Riemannian geometry you already own.

**Upper half-space model.** ℍ³ = {(x₁, x₂, y) : y > 0} with the metric

> ds = √(dx₁² + dx₂² + dy²) / y

— the Euclidean metric divided by the height. Constant curvature −1. Consequence you should
feel: two points near the floor y = 0 are enormously far apart hyperbolically even when they
are Euclidean-close, because the metric blows up like 1/y. The floor is infinitely far away.

**Boundary.** The geometric boundary of ℍ³ is the plane {y = 0} together with ∞ — which is
exactly Ĉ. So the sphere where the circles live *is* the boundary at infinity of the
hyperbolic space where the dynamics lives.

**Geodesics and planes.** Solve the geodesic equation for this metric and you get: geodesics
are vertical lines, or semicircles meeting the boundary at right angles. Totally geodesic
surfaces are vertical planes, or **hemispheres meeting the boundary at right angles**.

> **The dictionary.** A circle C ⊂ Ĉ ⟷ the hemisphere C† standing over it.
> This is a bijection between circles in the boundary and geodesic planes in ℍ³.

*(Figure 2.2 of the paper is this picture: two hemispheres over two circles in the floor
plane.)*

Every question about circles in the plane is therefore a question about totally geodesic
planes in a hyperbolic 3-manifold. That single dictionary converts the whole talk.

**How the action extends: the Poincaré extension theorem.** Möbius transformations act on the
boundary; do they act on the interior? Yes, and the geometric reason is the clean one Oh
gives. Every Möbius transformation is a composition of inversions in circles (§3.1). Given a
circle in the floor, extend its inversion to the *inversion in the hemisphere over it*.
Because that hemisphere meets the floor orthogonally, the inversion preserves the upper half
space; and inversion in a sphere is a conformal map, which for this metric means it is an
isometry. Compose. So:

> **PSL₂(ℂ) = Isom⁺(ℍ³)** (Poincaré extension theorem, paper §2.2).

Discreteness of Γ in PSL₂(ℂ) is now equivalent to the action on ℍ³ being **properly
discontinuous** — no orbit accumulates in the interior. Which is the snow statement again.

### 3.4 The quotient manifold, and the three size classes

Quotient by the group: ℳ = Γ\ℍ³. Assuming Γ is torsion-free (assumed throughout, both by
her and by the paper), ℳ is a complete hyperbolic 3-manifold, and conversely every complete
hyperbolic 3-manifold arises this way. So "Kleinian group" and "hyperbolic 3-manifold" are
two names for the same data.

The **convex core** is the part of ℳ that carries all of its topology:

> core ℳ := Γ\hull(Λ)

— take the convex hull of the limit set inside ℍ³, and quotient. Her one-line version: "the
smallest convex subset that carries all the topology of ℳ." Figure 2.5 shows a manifold with
three flaring blue **ends** going off to infinity, carrying all the infinite volume, and a
compact yellow convex core sitting in the middle.

Three classes, in increasing generality:

| Class | Definition | Limit set | Volume of ℳ |
|---|---|---|---|
| **Lattice** | vol(ℳ) < ∞ | Λ = Ĉ, all of it | finite |
| **Convex cocompact** | core ℳ is compact | fractal, dim < 2 | infinite |
| **Geometrically finite** | the *unit neighbourhood* of core ℳ has finite volume | fractal, dim < 2 | infinite |

Geometrically finite = convex cocompact plus finitely many **cusps** (thin tubes running off
to infinity of finite volume). It is the working hypothesis for almost every theorem below.

Two facts she stresses about why this is the right class:

1. **Lattices are rare and rigid.** By the local rigidity theorem of Selberg and Weil there
   are only *countably many* lattices up to conjugation, and constructing them generally
   needs number theory. Geometrically finite groups, by contrast, come in continuous
   families.
2. **Geometrically finite groups are everywhere.** She says from the podium that every
   finitely generated Kleinian group can be approximated by geometrically finite ones. The
   paper names this: it is the **Bers–Sullivan–Thurston density conjecture**, now a theorem
   (Namazi–Souto, Ohshika, building on many others), which says geometrically finite groups
   form an **open and dense** subset of the space of all finitely generated Kleinian groups.
   *(The captions render the attribution as "the Cannon conjecture"; that is a different
   conjecture. See §10.)*

**Note the definitional subtlety.** She says geometrically finite means the convex core has
finite volume; the paper says the *unit neighbourhood* of the convex core has finite volume.
For convex cocompact groups these agree. In the presence of cusps the paper's version is the
correct one, and I use the paper's throughout.

### 3.5 δ: growth rate, dimension, and why they are equal

The **critical exponent** of Γ (paper, Theorem 2.6):

> δ := limsup_{T→∞} (1/T) · log #{ x ∈ Γ(o) : d(x, o) ≤ T }

— the exponential growth rate of the orbit in the hyperbolic ball of radius T. Equivalently
#(orbit in a ball of radius T) ≍ c·e^{δT}. And the theorem:

> **δ = dim(Λ)** (Patterson, Sullivan)

The Hausdorff dimension of the fractal on the boundary is the exponential growth rate of the
group in the interior. For the **Apollonian** packing the paper records the numerical value:

> **δ_A ≈ 1.3057**, and it is the same for every Apollonian packing.

For lattices δ = 2 and Λ = Ĉ. Among geometrically finite groups, lattices are exactly the
ones with δ = 2; everything else has δ < 2.

### 3.6 The Patterson–Sullivan measure: a Gibbs state on a fractal

Lebesgue measure on the plane gives Λ mass zero — it is a fractal of dimension < 2. So you
need a measure that sees it. Here is the one, and it is short.

First, the transformation law you want to imitate. Let m_o be the rotation-invariant
probability measure on the sphere Ĉ as seen from o = (0,0,1). Push it forward by g ∈ PSL₂(ℂ)
and it stays absolutely continuous, with (paper, eq. 2.1):

> d(g_*m_o)/dm_o (ξ) = e^{2·β_ξ(o, go)}

where β is the **Busemann function**: β_ξ(x, y) = lim_{t→∞} [d(ξ_t, x) − d(ξ_t, y)] along a
geodesic ray heading to ξ. Read β_ξ(x,y) as "how much closer to ξ the point y is than x is" —
a renormalized difference of two infinite distances, exactly the trick you use to define a
potential relative to a reference point. The exponent 2 is the dimension of the sphere.

Now change the 2. A measure ν on Ĉ is **Γ-conformal of dimension s** if (paper, eq. 2.2):

> dγ_*ν/dν (ξ) = e^{s·β_ξ(o, γo)}  for all γ ∈ Γ.

This is a Gibbs/DLR condition: it prescribes exactly how the measure transforms under the
symmetry group, in terms of an energy. And:

> **Theorem (Patterson, Sullivan; paper Thm 2.8).** For any geometrically finite Γ there is a
> **unique** Γ-conformal probability measure ν_o of dimension **δ**, and it is supported on Λ.

That is the **Patterson–Sullivan measure**. It exists only at the critical value s = δ —
below it the construction diverges, above it converges to nothing. This is a phase transition
at a critical inverse temperature, and ν_o is the critical Gibbs state. It is the natural
fractal measure on Λ, and for convex cocompact groups and for the Apollonian symmetry group
it coincides (up to scale) with δ-dimensional Hausdorff measure.

One detail you will want when you read the counting theorem. The measure appearing there is
not ν_o itself but

> dω_Γ(z) = (|z|² + 1)^δ · dν_o(z),  z ∈ Λ ∩ ℂ

which is ν_o reweighted by the Jacobian factor converting the spherical metric on Ĉ to the
Euclidean metric on ℂ. It is stereographic projection bookkeeping, nothing more.

### 3.7 The flows, as right translations

Everything dynamical happens on the **frame bundle**

> F(ℳ) = Γ\PSL₂(ℂ)

whose points are orthonormal frames on ℳ. Flows are right translations by one-parameter
subgroups. Three of them:

| Subgroup | Matrix | Flow | Geometry |
|---|---|---|---|
| A | diag(e^{t/2}, e^{−t/2}) | geodesic / frame flow | move along a geodesic at unit speed |
| U | [[1, t],[0, 1]] | horocyclic (unipotent) flow | slide along a horosphere |
| PSL₂(ℝ) | real matrices | — | orbits project to **geodesic planes** |

The two facts that matter:

1. **Geodesic planes in ℳ = PSL₂(ℝ)-orbits in Γ\PSL₂(ℂ)**, projected down. Combined with
   §3.3, a circle in Ĉ gives a geodesic plane in ℍ³ gives a PSL₂(ℝ)-orbit upstairs. **The
   space of circles and the space of PSL₂(ℝ)-orbits are the same space.** Q2 is now a
   question in homogeneous dynamics.
2. **PSL₂(ℝ) is generated by unipotent subgroups** — the strictly upper and lower triangular
   ones. This is why Ratner's theorem is the relevant tool, since Ratner's theorem is about
   groups generated by unipotents.

A **unipotent** matrix is one all of whose eigenvalues are 1. The distinguishing dynamical
feature: nearby unipotent orbits separate **polynomially**, not exponentially. That
polynomial control is the source of every rigidity theorem in the subject, and it is why the
KAM picture (§2.4) does not apply.

### 3.8 Two measures: BMS and Burger–Roblin, and the one difference between them

You need both, and they differ in exactly one slot.

**Hopf coordinates.** A unit tangent vector v on ℍ³ is determined by three things: the forward
endpoint v⁺ ∈ Ĉ of its geodesic, the backward endpoint v⁻ ∈ Ĉ, and where along that geodesic
it sits. So

> T¹(ℍ³) = (Ĉ × Ĉ − diagonal) × ℝ.

That is (future, past, time) — a phase-space parametrisation, and the geodesic flow is
translation in the last coordinate. Now write down measures on it as products.

> **Bowen–Margulis–Sullivan.** dm̃^BMS = e^{δβ_{v⁺}(o,v)} e^{δβ_{v⁻}(o,v)} dν_o(v⁺) dν_o(v⁻) dt
>
> **Burger–Roblin.** dm̃^BR = e^{δβ_{v⁺}(o,v)} e^{2β_{v⁻}(o,v)} dν_o(v⁺) **dm_o(v⁻)** dt

The only difference is the **backward** slot: BMS uses the fractal Patterson–Sullivan measure
ν_o at both ends; BR uses the smooth spherical measure m_o at the backward end (and exponent
2 = d − 1 to match). The consequences:

| | BMS | Burger–Roblin |
|---|---|---|
| Support | vectors with **both** endpoints in Λ | vectors with forward endpoint in Λ |
| Projects into | the convex core (compact-ish) | all of ℳ |
| Invariance | geodesic flow A | the **horospherical** subgroup N |
| Total mass | **finite** for geometrically finite Γ | infinite unless Γ is a lattice |
| Role | the equilibrium state; the denominator | the answer measure; the numerator |

BMS is the finite invariant measure of §2.2 — the thing that replaces "vol(X) < ∞". BR is
what the renormalized correlation converges to, and it is what makes the equidistribution
statements come out; the paper notes it is the *unique* ergodic N-invariant measure not
supported on a single N-orbit. In the local mixing formula of §2.3 the BMS mass sits in the
denominator and the BR measures sit in the numerator. That is the shape of every constant in
the talk.

---

## 4. The talk, rebuilt

Her order, with the mathematics restored from the paper.

### 4.1 Q1: the circle-counting theorem

She states three versions, increasingly general. All are for a **locally finite** packing —
meaning that for each ε > 0 and each bounded region there are only finitely many circles of
radius > ε meeting it, which is precisely the condition making the counting question
well-posed.

**Version 1 — the Apollonian case** (Kontorovich–Oh, *J. Amer. Math. Soc.* 24 (2011); paper
Thm 2.1). For any bounded Apollonian packing 𝒫 there is c_𝒫 > 0 with

> #{C ∈ 𝒫 : rad(C) ≥ t} ~ c_𝒫 · t^{−δ_A}  as t → 0,  δ_A ≈ 1.3057.

**Version 2 — equidistribution** (Oh–Shah, *Invent. Math.* 187 (2012); paper Thm 2.2). The
circles do not merely proliferate, they spread out according to a definite measure. For any
region R bounded by a piecewise C¹ curve,

> #{C ∈ 𝒫 : rad(C) ≥ t, C ∩ R ≠ ∅} ~ c_A · ℋ^{δ_A}(R ∩ 𝒫̄) · t^{−δ_A}

with ℋ^{δ_A} the δ_A-dimensional Hausdorff measure. **The small circles equidistribute with
respect to the fractal measure on the limit set.** Her example region is a pink flower shape.

**Version 3 — the general theorem** (Oh–Shah; paper Thm 2.7). Let 𝒫 be a locally finite
circle packing invariant under a geometrically finite Kleinian group Γ, consisting of
finitely many Γ-orbits. Then there are 0 < c_𝒫 < ∞ and a locally finite measure ω_Γ on
Λ ∩ ℂ such that for any region R bounded by a piecewise algebraic curve,

> **#{C ∈ 𝒫 : rad(C) ≥ t, C ∩ R ≠ ∅} ~ c_𝒫 · ω_Γ(R) · t^{−δ}  as t → 0**

with δ = dim Λ and ω_Γ the reweighted Patterson–Sullivan measure of §3.6.

**Three points of care, all worth having.**

- *The hypothesis about bouquets.* She states the theorem with a blanket assumption that 𝒫
  contains no "infinite bouquet of tangent circles" (Figure 2.6: infinitely many circles all
  tangent at one point). The **paper imposes it only when δ ≤ 1**. Its purpose is to make the
  skinning constant finite, and the paper notes the constant is automatically finite when
  δ > 1. Since δ_A ≈ 1.3057 > 1, the Apollonian case never needs it. I quote the paper.
- *Contained versus meeting.* She says "circles contained in this region"; the paper counts
  circles with C ∩ R ≠ ∅. I quote the paper.
- *Which measure.* She says "Patterson–Sullivan measure of the region"; the paper's ω_Γ is
  PS measure times (|z|²+1)^δ. Same object up to the stereographic Jacobian.

### 4.2 Decoding the constant: the skinning measure

She asks the right question about her own theorem:

> "Any asymptotic like this must explain the source of the multiplicative constant."

The exponent δ is not surprising once you know δ is the orbit growth rate (Exercise 6.2
below makes that precise). The constant is where the content is, and the answer is a
geometric invariant of *how the plane sits inside the manifold*.

Take a circle C in the packing, form the hemisphere C† over it, and push it down to ℳ. If
the Γ-orbit of C is closed in the space of circles — equivalently (paper §2.4.2) if the map
Stab_Γ(C†)\C† → ℳ is proper — this is a properly immersed geodesic surface S ⊂ ℳ. Take its
**unit normal bundle**: at each point of S, the two unit vectors perpendicular to S. Now put
Patterson–Sullivan weights on the endpoints of the geodesics shot off in those normal
directions (paper §2.4.2):

> dμ^sk_{C†}(v) = e^{δβ_{v⁺}(o,v)} dν_o(v⁺) + e^{δβ_{v⁻}(o,v)} dν_o(v⁻)

The normalisation makes it Stab_Γ(C†)-invariant, so it descends to a measure on the immersed
surface. Its total mass is the **skinning constant**

> 0 < sk(C) := μ^sk_{C†}( Stab_Γ(C†)\C† ) ≤ ∞

and for a packing 𝒫 = ΓC₁ ∪ ⋯ ∪ ΓC_ℓ, sk_Γ(𝒫) = sk(C₁) + ⋯ + sk(C_ℓ). The paper's intuition
in one line: "the skinning measure records how the geodesic plane C† intersects the limit set
through its normal vectors."

And then the punchline that the talk gives only qualitatively and the paper states exactly:

> **c_𝒫 = sk_Γ(𝒫) / |m^BMS|**

The counting constant is a ratio: the mass of the surface's normal data, over the total mass
of the equilibrium state. Both masses are finite exactly under the hypotheses of the theorem.
Read against §2.3: this is the same numerator/denominator structure as the local mixing
formula, because it is derived from it. §5 gives the derivation.

### 4.3 Q2: orbit closures, and the closed-or-dense dichotomy

Now the second question. Γ acts on the space of circles; restrict attention to circles that
actually meet the limit set, since a circle disjoint from Λ has a closed orbit for a trivial
reason. Write 𝒞_Λ for the circles meeting Λ, and 𝒞*_Λ for the **separating** circles — those
with limit points both inside *and* outside. In her picture, a circle drawn across the carpet
is separating; a circle drawn inside one of the white discs is not.

She shows three orbits and this is the part of the talk where the pictures do real work:

1. **Dense.** A red circle, and its pink translates going everywhere — some so large you only
   see an arc of them — approximating every circle that meets Λ.
2. **Visibly closed.** The red circle is one of the circles *of the packing*. Its translates
   are other circles of the packing. Nothing new accumulates. Obvious.
3. **Invisibly closed.** A red circle that is *not* in the packing, whose translates
   nonetheless never accumulate on anything new. Her comment: "it's not obvious at all why
   this one must have a closed gamma orbit." These hidden closed orbits become the central
   obstruction in higher dimensions (§4.5).

Are there other possibilities? The answer depends on the shape of Λ.

**Round Sierpiński carpets.** Call Λ a **round Sierpiński carpet** if

> Ĉ − Λ = ⋃ B_i, with B_i infinitely many **round** open discs with **mutually disjoint
> closures**.

*(Figure 3.1: a black fractal with round white holes that do not touch.)*

The geometric meaning is exact and pretty: these are precisely the manifolds whose **convex
core has compact, totally geodesic boundary**. Each Γ-orbit of a white disc corresponds to
one boundary component of the convex core, and the disc being *round* is precisely the
statement that that boundary surface is *totally geodesic*. In Figure 3.2 two compact
geodesic surfaces S₁ and S₂ have been cut out of a closed hyperbolic 3-manifold; what remains
has S₁ and S₂ as its convex core boundary. She narrates: "the geodesic planes above these
white round open discs, they are exactly the coverings of these S₁ and S₂."

> **Theorem (McMullen–Mohammadi–Oh, *Invent. Math.* 209 (2017); extended to the geometrically
> finite case with Benoist, *ETDS* 42 (2022). Paper Thm 3.1.)**
> Let Γ be geometrically finite with Λ a round Sierpiński carpet, and C ∈ 𝒞_Λ.
> - If C is **separating**, then ΓC is either **closed** or **dense** in 𝒞_Λ.
> - If C is not separating, ΓC‾ = {D ∈ 𝒞_Λ : D ⊂ ΓB‾} for the disc B whose closure contains C.

Her summary of the second bullet: "for non-separating circles we have actually a third type
of behaviour, which is neither closed nor dense, but they are easy to analyse."

*(The captions attribute the geometrically finite extension to "If Bou-Rabee". No such name
appears anywhere in the paper's 85-entry bibliography and no such collaboration is findable;
the paper attributes it to [3], **Yves Benoist** and Oh. See §10.)*

**General Sierpiński carpets: allow the discs to be wobbly.** Now let the B_i be **Jordan**
discs — topological discs bounded by simple closed curves — still with disjoint closures.
Where do these come from? From **deformations**. She:

> "They arise from deformations of hyperbolic manifolds with Fuchsian ends... if the convex
> core has totally geodesic and compact boundaries, then for any deformation of this boundary
> surface, there is a new hyperbolic three-manifold realizing this deformation."

That is the **Ahlfors–Bers theorem** *(captions: "alpha's first theory")*. The paper's precise
version (Thm 3.2, Thurston and McMullen): every geometrically finite **acylindrical** Kleinian
group is quasiconformally conjugate to a geometrically finite **rigid** one (rigid = totally
geodesic convex-core boundary = round carpet), uniquely up to conjugation. The deformation
space is ∏_i Teich(S_i), a product of Teichmüller spaces of the convex-core boundary surfaces.
So these things exist in continuous families, which is the point of §3.4's remark that
lattices are countable and these are not.

A **quasiconformal** map is the standard definition and one you will recognise: a
homeomorphism that sends infinitesimal circles to ellipses of bounded eccentricity ≤ κ
(paper eq. 3.1). κ = 1 forces conformal, hence Möbius. So "quasiconformal" is "Möbius up to a
bounded amount of distortion", and the entirety of Q3 is about how much distortion is
detectable.

> **Theorem (McMullen–Mohammadi–Oh, *Duke* 171 (2022); with Benoist [3]. Paper Thm 3.3.)**
> For Γ geometrically finite acylindrical: any Γ-invariant subset of 𝒞*_Λ is either a finite
> union of closed orbits, or dense in 𝒞*_Λ. There are at most countably many closed orbits in
> 𝒞*_Λ. If Γ is rigid, the dense case is dense in the larger 𝒞_Λ.

**Why the ambient space had to shrink.** She flags this precisely: for non-rigid Γ, the right
ambient space is the separating circles 𝒞*_Λ, not all of 𝒞_Λ, "because Yongquan Zhang
constructed an example of an orbit ΓC which is closed in the space of separating circles but
not closed in the space of all circles" (*Math. Res. Lett.* 30 (2023), "Existence of an exotic
plane in an acylindrical 3-manifold"). The paper's explanation of the phenomenon is worth
having: the *interior* of the convex core behaves like a homogeneous space, but the interior
together with its boundary does not. So restrict to circles that see the interior.

Translated back through the dictionary of §3.3, this is a statement about surfaces (paper
Thm 3.7): **any geodesic plane meeting the interior of the convex core is either closed or
dense there**, and there are at most countably many closed ones.

### 4.4 The mechanism: thick recurrence, built by hand

This is where the anchor of §2.1 gets cashed out, and it is the most instructive part of the
talk.

In finite volume, the classification is a special case of **Ratner's theorem** (paper Thm 4.1;
Raghunathan's conjecture): for a connected Lie group G, a lattice Γ, and a subgroup U
generated by unipotents, every orbit closure xU‾ is xL for a closed connected subgroup L.
Since PSL₂(ℝ) is a maximal connected subgroup of PSL₂(ℂ), that gives closed-or-dense
immediately. (Proved independently in this special case by Shah, following Margulis and
Dani–Margulis on the Oppenheim conjecture.)

The proof of Ratner's theorem uses recurrence, and recurrence comes from finite measure. Oh:

> "But we are in the infinite volume setting. And the main difficulty is the lack of
> recurrence."

So build it. The key construction (paper §3.6) is an explicit compact set 𝓡 ⊂ Γ\G with a
quantitative return guarantee:

> **Thick recurrence.** There is κ > 1 such that for every x ∈ 𝓡 and every s > 0 there exists
> t with **s < |t| < κs** and x·u_t ∈ 𝓡.

Read the quantifiers. Not "returns infinitely often" — that is what Poincaré gives you for
free and it is not available. This says: *in every window of multiplicative width κ, at every
scale, there is a return*. Returns at all scales, with a uniform bound. That is a genuinely
stronger and more useful statement than recurrence, and it has to be constructed rather than
invoked. Moreover the construction is arranged so that **every** PSL₂(ℝ)-orbit corresponding
to a plane meeting the convex-core interior arises from some x ∈ 𝓡.

**Where the returns come from: the fractal is fat enough.** Oh's explanation is the heart of
it:

> "For Sierpiński carpet limit sets, every separating circle meets the limit set in a
> uniformly thick Cantor type subset. So, for every point in the intersection of C with Λ,
> there is a corresponding return time of the unipotent flow to a compact region. And this
> uniform thickness of the circular slice C ∩ Λ gives us enough recurrence for the unipotent
> flows."

Unpack the logic, because it is a beautiful chain:

1. A **circular slice** is C ∩ Λ: what the limit set looks like along one circle.
2. For a Sierpiński carpet, every separating circle cuts Λ in a Cantor set that is
   *uniformly perfect* — "a Cantor set with no gaps that are disproportionately large at any
   scale" (paper, footnote 5). No scale is empty.
3. The **visual image of a horocycle on Ĉ is a circle** (paper §3.6). So travelling along the
   unipotent flow is, seen from the boundary, sweeping along a circle.
4. Therefore each point of C ∩ Λ contributes a **return time**, and the no-empty-scale
   property of the Cantor set converts directly into no-empty-scale returns — thick
   recurrence.

The technical input making step 2 work is the **positive modulus property** of the limit set:
inf_{ℓ≠k} mod(Ĉ − (T̄_ℓ ∪ T̄_k)) > 0, where mod is the conformal modulus of an annulus. The
white discs are uniformly separated in the conformal metric, so the black stuff between them
is uniformly fat.

> **The recurrence hypothesis was replaced by a geometric fatness property of a fractal.**
> That is the transferable idea, and §7.2 is about it.

### 4.5 Where the rigidity fails, and where it is conjectural

Two limits, both stated by her and both important for calibration.

**Chaotic geodesic planes exist.** The dichotomy is *not* a general theorem about
geometrically finite manifolds. If the circular slices are too thin, it breaks. A
**quasi-Fuchsian** group is a quasiconformal deformation of a Fuchsian lattice in PSL₂(ℝ);
its limit set is a Jordan curve (Figure 2.4, first image). McMullen–Mohammadi–Oh showed that
many quasi-Fuchsian manifolds built by **bending** contain geodesic planes whose closures are
diffeomorphic to (closure of a geodesic on a closed hyperbolic surface) × ℝ. Geodesic
closures on closed hyperbolic surfaces are chaotic, so these plane closures are chaotic. This
is the closest thing in the subject to the mixed KAM picture of §2.4, and it is why the
carpet hypothesis is not decoration.

**The Apollonian case is open.** She goes back to the Apollonian gasket and shows why her
method dies:

> "In Apollonian circle packing, circular slices can be very thin... if you look at the
> circle connecting these three blue points [tangency points], it's very easy to see that its
> gamma orbit should be closed. But if I look at a nearby circle, then we expect this circle
> to have dense orbit. But as you can see visibly, the intersection of this red circle with
> the limit set is extremely small. So this thick recurrence method we used for Sierpiński
> carpet limit sets does not work anymore."

The structural reason (paper §3.4): the Apollonian group's compact core is a genus-two
handlebody, so its boundary is **compressible**, so it is not acylindrical. It sits just
outside the framework.

> **Conjecture 3.6 (Oh).** For an Apollonian circle packing with symmetry group Γ, and any
> separating circle C, the orbit ΓC is either closed or dense in 𝒞_Λ.

Her reason for caring: "Apollonian circle packing is one of the most canonical circle
packings. So this conjecture is really compelling."

### 4.6 Higher dimensions: intermediate spheres and the wild forest

Now go up. The boundary of ℍ^{d+1} is the sphere 𝕊^d. Higher-dimensional round Sierpiński
carpets exist: Λ ⊂ 𝕊^d whose complement is infinitely many round open d-balls with disjoint
closures. Take a circle in 𝕊^d and look at its Γ-orbit. What changes?

**A new possibility appears, for a reason you can see immediately.** In dimension 2 there is
no sphere strictly between a circle and the whole 2-sphere, so "closed or dense" is forced by
the lack of anything in between. In higher dimension there are proper sub-spheres. Suppose C
sits inside a k-sphere Σ, and suppose ΓΣ is *closed* in the space of sub-spheres. Then ΓC‾ is
trapped inside ΓΣ; it cannot get out. **Intermediate orbit closures are possible.**

The theorem says those are the only new possibilities:

> **Theorem (Minju Lee and Oh, *Geom. Topol.* 28 (2024); paper Cor. 4.7).** Let ℳ be a convex
> cocompact hyperbolic d-manifold with **Fuchsian ends** (= totally geodesic convex-core
> boundary; for d = 3 this is the rigid acylindrical case). Let C be a circle meeting Λ in
> **more than two points**. Then there is a k-sphere S with
>
> **ΓC‾ = { D ∈ 𝒞_Λ : D ⊂ ΓS }.**

If S = C, ΓC is closed. If S is the whole boundary sphere, ΓC is dense. Everything in between
is an intermediate closure, and each one is accounted for by an intermediate sphere with a
closed orbit.

*(She says "at least two points"; the paper says "more than two points". I quote the paper.)*

The underlying theorem (paper Thm 4.3) is a genuine Ratner analogue: for U any connected
closed subgroup generated by unipotents and normalized by A, and any x in the **renormalized
frame bundle** RF ℳ = {x : xA is bounded}, the closure xU‾ ∩ RF ℳ = xL ∩ RF ℳ for a closed
subgroup U < L < G with xL closed. RF ℳ is exactly the set of §2.2 — frames whose geodesic
stays bounded in both directions, the support of the BMS measure.

**What is new in the proof, and her best passage.** Thick recurrence is no longer enough,
because the returns might all happen inside one of the intermediate closed orbits, in which
case you learn nothing. You need an **avoidance theorem**: unless the orbit is already
trapped in an intermediate closed orbit, you must find thick recurrence times that also stay
a definite distance away from every compact piece of the singular set. This is the
infinite-volume descendant of the **Dani–Margulis avoidance principle**.

And the difficulty is that you do not know what you are avoiding:

> "So, remember this example about the closed orbit. So, there are visible obvious closed
> orbits, but there are invisible hidden closed intermediate orbits. So, the collection of
> all closed intermediate orbits — to me they're like wild forest that I cannot even draw...
> And now we need to find a time when this circular slice can get out of this wild forest.
> So, Minju and I, we got lost actually for a long time in this wild forest until we finally
> were able to get out."

With avoidance in hand the proof runs an elaborate induction over all possible intermediate
sub-spheres, indexed by the dimension of the maximal unipotent subgroup of the acting group.

> *[Gap: the internals of the avoidance theorem and the inductive scheme are not recoverable.
> The talk gives the two paragraphs quoted above; the paper (§4.2) gives one paragraph
> naming Dani–Margulis and saying the induction incorporates unipotent dimension plus
> equidistribution statements, then cites [43] and [57]. I state the motivation and the
> consequence and do not attempt the proof. **Impact: low.** These are the technical core of
> a 100-page paper; nothing downstream in the talk depends on their internals.]*

A geometric corollary worth having because it is so concrete (paper Cor. 4.4): in such a
manifold, **any horocycle** is either properly immersed and closed, or its closure is a
properly immersed totally geodesic k-plane (k ≥ 2), up to tilting. The paper points to Oh's
*Notices* article, where this is told as the journey of a traveller and compared to
**Kronecker's theorem** on the closure of a line in a torus — rational slope closes up,
irrational slope fills the torus, nothing else happens. That is the right one-line summary
of the whole rigidity phenomenon, and it is the version to remember.

### 4.7 Q3: rigidity — how many circles force Möbius

Now the third question, and the point where the talk becomes a 4.

Set-up. Given a Kleinian group Γ, let ℜ_disc(Γ) be its **discrete faithful representations**
ρ : Γ → PSL₂(ℂ). Conjugation by a fixed Möbius g gives one, γ ↦ gγg⁻¹; call those
**algebraic**. Question: when is a given ρ algebraic?

- **If Γ is a lattice: always.** That is **Mostow–Prasad strong rigidity** (paper Thm 5.1).
  So the question is entirely about the non-lattice, infinite-volume case.
- **If Λ = Ĉ but Γ is not a lattice: still yes** for quasiconformal deformations. That is
  **Sullivan's** quasiconformal rigidity theorem (paper Thm 5.3).
- **If Λ ≠ Ĉ: no.** By the Ahlfors finiteness theorem the deformation space is as big as the
  Teichmüller space of Γ\Ω. There are genuinely non-algebraic representations. So you need a
  *criterion*.

**Reformulate via the boundary map.** ρ carries the Γ-orbit to the ρ(Γ)-orbit; limit points
go to limit points. So there is a Γ-equivariant continuous embedding

> f : Λ → Ĉ,  the **boundary map** of ρ,

unique when it exists (existence: Tukia, when Γ and ρ(Γ) are geometrically finite and ρ is
type-preserving — loxodromics to loxodromics, parabolics to parabolics). And:

> **ρ is algebraic ⟺ f is the restriction to Λ of a Möbius transformation.**

*(Figure 5.3 in the paper is exactly this: two limit sets side by side with an arrow between
them.)*

**Sullivan's theorem as the model.** Sullivan proved: if f is Γ-equivariant quasiconformal
and **conformal on Ω** (the domain of discontinuity), then f is Möbius. So conformality on
the *complement* of the limit set forces rigidity. The natural question is whether
conformality on the limit set *itself* does. The obstacle: Λ typically has Lebesgue measure
zero (the **Ahlfors measure conjecture**, now a theorem via Thurston, Canary, Agol,
Calegari–Gabai on tameness: for finitely generated Γ, either Λ = Ĉ or Leb(Λ) = 0), so the
analytic definition of conformality is meaningless there.

**The geometric substitute is the circular slice.** Define f to be *conformal on Λ* if

> for every circle C, f(C ∩ Λ) is contained in a circle.

Note what this does *not* ask. It does not ask f to map circles to circles — f is defined only
on Λ. It asks only that the part of each circle that Λ actually sees goes into a circle.
Oh underlines this twice from the podium.

> **Theorem (Dongryul M. Kim and Oh, *Invent. Math.* 234 (2023); paper Thm 5.4).** Let Γ be a
> Kleinian group with Ω having **at least two components**, let f be a Γ-equivariant
> quasiconformal homeomorphism of Ĉ, and suppose neither Λ nor f(Λ) lies in a circle. If f is
> conformal on Λ in the above sense, then **f is a Möbius transformation.**

The hypothesis "Ω disconnected" is her spoken "the complement of the limit set is
disconnected", and it is genuinely needed: her third example (a limit set with connected
complement) is excluded. The paper notes the theorem applies to all geometrically finite
groups with **connected** limit set — so all acylindrical and all quasi-Fuchsian groups — but
not to Schottky groups.

**The cross-ratio form, which is the version to remember.** The cross-ratio of four points of
Ĉ is a complex number, invariant under Möbius transformations. The elementary fact:

> **the cross-ratio of four points is real ⟺ the four points lie on a circle.**

So "sends circular slices into circles" = "sends real-cross-ratio quadruples to
real-cross-ratio quadruples", and (paper Cor. 5.6):

> **Cross-ratio rigidity.** If f sends every quadruple of points of Λ with real cross-ratio to
> a quadruple with real cross-ratio, then f extends to a Möbius transformation.

Her emphasis, and it is the sharpest sentence in the talk:

> "Again, I would like to emphasize we are not asking F to preserve **values** of cross
> ratios. We are only asking F to preserve the **property** that the cross ratio is a real
> number."

Preserving values would be the whole Möbius invariant; that would be circular. Preserving a
purely qualitative property — the imaginary part vanishes — is an enormously weaker
hypothesis, and it forces the same conclusion. §7.4 is about why that is the interesting
shape.

**And it is a dichotomy, not just a criterion.** Let Λ_f be the union of all circular slices
that f sends into circles — her "conformal points" (paper eq. 5.1, Figure 5.2). Then (paper
Thm 5.5, topological criterion):

> **Either Λ_f = Λ (and f is Möbius), or Λ_f has empty interior in Λ.**

and (paper Thm 5.7, measure-theoretic criterion, for Γ geometrically finite and ρ
type-preserving geometrically finite; *J. Topol.* 18 (2025)):

> **Either Λ_f = Λ, or ν(Λ_f) = 0**, where ν is the Patterson–Sullivan measure of §3.6.

Her spoken version: if f is not Möbius, the set of circular slices it straightens is "trivial
both topologically and measure-theoretically" — a typical circular slice is *not* sent to a
circle. *(The captions render the measure as "parabolic measure"; the paper's ν is the
Patterson–Sullivan / geometric measure, and §5.1 says the set has zero δ-dimensional
Hausdorff measure. I quote the paper.)*

### 4.8 The mechanism for Q3: self-joinings, and going up in rank

How do you prove a rigidity statement like that? By a genuinely surprising move: **make a
new, bigger group out of the two you have, and study a flow on it.**

> **The self-joining.** Γ_ρ := (id × ρ)(Γ) = {(γ, ρ(γ)) : γ ∈ Γ} < PSL₂(ℂ) × PSL₂(ℂ)

— the graph of ρ, embedded diagonally. It is a discrete subgroup of the *product*, so it acts
on ℍ³ × ℍ³, and the quotient Γ_ρ\(ℍ³ × ℍ³) "joins" the two hyperbolic manifolds Γ\ℍ³ and
ρ(Γ)\ℍ³ into one object (Figure 5.4). Its limit set inside Ĉ × Ĉ is the graph of the boundary
map:

> Λ_ρ = {(ξ, f(ξ)) : ξ ∈ Λ}.

And the observation that makes the whole strategy work (paper eq. 5.4):

> **ρ is algebraic ⟺ Γ_ρ is NOT Zariski dense in PSL₂(ℂ) × PSL₂(ℂ).**

Which is obvious once you see it: if ρ = conjugation by g, then Γ_ρ sits inside the graph of
an automorphism, a proper algebraic subgroup. So **rigidity becomes a Zariski-density
question**, and Zariski density is what makes dynamical theorems apply.

The proof then shows that conformality of f on Λ *obstructs* Zariski density, using
topological transitivity (for Thm 5.5) and ergodicity (for Thm 5.7) of a diagonal flow on the
self-joining quotient.

**And here is where the rank jumps.** The product of two copies of PSL₂(ℂ) has a
**two-dimensional** diagonal subgroup:

> A_u = { (diag(e^{u₁t/2}, e^{−u₁t/2}), diag(e^{u₂t/2}, e^{−u₂t/2})) : t ∈ ℝ },  u = (u₁, u₂)

Instead of one geodesic flow there is now a **family of flows, one per direction u**, and — as
Oh says — "the dynamics of A_u in rank two depend crucially on the direction u". That is the
whole difference between rank one and higher rank, and it is why questions 3 and 4 are a
harder tier than 1 and 2. Everything is now indexed by a direction in a cone.

> *[Declining to teach: the Lie theory of higher rank. Positive Weyl chamber, Cartan
> projection μ(γ), limit cone ℒ_ρ, growth indicator ψ_ρ, tangent linear forms, Anosov and
> Borel Anosov subgroups. The paper defines all of them in §8; each definition is a paragraph
> and each is genuinely necessary for the proofs. You do not have the background and cannot
> get it from a tutorial. I state the results in words below and name the objects so you can
> recognise them, and no more. **Impact: moderate.** It costs you the ability to read §§8.1–8.5
> of the paper. It costs you nothing in the four questions.]*

The one piece of it worth internalising, because the anchor of §2.3 gives it to you free: the
**growth indicator** ψ_ρ is Quint's replacement for δ. Where δ was one abscissa of
convergence, ψ_ρ(u) is the abscissa of convergence of a Poincaré-type series computed within
a narrow cone of directions around u. It is upper semicontinuous and **concave**, and the
directions where it is ≥ 0 form the limit cone. A single free energy has become a concave
free-energy *function* on a cone of directions. Figure 8.1 draws exactly this: a cone in the
plane with a ray in its interior.

### 4.9 Q4: torus counting, and the exponent that depends on your ordering

A **torus** here is just a pair of circles T = (C₁, C₂) ⊂ ℂ², with

> vol(T) = rad(C₁) · rad(C₂).

*(She says "area"; the paper says "volume". Same formula.)* Where do torus packings come from?
From Q3. If f is a non-algebraic quasiconformal deformation, then by the *combination* of the
Q2 dichotomy and the Q3 rigidity theorem, the set of circles that f does straighten is a
finite union of closed orbits — because if it were dense, continuity would make f straighten
everything, and Thm 5.4 would force f Möbius, contradiction. That is the paper's Theorem 6.1
and its half-page proof is the one place where the four questions visibly interlock.

So take 𝒫 = {(C, f(C)) : #(C ∩ Λ) ≥ 2}, a locally finite torus packing invariant under the
self-joining Γ_ρ. Then:

> **Theorem (Samuel Edwards, Minju Lee and Oh, *J. reine angew. Math.* 807 (2024); paper Thms
> 6.2, 6.3).** There are constants c_f > 0, δ_f > 0 and a locally finite measure ω_f on the
> graph {(ξ, f(ξ))} such that
>
> **#{T ∈ 𝒫 : vol(T) ≥ t, T ∩ R ≠ ∅} ~ c_f · ω_f(R) · t^{−δ_f}  as t → 0.**

Same shape as circle counting: a power law, a constant, a measure controlling where the small
tori go. The hypothesis in the general version (Thm 6.3) is that all the representations are
**convex cocompact**, i.e. **no cusps** — Oh states this explicitly and explains why in §4.10.

**The genuinely new phenomenon, and the best idea in the second half.** In circle counting
there was one exponent, δ, a property of Γ. In torus counting the exponent
δ_{ρ,vol} **is not the critical exponent of Γ_ρ**. The paper, §6.3:

> "In higher rank, however, the exponent depends on how the tori are ordered in the counting
> problem."

Concretely: if you replace vol(T) = ∏ rad(C_i) by the weighted version ∏ rad(C_i)^{κ_i} with
weights κ_i > 0, the exponent becomes

> limsup_{t→∞} (1/t) · log #{ γ ∈ Γ : Σ_i κ_i · d(ρ_i(γ)o, o) ≤ t }.

Read that as a partition function again (§2.3), but now with a **joint energy**: each group
element is charged by a weighted sum of its displacements in the several manifolds at once.
Change the weights and you change which directions in the cone dominate, and you get a
different exponent. The volume ordering is the case κ_i = 1.

> **The scaling exponent is a property of your cost function, not of the object.** In rank one
> the cone is one-dimensional and there is nothing to choose, so the exponent looks intrinsic.
> It never was. §7.3.

### 4.10 What runs underneath: local mixing, and the cusp gap

Both counting theorems reduce to one analytic input. Oh names it in one sentence — "the main
dynamical tool behind this torus counting theorem is a local mixing theorem" — and the paper
spends two sections on it. Compressed to what she used:

- **Rank one** (paper Thm 7.2, Roblin, Winter): the renormalized correlation formula of §2.3.
  This is what drives circle counting.
- **Higher rank** (paper Thm 8.1, Edwards–Lee–Oh, *Geom. Topol.* 27 (2023)): for each
  direction u in the interior of the limit cone there is κ_u > 0 with
  lim t^{(n−1)/2} e^{t(σ−ψ_ρ)(u)} ⟨a_{tu}·f₁, f₂⟩ = κ_u · m^BR_u(f₁) m^BR*_u(f₂). Same shape:
  find the exact decay rate, divide it out, get a product of two measures. The rate now
  depends on the direction, via the growth indicator, and there is an extra polynomial factor
  t^{(n−1)/2}.
- **The gap Oh names out loud.** The counting theorem needs the self-joining Γ_ρ to be an
  **Anosov** subgroup (higher-rank analogue of convex cocompact), and Γ_ρ is Anosov exactly
  when every ρ_i is convex cocompact. With cusps you get a *relatively* Anosov group, and:

> "When there are cusps, this Γ_ρ is relatively Anosov, and this is why I had this hypothesis
> that the associated hyperbolic manifolds have no cusps — because higher rank local mixing
> is a missing input for relatively Anosov groups."

That is the honest frontier statement of the talk: one missing analytic theorem is what stops
Q4 from being known in the generality of Q1. The paper says the same in §6.4.

### 4.11 One paper-only result worth your time: the drunken bird

*(This is not in the talk. It is paper §8.4, and I include it because it is Pólya's theorem,
which you own cold.)*

The BMS measure in higher rank has a product structure: it is a rank-one BMS-type measure on
a *compact* space, times Lebesgue measure on ℝ^{n−1}. So the phase space is homeomorphic to
Ω_u × ℝ^{n−1} — a compact hyperbolic system times a Euclidean space of dimension n − 1. The
paper draws the obvious conclusion:

> "This suggests an analogy with random walks on Euclidean spaces. In dimensions one and two,
> a random walk almost surely returns home (a 'drunken person'), while in higher dimensions,
> a 'drunken bird' tends to fly off to infinity."

> **Theorem (Burger, Landesberg, Lee, Oh, *J. Mod. Dyn.* 19 (2023); paper Thm 8.4).** For u
> in the interior of the limit cone, the A_u-action on (Γ_ρ\G, m^BMS_u) is ergodic **if and
> only if n ≤ 3.**

Pólya's recurrence theorem, exactly: n − 1 ≤ 2 is recurrent, n − 1 ≥ 3 is transient, and
transience kills ergodicity. For self-joinings of two Kleinian groups n = 2, so the flow is
ergodic and Theorem 5.7 goes through. Join four or more and it does not. **A rank threshold in
a Lie-theoretic theorem is the dimension threshold of a random walk.**

---

## 5. The one argument: how circle counting actually works

Her proof of Q1, in her own order, with the pieces named. This is the argument to hold, and
every step uses something built above.

**Step 1 — turn circles into surfaces.** Take a circle C in the locally finite packing 𝒫.
Form the hemisphere C† over it (§3.3). Push down to ℳ = Γ\ℍ³. Because ΓC is closed in the
space of circles, the image is a **properly immersed closed geodesic surface** S ⊂ ℳ. In her
slide this is a green hemisphere upstairs and a green surface downstairs.

**Step 2 — take the normal bundle and flow.** Attach to S its unit normal bundle: at every
point of S, the two unit vectors perpendicular to it, drawn as outward arrows all over the
green surface. Now apply the geodesic flow for time t. What you get is the set of points at
perpendicular distance t from S — the **orthogonal translate** of S. Upstairs, these are
expanding balloons around the hemisphere (Figure 2.8). As t → ∞ the balloons in the universal
cover swell and escape.

**Step 3 — watch the mass die, and find the rate.** Downstairs, the translates do come back
into the compact part of ℳ, but less and less of them do:

> "As indicated in this picture, they do come back to a compact part. But however, lesser and
> lesser parts will come back to a compact part and more and more part will go toward
> infinity. So, in any fixed compact region, the mass seen will go to zero as t goes to
> infinity."

This is the failure of §2.1, seen concretely. The repair is §2.3: renormalize by the exact
rate, which is **e^{(2−δ)t}**.

**Step 4 — the renormalized limit is a measure, and it is Burger–Roblin.** After
renormalization the orthogonal translates **equidistribute** with respect to the
Burger–Roblin measure on the unit tangent bundle — the infinite fractal measure of §3.8,
built from Patterson–Sullivan data on the boundary. This is Theorem 7.2 of the paper applied
to this configuration; the mechanism is local mixing of the geodesic flow, plus Roblin's
transversal intersection argument to move from the BMS-measure statement to a Haar-measure
statement (Haar being the one you can change variables in).

**Step 5 — the coefficient is the skinning mass, and the counting follows.** The
proportionality coefficient in that equidistribution statement is the total mass of the
**skinning measure** of S (§4.2). Unwinding: each circle of radius ≥ t in 𝒫 corresponds to a
group element moving the base plane a hyperbolic distance ≤ log(1/t), the number of such
elements grows like e^{δT} with T = log(1/t) — giving t^{−δ} — and the constant of
proportionality is the skinning mass divided by the total BMS mass:

> **#{C ∈ 𝒫 : rad(C) ≥ t} ~ (sk_Γ(𝒫)/|m^BMS|) · ω_Γ(ℂ) · t^{−δ}.**

**Where each ingredient came from.** The exponent came from orbit growth = Hausdorff
dimension (§3.5). The measure came from Patterson–Sullivan (§3.6). The denominator came from
the finiteness of the BMS measure (§2.2), which needs geometric finiteness. The numerator came
from how the specific surface meets the limit set (§4.2). The renormalization exponent 2 − δ
came from the decay rate of correlations (§2.3). Remove any one of the five and the theorem
does not exist.

**One footnote from the paper worth having** (fn. 4): the *original* proof of the Apollonian
case used the **Descartes circle theorem** to convert circle counting into counting points in
the space of horospheres. That route is specific to Apollonian packings, and it is the reason
the Apollonian case came first historically. Exercise 6.1 is that theorem.

---

## 6. Do this by hand

Three exercises. The first two are the ones that teach.

### 6.1 The Apollonian recursion, and why the curvatures stay integers

Define the **curvature** of a circle to be 1/radius. Descartes' circle theorem (Descartes
1643; Soddy 1936) says that four mutually tangent circles with curvatures a, b, c, d satisfy

> **(a + b + c + d)² = 2(a² + b² + c² + d²).**

*(This identity is standard literature. Neither the talk nor the paper writes it out; the
paper names "the Descartes circle theorem" in footnote 4, and Corollary 7.8 refers to
"quadruples of curvatures of four mutually tangent circles" as points on "the zero locus of
the Descartes quadratic form", with the footnote "this means that curvatures of all circles
in 𝒫 are integers". So the object is in the source; the formula is mine.)*

**(a)** Fix a, b, c. Treat the identity as a quadratic equation in d. Show it has two roots
d and d′, and find d′ in terms of a, b, c, d.

**(b)** Explain what the two roots are, geometrically, in terms of Apollonius' theorem as
stated in §1.

**(c)** Conclude: if you begin with four mutually tangent circles whose curvatures are all
integers, every circle in the resulting Apollonian packing has integer curvature.

**(d)** Connect this to the talk. Oh says the symmetry group of an Apollonian packing "is
generated by the inversions with respect to the four dual circles" (paper §2.1, Figure 2.1:
four red circles, each orthogonal to three of the four mutually tangent ones). What does part
(a) have to do with those four generators?

<details>
<summary>Solution</summary>

**(a)** Write S = a + b + c and P = a² + b² + c². The identity reads (S + d)² = 2(P + d²),
i.e. S² + 2Sd + d² = 2P + 2d², i.e.

> d² − 2Sd + (2P − S²) = 0.

A monic quadratic, so by Vieta the two roots satisfy d + d′ = 2S. Hence

> **d′ = 2(a + b + c) − d.**

**(b)** They are the two circles of Apollonius' theorem: given the three mutually tangent
circles of curvature a, b, c, there are exactly two circles tangent to all three, and their
curvatures are the two roots. One sits in the curvilinear triangle (large curvature, small
circle), the other wraps around the outside (small or negative curvature — negative curvature
means the circle contains the others, i.e. it is the outer bounding circle traversed the
other way). Apollonius' theorem *is* the statement that this quadratic has two roots.

**(c)** Immediate induction. Every new circle is obtained from three existing ones plus the
one it replaces, by d′ = 2(a + b + c) − d. If a, b, c, d ∈ ℤ then d′ ∈ ℤ. Start integral, stay
integral, forever. This is why integral Apollonian packings exist at all, and why the paper
can ask (Cor. 7.8) how many circles have *prime* curvature — a question that only makes sense
because of this five-line computation.

**(d)** The map (a, b, c, d) ↦ (a, b, c, 2(a+b+c) − d) is an involution: apply it twice and
you are back. It is a **reflection** of ℤ⁴ — it fixes the hyperplane d = a + b + c and negates
the transverse direction — and it preserves the Descartes quadratic form
Q = 2(a²+b²+c²+d²) − (a+b+c+d)². There are four such involutions, one for each choice of
which coordinate to swap out. The group they generate is the **Apollonian group**, a discrete
group of integral matrices preserving Q, and it is the arithmetic avatar of the group Oh
describes as generated by inversions in the four dual circles. The quadratic form Q has
signature (3,1), so its orthogonal group is Isom(ℍ³) — which is why this whole
number-theoretic picture is *literally the same object* as the hyperbolic-geometry picture.
That equivalence is the bridge Kontorovich and Oh used in 2011.

*Marked as reconstructed:* parts (a) and (d) are my computation. What would verify (d): check
directly that Q(a,b,c,2(a+b+c)−d) = Q(a,b,c,d), and that the four reflections generate a group
of index 24 in the automorphism group of Q (the extra factor being permutations of
coordinates). The signature-(3,1) statement is standard; the paper states only that the
curvature quadruples lie on the zero locus of Q.

</details>

### 6.2 Why the exponent is δ — and why the constant is the hard part

Oh says of her own theorem: "perhaps it's less surprising that we see delta here, because
delta is the exponential growth rate of a Γ orbit." Make that precise.

Fix o = (0,0,1) ∈ ℍ³ and a base circle C₀ with hemisphere C₀†. The packing is 𝒫 = ΓC₀ (take
one orbit for simplicity).

**(a)** Show that a circle of Euclidean radius r centred at the origin has its hemisphere's
apex at hyperbolic distance |log r| from o. Conclude the heuristic: for g ∈ PSL₂(ℂ),

> rad(gC₀) ≈ e^{−d(o, gC₀†)}.

**(b)** Using #{γ ∈ Γ : d(o, γo) ≤ T} ≍ c·e^{δT} (§3.5), derive the shape of the counting
asymptotic.

**(c)** Say exactly what this argument does **not** deliver, and why that missing piece is the
subject of §4.2.

<details>
<summary>Solution</summary>

**(a)** The hemisphere over the circle of radius r centred at 0 has apex (0, 0, r). Along the
vertical axis the metric is dy/y, so

> d((0,0,1), (0,0,r)) = |∫_r^1 dy/y| = |log r|.

Hence r = e^{−d(o, apex)}. For a general small circle the apex is not the nearest point of the
hemisphere to o, but the two differ by a bounded amount, so rad ≍ e^{−d(o, C†)} up to
multiplicative constants depending on nothing that matters here.

**(b)** Set T = log(1/t). Then

> #{C ∈ 𝒫 : rad(C) ≥ t} ≈ #{γ ∈ Γ/Stab : d(o, γC₀†) ≤ T} ≍ e^{δT} = e^{δ log(1/t)} = **t^{−δ}**.

The exponent is forced, and it is forced by orbit growth alone. That is the whole content of
her remark.

**(c)** It gives the exponent and nothing else. It does not give:

- **the constant**, because ≍ hides a bounded multiplicative ambiguity, and the theorem claims
  an *asymptotic* (~), not a bound. Getting from ≍ to ~ requires knowing that the translates
  of the plane equidistribute, which is the whole of §5, and the constant that emerges is
  sk_Γ(𝒫)/|m^BMS|;
- **the local statement** — how many circles land in a given region R. That needs the measure
  ω_Γ, i.e. Patterson–Sullivan theory;
- **the dependence on how the plane sits**. Two different base circles C₀ with the same δ give
  different constants. The exponent is a property of the group; **the constant is a property
  of the surface**. That is why the skinning measure exists.

*Marked as reconstructed:* this heuristic is mine. Neither source writes it; Oh gestures at it
in one sentence. What would verify it: Oh–Shah, *The asymptotic distribution of circles in the
orbits of Kleinian groups*, Invent. Math. 187 (2012), where the relation between rad(gC) and
the displacement is made exact.

</details>

### 6.3 Real cross-ratio means concyclic

The identity behind cross-ratio rigidity (§4.7). For z₁, z₂, z₃, z₄ ∈ Ĉ the cross-ratio is
(z₁,z₂;z₃,z₄) = ((z₁−z₃)(z₂−z₄)) / ((z₁−z₄)(z₂−z₃)). Show it is real if and only if the four
points lie on a common circle or line.

<details>
<summary>Solution</summary>

The cross-ratio is real ⟺ its argument is 0 or π (mod 2π). Now

> arg(z₁,z₂;z₃,z₄) = [arg(z₁−z₃) − arg(z₂−z₃)] − [arg(z₁−z₄) − arg(z₂−z₄)]

which is the angle ∠z₁z₃z₂ minus the angle ∠z₁z₄z₂: the two angles subtended by the segment
z₁z₂ at the points z₃ and z₄. So the cross-ratio is real exactly when those two subtended
angles are equal (difference 0) or supplementary (difference π). The **inscribed angle
theorem** says that is exactly the condition for z₃ and z₄ to lie on a circle through z₁ and
z₂ — equal angles for the same arc, supplementary for opposite arcs. Degenerate case:
difference 0 with all four collinear, i.e. the circle through ∞.

Why this matters for the talk: it converts a *geometric* hypothesis ("f sends circular slices
into circles") into a purely *algebraic* one ("f preserves the reality of cross-ratios"), with
no geometry left in it. And "is real" is a codimension-one condition — a single equation,
Im = 0 — which is what makes it a weak hypothesis with a strong conclusion.

*This is standard; the paper states the fact and does not prove it. The proof above is mine.*

</details>

---

## 7. What is actually useful to you

Five things. The first two are the ones I would actually reach for.

### 7.1 When the average dies, find the rate — do not conclude "no signal"

The single reusable move of the talk. The raw correlation ⟨a_t f₁, f₂⟩ → 0. Every naive
statistic on this system returns zero. The response is not "the system is degenerate"; it is:

> find the exact exponential rate at which it dies, divide it out, and the limit is a real
> object.

Here the rate is e^{−(2−δ)t}, the limit is a product of Burger–Roblin masses, and *the entire
counting theory of the subject is downstream of it*. The renormalization exponent is not a
nuisance parameter — it is δ, the most important invariant in sight, and it fell out of the
requirement that the limit be finite and nonzero.

Applied to what you do: metrics that decay toward zero as a system scales up — per-step
success rates over long agent trajectories, per-token error rates as context grows, cache hit
rates as a corpus grows — are usually reported as "it degrades" and then abandoned. The
informative quantity is almost never the value; it is the exponent, and the exponent is often
a stable property of the system while the value is not. Two configurations with the same
decay exponent and different constants are the *same* system with different setups. Two with
different exponents are different systems. You cannot see that distinction without dividing
out the rate first.

And note the structural bonus: once you have the right renormalization, the limit *factorises*
into (a measure on where you started) × (a measure on where you ended) / (a normalising mass).
Correctly renormalized quantities decouple. Badly renormalized ones do not.

### 7.2 When the free invariant is gone, construct it — and make it quantitative

Poincaré recurrence is free in finite measure. It is unavailable here, and the response is not
to weaken the theorem. It is to build, explicitly, a compact set 𝓡 and prove a **quantitative
return guarantee**: for every x ∈ 𝓡 and every scale s, there is a return at some time t with
s < |t| < κs.

Look at the form of that statement, because it is the engineering content. Not "returns
infinitely often" (unfalsifiable in practice, and not what you need) but **"in every window of
fixed multiplicative width, at every scale, there is a return"**. Uniform, scale-invariant,
checkable.

And where does it come from? Not from measure theory. From a *geometric fatness property of a
fractal*: the limit set's circular slices contain uniformly perfect Cantor sets, which is a
statement that no scale is empty, which converts into no scale being return-free.

For agent systems the analogy is close enough to be operational. A long-running agent loop has
no conserved quantity and no invariant measure; "it eventually recovers" is not a property you
can build on. What you can build on is: a designated set of known-good states, plus a
guarantee that from any reachable state the system re-enters that set within a bounded
*multiple* of elapsed time — not a fixed timeout, a multiplicative window, so the guarantee
survives scale changes. That is exactly thick recurrence, and it is exactly what makes
otherwise-unprovable classification statements provable here.

### 7.3 Your scaling exponent is a property of your cost function

In rank one there is one exponent δ, and it looks like an intrinsic property of the group. In
rank two it is not: order the tori by volume and you get one exponent; order them by
∏ rad(C_i)^{κ_i} and you get

> limsup (1/t) log #{γ ∈ Γ : Σ_i κ_i d(ρ_i(γ)o, o) ≤ t},

a different number for different weights. The single number δ was an artefact of a
one-dimensional cone of directions, where there was nothing to choose.

This is directly transferable to any scaling claim you read or make. "Performance scales as
N^α" is a statement about the *ordering you sorted by*, not about the system, whenever the
system has more than one cost dimension. Sort by wall-clock and you get one exponent; by token
spend, by tool calls, by a weighted mixture — different exponents, all correct, all measuring
the same object through different cost functionals. Whenever you see a scaling exponent
reported without the cost functional stated, the exponent is underdetermined. The higher-rank
lesson is that the honest object is not a number but a **concave function on the cone of cost
directions**, and any single reported exponent is one tangent line to it.

### 7.4 Find the weakest qualitative invariant that forces the conclusion

Cross-ratio rigidity is the cleanest instance of a design pattern I keep wanting a name for.

You want to certify that a map f is exactly a Möbius transformation. The naive certificate:
check that f preserves cross-ratio *values*. That is circular — preserving all cross-ratios is
essentially a restatement of being Möbius, so it is not a test, it is the definition.

The theorem instead asks f to preserve only the **property** "this cross-ratio is real". That
is a single-bit, codimension-one, purely qualitative condition. It does not pin down any
value. And it still forces the full conclusion.

Two things make it work, and both are checkable in your own settings: the property is
**closed under the structure you care about** (real cross-ratio ⟺ concyclic, and Möbius maps
preserve concyclicity), and the object being tested is **rigid enough that a codimension-one
condition on a large enough set has no slack**. When both hold you get an enormous
strengthening for free — you have replaced a measurement with a predicate.

For verification of generated artefacts: the reflex is to check outputs against expected
values, which is expensive, brittle, and usually circular (you needed the answer to write the
test). The move here is to look for a *qualitative invariant* — a predicate with no
parameters, preserved by every legitimate transformation and violated by every illegitimate
one — and check that instead. Then add the second half of the theorem: the dichotomy. Oh does
not merely prove "preserve it everywhere ⟹ rigid"; she proves **either everywhere, or almost
nowhere** (Λ_f = Λ or ν(Λ_f) = 0). There is no middle. That is the property that makes a cheap
predicate into a real test: a partial pass is impossible, so a partial pass means your
assumptions are wrong.

### 7.5 The obstruction is rarely the chaos; it is the hidden intermediate structure

The higher-dimensional orbit-closure theorem was hard, and Oh is explicit about *why*, and it
is not the reason you would guess. The dense case is fine. The closed case is fine. What cost
her and Minju Lee a long time is the **wild forest**: a countable family of intermediate
closed orbits, some visible, most invisible, that a trajectory can get trapped in and that you
cannot enumerate or draw. The technical fix — the avoidance theorem — is specifically about
staying away from a set you cannot describe.

The general shape: when you classify the behaviours of a system, the enemy is not the chaotic
regime and not the trivial regime. It is the **countable family of partially-structured
absorbing states between them** — the modes where the system does something coherent but not
the coherent thing you designed for. Those are the ones that are invisible in aggregate
statistics (each is measure zero), impossible to enumerate in advance, and individually
sticky. The design response is not to enumerate them; it is to prove a positive statement
about escaping neighbourhoods of *all* of them at once.

That is what "avoidance" means as a discipline: you do not need to know the failure modes if
you can prove the system spends a definite fraction of its returns at a definite distance from
every one of them.

---

## 8. Where to read next

Three, ordered. Read the first one even if you read nothing else.

1. **Hee Oh, *Euclidean traveller in hyperbolic worlds*, Notices Amer. Math. Soc. 69 (2022),
   1888–1897.** Reference [56] of the paper. Written for a general mathematical audience, and
   it tells the horocycle-closure story as the journey of a traveller, comparing the rigidity
   theorem to Kronecker's theorem on lines in a torus (§4.6 above). It is the same mathematics
   as questions 1 and 2 with none of the machinery and all of the pictures. This is your
   fastest route to owning the geometry.
2. **Hee Oh, *Dynamics and Rigidity through the Lens of Circles*,
   [arXiv:2510.10771](https://arxiv.org/abs/2510.10771).** The proceedings paper and the
   source of every formula above. Sections 1–6 are the talk. §§2.4, 3.6 and 5.5 are the three
   places where reading the paper genuinely adds something the talk could not fit. Sections 7
   and 8 are for specialists.
3. **Hee Oh, *Dynamics for discrete subgroups of SL₂(ℂ)*, in *Dynamics, geometry, number
   theory — the impact of Margulis on modern mathematics*, Univ. Chicago Press, 2022,
   pp. 506–566.** Reference [57]. The long survey, with the proofs sketched at a level between
   the Notices article and the research papers.

If you want the original circle-counting theorem in its own words: Kontorovich and Oh,
*Apollonian circle packings and closed horospheres on hyperbolic 3-manifolds*, J. Amer. Math.
Soc. 24 (2011), 603–648 — the paper that started this line, and the one that uses the
Descartes theorem of Exercise 6.1.

---

## 9. Self-test

<details>
<summary>1. Why is "infinite volume" the defining difficulty of this subject, rather than a technical hypothesis?</summary>

Because a Kleinian group whose limit set is an interesting fractal is never a lattice — a
finite-volume quotient forces Λ = Ĉ, the whole sphere, with no fractal and no packing. So the
moment the picture is interesting, vol(Γ\ℍ³) = ∞. And infinite invariant measure removes both
Poincaré recurrence and the Birkhoff ergodic theorem, which are the hypotheses under which
every finite-volume counting, equidistribution and orbit-closure theorem was proved. Both
halves of the standard toolkit vanish at once.
</details>

<details>
<summary>2. What is the finite measure hiding inside the infinite one, and why does it exist?</summary>

The **Bowen–Margulis–Sullivan measure** on the frame bundle, supported on the vectors both of
whose geodesic endpoints lie in the limit set — equivalently, the directions along which the
geodesic stays bounded in both time directions. Its support projects into the convex core.
Sullivan proved |m^BMS| < ∞ for geometrically finite Γ; for convex cocompact groups this is
immediate from compactness of the core, and with cusps it is a real theorem about cusp
geometry. It is the object that replaces "vol(X) < ∞" in every proof, and it appears in the
denominator of every constant in the talk.
</details>

<details>
<summary>3. State the relation between δ, orbit growth, and Hausdorff dimension, and say why it is surprising.</summary>

δ is defined as the exponential growth rate of a Γ-orbit inside ℍ³:
δ = limsup_T (1/T) log #{x ∈ Γo : d(x,o) ≤ T}. The theorem of Patterson and Sullivan is that
**δ = dim(Λ)**, the Hausdorff dimension of the limit set on the boundary sphere. It is
surprising because it equates a growth rate measured in the interior with a fractal dimension
measured at infinity — a dynamical quantity with a geometric one. In thermodynamic terms it is
"free energy = dimension". For Apollonian packings δ_A ≈ 1.3057, the same for every such
packing.
</details>

<details>
<summary>4. What is the Patterson–Sullivan measure, in one line, and why does it exist only at s = δ?</summary>

It is the unique Γ-conformal probability measure of dimension δ: the unique ν on Ĉ with
dγ_*ν/dν(ξ) = e^{δ·β_ξ(o,γo)} for all γ ∈ Γ, where β is the Busemann function. It is supported
on Λ. It is a Gibbs state: the transformation law is a DLR condition prescribing how the
measure responds to the symmetry group in terms of an energy. It exists only at the critical
exponent because δ is exactly the abscissa of convergence of the associated Poincaré series —
below it the construction diverges, above it collapses. This is a phase transition, and ν is
the state at the critical point.
</details>

<details>
<summary>5. State the circle-counting theorem and say where each of its three pieces comes from.</summary>

For 𝒫 a locally finite circle packing invariant under a geometrically finite Γ with finitely
many Γ-orbits (and no infinite bouquet of tangent circles when δ ≤ 1),
#{C ∈ 𝒫 : rad(C) ≥ t, C ∩ R ≠ ∅} ~ c_𝒫 · ω_Γ(R) · t^{−δ} as t → 0.
The **exponent** δ = dim Λ comes from orbit growth alone. The **measure** ω_Γ is the
Patterson–Sullivan measure reweighted by the stereographic factor (|z|²+1)^δ, and it says the
small circles equidistribute on the fractal. The **constant** is c_𝒫 = sk_Γ(𝒫)/|m^BMS| — the
total skinning mass of the planes over the packing, divided by the total BMS mass. The
exponent is a property of the group; the constant is a property of how the specific planes sit.
</details>

<details>
<summary>6. What is a round Sierpiński carpet, what does it mean about the manifold, and what does the dichotomy say?</summary>

Λ is a round Sierpiński carpet if Ĉ − Λ is infinitely many **round** open discs with
**mutually disjoint closures**. Geometrically, these are exactly the manifolds whose convex
core has compact, **totally geodesic** boundary — each Γ-orbit of a disc is one boundary
component, and roundness is precisely total geodesy. The dichotomy (McMullen–Mohammadi–Oh,
extended with Benoist): for any **separating** circle C — one with limit points inside and
outside — ΓC is either closed or dense in 𝒞_Λ. Non-separating circles have a third,
easily-described behaviour. Equivalently: any geodesic plane meeting the interior of the
convex core is either closed or dense there.
</details>

<details>
<summary>7. What is thick recurrence, and where do the returns come from?</summary>

A compact set 𝓡 ⊂ Γ\G together with κ > 1 such that for every x ∈ 𝓡 and every s > 0 there is
t with **s < |t| < κs** and x·u_t ∈ 𝓡 — a return in every multiplicative window, at every
scale, not merely infinitely often. It replaces Poincaré recurrence, which is unavailable.
The returns come from the fractal: for a Sierpiński carpet limit set, every separating circle
meets Λ in a uniformly perfect Cantor set (no disproportionately large gaps at any scale),
and since the visual image of a horocycle on the boundary is a circle, each point of that
Cantor set contributes a return time. No empty scale in the fractal ⟹ no empty scale in the
return times. The technical input is the positive modulus property of the limit set.
</details>

<details>
<summary>8. Why does the closed-or-dense dichotomy break in higher dimensions, and what replaces it?</summary>

Because there are proper sub-spheres between a circle and the whole boundary sphere. If C ⊂ Σ
for a k-sphere Σ with ΓΣ closed, then ΓC‾ is trapped inside ΓΣ and cannot be dense.
Intermediate closures are genuinely possible. Lee–Oh prove these are the only new cases: for
convex cocompact manifolds with Fuchsian ends and C meeting Λ in more than two points, there
is a sphere S with ΓC‾ = {D ∈ 𝒞_Λ : D ⊂ ΓS}. S = C gives closed, S = the whole sphere gives
dense. The new proof ingredient is an **avoidance theorem** — thick recurrence times that also
stay away from every intermediate closed orbit — plus an induction over intermediate spheres.
</details>

<details>
<summary>9. State cross-ratio rigidity and explain why the hypothesis is much weaker than it looks.</summary>

If f is the boundary map of a discrete faithful representation (with Ω having at least two
components and neither Λ nor f(Λ) contained in a circle) and f sends every quadruple of points
of Λ with **real** cross-ratio to a quadruple with **real** cross-ratio, then f extends to a
Möbius transformation — so the representation is a conjugation. The hypothesis is weak because
(i) f is only defined on Λ, so nothing is asked about whole circles, only about the part of
each circle that Λ sees; and (ii) it asks preservation of the *property* Im = 0, not of the
*value* of the cross-ratio. Preserving values would essentially be the definition of Möbius;
preserving a single-bit, codimension-one property is a genuine hypothesis. The accompanying
dichotomy: either f straightens every circular slice, or the set it straightens has empty
interior in Λ and Patterson–Sullivan measure zero.
</details>

<details>
<summary>10. What is a self-joining, and why does going up in rank help?</summary>

Γ_ρ = {(γ, ρ(γ)) : γ ∈ Γ}, the graph of the representation, a discrete subgroup of
PSL₂(ℂ) × PSL₂(ℂ) acting on ℍ³ × ℍ³. Its limit set is the graph {(ξ, f(ξ))} of the boundary
map. It helps because of one observation: **ρ is algebraic ⟺ Γ_ρ is not Zariski dense in the
product**. So a rigidity question becomes a Zariski-density question, and Zariski density is
the hypothesis under which the ergodic theory of diagonal flows applies. The cost is that the
product has a two-dimensional diagonal subgroup, so there is a flow per direction, the
dynamics depends on the direction, and the single exponent δ is replaced by Quint's concave
growth indicator on a cone.
</details>

<details>
<summary>11. Why does the torus-counting exponent depend on the ordering, and why did this not arise for circles?</summary>

Because in higher rank the growth of the group is direction-dependent. Counting tori by
volume ∏ rad(C_i) gives an exponent δ_{ρ,vol}; counting by ∏ rad(C_i)^{κ_i} gives
limsup (1/t) log #{γ ∈ Γ : Σ κ_i d(ρ_i(γ)o,o) ≤ t}, a different number for different weights.
Each choice of weights picks out a different direction in the limit cone as dominant. This did
not arise for circles because rank one has a one-dimensional cone: there is only one direction,
so only one exponent, and it looks intrinsic. It never was. The honest object is Quint's
concave growth indicator on the cone; any single exponent is one tangent line to it.
</details>

---

## 10. Note on the tutorial process

**Difficulty against reputation: matched, and the split is real.** Sarnak's introduction says
Oh's work "on homogeneous dynamics in the infinite volume setting have shaped the modern
subject", and that is precisely the lecture. No Kontorovich-style inversion. The split I
assigned tracks a real seam in the talk itself: everything before the self-joining
construction lives on one hyperbolic manifold with one flow and one exponent; everything
after lives on a product with a cone of flows and a growth-indicator function. The paper's own
sections 7 versus 8 mirror the same seam exactly.

**How much mathematics survived the captions: none.** Not one formula, not one exponent, not
one constant. This was a slide talk whose written version has 24 figures, and the caption
track carries narration only. Everything displayed above is from arXiv:2510.10771v2. What the
transcript supplied and the paper did not: the snow metaphor, the traveller spending 0% of her
time in compact sets, the sesame-oil-in-soy-sauce photograph, the wild forest, the double
emphasis on preserving the *property* rather than the *value* of the cross-ratio, and the
statement of the cusp gap in §4.10. The two sources are close to complementary.

**Name corrections.** Verified against the paper's text or its 85-entry bibliography unless
marked.

| Caption | Correct | Source |
|---|---|---|
| "If Bou-Rabee" | **Yves Benoist** | paper [3], Benoist–Oh, *ETDS* 42 (2022); see note below |
| "Kurt McMullen" | **Curtis (Curt) T. McMullen** | paper [50]–[53] |
| "Minji Li" / "Minju" | **Minju Lee** | paper [43], [19], [20] |
| "Semyon" | **Samuel (Sam) Edwards** | paper [20], Edwards–Lee–Oh; moderate confidence |
| "Dong Yeol Kim" | **Dongryul M. Kim** | paper [34], [35], [36] |
| "Young-Chan Zeng" | **Yongquan Zhang** | paper [84], [85] |
| "Burger-Rubel measure" | **Burger–Roblin measure** | paper §7.3, [7], [69] |
| "alpha's first theory" | **Ahlfors–Bers theorem** | paper §3.2 |
| "Mostow's Prasad" | **Mostow–Prasad** | paper Thm 5.1, [55], [65] |
| "Klein Young group" (throughout) | **Kleinian group** | paper §2.2 |
| "Nearoski"-style garbles absent here — but "Hong Wang's notation" | **Hong Wang's lecture** (reconstructed) | not in paper |

**On "If Bou-Rabee".** This is the one correction I want to justify, because it is not a
spelling fix. Oh says the round-Sierpiński-carpet dichotomy was "first proved in joint work
with Curt McMullen and Amir Mohammadi in the case when there's no cusp, and in this generality
in joint work with If Bou-Rabee." The paper's Theorem 3.1 carries exactly that two-stage
attribution: [52] = McMullen–Mohammadi–Oh (convex cocompact), [3] = **Benoist**–Oh (extended
to all geometrically finite). No "Bou-Rabee" appears anywhere in the bibliography, and a web
search for any Bou-Rabee/Oh collaboration on Kleinian orbit closures returns nothing. The
talk postdates the paper's v2 by four months, so a brand-new collaborator was possible in
principle; I checked and found none. The correction is by content match, and I have flagged
it here rather than making it silently.

**Substantive caption errors corrected in the text, not just spellings.** Three, and all three
change meaning:

- **"This was the Cannon Conjecture, which is now a theorem"** — said of the statement that
  every finitely generated Kleinian group can be approximated by geometrically finite ones.
  That statement is the **Bers–Sullivan–Thurston density conjecture** (theorem: Namazi–Souto,
  Ohshika, building on many others), which is what the paper names. The Cannon conjecture is a
  different statement, about hyperbolic groups with 2-sphere boundary. Corrected in §3.4.
- **"its parabolic measure is zero"** — of the set of circular slices a non-Möbius boundary map
  straightens. The paper's Theorem 5.7 says ν(Λ_f) = 0 with ν the **Patterson–Sullivan**
  (geometric) measure, and §5.1 says the set has zero δ-dimensional Hausdorff measure.
  "Parabolic" is a live technical word in this subject (parabolic elements, parabolic fixed
  points), so this one is actively misleading. Corrected in §4.7.
- **"round Sierpiński gasket"** — used several times where the defined object is a round
  Sierpiński **carpet**. The gasket is a different fractal, and "Apollonian gasket" is used
  correctly elsewhere in the same talk, so the two coexist in the transcript. Corrected
  throughout.

**Six places where the talk and paper differ, all resolved in favour of the paper.**

| | Talk | Paper | Where |
|---|---|---|---|
| Bouquet hypothesis | assumed always | assumed only when δ ≤ 1 | §4.1 |
| Circles counted in a region | "contained in R" | "C ∩ R ≠ ∅" | §4.1 |
| The counting measure | "Patterson–Sullivan measure" | ω_Γ = (\|z\|²+1)^δ · ν_o | §4.1 |
| Geometrically finite | core has finite volume | **unit neighbourhood** of core has finite volume | §3.4 |
| Higher-dim orbit closures | C meets Λ in "at least two points" | "**more than** two points" | §4.6 |
| Torus size | "area" | "volume", vol(T) = ∏ rad(C_i) | §4.9 |

None is a slip by the speaker in a way that damages the talk; four of the six are the ordinary
compression of a hypothesis for a live audience. The δ ≤ 1 one is worth knowing because it
means the Apollonian case (δ_A ≈ 1.3057 > 1) never needs the hypothesis at all.

**Reconstructed, and what would verify each.**

- **The Poincaré series Σ_γ e^{−s d(o,γo)} as a partition function** (§2.3). Neither source
  writes the series. The paper gives δ as a limsup of log-counts and Quint's ψ_ρ as an
  abscissa of convergence of an explicit series, which is the same object; the identification
  of the series with a partition function and of ν_o with a Gibbs state is my framing.
  Standard in the thermodynamic-formalism literature. Verify against any account of
  Patterson's original construction, where ν_o is built as a weak limit of orbit sums
  normalized by the series as s ↓ δ.
- **Exercise 6.1(a) and (d)** — the Descartes recursion d′ = 2(a+b+c) − d and the identification
  of the four reflections with the Apollonian group. My computation. The paper names the
  Descartes circle theorem (fn. 4) and the Descartes quadratic form (Cor. 7.8) but writes
  neither. Verify (d) by checking Q is invariant under the substitution directly.
- **Exercise 6.2** — the heuristic rad(gC₀) ≈ e^{−d(o,gC₀†)} and the exponent derivation. Mine;
  Oh gestures at it in one sentence. Verify against Oh–Shah, Invent. Math. 187 (2012).
- **Exercise 6.3** — the inscribed-angle proof. Standard; the paper states the fact without
  proof.
- **The comparison table in §2.3** mapping statistical mechanics onto this subject. The
  right-hand column is all sourced; the left-hand column is my labelling.
- **"Hong Wang's notation"** (transcript) is almost certainly "Hong Wang's **lecture**" — Oh
  says "we already heard about the terminology Hausdorff dimension from Hong Wang's
  notation", which reads as a reference to an earlier ICM 2026 talk. Not load-bearing; I did
  not use it.

**Could not verify.**

- **"Semyon"** for the torus-counting collaborator. The paper's [20] is Edwards–Lee–Oh, so the
  person is **Samuel Edwards**, and the surname Lee in the same sentence matches. But "Semyon"
  is not a plausible caption garble of "Sam Edwards" the way the other corrections are, and I
  have no independent confirmation of what she said. Listed at moderate confidence.
- **"Laurie Sullivan"**, credited with the sesame-oil-in-soy-sauce photograph and described as
  "Sullivan's eldest daughter". Not in the paper, not findable. I kept the anecdote (it is
  charming and it is hers) and have not asserted the name in the body.
- **The exact form of the Apollonian orbit-closure conjecture as spoken.** She says "for any
  separating circle for the Apollonian gasket, the orbit is either closed or dense"; the
  paper's Conjecture 3.6 says closed or dense **in 𝒞_Λ**. I used the paper's ambient space.

**Gaps marked in place, with impact ratings.**

1. **The avoidance theorem and inductive scheme** (§4.6). **Impact: low.** Both sources give
   one paragraph of motivation and no internals. The consequence is fully stated; nothing else
   in the talk depends on the mechanism.
2. **The Lie theory of higher rank** — Weyl chambers, Cartan projection, limit cone, growth
   indicator, Anosov subgroups (§4.8). **Impact: moderate.** I state the results and name the
   objects and decline to teach them. It costs the reader §§8.1–8.5 of the paper. It costs
   nothing in the four questions, because every statement of the four questions is expressible
   without them. This is the AGCat decision from the Gaitsgory tutorial applied again: faking
   depth here would produce exactly the smooth fabrication that is worse than an acknowledged
   hole.
3. **Paper sections 7 and 8 generally** — exponential mixing, Dolgopyat's method, Markov
   sections, uniform exponential mixing over congruence covers, the affine sieve, temperedness
   of L²(Γ\G). **Impact: low for this talk, structural for the subject.** The talk mentions
   local mixing in four sentences and never gets to any of the rest. I compressed §§7–8 to
   the local-mixing statement, the cusp gap, and one paper-only paragraph (§4.11) on the
   drunken-bird dichotomy, which is Pólya recurrence and worth the space. A reader who wants
   the affine sieve — including the theorem that an integral Apollonian packing has
   ≪ T^{δ_A}/log T circles of prime curvature ≤ T — should go to paper §7.5.

**Where the paper is stronger than the talk.** Two places. First, the counting constant: the
talk says only "this geometric invariant becomes the skinning constant"; the paper gives
c_𝒫 = sk_Γ(𝒫)/|m^BMS| outright, and that formula is the single most illuminating line in
either source. Second, the thick-recurrence statement: the talk describes it qualitatively,
the paper gives the quantifiers (s < |t| < κs, all s > 0), and the quantifiers are the content.
Both are quoted above with the paper as source.

**On the paper's version and date.** The arXiv listing shows v1 submitted 12 October 2025 and
v2 on 13 April 2026; the HTML title block shows no misleading `\today` artefact in this case,
but the version stamp reads `arXiv:2510.10771v2 [math.DS] 13 Apr 2026` and that is the version
I read and cite. I found no invalid identifiers or broken references in the bibliography.

**One process note on infrastructure, not mathematics.** My first download of the paper's HTML
was silently overwritten by a concurrent agent writing a different paper to the same filename
in the shared scratchpad directory, and a first pass of my text extraction also swallowed
every formula containing a `<` character — which is exactly the formulas stating constants and
hypotheses (`0 < c_𝒫 < ∞`, `δ ≤ 1`). Both were caught before anything was written. Both are
worth naming, because a silent truncation at a `<` would have removed precisely the constants
this tutorial is built around.
