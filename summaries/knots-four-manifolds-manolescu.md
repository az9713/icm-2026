---
title: "From knots to four-manifolds"
speaker: Ciprian Manolescu (Stanford University)
source: https://www.youtube.com/watch?v=6GYIK6uK-s4
video_id: 6GYIK6uK-s4
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2601.05425
transcript: ../transcripts/6GYIK6uK-s4_transcript.txt
difficulty_for_you: 4/5 (the topological frame) — 2/5 (the two invariants, once framed)
reading_time: ~65 min
---

# From knots to four-manifolds — Ciprian Manolescu

**Field:** low-dimensional topology. Specifically: how a picture of a knotted loop in
three-dimensional space can be made to compute something about a four-dimensional space,
and why anyone would want that.

**Difficulty against your background: 4 out of 5, split — and the split is the whole
point of this tutorial.**

The *frame* is a genuine 4. You do not have algebraic topology. Almost every noun in this
talk — homology, fundamental group, handle decomposition, cobordism, intersection form,
chain complex — is a noun you have not been issued. Four separate unfamiliar layers stack
up before the first real result appears.

The *machinery* the talk actually spends its time on is a 2, and this is the surprise. The
two invariants at the centre of the talk — knot Floer homology via grid diagrams, and
Khovanov homology via the cube of resolutions — are, once defined, **finite linear algebra
over ℤ**. You count empty rectangles on an n×n grid drawn on a torus. You tensor together
copies of a rank-two abelian group over the vertices of a hypercube. There is no analysis
in either. You can do both by hand this afternoon, and §6 asks you to.

So the honest shape of this document is: a long bridge, then a short and unexpectedly easy
destination. The payoff for crossing the bridge is that you get to watch a hard fact about
smooth four-dimensional geometry — that two spaces are the same topologically and
different smoothly — get proved by counting.

**Prerequisites this tutorial builds:** homology of a chain complex, from linear algebra;
knots, links and their diagrams; the Alexander and Jones polynomials from skein relations;
framings and push-offs; the difference between homeomorphic and diffeomorphic, and why
exotic pairs exist; the intersection form; Morse theory as a decomposition tool and the
handles it produces; surgery, surgery traces and Kirby diagrams; cobordism, Floer homology
and the TQFT composition law.

**A note on sources.** This is the good case, and better than the good case. There is a
genuine ICM proceedings paper — [arXiv:2601.05425](https://arxiv.org/abs/2601.05425),
*From knots to four-manifolds*, Ciprian Manolescu, submitted 8 January 2026, 29 pages, 19
figures, comments field reading "to appear in Proceedings of the ICM 2026". The talk
follows the paper's section order exactly for the first six of its seven sections.

That matters here for a specific reason. The auto-captions carry **no formulas at all**,
and this was a talk built on nineteen figures. The mathematics lived on the slides and the
captions cannot see slides. Every displayed formula below comes from the paper. So does
every proper name — the captions destroy essentially all of them, and the correction table
in §10 has thirty entries.

Two structural differences between the talk and the paper you should know before you
start:

1. **The talk stops after §6 of the paper.** The paper's §7, "Probing four-manifolds with
   knots" — sliceness, the programme to attack the smooth four-dimensional Poincaré
   conjecture, RBG links, and a machine search over 350 million knots — **was never
   delivered**. I checked: the words "slice", "ribbon", "Dunfield" and "Gong" do not occur
   anywhere in the transcript. The abstract advertises it; the lecture ran out of time or
   was cut. I give it its own clearly-marked section, §4.14, because it is the part of the
   paper closest to your professional work.
2. **His pointer died** about twenty-two minutes in ("Oh, my pointer is out of battery. If
   anyone can bring me a different pointer, that would be great"), in the middle of
   explaining framings. He improvised with the cursor. It shows in the transcript and it
   is worth knowing that a couple of the vaguer passages are a man describing a picture he
   cannot point at.

Where the talk and the paper differ on substance — and they do, in three places — I say
which one I am quoting.

---

## 1. What is at stake

Here is the fact that makes this whole subject exist.

Take ℝⁿ, ordinary Euclidean space. Ask: in how many essentially different ways can you put
a smooth structure on it — a consistent notion of "differentiable function" — so that the
result is still the same topological space? For every n except one, the answer is **one**.
There is nothing to choose. For n = 4, the answer is **uncountably many**. Not two, not
finitely many: a continuum of genuinely different smooth structures on the space you have
been doing calculus in your entire career, if only it had four dimensions instead of three.

That is Taubes' theorem (1987), and Manolescu states it in the first five minutes. It is
accompanied by two more:

- In every dimension other than 4, a compact manifold admits only finitely many smooth
  structures. In dimension 4 there are compact examples with **infinitely many**.
- In every dimension other than 4, counting the smooth structures on the sphere Sⁿ has
  been reduced to a computation in algebraic topology. In dimension 4 nobody knows the
  answer even for S⁴. That the answer is 1 is the **smooth four-dimensional Poincaré
  conjecture**, and it is open.

Manolescu, on the podium, on that last one:

> "I should say that opinions are split, or maybe most mathematicians refuse to say that
> they have an opinion of whether this is true or false. Most work nowadays is trying to
> disprove it, because we have more promising methods in that direction, but it could also
> be true. We just don't know."

The organising phenomenon is the **exotic pair**: two smooth four-manifolds that are
homeomorphic — indistinguishable as topological spaces — but not diffeomorphic. Same
space, two incompatible calculuses on it. In dimension four this is not a pathology at the
edge of the subject; it is the subject.

Now the difficulty. How do you *prove* two things are not diffeomorphic? Every invariant
you meet in a first course in algebraic topology — homology, the fundamental group — is
built to be blind to smooth structure by construction. They are homotopy invariants; they
cannot see the distinction you care about. Manolescu:

> "You cannot distinguish them using the invariants that you learned in the first course in
> algebraic topology, like homology or fundamental group, because those are invariants up
> to homeomorphism — in fact up to homotopy equivalence. So to distinguish things up to
> diffeomorphism you have to do something else."

The something else, historically, was **gauge theory**: put a Riemannian metric on the
manifold, write down a nonlinear elliptic PDE with an infinite-dimensional symmetry group,
count its solutions with signs, and prove the count does not depend on the metric. Donaldson
did it with the anti-self-dual Yang–Mills equations in 1983. Seiberg and Witten wrote down
a better equation in 1994 and the field moved to it.

This works, and it is one of the great achievements of twentieth-century geometry. But it
has a hard practical limit: **you can only count the solutions when the manifold is special
enough that you can solve the PDE.** In practice that means the manifold comes from complex
algebraic geometry (a projective algebraic surface, where solutions correspond to
holomorphic bundles or to divisors), or it carries a metric of positive scalar curvature,
or it decomposes as a connected sum. That is a large supply of examples but it is not all
four-manifolds, and it is not the ones you most want.

So the question this talk answers is:

> **How do you get your hands on a *general* four-manifold, concretely enough to compute
> something, when you cannot solve the equation on it?**

The answer, and the title of the talk: **you draw it as a knot.** Every four-manifold is
encoded by a link — a collection of knotted circles in ordinary three-dimensional space —
with an integer written on each circle. That encoding is called a Kirby diagram, and the
entire lecture is about what you can compute once you have one.

---

## 2. Your anchor: Morse theory, used twice, at two different scales

You own Morse theory already, though possibly under another name. In the calculus of
variations you take a functional, find its critical points, and classify each one by the
signature of the second variation — how many independent directions the Hessian is negative
in. That number is the **index**. You have done this for the action functional in classical
mechanics, for energy functionals, for the eigenvalue problems where the index counts nodal
domains.

Morse theory is that idea applied to a function on a manifold, run for what it tells you
about the manifold rather than about the function.

**The talk's own use of it, in his words.** Manolescu introduces handle decompositions like
this:

> "This is part of a more general story that goes under the name handle decompositions. So
> this works in any dimension. It uses Morse theory, and what Morse theory gives you is
> that every smooth manifold is made of some basic objects called handles."

The mechanism is exactly the one you know. Take a smooth function f : X → ℝ on a compact
manifold X, generic, so all its critical points are non-degenerate. Watch the sublevel set
{f ≤ C} as C increases from −∞ to +∞. As long as you do not cross a critical value, the
sublevel set does not change shape. When you cross a critical point of index k, the
sublevel set changes in exactly one way: a **k-handle** gets glued on, which is a thickened
k-dimensional disc, Dᵏ × D^(n−k), attached along ∂Dᵏ × D^(n−k).

His picture, from the podium, is the torus standing on end with f the height function. Four
critical points: a minimum (a 0-handle, giving a disc), two saddles (two 1-handles, giving
the two "arms"), and a maximum (a 2-handle, capping it off). That is the whole surface, in
four pieces, read off from the critical points of a height function. If you have seen the
same picture in the context of "the Morse inequalities", you have seen this.

Everything in §3.6 and §4.5 below — surgery, traces, Kirby diagrams — is the four-dimensional
version of that torus picture.

**The second use, which is mine and which I am labelling as mine.** Floer homology, the
central technical object of the whole talk, is set up as follows. The paper's definition,
verbatim in structure:

> Given a three-manifold Y, look at solutions to the relevant equations (Yang–Mills or
> Seiberg–Witten) on the cylinder ℝ × Y that are invariant under translation in the ℝ
> direction. Define a chain complex whose **generators are these solutions**, with
> differential
>
> > ∂x = Σ_y n(x,y) · y,
>
> where n(x,y) ∈ ℤ counts the solutions on ℝ × Y — not necessarily translation-invariant —
> that limit to x as you go to −∞ and to y as you go to +∞.

Read that against Morse theory. In Morse homology you build a chain complex whose
generators are the critical points and whose differential counts **gradient flow lines**
running from one critical point to another. The two definitions are the same definition:
translation-invariant solutions play the role of critical points, and solutions on the
cylinder interpolating between two of them play the role of flow lines. The parameter along
the cylinder is the flow time.

> **Marked as my framing.** Neither the talk nor the paper uses the word "Morse" in
> connection with Floer homology; both use it only for handle decompositions. The
> identification is standard in the literature and is the reason Floer homology is called
> homology at all — the translation-invariant solutions are the critical points of an
> action functional (Chern–Simons in the Yang–Mills case, its Seiberg–Witten analogue in
> the other), and the equation on ℝ × Y is that functional's gradient flow. **What would
> verify it:** Floer's original paper, *An instanton-invariant for 3-manifolds*, Comm.
> Math. Phys. 118 (1988) 215–240, or Kronheimer–Mrowka's book *Monopoles and
> three-manifolds*, both of which the survey cites (references [21] and [45]) for exactly
> this construction. I have not read the derivation into the sources; I am telling you the
> shape so the definition is not a black box.

So the structure of the whole talk is: **an infinite-dimensional Morse theory, computed by
means of a finite-dimensional one.** You cannot do the Morse theory on the space of fields
directly. You can do the Morse theory on the manifold itself — that is Kirby diagrams — and
then use it to cut the field-theoretic problem into pieces small enough to solve.

**The payoff line, and this is the speaker handing you the anchor directly.** After defining
knot Floer homology combinatorially — count empty rectangles on a grid — he says:

> "Secretly each rectangle is a pseudo-holomorphic curve in the symmetric product of the
> torus. So by using knots we put ourselves into a situation where we can understand
> pseudo-holomorphic curves. It just happens they have a simple description in terms of
> just counting empty rectangles on the grid. And in fact, even more secretly, the
> rectangle is a solution of the Seiberg–Witten equations on ℝ² × T²."

The paper states it flatly:

> "each empty rectangle is a pseudo-holomorphic strip in the moduli space of vortices, and
> hence corresponds to a solution of the Seiberg-Witten equations on ℝ² × T²."

**A rectangle drawn on a chessboard is a solution of a nonlinear elliptic PDE.** That is
the single sentence I would keep from this talk. It is a discretisation result of a kind you
know well in spirit — you have watched a variational problem become a sparse linear system —
but with a far more extreme compression ratio, because the discretisation here is exact, not
approximate. The count of PDE solutions and the count of rectangles are equal, not close.

**Secondary anchor: the transfer matrix.** The other structure running through the talk is
the composition law for cut-and-paste computations. Cut a closed four-manifold W into pieces
along three-manifolds:

> W = W₁ ∪_{Y₁} W₂ ∪_{Y₂} ⋯ ∪_{Y_{n−1}} W_n

To each interface Y you associate a vector space F(Y) — its Floer homology. To each piece
W_i, which has two boundary components, you associate a **linear map** F(W_i) : F(Y_{i−1}) →
F(Y_i). And then

> F(W) = F(W_n) ∘ ⋯ ∘ F(W₂) ∘ F(W₁).

The invariant of the whole is the composite of the maps of the parts. This structure has a
name, and the paper gives it: a **topological quantum field theory**. You have met the same
bookkeeping as the transfer matrix in statistical mechanics — a partition function on a long
lattice is a product of local transfer matrices, one per slice, sandwiched between boundary
vectors. A closed four-manifold starts and ends at the empty set, F(∅) = ℤ, so the composite
is a map ℤ → ℤ, which is multiplication by an integer. That integer is the invariant.
Manolescu says exactly this from the podium and then adds, correctly, "the experts know this
is a lie" — the honest version needs several flavours of the homology at once.

**One anchor I considered and am rejecting.** You might expect exotic smooth structures
themselves to be the anchor. They are not; they are the *stake*. An anchor has to be
something you already own that the talk is structurally about, and you do not own exotic
structures — nobody's physics training contains them. They belong in §1, where I put them.

**One thing that is genuinely absent.** There is no physics-duality framing here — no
Kapustin–Witten, no S-duality, no branes. The physics in this talk is the older and more
literal kind: Yang–Mills and Seiberg–Witten are PDEs that came out of gauge theory, and the
talk uses them as PDEs. If you were expecting the categorical-duality style of the geometric
Langlands story (see `langlands-function-fields-gaitsgory.md`), this is not that; it is much
closer to the ground.

---

## 3. The bridge

Seven items. Each is defined by deforming something you already have. The first one is
load-bearing for everything else, so do not skip it.

### 3.1 Homology of a chain complex, from linear algebra

Every invariant in this talk is "the homology of a chain complex". Here is the whole
definition, in your own vocabulary, with no topology in it.

A **chain complex** is a sequence of abelian groups — for your purposes, think free
ℤ-modules, i.e. ℤⁿ, or just vector spaces if you prefer — with maps between consecutive
ones:

> ⋯ → C₂ --∂₂--> C₁ --∂₁--> C₀ → 0

subject to one condition: **∂ ∘ ∂ = 0.** Two consecutive maps compose to zero. Equivalently,
im ∂_{k+1} ⊆ ker ∂_k.

The **homology** is the failure of that containment to be an equality:

> H_k = ker ∂_k / im ∂_{k+1}.

That is it. Take the kernel of one matrix, quotient by the image of the next. It is a
finite linear-algebra computation the moment you write the maps as matrices: compute two
null spaces and two column spaces and take a quotient of free modules.

Three things to know about why anyone does this rather than just recording the ranks of the
C_k:

1. **The C_k depend on choices; the H_k do not.** You build the complex from a diagram, a
   grid, a triangulation. Change the diagram and every C_k changes. The homology does not.
   That is the entire game: manufacture a complex from a presentation, prove the homology is
   independent of the presentation, and you have an invariant.
2. **Homology is finer than the alternating sum of ranks.** Define the Euler characteristic
   χ = Σ_k (−1)^k rank(C_k). A short exercise shows χ = Σ_k (−1)^k rank(H_k) — the
   alternating sum is the same computed upstairs or downstairs. So the Euler characteristic
   sees only a shadow of the homology, and the homology is a strictly stronger invariant.
   **This is the exact relationship between the knot polynomials and the knot homologies in
   this talk.** The Alexander polynomial is an Euler characteristic of knot Floer homology;
   the Jones polynomial is an Euler characteristic of Khovanov homology. In both cases the
   homology remembers more.
3. **Gradings.** These complexes usually carry a second (or third) integer grading that the
   differential shifts in a controlled way, so the homology splits into pieces
   H_{i,j}. Both talk and paper decline to define the gradings ("I won't get into that"). I
   decline too, and none of what follows needs them except where I quote a graded answer
   from the paper.

If you want the one-line intuition: **homology measures cycles that are not boundaries.**
Things that close up but are not the edge of anything.

### 3.2 Knots, links, diagrams, and how you tell them apart

A **link** is a compact smooth one-dimensional submanifold of ℝ³ — finitely many disjoint
closed loops. A connected one is a **knot**. Topologists add a point at infinity and work in
the three-sphere S³ = ℝ³ ∪ {∞}, purely because compact spaces behave better.

The examples that recur (paper, Figure 1): the **unknot** (a round circle); the **Hopf link**
(two circles passing once through each other); the **trefoil** (the simplest genuinely
knotted knot, three crossings); the **Borromean rings** (three circles, no two of which are
linked, but the three together are); and the **Conway knot**, an eleven-crossing knot which
recurs throughout as the standard counterexample.

Two links are the same if one deforms smoothly into the other. Showing two links *are* the
same is easy — exhibit the deformation. Showing they are *different* requires an **invariant**:
some algebraic object computed from a planar picture, which provably does not change when
you deform the link. Manolescu:

> "What these are, they're just a way of getting algebra from topology. You start with a
> knot diagram, there is some procedure that I will not explain to get a polynomial, and you
> show that this polynomial doesn't depend on the diagram of the knot."

The reason a planar picture suffices: two planar diagrams represent the same link if and
only if they are related by a sequence of three local moves, the **Reidemeister moves**
(paper, Figure 2). So an invariant is anything you can compute from a diagram that is
unchanged by those three moves.

**The Alexander polynomial** Δ(L), from 1928. It is a Laurent polynomial in q^{1/2} —
"Laurent" meaning negative exponents are allowed, which Manolescu flags from the podium. It
is pinned down completely by two rules: Δ(unknot) = 1, and the **skein relation**

> Δ(L₊) − Δ(L₋) = (q^{1/2} − q^{−1/2}) · Δ(L₀).

Here L₊, L₋ and L₀ are three links that are identical outside a small disc, and inside that
disc look like: a positive crossing, a negative crossing, and no crossing at all (the two
strands turned back on themselves without meeting). The relation lets you compute recursively:
pick a crossing, change it, and you have traded one link for two simpler ones. You will run
this in §6.1 and get Δ(trefoil) = q⁻¹ − 1 + q.

**The Jones polynomial** V(L), from 1984, has a nearly identical characterisation —
V(unknot) = 1 plus

> q⁻¹ V(L₊) − q V(L₋) = (q^{1/2} − q^{−1/2}) · V(L₀)

— and yet, as the paper notes, no simple topological interpretation. It came from operator
algebras, not from geometry, and where it comes from is still a live question.

### 3.3 Framings, push-offs and the writhe

This is the piece the dead pointer damaged, so let me be careful.

A **framed link** is a link L together with a choice of normal vector field along it — a
consistently varying arrow sticking out sideways at every point. Manolescu's own remark:
once you have one arrow, you also have the tangent vector, and their cross product gives you
a third, so one vector field really does determine a full frame.

The useful way to think about it is the **push-off**. Slide the whole link a little way
along the vector field. You get a second, parallel copy L′ running alongside the original.
The framed link is the pair (L, L′).

How much information is in that choice? For each component, exactly one integer: the
**linking number** λ between that component and its push-off — how many times the pushed-off
copy winds around the original. So a framed link is a link plus one integer per component.
Framing λ = 0 is called the **Seifert framing**.

There is a second natural framing: push the link off *within the plane of the diagram*. This
is the **blackboard framing**, and its integer is the **writhe** of the diagram — the number
of positive crossings minus the number of negative crossings, where a crossing counts as
positive or negative according to which of L₊, L₋ it looks like. For the standard
right-handed trefoil diagram, all three crossings are positive, so the writhe is 3 and the
blackboard framing is λ = 3. That is the paper's own Figure 4.

> ⚠ **The companion document is wrong here, or at best ambiguous.** The paper prints
>
> > w = ½ (#positive crossings − #negative crossings)
>
> with a factor of ½, which would give the right-handed trefoil w = 3/2, contradicting its
> own Figure 4 caption ("This corresponds to λ = 3"). The formula is correct only if the
> crossings being counted are the crossings between L and its push-off L′ — each crossing of
> the diagram with itself produces two such — in which case the ½ restores it. Use
> **w = #positive − #negative** for a knot diagram and you will get 3 for the trefoil, which
> is the answer the paper's figure wants.

### 3.4 Homeomorphic versus diffeomorphic, and why exotic pairs are invisible to homology

A **topological manifold** is a space that looks locally like ℝⁿ. The natural equivalence is
**homeomorphism**: a bijection, continuous, with continuous inverse.

A **smooth manifold** is a topological manifold with an atlas of charts whose transition
maps are C^∞ — enough structure to differentiate. The natural equivalence is
**diffeomorphism**: a bijection which is C^∞ with C^∞ inverse.

Up to dimension 3 these are the same problem: every topological manifold in dimensions
0,1,2,3 has exactly one smooth structure. From dimension 4 they come apart, and dimension 4
is where the divergence is worst (§1). Two smooth manifolds that are homeomorphic but not
diffeomorphic are an **exotic pair**.

Why is this so hard to detect? Because homology and the fundamental group are invariants of
homotopy type, which is coarser than homeomorphism, which is coarser than diffeomorphism.
An exotic pair agrees on everything those tools can see, by construction. You need something
that reaches down to the smooth structure, and the only known way to reach that far is to
write down a differential equation — which only makes sense on a smooth manifold — and count
its solutions. Which is why the subject is a branch of PDE wearing a topologist's coat.

On the topological side the situation is, by contrast, completely understood in the
simply-connected case: Freedman's 1982 theorem classifies all closed simply-connected
topological four-manifolds up to homeomorphism. ("Simply connected" means every loop can be
contracted to a point; the paper notes the restriction is necessary, because with arbitrary
fundamental group the classification runs into the undecidable group isomorphism problem.)
So the topological question is finished and the smooth question is wide open — an inversion
of the usual state of affairs.

### 3.5 The intersection form

You own bilinear forms, so this is quick, and you need it for §4.10.

On a closed simply-connected four-manifold X there is a non-degenerate bilinear form

> H₂(X; ℤ) × H₂(X; ℤ) → ℤ

given by geometric intersection. The idea: classes in H₂ are represented by embedded
surfaces; two surfaces of dimension 2 inside a space of dimension 4 generically meet in
isolated points (2 + 2 = 4); count those points with signs. Manolescu's version: "for every
four-manifold you can look at the second homology, which is generated by surfaces in the
manifold, and you see how surfaces intersect — you count the intersection number, you get an
integer."

It is a symmetric integer bilinear form, so it has a signature, and the standard vocabulary
applies: **definite** if the form is positive or negative definite, **indefinite**
otherwise.

Why it matters: **every known exotic pair of simply-connected four-manifolds has indefinite
intersection form.** Whether an exotic structure exists on a manifold with definite form is
open, and is the paper's Question 3.2 — does there exist an exotic smooth structure on a
connected sum #ⁿℂP² for some n ≥ 0? The smooth four-dimensional Poincaré conjecture is the
case n = 0. So this one bilinear-algebra invariant separates the solved region of the subject
from the unsolved one.

### 3.6 Surgery, traces, and the Kirby diagram

Now the construction the title is about. The route from knots to four-manifolds goes through
dimension three.

**Step 1: surgery gives you three-manifolds.** Take a framed link 𝕃 = (L, λ) in S³ with ℓ
components. Cut out a tubular neighbourhood of the link — you have removed ℓ solid doughnuts
and are left with the link complement. Now glue the ℓ solid doughnuts back in, but *glued
differently*. The different gluings are exactly parameterised by the framing. The result is
a closed three-manifold, written S³(𝕃).

Manolescu, on the terminology:

> "What is surgery? Well, I don't know what it is in medicine. But what it is in topology is
> that we take out a neighbourhood of the link and we put it back in — but we put it back in
> in a different way."

> **Theorem (Lickorish 1962, Wallace 1960).** Every closed oriented three-manifold arises as
> surgery on some framed link in S³.

That is remarkable and it is the hinge of the subject. Every three-dimensional space, no
matter how complicated, is encoded by a picture you can draw on paper: a link, with an
integer on each component. The paper's Figure 6 gives such pictures for the Poincaré
homology sphere and for the three-torus.

**Step 2: the same data gives you a four-manifold.** This is the step to hold on to. The
framed link does not just specify a three-manifold; it specifies a compact four-manifold
whose boundary is that three-manifold. It is called the **trace of the surgery**, X(𝕃).

The construction, described in words since you cannot see Figure 7. Start with D⁴, the
four-dimensional ball. Its boundary is S³. Manolescu draws it one dimension down: the plane
on the slide represents S³, and D⁴ is everything below the plane. The link sits in that
plane. Now, for each component, glue on a **2-handle**: a copy of D² × D², attached along
∂D² × D² = S¹ × D², which is a thickened circle, matched to a thickened component of the
link. His phrase for it is "a cap": a thickened disc whose boundary is the knot, glued on
top.

> X(𝕃) = D⁴ ∪ (one copy of D² × D² per component)

The identification of the thickened link component with S¹ × D² is where the framing enters;
that is the only thing the integers are doing. The result has corners, which you smooth. Its
boundary is exactly S³(𝕃). So:

> **Corollary.** Every closed oriented three-manifold bounds a compact oriented
> four-manifold.

And if the surgery happens to give you back S³ — that is, if S³(𝕃) = S³ — then you can cap
the other end off with a second copy of D⁴ and you have a **closed** four-manifold.

**Step 3: Morse theory says this is general.** From §2, a Morse function on a closed
four-manifold decomposes it into handles: exactly one 0-handle (a D⁴), some 1-handles, some
2-handles, some 3-handles, and one 4-handle (another D⁴). All the complexity sits in the
2-handles, because that is where knotting can occur — a 2-handle is attached along a circle,
and circles in a three-manifold can knot and link. Manolescu: "most of the complication comes
in the middle, namely from two handles."

The **Kirby diagram** is the picture of where the 1- and 2-handles attach. The 1-handles
attach along pairs of balls (a 1-handle is attached along ∂D¹ × D³, and ∂D¹ is two points,
thickened to two balls); you draw the two balls and understand that they are identified. The
2-handles attach along a framed link. The 3- and 4-handles need no extra data — a theorem of
Laudenbach and Poénaru guarantees the 3-handles can only be attached one way, essentially.

So: **a four-manifold is a picture of a framed link.** That is the sentence the whole talk
turns on.

The paper's examples, Figure 10, all with no 1- or 3-handles:

| Four-manifold | Kirby diagram |
|---|---|
| S⁴ | the empty link |
| ℂP² | the unknot with framing +1 (framing −1 gives the reversed orientation, ℂP̄²) |
| S² × S² | the Hopf link, both components framed 0 |
| K3 surface | a 22-component link, all framings −2 except one trefoil framed 0, plus boxes marked −1 meaning "put a full negative twist through all the strands in this box" |

That last row is the picture Manolescu opened the lecture with, before saying anything —
"here is a knot and here is a four-manifold; as you can see, the four manifold we draw it
using knots." The K3 surface is the zero set of z₀⁴ + z₁⁴ + z₂⁴ + z₃⁴ = 0 in ℂP³. In
algebraic geometry there are many K3 surfaces; in topology there is exactly one, because
they are all diffeomorphic. And its picture is a 22-component link.

One restriction to note, since it recurs: a four-manifold whose handle decomposition needs
no 1-handles is called **geometrically simply connected**, and then the link lives in S³ and
you can just write integers on it. Whether every closed simply-connected four-manifold is
geometrically simply connected is open. Most of the ones people work with are.

### 3.7 Cobordism, Floer homology, and the composition law

The last piece, and it is §2's transfer matrix stated properly.

A **cobordism** from a three-manifold Y₀ to a three-manifold Y₁ is a four-manifold W whose
boundary is Y₁ together with Y₀ taken with reversed orientation. Think of it as a
four-dimensional "interpolation" between two three-dimensional spaces — a slab whose two
faces are Y₀ and Y₁.

The TQFT structure attaches:

- to each three-manifold Y, an abelian group F(Y) — its **Floer homology**;
- to each cobordism W from Y₀ to Y₁, a homomorphism F(W) : F(Y₀) → F(Y₁), obtained by
  counting solutions of the PDE on W;
- with F(∅) = ℤ, and composition of cobordisms sending to composition of maps.

The construction of the map, from the paper: F(W) counts solutions on W with a cylindrical
end attached, weighted by which generator they converge to at infinity. In §2's language:
the boundary condition at each end picks out a basis vector, and F(W) is the matrix of
transition amplitudes between them.

Two named theories appear:

- **Monopole Floer homology**, from the Seiberg–Witten equations, constructed in general by
  Kronheimer and Mrowka in their 2007 book, with Manolescu himself contributing an earlier
  partial construction. (He says "I gave one in 2001 for some cases"; the paper's
  bibliography dates the published version to Geometry & Topology 2003. Both are right — 2001
  is the preprint.)
- **Heegaard Floer homology**, Ozsváth and Szabó, which is the whole of §4.7 below.

---

## 4. The talk, rebuilt

Section order follows the lecture, which follows the paper.

### 4.1 One page of knot theory

He gives himself one slide. Knots and links, the five examples, the two polynomials, and
then the point of the section: the polynomials have been **upgraded to homology theories**.

> **Knot Floer homology** ĤFK(K) = ⊕_{i,s ∈ ℤ} ĤFK_i(K, s), a bigraded abelian group, due
> independently to Ozsváth–Szabó and to Rasmussen (2003–2004). Its graded Euler
> characteristic is the Alexander polynomial:
>
> > Σ_{s,i} (−1)^i q^s · rank_ℤ ĤFK_i(K, s) = Δ(K).
>
> **Khovanov homology** Kh(K) = ⊕_{i,j} Kh_{i,j}(K), Khovanov 2000, whose graded Euler
> characteristic is the normalised Jones polynomial:
>
> > Σ_{i,j} (−1)^i q^{j/2} · rank_ℤ Kh_{i,j}(K) = (q^{1/2} + q^{−1/2}) V(K).

This is §3.1's point 2 in the wild: alternating sum of ranks recovers the polynomial, the
homology remembers strictly more. Manolescu: "from HFK you can recover the polynomial but
not vice versa. HFK has more information."

> *Enrichment from the paper, not said aloud.* The paper makes the "strictly more" concrete
> with unknot detection. Does the invariant detect the unknot — if a knot has the same
> invariant as the unknot, is it the unknot? For the Alexander polynomial, **no**: the
> Conway knot has Δ = 1, exactly like the unknot. For the Jones polynomial, unknown, and
> famously so. But for both homologies the answer is **yes** — Ozsváth–Szabó proved it for
> knot Floer homology, Kronheimer–Mrowka for Khovanov homology. That is a clean statement of
> exactly how much the upgrade buys.

### 4.2 Four-dimensional topology

Covered in §1 and §3.4. The four facts (ℝ⁴ uncountable, compact examples with infinitely
many structures, S⁴ unknown, SPC4 open), then Freedman and Donaldson in the 1980s as the
moment the smooth and topological worlds separated, then exotic pairs as the object of study.

### 4.3 Where the computable examples come from

Gauge theory: nonlinear elliptic PDEs from physics with an infinite-dimensional gauge
symmetry. Two equations in practice — anti-self-dual Yang–Mills (Donaldson, 1983) and
Seiberg–Witten (1994). He puts the Seiberg–Witten equations on the slide and immediately
tells the room not to worry about them; the captions record only that they "involve a Dirac
operator, a spinor and the curvature of some connection", which is right.

Counting solutions is hard, so you need structure: complex algebraic geometry, or symplectic
geometry, or a scalar curvature condition, or a connected-sum decomposition. On projective
algebraic surfaces the Yang–Mills solutions correspond to holomorphic vector bundles and the
Seiberg–Witten solutions to divisors, and both counts become tractable. That gets you exotic
structures on ℂP² # 9ℂP̄² and on K3, and — combining with cut-and-paste — on ℂP² # kℂP̄² for
every k ≥ 2.

The general rule of thumb, from the paper: **the bigger the manifold, the easier the
exotica.** More homology means more room to manoeuvre. On the small ones —
S⁴, S²×S², ℂP², ℂP²#ℂP̄², S¹×S³, T⁴ — the existence of exotic structures is still open.
Manolescu on the podium: "the simpler the manifold, the harder it is to construct exotic
structures, because there's less stuff to play with."

### 4.4–4.5 Kirby diagrams

Covered in §3.6. This is the second of the two background sections and it ends with the K3
picture.

### 4.6 Seiberg–Witten, monopole Floer, and cut-and-paste

Covered in §3.7. The strategy in one line: cut the four-manifold into handles, replace each
handle by its cobordism map, compose, and read off the number. "If you understand all the
monopole homologies and you understand the cobordism maps for some simple pieces, then you
can compute the invariants."

The catch is the first clause. Monopole Floer homology is itself defined by solving PDEs on
ℝ × Y, so you have replaced one hard analysis problem by many.

### 4.7 Heegaard Floer homology: replacing the PDE with a different PDE

Ozsváth and Szabó's move, around 2000, was to build a theory with the same formal properties
out of symplectic geometry instead of gauge theory. Manolescu: "instead of those equations
from physics, they use symplectic geometry and they count pseudo-holomorphic curves."

The heuristic that produces it — and this is genuinely the nicest piece of reasoning in the
paper, so here it is properly:

1. Split the three-manifold Y along a surface Σ into two handlebodies U₀ and U₁. This is a
   **Heegaard splitting**, and every Y has one.
2. Stretch the metric along Σ. In that limit, the equations on ℝ × Y degenerate: they become
   maps
   > u : ℝ × [0,1] → M(Σ)
   into M(Σ), the moduli space of solutions on ℝ² × Σ invariant under both ℝ-translations.
   This is dimensional reduction, and the "stretch the neck and the field theory localises"
   move is one you have seen in other guises.
3. M(Σ) turns out to carry a natural symplectic structure, and the maps u must satisfy a
   nonlinear analogue of the Cauchy–Riemann equations — they are **pseudo-holomorphic**.
4. So the gauge-theoretic Floer homology of Y ought to equal a purely symplectic invariant.
   In the Yang–Mills setting this is the **Atiyah–Floer conjecture**. In the Seiberg–Witten
   setting it became a construction.

The concrete output: the dimensionally-reduced Seiberg–Witten equations on a surface are the
**vortex equations**, and their moduli space is a symmetric product of the surface. So set

> M(Σ) = Sym^g(Σ) = (Σ × ⋯ × Σ) / S_g,

g copies of Σ modulo permutations, where g is the genus of Σ. The handlebody U₀ is specified
by g curves α₁,…,α_g on Σ, and U₁ by g curves β₁,…,β_g. These give two submanifolds

> 𝕋_α = α₁ × ⋯ × α_g,  𝕋_β = β₁ × ⋯ × β_g ⊂ Sym^g(Σ),

and Heegaard Floer homology HF(Y) is the homology of the complex whose generators are the
intersection points 𝕋_α ∩ 𝕋_β and whose differential counts pseudo-holomorphic strips
between them with boundary on the two.

The gain is real but partial: **the generators are now completely combinatorial** — a
generator is a g-tuple of points {x₁,…,x_g} with x_i ∈ α_i ∩ β_{σ(i)} for some permutation
σ, so you can enumerate them by hand. The differential still requires solving the nonlinear
Cauchy–Riemann equation.

Status of the various conjectures, which the talk gets right and I record because it is easy
to garble:

- Heegaard Floer homology **is** isomorphic to monopole (Seiberg–Witten) Floer homology.
  Proved, by Kutluhan–Lee–Taubes and independently by Colin–Ghiggini–Honda.
- The Ozsváth–Szabó four-manifold invariants are **conjecturally** the Seiberg–Witten
  invariants. Not proved. Manolescu: "that's okay, because it turns out that these
  invariants have many of the same properties. So for many purposes this can act as a
  replacement for Seiberg–Witten theory, and it's easier to compute."

### 4.8 Knot Floer homology by grid diagrams — the combinatorial heart

This is the section where the analysis disappears, and it is the one to actually learn.

He explicitly announces he will give a definition that is not the original one: "the original
definition involves symplectic geometry. The one I will present is just combinatorial. It
uses a certain way of presenting knots and links, and you can plug it into a computer and get
answers." The reference is Manolescu–Ozsváth–Sarkar, *A combinatorial description of knot
Floer homology*, Annals of Mathematics 169 (2009).

**The grid diagram.** Take the torus, drawn as a square with opposite sides identified. Put
an n × n grid on it: n horizontal circles α₁,…,α_n cutting it into n rows, and n vertical
circles β₁,…,β_n cutting it into n columns. Now place markings:

- n markings labelled O, exactly one in each row and exactly one in each column;
- n markings labelled X, likewise one per row and one per column.

Join each O to the X in its row by a horizontal segment, and each O to the X in its column by
a vertical segment. Where segments cross, **the vertical one goes over**. The result is a
planar diagram of a link. Every link arises this way. Manolescu's example is a 5×5 grid whose
link is the trefoil.

> ⚠ **Small error in the companion.** The paper's bulleted definition calls the β curves "n
> parallel *horizontal* curves … splitting the torus into n columns". They are vertical; the
> word is a typo, and the rest of the definition and the figure make that unambiguous.

Once you have the O's and X's, you can throw the link picture away. The two n-element
markings determine everything.

**The chain complex.** A **generator** is an n-tuple of grid points x = {x₁,…,x_n} with one
point on each horizontal circle and one on each vertical circle. Equivalently: a permutation.
So there are exactly **n! generators**, and the chain group is the free abelian group on
them. Manolescu's slide shows two generators on the 5×5 grid, one in red and one in blue.

**The differential** counts **empty rectangles**:

> ∂x = Σ_y r(x, y) · y

where r(x,y) counts rectangles from x to y. A rectangle can exist only when x and y differ in
exactly two rows (and hence exactly two columns) — then those two rows and two columns cut
the torus into four rectangles, and an orientation convention picks out the two that run
"from x to y". Such a rectangle counts if it is **empty**: it contains no O marking, no X
marking, and no other coordinate of x or y. It is counted with a sign, by a rule neither
source spells out.

Two features worth noticing. First, you are on a torus, so rectangles **wrap around** — the
top edge is glued to the bottom, the left to the right. Manolescu is explicit about this.
Second, the whole thing is finite and mechanical: n! generators, and for each pair you check
a handful of rectangles for emptiness. There are working computer programs.

> **Theorem (Manolescu–Ozsváth–Sarkar 2009).** Knot Floer homology, in all its versions, is
> algorithmically computable.

And now the sentence from §2 again, because this is where it belongs: the reason this works
is that isolated holomorphic discs in Sym^n(T²) with the given boundary conditions are in
**one-to-one correspondence** with empty rectangles. Not approximated by — in bijection with.
Each rectangle is a solution of the Seiberg–Witten equations on ℝ² × T².

One caveat the talk skips and the paper states: the homology of the complex as I described
it, written H̃FK, is not quite a link invariant. For an ℓ-component link it equals the honest
invariant ĤFK tensored with n − ℓ copies of a rank-two free abelian group. A normalisation,
not a problem.

### 4.9 Surgery formulas, and the theorem that is true and useless

Now the assembly. We have an invariant of links. We want an invariant of four-manifolds. The
bridge is the **surgery formula**, which relates the knot Floer homology of a framed link to
the Heegaard Floer homology of the three-manifold you get by surgery on it.

For a knot, this is Ozsváth–Szabó's integral surgery formula: HF(S³(𝕃)) is the homology of a
mapping cone

> A(L) → A(∅)

where A is a particular flavour of knot Floer homology and the framing λ is what defines the
map. A **mapping cone** here is just: build a bigger complex out of two complexes and a map
between them. And crucially the same formula identifies the **four-manifold** invariant of
the trace X(𝕃) with a specific element of that cone. So the four-manifold invariant is in
there.

For links, Manolescu and Ozsváth generalised it, and the price is steep: instead of a mapping
cone between two objects you get a **mapping hypercube**, involving the knot Floer homologies
of the link and of every sublink, together with maps between them, chain homotopies between
those maps, higher chain homotopies between the homotopies, and so on. Manolescu, being
candid:

> "To tell the whole truth, the surgery formulas use the link Floer complexes not just for
> the link but also for all of its sublinks — you have to understand those as well — and
> they're all related to each other by some chain maps, and then chain homotopies between
> them, and then also higher chain homotopies, and so on."

The combinatorial description covers the vertices of that hypercube directly (§4.8). The maps
and higher homotopies took more work, done in Manolescu–Ozsváth–Thurston, *Grid diagrams and
Heegaard Floer invariants*, Annals of Mathematics 201 (2025), by counting more complicated
shapes on the grid — not just rectangles. The consequence:

> **Theorem (Manolescu–Ozsváth–Thurston).** The Heegaard Floer homologies of three-manifolds,
> and the Ozsváth–Szabó four-manifold invariants (mod 2), are algorithmically computable.

The mod 2 is technical: the link surgery formula is proved only with ℤ/2 coefficients, is
expected to hold over ℤ, and mod 2 suffices to detect many exotic pairs anyway.

**And then he tells you it does not work.** This is the most valuable thirty seconds in the
lecture:

> "The bad news is that this theorem is a conceptual result. It's nice to know that you can
> do it like this combinatorially, in terms of instead of analysis, but it cannot be used in
> practice, because the size of the grid gets too big for interesting manifolds. So for the
> K3 surface, you have 22 components and you need a grid that's at least of size 88. So you
> need 88 factorial generators, and there's no way a computer can handle that."

88! is about 1.85 × 10^134. The number of atoms in the observable universe is about 10^80.
The reduction is exact, correct, and completely inert.

> The figure "at least 88" is the speaker's, from the podium; the paper says only that the
> generator count n! is super-exponential in n and that this makes computation extremely
> difficult. I have not verified the 88 independently.

### 4.10 What actually works

Three things, in increasing order of how ad hoc they are.

**Bordered Floer homology** (Lipshitz–Ozsváth–Thurston). Apply the cut-and-paste principle
one level down: decompose the *three*-manifold into simpler three-manifolds with boundary. It
works in practice and there are computer programs for the hat version of Heegaard Floer
homology, and a parallel theory for knots that decomposes a knot into tangles. But it has not
been developed far enough to handle four-manifold invariants directly.

**Handle-by-handle, exploiting the specific link.** For any particular four-manifold, cut it
into handles, and take advantage of whatever is special about the links you meet when
attaching the 2-handles. Ozsváth and Szabó did exactly this for the K3 surface. Manolescu:
"if the links are sufficiently simple, then you can do it without grids."

**The recent results, which are the reason the talk exists.** Levine, Lidman and Piccirillo
(2023) refined the handle-by-handle method — using both the relation between knot Floer
homology and surgery cobordism maps, and bordered Floer homology — and constructed a **new**
exotic ℂP² # 9ℂP̄², proving it exotic with the Ozsváth–Szabó invariant. That is already
notable, because until then Heegaard Floer theory in four dimensions had mostly been
re-proving things gauge theory already knew.

What came out of it was better than the example itself. Their manifold carries a free
involution. Quotient by it, and you get a manifold with fundamental group ℤ/2 and
**negative definite** intersection form. Hence:

> **Theorem (Levine–Lidman–Piccirillo).** There exists an exotic pair of closed orientable
> four-manifolds with definite intersection form.

The first ever, and §3.5 explains why that is a landmark. Two caveats, of which the talk
gives one and the paper both:

- It does **not** settle Question 3.2, because the manifolds are not simply connected — they
  have π₁ = ℤ/2. The talk says "definite intersection form" without flagging this; the paper
  is explicit. Take the paper's version.
- In later work, **Lidman and Piccirillo** (2025) used similar methods to construct an exotic
  ℂP² # 5ℂP̄². The talk attributes this to all three authors ("they also used a similar
  method"); the paper's reference [52] is Lidman–Piccirillo only.

A fourth application the talk omits: knot Floer homology was used by Juhász and Zemke to
compute Ozsváth–Szabó invariants of manifolds built by "concordance surgery" — a computation
nobody knows how to do on the Seiberg–Witten side.

### 4.11 Khovanov homology — the second combinatorial heart

Now the talk changes direction. Everything so far computed **existing** invariants. The rest
constructs a **new** one, starting from a knot invariant that has no analysis in it anywhere.

Manolescu: "the definition is algebraic from the start. It doesn't use gauge theory, it
doesn't use pseudo-holomorphic curves. It's just something that you can implement on a
computer and it's quite elementary."

Here it is in full. There is nothing hidden.

**Step 1: the cube of resolutions.** Take a link diagram D with n crossings. At each
crossing there are two ways to cut it open and reconnect the strands — call them the 0-
and the 1-resolution. Choosing one at every crossing gives a vector ε = (ε₁,…,ε_n) ∈ {0,1}ⁿ,
and the corresponding **complete resolution**: a picture with no crossings at all, hence just
a disjoint collection of circles. There are 2ⁿ of them, sitting at the vertices of a
hypercube.

(This is a direct categorification of the Kauffman bracket. The bracket satisfies
⟨D⟩ = A⟨D₀⟩ + A⁻¹⟨D₁⟩; iterating it n times gives a sum of 2ⁿ terms, one per vertex. Khovanov
replaces each term by a group.)

**Step 2: put a group at each vertex.** Let

> V = span{1, x},

a free abelian group of rank 2. If the resolution at ε consists of m circles, place V^{⊗m}
there. The chain group in degree k is the direct sum of all the V^{⊗m} over vertices ε with
ε₁ + ⋯ + ε_n = k.

**Step 3: the differential.** Two vertices ε and ε′ are joined by an edge if they agree
everywhere except at one crossing j, where ε_j = 0 and ε′_j = 1. Going along that edge, the
picture changes in exactly one of two ways: two circles merge into one, or one circle splits
into two.

- **Merge** → use the multiplication m : V ⊗ V → V given by
  > 1·1 = 1,  1·x = x·1 = x,  x·x = 0,
  tensored with the identity on all the unchanged circles.
- **Split** → use the comultiplication Δ : V → V ⊗ V given by
  > Δ(1) = 1 ⊗ x + x ⊗ 1,  Δ(x) = x ⊗ x,
  again tensored with the identity elsewhere.

Multiply each edge's contribution by the sign

> (−1)^{ε₁ + ⋯ + ε_{j−1}}.

Then d² = 0, you have a chain complex, and its homology is **Khovanov homology** Kh(K). It
is a link invariant — independent of the diagram.

The algebra (V, m, Δ) is a **Frobenius algebra**, which is what makes the merges and splits
consistent. Manolescu names it and moves on; so do I. You will build this complex for the
Hopf link by hand in §6.2, and you will see that the sign is exactly what makes d² = 0.

**Step 4: the four-dimensional property.** This is why Khovanov homology is in a
four-manifolds talk. Suppose Σ is a smoothly embedded surface in [0,1] × ℝ³ whose boundary is
a link L₀ at one end and a link L₁ at the other — a **link cobordism**, a movie of a link
turning into another link. Then there is a well-defined map

> Kh(Σ) : Kh(L₀) → Kh(L₁),

and composing cobordisms composes the maps. Khovanov homology is a TQFT in the sense of
§3.7 — but a purely algebraic one, with no PDE underneath it. That is the property the whole
next section is built on.

### 4.12 Skein lasagna modules

Morrison, Walker and Wedrich, 2019 (published 2022). The construction takes a link invariant
with good cobordism behaviour and manufactures from it an invariant of four-manifolds.

The model is one dimension down. For a three-manifold Y, the **Kauffman bracket skein
module** KBSM(Y) is generated by all framed links in Y, modulo the local Kauffman relations
imposed inside small balls. For Y = S³ it collapses to ℤ[A, A⁻¹] and the class of a link is
just its Kauffman bracket — so the skein module generalises the Jones polynomial to arbitrary
three-manifolds. It is easy to define and hard to compute; Gunningham, Jordan and Safronov
proved a conjecture of Witten that it is at least finite dimensional after tensoring with
ℂ(A). (This paragraph is paper-only; the talk skips the three-dimensional model.)

**The four-dimensional version.** Let X be a compact four-manifold with boundary Y, and let
𝕃 be a framed link in Y. Here is the definition, and I will describe the pictures since you
cannot see Figures 13 and 14.

> **A lasagna filling** F of X with boundary 𝕃 consists of:
>
> 1. a finite collection of disjoint four-dimensional balls B₁,…,B_k embedded in the interior
>    of X — the **input balls**;
> 2. a framed surface Σ properly embedded in what is left, X minus the balls, meeting the
>    boundary ∂X in the link 𝕃, and meeting each ball's boundary ∂B_i — which is a copy of S³ —
>    in a link 𝕃_i;
> 3. for each i, a chosen element v_i ∈ Kh(𝕃_i).

The picture: X is a blob. On its outer boundary sits the link 𝕃. Inside, floating, are
several four-dimensional bubbles, each with a link drawn on its three-sphere surface. A
two-dimensional surface runs through the interior, ending on all of those links. Each bubble
is labelled with an element of the Khovanov homology of the link on it.

The logic behind the definition is worth stating plainly, because the definition looks
arbitrary until you see it. You want to associate something to a link in the boundary of an
*arbitrary* four-manifold. You only know how to associate something — Khovanov homology — to
a link in S³. So: find every copy of S³ you can inside X, namely the boundaries of embedded
balls, put links on them, use Khovanov homology there, and connect everything up with
surfaces. Manolescu says exactly this.

> **The skein lasagna module** 𝒮(X; 𝕃) is the free abelian group on lasagna fillings, modulo
> two relations:
>
> - **Multilinearity** in the labels v_i. Same filling with label v₁ plus same filling with
>   label v₂ equals same filling with label v₁ + v₂.
> - **Refinement.** If a filling F₁ has an input ball B_i labelled v_i, and F₂ is obtained by
>   replacing that ball with a whole lasagna filling F₃ of a four-ball, with labels v′_i, then
>   F₁ ~ F₂ **provided** v_i = Kh(Σ′)(⊗ v′_i) — the Khovanov cobordism map of the surface
>   inside the ball sends the finer labels to the coarser one.

The second relation is the one doing the work, and it needs a refinement of the cobordism
property from §4.11 that Morrison–Walker–Wedrich had to prove: given balls B₁,…,B_k inside a
larger ball B and a framed surface in the region between them, there is a well-defined map
⊗ Kh(𝕃_i) → Kh(𝕃). (The proof removes a basepoint from each sphere and a tree joining them,
which flattens the region into [0,1] × ℝ³ where the ordinary map applies, and then shows the
answer does not depend on the tree.)

Manolescu, on why the relation is not merely bureaucratic:

> "Roughly, I look at all possible Khovanov homologies of links inside, and I divide by all
> local relations coming from cobordism maps. And it turns out that this makes the abelian
> group much smaller. In some cases it makes it finite dimensional, and it's something
> manageable."

Take 𝕃 to be the **empty link** and you get an invariant of the four-manifold alone, written
𝒮(X). That is the four-manifold invariant.

Properties: it is functorial under cobordisms; the bigrading on Khovanov homology descends to
it; and there is a further decomposition by the relative homology class α of the surface in
the filling. Those gradings matter — the Ren–Willis argument in §5 lives entirely in one
graded piece.

And the name. He asks the question the room is thinking:

> "The question you all were wondering — why is this called lasagna? Well, the answer is kind
> of silly. It's just because it's two-dimensional. Before this, people were studying this one
> dimension down, where the balls were three-dimensional and instead of the blue surfaces you
> had some arcs, some tangles, and Jones called that *spaghetti with meatballs*. So then
> Morrison, Walker and Wedrich, when they defined this, they had a two-dimensional version. So
> they thought of some two-dimensional pasta, and there came the lasagna module."

The construction is general: it applies to any link homology with the right cobordism
behaviour. Morrison–Walker–Wedrich do it for the Khovanov–Rozansky homologies attached to
𝔤𝔩_N for every N (N = 2 being Khovanov homology), and Chen has done it for knot Floer homology,
producing a **Floer lasagna module**.

### 4.13 Computing it

The definition is abstract. The talk is honest that this is the problem: "the definition kind
of looks like abstract nonsense; the challenge is to compute this group."

**The base case.** For X = D⁴, the four-ball, the map that sends a filling to
Kh(Σ)(⊗ v_i) — apply the cobordism map of the surface to all the labels — is an
**isomorphism** 𝒮(D⁴; 𝕃) ≅ Kh(𝕃). So skein lasagna modules genuinely generalise Khovanov
homology, and the four-ball recovers it exactly.

**The handle formulas.** Manolescu with his student Ikshu Neithalath, and later with Walker
and Wedrich, worked out how 𝒮 behaves when you attach a handle — which, with §3.6, means you
can in principle compute from a Kirby diagram. The formulas get harder as the handle index
gets smaller. Attaching a 4-handle changes nothing (so 𝒮(D⁴) = 𝒮(S⁴) = ℤ). The 3-handle
formula is a quotient by the image of a difference of two cobordism maps. The 1-handle formula
involves Hochschild homology of a category of tangles and the paper declines to state it.

The one to look at is the **2-handle formula**, because 2-handles are where the knots are.
Suppose W′ is built from W by attaching 2-handles along a framed link 𝕂 in ∂W. Write
𝕂(r₁, r₂) for the **cable** of 𝕂: take r₁ + r₂ parallel push-off copies of 𝕂 according to its
framing, with r₁ oriented the same way as 𝕂 and r₂ the opposite way. Then

> 𝒮(W′; 𝕃) ≅ ⊕_{r₁, r₂ ∈ ℕ} 𝒮(W; 𝕂(r₁,r₂) ∪ 𝕃) / ~

where the relation ~ identifies permuted strands and imposes two relations coming from a
specific cobordism Z that adds one strand of each orientation.

Manolescu's plain summary: "our formula takes the form of a colimit over the Khovanov
homologies of all the cables of the knot. So understanding the Khovanov homology of links
allows you to understand the skein lasagna module of surgery on the link."

And immediately the catch: "it's still not the kind of thing you can plug into a computer,
because you need an infinite amount of data. You need the Khovanov homology of *all* the
cables."

**Sample computations**, refined by Sullivan–Zhang and by Ren–Willis:

| Four-manifold | 𝒮 |
|---|---|
| D⁴, S⁴ | ℤ |
| ℂP² | 0 |
| S² × S² | 0 |
| ℂP̄² (reversed orientation) | non-zero; only partially computed |

The last row is the interesting one. **𝒮(ℂP²) = 0 but 𝒮(ℂP̄²) ≠ 0**, so the invariant sees
orientation. Manolescu: "what's interesting is that it depends on the orientation, so this
makes it somewhat similar to the Seiberg–Witten invariants." Which is exactly the property
you want if the goal is detecting smooth structure.

> **A talk/paper discrepancy, unresolved.** The talk says: "you also get a non-zero answer
> for S¹ × S³ … for S¹ × S³ I think we have a full computation." The paper contains no
> computation for S¹ × S³. What it contains, in §6.4, is a computation for **S¹ × D³**, the
> four-manifold with boundary S¹ × S², with a specific link 𝕃_p in the boundary consisting of
> 2p parallel longitudes, half oriented each way:
>
> > 𝒮(S¹ × D³, 𝕃_p) ⊗ ℚ ≅ ℚ if p = 0; ℚ⁴ if p = 1; ℚ^∞ if p = ∞.
>
> The p = 0 case is the empty link and gives ℚ, which is non-zero — consistent with the
> talk's claim in spirit. S¹ × D³ and S¹ × S³ are different manifolds. I am quoting both
> sources rather than deciding that the speaker misspoke; he was working from slides I cannot
> see, and this is exactly the kind of thing the ½-line caption of a slide would settle.

### 4.14 The section that was never delivered — §7 of the paper

**Everything in this subsection is paper-only.** The lecture ends after §4.13 with the open
question in §5 below. I include §7 because it is the part of the paper closest to your work,
and because the abstract advertises it, so you would otherwise expect it.

A knot K ⊂ S³ is **slice** if it bounds a smoothly embedded disc in the four-ball D⁴, with
the disc's boundary being K sitting in ∂D⁴ = S³. This is a genuinely four-dimensional
property: in S⁴ every knot bounds a disc (you can undo the crossings by moving through the
extra dimension), and in S³ only the unknot bounds one, so the four-ball is where the
question is interesting.

A **ribbon** knot is one bounding an immersed disc in ℝ³ whose only self-intersections are of
a specific benign type; equivalently, a knot which some number k of band attachments turns
into the (k+1)-component unlink. Every ribbon knot is slice. Whether every slice knot is
ribbon is the **slice-ribbon conjecture**, open since 1966.

Two facts about the computational status, and they are unusual:

- Many three-dimensional problems are decidable — there are algorithms to decide whether two
  knots are isotopic, or whether two three-manifolds are homeomorphic. Many four-dimensional
  ones are **undecidable**, including the homeomorphism problem for four-manifolds.
- For sliceness, **nobody knows which side it is on.** There is no known algorithm and no
  proof that none exists.

In practice you attack it from both ends: **obstructions** (the Fox–Milnor condition on the
Alexander polynomial; the signature; invariants named τ, ε, ν, δ from Floer theory; and
Rasmussen's s-invariant from Khovanov homology) and **constructions** (search for bands that
turn the knot into an unlink).

And here is the paragraph that should interest you professionally. Dunfield and Gong ran the
combined obstruction-and-construction pipeline over **all ≈ 350 million prime knots with up
to 19 crossings**. Result: about 99.5% are provably not slice, about 0.5% are provably slice,
and for **0.003% — roughly 11,400 knots — the pipeline could not decide.** The smallest
undecided knots have 13 crossings. Separately, Gukov, Halverson, Manolescu and Ruehle used
Bayesian optimisation to search for ribbon bands.

Then the programme. Define, relative to a closed four-manifold X, three graded versions of
sliceness for a knot K in the boundary of X minus a ball: slice (bounds a disc), **H-slice**
(bounds a disc whose homology class is zero), and **k-slice** (bounds a disc of
self-intersection −k). Then reverse the usual question: instead of fixing X and asking which
knots are slice in it, fix K and ask what its sliceness tells you about X. Manolescu, Marengon
and Piccirillo proved that H-sliceness **does** detect exotic pairs — the right-handed trefoil
is H-slice in #3ℂP² # 20ℂP̄² but not in K3 # ℂP̄², two homeomorphic manifolds.

The most ambitious version aims at SPC4 itself. Suppose you find two knots K, K′ with the same
0-surgery — a **0-friend pair** — such that K is slice and K′ is not. Then glue the complement
of K's slice disc in D⁴ to the trace of the 0-surgery on K′:

> W = (D⁴ ∖ nbhd(Δ)) ∪_{S³(K,0)} X(K′, 0).

W is a homotopy four-sphere, and K′ is slice in it by construction. But K′ is not slice in S⁴.
So W is not diffeomorphic to S⁴, and SPC4 is false.

No such pair has been found. Manolescu and Piccirillo gave a general construction of 0-friends
via "RBG links" and proposed five candidate pairs; Nakamura shortly afterwards proved the K's
in all five were not slice. Dunfield and Gong found further candidates from their sweep,
including a knot whose 0-friend is provably ribbon while the knot itself resists every band
search — so either the bands exist and are hard to find, or that knot is a counterexample to
SPC4 or to the slice-ribbon conjecture.

---

## 5. The one argument: Ren and Willis

This is the talk's destination, and it is fully reconstructible.

**The objects.** Take two knots:

> K₁ = −5₂ (the mirror image of the knot catalogued as 5₂)
> K₂ = P(3, −3, −8), a pretzel knot

For each, form the trace of −1 surgery: attach a single 2-handle to D⁴ along the knot with
framing −1 (§3.6). Call the results

> W₁ = X(K₁, −1),  W₂ = X(K₂, −1).

Each is a compact four-manifold with boundary, built from exactly one 0-handle and one
2-handle. About as simple as a non-trivial four-manifold gets.

**Step 1 — they are homeomorphic.** Three facts: the two surgeries give the same
three-manifold, S³(K₁,−1) = S³(K₂,−1), so W₁ and W₂ have the same boundary; both are simply
connected; and they have the same homology and the same intersection form. A theorem of Boyer
classifying simply-connected compact four-manifolds with prescribed boundary then forces them
to be **homeomorphic**. Manolescu: "so they are homeomorphic but they are not
diffeomorphic."

**Step 2 — they are not diffeomorphic.** Compute the skein lasagna module in one bigrading,
in one homology class, over the rationals. Write 𝒮_{i,j}(W; α) for the piece in Khovanov
bigrading (i,j) and filling-homology-class α; take i = 0 and α = 1, the generator. Then

> 𝒮_{0,q}(W₁; 1) ⊗ ℚ ≅ ℚ if q = 1 or 3, and 0 otherwise;
>
> 𝒮_{0,q}(W₂; 1) ⊗ ℚ ≅ ℚ if q = −1 or 1, and 0 otherwise.

They differ at q = −1 and at q = 3. Manolescu's spoken version: "when q equals −1, the one on
the left has module zero and the one on the right has non-trivial module — it contains at
least a copy of ℚ." Since 𝒮 is a diffeomorphism invariant, W₁ and W₂ are **not
diffeomorphic**. ∎

**Step 3 — why the computation is possible at all.** By §4.13, the 2-handle formula expresses
𝒮(W_i) as a colimit over the Khovanov homologies of *all* the cables of K_i — infinitely much
data. It is tractable here only because each knot has a special property that pins down enough
of its cables' Khovanov homology:

- K₁ = −5₂ admits a diagram with **only positive crossings**;
- K₂ = P(3, −3, −8) is **slice** (in the sense of §4.14).

The calculations are partial — only the i = 0, α = 1 part, only over ℚ — and that is enough,
because to distinguish two objects you only need one coordinate where they disagree.

**Step 4 — what is actually new.** These two manifolds were already known to be an exotic
pair. Akbulut proved it in 1991 using gauge theory. What Ren and Willis produced is the
**first analysis-free proof** of the existence of an exotic pair of compact orientable
four-manifolds. Manolescu:

> "So we know from topology that they are homeomorphic, and now we have an analysis-free
> proof that they are not diffeomorphic. So this tells you that in this case at least,
> Khovanov homology can act as some sort of replacement for gauge theory."

Trace the dependencies. Step 1 uses Freedman-era topology. Step 2 uses Khovanov homology,
which is: a hypercube of resolutions, a rank-2 abelian group, a multiplication, a
comultiplication, and some signs. **No PDE. No metric. No moduli space. No compactness
theorem.** A fact about smooth structures in dimension four, which for forty years could only
be reached by nonlinear elliptic analysis, proved by linear algebra over ℤ.

And in the same paper Ren and Willis exhibited **new** exotic pairs — detectable by skein
lasagna modules and not, at present, by gauge theory or Heegaard Floer homology. The new tool
is not merely an alternative route to old results.

**The talk ends on the limitation.** Every example so far has non-empty boundary, which
matters because a manifold with boundary can be built from a single 2-handle — one knot, one
integer. A closed manifold like K3 needs 22 of them, and the cable computation gets
correspondingly worse.

> **Open question (talk's final slide).** Can skein lasagna modules detect exotic smooth
> structures on some **closed** four-manifold?

Gauge theory can. Heegaard Floer theory can. The new method, so far, cannot.

---

## 6. Do this by hand

Two exercises. The first is the polynomial layer; the second is the homology layer. Between
them they cover the entire computational content of the talk, and neither needs anything you
do not already have. Budget an hour.

### 6.1 The trefoil, twice (30 minutes, pen)

Use only: Δ(unknot) = 1, V(unknot) = 1, and the two skein relations

> Δ(L₊) − Δ(L₋) = (q^{1/2} − q^{−1/2}) Δ(L₀)
> q⁻¹ V(L₊) − q V(L₋) = (q^{1/2} − q^{−1/2}) V(L₀)

together with the fact (proved in the paper by one application of the Alexander relation)
that Δ(2-component unlink) = 0.

1. Compute Δ of the positive Hopf link, then Δ of the right-handed trefoil. Check your answer
   against the paper's stated Δ(T) = q⁻¹ − 1 + q.
2. Compute V of the 2-component unlink, then V of the positive Hopf link, then V of the
   right-handed trefoil.
3. *(Draws on §4.14, paper only.)* The Fox–Milnor condition says a slice knot has
   Δ(K) = f(q) f(q⁻¹). Deduce that |Δ(K)(−1)| must be a perfect square, and use it to show
   the trefoil is not slice.

<details>
<summary>Solutions</summary>

**(1) Alexander.** For the Hopf link, pick one of its two crossings. Changing it: L₊ is the
positive Hopf link, L₋ is the 2-component unlink, and L₀ is the unknot. So

> Δ(H₊) − Δ(unlink₂) = (q^{1/2} − q^{−1/2}) · Δ(unknot) = q^{1/2} − q^{−1/2}.

Since Δ(unlink₂) = 0, **Δ(H₊) = q^{1/2} − q^{−1/2}.**

For the trefoil, take the standard 3-crossing diagram, all crossings positive. Change one:
L₊ = trefoil T, L₋ = unknot, L₀ = positive Hopf link. So

> Δ(T) − 1 = (q^{1/2} − q^{−1/2}) · (q^{1/2} − q^{−1/2}) = q − 2 + q⁻¹,

giving **Δ(T) = q⁻¹ − 1 + q.** ✓ Matches the paper. And since Δ(unknot) = 1 ≠ Δ(T), the
trefoil is knotted.

**(2) Jones.** First the unlink. Take a diagram of the unknot with one extra kink, so that
L₊ and L₋ are both the unknot and L₀ is the 2-component unlink:

> q⁻¹ · 1 − q · 1 = (q^{1/2} − q^{−1/2}) V(unlink₂).

Factor q⁻¹ − q = −(q − q⁻¹) = −(q^{1/2} − q^{−1/2})(q^{1/2} + q^{−1/2}). Cancel:

> **V(unlink₂) = −(q^{1/2} + q^{−1/2}).**

Hopf link, same crossing choice as before:

> q⁻¹V(H₊) − q·(−(q^{1/2}+q^{−1/2})) = (q^{1/2} − q^{−1/2}) · 1
> q⁻¹V(H₊) = q^{1/2} − q^{−1/2} − q^{3/2} − q^{1/2} = −q^{−1/2} − q^{3/2}
> **V(H₊) = −q^{1/2} − q^{5/2}.**

Trefoil:

> q⁻¹V(T) − q·1 = (q^{1/2} − q^{−1/2})(−q^{1/2} − q^{5/2}) = −q − q³ + 1 + q²
> q⁻¹V(T) = 1 + q² − q³
> **V(T) = q + q³ − q⁴.**

That is the standard Jones polynomial of the right-handed trefoil in this normalisation, and
it is a good self-check on your sign conventions: if you get q⁻¹ + q⁻³ − q⁻⁴ you have built
the left-handed trefoil, which is the mirror image, and the two are genuinely different knots
— the Jones polynomial proves it.

**(3) Fox–Milnor.** If Δ(K) = f(q)f(q⁻¹), then evaluating at q = −1 gives
Δ(K)(−1) = f(−1) f(−1) = f(−1)². So |Δ(K)(−1)| is a perfect square. (The standard statement
allows an extra unit ±q^k, which at q = −1 contributes only ±1, so the conclusion survives.)

For the trefoil, Δ(T)(−1) = (−1)⁻¹ − 1 + (−1) = −1 − 1 − 1 = **−3**, so |Δ(T)(−1)| = 3, which
is not a square. **The trefoil is not slice.** ∎

The quantity |Δ(K)(−1)| is the **determinant** of the knot, and you have just shown a slice
knot has square determinant. This is the cheapest genuine four-dimensional obstruction in the
subject: a one-line evaluation of a polynomial rules out the existence of any smooth disc in
the four-ball.

</details>

### 6.2 The Khovanov complex of the Hopf link (30 minutes, pen)

Build the object from §4.11 completely, for the two-crossing diagram of the Hopf link. Work
ungraded — both the talk and the paper decline to define the bigradings, so anything needing
them is outside our sources.

Setup: 2 crossings, so 4 vertices ε ∈ {0,1}². In this diagram the resolutions ε = (0,0) and
ε = (1,1) each consist of **two** circles, and ε = (0,1) and ε = (1,0) each consist of
**one**. (Draw it and check; the transcript confirms the pattern — "to each resolution I
assign some tensor product, in this case either V or V ⊗ V".)

1. Write down the three chain groups C⁰, C¹, C² and their ranks.
2. Write down the four edge maps, with the sign rule (−1)^{ε₁+⋯+ε_{j−1}} applied to each,
   where j is the crossing that changes.
3. Verify d² = 0, and identify precisely which sign makes it work.
4. Compute the three homology groups and the total rank.
5. Check the Euler characteristic upstairs against the Euler characteristic downstairs.

<details>
<summary>Solutions</summary>

**(1)** V = span{1, x}, rank 2.

> C⁰ = V ⊗ V (from vertex 00), rank 4
> C¹ = V ⊕ V (from vertices 10 and 01), rank 4
> C² = V ⊗ V (from vertex 11), rank 4

**(2)** Edges out of 00 merge two circles into one, so they use m. Edges into 11 split one
circle into two, so they use Δ.

- 00 → 10 changes crossing j = 1: sign (−1)^{(empty sum)} = **+1**. Map: m.
- 00 → 01 changes crossing j = 2: sign (−1)^{ε₁} = (−1)⁰ = **+1**. Map: m.
- 01 → 11 changes crossing j = 1: sign (−1)^{(empty)} = **+1**. Map: Δ.
- 10 → 11 changes crossing j = 2: sign (−1)^{ε₁} = (−1)¹ = **−1**. Map: Δ.

Writing C¹ = V_{10} ⊕ V_{01}:

> d⁰(v) = ( m(v), m(v) )
> d¹(a, b) = −Δ(a) + Δ(b)

**(3)** d¹(d⁰(v)) = −Δ(m(v)) + Δ(m(v)) = 0. The **minus sign on the 10 → 11 edge** is
exactly what makes the square anticommute rather than commute, and hence what makes the
composite vanish. Without it you would get 2Δ(m(v)) and no chain complex. That is the whole
job of the sign rule.

**(4)** With m(1⊗1) = 1, m(1⊗x) = m(x⊗1) = x, m(x⊗x) = 0 and Δ(1) = 1⊗x + x⊗1,
Δ(x) = x⊗x:

- ker d⁰ = ker m = span{ x⊗x, 1⊗x − x⊗1 }, rank 2.
- im d⁰ = { (w,w) : w ∈ im m } = { (w,w) : w ∈ V }, rank 2 (m is onto).
- ker d¹ = { (a,b) : Δ(a) = Δ(b) } = { (a,a) }, rank 2, since Δ is injective.
- im d¹ = Δ(V) = span{ 1⊗x + x⊗1, x⊗x }, rank 2.

Hence

> H⁰ = ker d⁰ = span{ x⊗x, 1⊗x − x⊗1 } ≅ **ℤ²**
> H¹ = ker d¹ / im d⁰ = {(a,a)} / {(w,w)} = **0**
> H² = C² / im d¹ = (V⊗V) / span{1⊗x + x⊗1, x⊗x} ≅ **ℤ²**
>   (generated by the images of 1⊗1 and 1⊗x, with x⊗1 ≡ −1⊗x)

**Total rank 4**, all free, no torsion. That is the correct answer: the Khovanov homology of
the Hopf link has total rank 4.

**(5)** Upstairs: 4 − 4 + 4 = 4. Downstairs: 2 − 0 + 2 = 4. Equal, as §3.1 promised. ✓

**What you just did.** You computed a link invariant with nothing but two 4×4 integer
matrices. This is the object that, run through the machinery of §4.12 and §4.13, produces the
first proof that two four-manifolds are homeomorphic-but-not-diffeomorphic without solving a
single differential equation. Notice also H¹ = 0 with C¹ of rank 4 — the middle group
collapses entirely, which is what §3.1's point 1 means when it says the chain groups depend on
the diagram and the homology does not.

> **Reconstructed:** the assignment of which vertices carry two circles is read off the
> standard two-crossing Hopf link diagram, since paper Figure 12 is not text-extractable.
> **What would verify it:** draw the two-crossing Hopf link, resolve both crossings the same
> way, and count circles — you get 2; resolve them oppositely and you get 1. The sign
> convention and the maps m, Δ are quoted verbatim from the paper.

</details>

---

## 7. What is actually useful to you

Four things, in decreasing order of how transferable they are.

### 7.1 "Algorithmically computable" is a claim about existence, not about capability

The single most useful thirty seconds in the lecture is §4.9. Manolescu proves a theorem
whose statement is exactly what the field had wanted for a decade — Heegaard Floer homology
and the four-manifold invariants are algorithmically computable — and then tells the room, in
the next breath, that the algorithm cannot be run. K3 needs a grid of size 88, hence 88!
generators, which is 10^134.

He does not present this as a failure. He presents it as the correct status of the result: a
conceptual result, of little use in practice. And then the talk spends its remaining time on
what *did* work, which was uniformly **ad hoc, per-instance methods that exploit something
special about the particular link in front of you** — this knot has an all-positive diagram,
that one is slice, this manifold's handles happen to be simple.

You will recognise this shape. A general solver that provably handles every case, and a
collection of special-case tricks that actually return answers; the general solver being
correct is not the same as the general solver being useful; and progress coming from the
tricks. The discipline the talk models is: **state the general result honestly, including
the complexity that kills it, and then be specific about which special structure each real
computation actually exploited.** Levine–Lidman–Piccirillo did not run an algorithm. They
built one manifold, handle by handle, using facts about its particular links.

### 7.2 Change the representation until the analysis becomes a lattice count

The technical spine of the talk is a chain of representation changes, each one trading a
harder object for an equivalent easier one:

| From | To | By what |
|---|---|---|
| a four-manifold | a framed link in S³ | Morse theory / Kirby diagrams |
| a four-manifold invariant | a composite of cobordism maps | TQFT / transfer matrix |
| Seiberg–Witten Floer homology | Heegaard Floer homology | stretch the neck, dimensional reduction |
| pseudo-holomorphic discs in Sym^n(T²) | empty rectangles on a grid | grid diagrams |
| the Jones polynomial | a cube of tensor products | categorification |

The last two are exact bijections, not approximations. And each step is chosen so that the
*next* step becomes possible: you go to Kirby diagrams so you can cut into handles, you cut
into handles so you can compose local maps, you use grids so the local maps become countable.

The general move — do not attack the hard object, find a presentation of it in which the hard
part becomes finite, then verify the presentation-independence — is the one worth carrying.
The verification is not optional and is where most of the work is: §3.1's point 1 is the
reason all of this is mathematics rather than bookkeeping.

### 7.3 Replacing a whole toolchain with a cheaper one that answers the same question

Ren–Willis (§5) did not find a new theorem. They re-proved a theorem from 1991. What was new
was that the proof used **no analysis**: a fact previously reachable only through nonlinear
elliptic PDE became reachable through finite linear algebra.

Two things follow, and both are general.

First, the value of a re-proof is not zero and is not sentimental: it is that the new proof
has a **different failure surface**. In the same paper, Ren and Willis found examples the old
toolchain cannot reach at all. A cheaper method with a different set of blind spots
immediately extends past the expensive one somewhere.

Second, the honest accounting Manolescu gives: "there are still many examples where we only
know how to do it with gauge theory, but in this one we can do it either way." Neither method
dominates. Both are kept.

### 7.4 The paper's search programme is your professional territory

§4.14 — which the lecture never delivered — contains a piece of work that sits squarely in
your domain. Dunfield and Gong ran an automated obstruction-plus-construction pipeline over
**350 million knots**, resolving sliceness for 99.997% of them and leaving ~11,400 undecided,
including one whose resolution would falsify either the smooth four-dimensional Poincaré
conjecture or the slice-ribbon conjecture. Gukov, Halverson, Manolescu and Ruehle applied
Bayesian optimisation to the band-search half of the problem.

Note the architecture, because it is exactly the architecture of a well-built agent system.
There are two engines pointing in opposite directions — one trying to prove the knot is not
slice by computing obstructions, one trying to prove it is slice by finding an explicit
construction — and a knot is resolved when either fires. The residue is the set where both
engines fail, and that residue is where the mathematics is. The residue is the product. It is
also, notably, tiny and precisely located: 11,400 objects out of 350 million, with the
smallest at 13 crossings.

Where the interaction between machine search and mathematics is the subject rather than a
sidelight, see `shape-of-math-kontorovich.md` in this directory, which is entirely about
formal verification and AI in mathematics. I am not reproducing that discussion here.

---

## 8. Where to read next

1. **Manolescu, *From knots to four-manifolds*.**
   [arXiv:2601.05425](https://arxiv.org/abs/2601.05425) — the written version of this talk and
   the source of every formula above. Twenty-nine pages, nineteen figures, and the figures are
   the point: everything I had to describe in words is drawn there. Sections 2, 3 and 4 are
   readable straight through with this tutorial beside you; §7 is the material the lecture
   never reached.
2. **Gompf and Stipsicz, *4-manifolds and Kirby calculus*.** Graduate Studies in Mathematics
   20, AMS 1999. The standard reference for §3.6 — handle decompositions, Kirby diagrams, and
   the moves relating two diagrams of the same manifold. If you want to be able to *draw*
   rather than read, this is the book.
3. **Ozsváth, Stipsicz and Szabó, *Grid homology for knots and links*.** Mathematical Surveys
   and Monographs 208, AMS 2015. A whole textbook developing knot Floer homology through the
   combinatorial grid definition of §4.8, with no symplectic geometry required. This is the
   one place in the subject where a reader with your background can go from zero to the
   research frontier without acquiring a new field first.

---

## 9. Self-test

<details>
<summary>1. Why can homology and the fundamental group never detect an exotic pair?</summary>

Because both are invariants of homotopy type, which is strictly coarser than homeomorphism,
which is strictly coarser than diffeomorphism. An exotic pair is by definition homeomorphic,
so it agrees on every homotopy invariant. Detecting the difference requires an invariant that
depends on the smooth structure, and the only known constructions do so by writing down a
differential equation — which needs a smooth structure to even be posed — and counting its
solutions in a metric-independent way.
</details>

<details>
<summary>2. What is a Kirby diagram, and what theorem makes it possible?</summary>

A picture of a framed link — knotted circles with an integer on each component — encoding a
handle decomposition of a four-manifold: the 1-handles as pairs of identified balls, the
2-handles as the framed link. Two ingredients make it work. Morse theory says every smooth
manifold decomposes into handles, indexed by the critical points of a generic function.
Lickorish–Wallace says every closed oriented three-manifold is surgery on a framed link in S³,
and the same framed link data specifies the four-manifold (the surgery trace) that the
three-manifold bounds. The 3- and 4-handles need no extra data, by Laudenbach–Poénaru.
</details>

<details>
<summary>3. What is homology of a chain complex, and why is the invariant taken there rather than at the chain groups?</summary>

Given maps ∂_k : C_k → C_{k−1} with ∂∘∂ = 0, homology is H_k = ker ∂_k / im ∂_{k+1}. It is
finite linear algebra — two null spaces, one quotient. The chain groups depend on the
presentation used to build them (a diagram, a grid, a triangulation) and change when you
change it; the homology does not. That independence is what makes it an invariant. It is also
strictly stronger than the alternating sum of ranks, which is the Euler characteristic — and
that is exactly the relationship between knot Floer homology and the Alexander polynomial, and
between Khovanov homology and the Jones polynomial.
</details>

<details>
<summary>4. Describe the grid-diagram definition of knot Floer homology.</summary>

Draw an n × n grid on a torus. Place n O-markings and n X-markings, one of each per row and
per column; joining O's to X's (verticals over horizontals) draws the link. Generators of the
chain complex are n-tuples of grid points, one on each horizontal and each vertical circle —
so n! of them, one per permutation. The differential ∂x = Σ r(x,y) y counts **empty
rectangles** from x to y: x and y must differ in exactly two rows, the rectangle must contain
no O, no X, and no other coordinate of x or y, and it may wrap around the torus. Signs by a
convention neither source spells out. The homology is (a version of) knot Floer homology, and
it is algorithmically computable.
</details>

<details>
<summary>5. What is the connection between an empty rectangle and a partial differential equation?</summary>

They are the same thing. Isolated pseudo-holomorphic discs in the symmetric product Sym^n(T²)
with boundary on the two Lagrangian tori are in one-to-one correspondence with empty
rectangles on the grid. Since the symmetric product is the moduli space of vortices — the
dimensionally-reduced Seiberg–Witten equations on a surface — each rectangle corresponds to a
solution of the Seiberg–Witten equations on ℝ² × T². The correspondence is a bijection, not a
discretisation: the counts are equal, not approximately equal.
</details>

<details>
<summary>6. State the algorithmic-computability theorem, and say why it does not help.</summary>

Manolescu–Ozsváth–Thurston: the Heegaard Floer homologies of three-manifolds and the
Ozsváth–Szabó four-manifold invariants (mod 2) are algorithmically computable. It does not
help because the grid size for an interesting manifold is large and the generator count is
n!, which is super-exponential. K3 has a 22-component Kirby diagram and, by the speaker's
figure, needs a grid of size at least 88 — so 88! ≈ 10^134 generators. Every real computation
in the field instead uses ad hoc methods exploiting special properties of the specific links
that appear.
</details>

<details>
<summary>7. Give the Khovanov complex in full: chain groups, differential, and what makes d² = 0.</summary>

Take a diagram with n crossings. Each crossing has a 0- and a 1-resolution, so complete
resolutions are indexed by ε ∈ {0,1}ⁿ and each is a disjoint union of circles. At a vertex
with m circles put V^{⊗m}, where V = span{1, x} is free of rank 2; the chain group in degree k
is the sum over vertices with |ε| = k. Along an edge, two circles merge or one splits: merging
uses the multiplication m (1·1 = 1, 1·x = x·1 = x, x·x = 0), splitting uses the
comultiplication Δ (Δ(1) = 1⊗x + x⊗1, Δ(x) = x⊗x), tensored with the identity elsewhere. Each
edge is multiplied by (−1)^{ε₁+⋯+ε_{j−1}}, where j is the crossing being changed. Those signs
make each square of the hypercube anticommute, so d² = 0. The homology is Khovanov homology.
</details>

<details>
<summary>8. What is a lasagna filling, and why is it defined that way?</summary>

Given a compact four-manifold X with a framed link 𝕃 in its boundary: a finite set of disjoint
four-balls inside X (input balls), a framed surface embedded in X minus those balls meeting ∂X
in 𝕃 and meeting each ball's boundary S³ in a link 𝕃_i, and a chosen element of Kh(𝕃_i) for
each i. The reason for the shape: you want an invariant of a link in the boundary of an
arbitrary four-manifold, but Khovanov homology is only defined for links in S³. Embedded balls
supply copies of S³ inside X; the surface connects everything; and the quotient relation —
a ball can be replaced by a finer filling whose labels map to its label under the Khovanov
cobordism map — is what cuts the enormous free group down to something computable.
</details>

<details>
<summary>9. Reconstruct the Ren–Willis argument.</summary>

Take W₁ = X(−5₂, −1) and W₂ = X(P(3,−3,−8), −1): D⁴ with one 2-handle attached along each
knot with framing −1. They have the same boundary three-manifold, are simply connected, and
have the same homology and intersection form, so by Boyer's classification they are
homeomorphic. Their skein lasagna modules differ: over ℚ, in bigrading (0,q) and homology
class 1, W₁ gives ℚ at q = 1, 3 and W₂ gives ℚ at q = −1, 1. Hence not diffeomorphic. The
computation is feasible because the 2-handle formula reduces 𝒮 to Khovanov homology of all
cables, and −5₂ has an all-positive diagram while P(3,−3,−8) is slice — two properties that
control those cables. Akbulut had already proved the pair exotic by gauge theory in 1991; the
novelty is that this proof uses no analysis at all.
</details>

<details>
<summary>10. What is the talk's closing open problem, and why is the boundary case easier?</summary>

Can skein lasagna modules detect exotic smooth structures on a **closed** four-manifold?
Every example so far has non-empty boundary. The reason boundary helps: a compact
four-manifold with boundary can be built from D⁴ plus a single 2-handle, so its Kirby diagram
is one knot with one integer, and the 2-handle formula then involves the cables of one knot.
A closed manifold like K3 needs 22 two-handles, so the same formula requires control of the
Khovanov homology of the cables of a 22-component link. Gauge theory and Heegaard Floer theory
can both handle closed manifolds; skein lasagna modules, so far, cannot.
</details>

---

## 10. Note on the tutorial process

**Difficulty against reputation: the reputation was right about the subject and wrong about
the difficulty of the machinery.** Manolescu is known for exactly this — Floer homology, the
combinatorial description of knot Floer homology, the disproof of the triangulation
conjecture — and the talk is squarely that. No Rule-1 inversion. But the split matters: the
frame is a 4 and the two invariants at the centre are a 2, and I have written the document
around that gap. The exercises are genuinely doable, which is not something I could say about
the Gaitsgory talk.

**How much mathematics survived the captions: none, and worse than none.** This was a talk
built on nineteen figures. Auto-captions carry no formulas and no pictures. Every displayed
equation above comes from arXiv:2601.05425. Every figure I needed — the surgery trace, the
Kirby diagrams, the grid diagram, the Khovanov cube, the lasagna filling — I have described
in prose, because you cannot see them either; where the prose is my reconstruction of a
figure I have said so at the point of use.

**Name corrections.** Thirty. All verified against the paper's text or bibliography unless
marked. The auto-captions destroyed essentially every proper noun in the lecture, including
the speaker's own.

| Caption | Correct | Source |
|---|---|---|
| Chiprian / Chiprien / Chipian | **Ciprian** (Manolescu) | paper, author line |
| cyberwiten / cyber grid / cyberwidon / cyborg with an / cyber wooden | **Seiberg–Witten** | paper §3 |
| thebart subway / Dorsbar subway | **Ozsváth–Szabó** (invariants) | paper §5.2 |
| Oshbat / Obat / Obart / Orbat / Oshbad | **Ozsváth** | paper, [82], [83] |
| Sabo | **Szabó** | paper, [82], [83] |
| hegard flur / heard flur / Hegar flur / hegard floating | **Heegaard Floer** | paper §5 |
| havanopomology / hanofomology / Havanaology / hovvenomology / Hovanology | **Khovanov homology** | paper §6.1, [41] |
| nautler homology / nler homology / not flur homology | **knot Floer homology** | paper §5.3 |
| Rasm Muen | **Rasmussen** | paper, [88] |
| Kronheimer and Rufka | **Kronheimer and Mrowka** | paper, [45] |
| Kudluhani talps | **Kutluhan–Lee–Taubes** | paper, [47] |
| kangi jini Honda | **Colin–Ghiggini–Honda** | paper, [15] |
| lipshit thirstston (bordered) | **Lipshitz–Ozsváth–Thurston** | paper, [53], [54] |
| Sharkar | **Sarkar** | paper, [61] |
| thirsten | **Thurston** (D. P.) | paper, [62] |
| Lavin Lidman and Pikilo / Levvin … Pikerillo | **Levine, Lidman, Piccirillo** | paper, [49] |
| Morrison Walker and Vedric / VI / Vri | **Morrison, Walker, Wedrich** | paper, [71] |
| Nate Halot | **Ikshu Neithalath** | paper, [59]; full name confirmed by search |
| Salivan Jang | **Sullivan–Zhang** | paper, [96] |
| Ben Ren Willis | **Ren–Willis** (Qiuyu Ren, Michael Willis) | paper, [90]; full names confirmed by search |
| Abdulut | **Akbulut** | paper, [3] |
| Freriedman | **Freedman** | paper, [25] |
| Buer | **Boyer** | paper, [12] |
| Donaldelsson | **Donaldson** | paper, [17] |
| licorice wallace | **Lickorish–Wallace** | paper, Thm 4.1 |
| curvy diagram | **Kirby diagram** | paper §4 |
| boner sphere | **Poincaré homology sphere** | paper, Fig. 6(a) |
| bomian rings | **Borromean rings** | paper, Fig. 1(d) |
| TF foil | **trefoil** | paper, Fig. 1(c) |
| pancor conjecture | **Poincaré conjecture** | paper, Conj. 3.1 |
| dro operator / spinner | **Dirac operator** / **spinor** | paper §3 |

Routine caption mangles I corrected silently throughout, since they recur dozens of times and
listing each occurrence would not help: *coortism* → cobordism; *deomorphic/theomorphic* →
diffeomorphic; *bjective* → bijective; *a billion group / ailion group* → abelian group;
*oiler characteristic* → Euler characteristic; *lur/Lauram polomial* → Laurent polynomial;
*simplectic* → symplectic; *koshi / koshirman* → Cauchy–Riemann; *Frobinius* → Frobenius;
*commlication* → comultiplication; *homotopia* → homotopy; *scan/ske/skin lasagna* → skein
lasagna; *unnot* → unknot; *s0q* → 𝒮_{0,q}.

**Substantive corrections, not spellings.** Three, each changing the meaning:

- The talk attributes the exotic ℂP² # 5ℂP̄² to "Lidman and Piccirillo and Levine, they found
  new examples" — the paper's reference [52] is **Lidman–Piccirillo only**. Corrected in
  §4.10.
- The talk states the Levine–Lidman–Piccirillo definite-intersection-form example without
  saying the manifolds are **not simply connected** (π₁ = ℤ/2). The paper says so explicitly
  and notes it therefore does not settle Question 3.2. I use the paper's version, because the
  difference is exactly what keeps the question open.
- The talk says the knot surgery formula "was proved by Szabó"; the paper attributes the
  integral surgery formula to **Ozsváth and Szabó** jointly, reference [84]. Almost certainly
  a caption dropping half a hyphenated name. Corrected in §4.9.

**Errors in the companion document itself.** Two, both found by cross-checking the paper
against its own figures:

1. The **writhe formula** is printed as w = ½(#positive − #negative), which gives 3/2 for the
   right-handed trefoil and contradicts the paper's own Figure 4 caption stating λ = 3. The ½
   is correct only if the crossings counted are those between L and its push-off. Flagged in
   §3.3.
2. The **grid diagram definition** describes the β curves as "n parallel *horizontal* curves …
   splitting the torus into n columns". They are vertical. A typo, unambiguous from context.
   Flagged in §4.8.

**Reconstructed, and what would verify each:**

- **Floer homology as infinite-dimensional Morse theory** (§2). Neither source uses the word
  "Morse" for Floer homology. The structural match — translation-invariant solutions as
  critical points, cylinder solutions as gradient lines — is exact from the paper's own
  formula, but the underlying action functional is not named anywhere in either source.
  Verify against Floer [21] or Kronheimer–Mrowka [45].
- **The Khovanov cube for the Hopf link** in §6.2 — which vertices carry two circles. Read off
  the standard diagram, since Figure 12 is a picture. Verify by drawing it: same-way
  resolutions give two circles, opposite-way give one. The maps and the sign rule are quoted
  verbatim from the paper.
- **The skein computations in §6.1.** Mine; the paper states only Δ(unlink₂) = 0 and
  Δ(T) = q⁻¹ − 1 + q. My Δ(T) reproduces the paper's stated value, which is a real check on
  the derivation. The Jones values are unchecked against a source and are stated in the
  paper's own normalisation; V(T) = q + q³ − q⁴ is the standard right-handed answer in that
  convention.
- **The Fox–Milnor determinant argument** in §6.1(3). Mine. The paper states Fox–Milnor as
  Δ = f(q)f(q⁻¹) and no more; evaluating at q = −1 is a standard step I supplied.
- **The "88 factorial" figure** (§4.9) is the speaker's, spoken, and appears nowhere in the
  paper. I attribute it to him and have not verified it.

**Gaps, and how bad each is.**

1. **The bigradings, everywhere. Low impact.** Both talk and paper explicitly decline to
   define the two gradings on knot Floer homology and Khovanov homology ("I won't get into
   that"). Everything above is stated ungraded except where I quote a graded answer directly
   from the paper. The one place it costs something is §5, where the whole argument lives in
   bigrading (0, q) and I can quote the answer but not derive it. **Moderate** there,
   specifically.
2. **The sign rule for grid rectangles. Low impact.** The talk says "there is a way of
   assigning signs" and the paper says the rectangle "is counted (with a certain sign)".
   Neither gives the rule. Consequence: §6.2's Khovanov exercise is fully signed and
   verifiable, and no exercise on grid homology is possible. That is why §6 has the exercise
   it has.
3. **The Seiberg–Witten equations are never written down. Low impact.** They were on the
   slide; the captions preserve only that they involve a Dirac operator, a spinor and a
   curvature. The paper does not display them either. Nothing in the argument depends on their
   form.
4. **The 1-handle skein lasagna formula. Low impact.** The paper declines to state it,
   describing it only as involving Hochschild homology of a category of tangles. The talk
   never mentions 1-handles for this invariant at all. Not needed: every computation discussed
   is for 2-handlebodies.
5. **𝒮(S¹ × S³) versus 𝒮(S¹ × D³, 𝕃_p). Moderate impact, unresolved.** The talk claims a
   full computation for S¹ × S³; the paper gives one for S¹ × D³ with a family of boundary
   links. Different manifolds. I quote both in §4.13 and decide nothing. The slide would
   settle it.

**What I chose not to teach.** Three things get stated as facts with their motivation and
their consequence and nothing more: the mapping-hypercube structure of the link surgery
formula (§4.9), the Frobenius-algebra structure behind Khovanov homology (§4.11), and the
Hochschild-homology 1-handle formula (§4.13). Each is a genuine object with a genuine
definition, none is learnable in a tutorial, and inventing a plausible account of any of them
would be exactly the fabrication that is worse than a hole.

**Could not verify.** One item: the person who introduced the lecture is addressed as "Tom"
and says "I've known Ciprian since he was a glimmer in his advisor's eye." Manolescu's
doctoral advisor was at Harvard, and Tom Mrowka — who appears in this talk's bibliography —
is the obvious candidate, but nothing in either source identifies the introducer. I have not
named him.

**On dates.** The arXiv stamp on the HTML reads `arXiv:2601.05425v1 [math.GT] 08 Jan 2026`,
and that is the date I use. The talk's date, 2026-08-17, is the ICM lecture. Where the talk
gives a date the paper contradicts — "I gave one in 2001" against the 2003 publication of
[56] — both are correct; 2001 is the preprint, 2003 the journal. Noted in §3.7 rather than
corrected.
