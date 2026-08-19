---
title: "Uniformization theorems and related results in higher dimensional complex geometry"
speaker: Ngaiming Mok (University of Hong Kong)
source: https://www.youtube.com/watch?v=TYOQ2l6m4gM
video_id: TYOQ2l6m4gM
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: "none — companions: https://hkumath.hku.hk/~nmok/ICCM2007.pdf and http://hkumath.hku.hk/~imr/IMRPreprintSeries/2015/IMR2015-9.pdf"
transcript: ../transcripts/TYOQ2l6m4gM_transcript.txt
difficulty_for_you: 4/5
reading_time: ~90 min
---

# Uniformization theorems and related results in higher dimensional complex geometry — Ngaiming Mok

**Field:** complex differential geometry, several complex variables, and algebraic geometry,
braided together. Bounded symmetric domains, their quotients, and uniruled projective
manifolds.

**Difficulty against your background: 4 out of 5, and not split.** This is one theme in four
movements, not two half-talks, so a single number is honest. The reason it is a 4 rather
than a 3 is that the unfamiliar layers stack: you need bounded symmetric domains (several
complex variables), their arithmetic quotients (Lie theory and lattices), curvature of
Hermitian *bundles* rather than of Riemannian manifolds, and then a second, entirely
separate machine — varieties of minimal rational tangents — that lives in algebraic
geometry. Each layer alone would be a 3. The talk uses all four and assumes all four.

What makes it crossable is that the *shape* of every argument is one you own. Mok integrates
a nonnegative quantity over a bundle and concludes it vanishes pointwise — that is the
Bochner method, and you have done it. He propagates a local structure along a distinguished
family of curves to reach a bad set — that is analytic continuation with a codimension
count. He uses an ergodic theorem to promote "one instance exists" into "everything". None
of the moves are foreign. Only the objects are.

**Prerequisites this tutorial builds:** what a bounded symmetric domain is and why the unit
disc is the rank-one case; rank, and why rank ≥ 2 is the entire source of rigidity;
holomorphic bisectional curvature and Griffiths seminegativity; the Carathéodory metric and
why it is Finsler rather than Hermitian; lattices and finite-volume quotients; uniruled
manifolds, minimal rational curves and the variety of minimal rational tangents (VMRT);
Moore's ergodicity theorem in the one form the talk uses it.

**A note on sources — read this before anything else.**

There is **no ICM proceedings paper**. Mok's entire arXiv listing is twelve papers, the most
recent posted 29 January 2024, and none of them is a write-up of this lecture. He does not
name a survey from the podium either — I scanned the transcript for "my survey", "our
review", journal names and book titles, and he cites only theorems, never a place to read
them.

So I used **two companions, and neither is the proceedings paper**:

- **C1** — Mok, *"Ergodicity, bounded holomorphic functions and geometric structures in
  rigidity results on bounded symmetric domains"*, lecture slides, ICCM Hangzhou,
  17–22 December 2007
  ([PDF](https://hkumath.hku.hk/~nmok/ICCM2007.pdf); published version in *Proceedings of
  the ICCM, Hangzhou 2007*, Vol. II, Higher Education Press, Beijing, pp. 464–505). This is
  a 72-slide deck and it covers movements two and four of the talk almost statement for
  statement. It is nineteen years old, which matters: it stops short of the newest results.
- **C2** — Mok, *"Geometric structures and substructures on uniruled projective manifolds"*,
  in *Foliation Theory in Algebraic Geometry* (Simons Symposia), Springer 2016, pp. 103–148
  ([preprint PDF](http://hkumath.hku.hk/~imr/IMRPreprintSeries/2015/IMR2015-9.pdf)). This is
  a proper 36-page survey and it covers movement three and most of movement four.

Everything else in this document that is stated precisely comes from the **primary paper for
that one theorem**, cited inline by name and journal. That is the method the spec calls for
and it worked well here: between C1, C2 and about fifteen primary papers I was able to
restore roughly 80% of the mathematics that the captions destroyed.

**A note on the title.** The lecture's YouTube title is generic — the oEmbed record returns
exactly `"ICM 2026 Plenary Lecture - Ngaiming Mok"` and nothing more. The title in the front
matter above is the one **spoken in the room**: the introducer says Mok "will speak about
uniformization theorems and related results in higher dimensional complex geometry", and Mok
opens with "the title of my talk addresses uniformization theorems". My brief supplied a
different title — *"Starting with the Gauss–Bonnet formula: rigidity phenomena on bounded
symmetric domains"*. **That title has no support anywhere in this recording.** The
Gauss–Bonnet formula is never mentioned, not once, in ninety minutes. See §10.

---

## 1. What is at stake

In one complex dimension there is a complete answer to a very ambitious question, and you
already know it.

Take any Riemann surface — any one-complex-dimensional complex manifold, connected, however
exotic. Pass to its universal cover. The **uniformization theorem** says that the universal
cover is one of exactly three things: the Riemann sphere, the complex plane, or the unit
disc. Nothing else. Every Riemann surface in existence is a quotient of one of those three
by a group acting freely and properly discontinuously.

That is a shocking amount of control. An arbitrary object, described by almost no data, is
forced into one of three boxes. And the three boxes line up with curvature: positive, zero,
negative. Give the surface its natural metric and the sphere has curvature +1, the plane 0,
the disc −1. So a **topological** classification and a **curvature** classification agree
exactly. Mok says this in his first minute: "in the case of one dimension there are two main
themes, one is topology, the other is geometry, especially curvature."

Now ask for the same thing in complex dimension two, three, *n*. It fails immediately and
completely. There is no list of three model spaces. There is not even a list. Universal
covers of compact complex manifolds are wild — for a long time it was not known whether they
are even Stein in reasonable cases.

**The entire talk is about what survives.** Mok's answer, developed over about forty years,
is that you give up on classifying everything and instead do four narrower things:

1. **Characterize the model spaces by curvature.** If a compact Kähler manifold has
   nonnegative holomorphic bisectional curvature, what is it? (Answer: essentially forced.)
2. **Prove that quotients of the negatively curved models cannot be deformed.** If a
   manifold merely has the *fundamental group* of a quotient of a bounded symmetric domain,
   is it that quotient? (Answer: yes, under hypotheses, and the proof runs on bounded
   holomorphic functions and an ergodic theorem.)
3. **Characterize the models by an algebro-geometric invariant instead of curvature** — the
   variety of minimal rational tangents. This works where curvature is unavailable.
4. **Do all of the above for subspaces**, not just for whole manifolds.

Those are the four sections of the lecture, and he colour-codes them on his slides: "light
green is what is the emphasis of this talk, and yellow indicates where the questions arise."

The word that runs through all four is **rigidity**. Rigidity means: a weak hypothesis
forces a strong conclusion, so the object cannot be deformed. You know the shape from
physics — a symmetry assumption that leaves exactly one solution, or a conserved quantity
that pins down a trajectory you thought had a family. Here the hypotheses are astonishingly
weak (a fundamental group; a curvature sign; the tangent directions to one family of
curves at one point) and the conclusions are astonishingly strong (the manifold is *this*
manifold, biholomorphically).

---

## 2. Your anchor

### 2.1 The anchor is the uniformization theorem itself

You do not need an analogy for this talk. You need the one-variable theorem you already own,
held up as a template, with each of its parts asked about separately.

| One variable, which you have | The talk's higher-dimensional replacement |
|---|---|
| Sphere ℙ¹ — positive curvature | ℙⁿ and the compact Hermitian symmetric spaces (§4.1) |
| Plane ℂ — flat | flat factors ℂᵏ, which survive in Mok's structure theorem |
| Disc Δ — negative curvature | **bounded symmetric domains** Ω, of which Δ is the rank-one case (§3.1) |
| Quotient Δ/Γ by a Fuchsian group | Ω/Γ for Γ a lattice — the objects of §4.2 |
| "Which surface is it?" answered by genus | answered by curvature, by π₁, or by the VMRT |

The disc with the Poincaré metric is the base case you can hold onto concretely, and the
talk supports that reading: every bounded symmetric domain contains totally geodesic
polydiscs Δ^r, and its **rank** is r, the largest such. Rank one means the disc (or its
higher-dimensional cousin the ball). Rank ≥ 2 means there is genuinely more than one
independent disc direction, and that turns out to be where all the rigidity comes from.

### 2.2 The anchor Mok hands you from the podium

The best anchor in a talk is one the speaker gives you, and Mok gives a very good one for
the hardest machinery in the lecture — the VMRT theory of §4.3. He says:

> "An important principle is that I want to think about the minimal rational curves as some
> kind of special geodesics. **They are carriers of information.** So the idea is to carry
> the information at a general point to a bad point, and thereby you can start with local
> properties, propagate properties across the manifold, in order to prove rigidity theorems."

And near the end he puts the whole dictionary on a slide:

> "So there's parallelism. You have the uniruled projective manifold as [the] Riemannian
> manifold here. Here you look at the 𝒞(X), the VMRTs, [as the] analogue of the sphere
> bundle. And here you look at minimal rational curves as [the] analogue of geodesic curves,
> but only in certain directions you have them. And you look at the [tautological] foliation
> as a kind of geodesic flow, heuristically. And then the sub[-VMRT] structure is the
> Riemannian submanifolds. The analogues [of] totally geodesic subsets are more ample here.
> These are the projective uniruled subvarieties."

| Riemannian geometry (yours) | VMRT geometry (his) |
|---|---|
| Riemannian manifold | uniruled projective manifold (X, 𝒦) |
| unit sphere bundle | the VMRT structure 𝒞(X) ⊂ ℙT(X) |
| geodesics | minimal rational curves — but only in *some* directions |
| geodesic flow | the tautological foliation on 𝒞(X) |
| Riemannian submanifold | sub-VMRT structure 𝒞(S) ⊂ ℙT(S) |
| totally geodesic submanifold | uniruled projective subvariety |

That table is the single most useful thing in the lecture for someone with your background,
and it is his, not mine. Hold it. Every theorem in §4.3 and §4.4 is a theorem about that
dictionary.

The one place the dictionary genuinely breaks — and he flags it — is that in Riemannian
geometry there is a geodesic in *every* direction, whereas here the minimal rational curves
exist only in the directions that lie in the VMRT. The VMRT is a proper subvariety of the
projectivized tangent space, and its shape is the whole invariant.

### 2.3 A word on a formula that is not here

Gauss–Bonnet — curvature integrated over a surface equalling a topological invariant — is
the natural anchor you would reach for if someone told you this talk was about "curvature
forcing topology". It is a perfectly good anchor for a different lecture. **It is not in
this one.** Mok never says the words. The closest the captions come is the phrase "one wants
a Gauss formula" in the proof sketch of Hermitian metric rigidity, and that is the *Gauss
equation* relating curvature of a submanifold to curvature of the ambient space — a
different classical result with the same surname on it.

What Mok does use, repeatedly, is an integral identity over a bundle whose integrand has a
sign, forcing pointwise vanishing (§4.2.3). That is a **Bochner** argument, not a
Gauss–Bonnet argument. The difference matters: Gauss–Bonnet computes a number; Bochner
proves a vanishing theorem. Mok wants vanishing theorems.

I am naming this only so you know the formula exists and know it is absent. Decorating the
talk with it would be inventing content.

---

## 3. The bridge

Seven ideas. Each is defined by deforming something you already have, and each gets a small
concrete example. Everything else in the talk gets one sentence at the point of use.

### 3.1 Bounded symmetric domains: the disc, promoted

Start with what you know. The unit disc Δ ⊂ ℂ carries the Poincaré metric, and its
automorphism group (Möbius transformations preserving Δ) acts transitively: any point can be
moved to any other. More than that, at every point there is a holomorphic involution fixing
that point and reversing directions — for the origin it is z ↦ −z. A domain with that
property is called **symmetric**.

A **bounded symmetric domain** is a bounded domain Ω ⊂ ℂⁿ, biholomorphic to a bounded
domain, such that every point has such a holomorphic symmetry. That is the complex analogue
of a Riemannian symmetric space of noncompact type — the same definition with "holomorphic"
inserted.

Élie Cartan classified them. There are four infinite classical series plus two exceptional
ones. The three easiest to hold are matrix domains — this is the concrete version, and you
should carry it:

- **Type I**: Ω = { Z ∈ M(p, q; ℂ) : I_q − Z̄ᵗZ > 0 }, i.e. all p×q complex matrices of
  operator norm < 1. Taking p = q = 1 gives exactly the unit disc. Taking q = 1 gives the
  unit ball in ℂᵖ.
- **Type II**: the same, restricted to antisymmetric matrices.
- **Type III**: the same, restricted to symmetric matrices. Its unbounded realization, via a
  Cayley transform, is the **Siegel upper half-plane**
  ℍ_n = { τ ∈ M(n,n;ℂ) : τᵗ = τ, Im τ > 0 }, which parametrizes polarized abelian varieties.
  Mok flags this in the last section of the talk and it is why type III matters.
- **Type IV**: the "Lie ball", a quadric-type domain, always of rank 2.
- Two exceptional domains, of complex dimensions **16 and 27**, attached to E₆ and E₇.

Every bounded symmetric domain has a canonical realization as a *convex* bounded domain,
the **Harish-Chandra realization**; for the classical types these are Cartan's matrix
realizations above. (Mok and I-Hsun Tsai proved in *J. reine angew. Math.* **431** (1992),
91–122 that for rank ≥ 2 this convex realization is unique up to an affine transformation —
a rigidity result about the *picture* itself.)

### 3.2 Rank, and why it is the whole story

**Rank** is the one number that governs everything in movements two and four.

Definition, in the form you want: Ω contains totally geodesic **polydiscs** Δ^r — products of
r copies of the unit disc, embedded so that the ambient metric restricts to the product of
Poincaré metrics. The **rank** r of Ω is the largest such. The **Polydisc Theorem** says
more: fixing a maximal polydisc P ⊂ Ω and the isotropy group K at a base point,
⋃_{k ∈ K} kP = Ω. Every point of Ω lies on some maximal polydisc. (C1, slide 4.)

For type I with p×q matrices, rank = min(p, q). So the disc, the ball, and type IV in one
sense are the low-rank cases; big square matrix domains have big rank.

**Why rank ≥ 2 creates rigidity.** Here is the mechanism in one sentence, and it is worth
slowing down for. In the polydisc Δ × Δ with the product metric, consider the holomorphic
bisectional curvature between a direction along the first factor and a direction along the
second. For a *product* metric that curvature is **zero** — curvature does not mix factors.
So as soon as r ≥ 2, the curvature tensor of Ω has genuine null directions. Those null
directions form a distinguished subbundle, and *integrating over exactly that subbundle* is
what makes the rigidity proofs work. Rank one — the disc and the ball — has no such null
directions, and correspondingly **all the rigidity theorems in this talk are false for the
ball.** Mok states the rank ≥ 2 hypothesis in every single theorem of movements two and four.

You will see this in §4.2.3: the integral is not over the whole projectivized tangent
bundle, it is over a sub-bundle picked out by the zeros of the bisectional curvature, and
one of the technical points Mok mentions explicitly is checking that the null vectors are
tangent to that sub-bundle.

A **characteristic vector** at x ∈ Ω is a tangent vector tangent to a *minimal disc* — a
totally geodesic disc of the smallest kind, corresponding to a single factor of a maximal
polydisc. The **minimal characteristic bundle** 𝒮 ⊂ ℙT(X) is the set of all characteristic
directions. (C1, slide 4.) This is the bundle everything is integrated over. Keep the name.

### 3.3 Lattices and quotients: the objects that are actually studied

Ω itself is contractible and boring. The interesting objects are its quotients.

Let G = Aut₀(Ω) be the identity component of the automorphism group — a semisimple real Lie
group. A **lattice** Γ ⊂ G is a discrete subgroup of finite covolume. If Γ is torsion-free it
acts freely and X_Γ := Ω/Γ is a complex manifold. Two cases:

- **cocompact** (Γ\G compact): X_Γ is a compact complex manifold;
- **non-uniform** but finite volume: X_Γ is noncompact but has finite volume in the canonical
  metric. These are the *arithmetic varieties* — the higher-rank cousins of a non-compact
  finite-area hyperbolic Riemann surface.

Γ is **irreducible** if it does not split as a product along a splitting of Ω. Irreducibility
is a hypothesis in almost every theorem below, and it is what lets Moore's ergodicity
theorem (§3.7) bite.

Note π₁(X_Γ) = Γ. So the sentence "a map inducing an isomorphism on fundamental groups" means
"a map inducing an isomorphism of lattices", and that is a purely group-theoretic hypothesis
with no analysis in it at all. The astonishing content of movement two is that this
group-theoretic hypothesis forces a biholomorphism.

### 3.4 Curvature, the complex version

You know sectional curvature: pick a real 2-plane, get a number. In complex geometry the
useful notion is finer.

For a Kähler manifold and two holomorphic tangent directions ξ, η, the **holomorphic
bisectional curvature** is R(ξ, ξ̄, η, η̄). Setting η = ξ recovers the **holomorphic
sectional curvature**, which is the ordinary sectional curvature of the real 2-plane spanned
by ξ and iξ. Bisectional curvature is stronger data than sectional curvature and weaker than
the full curvature tensor. Concretely:

- ℙⁿ with Fubini–Study: bisectional curvature > 0 everywhere.
- Δ, or any bounded symmetric domain, with its canonical metric: bisectional curvature ≤ 0,
  with equality exactly in the directions described in §3.2.
- A product: bisectional curvature between the factors is 0.

For a Hermitian *vector bundle* (E, h) — not just a manifold — the analogous condition is
**seminegativity in the sense of Griffiths**: the curvature form Θ(h) satisfies
Θ(h)(ξ, ξ̄; v, v̄) ≤ 0 for every tangent direction ξ and every section direction v. When
E = T_X this is precisely "all holomorphic bisectional curvatures ≤ 0". Griffiths
seminegativity is the hypothesis in Mok's metric rigidity theorem, and it is deliberately
weaker than requiring the metric to be Kähler.

Finally, each X_Γ carries a **canonical Kähler–Einstein metric** g of negative Ricci
curvature, unique up to scale, descended from Ω. That is the reference metric against which
every other metric is compared.

### 3.5 The Carathéodory metric: a metric built out of bounded functions

This is the most important new object for movement two, and it is completely elementary.
Build it now.

Let M be a complex manifold and let H(M) be the set of holomorphic maps f : M → Δ into the
unit disc. For a tangent vector ξ ∈ T_x(M) define

  ‖ξ‖_κ := sup_{f ∈ H(M)} ‖df(ξ)‖_{Poincaré}.

That is the **Carathéodory pseudometric**. In words: *measure a tangent vector by how fast
the best bounded holomorphic function can move in that direction.* (C1, slide 13.)

Three facts you should verify or accept:

1. On Δ itself, κ *is* the Poincaré metric — this is the Schwarz–Pick lemma, which you know.
2. On a bounded domain in ℂⁿ it is nondegenerate — because coordinate functions, rescaled,
   are bounded holomorphic functions that move in every direction.
3. On the ball Bⁿ it agrees with the Bergman metric up to a constant.

And now the point. On the polydisc Δⁿ, for ξ = (ξ₁,…,ξₙ),

  ‖ξ‖_κ = max_k ‖ξ_k‖_{Poincaré}.

That is a **sup-norm**. It does not come from an inner product. So the Carathéodory metric is
in general a **complex Finsler metric** — a norm on each tangent space, varying
holomorphically, not necessarily Hermitian — and this is why Mok has to prove a Finsler
version of his rigidity theorem, not just a Hermitian one. You will do this computation by
hand in §6.1.

Why bother? Mok gives the reason directly from the podium, and it is a design decision worth
naming:

> "Although the theorem of rigidity of maps and so on is very nice, it is very difficult to
> construct a manifold with that curvature condition… but then there are complex Finsler
> metrics that exist for any bounded domain, and this is the Carathéodory metric, and they
> are constructed from bounded holomorphic functions."

Hermitian metrics of seminegative curvature are rare and hard to produce. Carathéodory
metrics are *automatic* — every bounded domain has one, for free, because every bounded
domain has bounded holomorphic functions. Mok trades a strong hypothesis you cannot verify
for a weak one you get for nothing, and then works harder. Remember this move; it recurs in
§7.1.

One more fact, needed in §4.2.4: for a maximal polydisc P ⊂ Ω, the Carathéodory metric of P
equals the restriction of the Carathéodory metric of Ω. Maximal polydiscs are
Carathéodory-isometrically embedded. (C1, slide 14.)

### 3.6 Rational curves, uniruled manifolds, and the VMRT

Now switch worlds entirely. Movements three and four live in algebraic geometry, and
curvature is not available there. This subsection builds the replacement.

A **rational curve** on a projective manifold X is a nonconstant holomorphic map
f : ℙ¹ → X, taken up to reparametrization. X is **uniruled** if it is covered by them —
Mok's phrase is that X "is filled up by Riemann spheres". Uniruledness is the algebraic
analogue of "positively curved": rational curves exist as soon as the canonical bundle fails
to be nef (Mori 1979), and any Fano manifold is uniruled (Miyaoka–Mori, *Ann. Math.* **124**
(1986), 65–69). In the Kodaira
classification uniruledness is what κ(X) = −∞ means (proved for surfaces classically,
for threefolds, and **still open from dimension four onward** — Mok says so explicitly).

A rational curve is **free** if f*T_X is semipositive, i.e. a direct sum of line bundles of
degree ≥ 0. Freeness is exactly the condition that guarantees the curve can be deformed to
move in every direction, so that deformation theory works. X is uniruled if and only if it
carries a free rational curve.

Now minimize. Fix a polarization, take free rational curves of the smallest possible degree —
Mok's image is that you deform a rational curve "until it cannot break up anymore" — and
collect them into a **minimal rational component** 𝒦, an irreducible component of the Chow
space. This gives a **double fibration**

  𝒦 ←^π 𝒰 →^μ X,

where 𝒰 is the universal family (fibres of π are the curves) and μ is evaluation. For a
general point x ∈ X, the fibre 𝒰_x parametrizes minimal rational curves through x with a
marking at x.

**The tangent map** τ_x : 𝒰_x → ℙT_x(X) sends a curve to its tangent direction at x:
τ([C]) = [T_x(C)]. Its image (strict transform) is

  **𝒞_x(X) ⊂ ℙT_x(X) — the variety of minimal rational tangents (VMRT) at x.**

In the dictionary of §2.2, 𝒞_x(X) is the unit sphere at x. But unlike a sphere it is a
proper, and usually small, subvariety, and *its projective geometry is the invariant that
carries all the information.*

Two theorems make the definition usable:

- **(Kebekus, J. Algebraic Geom. 11 (2002), 245–256.)** At a general point x, the tangent map
  τ_x is a morphism — i.e. every minimal rational curve through a general point is free and
  immersed there. Mok says this in the talk and dates it correctly to 2002.
- **(Hwang–Mok, Asian J. Math. 8 (2004), 51–63.)** At a general point, τ_x : 𝒰_x → 𝒞_x(X) is
  a *birational* morphism, in fact generically finite. Mok remarks from the podium that he
  and Hwang initially expected it to be an isomorphism, that counterexamples were later
  found, but that for the spaces they cared about (hypersurfaces, and the model spaces) it
  is one.

**The bad set.** For a general uniruled X there is a subvariety B ⊂ X — the (enhanced) bad
locus — over which minimal rational curves fail to be free, deformation theory fails, and
none of the above holds. Mok is emphatic that dealing with the bad set is "usually the
difficulty of a problem", and the codimension of the bad set is the running quantity in §4.3.

**The VMRT table** you actually need — the compact Hermitian symmetric spaces and their
VMRTs, all classical (C1, slide 53):

| S (compact Hermitian symmetric space) | VMRT 𝒞_x(S) | embedded by |
|---|---|---|
| Grassmannian G(p,q) | ℙ^{p−1} × ℙ^{q−1} | **Segre** |
| orthogonal Grassmannian G^{II}(n,n) | G(2, n−2) | **Plücker** |
| Lagrangian Grassmannian G^{III}(n,n) | ℙ^{n−1} | **Veronese** |
| hyperquadric Qⁿ | Q^{n−2} | by 𝒪(1) |
| exceptional (E₆, dim 16) | G^{II}(5,5) | by 𝒪(1) |
| exceptional (E₇, dim 27) | (E₆ case) | **Severi** |

Mok notes on the podium that all of these VMRTs are themselves Hermitian symmetric of rank
≤ 2, and all are irreducible except the Grassmannian's — a small observation that turns out
to control which inductions are available.

**Picard number one.** The last piece of vocabulary. The Picard number is the rank of the
group of divisors modulo numerical equivalence; ρ(X) = 1 means there is essentially one
divisor class, so *no fibration structure to exploit*. Mori theory works by producing
extremal rays and contractions; when ρ = 1 there is nothing to contract. Mok's opening
motivation for the whole VMRT theory is exactly this: "especially in the case where you have
Picard number one, there was at that point no other way to study the geometry of uniruled
projective manifolds of Picard number one."

### 3.7 Ergodicity, in the one form the talk uses

The engine of movement two is an ergodic theorem, and you need only its statement.

**Moore's ergodicity theorem.** Let G be a semisimple real Lie group, Γ ⊂ G an irreducible
lattice, and H ⊂ G a closed **noncompact** subgroup. Then Γ acts ergodically on G/H —
every Γ-invariant measurable subset has measure zero or full measure. (C1, slide 8.)

The corollary used in practice: **for almost every point gH ∈ G/H, the orbit Γ·gH is dense
in G/H.** There is a null set E off which density holds. (C1, slide 8, "Lemma".)

That "almost every" is not a technicality; it is the source of the talk's hardest technical
work. A specific maximal polydisc may lie in the bad null set, in which case the density
argument fails there and Mok must recover it by a limiting argument with uniform constants.
He says so: "there may in fact be a maximal polydisc P such that its orbit under Γ gives a
discrete set of maximal polydiscs" (C1, slide 37).

For the anchor: this is the same logical shape as an ergodic-hypothesis argument in
statistical mechanics. A single trajectory, run long enough, visits everything; therefore a
quantity constant along the trajectory is constant everywhere. Mok's version: a bounded
holomorphic function invariant under a flow, plus density of a lattice orbit, is constant on
a whole homogeneous space.

---

## 4. The talk, rebuilt

Mok's own division: "I will divide the talk into four sections." I follow it exactly.

### 4.1 Movement one — positive curvature, and the generalized Frankel conjecture

He opens with old work of his own, and says why: it is the piece that shows his method.

**The setting.** In one variable, positive curvature meant the sphere. In several variables
the question is: which compact Kähler manifolds have positive holomorphic bisectional
curvature? The expected answer — that they are all ℙⁿ — is the **Frankel conjecture**.

Two solutions arrived within a year of each other, from opposite directions:

- **Mori** (*Ann. of Math.* **110** (1979), 593–606) proved the **Hartshorne conjecture**: a
  projective manifold with **ample tangent bundle** is biholomorphic to ℙⁿ. This is
  algebro-geometric, and it is the paper that introduced bend-and-break and rational curves in
  characteristic p — the technique that founds all of §4.3.
- **Siu and Yau** (1980) proved the Frankel conjecture itself, by **analytic** methods, using
  stable harmonic maps. Mok's phrasing: "this was established in the positive by Siu–Yau by
  methods of analytic methods involving especially stable harmonic maps."

**The generalized Frankel conjecture** relaxes the hypothesis from positive to
**semipositive** (nonnegative) holomorphic bisectional curvature. That is a much harder
problem, because now degenerate cases are allowed in and the answer is a structure theorem
rather than a single space: flat factors, compact Hermitian symmetric spaces, and
ℙⁿ-like factors can all occur. Mok solved it completely:

> **Mok, "The uniformization theorem for compact Kähler manifolds of nonnegative holomorphic
> bisectional curvature", *J. Differential Geom.* 27 (1988), 179–214.**

> *[Gap: Mok does not read the statement of his own theorem aloud, and it was on the slide.
> The precise structure theorem — the exact list of factors of the universal cover and the
> normalization conventions — is not recoverable from the captions and is not restated in
> either companion. Impact: **low**. The shape (semipositive bisectional curvature forces a
> product decomposition into flat, Hermitian symmetric, and positively curved pieces) is what
> the rest of the talk uses, and that is stated. Read the 1988 paper for the statement.]*

**What matters here is the method, and he says so.** Three ingredients, from three different
subjects:

1. **Kähler–Ricci flow.** He proves that semipositivity of holomorphic bisectional curvature
   is *preserved under the flow* — a maximum-principle statement about a nonlinear parabolic
   PDE, and exactly the kind of thing you have done. Running the flow improves the geometry
   without leaving the class.
2. **Deformation of rational curves.** Once a rational curve exists you deform it "until it
   cannot break up anymore", producing minimal rational curves. This is Mori's machine, used
   inside a differential-geometric proof, and it is the seed of everything in §4.3.
3. **Berger's holonomy theorem** in Riemannian geometry, to finish. *(This attribution is a
   caption reconstruction — see §10.)*

Then the methodological remark, which is the most quotable line in the lecture:

> "It illustrated my approach to solving such problems. I'm — this is **problem-based**. Once
> a problem is formulated, even though it's a problem in Kähler geometry, I make use of a
> collection of methods ranging from nonlinear PDE, algebraic geometry, [several complex
> variables], and then Riemannian geometry."

He returns to this in his overview slide, listing the fields that enter his work over forty
years: nonlinear PDE, algebraic geometry and Riemannian geometry at the start; several
complex variables, harmonic analysis and ergodic theory in the recent work. That trajectory —
same problems, steadily more distant tools — is the shape of the whole talk.

### 4.2 Movement two — negative curvature, and rigidity from the fundamental group alone

This is the emphasis of the lecture (his light-green colour) and where the newest results
are. He states the destination first, then spends thirty minutes building up to it.

#### 4.2.1 The destination

> **Isomorphism Theorem (recent; Mok, and Mok with Kwok-Kin Wong).** Let Ω be a bounded
> symmetric domain of rank ≥ 2, Γ ⊂ Aut(Ω) an irreducible torsion-free lattice, and
> X_Γ = Ω/Γ. Let the target be a quotient D/Γ′ of a bounded domain D. If a holomorphic map
> f : X_Γ → D/Γ′ **induces an isomorphism on fundamental groups**, then f is a
> biholomorphism.

Mok emphasises the point: "the important thing is that only [the] fundamental group is
concerning the hypothesis". A purely group-theoretic input; a complex-analytic conclusion.
He immediately adds that this cannot be true in general — one needs *something* about the
target — and says what he assumes instead of higher homotopy: "I impose conditions of the
existence of bounded holomorphic functions, essentially on the [universal cover] of the
target manifold."

The precise statement I can restore is the 2007 version from C1 (slide 46), which needs
extra hypotheses that the 2026 version apparently removes:

> **Isomorphism Theorem (C1, slide 46).** Ω ⊂ ℂⁿ a bounded symmetric domain of rank ≥ 2,
> X = Ω/Γ. Let M be a Stein manifold, D ⋐ M, Γ′ a torsion-free discrete group of
> automorphisms of D, N := D/Γ′, and μ the Kobayashi–Royden measure. Suppose μ(N) < ∞ and
> f_* : Γ ≅ Γ′. Then f : X → N is biholomorphic.

> *[Gap: the exact hypotheses of the 2026 version. The talk describes the target as
> "quasi-projective" and later says the theorem "is actually stated in general for D" an
> arbitrary bounded domain, but the captions do not give the full statement, and the relevant
> paper — Mok–Wong, "Extension of inverses of Γ-equivariant holomorphic embeddings of bounded
> symmetric domains of rank ≥ 2 and applications to rigidity problems", *Algebraic Geometry
> and Physics* **2** (2025), 197–269 — is not on arXiv and I could not obtain it. Impact:
> **moderate.** The whole point of the new work is that the hypotheses got weaker, and I
> cannot tell you by how much.]*

#### 4.2.2 The prehistory: Siu's strong rigidity, and the two differences

Before his own result Mok recalls the founding theorem of the subject:

**Siu (1980).** Let X_Γ = Ω/Γ be a **compact** quotient of an *irreducible* bounded
symmetric domain, of any rank, of complex dimension ≥ 2. Let Y be a compact Kähler manifold
homotopy-equivalent to X_Γ. Then Y is biholomorphic or anti-biholomorphic to X_Γ.

The method is the one you would guess from Riemannian geometry: take the homotopy
equivalence, smooth it, run the **heat flow** to get a harmonic map, then prove — via a
∂∂̄-Kodaira-type Bochner identity, under a rank condition — that the harmonic map is
holomorphic or anti-holomorphic. Mok's phrasing: "one starts with a [homotopy equivalence],
slightly modifies it to give a smooth map, and deforms it using the heat flow, and in the
final analysis you get a harmonic map, which Siu proved to verify some very interesting
∂∂̄-Kodaira formula."

Mok then names the two differences between Siu's theorem and his own, and both are worth
holding:

1. **Direction.** Siu maps *Y → X_Γ*, from the unknown manifold into the model. Mok maps
   *X_Γ → Y*, out of the model into the unknown. The second is harder: you have no
   structure at the target to pull back.
2. **Compactness.** Siu is restricted to the compact case. Mok works in the finite-volume
   case, which includes non-compact arithmetic quotients.

#### 4.2.3 Hermitian metric rigidity, and the integral identity

Now the theorem the whole machine is built on, and the one place a Bochner-type argument is
visible.

> **Hermitian Metric Rigidity (Mok 1987; hypothesis weakened by To 1989).** Let Ω be an
> **irreducible** bounded symmetric domain of **rank ≥ 2**, Γ ⊂ Aut(Ω) a torsion-free
> lattice, X = Ω/Γ, and g the canonical Kähler–Einstein metric. Let h be *any* Hermitian
> metric on X whose curvature Θ(h) is **seminegative in the sense of Griffiths**. Then
> h ≡ c·g for a constant c > 0.

Primary source: **Mok, "Uniqueness theorems of Hermitian metrics of seminegative curvature on
locally symmetric spaces of negative Ricci curvature", *Ann. of Math.* 125 (1987),
105–152**, and the book-length treatment **Mok, *Metric Rigidity Theorems on Hermitian
Locally Symmetric Manifolds*, Series in Pure Mathematics 6, World Scientific, 1989** — the
monograph. Mok's original theorem assumed in addition that h is **dominated by** the
canonical metric; he says from the podium that "this condition of domination was removed by
To in 1989", and C1 records the attribution as "Mok 87, To 89".

Read what this says. A Hermitian metric is an enormous amount of freedom — a positive-definite
Hermitian form at every point, varying smoothly. The only constraint imposed is a **sign on
its curvature**. And that sign collapses the entire infinite-dimensional space of choices to
a single one-parameter family. That is rigidity in its purest form, and it is false for the
disc: on a hyperbolic Riemann surface there are many metrics of nonpositive curvature. Rank
≥ 2 is doing all the work.

**The immediate corollary, which is what gets used:**

> If (N, h) is any Hermitian manifold of nonpositive curvature in the sense of Griffiths, and
> f : X → N is a nonconstant holomorphic map, then f is an **immersion**; and if (N, h) is
> Kähler, f is **totally geodesic**. In particular, if N = Ω/Γ′ is itself Hermitian locally
> symmetric, then f lifts to a totally geodesic — hence injective — map F : Ω → Ω′.
> (C1, slides 2–3.)

Mok explains the deduction on the podium in one sentence: "if you have a map you can pull
back a Hermitian metric and then add to it and still get a metric of seminegative curvature,
and then you make use of the uniqueness." Pull back the target metric along f, add the
canonical metric to keep it nondegenerate, observe the sum still has seminegative curvature,
apply the uniqueness theorem, and read off that the pullback contributed nothing degenerate —
i.e. df has no kernel.

**The proof, at honest depth.** It is an integral identity, and here is the shape.

Work on the **minimal characteristic bundle** 𝒮 ⊂ ℙT_X (§3.2) — *not* on X, and *not* on the
whole projectivized tangent bundle. Let (L, ĝ) → ℙT_X be the tautological line bundle with the
metric induced by the canonical metric g, and write Θ = −c₁(L, ĝ) ≥ 0. Because 𝒮 is picked
out by the zeros of the bisectional curvature, Θ is degenerate along 𝒮, of some constant
rank; let q be the dimension of its kernel. Let ρ : ℙT_X → X be the projection and
σ := ρ*ω − c₁(L, ĝ) > 0, where ω is the Kähler form of g. Then (C1, slide 9) for **any**
Hermitian metric h on L,

  0 = ∫_𝒮 [−c₁(L, ĝ)]^{2n−2q} ∧ σ^{q−1} = ∫_𝒮 [−c₁(L, h)] ∧ [−c₁(L, ĝ)]^{2n−2q−1} ∧ σ^{q−1}.

The first equality is a degree/type vanishing on 𝒮. The second rewrites it with an arbitrary
h. Now if h has seminegative curvature the integrand of the right-hand integral is **≥ 0
pointwise**. An integral of a nonnegative quantity that vanishes forces the integrand to
vanish identically — and pointwise vanishing of that integrand is exactly the statement that
h agrees with g in the characteristic directions.

That last step is the Bochner move, and it is the reason this talk is reachable for you. The
whole difficulty is arranging the geometry so that a signed integrand appears at all.

Mok flags the one technical point that makes the setup legitimate:

> "One thing one has to check is that you integrate over some subset — you don't integrate
> over the whole projective tangent bundle — and so you have to prove that although this has
> zero eigenvalues, the zero vectors are actually tangent to the subspace, and this can be
> checked geometrically."

In other words: the kernel of the degenerate form must be tangent to 𝒮, or the integration
by parts is meaningless. It is, and the verification is geometric.

#### 4.2.4 From Hermitian to Finsler: buying existence with weaker conclusions

Now the design decision from §3.5, executed.

Hermitian metrics of Griffiths-seminegative curvature are hard to construct. Carathéodory
metrics exist on every bounded domain for free but are Finsler, not Hermitian. So Mok proves
the Finsler version — and pays for it by getting a weaker conclusion.

> **Complex Finsler Metric Rigidity (Mok 2002).** Ω a bounded symmetric domain of rank ≥ 2,
> Γ a torsion-free lattice, X = Ω/Γ, g the canonical Kähler–Einstein metric. Let h be a
> **continuous complex Finsler metric of nonpositive curvature** on X, and let
> Ω = Ω₁ × ⋯ × Ω_m be the decomposition into irreducible factors. Then there are constants
> c₁, …, c_m > 0 such that ‖α‖_h = c_k ‖α‖_g for every **minimal characteristic** vector α
> whose lift belongs to the k-th factor.

Note what is *not* claimed: nothing at all about non-characteristic directions. Mok is
explicit and cheerful about this:

> "Of course you can always perturb the metric outside of the zeros and that gives you also
> still seminegativity. So the rigidity here is just along the [characteristic bundle], which
> I could call the VMRT bundle… the statement therefore is just that you have uniqueness of
> metric along minimal directions. But that was good enough to have interesting
> consequences."

*(The version of this statement on C1 slide 15 is phrased for all vectors lifting into the
k-th factor, without the word "characteristic". The talk is unambiguous that the conclusion
holds only along minimal directions, and the surrounding slides of C1 agree with the talk. I
have followed the talk. See §10.)*

He also notes in passing why "the VMRT bundle" is a fair name for the characteristic bundle:
embed Ω into its compact dual by the Borel embedding; minimal rational curves on the compact
dual meet Ω in minimal discs; so the characteristic directions on Ω are literally the VMRT
directions of the compact dual. That is the bridge between movements two and three, and it is
his sentence, not mine.

Note also the *rewards* of Finsler weakness. Mok remarks that Hermitian metrics of
seminegative curvature, when they do exist, come from interesting places — families of
abelian varieties, and more generally spaces parametrizing Hodge decompositions — but that
this is "not the emphasis of this talk".

#### 4.2.5 The embedding theorem (2004)

With Finsler rigidity in hand, the first big payoff.

> **Embedding Theorem (Mok, "Extremal bounded holomorphic functions and an embedding theorem
> for arithmetic varieties of rank ≥ 2", *Invent. Math.* 158 (2004), 1–31).** Two forms,
> both from C1:
>
> *(Theorem 1, C1 slide 16.)* Ω irreducible of rank ≥ 2, Γ a torsion-free lattice,
> X = Ω/Γ, N a complex manifold, f : X → N holomorphic with lift F : Ω → Ñ. Suppose there
> exists a bounded holomorphic function h on Ñ with F*h ≢ constant. Then F : Ω → Ñ is an
> **embedding**; in particular f is an immersion.
>
> *(Theorem 2, C1 slide 18.)* Ω of rank ≥ 2, Γ a torsion-free **irreducible** lattice,
> X = Ω/Γ, D an arbitrary bounded domain, Γ′ ⊂ Aut(D) torsion-free discrete, N = D/Γ′,
> f : X → N nonconstant holomorphic with lift F : Ω → D. Then F : Ω → D is an **embedding**.

The talk states the second form, in equivariant language: "an assumption of a map from Ω into
some [bounded] domain, this is equivariant and the representation is one which has infinite
image on the fundamental [group]. Then when you lift to universal covers, F is actually an
embedding."

The hypothesis is almost nothing — a single nonconstant bounded holomorphic function pulled
back. The conclusion is injectivity of a map between n-dimensional manifolds. Mok's own
reaction, from the podium: "well, this was a little surprising to me when I proved it."

**How Finsler rigidity enters.** In the minimal (characteristic) directions, the
Carathéodory-type metric constructed from the available bounded holomorphic functions is
pinned to the canonical metric by Finsler rigidity, so it is nondegenerate there and F is an
immersion along those directions. Extending to *all* directions takes more work. Separating
*points* — injectivity — is harder still, and this is where the **averaging technique** comes
in: one averages extremal bounded holomorphic functions over geodesic circles, then uses
Moore ergodicity plus a density argument to promote the conclusion from one polydisc to all.
The rough sketch: if F(x) = F(y) then every pulled-back bounded holomorphic function takes
the same value at x and y; the density lemma then forces the function to be constant on a
whole circle; contradiction with a lower bound on its derivative. (C1, slides 25–26, 36–38.)

#### 4.2.6 The extension problem, and the retraction map

Mok then says he guessed the embedding theorem was hiding something stronger, and states the
question that organizes the rest of movement two:

> "An embedding doesn't have to have closed image a priori, in the sense I define it, but I
> raised the following question — **the extension problem**. I have Ω going into D. Can I go
> back from D to Ω? But first, can I go back from D to ℂⁿ? If I can go back from D to ℂⁿ and
> get a sort of **retraction map** such that [the] composition is equal to [the] identity,
> then this already implies the embedding theorem — but then maybe one can draw [a] strong
> conclusion from this."

This is a good research move to notice: he replaces "F is injective" with "F has a
left inverse", which is formally stronger, and then finds that the stronger statement is
*more* provable because it is constructive. The restored 2007 form:

> **Theorem on the Extension Problem (C1, slide 39).** Ω ⊂ ℂⁿ in its Harish-Chandra
> realization, of rank ≥ 2; Γ an irreducible lattice; X = Ω/Γ. Let N be *quasi-compact*
> (Zariski-open in a compact complex manifold), f : X → N holomorphic with lift F : Ω → Ñ,
> and assume a non-degeneracy condition (†). Then there is a **bounded vector-valued
> holomorphic map ℛ : Ñ → ℂⁿ with ℛ ∘ F = id**.

And then the two consequences (C1, slides 45–46): the **Fibration Theorem** (if
f_* : Γ ≅ π₁(N) then f is an embedding and there is a holomorphic fibration ρ : N → X with
connected fibres and ρ ∘ f = id_X), and the **Isomorphism Theorem** of §4.2.1.

The 2026 version of the extension theorem is the joint work with **Kwok-Kin Wong** cited
above. Mok describes what has to be added for the arithmetic (non-cocompact) case: first get
the map to descend to the quotient, which "involves some Riemann extension theorem argument";
then prove the retraction has **zero-dimensional fibres**. The second is the interesting one,
and the argument is a small gem:

> Suppose the fibres were positive-dimensional. Restrict the bounded holomorphic functions to
> a fibre. The fibres carry complete Kähler metrics of finite volume, generically. But a
> bounded plurisubharmonic function on a complete Kähler manifold of finite volume is
> constant. Contradiction.

C1 records the lemma that does this exactly (slide 47): *let (Z, ω) be a complete Kähler
manifold of finite volume and u a uniformly Lipschitz bounded plurisubharmonic function on Z;
then u is constant.* Zero-dimensional fibres plus the embedding gives an open map, hence an
isomorphism.

#### 4.2.7 The last hypothesis: dropping Kähler–Einstein on the target

The final refinement in movement two. The argument above wanted a canonical complete
Kähler–Einstein metric on the target's universal cover D. Not every bounded domain has one —
but every **domain of holomorphy** does:

> "By the old work of **Cheng and Yau**, and **Yau and myself**, we prove that on a bounded
> domain of holomorphy there always exists a canonical complete Kähler–Einstein [metric]."

So: replace D by its **hull of holomorphy** D̂, which is a domain of holomorphy and therefore
has the metric. In general the hull can be enormously bigger than D, which would ruin
everything — but Mok proves that in this situation **the complement D̂ ∖ D has zero Lebesgue
measure**, so the volume estimates survive the enlargement. Prove the isomorphism upstairs
with D̂, then descend.

*(The primary references, reconstructed from "chu and yao and yao and myself": Cheng–Yau on
complete Kähler–Einstein metrics on non-compact complex manifolds, and Mok–Yau,
"Completeness of the Kähler–Einstein metric on bounded domains and the characterization of
domains of holomorphy by curvature conditions", 1983. See §10.)*

### 4.3 Movement three — varieties of minimal rational tangents

Now the second machine. Curvature is gone; the VMRT replaces it.

#### 4.3.1 Why the theory exists

Mok gives the motivation twice. First from Kodaira's classification: for surfaces the picture
is clean, with the Kodaira dimension κ(X) as the birational invariant measuring growth of
spaces of pluricanonical sections, and κ(X) = −∞ characterized by uniruledness. That
characterization is proven for surfaces, proven in dimension three, and **open from dimension
four** — his words: "still well open starting with dimension four." Second, from Picard
number one, where Mori theory has nothing to contract (§3.6).

His own path in was the generalized Frankel conjecture: "from my side one motivation of
course was coming from [the] generalized Frankel conjecture — I wanted to look at the
algebro-geometric analogues."

The theory is joint with **Jun-Muk Hwang**, beginning with Hwang–Mok 1998.

#### 4.3.2 The central idea: minimal rational curves as carriers of information

Everything in this movement is the sentence quoted in §2.2. The pattern is always:

1. At a **general** point x, the VMRT 𝒞_x(X) is known — it is congruent to the model's.
2. At a **bad** point y ∈ B, nothing is known.
3. Take a minimal rational curve through y coming from a good point, lift it to the universal
   family, and **transport the invariant along it**.
4. Conclude the invariant survives at y, so the bad set was not bad after all — or at least
   is smaller than you feared.

Mok is explicit that this is analytic continuation with a **codimension budget**. Reducing
the bad set from codimension 1 to codimension 2 is decisive, because a holomorphic object
defined off a codimension-2 set extends by **Hartogs**. That single fact is the hinge of the
whole method.

#### 4.3.3 Deformation rigidity, and the one exception

The first family of results:

> **Deformation rigidity (Hwang–Mok, 1998–2005).** Let S = G/P be a rational homogeneous
> space of Picard number 1. Let 𝒳 → Δ be a regular family of projective manifolds over the
> disc whose fibres 𝒳_t are biholomorphic to S for t ≠ 0. Then the central fibre 𝒳₀ is also
> biholomorphic to S — **with exactly one exception**, the 7-dimensional Fano homogeneous
> contact manifold F₅.

(C2, Theorem 3.3.2. The series: Hwang–Mok, *Invent. Math.* **131** (1998), 393–418 — the
irreducible Hermitian symmetric spaces of compact type, which Mok says on the podium "were
the first that we studied in 1998"; *Ann. Sci. ÉNS* **35** (2002), 173–184 — the long-root
case; and *Invent. Math.* **160** (2005), 591–645 — the general case, via prolongations of
infinitesimal linear automorphisms.)

**The exception.** F₅ is the space of lines on the 5-dimensional hyperquadric Q⁵ — equivalently
the orthogonal Grassmannian of isotropic 2-planes in ℂ⁷, the adjoint variety of SO(7),
7-dimensional and contact. **Pasquier and Perrin** (*Math. Z.* **265** (2010), 589–600,
"Local rigidity of quasi-regular varieties") produced the deformation that breaks it: F₅
degenerates to a **G₂-horospherical variety**, an almost-homogeneous (two-orbit) variety with
non-reductive automorphism group. **Hwang** later showed these are the only two possibilities:
the central fibre is either F₅ or that horospherical variety (C2, Theorem 3.3.3).

Mok explains the mechanism in one line — and this is the part I could only half recover:

> "the explanation of that is also the storytelling, because it is due to the fact that the
> VMRT can jump — it can jump from a ℙ¹ × ℙ¹ to [a] hypersurface of genus 2."

> *[Gap: the target of the jump. The VMRT of F₅ is the quadric surface ℙ¹ × ℙ¹; the captions
> render what it jumps to as "hypersurface of genus 2", which is not a well-formed
> description of a surface, and neither companion states it. Impact: **low** — the point,
> that deformation rigidity fails precisely because the VMRT is not itself rigid, survives
> intact. The Pasquier–Perrin paper would settle it.]*

He generalizes forward: since the obstruction is VMRT-jumping, the same method should apply
"to many more situations even in high Picard number situations… for instance horospherical
varieties and even wonderful compactifications", and notes work in that direction by
**Fu, Hwang and Li** *(names reconstructed — see §10)*.

#### 4.3.4 The Recognition Problem

The deformation results all have the same two-step structure, and Mok isolates the second
step as a problem in its own right:

> **The Recognition Problem.** Let S = G/P be a model — a rational homogeneous space of
> Picard number 1. Let X be a uniruled projective manifold of Picard number 1 with a minimal
> rational component, whose VMRT **at a general point** is projectively congruent to that of
> S. Is X biholomorphic to S?

An affirmative answer would give a uniform proof of deformation rigidity (with the F₅
exception), because deformation always gives you the model VMRT in the limit; the work is
getting from the VMRT back to the manifold.

The baseline case is classical: if 𝒞_x(X) = ℙT_x(X) — the VMRT is everything — then X ≅ ℙⁿ.
The problem is about models where the VMRT is a *proper* subvariety.

> **Theorem (Mok 2008; Hong–Hwang 2008).** For S = G/P with P corresponding to a **long
> simple root**, the Recognition Problem is solved in the affirmative.

(C2, Theorem 3.2.1. Mok, "Recognizing certain rational homogeneous manifolds of Picard number
1 from their varieties of minimal rational tangents", *AMS/IP Stud. Adv. Math.* **42** (2008),
41–61, which does the Hermitian symmetric and contact homogeneous cases; Hong–Hwang,
"Characterization of the rational homogeneous manifold associated to a long simple root by
its variety of minimal rational tangents", *Adv. Stud. Pure Math.* **50** (2008), 217–236,
for the remaining long-root cases.)

#### 4.3.5 The flat-bundle trick: holonomy without a metric

This is the most beautiful idea in movement three, and Mok tells it as a story about giving
something up.

His starting instinct came from movement one: "since I was working on the generalized Frankel
conjecture, I take holonomy as a very important ingredient — but holonomy was defined in
terms of Riemannian geometry. So I have [a] Riemannian metric in the background, in that case
a Kähler metric."

But uniruled projective manifolds of Picard number 1 carry no canonical metric. So: **how do
you do parallel transport with no connection?**

> "I was asking in what way one can do parallel transport, holonomy, in the context of
> uniruled projective manifolds, and it came to me that there's only one canonical way that
> one can do. **If in some geometric problems I can identify a flat vector bundle, then I can
> do Euclidean geometry** — [it's] like a Gauss–Manin connection: you can move from one point
> to another by using the flat connection."

Then the observation that makes it work. Take a minimal rational curve ℓ through a bad point,
lift it to the embedded universal family, and look at the family of VMRTs along the lift. Each
VMRT is a projective subvariety of a projective space, so it has a **projective second
fundamental form** — the classical invariant measuring how a submanifold of projective space
curves away from its embedded tangent space, a section of

  Sym²T* ⊗ N (symmetric square of the cotangent bundle, valued in the normal bundle).

Compute what bundle the *relative* second fundamental form is a section of along ℓ. By
Grothendieck's splitting of vector bundles on ℙ¹ the answer is a direct sum of line bundles,
and Mok's calculation is that **this particular bundle is flat** — trivial. A section of a
flat bundle is determined by its value at one point. So the second fundamental form at a good
point *determines* the second fundamental form at the bad point.

Consequence: if the fibre at the bad point were degenerate, the second fundamental form would
degenerate too — but it cannot, because it is transported from a good point. So a
codimension-1 bad set is impossible; the bad set has codimension ≥ 2; Hartogs extends the
geometric structure across it; and a theorem of Hwang–Mok (*J. reine angew. Math.* **490**
(1997), 55–64: a uniruled projective manifold with an irreducible reductive G-structure is an
irreducible Hermitian symmetric space of compact type of rank ≥ 2) finishes.

In the contact case Mok says the same trick works one order higher — "miraculously" — with the
**third** fundamental form, again landing in a flat bundle. C2 (§3.2, discussion after Theorem
3.2.1) confirms both, and records the precise splitting type of the corank-1 distribution
along a minimal rational curve that makes the third-order version go through.

**This is the transferable idea of movement three.** You cannot transport an invariant unless
you have a connection. If no metric is available, look for a bundle in which your invariant
naturally lives, and check whether *that* bundle happens to be flat. Flatness is a much
cheaper hypothesis than a metric, and it buys exactly the same thing: a canonical
identification between fibres over different points.

#### 4.3.6 Short roots, and where it is still hard

Mok flags where the method strains. For long roots, the space of minimal rational curves
through a point is homogeneous. For **short** roots it need not be — for the symplectic
Grassmannian there are two genuinely different types of minimal rational curve, "which can be
defined simply by using linear algebra". Non-homogeneity breaks the induction.

The short-root Recognition Problem stayed open for years and was solved recently:

> **Hwang and Qifeng Li, "Characterizing symplectic Grassmannians by varieties of minimal
> rational tangents", *J. Differential Geom.* 119 (2021), 309–381.**

Mok reports the shape of their answer, which is *not* a clean "yes": from a good VMRT
structure at a good point one gets a neighbourhood on which the VMRT structure determines the
geometric structure **up to a finite number of possibilities**, indexed by the **rank of a
bilinear form** ("and this bilinear form I would not explain further"). Adding a
non-degeneracy condition — maximal rank — picks out the symplectic Grassmannian. C2 (§3.3)
independently describes the same phenomenon from the deformation side: local models for
isotrivial VMRTs on a symplectic Grassmannian depend on the rank of a skew-symmetric bilinear
form determined by the Frobenius form, and the smoothness of the central fibre forces maximal
rank.

Mok says this "turns out to be important for the last section of this talk". Hold onto it; it
is the load-bearing input in §4.4.4.

### 4.4 Movement four — uniformization for *subspaces*

The final move: run the whole programme one dimension down, for subvarieties rather than
manifolds.

#### 4.4.1 Schubert rigidity

Take a rational homogeneous space S = G/P of Picard number 1 and a **Schubert variety** S₀
inside it. Its homology class generates an extremal ray. Obvious representatives of multiples
of that class: sums of translates γ(S₀) by γ ∈ Aut(S). Question: **are those all of them?**

- **(S, S₀) is homologically rigid** if any subvariety with homology class exactly [S₀] is a
  translate of S₀.
- **(S, S₀) is Schur rigid** if any subvariety with class a *multiple* of [S₀] is a *sum of
  translates* of S₀.

The motivation Mok gives is a 1961 question of **Borel and Haefliger** on the **smoothability
of singular cycles** *(names reconstructed — see §10)*: if a pair is Schur rigid and S₀ is
singular, then no multiple of [S₀] can be represented by a smooth subvariety, because the only
representatives are sums of translates of a singular thing.

The history, all verified against the Hong–Mok bibliography:

- **M. Walters** (Ph.D. thesis, University of Michigan, 1997) and **Robert Bryant**
  ("Rigidity and quasi-rigidity of extremal cycles in compact Hermitian symmetric spaces",
  math.DG/0006186) opened the problem using **exterior differential systems**: one compares
  the *Schur* differential system (tangent planes annihilating certain Kostant forms) with
  the *Schubert* differential system (tangent planes to translates), and rigidity reduces to
  (1) equality of the two systems and (2) uniqueness of integral varieties.
- **Colleen Robles and Dennis The** ("Rigid Schubert varieties in compact Hermitian symmetric
  spaces", *Selecta Math.* **18** (2012), 717–777) settled the Hermitian symmetric case
  completely by Lie-algebra-cohomology methods. Mok's phrasing: "settled by algebraic
  Lie-theoretic methods".
- **Hong and Mok**, using VMRT geometry instead, extended it beyond the Hermitian symmetric
  case: **"Schur rigidity of Schubert varieties in rational homogeneous manifolds of Picard
  number one", *Selecta Math.* 26 (2020), no. 41**, whose Theorem 1.1 reads: *let S = G/P have
  Picard number one and let S₀ be a **non-linear smooth** Schubert variety of S; then (S, S₀)
  is Schur rigid.* Mok's summary from the podium: "applying VMRT geometry, Hong and myself
  solved the problem for smooth Schubert cycles on G/P."

#### 4.4.2 Sub-VMRT structures

Now the general machine. Let X be uniruled of Picard number 1 with VMRT structure
𝒞(X) → X, and let S ⊂ X be a complex submanifold (possibly only a *germ*, possibly only
locally defined, possibly transcendental). Define

  **𝒞(S) := 𝒞(X) ∩ ℙT(S)** — the **sub-VMRT structure**.

Mok's own description is exactly this: "you take a point and you take the VMRT of the ambient
manifold, you intersect with [the] tangent space, and then you get a subspace." It might be
empty; one assumes it is not, and that it dominates S.

The question — the **Recognition Problem for a pair** — is: *does the sub-VMRT structure
determine S?*

**In general, no**, and Mok gives the counterexample immediately: take a hyperquadric and any
hypersurface inside it; the hypersurface inherits a quadric structure, "but this is not
integrable". Some extra condition is needed. And the condition that works is, in his framing,
a form of **unlikely intersection**:

> Look at a Grassmannian, its Segre-embedded VMRT, and intersect with a sub-Grassmannian. You
> get the Segre embedding of a lower-dimensional product of projective spaces — and if you
> count dimensions, that intersection is **far larger than a generic intersection of those
> dimensions would be**. "So you have intersection at the level of projective tangent space
> of a dimension that is bigger than what you expect, but in a very specific way — so you can
> study that."

The intersection is unexpectedly big, and the fact that it is big *in a controlled way* is
exactly the extra structure that makes recognition possible.

#### 4.4.3 The Mok–Zhang theorems: from a transcendental germ to an algebraic variety

The general theory is joint with **Y. Zhang** *(first name unverified — see §10)*:
**Mok–Zhang, "Rigidity of pairs of rational homogeneous spaces of Picard number 1 and
analytic continuation of geometric substructures on uniruled projective manifolds",
*J. Differential Geom.* 112 (2019), 263–345.** C2 states the results; I quote them from there.

Two hypotheses, both of which Mok names on the podium:

- **Condition (T)**, a technical condition on the intersection 𝒞(X) ∩ ℙT(S), automatic for
  the model pairs;
- **non-degeneracy for substructures**, defined via the projective **second fundamental
  form** — Mok: "this can be defined in terms of the second fundamental form".

> **Rational saturation (C2, Theorem 4.5.1 = Mok–Zhang Thm 1.4).** Under Condition (T) and
> non-degeneracy for substructures at general points, the submanifold S is **rationally
> saturated**: S is uniruled by open subsets of minimal rational curves belonging to 𝒦.

That is the first miracle. You start with an arbitrary complex submanifold germ whose only
property is how its tangent spaces meet the VMRTs — and you conclude that it is *swept out by
pieces of minimal rational curves*. Mok: "if you have something tangent to this germ, which
is transcendental analytic a priori, then actually you can pass a whole line inside."

> **Algebraicity (C2, Theorem 4.5.2 = Mok–Zhang Main Theorem 2).** Suppose in addition that X
> has Picard number 1 and is **uniruled by lines** (minimal rational curves of degree one),
> and that the distribution D on S spanned pointwise by 𝒞_x(S) is **bracket generating**.
> Then there is an irreducible subvariety Z ⊂ X with S ⊂ Z and dim Z = dim S.

That is the second miracle, and it is the one Mok highlights: *"this is a kind of theorem
passing from analyticity to algebraicity."* A transcendental germ, satisfying an infinitesimal
condition, is forced to be an open piece of a projective-algebraic variety.

The technical heart, which he names: the **Thickening Lemma**. To propagate the sub-VMRT
structure along a chain of minimal rational curves you need not just the curve but a
neighbourhood of it. Mok: "the thickening lemma tells you that you take this line, and then
you can construct a smooth neighbourhood — more properly an immersed neighbourhood — where
you can then do deformation theory inside this neighbourhood, and that's very important."
C2 (Theorem 4.5.3) states it: given a suitable point of 𝒞(S) and the minimal rational curve ℓ
in that direction, there is an s-dimensional complex manifold E containing ℙ¹ and an
immersion F : E → X restricting to the normalization of ℓ and whose image contains a
neighbourhood of x in S.

C2 also names the obstruction that has to be beaten: in the inductive propagation along chains
of rational curves, the obstruction lies on subvarieties of **codimension ≥ 2** in certain
universal families of chains — and codimension ≥ 2 is, again, where Hartogs-type extension
lives.

Then the dictionary of §2.2 goes on the screen, and the movement ends with the observation
that this framework tolerates singular subvarieties better than Riemannian geometry does:
"normally when you have singularity it's very difficult to study deformation, but if you have
an ambient space which [is] smooth you can still study it."

#### 4.4.4 The final theorem: semi-rigidity of proper holomorphic maps

The last twelve minutes, and the newest result.

**Why proper maps.** Mok gives the link that motivates the whole question, and it ties movement
four back to movement two: if you have cocompact lattices and an injective homomorphism
between them, the lifted map between the domains is **proper**. So proper holomorphic maps are
the natural generalization of the maps studied in §4.2 — you keep the boundary behaviour but
drop the equivariance.

**Step one, equal rank.** Mok made a conjecture in 1989; his student **I-Hsun Tsai** proved it:

> **(Tsai, "Rigidity of proper holomorphic maps between symmetric domains", *J. Differential
> Geom.* 37 (1993), 123–160.)** Let F : D → D′ be a proper holomorphic map between bounded
> symmetric domains with rank(D) ≥ 2 and rank(D′) ≤ rank(D). Then rank(D) = rank(D′) and F is
> **totally geodesic**.

(C1, slide 58, which also records the 1989 attribution of the conjecture. The talk states a
slightly weaker version — same rank, rank ≥ 2 — and C1's version is stronger; I quote C1.)

The method is the one to remember, because it recurs: **look at what the map does to the
boundary.** A bounded symmetric domain of rank r has a boundary stratified by **boundary
components** (faces), each of which is itself a bounded symmetric domain of lower rank; the
maximal ones have rank r − 1. The moduli space of maximal boundary components is an open
subset of a rational homogeneous space G/P — the compact dual's Grassmannian. So a proper map
Ω → Ω′ induces a **moduli map between rational homogeneous spaces**, and now all of movement
three is available. Mok: "then one studies associated maps on G/P — that's the basic
philosophy."

C1 (slides 59–60) gives the analytic mechanism concretely: writing Ω ⊃ Δ × Ω″ with Ω″ of rank
r − 1, one takes non-tangential limits F*(w) := lim_{z→ξ} F(w, z) for almost every ξ in the
boundary circle. Properness forces F* to map into ∂Ω′. Then a Poisson-type integral
representation recovers F from its boundary values, and *that* forces algebraic constraints on
the images of the totally geodesic subdomains. Non-tangential limits plus integrals of
boundary values equals algebraic constraints — that is the sentence.

**Step two, unequal rank — semi-rigidity.** When rank(Ω′) > rank(Ω) total geodesy is simply
false, and the reason is easy: given any bounded holomorphic function g on Ω, the **graph**
map z ↦ (F₀(z), g(z)) is still proper into a bigger domain but is certainly not totally
geodesic. The best you can hope for is that this is the *only* way to be non-rigid. That is
**semi-rigidity**: every proper map is a standard embedding composed with a graph.

Mok's conjecture, and the theorem:

> **Theorem (Sung-Yeon Kim, Ngaiming Mok, Aeryeong Seo, "Proper holomorphic maps between
> bounded symmetric domains with small rank differences", *J. Differential Geom.* 131 (2025),
> 551–631; arXiv:2307.03390, posted 7 July 2023, revised 13 January 2025).**
>
> Let Ω, Ω′ be irreducible bounded symmetric domains with
> **2 ≤ rank(Ω′) < 2·rank(Ω) − 1**, and suppose either Ω and Ω′ have the same type, or Ω is of
> **type III** and Ω′ is of **type I**. Then any proper holomorphic map f : Ω → Ω′ is, up to
> automorphisms, of the form f = ι ∘ F where F = F₁ × F₂ : Ω → Ω′₁ × Ω′₂, F₁ is a **standard
> embedding**, F₂ is arbitrary holomorphic, and ι : Ω′₁ × Ω′₂ → Ω′ is a totally geodesic
> holomorphic isometric embedding.
>
> Moreover, under the same rank condition, **no proper holomorphic map exists at all** if Ω is
> of type I and Ω′ of type III, or if Ω is of type II and Ω′ is of type I or III.

The rank condition rank(Ω′) < 2·rank(Ω) − 1 is exactly the talk's "r′ ≤ 2r − 2", which the
captions render correctly — I verified it against the paper's abstract. Type III to type I is
the case Mok singles out as hardest, and it is why the Siegel upper half-plane appears: type
III domains are the ones biholomorphic to Siegel upper half-planes parametrizing polarized
abelian varieties.

**The example that shows the theorem is sharp.** Mok credits **Aeryeong Seo** ("New examples
of proper holomorphic maps among symmetric domains", *Michigan Math. J.* **64** (2015),
435–448) with generalized **Whitney maps** in this setting. The classical Whitney map is the
proper map Bⁿ → B^{2n−1} between balls, which is proper and non-linear; Mok points out why it
turns up here — balls really are embedded inside these domains, as the fibres of the boundary
projections he described earlier, so ball-to-ball proper maps are automatically available as
building blocks.

**The proof scheme**, in his own order, and it is a beautiful chain that uses every previous
movement:

1. Pass from the proper map to **moduli maps** between spaces of boundary components. These
   are now maps between Grassmannians — and, crucially, not only between the maximal ones:
   "one can study moduli spaces not just those which are maximal boundary components but also
   other spaces, and in this case one can induce maps on Grassmannians of different types."
2. What you get is a **germ of a map** between domains in the compact duals. Study it with
   **CR geometry** — the methods of **Sung-Yeon Kim**, and of **Kim with Dmitri Zaitsev**
   (*Invent. Math.* **193** (2013), 409–437, on CR maps between Shilov boundaries;
   *Math. Ann.* **362** (2015), 639–677, on proper holomorphic maps between bounded symmetric
   domains). The properness produces **CR-maps between CR-hypersurfaces of mixed signature**
   (the paper's own phrase), and those satisfy strong local differential-geometric
   constraints.
3. Conclude that the germ is **VMRT-respecting** and **line-preserving** — it sends germs of
   lines to germs of lines, and sends the VMRT not merely into the target VMRT but onto a
   **linear section** of it. Mok is careful about this: "VMRT-respecting means that it sends
   VMRT — it's a subset of the VMRTs — but it's better than that: it's actually sending this
   to a linear section of the VMRT of the target." A linear section of a VMRT is precisely a
   sub-VMRT structure (§4.4.2).
4. **Same type:** apply the rigidity results for VMRT-respecting maps from §4.3–4.4 (Mok's
   own, and Hong–Mok). Done.
5. **Type III into type I — the hard case:** the moduli spaces you meet on the type III side
   are **symplectic Grassmannians**, so you need maps from a symplectic Grassmannian into an
   ordinary Grassmannian. This is where **Hwang–Li (2021)** enters: their solution of the
   short-root Recognition Problem applies, and — because of where the problem came from — one
   can prove the relevant bilinear form has **maximal rank**, which is exactly the extra
   condition their theorem needs. That gives the symplectic Grassmannian structure.
6. Finally solve the **Recognition Problem for a pair** in that setting — which Mok had solved
   for the Lagrangian Grassmannian, and which was then extended to the symplectic case. "And
   then by the generalization of this argument one can solve the problem totally."

Then: "Thank you." The talk ends there, with no summary.

---

## 5. The one argument

The talk's stated emphasis is movement two, and its engine is the piece with no analogue
anywhere else in the lecture: **an ergodic theorem used to manufacture holomorphic functions.**
Here it is, as precisely as the sources allow.

**The goal.** Given F : Ω → Ñ (the lift of f : X_Γ → N), produce a holomorphic retraction
ℛ : Ñ → ℂⁿ with ℛ ∘ F = id. Equivalently: produce n bounded holomorphic functions on Ñ whose
pullbacks under F are the **coordinate functions** z₁, …, zₙ of the Harish-Chandra realization
of Ω.

**The obstacle.** You have no control over F. Pull back a bounded holomorphic function h from
Ñ and you get some bounded holomorphic function F*h on Ω about which you know nothing. Mok:
"the map capital F is rather arbitrary a priori; when you pull it back, actually what you get
is functions which might be rather chaotic on the boundary."

**The object to work with.** Define

  ℱ := F*H(Ñ) = { F*h : h a bounded holomorphic function on Ñ } ,

the space of pullbacks. It has exactly three properties, and Mok lists them from the podium:

1. **Γ-invariance.** ℱ is a Γ-invariant complex vector space: s ∈ ℱ and γ ∈ Γ imply
   s ∘ γ ∈ ℱ. (Because F is Γ-equivariant.)
2. **Normality.** A uniformly bounded sequence in ℱ has a subsequence converging uniformly on
   compact subsets, and the limit is again in ℱ.
3. **Closure under averaging.** One can integrate members of ℱ against a measure and stay in
   ℱ.

Those three properties are the whole toolkit. Property 2 lets you take limits; property 3 lets
you average; property 1 lets Γ act. Nothing else is used.

**Step 1 — a flow, and a projection.** Because Ω is irreducible of rank r ≥ 2, it contains
totally geodesic products Δ × Ω″ with Ω″ of rank r − 1. Take the **hyperbolic flow** along a
geodesic in the Δ factor — the one-parameter group of transvections z ↦ (z + t)/(1 + tz),
−1 < t < 1 — and extend it to a flow on all of Ω. Associated to it is a **projection onto a
maximal boundary component**, i.e. onto a boundary face of rank r − 1.

> *[Gap: the name of this projection. The captions render it "ka projection" / "KD
> projection" and I could not identify it against any source; C1 writes it as π_Φ, the
> projection onto a rank-1 boundary component Φ, without a person's name attached. Impact:
> **low** — the object is unambiguous, only its name is lost. I call it "the projection onto a
> boundary face" throughout.]*

Mok adds a counterintuitive fact about which faces are connected by such flows: "counter to
what one might think, when you have a hyperbolic flow, actually the two faces flowing from one
to the other are rather arbitrary. In fact if you take any two maximal faces whose closures do
not intersect, you have a flow." So the right parameter space is the space of **regular pairs
of faces**, which is explicit and carries a G₀-action, G₀ = Aut₀(Ω).

**Step 2 — boundary values, from real analysis.** Now you need the pulled-back functions to
have boundary values. For the **ball** there is a classical theory of **admissible (Korányi)
limits**: instead of non-tangential approach along a cone you approach through wider,
anisotropic regions, and a bounded holomorphic function has an admissible limit at almost
every boundary point. The relevant refinement here — non-tangential convergence to a *boundary
component*, not to the Shilov boundary — is due to **Korányi (1976)**. C1 (slide 44) states
exactly this and cites it.

But you need boundary values on a *face*, not at a point, so you must choose a face on which
almost every point has an admissible limit. Mok:

> "I have to choose a boundary face where almost every point has an admissible boundary limit,
> and this one can do carefully by making use of the [Fubini theorem]. So this is where some
> real analysis enters into the picture."

A Fubini argument on the fibration of the boundary by faces: if the bad set has measure zero
in the boundary, then for almost every face it has measure zero in that face. Standard, and
decisive.

He also notes the compatibility that makes the whole thing consistent: when you flow along a
geodesic, "actually it stays inside the admissible region" — the hyperbolic flow approaches
the boundary admissibly, which is precisely the approach mode for which the limits exist.

**Step 3 — the "one of the two" proposition.** Here is where the ergodic theorem enters, and
where Mok is candid about the cost.

> **Proposition (as stated in the talk).** Let (Φ, Φ′) be a regular pair of faces such that
> both relevant pullbacks have admissible boundary values. Then **one of the two** functions —
> the pullback along the projection to Φ, or the pullback along the projection to Φ′ —
> belongs to ℱ.

Why only one of the two? Because Moore's ergodicity theorem gives you density of a lattice
orbit but tells you nothing about *direction*. Mok:

> "Why one of the two? Because when I apply the Moore ergodicity theorem, actually I don't
> know where I can take the limit, so it's only one of the two possible directions. So this
> introduces some complexity into the problem."

**Step 4 — one is enough.** The saving observation, and the reason the whole thing works:

> "The idea is that one can do this carefully, and in fact there exist such a function.
> **[The] existence of one single such function is good enough.**"

Because such a function is invariant under the flow, and each fibre of the boundary projection
is (a ball, hence) connected and swept by the flow, the function is constant on whole fibres:
"this would be [flow]-invariant, and so the whole ball will take the same value."

**Step 5 — density upgrades one to all.** Now ℱ contains a subspace V that is invariant not
just under Γ but under the whole group G₀ — because elements of G₀ can be approximated by
products γ·h with γ ∈ Γ and h in the hyperbolic flow, **assuming ΓH is dense in G₀**, which
Mok says "can always be assumed". That is Moore ergodicity doing its job: a lattice orbit is
dense off a null set, and the null set is handled by the uniform-constant limiting argument of
C1 slides 37–38.

**Step 6 — the vanishing theorem for invariant subspaces.**

> **Theorem (as stated in the talk).** Let Ω be an irreducible bounded symmetric domain of
> rank ≥ 2. If V is a G₀-invariant vector subspace of bounded holomorphic functions that
> **properly contains the constants**, then V is the **entire space**.

There is no room between "more than the constants" and "everything". This is the rigidity
statement that ends the argument.

**Step 7 — from functions to coordinates.** V being everything means in particular that the
**identity map** is realized: you obtain functions on Ñ pulling back to z₁, …, zₙ. Those are
the components of the retraction ℛ. Mok makes one further remark that is worth pausing on:

> "If you have the coordinates, if you can multiply, you would get the whole Taylor expansion.
> The point here is that **you don't need to assume that it's an algebra**. It is possible to
> generate the other functions by making use of Lie algebras."

ℱ is only a vector space — closed under addition and limits, not under multiplication. Getting
higher-order functions from linear ones would be trivial in an algebra and is not available
here; the Lie algebra of G₀ supplies the missing generation. That is a genuine technical
subtlety and he flags it as one.

**Step 8 — descend, and finish.** With ℛ ∘ F = id: prove ℛ is Γ-equivariant (by the maximum
principle, C1 slide 45) so it descends to ρ : N → X with ρ ∘ f = id; prove the fibres of ρ are
**zero-dimensional** by the plurisubharmonic-function-on-a-finite-volume-complete-Kähler-manifold
lemma of §4.2.6; conclude f is an open injective map between manifolds of the same dimension,
hence a biholomorphism.

**What to take away.** The argument's spine is: *build a space of functions with three closure
properties; use a dynamical system to produce one element with a special invariance; use
density to promote invariance under a discrete group to invariance under a continuous one; use
a rigidity theorem to jump from "more than trivial" to "everything".* Steps 4 and 5 are the
interesting ones. Existence of a single object plus a density argument gives you the entire
object. That pattern is worth stealing (§7.3).

---

## 6. Do this by hand

Two exercises. The first makes the Finsler/Hermitian distinction concrete and shows you where
rank ≥ 2 lives. The second computes a VMRT from scratch. Neither needs anything you do not
already have.

### 6.1 The bidisc: a metric that is not Hermitian, and a curvature that vanishes (30 minutes, pen)

Let Ω = Δ × Δ ⊂ ℂ², the bidisc — the simplest bounded symmetric domain of rank 2, and a
maximal polydisc in itself.

**(a)** Recall the Carathéodory metric of §3.5: ‖ξ‖_κ = sup over holomorphic f : Ω → Δ of
‖df(ξ)‖_Poincaré. Show that at the origin, for ξ = (ξ₁, ξ₂) ∈ T₀(Ω) ≅ ℂ²,

  ‖ξ‖_κ = max( |ξ₁|, |ξ₂| ).

**(b)** Show that this norm does **not** come from any Hermitian inner product on ℂ².

**(c)** Give Ω the product Poincaré metric. Compute the holomorphic bisectional curvature
R(ξ, ξ̄, η, η̄) where ξ = (1,0) and η = (0,1) at the origin. Then say, in one sentence, what
this has to do with the statement "rigidity requires rank ≥ 2".

<details>
<summary>Solution</summary>

**(a)** *Lower bound.* The coordinate projections p₁(z₁,z₂) = z₁ and p₂(z₁,z₂) = z₂ are
holomorphic maps Ω → Δ. At the origin the Poincaré metric on Δ is ds² = |dw|²/(1−|w|²)², so
‖dw‖_Poincaré = |w| at 0 (with the normalization ‖·‖ = |·|/(1−|·|²) evaluated at 0). Hence
dp_k(ξ) = ξ_k gives ‖ξ‖_κ ≥ max(|ξ₁|, |ξ₂|).

*Upper bound.* Let f : Ω → Δ be holomorphic with f(0) = 0 (compose with an automorphism of Δ
if not; that does not change the Poincaré norm of the differential). Write
df₀(ξ) = a ξ₁ + b ξ₂. Restrict f to the disc t ↦ (t·u₁, t·u₂) for a unit vector u in the
*polydisc* sense, i.e. max(|u₁|,|u₂|) = 1 — this really is a holomorphic map Δ → Ω. The
composite Δ → Δ fixes 0, so Schwarz gives |a u₁ + b u₂| ≤ 1 for all such u. Taking
u = (e^{iθ₁}, e^{iθ₂}) and optimizing the phases gives |a| + |b| ≤ 1. Then
|df₀(ξ)| = |aξ₁ + bξ₂| ≤ (|a|+|b|)·max(|ξ₁|,|ξ₂|) ≤ max(|ξ₁|,|ξ₂|).

So ‖ξ‖_κ = max(|ξ₁|, |ξ₂|) — the **sup norm**, exactly as C1 slide 14 asserts for Δⁿ.

**(b)** A norm comes from an inner product if and only if it satisfies the parallelogram law
‖x+y‖² + ‖x−y‖² = 2‖x‖² + 2‖y‖². Take x = (1,0), y = (0,1). Then
‖x+y‖ = ‖x−y‖ = 1, so the left side is 2; but 2‖x‖² + 2‖y‖² = 4. Fails. So the Carathéodory
metric of the bidisc is genuinely **Finsler and not Hermitian**.

This is the entire reason Mok needs a Finsler rigidity theorem: the metric he can always
construct is not of the type his 1987 theorem handles.

**(c)** For a **product** metric the curvature tensor is block-diagonal: any curvature
component mixing the two factors vanishes. So R(ξ, ξ̄, η, η̄) = **0** for ξ tangent to the
first factor and η tangent to the second. (Meanwhile R(ξ,ξ̄,ξ,ξ̄) < 0 — each factor is a
hyperbolic disc.)

The connection to rank: those null directions of the bisectional curvature are exactly what
the rigidity proofs integrate over. The **minimal characteristic bundle** 𝒮 (§3.2) is built
from them, and the integral identity of §4.2.3 lives on 𝒮 and has a degenerate 2-form with a
q-dimensional kernel — q being the dimension coming from these zeros. In rank 1 (the disc, the
ball) the bisectional curvature has no zeros, 𝒮 is everything, the identity degenerates, and
**every theorem in movement two is false**. Rank ≥ 2 is not a technical convenience; it is the
hypothesis that creates the object being integrated over.
</details>

### 6.2 Compute a VMRT (25 minutes, pen)

Let X ⊂ ℙ^{n+1} be the **Fermat hypersurface** of degree d,

  X = { Z₀^d + Z₁^d + ⋯ + Z_{n+1}^d = 0 },

and assume 1 ≤ d ≤ n. Its minimal rational curves are the **lines** contained in X (this is
given; you do not have to prove it). Fix a point z = [z₀, …, z_{n+1}] ∈ X.

**(a)** Write down the conditions on a direction w = (w₀, …, w_{n+1}) for the line
t ↦ [z + tw] to lie entirely in X, and count them.

**(b)** Deduce the dimension of the VMRT 𝒞_z(X) ⊂ ℙT_z(X).

**(c)** Specialize to d = 2 — the smooth quadric Qⁿ — and check your answer against the table
in §3.6.

<details>
<summary>Solution</summary>

**(a)** Substitute and expand in t:

  Σ_j (z_j + t w_j)^d = Σ_j z_j^d + t·d·Σ_j z_j^{d−1} w_j + t²·(d(d−1)/2)·Σ_j z_j^{d−2} w_j²
    + ⋯ + t^d·Σ_j w_j^d.

For the whole line to lie in X this polynomial in t must vanish identically, so **every
coefficient** must vanish. The t⁰ coefficient vanishes because z ∈ X. That leaves the
coefficients of t¹, t², …, t^d: exactly **d equations**, namely

  Σ_j z_j^{d−k} w_j^{k+1} = 0 for k = 0, 1, …, d−1.

(C1 slide 52 does this computation and counts "d+1 equations" including the one automatically
satisfied at t⁰.)

**(b)** The directions w live in ℂ^{n+2}. Imposing the d conditions cuts that down to
n + 2 − d; then subtract 1 because w and w + λz span the same line, and 1 more for
projectivizing. So

  **dim 𝒞_z(X) = (n+2) − d − 1 − 1 = n − d.**

(C1 slide 52 does the same count and writes (n+1) − (d+1) − 1 = n − d − 1, because *its*
Fermat hypersurface sits in ℙ^n with n+1 coordinates rather than in ℙ^{n+1} with n+2. Shift n
by one and the two agree.)

The condition d ≤ n is what makes this nonnegative — i.e. what makes X uniruled by lines at
all. When d gets large relative to n the hypersurface stops containing lines through a general
point, and indeed stops being Fano.

**(c)** d = 2: the equations are Σ z_j w_j = 0 (the tangent hyperplane) and Σ w_j² = 0 (the
quadric itself). So the lines through z in Qⁿ are cut out by intersecting the tangent
hyperplane section with the quadric — and the VMRT is a **quadric of dimension n − 2**, i.e.
**Q^{n−2}**. That is exactly the row for Qⁿ in the table of §3.6.

**What you have just seen.** The VMRT of a quadric is a smaller quadric; the VMRT of ℙⁿ is all
of ℙ^{n−1}; the VMRT of a Grassmannian is a Segre variety. In each case a *global* object is
encoded in a *projective subvariety of one tangent space*. The Recognition Problem (§4.3.4)
asks whether the encoding is injective — whether that one subvariety at one general point
determines the manifold. For long roots the answer is yes.
</details>

---

## 7. What is actually useful to you

This talk is a long way from agent systems, and I am not going to pretend otherwise. But five
of its moves are method, not content, and each one is a thing you can actually do.

### 7.1 Choose the invariant that always exists, then weaken the conclusion to match

The cleanest decision in the lecture. Mok's 1987 theorem needs a Hermitian metric of
Griffiths-seminegative curvature, and he says plainly that such things are "very difficult to
construct". So he switches to the **Carathéodory metric**, which exists on every bounded
domain for free — because bounded holomorphic functions exist on every bounded domain for
free — and which is Finsler rather than Hermitian. The price is a weaker theorem: uniqueness
only along minimal characteristic directions, with the metric free to be perturbed elsewhere.
He pays it and says "that was good enough to have interesting consequences."

The general form: **when your strong hypothesis is unverifiable in practice, find the weakest
structure that is automatically present, and see how much of the conclusion survives.** A
partial conclusion on a distinguished sub-bundle beat a total conclusion you could never
invoke. In your own work this is the difference between an invariant you can only assert and
one a system can always compute — the second is worth a weaker theorem.

### 7.2 Replace "injective" with "has a left inverse"

Mok had an embedding theorem. He noticed that the *stronger* statement — the existence of a
retraction ℛ with ℛ ∘ F = id — was actually the more tractable one, because a retraction is a
thing you can try to **build**, whereas injectivity is a thing you can only try to **verify**.
He says so: "if I can go back from D to ℂⁿ and get a sort of retraction map such that the
composition is equal to identity, then this already implies the embedding theorem — but then
maybe one can draw a strong conclusion from this."

Constructive strengthenings are often easier than the non-constructive statements they imply.
Worth remembering the next time a property is stated as a negation ("no two inputs collide")
rather than as a construction ("here is the decoder").

### 7.3 One instance, plus density, equals everything

The engine of §5, and the most transferable pattern in the talk.

Mok cannot control which of two limits an ergodic argument delivers, so he proves that
**one of the two** always lands in his function space ℱ — and then observes that the
**existence of a single such function is enough**, because it is invariant under a flow, and
because a lattice orbit is dense, so invariance under the discrete group upgrades to
invariance under the whole continuous group, at which point a rigidity theorem says the
invariant subspace must be everything.

Structurally: *weak existence + a symmetry + a density statement ⟹ full generality.* You
already know this shape from ergodic arguments in statistical mechanics. It is worth naming
because it is a way to make progress when your procedure is non-deterministic in a direction
you cannot control. Do not fight for a canonical choice; prove that either choice suffices,
get one instance, and let the group action do the rest.

The honest caveat, which Mok also names, is that ergodicity gives density **off a null set**,
and the null set is real: there are maximal polydiscs whose orbit is discrete. His fix is a
**uniform lower bound** on a derivative, independent of the polydisc, which lets him take
limits to reach the exceptional cases (C1, slide 38). If you use this pattern, the exceptional
set is where the actual work is.

### 7.4 If you have no connection, look for a flat bundle

The most elegant idea in the lecture (§4.3.5). Mok wants to transport a local invariant from a
good point to a bad point. In Riemannian geometry you would use the metric connection. He has
no metric. So he asks which bundle his invariant naturally lives in — for the second
fundamental form, Sym²T* ⊗ N restricted to a rational curve — and computes that **that bundle
is flat**. A section of a flat bundle is determined by its value at one point. Transport for
free.

The generalizable claim: *parallel transport is not about metrics, it is about trivializable
bundles.* When you need to compare a quantity at two different states of a system and there is
no canonical way to identify the state spaces, do not build a metric; look for a
representation in which the quantity is literally the same object at both states.

The companion piece is the **codimension budget**. Mok's whole method is bookkeeping on how
big the bad set is: codimension 1 is fatal, codimension 2 is fine because Hartogs extends
across it. Having an explicit "how much of the domain can I fail to control and still win"
threshold is a good discipline, and it is exactly the question you should ask of any
propagation or repair procedure.

### 7.5 Characterize a global object by a pointwise invariant — and expect it to almost work

The Recognition Problem (§4.3.4) is: *does the VMRT at one general point determine the whole
manifold?* This is the same question as "does the type signature determine the
implementation?", and the answers are instructive because they are not clean.

- For long roots: **yes**, cleanly (Mok 2008, Hong–Hwang 2008).
- For short roots: **no** — Hwang–Li get the structure only up to a **finite** list of
  candidates, indexed by the rank of a bilinear form, and need one extra non-degeneracy
  condition to single out the right one.
- For the *pair* version (sub-VMRT structures, §4.4.2): **no in general** — the hyperquadric
  counterexample — but yes under Condition (T) plus non-degeneracy for substructures.

That pattern — a pointwise invariant that determines the object up to finitely many choices,
with a separate non-degeneracy condition breaking the tie — is what a realistic
"specification determines implementation" claim actually looks like. When a characterization
theorem gets a "finite number of possibilities" clause, that is not a failure of the theorem;
it is the theorem telling you which extra bit of data you forgot to specify.

### 7.6 The one about research practice

Mok's own summary of his method is worth quoting for its own sake:

> "This is **problem-based**. Once a problem is formulated, even though it's a problem in
> Kähler geometry, I make use of a collection of methods ranging from nonlinear PDE, algebraic
> geometry, [several complex variables], and then Riemannian geometry."

His 1988 proof used the Kähler–Ricci flow (PDE), deformation of rational curves (algebraic
geometry) and Berger's holonomy theorem (Riemannian geometry) in a single argument. His 2025
work uses ergodic theory, harmonic analysis on symmetric spaces, CR geometry, and the VMRT
machinery, in a single argument. Forty years of increasing methodological distance, all aimed
at the same handful of questions.

The pointed observation: the *problems* stayed fixed and the *tools* were imported as needed.
That is the opposite of the more common pattern — pick a technique, then look for problems it
fits. It is also the harder discipline, because it requires learning a subject you do not
already know in order to finish something you started years ago.

---

## 8. Where to read next

1. **Mok, "Geometric structures and substructures on uniruled projective manifolds"**, in
   *Foliation Theory in Algebraic Geometry* (Simons Symposia), Springer 2016, pp. 103–148 —
   [preprint PDF](http://hkumath.hku.hk/~imr/IMRPreprintSeries/2015/IMR2015-9.pdf). Start
   here. It is a real survey with real statements, it covers movements three and four, and it
   is the closest thing to a companion paper that exists for this talk. §§2.1–2.2 (Ochiai,
   Cartan–Fubini) and §§4.4–4.5 (sub-VMRT structures, rational saturation, the Thickening
   Lemma) are the load-bearing sections.

2. **Mok, "Ergodicity, bounded holomorphic functions and geometric structures in rigidity
   results on bounded symmetric domains"**, ICCM Hangzhou 2007 —
   [slides PDF](https://hkumath.hku.hk/~nmok/ICCM2007.pdf). Seventy-two slides, mostly
   statements, covering movement two end to end: Hermitian metric rigidity, the integral
   curvature identity, the Carathéodory metric, Finsler rigidity, the 2004 embedding theorem,
   the extension problem, the fibration and isomorphism theorems, and the proper-map material.
   Dense but very fast to read because it is a slide deck.

3. **Kim, Mok and Seo, "Proper holomorphic maps between bounded symmetric domains with small
   rank differences"**, *J. Differential Geom.* **131** (2025), 551–631 —
   [arXiv:2307.03390](https://arxiv.org/abs/2307.03390). The talk's final theorem, with the
   full statement and the CR-geometry machinery. Read the abstract and the introduction even
   if you read nothing else; the abstract alone confirms the rank condition and names the
   whole proof strategy.

If you want the monograph rather than the surveys: **Mok, *Metric Rigidity Theorems on
Hermitian Locally Symmetric Manifolds*, Series in Pure Mathematics 6, World Scientific,
1989** — the book behind §4.2.3.

---

## 9. Self-test

<details>
<summary>1. State the uniformization theorem in one variable, and say precisely which of its features Mok's four movements are trying to recover in higher dimensions.</summary>

Every Riemann surface has universal cover the sphere, the plane, or the disc — three models,
matching curvature +, 0, −. Two features are recovered separately: **characterization of the
models by curvature** (movement one: nonnegative holomorphic bisectional curvature forces the
manifold; movement two: quotients of bounded symmetric domains cannot be deformed), and
**characterization by a discrete invariant** — genus in one variable, replaced in movement two
by the fundamental group and in movement three by the variety of minimal rational tangents.
Movement four does the same for subvarieties rather than manifolds. What is *not* recovered is
a finite list of models; there is none in higher dimension.
</details>

<details>
<summary>2. What is the rank of a bounded symmetric domain, and why does every rigidity theorem in movements two and four assume rank ≥ 2?</summary>

The rank is the largest r with a totally geodesic polydisc Δ^r ⊂ Ω; equivalently
min(p,q) for the type I matrix domain of p×q matrices. Rank ≥ 2 matters because in a product
the holomorphic bisectional curvature *between the factors vanishes*. Those zeros define the
minimal characteristic bundle 𝒮, and every rigidity proof is an integral identity over 𝒮 with
a degenerate curvature form whose kernel has to be tangent to 𝒮. Rank 1 — disc, ball — has no
zeros, no 𝒮, and no theorems: all of the rigidity statements are false there.
</details>

<details>
<summary>3. Define the Carathéodory metric, compute it on the polydisc, and say why Mok needs a Finsler rigidity theorem and not just a Hermitian one.</summary>

‖ξ‖_κ = sup over holomorphic f : M → Δ of ‖df(ξ)‖ in the Poincaré metric. On Δⁿ it is
max_k |ξ_k| — a sup norm, which fails the parallelogram law, hence is not induced by any
Hermitian inner product. Mok needs the Finsler theorem because Hermitian metrics of
Griffiths-seminegative curvature are hard to construct, whereas the Carathéodory metric exists
on every bounded domain automatically — built out of bounded holomorphic functions, which
every bounded domain has. He trades an unverifiable hypothesis for a free one, and pays with a
weaker conclusion: uniqueness only along minimal characteristic directions.
</details>

<details>
<summary>4. State Hermitian metric rigidity, and describe its proof in the terms you already own.</summary>

Ω irreducible bounded symmetric of rank ≥ 2, Γ a torsion-free lattice, X = Ω/Γ, g the
canonical Kähler–Einstein metric. If h is any Hermitian metric on X with curvature
seminegative in the sense of Griffiths, then h ≡ c·g. (Mok, *Ann. of Math.* 125 (1987); the
domination hypothesis removed by To in 1989.) The proof is a **Bochner argument**: on the
minimal characteristic bundle 𝒮 an integral of a top-degree curvature form vanishes for
degree/type reasons; rewriting it with an arbitrary metric h gives an integral whose integrand
is pointwise ≥ 0 when h has seminegative curvature; a nonnegative integrand with vanishing
integral vanishes identically; and pointwise vanishing is exactly h = cg on characteristic
directions. The technical point is that the integration is over 𝒮 and not over all of ℙT_X,
and that the null vectors of the degenerate form are tangent to 𝒮.
</details>

<details>
<summary>5. What is the hypothesis of the Isomorphism Theorem, and why is it startling?</summary>

That a holomorphic map f : Ω/Γ → D/Γ′ induces an **isomorphism on fundamental groups** — i.e.
of lattices. The conclusion is that f is a biholomorphism. It is startling because the
hypothesis is purely group-theoretic and carries no analytic information at all, and because
in general it cannot be true: Mok replaces conditions on higher homotopy groups with the
assumption that the target's universal cover carries enough **bounded holomorphic functions**.
Ω must have rank ≥ 2 and Γ must be irreducible.
</details>

<details>
<summary>6. Define the VMRT, and give Mok's dictionary between VMRT geometry and Riemannian geometry.</summary>

For X uniruled with a minimal rational component 𝒦, at a general point x the tangent map sends
each minimal rational curve through x to its tangent direction; the image
𝒞_x(X) ⊂ ℙT_x(X) is the variety of minimal rational tangents. Mok's dictionary: uniruled
projective manifold ↔ Riemannian manifold; 𝒞(X) ↔ unit sphere bundle; minimal rational curves
↔ geodesics (but only in the directions lying in the VMRT); the tautological foliation ↔ the
geodesic flow; sub-VMRT structure ↔ Riemannian submanifold; uniruled projective subvariety ↔
totally geodesic submanifold. The dictionary's one genuine break: geodesics exist in every
direction, minimal rational curves do not.
</details>

<details>
<summary>7. What is the Recognition Problem, what is known, and what does its short-root answer look like?</summary>

Given a model S = G/P of Picard number 1, and a uniruled projective manifold X of Picard
number 1 whose VMRT at a *general* point is projectively congruent to that of S — is X ≅ S?
Solved affirmatively for P corresponding to a **long simple root** (Mok 2008 for the Hermitian
symmetric and contact cases; Hong–Hwang 2008 for the rest). For **short** roots the space of
minimal rational curves through a point need not be homogeneous — the symplectic Grassmannian
has two types of minimal rational curve — and Hwang–Li (*JDG* 119, 2021) get the structure only
up to a **finite** list of candidates indexed by the rank of a bilinear form; a maximal-rank
non-degeneracy condition then picks out the symplectic Grassmannian.
</details>

<details>
<summary>8. Explain the flat-bundle trick, and what problem it solves.</summary>

Problem: transport a local invariant from a general point to a bad point on a uniruled
projective manifold of Picard number 1, where no canonical metric — hence no metric connection
— exists. Solution: identify the bundle in which the invariant lives. Mok takes the projective
second fundamental form of the VMRTs along a minimal rational curve, a section of
Sym²T* ⊗ N, and computes that this bundle is **flat**. A section of a flat bundle is
determined by its value at one point, so the invariant transports for free. Consequence: the
bad set cannot have codimension 1; it has codimension ≥ 2; **Hartogs** then extends the
geometric structure across it. In the contact case the same works one order up, with the third
fundamental form.
</details>

<details>
<summary>9. Why does the ergodic argument give only "one of the two", and why is that enough?</summary>

Moore's ergodicity theorem gives density of a lattice orbit in G/H for H closed noncompact,
but says nothing about *which* direction a limit can be taken in — so for a regular pair of
boundary faces, only one of the two pulled-back functions is known to lie in the function
space ℱ. It is enough because a *single* such function suffices: it is invariant under the
hyperbolic flow, hence constant on the fibres of the boundary projection; ℱ then contains a
subspace invariant not just under Γ but under all of G₀ (density of ΓH in G₀); and a
G₀-invariant subspace of bounded holomorphic functions that properly contains the constants
must be everything. Existence of one object plus density plus a rigidity theorem gives full
generality.
</details>

<details>
<summary>10. State the talk's final theorem and name the three earlier results its proof consumes.</summary>

Kim–Mok–Seo (*JDG* 131, 2025): for irreducible bounded symmetric domains with
2 ≤ rank(Ω′) < 2·rank(Ω) − 1, and either Ω, Ω′ of the same type or Ω of type III and Ω′ of
type I, every proper holomorphic map is **semi-rigid** — up to automorphisms it is
ι ∘ (F₁ × F₂) with F₁ a standard embedding, F₂ arbitrary, ι totally geodesic isometric; and no
proper map exists at all in the type I → III and type II → I or III cases. The proof consumes
(i) the boundary-component/moduli-map technique going back to Tsai's 1993 theorem, (ii) the CR
rigidity results of Kim and of Kim–Zaitsev, and (iii) Hwang–Li's 2021 solution of the
Recognition Problem for symplectic Grassmannians, plus Mok's own recognition results for
*pairs* (sub-VMRT structures).
</details>

---

## 10. Note on the tutorial process

**The title, and how the brief got it wrong.** My brief supplied the title *"Starting with the
Gauss–Bonnet formula: rigidity phenomena on bounded symmetric domains"*, described as taken
from the recorded lecture's own video title and therefore of reasonable provenance. It is not.
The YouTube oEmbed record for `TYOQ2l6m4gM` returns the title `"ICM 2026 Plenary Lecture -
Ngaiming Mok"` and nothing else — there is no descriptive video title to take. The title in my
front matter is the one spoken twice in the room, once by the introducer ("uniformization
theorems and related results in higher dimensional complex geometry") and once by Mok ("the
title of my talk addresses uniformization theorems"). Gauss–Bonnet does not occur in the
transcript. **Impact: structural, and caught before writing.** Had I built the tutorial around
Gauss–Bonnet and bounded symmetric domains as the announced frame, three of the four movements
would have been misdescribed — movements one, three and four are not about bounded symmetric
domains at all. I rejected the suggested anchor for the same reason, and said so in §2.3.

**Difficulty against reputation: matched, and then some.** Mok is known for complex
differential geometry and rigidity, and that is exactly what the talk is. Unlike Kontorovich
there was no inversion. If anything the reputation *understates* it: the lecture is a
retrospective spanning four sub-fields and forty years, and it moves fast because he is
covering four programmes rather than one result.

**No proceedings paper, and no self-citation from the podium.** Mok's arXiv listing is twelve
papers, most recent 29 January 2024, none of them a write-up of this lecture. I scanned the
transcript for "my survey", "our review", "the paper with", journal names and book titles: he
names collaborators and dates constantly but never once names a place to read the work. The
Bartlett trick — the speaker citing his own review aloud — does not apply here. The two
companions were found by going to his own publication page at `hkumath.hku.hk/~nmok/`, which
lists 62 papers plus four sets of lecture notes with PDFs, and picking the two whose scope
matched the talk's halves. That page, not a search engine, is the thing that made this
tutorial possible.

**How much mathematics survived the captions: formulas 0%, spoken statements about 20%.** This
was a slide talk in a large hall, and the caption track carries **not one equation and not one
displayed statement** — everything symbolic lived on the slides. Of the theorems Mok states
aloud, roughly a fifth arrive with enough hypotheses attached to be usable as stated; the rest
are gestured at by name. What did survive is narrative, attribution, dates, and Mok's own
explanations of *why* he did things — which is the genuinely valuable part, and is absent from
the written sources. Every precise statement in §§3–5 above comes from C1, C2, or a named
primary paper. The two source types are close to complementary.

**Length note.** This runs to about twenty thousand words — longer than the Gaitsgory
tutorial's fourteen thousand, and much longer than the two short model tutorials. The reason
is structural, not padding: Gaitsgory's lecture is one research programme presented twice
(global, then local), whereas Mok's is **four largely disjoint programmes** — Kähler–Ricci
flow and positive curvature, bounded symmetric domains and ergodic theory, VMRT geometry, and
subvariety rigidity — each with its own vocabulary, its own bridge section, and its own set of
theorems. §3 has to build two independent toolkits (complex-analytic and algebro-geometric)
because §4 uses both. I trimmed rather than truncated; nothing in the walkthrough was dropped,
and no movement was compressed to save effort.

**Name corrections.** Verified against C1, C2, the Hong–Mok *Selecta* bibliography, the
Kim–Mok–Seo bibliography, Mok's own publication page, or arXiv, unless marked otherwise.

| Caption | Correct | Source |
|---|---|---|
| "Naming Mock" / "Professor Mark" | **Ngaiming Mok** | speaker |
| "Reman, Klene, Pankare, Kerber" | **Riemann, Klein, Poincaré, Koebe** | standard |
| "federico and ease" | **Federigo Enriques** (the classification is Castelnuovo–Enriques) | standard |
| "kunhiko or kodara", "kodara dimension" | **Kunihiko Kodaira**, **Kodaira dimension** | standard |
| "Franco conjecture" / "generalized triangle conjecture" | **Frankel conjecture** / **generalized Frankel conjecture** | C2, [Mk88] |
| "cartoon conjecture" | **Hartshorne conjecture** | C2, [Mr79] |
| "empess of the tangent bundle" | **ampleness of the tangent bundle** | Mori 1979 title |
| "Mori", 1979 | **Shigefumi Mori**, *Ann. Math.* 110 (1979) 593–606 | C2, [Mr79] |
| "su yao", 1980 | **Siu–Yau** (Yum-Tong Siu, Shing-Tung Yau) | talk + standard |
| "Yamong Su" | **Yum-Tong Siu** | talk context |
| "kala rich flow" | **Kähler–Ricci flow** | standard |
| "bees theorem on hologamy" | **Berger's theorem on holonomy** *(reconstructed)* | — |
| "toll in 1989" | **To**, 1989 | C1 slide 1 ("Mok 87, To 89") |
| "in the sense of griffith" | **in the sense of Griffiths** | C1 slide 1 |
| "car matrix", "cartial dorometric" | **Carathéodory metric** | C1 slides 13–14 |
| "Modicity theorem", "more aodicity" | **Moore's ergodicity theorem** | C1 slide 8 |
| "Kurani and Fenbach" | **Korányi** (1976) + one unidentified name | C1 slide 44 |
| "chu and yao and yao and myself" | **Cheng–Yau**, and **Mok–Yau** *(reconstructed)* | — |
| "reman extension theorem" | **Riemann extension theorem** | standard |
| "quinong" | **Kwok-Kin Wong** | Mok's publication page, "Mok, N. & Wong, K.-K." |
| "crazy projective" / "quite projective" | **quasi-projective** | context |
| "Quebec has proved… in 2002" | **Stefan Kebekus**, *J. Alg. Geom.* 11 (2002) | C2, [Ke02] |
| "Jim Huang" / "Jim Muang" / "Jim Hua" | **Jun-Muk Hwang** | C2, all [HM] entries |
| "GMAP P", "gimm", "GM of P" | **G/P** | C2 |
| "pick / pean / picon number" | **Picard number** | C2 |
| "sac batting" | **Segre embedding** | C1 slide 53 |
| "plug embedding" | **Plücker embedding** | C1 slide 53 |
| "renesian embedding" | **Veronese embedding** | C1 slide 53 |
| "lranging / lranjen grasman" | **Lagrangian Grassmannian** | C1 slide 53 |
| "of hard extension" | **Hartogs extension** | C2 §3.2 |
| "long route in the dinken diagram" | **long simple root in the Dynkin diagram** | C2, Thm 3.2.1 |
| "Hong and Huang" (long-root recognition) | **Hong and Hwang**, 2008 | C2, [HH08] |
| "horosphere / horoscopical varieties" | **horospherical varieties** | C2, [PP10] |
| "wonderful comparifications" | **wonderful compactifications** | standard |
| "Hang and Lee Chief Lee", 2021 | **Hwang and Qifeng Li**, *JDG* 119 (2021) | Kim–Mok–Seo, [HwL21] |
| "Maria Waters and Robert Bryan" | **M. Walters** (thesis, Michigan 1997) and **Robert Bryant** | Hong–Mok refs [37], [5] |
| "Boral and Havla in 1961" | **Borel and Haefliger**, 1961 *(reconstructed)* | — |
| "Robless and Tay in 2012" | **Robles and The**, *Selecta Math.* 18 (2012) | Hong–Mok ref [34] |
| "yunin jang" | **Y. Zhang** (Mok–Zhang, *JDG* 112 (2019)) | C2, [MZ15] |
| "thickening lammer" | **Thickening Lemma** | C2, Thm 4.5.3 |
| "eastern tai" / "the time u tai" | **I-Hsun Tsai**, *JDG* 37 (1993) | C1 slide 58 |
| "Kim and size", "Kim with Zaitf" | **Sung-Yeon Kim** and **Dmitri Zaitsev** | Kim–Mok–Seo, [KZ13], [KZ15] |
| "Saul in 2015" | **Aeryeong Seo**, *Michigan Math. J.* 64 (2015) | Kim–Mok–Seo, [S15] |
| "adakdong" (classification of BSDs) | **É. Cartan** *(reconstructed)* | C1 slide 56 |
| "ziggo upper half plane" | **Siegel upper half-plane** | C1 slide 57 |
| "billion varieties" | **abelian varieties** | context |
| "kala geometry" | **Kähler geometry** | standard |
| "le algebbras" | **Lie algebras** | standard |
| "bound holoic / boundomoric functions" | **bounded holomorphic functions** | C1 throughout |
| "erodic / erodically / latis" | **ergodic / ergodically / lattice** | standard |
| "Fahua and Jim Hua and Liy" | **Fu, Hwang and Li** *(reconstructed, unverified)* | — |

**Substantive caption errors corrected in the text, not just spellings.** Four:

- **"locally reducible of rank at least equal to two"** in the statement of the corollary to
  Hermitian metric rigidity → the hypothesis is **irreducible** (C1 slides 1–3 and every
  published version). The caption states the opposite of the hypothesis, and the theorem is
  false as captioned.
- **"C0s"** throughout movement three → **𝒞_x**, the VMRT. Not a name, a symbol.
- **"of hard extension"** → **Hartogs extension**. This is not cosmetic: the whole
  codimension-1-to-codimension-2 argument of §4.3.5 exists in order to invoke Hartogs, and
  without the correct word the argument has no punchline.
- **"the sig betting"** occurs twice with two different meanings. The first is the **Segre
  embedding** (the VMRT of a Grassmannian). The second, in "this is a question that I raised
  and which is called the sig betting", is a garble of what he names in his very next sentence:
  **the Recognition Problem**. I used his next sentence rather than guessing at the garble.

**Reconstructed, and what would verify each:**

- **Berger's holonomy theorem** as the third ingredient of the 1988 proof. The captions say
  "bees theorem on hologamy in Riemannian geometry" and neither companion discusses the 1988
  proof's internals. Verify by reading §§5–6 of *J. Differential Geom.* 27 (1988), 179–214.
- **Cheng–Yau and Mok–Yau** for complete Kähler–Einstein metrics on bounded domains of
  holomorphy. Captions: "chu and yao and yao and myself". The attribution is standard and Mok
  says "yao and myself", so Mok–Yau is certain; Cheng–Yau is the natural reading of "chu and
  yao". Verify against Mok–Yau 1983, *Proc. Symp. Pure Math.* 39.
- **Borel–Haefliger 1961** as the source of the smoothability question. Captions: "Boral and
  Havla in 1961". The year and subject match "La classe d'homologie fondamentale d'un espace
  analytique", Bull. SMF 89 (1961) exactly; it is not in either companion's bibliography, so
  it is an identification from context, not a citation I checked.
- **É. Cartan** for the classification of bounded symmetric domains. Captions: "adakdong". C1
  slide 56 says "E. Cartan's realizations in the classical case", which supports the
  identification but is not the same sentence.
- **Fu, Hwang and Li** for recent work on horospherical varieties and wonderful
  compactifications. Captions: "work of Fahua and Jim Hua and Liy". Jun-Muk Hwang is certain
  from context; Baohua Fu and Qifeng Li are the natural reading and both work in this exact
  area, but I did not verify a joint paper. Treat as unverified.
- **The table in §2.2** (the Riemannian/VMRT dictionary). Layout mine; every row is spoken
  aloud by Mok in the passage quoted immediately above it, and every row is independently
  supported by C2's opening paragraphs.
- **Exercise 6.1(a)–(b)**. My computation. C1 slide 14 asserts the sup-norm formula for Δⁿ; the
  Schwarz-lemma derivation and the parallelogram-law argument are mine and are checkable in
  ten lines.

**Could not verify:**

- **The second name in "Korányi and Fenbach"** (§5, step 2). Korányi is certain and C1 slide 44
  cites "Koranyi 1976" alone for exactly this result. The second name is not recoverable from
  the captions and I would not guess: Korányi has standard joint work with Vági (Hardy spaces
  on bounded symmetric domains) and with Wolf (Cayley transforms), and either would be a
  plausible pairing, which is precisely why I have not asserted one.
- **Mok's endowed chair.** The introducer names it and the captions render it "the Edmund and
  Peggy C professor in mathematics". I could not confirm the full name from any source I could
  reach, so I have omitted it rather than complete it.
- **The 2012 attribution for the ball-embedding result.** Mok says "I prove in 2012 that this
  is a holomorphic isometric embedding of the ball", referring to the union of minimal rational
  curves through a regular boundary point intersected with Ω. His 2012 paper is "Extension of
  germs of holomorphic isometries up to normalizing constants with respect to the Bergman
  metric", *J. Eur. Math. Soc.* 14 (2012), 1617–1656, and the closely related statement appears
  in his 2018 *Contemp. Math.* paper "Full cones swept out by minimal rational curves on
  irreducible Hermitian symmetric spaces…". I did not confirm which paper contains the exact
  statement, so I described the result without pinning it to a reference.
- **The name of the projection onto a boundary face** ("ka projection" / "KD projection"). See
  the gap note in §5.
- **The precise hypotheses of the 2026 Isomorphism Theorem.** The Mok–Wong paper is not on
  arXiv; only the 2007 version is restorable. See the gap note in §4.2.1.
- **"recently elected to the Chinese Academy of Sciences"** (the introducer). Public sources
  give 2015 for the election, and 2009 for the Stefan Bergman Prize, which the introducer also
  mentions. The word "recently" is the introducer's, not Mok's, and I have not repeated it.

**Gaps marked in place, and how bad they are.** Four, rated:

1. **The statement of Mok's 1988 structure theorem** (§4.1). **Low impact.** The theorem's
   shape is stated and is all the rest of the talk uses; the precise list of factors is in the
   1988 paper.
2. **The precise hypotheses of the 2026 Isomorphism Theorem** (§4.2.1). **Moderate impact.**
   The novelty of the new work is exactly the weakening of hypotheses, and I can only give you
   the 2007 version plus a qualitative account of what changed.
3. **What the VMRT of F₅ jumps to** (§4.3.3). **Low impact.** The mechanism — deformation
   rigidity fails because the VMRT is not rigid — is intact.
4. **The name of the boundary-face projection** (§5). **Low impact.** The object is
   unambiguous.

Beyond these I did **not** attempt to teach three things, and the omissions are deliberate:
Ochiai's theorem on G-structures and the theory of G-structures generally; the exterior
differential systems formulation of Schubert rigidity (Kostant forms, the Schur versus
Schubert differential systems); and the Lie-theoretic classification machinery — marked Dynkin
diagrams, sub-diagram type, admissible pairs — that indexes most of movements three and four.
Each appears as a fact with its motivation and its consequence and no more. They are not
learnable in a tutorial, and faking them would produce exactly the smooth fabrication that is
worse than an acknowledged hole.

**One place a companion beats the talk.** Mok states Tsai's theorem from the podium for
domains "of the same rank"; C1 slide 58 states it in the stronger form Tsai actually proved —
rank(D′) ≤ rank(D) as a *hypothesis*, with rank(D) = rank(D′) part of the *conclusion*. I
quoted C1. Similarly the talk states the 2004 embedding theorem in its equivariant form only;
C1 gives both forms, and I gave both.

**One place the talk beats the companions.** Everything about *why*. The problem-based
methodology, the flat-bundle insight told as a story about giving up on holonomy, "minimal
rational curves as carriers of information", "the existence of one single such function is
good enough", and the Riemannian/VMRT dictionary are all in the transcript and in neither
written source. That is the material that makes the mathematics comprehensible, and it exists
nowhere but on this recording.


