---
title: "Local and global Langlands conjecture(s) over function fields"
speaker: Dennis Gaitsgory (Max Planck Institute for Mathematics, Bonn)
source: https://www.youtube.com/watch?v=aeZ0TpVvM5w
video_id: aeZ0TpVvM5w
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2509.24902
transcript: ../transcripts/aeZ0TpVvM5w_transcript.txt
difficulty_for_you: 5/5 (the local half) — 4/5 (the global half)
reading_time: ~75 min
---

# Local and global Langlands conjecture(s) over function fields — Dennis Gaitsgory

**Field:** geometric Langlands, over function fields. Algebraic geometry, derived algebraic
geometry, and higher category theory, aimed at one very old and very concrete question in
number theory.

**Difficulty against your background: 5 out of 5, split.** The first half — the global
unramified story — is a hard but crossable 4. The speaker deliberately slowed down for it,
and its skeleton is four statements you can hold in your head at once. The second half —
the local theory — is the full 5: it runs in 2-categories, and the objects there have no
counterpart anywhere in your training. This is the hardest talk in the playlist, and unlike
Kontorovich it is hard for exactly the reason its reputation predicts.

The speaker says so himself, twice. At the opening:

> "It may be too technical the way I prepared it. So I'll go twice as slow, three times as
> slow as planned and I might not be able to cover even the third of what's in the slides."

And at the half-hour mark:

> "If you understood some parts of it, I'm already very happy… don't feel bad if you don't
> understand the sequel."

That is a plenary speaker telling a room full of professional mathematicians not to expect
to follow. Calibrate accordingly. The goal of this tutorial is not to make you able to do
this mathematics. It is to make you able to read the shape of it — what the question is,
what the answer looks like, and what the three-step method is that gets from one to the
other. That method is the transferable part, and it is genuinely good.

**Prerequisites this tutorial builds:** counting points over a finite field; what a local
system is (monodromy of a linear ODE, in the algebraic setting); Grothendieck's
functions–sheaves dictionary; the categorification ladder and why the categorical trace
walks down it; singular support as a wavefront set; the nilpotent cone; the difference
between functions and densities on a singular space; what a stack is, in one paragraph.

**A note on sources.** This is the good case. There is a genuine ICM proceedings paper —
[arXiv:2509.24902](https://arxiv.org/abs/2509.24902), "Local and global Langlands
conjecture(s) over function fields", Dennis Gaitsgory, posted 29 September 2025, whose
abstract opens "This is a write-up for the plenary ICM talk, 2026". The paper is three
sections plus an appendix and follows the talk's order almost exactly.

That matters more here than in any other talk in this set, because **the auto-captions
carry not a single formula.** This was a slide talk with dense notation, and the caption
track contains none of it. Every displayed formula, every conjecture statement, and every
numbered result below comes from the paper. Where the talk says something the paper does
not, or says it differently, I say which one I am quoting. Where I could restore nothing, I
mark the gap in place.

The talk numbers its results Conjecture 1 through Conjecture 7. The paper numbers them by
section. **The mapping between the two is my reconstruction**, made from the order of
presentation and the content of each statement; the speaker never reads a paper section
number aloud. It is given in full in §4.15 and I use it throughout.

---

## 1. What is at stake

Robert Langlands asked one question. It has a one-line statement and no known answer.

You have a space of **automorphic functions** — a concrete, down-to-earth vector space of
functions on a set. Acting on it is a commuting family of operators, the **Hecke
operators**. Separately, and apparently unrelatedly, you have the **spectral side**: a
collection of algebraic gadgets called Langlands parameters, which in this setting are
**local systems** — representations of a fundamental group into a group Ǧ.

Langlands' question: **describe the space of automorphic functions in terms of the spectral
side.**

The paper's opening sentence is exactly this:

> "The goal of this paper is to propose a set of conjectures whose aim is to answer the
> basic question of the Langlands program (over function fields): how to describe the space
> of automorphic functions in terms of the spectral side (i.e., Langlands parameters)?"

Note the word *propose*. This is not a talk announcing a proof. It is a talk announcing
what the correct **statement** is — and the whole drama is that finding the correct
statement took fifty years, three failed attempts, and the invention of several new
branches of algebraic geometry. The obvious guess is false. The second guess is false. The
third guess is false. The fourth guess is Conjecture 7, and it is false-looking too until
you see what each of the three corrections was fixing.

Gaitsgory has a running joke that organizes the whole hour, and it is the best teaching
device in the talk. Each successive guess gets an epoch:

| Epoch | What it proposes |
|---|---|
| **Stone Age** | Automorphic functions = a direct sum of one-dimensional eigenspaces, one per parameter |
| **Early agricultural** | Automorphic functions = regular *functions* on the parameter space |
| **Industrial** | Sheaves get a singular-support restriction; QCoh becomes IndCoh |
| **Post-industrial** | The same corrections, one categorical level up, for the local theory |

Everything below is the story of why each epoch had to end.

**One thing to fix before you start: "function fields".** In classical number theory you work
over ℚ and its rings of integers. There is a second world that behaves almost identically
and is far more tractable: instead of ℚ, take the field of rational functions on an
algebraic curve *X* over a finite field 𝔽_q. Primes become points of the curve. The whole
Langlands program has a mirror image there, and — crucially — that mirror image has
*geometry*, because a curve is a geometric object and ℚ is not. The talk lives entirely in
that mirror. That is what "over function fields" means, and it is why algebraic geometry is
allowed in the room at all.

---

## 2. Your anchor: this is a Fourier transform

You do not need to reach for an analogy. The speaker hands you one, and it is exactly the
right one:

> "So, what's relevant here is really ℤ and 𝔾_m, and we talk about some algebraic version
> of Fourier transform. And in general, the phenomenon of Langlands correspondence should
> be seen as some sort of non-abelian Fourier transform."

That is the anchor, in his words, from the podium. The Langlands correspondence is a
spectral decomposition. You have a vector space with a commuting family of operators acting
on it (Hecke operators), and you want to diagonalize. The space of joint eigenvalues is the
"frequency domain". Langlands' insight was that the frequency domain is not some
featureless index set — it is a space of **Galois representations**, an object from an
entirely different subject.

You know this move cold — Fourier series, the spectral theorem, Plancherel. The Langlands
correspondence is that statement for a wildly non-abelian group, where the frequency domain
has to be discovered rather than written down.

**Three things go wrong relative to your Fourier intuition, and the whole talk is about
fixing them.**

1. **The frequency domain was not known.** For fifty years nobody knew what algebro-geometric
   object should carry the Langlands parameters. §4.2 is where it gets defined.
2. **You cannot decompose into a direct sum of eigenlines.** This is the Stone-Age failure,
   and its cause is one you have met: a continuous spectrum has no eigenbasis. §4.1.
3. **"Functions on the frequency domain" is the wrong recipient.** The right one is
   *densities*, not functions — sections of the dualizing sheaf ω rather than of the
   structure sheaf 𝒪. On a smooth space with a chosen volume form those agree. The
   parameter space here is not smooth. §3.7 and §4.4.

**One thing to set aside.** You might expect the physics route in — Kapustin–Witten,
electric–magnetic duality, S-duality of N=4 super Yang–Mills, which is a genuine and famous
bridge into geometric Langlands. **The talk never mentions it, not once.** No gauge theory,
no branes, no mirror symmetry. Using it here would be decorating the talk with someone
else's picture. I am naming it only so you know it exists and know it is absent.

A second, quieter anchor is worth flagging now because it becomes the engine of the whole
argument in §5: the **trace**. Gaitsgory's central technical device is the categorical trace
of Frobenius, and it is a direct categorification of two things you own — the ordinary trace
of a matrix, and the **Lefschetz fixed-point formula**, which says that a trace on
cohomology counts fixed points. Grothendieck's whole point-counting machine over finite
fields is the Lefschetz formula. So is Selberg's trace formula, which you met as the
analogue of Gutzwiller's. Keep "trace = sum over fixed points" in your hand; you will need
it in §3.5.

---

## 3. The bridge

Seven ideas. Each is defined by deforming something you already have. Everything else in
the talk gets one sentence at the point of use, because you cannot learn it in an afternoon
and you do not need to.

### 3.1 Counting solutions over a finite field, and the functions that result

Fix a finite field 𝔽_q with q elements. Take some system of polynomial equations. The set of
solutions with coordinates in 𝔽_q is *finite*, and counting it is the basic act of the
subject.

To get at more, you also look at solutions over the algebraic closure 𝔽̄_q — an infinite
set. There is a distinguished symmetry of 𝔽̄_q that fixes 𝔽_q pointwise: the map
x ↦ x^q, the **Frobenius**. It generates (topologically) the Galois group of 𝔽̄_q over 𝔽_q.
And an element of 𝔽̄_q lies in 𝔽_q exactly when Frobenius fixes it.

So: **the 𝔽_q-points are the fixed points of Frobenius on the 𝔽̄_q-points.** Every
"counting" statement becomes a "fixed point" statement, and that is why traces appear
everywhere. Hold this; it is the hinge of the entire talk.

The talk's first move is exactly this. Take *X* a smooth complete curve and *G* a reductive
group (the speaker says immediately: "think about GL_n, the group of matrices"; you should
too, everywhere below). Form the moduli object **Bun_G** classifying G-bundles on X — for
GL_n, rank-n vector bundles on the curve. Take its 𝔽_q-points: this is the set of
isomorphism classes of such bundles defined over 𝔽_q. It is infinite but countable, and
completely discrete.

**Then take the vector space of finitely-supported functions on that set.** That is the
space of automorphic functions:

> Autom(X, G) := Funct_c( Bun_G(𝔽_q) )

That is it. The central object of the entire subject is "functions with finite support on a
countable set". Everything hard is in the structure on it, not in the object.

### 3.2 What a stack is, in one paragraph

Bun_G is not a variety and not a scheme. It is a **stack**, and here is the whole content of
that word for your purposes: a moduli object whose points have automorphisms, and which
remembers them.

Concretely: a vector bundle on a curve has a nontrivial automorphism group (at minimum,
scaling). If you form the naive set of isomorphism classes you throw that away, and the
resulting object has bad geometric properties — it is not a variety, families over it do not
glue. A stack keeps the automorphism groups as part of the data. The simplest example, and
one the talk uses constantly, is **pt/H**: a single point with a group H worth of
automorphisms. Sheaves on pt/H are exactly **representations of H**. You will see
`pt/L(G)(𝔽_q)` several times below; it means nothing more than "the place where
representations of that group live".

If you want a picture from your own training: an orbifold is a manifold that remembers the
finite stabilizers of a group action. A stack is that idea, without the finiteness and
without the manifold.

The speaker's own version: "It's not quite a scheme, it's not algebraic variety, it's what's
called a stack. Slightly fancier version of schemes."

### 3.3 Local systems: monodromy, and why the coefficients must change

A **local system** on a space is a locally constant sheaf of vector spaces — equivalently, a
vector bundle with a flat connection, equivalently a representation of the fundamental
group. You already own the analytic version: take a linear ODE with periodic or
multiply-connected domain, carry a solution basis around a loop, and you come back to a
different basis. The matrix relating them is the **monodromy**. The assignment
loop ↦ monodromy matrix is a homomorphism π₁ → GL_n. That homomorphism *is* the local
system. Floquet theory is this in one dimension.

Algebraic geometry has its own fundamental group — the **étale** fundamental group, built by
Grothendieck in the 1960s from finite covering spaces rather than loops. (The transcript
credits "Grothendieck and Ray"; this is almost certainly Grothendieck and Raynaud, SGA 1 —
see the process note. The paper does not name anyone here.) It is a **profinite** group: an
inverse limit of finite groups, and therefore compact and totally disconnected, like the
p-adic integers.

The spectral side of Langlands is the set of continuous homomorphisms

> π₁^arith(X) → Ǧ(coefficients)

where **Ǧ is the Langlands dual group** of G. You can treat that as a black box: the talk
tells you to, and gives the only case you need — *if G is GL_n, then Ǧ is also GL_n.* So for
your purposes, the spectral side is "n-dimensional representations of the fundamental group
of the curve".

**Now: why ℚ̄_ℓ and not ℚ.** This is a genuine detail with a clean reason, and the talk gives
it. The source of the homomorphism is profinite. If you want *continuous* homomorphisms to
mean anything, the target must have a compatible topology. ℚ with the discrete topology
gives you almost nothing. So you replace the coefficient field ℚ by ℚ̄_ℓ — the algebraic
closure of the ℓ-adic numbers, for a prime ℓ different from the characteristic. ℚ_ℓ is the
completion of ℚ in the ℓ-adic metric, exactly parallel to how ℝ is the completion in the
usual one; it carries a profinite-compatible topology, so continuity has content. The whole
subject is built over ℚ̄_ℓ for this one reason and no other. The talk:

> "We want to give the target also pro-finite topology. And for that reason, we have to take
> coefficients to be, well, something that has something pro-finite inside. And this is
> ℚ̄_ℓ or ℚ_ℓ. So that's why this change is necessary."

The automorphic side changes coefficients to match: functions valued in ℚ̄_ℓ rather than ℚ.

### 3.4 Grothendieck's dictionary: how a sheaf becomes a function

This is the single most important piece of machinery in the talk, and it is beautiful.

A **sheaf** on a space, for present purposes, is a rule that assigns a vector space (really a
complex of vector spaces) to each point, varying algebraically. If your space is defined over
𝔽_q, Frobenius acts on the whole picture, and in particular acts on the vector space sitting
over each 𝔽_q-point.

Now do the obvious thing: **at each 𝔽_q-point, take the trace of Frobenius acting on that
point's vector space.** You get a number. Ranging over all 𝔽_q-points, you get a *function*
on the finite (or countable) set of 𝔽_q-points.

That is the **functions–sheaves dictionary**. It converts a geometric object (a sheaf, which
lives over 𝔽̄_q and has actual geometry) into an arithmetic object (a function on a discrete
set of 𝔽_q-points). In the paper it is the map ℱ ↦ funct(ℱ, α), where α : ℱ → Frob_*(ℱ) is
the extra structure that lets Frobenius act (a "weak Weil structure").

The talk calls this "another main contribution of Grothendieck", which is fair.

**Why it matters strategically:** the automorphic side is functions, which is a poor object
with little structure. The category of sheaves is rich — it has functors, adjoints, duality,
gluing. So the plan is: prove the theorem upstairs, in sheaves, then push it down the
dictionary to get the statement about functions. That plan is the entire architecture of
this talk.

### 3.5 The categorification ladder, and trace as the down-arrow

Here is the structural spine. There is a hierarchy:

| Level | Object | Example |
|---|---|---|
| 0 | a number | 7 |
| 1 | a vector space | ℚ̄_ℓ^7 |
| 2 | a category | the category of vector spaces |
| 3 | a 2-category | the category of categories |

Going *up* is called categorification: replace numbers by vector spaces whose dimensions are
those numbers, replace vector spaces by categories whose objects are those vectors, and so
on. Going *down* needs an operation. **The operation is the trace.**

Start with what you know. Let V be a finite-dimensional vector space and T : V → V linear.
The trace is Σ T_ii. But there is a definition with no basis in it, and the talk gives
exactly this one:

> ℚ̄_ℓ --unit--> V ⊗ V* --T ⊗ id--> V ⊗ V* --evaluation--> ℚ̄_ℓ

The composite is a linear map from the ground field to itself, i.e. multiplication by a
scalar. **That scalar is the trace.** (Exercise 6.2 asks you to verify it.)

Now notice what that definition used. It used a tensor product, a unit object, an object
with a dual, and evaluation maps. It never used numbers, bases, or finite dimension. So it
runs verbatim in **any symmetric monoidal category** — any setting where you can tensor
things together. Feed it a *category* with an endofunctor instead of a vector space with an
endomorphism, and you get out a *vector space*. Feed it a 2-category with an endofunctor and
you get out a category.

> **The trace walks one rung down the ladder.**

The talk states this and then names the classical shadow: for a category of modules, this
trace is **Hochschild homology**. And when the endofunctor is Frobenius, the trace is the
categorified Lefschetz fixed-point formula. The paper's Lemma-level computations make this
completely explicit and they are the two facts you actually need:

> **(Lemma 1, paper §1.5.2)** For a prestack 𝒴 with an endomorphism φ:
> Tr(φ_*, QCoh(𝒴)) ≅ Γ(𝒴^φ, 𝒪) — *the ring of functions on the fixed-point locus.*
>
> **(Lemma 2, paper §1.5.2)** Tr(φ_*, IndCoh(𝒴)) ≅ Γ(𝒴^φ, ω) — *sections of the dualizing
> sheaf on the fixed-point locus.*

Read Lemma 1 in plain English: **the trace of an endomorphism, taken on the category of
sheaves, is the functions on the fixed points.** That is the Lefschetz formula with the
words rearranged, and it is the engine of everything below.

### 3.6 Singular support is a wavefront set

The talk refuses to define this ("I'm not going to define what it is. Again, it's too
technical"), but you have the right background for it and the paper gives the definition, so
here it is.

You know wavefront sets. Given a distribution on a manifold, its singular support tells you
*where* it fails to be smooth; Hörmander's wavefront set refines this to tell you *in which
codirections* it fails, and therefore lives in the cotangent bundle T*M, not in M. It is
conical: scaling a covector does not change whether you are singular in that direction.

Sheaves have exactly the same invariant. Following Beilinson, to a constructible sheaf ℱ on
a stack 𝒴 one assigns a conical subset

> SingSupp(ℱ) ⊂ T*(𝒴)

measuring the codirections in which ℱ fails to be locally constant. Run it backwards:
given a conical subset 𝒩 ⊂ T*(𝒴), let Shv_𝒩(𝒴) be the full subcategory of sheaves whose
singular support lies inside 𝒩. You are selecting sheaves by a microlocal condition,
exactly as you would select distributions with wavefront set in a given cone.

Now the specific choice. Take 𝒴 = Bun_G. **Its cotangent bundle is the moduli space of Higgs
bundles** — that is a real theorem, not an analogy, and it is where Hitchin's integrable
system lives. Inside it sits the **global nilpotent cone** Nilp: roughly, the Higgs fields
whose "eigenvalues" all vanish, i.e. the nilpotent ones. It is the zero fibre of the Hitchin
map, and it is Lagrangian.

Then:

> **Shv_Nilp(Bun_G) ⊂ Shv(Bun_G)** — the sheaves on Bun_G whose wavefront set lies in the
> nilpotent cone.

This subcategory is the automorphic side of everything that follows. The talk records its
history: the relevance was noticed long ago, and it returned to prominence about ten years
ago through the work of **David Ben-Zvi and David Nadler**. (The captions attribute the
original observation to "Jean-Pierre Serre… 40 years ago"; the paper's Remark 1.1.8
attributes it to **G. Laumon's** 1987 *Duke* paper. I follow the paper — see the process
note.)

There is a second, equivalent description that the talk skips and the paper gives, and it is
the one actually used in the proofs. Call a sheaf **Hecke-lisse** if applying any Hecke
functor H_V produces something that is lisse (locally constant) in the curve direction.
Theorem 14.4.3 of AGKRRV1 says:

> Shv_Nilp(Bun_G) = Shv_HL(Bun_G)

A microlocal condition and a condition about Hecke operators define the same subcategory.
That is a real theorem and it is the technical foundation of the whole programme.

### 3.7 Functions versus densities: 𝒪 against ω

The last piece, and the one that carries the punchline of Conjecture 1.

On a manifold you learn to distinguish **functions** from **densities**. A function is what
you evaluate; a density is what you integrate. They are sections of different line bundles,
and if you pick a nowhere-vanishing volume form you can identify them — but the
identification is a choice, not canonical.

Algebraic geometry has the same distinction. Functions are sections of the **structure
sheaf** 𝒪. The integrable objects are sections of the **dualizing sheaf** ω, introduced by
Grothendieck in the 1960s; it is the object that makes duality theorems (Serre duality,
Poincaré duality) come out right. On a smooth space of dimension d, ω is the sheaf of top
differential forms — literally the densities. On a singular space it is a derived object and
it is *not* isomorphic to 𝒪.

Two categories of sheaves ride on the same distinction:

- **QCoh(𝒴)** — quasi-coherent sheaves. The default. Behaves well when 𝒴 is smooth.
- **IndCoh(𝒴)** — ind-coherent sheaves. A variant that differs from QCoh precisely when 𝒴 is
  singular, and is built to see the singularities. The talk's gloss: "this modification has
  to do with the fact that this object is not smooth, it's singular, and this modification
  takes into account the singularities. Technically, compact objects are no longer perfect,
  but coherent."

Compare Lemma 1 and Lemma 2 in §3.5 and you see the whole point. QCoh gives you **functions**
on the fixed points. IndCoh gives you **densities**. When the fixed-point space is smooth
these agree. When it is not, they do not, and the difference is the correction that takes
you from the early-agricultural conjecture to the correct one.

One more technical fact from the paper (Remark 1.5.4), because it is the precise reason the
correction is unavoidable here: the arithmetic parameter space LS^arithm is **quasi-quasi-
smooth** — its cotangent fibres have cohomological amplitude [−2, 1] — and it is not
eventually coconnective. Translation: it is singular in a way that goes beyond the mildest
kind, and no choice of volume form is going to save you.

And a fact worth keeping (Remark 1.5.9): as a fixed-point stack, LS^arithm is canonically
**Calabi–Yau**, so over the well-behaved locus ω *does* equal 𝒪 — the two conjectures agree
there. The discrepancy is concentrated on the bad locus, and Gaitsgory says that discrepancy
is a source of **non-temperedness**, which is the classical Langlands word for automorphic
representations that fail the expected size bounds. The correction is not a technicality; it
is where a known classical phenomenon lives.

---

## 4. The talk, rebuilt

The speaker's order, with the mathematics restored from the paper. I flag every place the
two differ.

### 4.1 The Stone-Age conjecture, and how it dies

Start with the naive spectral decomposition. You have a vector space Autom with commuting
Hecke operators. Diagonalize it:

> **Stone Age.** Autom(X, G) ≅ ⊕_σ (a one-dimensional space), one summand for each Langlands
> parameter σ.

"And this is completely false even in the simplest case."

The simplest case: G = 𝔾_m (the multiplicative group, i.e. GL_1) and X = ℙ¹.

- **Left side.** Bun_{𝔾_m} classifies line bundles. On ℙ¹ every line bundle is 𝒪(n), so the
  set of isomorphism classes of 𝔽_q-points is **ℤ**, indexed by degree. So
  Autom = Funct_c(ℤ) — finitely supported functions on the integers. Its dimension is
  countably infinite; a basis is the delta functions δ_n.
- **Right side.** The parameters here are one-dimensional local systems, and the talk says
  the index set is the ℚ̄_ℓ-points of 𝔾_m, i.e. ℚ̄_ℓ^×. (Unpacking why, which the talk leaves
  implicit: ℙ¹ is simply connected, so the arithmetic fundamental group is generated by
  Frobenius alone, and a one-dimensional representation is nothing but the eigenvalue of
  Frobenius — an arbitrary nonzero scalar.) So the proposed right side is a direct sum of
  one-dimensional spaces indexed by ℚ̄_ℓ^×.

Now count. ℚ̄_ℓ^× is **uncountable**, so a direct sum over it has uncountable dimension.
Funct_c(ℤ) has countable dimension. They cannot be isomorphic. The speaker's phrasing: "it's
really unreasonable to take this infinite direct sum."

**Here is the version of that failure you already know**, and it is not decoration — it is
the same phenomenon. A self-adjoint operator with **continuous spectrum has no
eigenbasis**. The position operator on L²(ℝ) has no eigenvectors in the space at all. You do
not decompose L²(ℝ) as a direct sum of eigenlines; you decompose it as a **direct integral**
over the spectrum, which is to say, you replace "sum over eigenvalues" with "functions on
the spectrum". The Stone-Age conjecture is trying to write a direct sum where the spectrum
is continuous.

And the fix is the fix you would make. The talk:

> "This space of compactly supported functions on ℤ is the same as the space of regular
> functions on 𝔾_m."

Funct_c(ℤ) ≅ ℚ̄_ℓ[t, t^{-1}], by δ_n ↦ t^n. Laurent polynomials. **This is Fourier series.**
ℤ is the character group of the circle; functions on ℤ are Fourier coefficients; Laurent
polynomials are the finite Fourier series. Exercise 6.1 makes you do it.

So the correct shape is not a direct sum over the parameter space. It is **the ring of
functions on the parameter space** — which is precisely the direct-integral answer, written
algebraically.

### 4.2 The frequency domain had to be built: LocSys with restricted variation

To write "functions on the parameter space" you need the parameter space to be a space. It
was not. The paper is blunt about it (§1.1.5): "We do not know what the relevant
algebro-geometric object should be that can reasonably be thought of as the moduli stack of
Ǧ-local systems."

The talk's framing is the funniest line in the hour:

> "As society progressed, humans realized that if some objects can be organized in a family,
> they should."

The object that resolves it is the **stack of local systems with restricted variation**,
written LS^restr_Ǧ(X). The talk says it was discovered relatively recently and
independently by **Peter Scholze**, **Xinwen Zhu**, and the authors of the AGKRRV series —
**D. Arinkin, D. Gaitsgory, D. Kazhdan, S. Raskin, N. Rozenblyum, Y. Varshavsky**.

The definition is not a formula but a representability statement, and here it is from the
paper (§1.3.1), because it is the sort of definition that is clearer than it looks. The
prestack LS^restr_Ǧ(X) is defined by what it does to test algebras: for a connective
commutative ℚ̄_ℓ-algebra R, its R-points are the space of

> right t-exact symmetric monoidal functors  Rep(Ǧ) → R-mod(Shv(X))

Read that as: *a local system is exactly a rule that turns every representation of Ǧ into a
sheaf on X, compatibly with tensor products.* That is Tannakian thinking — you recover a
group homomorphism from what it does to representations. It is the same move as recovering a
group from its character table, done properly.

Two facts from the paper you should carry:

- LS^restr_Ǧ(X) is a **formal algebraic stack**, locally almost of finite type, and it is
  **quasi-smooth** (AGKRRV1, Theorem 1.4.5). Quasi-smooth means "derived complete
  intersection" — cut out by equations whose number is right but whose Jacobian may drop
  rank. It is the mildest failure of smoothness, and it is exactly what triggers the QCoh →
  IndCoh correction.
- "Restricted variation" is what makes the object *algebraic* rather than a wild
  moduli-of-representations mess: essentially it is a disjoint union of formal completions
  at semisimple parameters, rather than the whole naive representation variety.

Then the **arithmetic** version is obtained by taking Frobenius fixed points:

> LS^arithm_Ǧ(X) := ( LS^restr_Ǧ(X) )^Frob

and its ℚ̄_ℓ-points are local systems equipped with a Weil structure. It is quasi-compact
(AGKRRV1, Theorem 24.1.4).

### 4.3 Conjecture 1: the answer, with ω

The early-agricultural conjecture would be Autom ≅ Γ(LS^arithm, 𝒪) — regular functions on
the parameter space. For 𝔾_m that gives exactly the right answer, as §4.1 showed. In general
it is still false.

The correct statement, the talk's **Conjecture 1** and the paper's Corollary 1.5.8:

> **Autom(X, G) ≅ Γ( LS^arithm_Ǧ(X), ω )**

Automorphic functions are the **global sections of the dualizing sheaf** on the stack of
arithmetic Langlands parameters. Not functions on it — densities on it.

Read against §3.7: the parameter space is singular, so functions and densities differ; the
right recipient of a Fourier-type isomorphism is the densities; and where the space is
well-behaved the two agree, so the classical picture is recovered on the tempered part.

### 4.4 Theorem 1: what is actually proved

> **Theorem 1 (talk).** Conjecture 1 holds after replacing LS^arithm by the union of *some*
> of its connected components. Conjecturally that is all of them; at present it is known to
> be only some.

The paper is more precise, and here the paper says more than the talk did. Its Theorem 1.4.6
(from **Gaitsgory–Raskin**, [arXiv:2508.02237](https://arxiv.org/abs/2508.02237)) gives the
component-restricted equivalence in general — and §1.4.3 records that the full statement, with
no restriction on components, **is a theorem when the ground field has characteristic 0, and
when G = GL_n over any ground field.** The talk does not mention the characteristic-0 and
GL_n cases. If you take one thing from the talk-versus-paper comparison, take this: the
result is stronger than the talk lets on.

The talk also attributes the theorem to "a series of papers by nine authors" and then
declines to name them, citing jet lag. The AGKRRV series has six authors; Gaitsgory–Raskin
has two. I could not reconcile the number nine and have not guessed at a list.

### 4.5 Going upstairs: the category of sheaves on Bun_G

Now the actual strategy. Autom is a poor object. So access it through a rich one: the
category of ℓ-adic **sheaves** on Bun_G, and come back down via the functions–sheaves
dictionary of §3.4.

The possibility of relating that category directly to local systems was envisaged by
**Beilinson and Drinfeld** — the categorical geometric Langlands program. But their setting
was D-modules, and in the ℓ-adic setting the whole category of sheaves is too big. You must
pass to the subcategory with **nilpotent singular support**, Shv_Nilp(Bun_G), as built in
§3.6.

The talk gives the one case where you can see what the condition means concretely: for
G = 𝔾_m, Bun_G is a Picard stack and the subcategory consists exactly of the **locally
constant** sheaves. That is a real check — locally constant is wavefront-set-zero, and for a
torus the nilpotent cone is the zero section.

### 4.6 Conjecture 2: geometric Langlands, restricted

> **Conjecture 2 (talk) = Conjecture 1.4.4 (paper).**
> Shv_Nilp(Bun_G) ≃ IndCoh_Nilp( LS^restr_Ǧ(X) ), compatibly with the QCoh(LS^restr)-action.

The early-agricultural version would have said QCoh on the right. The industrial version says
IndCoh_Nilp — ind-coherent sheaves with their own singular-support condition, because
LS^restr is quasi-smooth. Note the pleasing symmetry: **a singular-support condition on each
side.** On the automorphic side it is a condition on sheaves over a smooth-ish stack; on the
spectral side it is the coherent-sheaf analogue developed by Arinkin–Gaitsgory.

The known status is Theorem 1.4.6 as in §4.4.

An important structural fact, Theorem 1.4.2 of the paper: **QCoh(LS^restr_Ǧ(X)) acts on
Shv_Nilp(Bun_G)**, and under that action the Hecke functor H_V is tensoring by a tautological
object ℰ_V. This is the precise sense in which "Hecke eigenvalues are Langlands parameters" —
the parameter space acts, and the Hecke operators are the action of specific elements.

> *[Gap: the talk explicitly declines to define Hecke operators — "I'm not going to say what
> Hecke operators are in this talk because it would take me just too long." The paper gives
> only their shape: for each V ∈ Rep(Ǧ), a functor H_V : Shv(Bun_G) → Shv(Bun_G × X), coming
> from the geometric Satake construction. The construction itself (modifications of bundles
> at a point, the affine Grassmannian, the Satake equivalence) is in neither source. If you
> want it you must go to AGKRRV1. Everything below uses only the shape.]*

### 4.7 The trace machine: how Conjecture 2 implies Conjecture 1

This is the part the speaker stops to underline:

> "So, let me just rewind it for a second. So, it may be the most important point in this
> talk."

Three ingredients.

**Ingredient A — the geometric side descends to automorphic functions.** The talk's
**Theorem 3**, the paper's Theorem 1.2.3 (from AGKRRV3, Theorems 0.2.6 and 0.6.8):

> Tr( Frob_*, Shv_Nilp(Bun_G) ) → Tr( Frob_*, Shv(Bun_G) ) --LT^true--> Funct_c(Bun_G(𝔽_q))
>
> **is an isomorphism.**

Read it slowly. Take the category of automorphic sheaves. Take the categorical trace of
Frobenius on it — which by §3.5 produces a vector space. **That vector space is the space of
automorphic functions.** Nothing lost, nothing added.

The subtlety, and it is the reason the singular-support condition exists at all: the map
LT^true out of Tr(Frob_*, Shv(𝒴)) to functions is *almost never* an isomorphism for a general
stack 𝒴. It becomes one after you cut down to nilpotent singular support. The talk says
exactly this. The paper explains the mechanism in §2.2.8: the failure traces back to the
failure of a Künneth formula, and can be repaired by taking the trace in a bigger ambient
2-category (see §4.10 below).

**Ingredient B — the spectral side descends too.** Lemma 1 and Lemma 2 of §3.5, applied to
𝒴 = LS^restr and φ = Frob, whose fixed points are LS^arithm by definition. Plus one fact the
talk omits and the paper supplies (Proposition 1.5.6, from Gaitsgory–Raskin citing
Beraldo–Lin–Reeves): the inclusion IndCoh_Nilp ↪ IndCoh **induces an isomorphism on traces**,
so the Nilp condition costs nothing at this step.

**Ingredient C — Conjecture 2 says the two categories in A and B are the same**, so their
traces are the same, so the two vector spaces are the same. That is Conjecture 1. Three
isomorphisms in a row; the full derivation is §5.

Notice what just happened, because it is the reusable idea: the hard statement (Conjecture 2)
was proved one level up, in categories, where there is enough structure to state an
equivalence. The statement people actually care about (Conjecture 1) is its **shadow**,
obtained by applying a functorial operation. You never prove the shadow directly.

### 4.8 The half-hour mark: ramification

Everything so far is the **unramified** case. Now the harder half.

Fix a point x on the curve (or a finite set of them). Instead of Bun_G, consider
**Bun_G^{level_x}**: G-bundles together with a **trivialization of their restriction to the
formal disc around x**. Adding that rigidification is what "level structure" means, and it is
the direct analogue of level structures in classical modular forms — Γ₀(N) and friends.

Two things change.

1. Bun_G^{level_x} is no longer just a stack; with x nonempty it is a *scheme*, of infinite
   type.
2. It carries an action of the **loop group** 𝔏(G) := G((t)), where t is a local coordinate
   at x. Concretely G with entries in formal Laurent series.

So the space of automorphic functions with level structure —

> Autom(X,G)^{level_x} := compactly supported locally constant functions on
> Bun_G^{level_x}(𝔽_q)

— is not merely a vector space. It is a **representation of the group 𝔏(G)(𝔽_q) = G(𝔽_q((t)))**,
a locally compact group. (The captions render the last phrase as "the slow local field"; it is
the local field 𝔽_q((t)).)

And that changes the question. You cannot ask for an isomorphism of vector spaces any more,
because one side has a group acting and the other does not. The talk:

> "We do not expect that this space is the space of functions or sections of the dualizing
> sheaf on this object, just because it would be comparing apples and oranges."

So: build a representation of that same group **out of the spectral side**, then compare.
Doing that is what the **local Langlands program** is.

### 4.9 The local theory, and the third main point: isocrystals

The local side works over the **formal punctured disc** 𝒟̊ around x rather than the whole
curve, and the naive guess follows the same epochs: representations of the p-adic group
should be equivalent to QCoh, then (industrial correction) **IndCoh**, of the space of local
systems on 𝒟̊.

But something new goes wrong, and the speaker calls it the third main point of the talk.

> **Rep(𝔏(G)(𝔽_q)) is not the right category.**

It is a *full subcategory* of a bigger one, and it is the bigger one that matches the spectral
side. The paper (footnote 13) dates the idea: it occurred to **V. Lafforgue and the author
around 2013**; the talk says "I first realized it discussing with Vincent Lafforgue and then
it was rediscovered by Fargues and Scholze, but in the analytic framework."

The bigger category is sheaves on the space of **isocrystals**:

> Isoc_G := 𝔏(G) / Ad_Frob(𝔏(G))

the quotient of the loop group by **Frobenius-twisted conjugation**, g ↦ h^{-1} g Frob(h).

**Why this object, and why it is bigger.** This is the cleanest piece of reasoning in the
talk and you can check every step.

Start with **Lang's theorem**. Let H be a *connected* algebraic group over 𝔽_q. Then

> H / Ad_Frob(H) ≅ pt / H(𝔽_q)

In words: twisted conjugation has exactly one orbit, and the stabilizer is the finite group
of 𝔽_q-points. Consequently sheaves on H/Ad_Frob(H) are exactly **Rep(H(𝔽_q))** — see §3.2 on
what pt/H means. So for a connected finite-dimensional group, the isocrystal picture and the
representation picture agree, and nothing is gained.

**But the loop group is not a connected algebraic group.** It is an ind-scheme of infinite
type, and **Lang's theorem fails for it.** The point pt/𝔏(G)(𝔽_q) is still there — it sits
inside Isoc_G as a closed subfunctor — but it is not everything. Hence a pair of adjoint
functors

> ι_! : Rep(𝔏(G)(𝔽_q)) ⇄ Shv(Isoc_G) : ι^!

with Rep sitting inside Shv(Isoc_G) as a full subcategory, properly.

Exercise 6.2(b) makes you verify the failure of Lang for the loop group of 𝔾_m in about ten
lines. Do it; it is the one place in this talk where you can touch the mathematics directly.

The talk also gives the *conceptual* reason isocrystals appear, and it is the trace again.
The paper's equation (2.18):

> Tr( Frob, 𝔏(G)-Cat ) ≅ Shv(Isoc_G)

> "This isomorphism may be viewed as an explanation of why isocrystals appear. They appear
> naturally as the recipient of the trace."

That is the talk's best single sentence. The object was not chosen; it was computed.

The paper adds credits the talk does not: a comprehensive study of Isoc_G is due to **X. Zhu**
(*Tame categorical local Langlands correspondence*,
[arXiv:2504.07482](https://arxiv.org/abs/2504.07482)), including the facts that Isoc_G is
"restricted" and that Shv(Isoc_G) is dualizable and self-dual — both of which get used later.

### 4.10 Conjecture 3: the classical local Langlands conjecture

> **Conjecture 3 (talk) = Corollary-of-Conjecture 2.7.9 (paper).**
> Shv(Isoc_G) ≃ IndCoh( LS^arithm_Ǧ(𝒟̊) )

Note the structural difference from the global case, which the speaker points out: globally,
the classical statement was an isomorphism of *vector spaces*. Locally, the classical
statement is an equivalence of *categories*. Local is one rung up the ladder from global.

The paper is careful about attribution here and the talk is not:

- This conjecture was **first proposed by X. Zhu**, as Conjecture 4.6.4 of *Coherent sheaves
  on the stack of Langlands parameters*. (Zhu's tame/depth-0 part of it is established in
  the *Tame categorical* paper above.)
- It is **closely related to the Fargues–Scholze conjecture**,
  [arXiv:2102.13459](https://arxiv.org/abs/2102.13459), Conjecture I.10.2, which states
  D(Bun^local_G) ≃ IndCoh(Param_Ǧ) with Bun^local_G the analytic stack of G-bundles on the
  Fargues–Fontaine curve.
- The two are **equivalent** given two inputs: one can show Param_Ǧ ≅ LS^arithm_Ǧ(𝒟̊), and the
  ongoing work of Gleason–Ivanov–João–Hamann–Zou aims to establish
  D(Bun^local_G) ≃ Shv(Isoc_G). **The second of those is not yet done.** The talk states the
  equivalence flatly; the paper flags that half of it rests on work in progress.

*(The captions render Fargues–Scholze variously as "Fargues-Scholten", "Fargues-Fontaine",
and "Park Shultz". See the process note.)*

### 4.11 Conjecture 4: the local geometric conjecture, in 2-categories

Now the geometric counterpart, one level up again. This is where the talk becomes genuinely
inaccessible without the field, and I will not pretend otherwise. What follows is the shape,
which is all you need.

**The automorphic side** is the 2-category of **categorical representations of the loop
group**: objects are DG categories equipped with an action of 𝔏(G). Notation 𝔏(G)-Cat.
Just as Shv_Nilp(Bun_G) was the global geometric object, this is its local counterpart.

Two corrections are needed, both parallel to corrections you have already seen.

**Correction one: the ambient 2-category has to be rebuilt.** For D-modules there is a
*categorical Künneth formula*: D-mod(Y) ⊗ D-mod(Y′) ≅ D-mod(Y × Y′). That equivalence is
what lets you define a group acting on a category (you need it to make sheaves on the group
into a Hopf object). **For ℓ-adic sheaves it fails.** The paper is emphatic: the analogous
map Shv(Y) ⊗ Shv(Y′) → Shv(Y × Y′) is fully faithful but "is never an equivalence if both Y
and Y′ are positive-dimensional schemes of finite type."

So the entire ambient framework gets replaced. Gaitsgory, Rozenblyum and Varshavsky build a
2-category called **AGCat**, whose objects are not categories but *families of categories over
all affine schemes S* with pullback and pushforward and base change. AGCat is designed to have
exactly the tensor property that failed: Shv(S₁) ⊗ Shv(S₂) = Shv(S₁ × S₂). The paper credits
the idea to **V. Drinfeld, "some 20 years" ago**.

And AGCat is what repairs the trace map of §4.7: the failure of
Tr(Frob, Shv(𝒴)) → Funct(𝒴(𝔽_q)) to be an isomorphism is *precisely* the failure of that
Künneth map, and taking the trace in AGCat instead makes it an isomorphism.

> **One broken tensor identity forced the reconstruction of the entire ambient framework.**
> Keep that; §7.3 is about it.

**Correction two: trim to "restricted".** 𝔏(G)-Cat is tensored over AGCat, but any spectral
counterpart will only be tensored over DGCat. So it is *too big*, and one cuts down to a full
subcategory **𝔏(G)-Cat_restr**. The paper is explicit that this is "loosely analogous" to the
passage Shv(Bun_G) ↝ Shv_Nilp(Bun_G) — the same move, one level up.

> *[Gap: the definition of "restricted" for the loop group is given in the paper only as
> provisional (§2.4.6), by requiring certain 𝔏(N)-invariants to be restricted objects of
> AGCat. The definition the field will actually use comes from the forthcoming work of
> G. Dhillon, Y. Varshavsky and D. Yang using **refined categorical Moy–Prasad theory**, which
> is not yet public. The talk names it; neither talk nor paper states it. Both note it needs
> char(k) > |W|.]*

**The spectral side** needs a 2-categorical version of the QCoh → IndCoh correction. That
theory is due to **D. Arinkin** (about fifteen years ago, per the talk), with an alternative
approach later by **G. Stefanich**. Write 2-QCoh(S) for categories with an action of QCoh(S);
the corrected object is **2-IndCoh_𝒩(S)**, built from a resolution S̃ → S and defined as
modules over a localization of IndCoh(S̃ ×_S S̃).

One technical point worth having, because it explains why the local case is *easier* here than
the global one: the local parameter space LS^restr_Ǧ(𝒟̊) is **formally smooth**, not merely
quasi-smooth, because the relevant sheaf theory on the punctured disc has cohomological
dimension 1. Nilp sits inside its cotangent bundle as a Lagrangian, and the correction is
applied relative to that.

> **Conjecture 4 (talk) = Conjecture 2.6.10 (paper).**
> 𝔏(G)-Cat_restr ≃ 2-IndCoh_Nilp( LS^restr_Ǧ(𝒟̊) )

Very significant progress towards it is the Dhillon–Varshavsky–Yang work.

And then the caveat the talk does not give but the paper does (Remark 2.6.11), which is the
sharpest thing in the paper for your purposes: **DVY establish an equivalence of the two
sides as abstract 2-categories, but both sides carry an extra structure — an action of
QCoh(LS^restr) via the Bernstein centre — and it is not yet known that the equivalence is
compatible with it.** An equivalence that does not respect the structure you care about is not
yet the theorem you wanted. Hold that thought for §7.4.

### 4.12 Conjecture 5: the local trace

The same descent as §4.7, one level up.

> **Conjecture 5 (talk) = Conjecture 2.5.12 (paper).** The natural map
> Tr(Frob, 𝔏(G)-Cat_restr) → Tr(Frob, 𝔏(G)-Cat) ≅ Shv(Isoc_G)
> **is an isomorphism.**

Compare Theorem 3 in §4.7 line by line: cutting down to the restricted subcategory does not
change the trace, and the trace is the classical object. Identical statement, one rung up.

Two status notes from the paper that the talk gives only partially:

- The **finite-dimensional analogue is a theorem**, equivalent to Theorem 6.1.1 of
  **A. Eteve**: Tr(Frob, G-Cat_restr) ≅ Rep(G(𝔽_q)). The talk names this ("a counterpart of
  this conjecture, when instead of the loop group you consider finite dimensional reductive
  group, it's a theorem of Arnaud Eteve").
- Substantial progress on the loop-group case is joint work of **Dhillon, Eteve, Gaitsgory,
  Raskin, Varshavsky and Yang**, and **independently by C. Chan, T. Kaletha and X. Zhu by a
  different method**. *(That last credit is in the paper, §2.5.13; the talk says only "a lot of
  progress has been made toward this conjecture recently".)* The paper adds a nice aside:
  "(un)surprisingly, this statement ended up being much simpler than its global counterpart."

The paper also has an example the talk omits, and it is the best evidence that the machinery
is doing something real rather than shuffling definitions: in the finite-dimensional case, the
"class" construction applied to Shv(G/B)^χ with a Weyl-group twist produces exactly the
**Deligne–Lusztig representation** attached to (χ, w). One of the central constructions of
finite-group representation theory falls out as a special case.

### 4.13 The global ramified case: shtukas, and the enhanced automorphic space

Now combine. Take the category of sheaves on Bun_G^{level_x}, with its 𝔏(G)-action, and cut
down by a condition that plays the role of nilpotent singular support. The talk calls it
"Hecke finite"; the paper's condition is **Shv_HL** — "Hecke-lisse" — recall §3.6: the
sheaves whose Hecke transforms are lisse along the curve. I use the paper's definition
throughout; see the process note on the naming.

> **Conjecture 3.1.5 (paper).** Shv_HL(Bun_G^{level_x}) is a *restricted* object of
> 𝔏(G)_x-Cat, i.e. it lands where Conjecture 4 can be applied to it.

> **The global ramified geometric conjecture — Conjecture 6 (talk) = Conjecture 3.4.4
> (paper).** Under the local geometric equivalence of Conjecture 4,
>
> Shv_HL(Bun_G^{level_x})  corresponds to  IndCoh_Nilp( LS^restr_Ǧ(X̊) | LS^restr_Ǧ(𝒟̊_x) )

where X̊ is the curve with the points removed, and the bar notation means "the object of the
2-category attached to the restriction map LS(X̊) → LS(𝒟̊)". The geometry is exactly what you
would hope: **restricting a local system from the punctured curve to the punctured disc.**
That single map carries all the global information into the local picture.

Now the classical consequence, and here comes the last correction.

The object you would want to describe is Autom^{level_x}, a representation of 𝔏(G)_x(𝔽_q). But
§4.9 said that category is the wrong one. So **enhance the object**: define

> Autom(X,G)^{enh_x} ∈ Shv(Isoc_{G,x})

from which the ordinary Autom^{level_x} is recovered by applying ι^! — the right adjoint of the
embedding in §4.9. You do not lose the object you started with; you place it inside a larger
one where the answer is clean.

**How the enhanced object is built: shtukas.** Define

> Sht_x := Bun_G ×_{(Bun_G × Bun_G)} ℋ_x,   with the map (Id, Frob)

where ℋ_x is the Hecke groupoid at x. A shtuka is a bundle together with a modification at x
relating it to its own Frobenius twist — the function-field replacement for a Shimura variety,
and the object Vincent Lafforgue used to construct global Langlands parameters. The paper's
Remark 3.2.4 gives the slogan: Sht̊_x is (Bun_G(X̊))^Frob. **Fixed points again.**

There is a map π : Sht̊_x → Isoc_{G,x}, given by restricting from X to the disc around x, and
the enhanced automorphic object is built from it.

> *[Discrepancy, both sources quoted. The **talk** says: "we take the constant sheaf on the
> space of shtukas and we take its direct image with compact supports" along π. The **paper**
> (§3.2.5) defines it dually: using the self-duality of Shv(Isoc), it specifies the functor
> ℱ ↦ C_c(Sht̊_x, π^!(ℱ)), and Autom^{enh} is the object corresponding to that functor. I have
> not verified that the talk's phrasing is literally the paper's construction rather than its
> dual, so I give both. What would settle it: unwinding the self-duality of Shv(Isoc_G) from
> Zhu's Proposition 3.82.]*

The paper does verify the compatibility you care about (§3.2.6): pairing Autom^{enh} against
the delta-function object at the identity recovers Autom^{level} exactly, by base change along
a Cartesian square. So the enhancement is a genuine enlargement, not a replacement.

> **Conjecture 7 (talk) = Corollary-of-Conjecture 3.5.9 (paper).** Under the local equivalence
> Shv(Isoc_{G,x}) ≃ IndCoh(LS^arithm_Ǧ(𝒟̊_x)), the object
>
> Autom(X,G)^{enh_x}   corresponds to   (𝔯^arithm)_* ω_{LS^arithm_Ǧ(X̊)}
>
> where 𝔯^arithm : LS^arithm_Ǧ(X̊) → LS^arithm_Ǧ(𝒟̊_x) is restriction from the punctured curve
> to the punctured disc, and the pushforward is the IndCoh one.

The speaker:

> "This conjecture seven in some sense is the ultimate answer to the Langlands program over
> function fields. Langlands asked just describe the space of automorphic functions in terms
> of the spectral side. We can't quite do this. We performed a bunch of modifications, but at
> the end of the day we arrive at this conjecture seven."

**Read the answer in plain language.** Automorphic functions are the pushforward of the
dualizing sheaf, along the map that restricts a Langlands parameter from the punctured curve
to a punctured disc around the ramification point. In Fourier language: the automorphic
spectrum, as seen from the local place x, is obtained by *integrating the global parameter
space over the fibres of the restriction map*. Pushforward is integration along fibres, and
ω is what you are allowed to integrate. That reading is honest — it is exactly what the
formula says.

The talk notes the statement was **independently proposed by Xinwen Zhu**; the paper's
footnote 19 puts it more precisely: "The statement of Corollary 3.5.9 was inspired by a
seminar talk by X. Zhu in 2020."

A last item, in the paper only (Remark 3.5.10), and worth knowing because it links back to a
Fields-Medal-winning theorem: Lafforgue's work equips Autom^{level} with an action of the
**excursion algebra**, which the paper reinterprets as Γ(LS^arithm(X̊), 𝒪) — the *functions* on
the global parameter space. Work in progress with Genestier, Eteve and Lafforgue extends that
action to the enhanced object, where it should become the tautological action of functions on
sections of ω. Functions act on densities. Of course they do.

### 4.14 The ladder, in one picture

**Reconstructed diagram.** The layout is mine; every cell and every arrow is stated in the
talk or the paper.

```
                   AUTOMORPHIC side                       SPECTRAL side          level
LOCAL              𝔏(G)-Cat_restr        ≃ Conj 4 ≃    2-IndCoh_Nilp(LS^restr(𝒟̊))    2
geometric                │                                     │
                         │ Tr(Frob) — Conj 5                   │ Tr(Frob) — Cor 2.7.7
                         ▼                                     ▼
LOCAL              Shv(Isoc_G)           ≃ Conj 3 ≃    IndCoh(LS^arithm(𝒟̊))          1
classical

GLOBAL             Shv_Nilp(Bun_G)       ≃ Conj 2 ≃    IndCoh_Nilp(LS^restr(X))       1
geometric                │                                     │
                         │ Tr(Frob) — Thm 3                    │ Tr(Frob) — Lemma 2
                         ▼                                     ▼
GLOBAL             Autom(X,G)            ≃ Conj 1 ≃    Γ(LS^arithm(X), ω)             0
classical
```

The two rules, both stated by the speaker:

- **Geometric ⇒ classical lowers the categorical level by one**, and the operation that does
  it is Tr(Frob).
- **Global ⇒ local raises it by one.** Globally, classical is a vector space; locally,
  classical is a category.

The horizontal arrows are the Langlands equivalences. The vertical arrows are traces. Every
statement in this talk is one arrow in this diagram, and the method of proof is always the
same: **establish the top arrow, then take traces to get the bottom one.**

### 4.15 Status, and the numbering map

The talk's numbering against the paper's, with what is proved. The mapping is my
reconstruction from order and content; the paper's own numbers and status claims are quoted.

| Talk | Paper | Statement | Status |
|---|---|---|---|
| Conjecture 1 | Corollary 1.5.8 | Autom(X,G) ≅ Γ(LS^arithm(X), ω) | Consequence of Conj 1.4.4 |
| Theorem 1 | via Thm 1.4.6 | The same, over a union of some connected components | **Theorem** |
| Conjecture 2 | Conjecture 1.4.4 | Shv_Nilp(Bun_G) ≃ IndCoh_Nilp(LS^restr(X)) | **Theorem** in char 0, and for GL_n over any field; else up to components |
| Theorem 2 | Theorem 1.4.6 | Conj 2 up to connected components | **Theorem** [GR] |
| Theorem 3 | Theorem 1.2.3 | Tr(Frob, Shv_Nilp(Bun_G)) ≅ Autom | **Theorem** [AGKRRV3] |
| Lemma 1 | §1.5.2 | Tr(φ, QCoh(𝒴)) ≅ Γ(𝒴^φ, 𝒪) | **Theorem** |
| Lemma 2 | §1.5.2 | Tr(φ, IndCoh(𝒴)) ≅ Γ(𝒴^φ, ω) | **Theorem** |
| Conjecture 3 | Cor-of-Conj 2.7.9 | Shv(Isoc_G) ≃ IndCoh(LS^arithm(𝒟̊)) | Conjecture; first proposed by Zhu; tame/depth-0 case done |
| Conjecture 4 | Conjecture 2.6.10 | 𝔏(G)-Cat_restr ≃ 2-IndCoh_Nilp(LS^restr(𝒟̊)) | Conjecture; major progress [DVY], modulo Bernstein-centre compatibility |
| Conjecture 5 | Conjecture 2.5.12 | The local trace isomorphism | Conjecture; finite-dim case is a theorem [Eteve]; two independent partial results |
| Conjecture 6 | Conjecture 3.4.4 | The global ramified geometric conjecture | Conjecture |
| Conjecture 7 | Cor-of-Conj 3.5.9 | The spectral description of Autom^enh | Conjecture; "the ultimate answer" |

The line the talk draws is clean: "from now on it'll be just conjectures, no theorems"
arrives exactly at the ramified case. Everything global and unramified is proved or nearly
proved. Everything local is conjectural and moving fast.

He ends: "And miraculously I've covered all my material. I wasn't even intending to."

---

## 5. The one argument, stated precisely

Strip away the vocabulary and one derivation carries the whole talk. Here it is with every
symbol defined.

**Setup.** X a smooth complete curve over 𝔽_q, G reductive (think GL_n), Ǧ its Langlands
dual (for GL_n, again GL_n). Coefficients ℚ̄_ℓ throughout. Bun_G is the moduli stack of
G-bundles on X. Autom(X,G) := Funct_c(Bun_G(𝔽_q)), the finitely-supported ℚ̄_ℓ-valued
functions on the set of 𝔽_q-points. Shv_Nilp(Bun_G) is the category of ℓ-adic sheaves on
Bun_G whose singular support lies in the global nilpotent cone. LS^restr_Ǧ(X) is the stack
of Ǧ-local systems with restricted variation; LS^arithm_Ǧ(X) is its Frobenius fixed-point
locus. Frob is the geometric Frobenius; Tr(Frob, −) is the categorical trace of §3.5; ω is
the dualizing sheaf.

**Step 1 — descend the automorphic side (Theorem 1.2.3, proved).**

> Tr( Frob, Shv_Nilp(Bun_G) ) ≅ Autom(X, G)

The categorical trace of Frobenius on automorphic sheaves *is* the space of automorphic
functions. The composite is the trace map into Tr(Frob, Shv(Bun_G)) followed by
Grothendieck's local-term map LT^true. Neither factor is an isomorphism on its own; the
composite is.

**Step 2 — the Langlands equivalence one level up (Conjecture 1.4.4).**

> Shv_Nilp(Bun_G) ≃ IndCoh_Nilp( LS^restr_Ǧ(X) )

compatibly with the QCoh(LS^restr)-action on both sides, and — this is what makes Step 3
legal — compatibly with Frobenius, since the construction is canonical and therefore
commutes with base change along Frobenius.

**Step 3 — descend the spectral side (§1.5.2 plus Proposition 1.5.6, proved).**

> Tr( Frob, IndCoh_Nilp(LS^restr_Ǧ(X)) ) ≅ Tr( Frob, IndCoh(LS^restr_Ǧ(X)) )
>                                        ≅ Γ( LS^arithm_Ǧ(X), ω )

The first isomorphism is Proposition 1.5.6 (the Nilp condition is invisible to the trace).
The second is the IndCoh trace formula: the trace of pushforward along φ on IndCoh is the
ω-sections of the fixed-point locus, and the fixed-point locus of Frobenius on LS^restr is
LS^arithm by definition.

**Conclusion (Corollary 1.5.8).**

> **Autom(X, G) ≅ Γ( LS^arithm_Ǧ(X), ω )**

Apply Tr(Frob, −) to Step 2 and splice Steps 1 and 3 onto the two ends. That is the proof.
It is three lines because all the work is in the objects.

**The proof-sketch honesty check.** Steps 1 and 3 are theorems. Step 2 is a theorem in
characteristic 0 and for GL_n over any field, and in general is known after restricting to a
union of connected components. So the conclusion is a theorem in exactly those cases and in
general holds over a union of components.

**And the shape of the whole talk is this derivation, twice more.** Replace (global,
unramified) by (local) and every object goes up one categorical level: Steps 1 and 3 become
Conjecture 2.5.12 and Corollary 2.7.7, Step 2 becomes Conjecture 2.6.10, and the conclusion
becomes Corollary 2.7.9. Replace it by (global, ramified) and you get Conjecture 3.3.3,
Conjecture 3.5.5, Conjecture 3.4.4, and Corollary 3.5.9. **One argument, three times.**

---

## 6. Do this by hand

Two exercises. Between them they touch the two ideas that carry the talk — the Fourier
anchor, and the trace. Both are elementary; neither needs anything from algebraic geometry.

### 6.1 The 𝔾_m case: watch the Stone-Age conjecture die (20 minutes, pen)

Take G = 𝔾_m (so Bun_G classifies line bundles) and X = ℙ¹ over 𝔽_q. Take as given that the
set of isomorphism classes of line bundles on ℙ¹ over 𝔽_q is ℤ, indexed by degree.

1. Write down Autom = Funct_c(ℤ) explicitly, and give a basis.
2. Show Funct_c(ℤ) ≅ ℚ̄_ℓ[t, t^{-1}], the ring of Laurent polynomials, which is the ring of
   regular functions on 𝔾_m. Say what this is in Fourier language.
3. The Stone-Age conjecture proposes ⊕_{σ ∈ 𝔾_m(ℚ̄_ℓ)} ℚ̄_ℓ instead. Give a one-line reason it
   cannot be isomorphic to the answer in (1).
4. State, in your own words, which classical fact from spectral theory this is.

<details>
<summary>Solutions</summary>

**(1)** Funct_c(ℤ) = finitely supported functions ℤ → ℚ̄_ℓ. A basis is {δ_n : n ∈ ℤ}, where
δ_n(m) = 1 if m = n and 0 otherwise. Dimension: countably infinite.

**(2)** Send δ_n ↦ t^n. This is a linear bijection onto the span of {t^n : n ∈ ℤ} =
ℚ̄_ℓ[t, t^{-1}] = 𝒪(𝔾_m), since 𝔾_m = Spec ℚ̄_ℓ[t, t^{-1}]. A finitely supported function on ℤ
is exactly a finite Fourier series: **ℤ is the character group of the circle**, and
"coefficients indexed by ℤ" ↔ "a function on the dual group". This is the discrete Fourier
transform in its cleanest algebraic form, and it is the whole content of the speaker's
remark that "what's relevant here is really ℤ and 𝔾_m."

**(3)** 𝔾_m(ℚ̄_ℓ) = ℚ̄_ℓ^× is **uncountable**. A direct sum of one-dimensional spaces indexed by
an uncountable set has uncountable dimension. Funct_c(ℤ) has countable dimension. No
isomorphism of vector spaces exists. Done.

**(4)** An operator with **continuous spectrum has no eigenbasis**. You cannot write
L²(ℝ) as a direct sum of eigenlines of the position operator — there are no eigenvectors in
the space. The correct decomposition is a **direct integral over the spectrum**, i.e. you
replace "sum over eigenvalues" with "functions on the spectrum". The Stone-Age conjecture
writes ⊕ where the parameter space is a continuum; the early-agricultural fix, 𝒪(parameter
space), is the direct-integral version written algebraically.

**The point of the exercise.** The Hecke eigenvalue for the parameter σ ∈ 𝔾_m is a genuine
continuous parameter. Every subsequent correction in the talk — 𝒪 to ω, QCoh to IndCoh — is a
further refinement of "what exactly do you take on the spectrum". Getting from ⊕ to 𝒪 was the
easy one, and it still took an epoch.

</details>

### 6.2 The trace, and why Lang's theorem fails upstairs (30 minutes, pen)

**(a) The basis-free trace.** Let V be a finite-dimensional vector space over a field k with
dual V*, and T : V → V linear. Consider the composite

> k --unit--> V ⊗ V* --T ⊗ id--> V ⊗ V* --ev--> k

where unit(1) = Σ_i e_i ⊗ e^i for a basis {e_i} and dual basis {e^i}, and
ev(v ⊗ f) = f(v). Compute the composite and confirm it is multiplication by tr(T). Then say
which ingredients of the computation would still make sense if V were a *category* and T a
functor.

**(b) Lang's theorem, and its failure for the loop group.** Frobenius-twisted conjugation on
a group H is the action h · g := h^{-1} g Frob(h).

- Take H = 𝔾_m over 𝔽̄_q, so H(𝔽̄_q) = 𝔽̄_q^× and Frob(x) = x^q. Compute the twisted-conjugacy
  orbits. How many are there, and what is the stabilizer of a point?
- Now take the loop group 𝔏(𝔾_m), whose points are 𝔽̄_q((t))^×, with Frobenius acting on
  coefficients (Frob(Σ a_i t^i) = Σ a_i^q t^i). Find one invariant of twisted conjugacy that
  is not constant, and conclude that Lang's theorem fails.

<details>
<summary>Solutions</summary>

**(a)** Track the element 1 ∈ k. unit sends it to Σ_i e_i ⊗ e^i. Applying T ⊗ id gives
Σ_i T(e_i) ⊗ e^i. Applying ev gives Σ_i e^i( T(e_i) ) = Σ_i T_ii = tr(T). Since a linear map
k → k is multiplication by a scalar, the composite is multiplication by tr(T). ∎

What the computation used: a tensor product, a unit object, an object with a dual, and unit
and evaluation maps satisfying the obvious compatibilities. It did **not** use a basis, the
dimension, or the fact that the entries are numbers. So the same string of arrows defines a
trace in any symmetric monoidal category, for any dualizable object with an endomorphism.
Feed it (category, endofunctor) and out comes a vector space — Hochschild homology. That is
§3.5, and it is exactly what the speaker does from the podium.

**(b) Finite-dimensional case.** For H abelian, h^{-1} g Frob(h) = g · h^{q-1}. So the orbit of
g is g · {h^{q-1} : h ∈ 𝔽̄_q^×}. Since 𝔽̄_q is algebraically closed, x ↦ x^{q-1} is
**surjective** on 𝔽̄_q^×, so the orbit of g is everything: there is exactly **one** orbit. The
stabilizer of g = 1 is {h : h^{q-1} = 1} = μ_{q-1} = 𝔽_q^× = H(𝔽_q). Hence
H / Ad_Frob(H) ≅ pt / H(𝔽_q). **That is Lang's theorem** in the simplest case, and it says
sheaves on the twisted-conjugation quotient are just representations of the finite group
H(𝔽_q).

**Loop group case.** Now g ∈ 𝔽̄_q((t))^× and the orbit is g · {Frob(h)/h : h ∈ 𝔽̄_q((t))^×}.
Key observation: **Frobenius acts on coefficients and does not touch t**, so it preserves the
t-adic valuation: v(Frob(h)) = v(h). Therefore

> v( Frob(h)/h ) = v(Frob(h)) − v(h) = 0   for every h.

So every element of the acting set has valuation 0, and the valuation v(g) ∈ ℤ is
**constant on twisted-conjugacy orbits**. It is a non-constant invariant — v(t) = 1 while
v(1) = 0 — so there is more than one orbit. **Lang's theorem fails.** In fact the valuation
gives a surjection Isoc_{𝔾_m} ↠ ℤ.

**What this shows and what it does not.** It shows exactly the point Gaitsgory makes: the
loop group is not a connected algebraic group, Lang fails, and therefore Isoc_G is strictly
bigger than pt/𝔏(G)(𝔽_q) — so Shv(Isoc_G) is strictly bigger than Rep(𝔏(G)(𝔽_q)). It does
**not** compute Isoc_G. The full classification of isocrystals (Dieudonné–Manin for GL_n,
Kottwitz's B(G) in general) is not discussed in either the talk or the paper.

**Marked as reconstructed:** this computation is mine. Neither the talk nor the paper works
it out; both simply assert that Lang's theorem fails for the loop group. What would verify
it: the assertion v(Frob(h)) = v(h) — check it directly on Σ a_i t^i, whose lowest nonzero
coefficient a_m maps to a_m^q ≠ 0.

</details>

---

## 7. What is actually useful to you

The mathematics here will not transfer to your work. The **method** will, and it is unusually
crisp because Gaitsgory states it as a method rather than leaving it implicit.

### 7.1 When the theorem is false, the object is wrong — not the theorem

This is the strongest transferable idea in the talk, and it is repeated four times without
variation.

Every time a statement fails, Gaitsgory does **not** add an error term, a correction factor,
or a hypothesis. He identifies which object in the statement was the wrong object, and
replaces it:

| Statement fails because… | The object replaced |
|---|---|
| Continuous spectrum, no eigenbasis | ⊕ over parameters ↝ 𝒪(parameter space) |
| Parameter space is singular | 𝒪 ↝ ω, QCoh ↝ IndCoh |
| Trace map isn't an isomorphism | Shv(Bun_G) ↝ Shv_Nilp(Bun_G) |
| Nothing on the spectral side can carry a loop-group action | Rep(𝔏(G)(𝔽_q)) ↝ Shv(Isoc_G) |
| The 2-category is too big for its spectral partner | 𝔏(G)-Cat ↝ 𝔏(G)-Cat_restr |

And the method for finding the replacement is always the same: **take the smallest example
where the statement is false, and read the correct object off the failure.** 𝔾_m on ℙ¹ is a
two-line computation, and it dictates the shape of every conjecture in a sixty-page paper.

Applied to your work: when an agent's output does not match its spec, the reflex is to patch
the prompt. The move here is different — find the smallest input where the spec is wrong, and
ask what object the spec should have been written about. The epoch joke is a methodology:
state the naive version, break it deliberately on a toy case, name what the breakage tells
you, then write the next version. Four rounds of that is the process working, not failing.

### 7.2 Prove it one level up, then descend by a functorial operation

The architectural idea, and it is stated as a three-step recipe in the paper's very first
substantive paragraph:

> "Formulate (a higher-categorical) geometric statement; apply the operation of
> (higher-categorical) trace of Frobenius, and identify the result with the classical object
> of interest; deduce the sought-for description for the classical object."

Nobody proves the statement about automorphic functions. They prove the statement about
categories of sheaves, where there is enough structure to state an *equivalence* rather than a
coincidence of dimensions — and then apply an operation that is functorial by construction,
so the equivalence descends automatically.

Why the upstairs statement is easier despite being bigger: **more structure means more
rigidity**. An equivalence of categories has to commute with everything; there are far fewer
candidate equivalences than there are candidate linear isomorphisms. The constraints are the
help.

For agent systems: this is the difference between verifying outputs and verifying the
generator. A property proved about the schema, the type, or the constructor descends to every
output for free, and you never test outputs one at a time. Gaitsgory's Theorem 3 is precisely
a statement that "trace of the generator = the thing I care about" — a soundness theorem for
a compiler, not a test of a program.

### 7.3 One broken compositionality law can force you to rebuild the framework

The sharpest engineering lesson here, buried in §2.1–2.2 of the paper. For D-modules there is
a Künneth formula: sheaves on a product = tensor product of sheaves. For ℓ-adic sheaves it
**fails**, and not marginally — "it is never an equivalence if both Y and Y′ are
positive-dimensional schemes of finite type."

That single failure is why you cannot define "a group acting on a category" the obvious way,
why the trace map from geometry to functions is not an isomorphism, why AGCat had to be
constructed, and why "restricted" exists as a notion at all. Nobody patched around it: the
compositionality law is what everything else is built out of, so when it fails, no local fix
helps and you change the ambient category.

You compose things for a living — skills, subagents, MCP servers. The transferable question
is: **which of my composition laws actually holds, and which am I quietly patching around at
every call site?** A law that holds only approximately is not a law, and every downstream
abstraction is paying for it.

### 7.4 An equivalence that does not respect the structure is not the theorem

Remark 2.6.11 of the paper is the sharpest caveat in either document, and the talk omits it
entirely.

Dhillon–Varshavsky–Yang have made very significant progress on Conjecture 2.6.10 — but what
they establish is an equivalence **of abstract 2-categories**. Both sides carry more: an
action of QCoh(LS^restr) via the Bernstein centre. And, in the paper's words: "What we do not
know yet is why the equivalence of [DVY] is compatible with the maps from QCoh to the
Bernstein centres of the two sides."

So: the objects match, and it is not yet known that the match respects the operators that make
the objects mean anything. The Hecke action is the entire point of Langlands; an equivalence
that ignores it is a coincidence of size.

This is the same finding Kontorovich reaches from the other direction, with his Vulcan joke —
a Lean file that compiles is a file that compiles, and meaning is on the human side. Two ICM
plenary speakers, two fields, same lesson: **a passing check on the object is not a check on
the structure you cared about.** For you: an agent that produces a well-typed artefact
satisfying the schema has satisfied the schema. Whether it respects the invariant the schema
was written to protect is a separate theorem and usually an unproved one.

### 7.5 When the quantity has no clean answer, enlarge it until it does

The final move of the talk (§4.13) is worth isolating because it is counterintuitive and
generally useful.

Autom^{level}, the object people have cared about for fifty years, has **no clean spectral
description** — the paper says flatly, "we do not know how to translate the category
Rep(𝔏(G)(𝔽_q))". The response is not to give up and not to approximate. It is to construct a
*larger* object, Autom^{enh}, living in a bigger category, which **does** have a clean
description — and from which the original is recovered by a right adjoint, ι^!. Nothing is
lost; a projection gets you back.

You know this shape. Distributions are worse-behaved than functions in every naive sense, and
you enlarge to them because differentiation becomes total. Complex numbers are an enlargement
that makes root-finding total. Adding auxiliary variables to close a recursion is the same
move.

The operational version: when a quantity resists a clean formula, ask whether it is the
*shadow* of something larger that has one. The test that you have found the right enlargement
is the one the paper performs in §3.2.6 — check that the projection back really does recover
the original object, on the nose.

---

## 8. Where to read next

Ordered. All three are hard; the first is the only one written for a general audience.

1. **Gaitsgory, *Local and global Langlands conjecture(s) over function fields*.**
   [arXiv:2509.24902](https://arxiv.org/abs/2509.24902) — the written version of this talk, and
   the source of every formula above. §0.1 and §1 are readable with this tutorial beside you;
   §1.5 is the derivation in §5 of this document. Sections 2 and 3 are for specialists.
2. **Arinkin, Gaitsgory, Kazhdan, Raskin, Rozenblyum, Varshavsky, *The stack of local systems
   with restricted variation and geometric Langlands theory with nilpotent singular support*.**
   [arXiv:2010.01906](https://arxiv.org/abs/2010.01906) — where LS^restr is defined and where
   Shv_Nilp = Shv_HL is proved. This is the foundational paper for the whole global half.
3. **Gaitsgory and Raskin, *Geometric Langlands in positive characteristic from characteristic
   zero*.** [arXiv:2508.02237](https://arxiv.org/abs/2508.02237) — the source of Theorem 1.4.6,
   i.e. of everything the talk is able to call a theorem.

If you want the neighbouring conjecture in its own words rather than through this paper's
translation: Fargues and Scholze, *Geometrization of the local Langlands correspondence*,
[arXiv:2102.13459](https://arxiv.org/abs/2102.13459).

---

## 9. Self-test

<details>
<summary>1. State Langlands' question in one sentence, and say what "over function fields" changes.</summary>

Describe the space of automorphic functions in terms of the spectral side — the Langlands
parameters. "Over function fields" means you replace ℚ by the field of rational functions on a
curve X over a finite field 𝔽_q; primes become points of the curve. The gain is that the
setting now has *geometry*, so algebraic geometry and sheaf theory become available. That is
the only reason any of this machinery applies.
</details>

<details>
<summary>2. What is the space of automorphic functions, concretely?</summary>

Autom(X,G) = Funct_c(Bun_G(𝔽_q)): the finitely supported ℚ̄_ℓ-valued functions on the set of
isomorphism classes of G-bundles on X defined over 𝔽_q. For G = GL_n that is rank-n vector
bundles. The set is discrete, infinite, and countable. The object is elementary; all the
structure is in the Hecke operators acting on it.
</details>

<details>
<summary>3. Why is the Stone-Age conjecture false, and what is the classical analogue of the failure?</summary>

For G = 𝔾_m, X = ℙ¹: the left side is Funct_c(ℤ), of countable dimension; the proposed right
side is a direct sum of lines indexed by 𝔾_m(ℚ̄_ℓ) = ℚ̄_ℓ^×, which is uncountable. Classical
analogue: an operator with continuous spectrum has no eigenbasis, so you must use a direct
integral over the spectrum rather than a direct sum of eigenlines. The fix — replace ⊕ over
parameters by 𝒪(parameter space) — is that direct integral, written algebraically. For 𝔾_m it
is literally Fourier series: Funct_c(ℤ) ≅ ℚ̄_ℓ[t,t^{-1}] = 𝒪(𝔾_m).
</details>

<details>
<summary>4. Why does the coefficient field have to change from ℚ to ℚ̄_ℓ?</summary>

The spectral side consists of *continuous* homomorphisms out of the étale fundamental group,
which is profinite. For continuity to have content the target group must carry a compatible
topology. ℚ̄_ℓ — the algebraic closure of the ℓ-adic numbers, ℓ ≠ char — has one; ℚ does not.
That is the entire reason, and it is the only reason.
</details>

<details>
<summary>5. Why is the answer ω and not 𝒪?</summary>

Because the arithmetic parameter space LS^arithm is singular — the paper says
quasi-quasi-smooth, cotangent fibres of amplitude [−2,1], not eventually coconnective — and on
a singular space functions and densities are genuinely different objects. The trace formula
supplies the mechanism directly: Tr(φ, QCoh) = Γ(fixed points, 𝒪) but Tr(φ, IndCoh) =
Γ(fixed points, ω), and the correct automorphic category corresponds to IndCoh, not QCoh.
Where the space is well-behaved they agree (the stack is Calabi–Yau); the discrepancy on the
bad locus is a source of non-temperedness.
</details>

<details>
<summary>6. What is singular support, and which condition is imposed on Bun_G?</summary>

Singular support is the sheaf-theoretic wavefront set: a conical subset of T*(𝒴) recording the
codirections in which a sheaf fails to be locally constant. For 𝒴 = Bun_G, the cotangent
bundle is the moduli of Higgs bundles, and one imposes that the singular support lie in the
**global nilpotent cone** Nilp, giving Shv_Nilp(Bun_G). Equivalent characterisation
(AGKRRV1, Thm 14.4.3): the same subcategory is Shv_HL(Bun_G), the sheaves whose Hecke
transforms are lisse along the curve.
</details>

<details>
<summary>7. Explain the categorical trace, and what it does to the categorical level.</summary>

Take the basis-free definition of the ordinary trace — unit into V ⊗ V*, apply the
endomorphism, evaluate — and observe it uses only a tensor product, a unit, a dual, and
evaluation. So it runs in any symmetric monoidal category. Applied to a dualizable *category*
with an endofunctor it produces a *vector space* (Hochschild homology); applied to a
2-category it produces a category. **The trace walks one rung down the categorification
ladder**, and taking the trace of Frobenius is the operation that converts geometric
statements into classical ones.
</details>

<details>
<summary>8. Give the three-step derivation of Conjecture 1 from Conjecture 2.</summary>

(1) Theorem 1.2.3: Tr(Frob, Shv_Nilp(Bun_G)) ≅ Autom(X,G). (2) Conjecture 1.4.4:
Shv_Nilp(Bun_G) ≃ IndCoh_Nilp(LS^restr(X)), Frobenius-compatibly, so the traces agree.
(3) The IndCoh trace formula plus Proposition 1.5.6:
Tr(Frob, IndCoh_Nilp(LS^restr(X))) ≅ Γ(LS^arithm(X), ω). Splice: Autom ≅ Γ(LS^arithm, ω).
Steps 1 and 3 are theorems; step 2 is a theorem in characteristic 0 and for GL_n, and in
general holds over a union of connected components.
</details>

<details>
<summary>9. Why do isocrystals appear, and what is Lang's theorem doing?</summary>

Isoc_G := 𝔏(G)/Ad_Frob(𝔏(G)), the loop group modulo Frobenius-twisted conjugation. For a
*connected* algebraic group H, Lang's theorem says H/Ad_Frob(H) ≅ pt/H(𝔽_q), so sheaves there
are just Rep(H(𝔽_q)) and nothing is gained. The loop group is an ind-scheme and **Lang fails**
for it — e.g. for 𝔏(𝔾_m) the t-adic valuation is a nonconstant twisted-conjugacy invariant. So
Isoc_G properly contains pt/𝔏(G)(𝔽_q), and Shv(Isoc_G) properly contains Rep(𝔏(G)(𝔽_q)). The
conceptual reason it is the *right* enlargement: it is what Tr(Frob, 𝔏(G)-Cat) computes — "they
appear naturally as the recipient of the trace."
</details>

<details>
<summary>10. What does Conjecture 7 say, and in what sense is it the answer?</summary>

Under the local equivalence Shv(Isoc_{G,x}) ≃ IndCoh(LS^arithm(𝒟̊_x)), the enhanced automorphic
object Autom^{enh_x} corresponds to (𝔯^arithm)_* ω, the IndCoh pushforward of the dualizing
sheaf along restriction from the punctured curve to the punctured disc. It is "the answer"
because it finally does what Langlands asked — describes automorphic functions purely in
spectral terms — at the cost of three modifications: the parameter space had to be constructed,
𝒪 had to become ω, and the automorphic object itself had to be enlarged from Autom^{level} to
Autom^{enh} (with the original recovered by the right adjoint ι^!).
</details>

---

## 10. Note on the tutorial process

**Difficulty against reputation: matched, for once.** Gaitsgory is known for geometric
Langlands and the talk is geometric Langlands at its frontier, so the Rule-1 inversion that
caught Kontorovich did not apply. What the transcript *did* settle is the split: the global
unramified half is a hard 4 — four statements and one argument, delivered deliberately
slowly — and the local half is a 5 and is not learnable from a talk.

**How much mathematics survived the captions: none.** This was a slide talk with dense
notation, and auto-captions carry no formulas at all. Every displayed formula, conjecture
statement, and numbered result here comes from arXiv:2509.24902. The transcript supplied the
narrative, the epoch joke, the motivations, the attributions, and the two "main point of this
talk" markers — all absent from the paper. The two sources are nearly complementary, which is
lucky and unusual.

**Length note.** This runs longer than the two model tutorials. At difficulty 5 the bridge is
the deliverable, and §3 plus the walkthrough carry twelve numbered statements across two
settings. I trimmed rather than truncated; nothing in the walkthrough was dropped.

**Name corrections.** Every one verified against the paper's own text or bibliography unless
marked.

| Caption | Correct | Source |
|---|---|---|
| Rosenblum | **Rozenblyum** | paper, [AGKRRV1] |
| Shen Wei Zhu / Shin Won Joon | **Xinwen Zhu** | paper, [Zhu1], [Zhu2], fn. 19 |
| Fargues-Scholten / Fargues-Fontaine / Park Shultz | **Fargues–Scholze** | paper, [FS] |
| Erinkin | **Arinkin** | paper, §2.6.2, [AG] |
| Herman Stefanich | **German Stefanich** | paper, [Ste] |
| Gurpreet Dhillon | **Gurbir Dhillon** | paper, [DVY]; confirmed by search |
| Dylan Yang | **D. (David) Yang** | paper, [DVY] |
| Arnaud Etam | **Arnaud Eteve** | paper, [Ete] |
| Moy Prasad | **Moy–Prasad** | paper, [DVY] title |
| Jean-Pierre Serre (for nilpotent singular support, "40 years ago") | **G. Laumon**, 1987 | paper, Remark 1.1.8, [Laum] |

**Substantive caption errors corrected in the text, not just spellings.** Four, and all four
change the meaning:

- "representations of this Picard group" → **p-adic group**. The speaker says "p-adic group"
  correctly moments later. This one is actively misleading, because "Picard" is a real object
  in this talk — Bun_{𝔾_m} *is* a Picard stack.
- "nilpotent **single** support" throughout → **singular support**.
- "G with coefficients in the **slow** local field" → **the local field** 𝔽_q((t)).
- "incoherent" / "into coherent" / "integral coherent" throughout → **ind-coherent** (IndCoh).

**Reconstructed, and what would verify each:**

- **The talk-number ↔ paper-number map** (§4.15). Built from order and content; the speaker
  never reads a paper section number aloud. All twelve rows match on content. The slides would
  settle it and are not public.
- **The ladder diagram** (§4.14). Layout mine; every cell and arrow is stated in a source, and
  the two rules beneath it are the speaker's own words.
- **Exercise 6.2(b)**, the failure of Lang's theorem for 𝔏(𝔾_m). My computation; both sources
  merely assert the failure. Verify in one line: Frobenius acts on coefficients, so it
  preserves the t-adic valuation.
- **The 𝔾_m/ℙ¹ parameter count** in §4.1 — the parenthetical explaining why the index set is
  ℚ̄_ℓ^×. Standard, but mine; the talk asserts the index set without justification.
- **"Grothendieck and Ray"** → almost certainly **Grothendieck and Raynaud** (SGA 1). Not in
  the paper, so flagged in §3.3 and not relied on.
- **"the functional zeta conjecture"** should, from context, be the **Fargues–Scholze
  conjecture**. I did not write that reconstruction into the body; the sentence is paraphrased
  without a name.

**Could not verify:**

- **"a series of papers by nine authors"** (talk, §4.4). The AGKRRV series has six authors;
  Gaitsgory–Raskin has two. The speaker then declines to name them ("I'm too jet-lagged"). I
  could not reconcile the number and have not guessed a list.
- **"Hecke finite" versus "Hecke-lisse"** (§4.13). Captions say "hecke finite"; the paper's
  condition is Shv_HL, expanded in its footnote 3 as "Hecke-lisse". But *Hecke-finiteness* is
  also a real term in this literature (it appears in Lafforgue's shtuka work), so this is
  **not** safely a caption mangle. I used the paper's definition and flagged it in place.
  Unresolved.
- **The direction of the shtuka construction** (§4.13). The talk says "direct image with
  compact supports of the constant sheaf"; the paper defines the object dually via
  ℱ ↦ C_c(Sht̊, π^!ℱ). Both quoted; I did not assert they are the same construction.

**Gaps marked in place, and how bad they are.** Two, both mild:

1. **Hecke operators are never defined** (§4.6). The speaker refuses on time grounds; the paper
   gives only the functor's shape and cites geometric Satake. It is the most important
   undefined object in the talk, but survivable, because every statement below uses only the
   shape.
2. **"Restricted" for the loop group is only provisionally defined** (§4.11). The definition
   the field will use is in Dhillon–Varshavsky–Yang, listed as *forthcoming*. Not recoverable
   from any public source.

Beyond those two I did **not** attempt to teach AGCat or 2-IndCoh: both appear as facts with
their motivation and their consequence, and no more. Deliberate. They are not learnable in a
tutorial, and faking it would produce exactly the smooth fabrication that is worse than a gap.

**One error found in the paper.** Its bibliography lists [Zhu1] as arXiv:2020.02998, not a
valid identifier (there is no month 20). The correct one is **arXiv:2008.02998** — X. Zhu,
*Coherent sheaves on the stack of Langlands parameters*, 7 August 2020. Verified by search;
corrected in §4.10.

**One place the paper beats the talk.** The talk presents Conjecture 2 as known only up to a
union of connected components. The paper (§1.4.3) records that Gaitsgory–Raskin establish it
**in full in characteristic 0, and for G = GL_n over any ground field**. Where a speaker
undersells and the paper does not, quote the paper.

**On the paper's date line.** The arXiv HTML shows "11 August 2026" in the title block. That
is LaTeX's `\today` at HTML regeneration, not a submission date; the arXiv stamp on the same
page reads **arXiv:2509.24902v1 [math.AG] 29 Sep 2025**, which is the date in the front matter.
