---
title: "Prismatic Stable Homotopy Theory"
speaker: Jacob Lurie (Institute for Advanced Study)
source: https://www.youtube.com/watch?v=wkUJoGqYFN4
video_id: wkUJoGqYFN4
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: none
transcript: ../transcripts/wkUJoGqYFN4_transcript.txt
difficulty_for_you: 5/5 (the objects) — 3/5 (the narrative as delivered)
reading_time: ~65 min
---

# Prismatic Stable Homotopy Theory — Jacob Lurie

**Field:** the meeting point of algebraic topology and algebraic geometry — his own opening
words. Concretely: algebraic K-theory, topological cyclic homology, prismatic and syntomic
cohomology, and a conjectural framework proposed to contain all of them.

**Difficulty against your background: split, 5 out of 5 for the objects, 3 out of 5 for the
narrative as delivered.** The objects in this talk sit at the top of the abstraction ladder —
cyclotomic spectra, prismatic F-gauges, a stable homotopy category for p-adic geometry that
does not yet exist. None of them is in your training and none is learnable in an afternoon.
But **the speaker black-boxes them himself, twice, out loud**, and builds his whole hour on
two properties that survive the black box: "it is a tensor category, so you can talk about
algebras and modules" and "it is a triangulated category, so you can talk about Ext groups."
That is a deliberate teaching decision by a speaker who wrote the standard references on the
machinery he is refusing to explain, and it makes the *story* followable at difficulty 3
while the *objects* stay at 5.

His own framing of the black-box move, which you should take at face value:

> "Now in this lecture I'm going to treat that as a black box. I'm not going to tell you what
> a cyclotomic spectrum is, but let me just tell you a few things about them."

and, forty minutes later, on the thing he is actually proposing:

> "So unfortunately, I didn't tell you what any of these things are… And what I'm proposing
> is these two well-defined black boxes should actually be fit into a larger black box that I
> do not have a precise definition of."

That sentence is the talk. He is asking for an object he cannot define, specified entirely by
the properties it must have and by one calculation it must reproduce.

**Prerequisites this tutorial builds:** what a generalized cohomology theory is and why
dropping one axiom matters; the Grothendieck group construction; Bott periodicity as a
statement, not a proof; what the stable homotopy category is, via Brown representability;
Chern classes, complex orientation, and formal group laws (with the Baker–Campbell–Hausdorff
formula as the bridge); complex cobordism and Quillen's theorem; Hochschild homology and the
HKR theorem as a differential-forms machine; what p-completion and étale descent buy you;
spectral sequences read as perturbation series.

**A note on sources.** This is the hard case, and it is the case the spec anticipates in
option 3.

- **There is no ICM proceedings paper.** Lurie has posted nothing to arXiv since January 2022.
- **There is no companion on his own website.** I checked `math.ias.edu/~lurie/`. The listed
  papers stop at *Ultracategories* and *Revisiting the de Rham–Witt Complex* (December 2019);
  the books are *Higher Topos Theory* (2017), *Higher Algebra* (2017), and *Spectral Algebraic
  Geometry* (2018, incomplete). **Nothing on prismatic anything.** The talk covers material
  from none of the three books, so none of them is a legitimate companion.
- **He names no survey of his own from the podium.** I scanned the transcript for it.

What does exist, and what I used:

1. **A second recording of the same lecture, by the same speaker, seventeen months earlier**:
   *Prismatic Stable Homotopy Theory*, Simons Collaboration on Perfection in Algebra, Geometry
   and Topology annual meeting, 14 March 2025,
   [youtube.com/watch?v=1fSd7FxEA3w](https://www.youtube.com/watch?v=1fSd7FxEA3w). Same title,
   same conjecture, same acceptance test, but aimed at specialists and therefore far more
   explicit. It is **not a paper and not lecture notes** — it is a second set of auto-captions,
   with the same formula-blindness. I use it as a labelled cross-check and I mark every place
   I draw on it, because material in the 2025 talk that is not in the ICM talk is *not what he
   said at the ICM*.
2. **Primary literature for the individual results he cites.** Where the talk names a theorem,
   I recovered its statement from the paper that proved it and cite that paper by name. Those
   are primary sources for one theorem each; they are not a substitute for a proceedings paper
   and I do not present them as one.

**The consequence for you: every formula below is either spoken aloud in one of the two
recordings, or recovered from a named paper, or marked reconstructed, or marked as a gap.**
More survived than you might expect, for one specific reason — **this is a talk of spoken
formulas.** Lurie says "TC of R can be defined as extensions from the unit object into THH of
R" out loud, in words, and the caption track catches it. The mathematics that died on the
slides is the *indexing*: which degree, which twist, which page of which spectral sequence.
The shapes survived. The subscripts did not.

---

## 1. What is at stake

Here is the question, with no jargon in it.

You have a mathematical object — a ring, or a space. You want to attach numbers to it that are
invariant, computable, and informative. Over the last century, topologists built an enormous
catalogue of ways to do that: ordinary cohomology, K-theory, cobordism, elliptic cohomology,
and hundreds more. Algebraic geometers have a much shorter catalogue, and the shortness hurts.

Lurie's opening moral, stated twice:

> "It's useful to have a lot of tools. That is, problems that can be quite difficult using a
> limited set of tools can become much easier if you bring the right tool for the job."

His evidence is a specific, famous, checkable story. In the 1930s Hopf built some remarkable
maps between spheres out of the real division algebras — the complex numbers, the quaternions,
the octonions. They have a numerical property no other map between spheres seemed to have.
*Are there others, in other dimensions?* The question stood for thirty years. Adams answered
it — no — in 1960, in an 85-page paper using secondary cohomology operations. Then Adams and
Atiyah reproved it using complex K-theory in **eight pages, with the main argument in a single
paragraph**. Lurie calls it a proof from the Book, in Erdős's sense, and he is right.

So: a tool that did not exist in 1955 turned a thirty-year problem into one paragraph. That is
what a new cohomology theory is worth.

**The p-adic world is short of tools.** And the last decade has produced a spectacular set of
new ones — prismatic cohomology, syntomic cohomology, the modern theory of topological cyclic
homology — which have already cracked problems that stood for decades. Lurie's question is:
*why did that work, and is there a general reason?*

His answer is a conjecture with a very precise shape. In topology, all cohomology theories live
in one place: the **stable homotopy category**. That single category organizes the whole
catalogue, and it is the reason topologists have hundreds of tools rather than three. Lurie
conjectures that **p-adic geometry has its own stable homotopy category** — he calls it the
*prismatic stable homotopy category*, written SH_prism — and that the recent p-adic invariants
are the first few objects in it, the way ordinary cohomology and K-theory are the first two
objects in the classical one.

He cannot define it. He states what it must do, and he states one calculation that any correct
definition must reproduce. And he tells you why he wants it, in the most honest sentence in the
hour:

> "There are some invariants that I can compute without being able to define, and I'm searching
> for the definition of what it is that I am computing."

You know that shape. It is the path integral. It is the delta function before Schwartz. It is
renormalization before Wilson. Physicists computed with all three for decades before anyone
could say what the object was. Lurie is describing exactly that position, from an ICM podium,
about his own work.

---

## 2. Your anchor

Three things in this talk are structurally something you already own. The first is the
strongest, and it is the talk's actual engine.

### 2.1 Künneth is "independent subsystems factorize"

Watch how often the following appears: **the invariant of a product should be the product of
the invariants.** Lurie returns to it five separate times, and every single design decision in
the talk is made to protect it.

You have owned this since your first statistical mechanics course. Two non-interacting
subsystems: the Hamiltonian is a sum, so the partition function is a product,
Z(A ⊔ B) = Z(A)·Z(B). Two independent random variables: the characteristic function of the sum
is the product of the characteristic functions. Convolution in one domain, multiplication in
the other — that is Fourier's whole point. A separable PDE: the solution factorizes over the
directions.

In topology, the same principle is called the **Künneth formula**. For a cohomology theory E
and spaces X, Y, you want

> E(X × Y) ≅ E(X) ⊗_{E(pt)} E(Y)

and Lurie's first observation is that **complex K-theory satisfies it** (exactly when things
are torsion-free, with a small correction otherwise), which is a large part of why K-theory is
so usable. His second observation is that **algebraic K-theory does not**, and neither does its
computable surrogate TC, and neither does motivic cohomology, and neither does syntomic
cohomology.

Now the move that makes the talk. When factorization fails, he does not add a correction term.
He asks: **where in the pipeline did it break?** And each time, the answer is the same. The
invariant is computed in two steps:

1. Turn the geometric object X into an algebraic coefficient object M(X) — a "motive".
2. Take Ext groups out of the unit object into M(X).

**Step 1 factorizes. Step 2 destroys the factorization.** So back up: do not work with the
invariant, work with the coefficient object M(X), where Künneth still holds, and take the Ext
only at the very end. That is what topological Hochschild homology THH is for K-theory, and it
is what prismatic F-gauges are for syntomic cohomology. Both objects exist for exactly this
reason and he says so in both cases.

> **Hold this one sentence and the talk decodes: the failure of factorization is never in the
> object, it is in the last step of the pipeline, so move the last step later.**

This is also the point at which this talk touches a sibling in this set. Gaitsgory's ICM
lecture has the *same disease with the same cure shape*: ℓ-adic sheaves fail a Künneth formula,
and that single failure forces the reconstruction of the entire ambient 2-category (AGCat).
See `summaries/langlands-function-fields-gaitsgory.md` §7.3 — it is written up at length there
and I will not repeat it. Two plenary speakers in different fields, both spending their hour on
what one broken compositionality law costs.

### 2.2 A surrogate with a certificate, not just an approximation

The second anchor is Lurie's own methodological remark:

> "Someone gives you a math problem and the math problem is too hard. What you might try to do
> is to try to solve an easier version of that problem."

That is not interesting by itself. What *is* interesting is the standard he holds the
approximation to. Algebraic K-theory K(R) is very hard. Topological cyclic homology TC(R) is
much easier and there is a trace map K(R) → TC(R). Every applied mathematician has built
surrogates like that: a preconditioner, a reduced-order model, a coarse-grained Hamiltonian.
The question is always the same — *how wrong is it?*

The answer here is not a bound. It is an exact characterization. Lurie lists three specific
ways TC fails to behave like K-theory, and then states that a theorem of Clausen, Mathew and
Morrow says **those three are the entire difference**: on p-complete rings, TC is precisely
what you get from K-theory by forcing those three properties on it, and nothing else is lost.

That is the difference between "an approximation" and a **surrogate with a certificate** —
a cheap model together with a theorem saying exactly on what domain, and modulo exactly what,
it is the real thing. It is the analogue of a spectral-equivalence proof for a preconditioner
rather than a numerical experiment that it seems to work. §8 comes back to this; it is the
most transferable idea in the lecture.

### 2.3 Spectral sequences are perturbation series

Lurie uses the phrase "a good first approximation" for the E₂ page of a spectral sequence, and
you should read it exactly that way. The pattern in the talk is:

> hard invariant ≈ easy invariant ⊗ (invariant of a point), plus corrections

which is a perturbation series: leading term, then corrections organized by order. The
differentials are the corrections. Convergence is resummation.

**One honest caveat, because it matters when you read the results:** a spectral sequence does
not hand you the answer. It hands you the associated graded of a filtration on the answer, and
you still have extension problems — knowing the pieces of a group is not knowing the group.
That is exactly why computing K-theory stayed hard even after the spectral sequences existed,
and why the recent computation of the K-theory of ℤ/4 was news.

### 2.4 One thing to set aside: ∞-categories

You might expect this talk to be about ∞-categories. Lurie is the person who wrote *Higher
Topos Theory* and *Higher Algebra*; the anchor briefed for this tutorial was homotopy — "equal"
replaced by "connected by a path", paths between paths, forever, the way gauge-equivalent field
configurations are different but physically identical.

**The talk never says "∞-category". It never says "higher category". It never says "homotopy"
in that sense.** I checked the whole transcript. What he says instead, twice, is "it's a tensor
category" and "it's a triangulated category, so it makes sense to talk about Ext groups."

That is a deliberate choice and you should respect it. Everything in this lecture is *built* on
higher-categorical foundations — "triangulated category" is the flattened shadow of a stable
∞-category, and the objects he calls black boxes are ∞-categorical objects. But teaching you
∞-categories here would be decorating his talk with someone else's picture, and it would be
teaching you machinery the talk deliberately does not use. **I am naming it so you know it is
there and know it is absent, and then leaving it alone.** If you ever want it, it is *Higher
Topos Theory*, it is a thousand pages, and this talk is not the on-ramp.

What you need instead is much smaller, and it is genuinely just two rules:

- **"tensor category"** — there is a way to multiply two objects, written ⊗, with a unit object
  (a "1"). Because there is a ⊗ and a 1, the words *algebra* and *module* make sense.
- **"triangulated category, so Ext groups make sense"** — there is a notion of one object
  mapping to another, in a graded family indexed by an integer n, written Ext^n(A, B), and
  these fit into long exact sequences. Read Ext^n(A, B) as "the degree-n maps from A to B", and
  read "the E-cohomology of X is Ext^n(motive of X, E)" as a **pairing**: the invariant is what
  you get when you test the object against the theory.

That is the whole categorical prerequisite. Everything else he black-boxes and so do I.

---

## 3. The bridge

Eight ideas. Each is defined by deforming something you have. Read §3.1 to §3.5 carefully; they
are the load-bearing ones.

### 3.1 A generalized cohomology theory is cohomology with one axiom deleted

You know de Rham cohomology: differential forms, d² = 0, closed modulo exact, and the payoff is
that it is computable by cutting the manifold into pieces (Mayer–Vietoris) and gluing the
answers.

That computability is not an accident of differential forms. It is a short list of formal
properties, and in the 1940s Eilenberg and Steenrod isolated them: homotopy invariance, long
exact sequences of a pair, excision, Mayer–Vietoris, additivity — plus one more, the
**dimension axiom**, which says that the cohomology of a single point is ℤ in degree 0 and zero
in every other degree.

A **generalized cohomology theory** is a functor satisfying everything on that list *except the
dimension axiom*. Lurie's phrasing:

> "If you make a list of the properties that cohomology has that make it convenient to work
> with — like long exact sequences, or excision, or Mayer–Vietoris, etc. — then K-theory has
> almost all of those features. The only exception is that unlike cohomology the K-theory of a
> point is not concentrated in a single degree."

Why that deletion is the whole game: the bookkeeping axioms are what make an invariant
*computable*. The dimension axiom is what makes it *unique*. Delete it and you keep all the
computability and you get a whole catalogue instead of one theory. Every object in this talk is
downstream of that one deletion.

### 3.2 K-theory is what happens when you insist on subtraction

This one is elementary and completely concrete, and it is where the talk starts.

Take X a nice space — a compact manifold. Consider complex vector bundles on X: at each point
of X, a copy of ℂ^k, varying continuously. You can add two of them by taking the direct sum
fibrewise. Isomorphism classes of bundles under ⊕ form a **commutative monoid**: you can add,
there is a zero, but **you cannot subtract**.

Now do to that monoid exactly what you did to ℕ in primary school to get ℤ: formally adjoin
inverses. Elements become formal differences [E] − [F], with [E] − [F] = [E′] − [F′] whenever
they differ by adding the same thing to both sides. The result is a genuine abelian group.

> **KU⁰(X)** := the group completion of (isomorphism classes of complex vector bundles on X, ⊕).

Atiyah and Hirzebruch, around 1960. Sanity check, and Lurie gives exactly this one: if X is a
single point, a vector bundle is just a vector space, classified up to isomorphism by its
dimension, so the monoid is ℕ; group-complete and you get **ℤ**.

The same construction runs verbatim in algebra. Replace "complex vector bundle on X" by
"finitely generated projective module over a ring R" — the algebraic analogue, and Lurie says
so explicitly — take ⊕, group-complete, and you get **K₀(R)**, the Grothendieck group. Lurie
notes that this came *first*: "this definition goes back to Grothendieck and it actually
predates the definition of [K-theory in topology]… they were imitating Grothendieck." Sanity
check again: R a field, projective modules are vector spaces, classified by dimension, so
K₀(field) = ℤ.

**Both of the two columns in this talk begin at exactly this construction.** That is worth
noticing now, because the parallel between the columns is the whole lecture.

### 3.3 Bott periodicity, stated and not proved

KU⁰ extends to a family KU^n(X), one for every integer n. The dimension axiom fails, and it
fails in a very specific and beautiful way:

> **KU^n(pt) = ℤ for every even n, and 0 for every odd n.**

Equivalently KU^n ≅ KU^{n+2}: complex K-theory is **2-periodic**. This is Bott's periodicity
theorem, and Lurie states it and moves on. So do I — it is a real theorem with a real proof and
neither belongs here. Take it as a fact about the object.

Keep the *shape* though, because it comes back: **an infinite periodic pattern where ordinary
cohomology has a single ℤ.** When Bökstedt later computes THH(𝔽_p) and gets a polynomial ring
on one generator in degree 2, Lurie says out loud that you should read it as "some incarnation
of Bott periodicity but in an algebraic world". He is telling you the pattern repeats.

### 3.4 The stable homotopy category, via Brown representability

Here is the object that organizes the topological catalogue, and here is the honest way in.

You have a whole zoo of generalized cohomology theories. Is there a single mathematical object
whose *elements* are cohomology theories? Yes:

> **The stable homotopy category SH.** It is a tensor category with unit object **S**, the
> *sphere spectrum*. It is triangulated, so Ext groups make sense. Every topological space X
> has an incarnation S[X] ∈ SH called its suspension spectrum. And every object E ∈ SH defines
> a cohomology theory by
>
> **E^n(X) := Ext^n( S[X], E ).**

And then the theorem that makes it worth having, which Lurie attributes to Brown in the 1960s:

> **Every generalized cohomology theory arises this way, from an essentially unique object E.**

**The anchor for this is the Riesz representation theorem**, and the analogy is tight, not
decorative. A cohomology theory is a rule that eats a space and returns graded groups, subject
to compatibility axioms — a "functional on spaces". Brown representability says every such
functional is represented by pairing against a fixed object, exactly as every bounded linear
functional on a Hilbert space is ⟨·, v⟩ for a unique v. Once you know that, you stop studying
functionals and start studying the representing objects — because the objects can be added,
multiplied, and resolved, and functionals cannot.

Two objects you need by name:

- **Hℤ**, the *Eilenberg–MacLane spectrum*, representing ordinary cohomology.
- **KU**, representing complex K-theory.

And the structural slogan Lurie uses, which is worth memorizing because the entire conjecture is
a copy of it: **modules over Hℤ in SH are the same thing as chain complexes of abelian groups.**
(This is stated in the March 2025 recording, not at the ICM. The ICM talk states only the
corresponding prismatic version.) Ordinary homological algebra sits inside stable homotopy
theory as the module category over one particular object. Everything else in SH is, in a precise
sense, *less linear* than chain complexes.

### 3.5 Chern classes, complex orientation, and formal group laws

This is the one piece of real technical content the talk both needs and can teach you, and it is
much closer to your training than it looks.

A complex line bundle L on X has a first Chern class c₁(L), an element of E²(X) for a suitable
cohomology theory E. Saying that E *has* a sensible theory of Chern classes for all complex
vector bundles is the condition called **complex orientability**. Ordinary cohomology is complex
orientable. So is K-theory. So are a great many others — Lurie: "there's a huge number of
complex-oriented cohomology theories."

Now the sharp question. Given two line bundles L₁, L₂, what is c₁(L₁ ⊗ L₂)?

For ordinary cohomology, the answer is what you would guess: **c₁(L₁ ⊗ L₂) = c₁(L₁) + c₁(L₂)**.
Chern classes add.

For a general complex-oriented theory, **they do not.** Instead there is a power series in two
variables,

> c₁(L₁ ⊗ L₂) = F( c₁(L₁), c₁(L₂) ),

and the axioms of tensor product force F to satisfy

> F(x, 0) = x,  F(x, y) = F(y, x),  F( F(x,y), z ) = F( x, F(y,z) ).

A power series satisfying those three is called a **one-dimensional formal group law**. It is
an associative, commutative group operation written as a formal power series with no convergence
requirement.

**Your anchor here is the Baker–Campbell–Hausdorff formula.** For a Lie group, multiplication
near the identity in exponential coordinates is
exp(X)exp(Y) = exp(X + Y + ½[X,Y] + …) — an associative product written as a formal power
series in the coordinates. That *is* a formal group law, in higher dimension. A one-dimensional
formal group law is the germ of a one-dimensional group at its identity, remembered as a power
series and nothing else.

Two examples you should carry:

- **Additive:** F(x,y) = x + y. This is ordinary cohomology.
- **Multiplicative:** F(x,y) = x + y + βxy. This is complex K-theory.
  *(Reconstructed from standard literature — the talk states the additive case only, and names
  the multiplicative one nowhere. It is the standard fact and Exercise 7.2 makes you check it
  is a legitimate formal group law; take the identification with K-theory itself on trust.)*

And the punchline of the exercise in §7.2, which is the punchline of the whole subject:
**over ℚ these are isomorphic and over ℤ_p they are not.** Every one-dimensional formal group
law over a ℚ-algebra can be straightened into the additive one by a formal logarithm, and the
logarithm has denominators. Kill the denominators — work p-adically — and a rich classification
appears. **The whole catalogue of cohomology theories lives in those denominators.** That is why
this talk is about p-adic geometry and not about characteristic zero.

### 3.6 Complex cobordism MU, and Quillen's theorem

Among complex-orientable theories there is a universal one — richest, mapping to all others.

> **MU**, complex cobordism.

Its name is literal. Two closed manifolds are **cobordant** if together they bound a compact
manifold of one dimension higher. Cobordism classes form a ring: addition is disjoint union,
multiplication is product. (If you have met bordism in topological field theory, this is that.)
MU uses manifolds with an almost complex structure on the stable normal bundle, and its
coefficient ring MU^*(pt) is exactly the ring of such manifolds up to compatible cobordism.

**Milnor computed it, around 1960:** MU^*(pt) is a **polynomial ring on an infinite sequence of
generators, one in each even degree.** Write them t₁, t₂, t₃, …. And Milnor's calculation has a
second reading, which Lurie gives:

> **Mod out MU by Milnor's generators and you get Hℤ.**

Then Quillen's reinterpretation, which is the theorem this talk is organized around. That
polynomial ring is not just abstractly a polynomial ring — it is *the* ring that classifies
one-dimensional formal group laws (the Lazard ring), and under that identification:

> **Quillen's theorem. The formal group law carried by MU is the universal one.** MU is the
> universal complex-oriented cohomology theory *and* it carries the universal formal group law,
> and those two universal properties are the same statement.

Read against §3.5, Quillen's theorem answers "what is special about ordinary cohomology?" with:
it is complex-orientable, **and** its formal group law is the additive one. And the two-step
factorization it gives is the exact template for the conjecture:

> **S → MU → Hℤ**: first make the theory complex-oriented (pass to MU), then kill the Milnor
> generators (to get Hℤ).

Lurie's heuristic gloss, which is the sentence to remember:

> "There are roughly as many cohomology theories in the world of topology as there are formal
> groups."

### 3.7 THH and TC: what survives the black box

Now the K-theory column's machinery. Lurie declines to define a cyclotomic spectrum and so do I.
Here is everything he gives you and everything you need.

**Hochschild homology HH(R)** is old and concrete: an explicit chain complex built from R,
computable by hand from generators and relations. Its content, and the reason it matters here,
is the **HKR theorem**: for R a smooth algebra, HH_n(R) is the module of algebraic differential
n-forms Ω^n_R. Lurie says exactly this for 𝔽_p-algebras — "if R is a smooth algebra over 𝔽_p
then its Hochschild homology groups are just the groups of algebraic differential forms for the
ring R… If you have a presentation of R by generators and relations, then you can write these
things down very explicitly."

**That is the anchor for the entire construction: Hochschild homology manufactures differential
forms out of a ring, with no manifold anywhere in sight.** You own differential forms. This is
how they get into a subject that has no smooth structure.

**Topological Hochschild homology THH(R)** is the refinement of HH in which the ground ring is
not ℤ but the sphere spectrum S. It is a **cyclotomic spectrum** — black box, declined. Two
facts survive and are all that get used:

- Cyclotomic spectra form a tensor category (so algebras and modules make sense) and a
  triangulated category (so Ext makes sense).
- Every ring R is a ℤ-algebra, so **THH(R) is a module over THH(ℤ)**.

**Bökstedt's calculation**, from the 1980s, is the one number in the talk:

> **THH(𝔽_p) = a polynomial ring on a single generator of degree 2.**

Lurie: "you can think about this as some incarnation of Bott periodicity but in an algebraic
world." And it is what connects THH to the concrete: for R an 𝔽_p-algebra, THH(R) is a module
over THH(𝔽_p); reduce modulo that degree-2 generator and you land in ordinary Hochschild
homology, hence in differential forms. His conclusion:

> "Computing things about THH of R, it's one spectral sequence away from just understanding
> algebraic differential forms."

**Topological cyclic homology TC(R)** is then defined *inside* that world:

> **TC(R) = Ext( unit object, THH(R) )**, computed in the category of cyclotomic
> THH(ℤ)-modules.

Spoken aloud, verbatim: "TC of R can be defined as just extensions from the unit object into
THH of R." (This is the Nikolaus–Scholze formulation; Lurie names them in the March 2025
recording, not at the ICM.) TC was introduced by **Bökstedt, Hsiang and Madsen** around 1990,
and — the fine print he flags and I will hold to — **throughout, "TC" means the p-adically
completed version, for one fixed prime p.** For the K-theory of ℤ/4, the interesting prime is
p = 2.

### 3.8 p-completion and étale descent, in one paragraph each

Two operations get applied over and over, always as a pair. Both are simplifications, and both
throw information away on purpose.

**p-completion.** Fix a prime p and remember only p-power torsion information — formally, take
the limit of the reductions mod p^n. You already own the analogy: ℤ_p is to ℤ as ℝ is to ℚ, a
completion in a different metric. The cost is stated by Lurie as a genuine defect: **TC(R)
depends only on the p-adic completion of R**, so it cannot see anything about R away from p.
K-theory has no such blindness.

**Étale descent.** A local-to-global principle: compute the invariant of a small ring from the
invariant of covers of it, glued. It is exactly a sheaf condition — the same shape as
reconstructing a function on a manifold from its values on a good cover, with the étale
topology in place of the ordinary one. Lurie's gloss: "it satisfies what's called étale descent,
which lets you compute the invariant for small rings in terms of the invariant for enlargements
of those rings." Again a defect *and* the source of the computability: K-theory does not satisfy
it, TC does, and that is a large part of why TC is tractable.

---

## 4. The talk, rebuilt

His order, with the mathematics restored where I could restore it and marked where I could not.

### 4.1 Story one: from complex K-theory down to differential forms

He builds a chain of four objects, and the shape of that chain is the whole point.

**Step 1: complex K-theory KU** (§3.2, §3.3). A generalized cohomology theory on topological
spaces. Useful enough to turn a thirty-year problem into eight pages.

**Step 2: its algebro-geometric avatar, algebraic K-theory.** K₀(R) by group completion
(§3.2), extended by **Quillen in the 1970s** to higher K-groups K_n(R). Lurie lists three
constituencies who want these groups, and they are genuinely unrelated to each other:

- **Algebraic geometry** — Grothendieck's original motivation, generalizations of
  Riemann–Roch.
- **Number theory** — "the K-groups of number fields are conjecturally related to special
  values of L-functions."
- **Geometric topology** — "if you're interested in questions related to the surgery
  classification of manifolds, you often run into obstructions that live in certain K-theory
  groups."

**And the problem: they are almost impossible to compute.** His example is deliberately
humiliating in its simplicity — *the algebraic K-theory of ℤ/4 is still not completely known.*
Not a variety, not a scheme, not a number field. The integers mod four.

He then says that very recently we know much more: in degrees greater than zero the K-groups of
ℤ/4 are finite abelian groups **and we now know how big they are**.

> *[Attribution restored, and the talk does not name the authors. This is Antieau, Krause and
> Nikolaus, "On the K-theory of ℤ/p^n", [arXiv:2405.04329](https://arxiv.org/abs/2405.04329),
> which gives an explicit prismatic-cohomology description of the K-groups of 𝒪_K/I and an
> algorithm that computes them — ℤ/4 included. Their methods are exactly the ones this talk is
> about, which is presumably why he raised the example.]*

He splits the difficulty honestly: these are finite groups, so they split into an odd part and a
2-torsion part; **the odd part has been understood since Quillen in the 1970s**, and it is the
p-adic part that is hard.

**Step 3: the surrogate, TC** (§3.7, §2.2). Trace map K(R) → TC(R). Two virtues: a good
approximation, and computable. And then the certificate. The three ways TC is *not* K-theory:

1. It is p-adically complete by fiat.
2. Consequently TC(R) depends only on the p-adic completion of R — a property K-theory does
   not have.
3. It satisfies étale descent, a stronger local-to-global principle than K-theory has.

And the theorem that makes those three exhaustive, which he attributes to **Clausen, Mathew and
Morrow**:

> "There's a recent result of Clausen and Mathew and Morrow that says if you stick to p-complete
> rings then this trace map, it exhibits topological cyclic homology as what you get from
> K-theory by forcing it to have the properties on the previous slide — to force it to be
> p-adically complete and to satisfy this strong local-to-global principle."

*(I quote his phrasing rather than sharpening it. The precise statements in the Clausen–Mathew–
Morrow literature carry hypotheses that the captions do not carry, and I am not going to
manufacture them. What is safe, and is what he uses: on p-complete rings the difference between
K and TC is exactly those three properties and nothing more.)*

**Step 4: under the hood, THH** (§3.7). TC(R) = Ext(unit, THH(R)) in cyclotomic THH(ℤ)-modules;
THH is one spectral sequence from differential forms; and — the property that motivates its
existence —

> **THH satisfies the Künneth formula, in the naive sense, in cyclotomic spectra:**
> THH(R ⊗_k S) ≅ THH(R) ⊗_{THH(k)} THH(S).

Contrast, in his own words, with what fails: complex K-theory "essentially satisfies a Künneth
formula" and this is "a very valuable thing if you want to actually compute with it"; algebraic
K-theory "has no obvious Künneth formula"; and TC does not either. THH does. **The Künneth is
recovered by backing up one step in the pipeline** — exactly §2.1.

> *[Gap: the correction term in the K-theory Künneth formula. He says that when KU(X) is
> torsion-free the map KU(X) ⊗_{KU(pt)} KU(Y) → KU(X × Y) is an isomorphism, and "if it's not
> torsion-free, there's some slight correction". The correction is a Tor term and was, if
> anywhere, on the slide. **Impact: low.** Nothing downstream uses it; only the existence of a
> Künneth formula is used.]*

### 4.2 Story two: from ordinary cohomology down to prismatic F-gauges

Now the same four steps, for the other most basic cohomology theory, and the parallel is exact.

**Step 1: ordinary cohomology.**

**Step 2: its avatar in algebraic geometry, motivic cohomology.** He introduces it through the
spectral sequence that relates it to K-theory. In topology there is the **Atiyah–Hirzebruch
spectral sequence**: take the ordinary cohomology of X, tensor with the K-theory of a point,
and that is the first page of a spectral sequence converging to KU(X) — "that's not what
K-theory is. If that was what K-theory is, there would be no point in having K-theory. But it's
a good first approximation."

> *[Reconstructed from standard literature: the E₂ page is E₂^{s,t} = H^s(X; KU^t(pt)),
> converging to KU^{s+t}(X). He states the shape in words; the indices were on the slide.
> Verified by: any algebraic topology text; the statement is standard. **Impact: low.**]*

The algebro-geometric counterpart, which he dates to **around 2000** and attributes to
**Levine and to Friedlander–Suslin**: for the coordinate ring of a smooth algebraic variety,
there is a spectral sequence computing algebraic K-theory from the **motivic cohomology** groups
of the variety. He notes the case of a field was done earlier, and that the result has recently
been extended to completely general situations.

> *[Attribution as the speaker gave it. He does not name the earlier field case and I have not
> supplied a name for it. **Impact: low** — the attribution is not load-bearing; the parallel
> is.]*

**Step 3: the simplified version, syntomic cohomology.** He immediately says motivic cohomology
is not what he wants to talk about — he wants the analogue of the story for TC, not for K.

> **Bhatt–Morrow–Scholze**, over the last decade: for a p-complete ring R there is a spectral
> sequence starting from the **syntomic cohomology** groups of Spec R and converging to
> **TC(R)**.

Syntomic cohomology has a long history: **Fontaine and Messing** in the 1980s defined it in
good cases with rational coefficients; Bhatt–Morrow–Scholze give an *integral* version in all
weights. Note the direction of construction, because it is unusual and he flags it: they built
syntomic cohomology **using topological methods** — they used topological cyclic homology to
define it. The topology came first.

> *[From the March 2025 recording, not the ICM talk — the cleanest one-line description of what
> syntomic cohomology is for: if p is invertible on a scheme you can talk about its p-adic étale
> cohomology with a Tate twist, and the Tate twist a priori only makes sense when p is
> invertible; syntomic cohomology is the extension of that invariant to all schemes, including
> those where p = 0. That sentence is not in the ICM talk and I flag it as a cross-check, not
> as something he said at the ICM.]*

**Bhatt and Scholze** then reinterpreted it through **prismatic cohomology**, and here Lurie
gives a one-line slogan:

> "This syntomic cohomology, you can think of it as the part of prismatic cohomology where the
> Frobenius acts by the identity."

*(Take that as the heuristic he offers it as. He does not state the precise form, and the
precise form has a Nygaard-completion in it. **Impact: low** — nothing below depends on the
precise form.)*

**Step 4: the coefficient category, prismatic F-gauges.** Black box number two, declined
exactly as cyclotomic spectra were, with exactly the same two survivals: tensor category,
triangulated category. And then the same formula shape:

> **Syntomic cohomology groups = Ext( unit object, or a twist of it, ℤ_prism^X )**
> in the category of prismatic F-gauges,

where ℤ_prism^X is the coefficient object attached to the p-adic formal scheme X — its
"cohomological motive". And then the reason for the whole construction, which is again Künneth,
stated by him in as many words:

> "You might ask what is the point of having a formula like this? And the way that I think about
> it, the point of having a formula like this is so that you can think about the Künneth
> formula."

Motivic cohomology has no obvious Künneth. Syntomic cohomology has no obvious Künneth. **But the
motives do:**

> **ℤ_prism^{X × Y} ≅ ℤ_prism^X ⊗ ℤ_prism^Y** (under a mild assumption).

And therefore there *is* a Künneth formula for syntomic cohomology — stated in the language of
F-gauges. "That's the price that you pay for being able to write down a Künneth formula."

> *[**Gap, and this is the most consequential one in the talk.** He says: "There is a formula
> written here that tells you what the syntomic cohomology of a product X × Y looks like." The
> formula was on the slide. The captions carry nothing — no indices, no twists, no Tor or Ext
> correction terms. What survives is: the motives tensor, and therefore a Künneth formula for
> syntomic cohomology exists and is expressible only in F-gauge language. **Impact: moderate.**
> The *shape* is what the argument uses, and the shape is intact; but this is the single
> concrete payoff he offers for introducing F-gauges at all, and I cannot show it to you.]*

### 4.3 The chart — the centre of the lecture

He now lays the two stories side by side, and this table is the object the rest of the hour
manipulates.

**Reconstructed as a table; the layout is mine, every cell is stated aloud in the talk.**

| | **K-theory column** | **ordinary-cohomology column** |
|---|---|---|
| **Classical topology** | complex K-theory, **KU** | ordinary cohomology, **Hℤ** |
| **Avatar in algebraic geometry** | algebraic K-theory | motivic cohomology |
| **Simplified** (p-complete + étale descent) | **TC** | **syntomic cohomology** |
| **Expressed as Ext in a category** | cyclotomic modules over THH(ℤ) | prismatic F-gauges |
| **Coefficient object attached to X** | **THH(X)** | **ℤ_prism^X** |
| **Künneth holds at the level of** | THH | the motives ℤ_prism^X |

Read the rows, then read the columns, then read his conjecture:

> "The conjecture that I want to make in some vague form is that actually we could extend this
> chart to the right as far as we wanted. There are many, many stories like this, and I could
> tell you as many as you had the patience to listen to."

**That is the thesis of the lecture in one sentence.** Two columns are not a coincidence. There
should be infinitely many, and there should be a single object that contains them all.

He then says the thing that makes it a talk and not a list: rather than telling you a third
story, he jumps to **the universal one**.

### 4.4 The classical model: what SH does, restated as a specification

Before proposing the new object he restates the old one as a list of demands, which is the
cleanest structural move in the hour. From §3.4: SH is a tensor category with unit S; it is
triangulated; every space X gives S[X]; every object E gives a cohomology theory
E^n(X) = Ext^n(S[X], E); and by Brown representability *every* generalized cohomology theory
arises this way, essentially uniquely. Hℤ and KU are two of its objects.

That is now a **specification**, not a description. And the conjecture is: build the same thing
for p-adic geometry.

### 4.5 The conjecture: SH_prism

> **Conjecture (vague form).** There is a category **SH_prism**, the *prismatic stable homotopy
> category*, playing the role in p-adic geometry that SH plays in topology.

The demands, in his order:

**(a)** It is a tensor category, with a unit object **S_prism** — "the prismatic version of the
sphere spectrum".

**(b)** Every p-adic formal scheme X has an associated object **S_prism^X ∈ SH_prism**, "some
kind of cohomological motive of X". Note the variance: it is *contravariant* in X — the dual of
the suspension spectrum, cohomology rather than homology.

**(c)** Every object E ∈ SH_prism defines a cohomology theory on p-adic formal schemes:

> **E-cohomology of X := Ext( unit object, E ⊗ S_prism^X )**.

**(d)** The motives satisfy a **Künneth formula**: S_prism^{X × Y} ≅ S_prism^X ⊗ S_prism^Y,
under mild assumptions.

Then the compatibility demands that tie it to §4.3:

**(e)** TC and syntomic cohomology are representable in SH_prism, by algebras he names
**KU_prism** and **Hℤ_prism** — "the avatars of the Eilenberg–MacLane spectrum and the K-theory
spectrum in this prismatic stable homotopy category".

**(f)** And — he insists on this, it is not just about groups — the representability holds **at
the level of the coefficient categories**:

> **modules over KU_prism  =  cyclotomic THH(ℤ)-modules**
> **modules over Hℤ_prism  =  prismatic F-gauges**

**(g)** Compatibly with the coefficient objects:

> **S_prism^X ⊗ KU_prism  ↔  THH(X)**
> **S_prism^X ⊗ Hℤ_prism  ↔  ℤ_prism^X**

And then the sentence quoted at the top of this tutorial: the two well-defined black boxes
should fit inside one larger black box that he does not have a definition of.

**What (f) is really saying, and why it is the strong form.** Recall from §3.4 that in classical
topology, modules over Hℤ are chain complexes. So demand (f) reads: *prismatic F-gauges are to
SH_prism as chain complexes are to SH.* He states the analogy in exactly that form later:

> "The prismatic stable homotopy category should be to the classical stable homotopy category
> as prismatic F-gauges are to the theory of chain complexes."

### 4.6 Minimal versus maximal: why he wants a big answer

He immediately concedes that the demands so far are badly underdetermined. There is a **minimal
solution**, where the only cohomology theories living in SH_prism are the ones already known —
the ones related to K-theory and syntomic cohomology. That solution is not interesting; it is
the two-column chart with a box drawn around it.

> "Instead I would like to propose that we search for a **maximal** solution."

Maximal meaning: SH_prism should be as rich as SH is. Concretely, the map from the unit S_prism
to Hℤ_prism should behave the same way as the classical map S → Hℤ. And that is where the
specification becomes testable, because there is a classical theorem describing exactly how
that map behaves.

### 4.7 The acceptance test: a prismatic Quillen theorem

The question becomes: **what distinguishes ordinary cohomology from all other cohomology
theories?**

One answer he gives and immediately discards: the cohomology of a point is concentrated in
degree zero. True, but useless as a guide — it is a statement about the dimension axiom, and the
p-adic world gives him no handle on it.

The better answer is §3.5–§3.6: ordinary cohomology is complex-oriented, and its formal group
law is the additive one. Equivalently, via Milnor and Quillen: **kill the Milnor generators in
MU and you get Hℤ.**

Now transport that. MU is built out of smooth projective varieties over ℂ — Grassmannians —
and that construction is available in algebraic geometry. So inside any candidate SH_prism you
can build:

> **MU_prism** — assembled from the motives of Grassmannians, "in a way that parallels what you
> do in classical topology". It is the universal example of a p-adic cohomology theory with
> Chern classes for **algebraic** vector bundles.

> *[Gap, by the speaker's own choice: "let me not get into details… the details of the
> construction are not the thing to focus on." No construction is given in either recording.
> **Impact: low** — he tells you explicitly that the role, not the construction, is the point.]*

And then the test:

> **The acceptance test.** Take MU_prism and mod out by the same sequence of Milnor generators.
> **Do you get Hℤ_prism?**
>
> "This I want to say is *the test that you have to pass to prove the conjecture*. You have to
> give a definition of a prismatic stable homotopy category with the properties that I've laid
> out so far. And this calculation has to work out."

Why this test and not another: because the demand was that S_prism → Hℤ_prism behave like
S → Hℤ, and classically that map factors in two steps — make it complex-oriented, then kill the
generators. Reproducing the factorization is reproducing the behaviour.

**The precedent, and the reason it is a conjecture and not a theorem.** In motivic homotopy
theory, a statement of this form is known — the **Hopkins–Morel theorem** — but for p-complete
coefficients over fields of characteristic **different from p**. Lurie is explicit that this is
not his setting: "I'm talking about things that are more like p-adic coefficients, but the
geometric objects are varieties in characteristic p."

And then the cleanest conditional in the talk:

> "It may be that somebody knows how to prove the Hopkins–Morel theorem in that context. And if
> they do, then everything in this talk that I'm describing as a conjecture can instead be
> described as a construction."

*(In the March 2025 recording he adds that Marc Hoyois extended Hopkins–Morel to the mod-p
statement when p is invertible in the ground field, and adds a hedge: "I don't know if you
should believe the Hopkins–Morel theorem in equal characteristic p, but I believe that even if
it's false these theories still exist — you just can't necessarily construct them that way."
That hedge is **not** in the ICM talk.)*

### 4.8 Why you would want it — payoff one: Steenrod operations

Two payoffs. The first is concrete and already cashed.

Quillen's theorem, he says, is essentially a repackaging of an earlier calculation: **Cartan and
Serre's determination of the Steenrod algebra.** The Steenrod algebra is Ext from Hℤ to itself
in SH — the operations that ordinary mod-p cohomology carries beyond being a graded ring. And it
matters structurally, not decoratively:

> "Those Eilenberg–MacLane objects are like the basic building blocks, and so knowing how those
> basic building blocks map to each other is something that really controls the structure of the
> entire category."

So a prismatic Quillen theorem would deliver **Steenrod operations on syntomic cohomology and on
prismatic cohomology.** He stresses this is not an arbitrary test: "I took the important
structural theorem in algebraic topology and asked for something that would really control the
whole structure of SH_prism if it were true." *(That last sentence is from the March 2025
recording; the ICM version is the "basic building blocks" quote above.)*

**And this part is already done, in a case.** Recent work of **Shachar Carmeli and Tony Feng**
constructs these operations for algebraic varieties over fields of characteristic p, and applies
them:

> **Carmeli–Feng, "Prismatic Steenrod operations and arithmetic duality on Brauer groups",
> [arXiv:2507.13471](https://arxiv.org/abs/2507.13471), submitted 17 July 2025.** From the
> abstract: they construct and analyse "the syntomic Steenrod algebra, which acts on the mod p
> syntomic cohomology (also known as étale-motivic cohomology) of algebraic varieties in
> characteristic p", and apply it "to resolve the last open cases of a 1966 Conjecture of Tate,
> concerning the existence of a symplectic form on the Brauer groups of smooth proper surfaces
> over finite fields." They also organise their theories "into a category of *spectral prismatic
> F-gauges*, generalizing the prismatic F-gauges of Drinfeld and Bhatt–Lurie."

The ICM talk says they proved Tate's conjecture "in, well, in the trickiest cases let's say";
the March 2025 talk says "some concrete statements about Brauer groups of surfaces in
characteristic two". The paper's own abstract says "the last open cases". **I quote the paper.**

Lurie's verdict: "I think of this as kind of a proof of concept."

### 4.9 Why you would want it — payoff two: a bigger catalogue

The second payoff is the one he says was his actual motivation, and it is the §3.5 punchline
transported.

The heuristic content of Quillen's theorem: *there are roughly as many cohomology theories in
topology as there are formal groups.* A prismatic Quillen theorem would say: **there are roughly
as many cohomology theories in p-adic geometry as there are formal groups.**

And therefore there is a translation rule:

> **A huge number of cohomology theories on ordinary topological spaces would have counterparts
> in p-adic geometry. Namely: look for a p-adic cohomology theory where the formal groups match
> up.**

And each of those counterparts would come with its own version of the story in §4.1 — its own
TC, its own THH, its own spectral sequence down to something differential-form-like. The whole
K-theory column would be one instance of an infinite family.

Then the closing motivation, already quoted, and worth reading once more slowly:

> "This was my original motivation. There are some invariants that I can compute without being
> able to define, and I'm searching for the definition of what it is that I am computing."

### 4.10 The evidence: a relative version that actually exists

He closes with one piece of hard evidence, and it is a genuine construction rather than a
conjecture.

Let R be a p-complete ring and X = Spec R. Define the **relative** prismatic stable homotopy
category:

> **SH_prism(R) := modules over S_prism^X inside SH_prism.**

Since S_prism^X is an algebra, its modules form a category, and just as SH_prism was supposed to
be a world of cohomology theories on *all* p-adic formal schemes, this relative version is a
world of cohomology theories on p-adic formal schemes **living over X**.

He is careful: "I'm calling this a definition, but that's maybe a little bit misleading. It's a
provisional definition. It's a conditional definition, because I don't have a definition of this
prismatic stable homotopy category."

**But the relative version can be defined outright in a real case:**

> If R is any p-complete ring carrying a **compatible system of p^n-th roots of unity**, then
> there is a definition you can write down that has all of the expected properties.

> "And in particular, that is true when R is a ring in which p is equal to zero. For example,
> ℤ mod p. And in that case, the construction was essentially written down in this work of
> Carmeli and Feng that I mentioned earlier."

> *[Reconstruction, flagged: why does p = 0 in R make the roots-of-unity condition automatic? In
> characteristic p, x^{p^n} = 1 forces (x−1)^{p^n} = 0, so the only p-power root of unity is 1
> and the constant system 1, 1, 1, … is a compatible system. The condition is satisfied
> trivially. **Neither recording says this**; it is my explanation of his aside. The March 2025
> recording gives the mechanism differently and more precisely: Carmeli–Feng construct the theory
> over the cyclotomic base ring ℤ_p[ζ_{p^∞}]^∧, and 𝔽_p is an algebra over that base, so the
> theory descends to 𝔽_p. That is the route, and it is his own account of it — from the 2025
> talk, not the ICM one.]*

> *[Gap: no definition is given, in either recording, of the relative construction. "There's a
> definition that you can write down that has all of the expected properties" is the entire
> content. **Impact: moderate.** This is the only unconditional mathematics in the last third of
> the talk and it is a pointer, not a statement. To recover it you must go to arXiv:2507.13471.]*

And that is where he stops. "All right, I think that is all I have to say."

---

## 5. The one conjecture, stated precisely

Strip the narrative and one specification carries the lecture. Here it is with every symbol
defined, exactly at the depth the sources support and no deeper.

**Setup.** p is a fixed prime. All rings are p-complete; all invariants are p-adically
completed. SH is the classical stable homotopy category, with unit S, Eilenberg–MacLane object
Hℤ, complex K-theory object KU, and complex cobordism object MU. THH is topological Hochschild
homology; TC is topological cyclic homology, p-completed. "Syntomic cohomology" is the
Bhatt–Morrow–Scholze integral theory. "Prismatic F-gauges" and "cyclotomic spectra" are treated
as black boxes with two properties each: tensor category, and triangulated so Ext exists.

**The conjecture.** There exists a symmetric monoidal, triangulated category **SH_prism** with
unit **S_prism**, together with, for each p-adic formal scheme X, an object **S_prism^X**
contravariant in X, such that:

1. **(Cohomology theories)** Each E ∈ SH_prism defines a cohomology theory on p-adic formal
   schemes by X ↦ Ext(S_prism, E ⊗ S_prism^X).
2. **(Künneth)** S_prism^{X × Y} ≅ S_prism^X ⊗ S_prism^Y, under mild hypotheses.
3. **(K-theory)** There is an algebra KU_prism ∈ SH_prism representing TC, whose module
   category is the category of cyclotomic THH(ℤ)-modules, with
   S_prism^X ⊗ KU_prism ↔ THH(X).
4. **(Ordinary cohomology)** There is an algebra Hℤ_prism ∈ SH_prism representing syntomic
   cohomology, whose module category is the category of prismatic F-gauges, with
   S_prism^X ⊗ Hℤ_prism ↔ ℤ_prism^X.
5. **(Maximality)** SH_prism is to SH as prismatic F-gauges are to chain complexes. Precisely
   enough to test: the unit map S_prism → Hℤ_prism factors as S_prism → MU_prism → Hℤ_prism,
   where MU_prism is built from the motives of Grassmannians, and the second map is the quotient
   by Milnor's generators.

**The acceptance test.** Any proposed definition of SH_prism must satisfy 1–4, and must satisfy
the **prismatic Quillen theorem**: MU_prism modulo Milnor's generators is Hℤ_prism.

**Status, honestly.**

| Item | Status |
|---|---|
| SH_prism in general | **No definition exists.** This is the point of the talk. |
| Prismatic Quillen theorem | **Open**, and it is the stated acceptance test. |
| Analogue in motivic homotopy theory | **Known** (Hopkins–Morel) for p-complete coefficients over fields of characteristic ≠ p — **not** this setting. |
| Steenrod operations on syntomic cohomology in char p | **Constructed** (Carmeli–Feng, arXiv:2507.13471), with a proof of Tate's 1966 conjecture as application. |
| Relative SH_prism(R), R with p-power roots of unity | **Constructible**, "with all of the expected properties"; over 𝔽_p, essentially in Carmeli–Feng. No definition given in either recording. |
| The conditional | If someone proves Hopkins–Morel in this context, **the conjectures become constructions.** His words. |

**What I will not pretend to.** I have not told you what a cyclotomic spectrum is, what a
prismatic F-gauge is, or what the higher-categorical substrate of SH_prism would be. Neither did
he — he declined the first two explicitly from the podium and never raised the third. Each
appears here as a fact with its motivation and its consequence, and no more. That is deliberate,
and it follows the same decision made in `summaries/langlands-function-fields-gaitsgory.md` for
AGCat and 2-IndCoh. These objects are not learnable from a lecture, and a smooth account of them
would be a fabrication you could not detect.

---

## 6. What the chart is really claiming

One short section, because it is the piece most likely to be misread.

Look again at §4.3. It is tempting to read it as an analogy table — "K-theory is like ordinary
cohomology in the following ways". It is not. **Rows two through five are constructions, not
resemblances**: each row is produced from the row above it by a specific operation, and the
operations are the same in both columns.

- Row 1 → Row 2: find the algebro-geometric analogue of a topological cohomology theory.
- Row 2 → Row 3: **p-complete, and force étale descent.** Same operation in both columns, and by
  Clausen–Mathew–Morrow it is the *only* difference in the left column.
- Row 3 → Row 4: express the invariant as Ext out of a unit object in a suitable coefficient
  category. Same shape in both columns.
- Row 4 → Row 5: the coefficient object attached to X — the "motive".
- Row 5: **Künneth holds here, and only here.**

So the conjecture "extend the chart to the right" is not "find more analogies". It is: *the
operations that build the chart do not depend on which cohomology theory you start with, so
starting from any object of SH you should get a column, and all the columns should live in one
category.* That is exactly the relation between SH and the classical catalogue — Brown
representability says the catalogue *is* the objects of one category — and it is why he goes
straight to SH_prism instead of telling a third story.

And read row 5 once more against §2.1. **Every column ends at the place where factorization
holds.** The last row is not the bottom of the construction; it is the level at which the
pipeline is still compositional. Everything above it has already destroyed the Künneth formula by
taking Ext too early.

---

## 7. Do this by hand

Two exercises. The first takes twenty minutes and shows you what K-theory is by breaking it. The
second is straight calculus and delivers the punchline of the whole lecture.

### 7.1 Group completion, and why "finitely generated" is not a technicality

Recall §3.2: K-theory is the group completion of a monoid of objects under ⊕.

**(a)** Let M be the monoid of isomorphism classes of finite-dimensional complex vector spaces
under ⊕. Identify M, and compute its group completion. Confirm it is ℤ.

**(b)** State the group completion abstractly: for a commutative monoid (M, +), the group
completion is the set of formal differences a − b with a, b ∈ M, modulo the relation a − b ~
a′ − b′ iff a + b′ + c = a′ + b + c for some c ∈ M. Explain in one sentence why that extra "+ c"
is needed — i.e. give a monoid where dropping it fails to give an equivalence relation, or at
least fails to give the right answer.

**(c)** Now break it. Let M∞ be the monoid of isomorphism classes of complex vector spaces of
**countable** dimension (so ℂ^0, ℂ^1, ℂ^2, …, and ℂ^∞), under ⊕. Compute the group completion of
M∞. Then say, in one sentence, why algebraic K-theory is defined using **finitely generated**
projective modules and not arbitrary ones.

<details>
<summary>Solutions</summary>

**(a)** A finite-dimensional complex vector space is determined up to isomorphism by its
dimension, and ⊕ adds dimensions. So M ≅ (ℕ, +). The group completion of (ℕ, +) is (ℤ, +): the
formal difference a − b is the integer a − b, and every integer arises. This is literally the
construction of the integers from the natural numbers, and it is literally the definition of
KU⁰(pt) = ℤ. Lurie gives exactly this example.

**(b)** Without the "+ c", the putative relation need not be transitive in a monoid that is not
cancellative. Concretely, take M = {0, 1, 2, …} ∪ {∞} with ∞ + n = ∞. Then 1 + ∞ = 0 + ∞, so we
would want 1 − 0 ~ 0 − 0, i.e. 1 ~ 0 — which is only visible if you are allowed to add a witness
c = ∞. The correct definition builds that witness in. (In (ℕ,+), which is cancellative, you never
need c, which is why the construction of ℤ looks simpler than it is.)

**(c)** In M∞ we have ℂ^∞ ⊕ ℂ^n ≅ ℂ^∞ for every n, including n = ∞. So in the group completion,
[ℂ^∞] + [ℂ^n] = [ℂ^∞], and subtracting [ℂ^∞] — which is now legal, since we have inverses —
gives **[ℂ^n] = 0 for every n**. The group completion is the **trivial group**. Everything
collapses.

This is the **Eilenberg swindle**, and it is the whole reason for the finiteness hypothesis.
An object that absorbs copies of itself has no interesting K-theory: allow infinite direct sums
and the invariant is zero. So "finitely generated projective" is not bureaucratic hedging — drop
it and the subject evaporates. Equivalently: K-theory measures how objects fail to be
cancellable, and infinite objects cancel everything.

*(The swindle is standard and is not in either recording; the exercise is mine.)*

</details>

### 7.2 Formal group laws, the logarithm, and where the denominators go

This is the exercise. It is calculus, it takes forty minutes, and at the end you will understand
why this talk is about p-adic geometry.

Recall §3.5: a **one-dimensional formal group law** over a commutative ring A is a power series
F(x, y) ∈ A[[x, y]] with

> F(x, 0) = x,  F(x, y) = F(y, x),  F(F(x, y), z) = F(x, F(y, z)).

**(a)** Check that **F_a(x, y) = x + y** (the *additive* law) satisfies all three.

**(b)** Check that **F_m(x, y) = x + y + βxy** (the *multiplicative* law), for β any element of
A, satisfies all three. Hint for associativity: factor 1 + βF_m(x,y).

**(c)** An **isomorphism** from F to G is a power series f(x) = x + (higher terms) with
f(F(x,y)) = G(f(x), f(y)). Suppose A is a ℚ-algebra. Define

> **log_F(x) := ∫₀^x dt / F_y(t, 0)**,  where F_y(x, y) := ∂F/∂y.

Compute log_F for F_a and for F_m. Then verify directly, for F_m, that
log(F_m(x,y)) = log(x) + log(y) — i.e. that log_{F_m} is an isomorphism from the multiplicative
law to the additive one.

**(d)** Look at the coefficients of log_{F_m}. Which primes appear in the denominators? Conclude:
over ℚ, how many one-dimensional formal group laws are there up to isomorphism? Over ℤ_p, is the
same argument available?

**(e)** Now connect it back. Ordinary cohomology has the additive formal group law and complex
K-theory has the multiplicative one (§3.5). Using (d), say in one sentence why Lurie's slogan
"there are roughly as many cohomology theories as there are formal groups" would be *empty* if
the coefficients were rational — and therefore why the whole talk lives p-adically.

<details>
<summary>Solutions</summary>

**(a)** F_a(x,0) = x ✓. Symmetry ✓. F_a(F_a(x,y),z) = (x+y)+z = x+(y+z) = F_a(x,F_a(y,z)) ✓.

**(b)** F_m(x,0) = x + 0 + 0 = x ✓. Symmetry is clear ✓. For associativity, note
1 + βF_m(x,y) = 1 + βx + βy + β²xy = (1 + βx)(1 + βy). So if we write u = 1 + βx, v = 1 + βy,
w = 1 + βz, then 1 + βF_m(a,b) is multiplicative in exactly this sense, and
1 + βF_m(F_m(x,y), z) = (1 + βF_m(x,y))·w = uvw, which is symmetric in u, v, w. Hence
F_m(F_m(x,y),z) = F_m(x,F_m(y,z)) ✓. **That factorization is the reason it is called
multiplicative**: it is the group law on 1 + βx, i.e. on the multiplicative group, written in
the coordinate x = (u − 1)/β.

**(c)** For F_a: F_y(x,y) = 1, so F_y(t,0) = 1 and **log_{F_a}(x) = x**. The additive law is
already additive.

For F_m: F_m = x + y + βxy, so ∂F/∂y = 1 + βx, hence F_y(t,0) = 1 + βt and

> **log_{F_m}(x) = ∫₀^x dt/(1 + βt) = (1/β)·ln(1 + βx) = Σ_{n ≥ 1} (−1)^{n−1} β^{n−1} x^n / n**
> = x − βx²/2 + β²x³/3 − β³x⁴/4 + …

Verification: log(F_m(x,y)) = (1/β)ln(1 + β(x + y + βxy)) = (1/β)ln((1 + βx)(1 + βy))
= (1/β)ln(1 + βx) + (1/β)ln(1 + βy) = log(x) + log(y). ✓ Exactly the additive law in the new
coordinate.

**(d)** The coefficient of x^n is ±β^{n−1}/n. **Every prime appears in the denominators**, since
every integer n appears. So the argument needs 1/n for all n — i.e. it needs A to be a
ℚ-algebra. Over a ℚ-algebra, this construction generalizes: **every** one-dimensional formal
group law is isomorphic to the additive one via its logarithm, so **there is exactly one, up to
isomorphism**.

Over ℤ_p the argument is unavailable: 1/p does not exist, so the term ±β^{p−1}x^p/p is not
integral, and the logarithm is not a power series over ℤ_p. And indeed the classification over
ℤ_p (or over 𝔽_p) is rich — formal group laws are graded by an invariant called *height*, with
the additive law at height ∞ and the multiplicative law at height 1, and they are genuinely
non-isomorphic.

**(e)** If the coefficients were rational, there would be **one** formal group law up to
isomorphism, so "as many cohomology theories as formal groups" would say there is essentially
one cohomology theory — which is false and useless. **The entire catalogue lives in the failure
of the logarithm to be integral.** Since that failure is prime-by-prime, the catalogue is
inherently p-adic. That is why Lurie's conjecture is about *p-adic* geometry and about
*p*-complete invariants, and it is why the Hopkins–Morel precedent (characteristic ≠ p) does not
settle his case: it is proved exactly where the p-adic difficulty is not.

**Marked as reconstructed:** this exercise is mine end to end. The talk states that MU carries
the universal formal group law and gives the additive law for ordinary cohomology; it never
writes down the multiplicative law, the logarithm, or the denominators. What would verify it: the
identity 1 + βF_m(x,y) = (1+βx)(1+βy), checkable in one line, plus term-by-term integration of
1/(1+βt).

</details>

---

## 8. What is actually useful to you

The mathematics will not transfer. Four things will, and two of them are unusually sharp because
Lurie states them as method rather than leaving them implicit.

### 8.1 A surrogate is worth having only when you can say exactly what it loses

This is the strongest transferable idea in the talk (§2.2, §4.1).

K-theory is intractable. TC is tractable. Everyone builds surrogates like that. What makes this
one a research programme rather than a heuristic is the **certificate**: Clausen–Mathew–Morrow
identify *exactly three* properties by which TC differs from K, and prove that on p-complete
rings those three are the whole difference — TC is K-theory with those three properties forced
on it, and nothing else changed.

Note the form of the certificate. It is not an error bound. It is a **universal property**: TC
is the closest object to K that satisfies the three constraints. You get an exact statement of
what was traded away, so you know precisely when the surrogate is safe to use and when it is
not — and the two known blind spots (it only sees the p-adic completion of R; it satisfies étale
descent whether or not you wanted that) are *stated in advance*, not discovered by failure.

For your work: this is the difference between "the cheap evaluator agrees with the expensive one
on my test set" and "the cheap evaluator is the expensive one with these three specific
invariances imposed, and here is the proof." The first tells you nothing about inputs you have
not tried. The second tells you the full set of failure modes up front — they are exactly the
distinctions the imposed invariances collapse. **When you build a cheap stand-in for an expensive
check, the deliverable is not the stand-in, it is the characterization of what it cannot see.**

### 8.2 When composition breaks, move the collapse later in the pipeline

§2.1, and it is the design principle behind every object he introduces.

The pattern, three times over: the invariant you want is computed as *(build a coefficient
object)* then *(take Ext out of the unit)*. The first step respects products. The second does
not. So the composition law fails for the invariant, and it is unfixable **at the level of the
invariant** — because the damage was already done by the time you looked.

The fix is never a correction term. It is: **stop working with the output, work with the
intermediate object, and defer the collapsing step to the very end.** THH exists because K-theory
and TC lose Künneth and THH does not. Prismatic F-gauges exist because syntomic cohomology loses
Künneth and the motives do not. Both objects are, in effect, "the last stage of the pipeline
before compositionality dies".

You compose for a living — skills, subagents, MCP servers, tool chains. The transferable
question: **at which stage of my pipeline does composability die, and am I doing that stage
earlier than I need to?** If your agents exchange rendered text when they could exchange the
structured object the text was rendered from, you have taken the Ext early. Everything downstream
then needs a special case, and the special cases are the corrections you are paying instead of
just moving the render to the end.

The cross-reference is not decorative: Gaitsgory's plenary spends its hour on the same failure
with the same cure — see `summaries/langlands-function-fields-gaitsgory.md` §7.3, where one
broken Künneth formula forces the reconstruction of an entire ambient 2-category. Two fields, two
speakers, one lesson about compositionality laws.

### 8.3 Publish the specification and the acceptance test, before the implementation

This talk is a **spec**, delivered from a plenary podium, for an object that does not exist.

Look at the structure of §4.5 to §4.7 with engineering eyes. He gives a list of required
properties (1–4), a statement of the desired *richness* rather than mere correctness (5, the
maximal-versus-minimal discussion — a minimal implementation would satisfy the interface and be
worthless), and then **one concrete acceptance test that any implementation must pass**: the
prismatic Quillen theorem. Not a vague "it should be useful". A specific calculation with a
specific expected answer.

And then the conditional that makes the whole thing falsifiable and hand-offable: *if someone
proves Hopkins–Morel in this context, everything I have called a conjecture becomes a
construction.* He has told the audience precisely which external result would convert his
speculation into mathematics.

That is spec-first development, and the parts worth stealing are the two that people usually
skip: **the anti-degenerate clause** (state why the minimal implementation satisfying your
interface would be useless, so nobody builds it), and **the single acceptance test** (one
concrete case with a known expected answer, chosen because it controls the structure rather than
because it is easy). For agent systems: an eval that a trivial implementation passes is not an
eval, and "it should behave sensibly" is not a spec.

### 8.4 It is legitimate to compute with something you cannot define

The closing motivation — "there are some invariants that I can compute without being able to
define, and I'm searching for the definition of what it is that I am computing" — is worth
sitting with, because the instinct in engineering runs the other way.

He has a working procedure that produces answers he trusts, and no account of what object the
procedure is computing. He does not stop using the procedure. He treats the missing definition as
the research problem and keeps computing in the meantime. And he does something more useful than
waiting: he writes down what the object would have to satisfy, which is what makes the search
finite.

This is the healthy version of a pattern you will recognize from working with systems whose
behaviour outruns their specification. The mistake is not using the thing you cannot fully
characterize. The mistake is **not writing down what you are assuming about it** — because then
when it fails you have no way to tell whether the assumption or the implementation broke. Lurie's
list of demands is exactly that document.

---

## 9. Where to read next

Three, ordered. None is easy; the first is the only one that is really an on-ramp.

1. **The March 2025 recording of this same lecture** —
   [youtube.com/watch?v=1fSd7FxEA3w](https://www.youtube.com/watch?v=1fSd7FxEA3w), Simons
   Foundation, 49 minutes. Same title, same conjecture, same acceptance test, but for
   specialists: it names Nikolaus–Scholze, lays out the Drinfeld/Bhatt syntomic stack ℤ_p^syn
   and the specific loci on it that give de Rham, crystalline, Hodge–Tate, prismatic and
   q-de Rham cohomology, and gives the parallel list of what those loci give when you use
   KU_prism instead (TP, TC⁻, THH, periodic Hochschild homology). If the ICM talk left you
   wanting the *contents* of the black boxes, this is where the extra half-inch is.
2. **Bhargav Bhatt, *Prismatic F-gauges*, Princeton MAT 549, Fall 2022 lecture notes** —
   [math.ias.edu/~bhatt/teaching/mat549f22/lectures.pdf](https://www.math.ias.edu/~bhatt/teaching/mat549f22/lectures.pdf).
   The standard written reference for the second black box, by the person who built much of it.
   This is where "prismatic F-gauge" stops being a black box, at real cost in prerequisites.
3. **Carmeli and Feng, *Prismatic Steenrod operations and arithmetic duality on Brauer groups*** —
   [arXiv:2507.13471](https://arxiv.org/abs/2507.13471). The one place where the picture in this
   talk is a construction rather than a conjecture: the syntomic Steenrod algebra, the category
   of spectral prismatic F-gauges, and the resolution of Tate's 1966 conjecture. Read the
   introduction; it is written to be read.

For the K-theory computation he uses as his motivating example, and does not attribute:
Antieau, Krause and Nikolaus, *On the K-theory of ℤ/p^n*,
[arXiv:2405.04329](https://arxiv.org/abs/2405.04329).

---

## 10. Self-test

<details>
<summary>1. What is a generalized cohomology theory, and which single axiom is dropped?</summary>

A functor from spaces to graded abelian groups satisfying the Eilenberg–Steenrod package —
homotopy invariance, long exact sequences, excision, Mayer–Vietoris, additivity — but **not** the
**dimension axiom**, which requires the cohomology of a point to be concentrated in degree 0.
Dropping it costs uniqueness and keeps computability, which is why there is a catalogue of
theories rather than one. Complex K-theory is the basic example: KU^n(pt) = ℤ in every even
degree (Bott periodicity), not just in degree 0.
</details>

<details>
<summary>2. Define K⁰ of a space and K₀ of a ring, in the same sentence.</summary>

Take a commutative monoid under direct sum — complex vector bundles on X in the topological
case, finitely generated projective modules over R in the algebraic case — and **group-complete
it**, formally adjoining inverses exactly as ℕ becomes ℤ. Both give ℤ on the simplest example (a
point; a field). Atiyah–Hirzebruch ~1960 for the topological version; Grothendieck earlier for
the algebraic one, which the topological definition was imitating.
</details>

<details>
<summary>3. What is TC, why does anyone use it, and what does it cost?</summary>

TC is topological cyclic homology, p-adically completed, introduced by Bökstedt–Hsiang–Madsen
around 1990. There is a trace map K(R) → TC(R); TC is far more computable than K. The cost is
three specific defects: it is p-complete by fiat, it therefore depends only on the p-adic
completion of R, and it satisfies étale descent — none of which K-theory does. The point is that
by a theorem of Clausen–Mathew–Morrow those three are the **entire** difference on p-complete
rings: TC is K-theory with exactly those properties forced on it.
</details>

<details>
<summary>4. Why does THH exist, if TC is the thing you wanted?</summary>

Two reasons, both stated in the talk. **Computability:** THH is one spectral sequence away from
algebraic differential forms — for R smooth over 𝔽_p, reducing THH(R) modulo Bökstedt's degree-2
generator in THH(𝔽_p) gives Hochschild homology, which by HKR is the algebraic differential
forms of R. **Künneth:** THH(R ⊗_k S) ≅ THH(R) ⊗_{THH(k)} THH(S), naively, in cyclotomic
spectra — whereas neither algebraic K-theory nor TC has any obvious Künneth formula. TC is
recovered as Ext(unit, THH(R)) in cyclotomic THH(ℤ)-modules, and it is precisely that last Ext
step that destroys the Künneth property.
</details>

<details>
<summary>5. State the two-column chart from memory, and say what the conjecture does to it.</summary>

Left column: complex K-theory KU → algebraic K-theory → TC → Ext in cyclotomic THH(ℤ)-modules,
with coefficient object THH(X). Right column: ordinary cohomology Hℤ → motivic cohomology →
syntomic cohomology → Ext in prismatic F-gauges, with coefficient object ℤ_prism^X. Row 2 to row
3 is "p-complete and force étale descent" in both columns. Künneth holds only in the last row.
The conjecture is that the chart extends **rightward** indefinitely, and that all the columns are
objects of one category, SH_prism — exactly as Brown representability makes the classical
catalogue the objects of SH.
</details>

<details>
<summary>6. What must SH_prism satisfy, and what is the single test?</summary>

A tensor category with unit S_prism; a contravariant motive S_prism^X for each p-adic formal
scheme X; cohomology theories as Ext(unit, E ⊗ S_prism^X); a Künneth formula for the motives; an
algebra KU_prism whose modules are cyclotomic THH(ℤ)-modules and which represents TC; an algebra
Hℤ_prism whose modules are prismatic F-gauges and which represents syntomic cohomology; and
maximality — SH_prism should be to SH as F-gauges are to chain complexes. **The test:** build
MU_prism from the motives of Grassmannians, mod out by Milnor's generators, and check you get
Hℤ_prism. That is the prismatic Quillen theorem, and Lurie says it is the test any proof must
pass.
</details>

<details>
<summary>7. What is a formal group law, and what is Quillen's theorem?</summary>

A power series F(x,y) with F(x,0) = x, commutative and associative — the group law of a
one-dimensional group written as a formal power series, the way BCH writes Lie group
multiplication near the identity. It arises from a complex-oriented cohomology theory as the
rule for c₁(L₁ ⊗ L₂) in terms of c₁(L₁) and c₁(L₂); ordinary cohomology gives the additive law.
Milnor computed MU^*(pt) to be a polynomial ring on generators in each even degree; Quillen
identified that ring as the one classifying formal group laws, so MU carries the **universal**
formal group law. Heuristic consequence: there are roughly as many cohomology theories as there
are formal groups.
</details>

<details>
<summary>8. Why must this story be p-adic rather than rational?</summary>

Because over a ℚ-algebra every one-dimensional formal group law is isomorphic to the additive
one, via the logarithm log_F(x) = ∫₀^x dt/F_y(t,0) — whose coefficients have every integer in the
denominator. One formal group law up to isomorphism means, by Quillen's heuristic, essentially
one cohomology theory: the slogan is empty. Kill the denominators — work over ℤ_p or 𝔽_p — and a
rich classification appears. The catalogue lives entirely in the non-integrality of the
logarithm, which is a prime-by-prime phenomenon. It is also why the Hopkins–Morel precedent does
not settle Lurie's case: it holds for characteristic ≠ p, which is exactly where the difficulty
is not.
</details>

<details>
<summary>9. What would a prismatic Quillen theorem buy, concretely?</summary>

Two things. **Steenrod operations** on syntomic and prismatic cohomology, because classically
Quillen's theorem is a repackaging of Cartan–Serre's determination of the Steenrod algebra — Ext
from Hℤ to itself — which controls the structure of the whole stable homotopy category. Already
cashed in a case: Carmeli–Feng constructed these operations in characteristic p and used them to
resolve the last open cases of Tate's 1966 conjecture on symplectic forms on Brauer groups of
smooth proper surfaces over finite fields. And **a bigger catalogue**: a translation rule saying
that any cohomology theory on topological spaces should have a p-adic counterpart with the same
formal group, each carrying its own TC/THH story.
</details>

<details>
<summary>10. What actually exists today, as opposed to being conjectured?</summary>

SH_prism itself: no definition. The prismatic Quillen theorem: open. What does exist: the two
black boxes at either end (cyclotomic spectra, prismatic F-gauges) are well-defined; the
Steenrod operations in characteristic p are constructed (Carmeli–Feng); and a **relative**
version SH_prism(R) — modules over S_prism^X — can be defined outright whenever R is a p-complete
ring carrying a compatible system of p^n-th roots of unity, which includes every ring in which
p = 0, e.g. ℤ/p. Over 𝔽_p that construction is essentially in Carmeli–Feng. Neither recording
gives the definition.
</details>

---

## 11. Note on the tutorial process

**Difficulty against reputation: partially matched, and the split is the finding.** Lurie's
reputation predicts maximal abstraction, and the *objects* deliver exactly that — a 5. What the
transcript settled, and no amount of reputation would have predicted, is that **he black-boxes
the hard objects himself, out loud, twice**, and builds the entire hour on two consequences
("tensor category", "triangulated category, so Ext makes sense") that a physicist can hold. The
narrative as delivered is a 3. This is the reverse of the Gaitsgory case, where the speaker
warned the room they would not follow; here the speaker engineered the talk so they would.

**Rule 1 in action: the brief's anchor was wrong and the transcript said so.** The brief proposed
∞-categories and homotopy — "equal" replaced by "connected by a path" — as the honest anchor.
**The talk never says "∞-category", "higher category", or "homotopy" in that sense, once.** Using
it would have been decorating this talk with someone else's picture, exactly as the Gaitsgory
tutorial declined to import Kapustin–Witten. I named it as present-and-untaught in one paragraph
(§2.4) and anchored instead to what the talk actually repeats: **Künneth as the factorization of
independent subsystems** (§2.1), the **certified surrogate** (§2.2), and **spectral sequences as
perturbation series** (§2.3). The first of these is not a loose analogy — it is the stated design
criterion for both THH and prismatic F-gauges, in his own words, twice.

**How much mathematics survived the captions: most of the shapes, none of the indices.** This is
the important correction to the brief, which predicted a board talk whose formulas the captions
would destroy entirely. It was a **slide** talk, and more to the point **a talk of spoken
formulas**: Lurie states TC(R) = Ext(unit, THH(R)), THH(𝔽_p) = a polynomial ring on one generator
of degree 2, the THH Künneth formula, ℤ_prism^{X×Y} = ℤ_prism^X ⊗ ℤ_prism^Y, MU^*(pt) = a
polynomial ring on one generator in each even degree, and "mod out MU by those generators and you
get Hℤ" — **all in words, all caught by the captions.** What died on the slides is the indexing:
degrees, weights, Tate twists, spectral-sequence pages, and the one displayed Künneth formula for
syntomic cohomology.

**Sources, precisely.** No proceedings paper. No companion on `math.ias.edu/~lurie/` — I checked;
the site lists nothing on prismatic anything and nothing after December 2019 apart from the three
books, and the talk covers none of them. He names no survey of his own from the podium. I used a
second recording of the same lecture (Simons Foundation, 14 March 2025, video `1fSd7FxEA3w`,
same title, more technical) as a labelled cross-check, and marked every place I drew on it. I
restored theorem statements from the primary literature for the individual results, cited inline.
The 2025 recording's transcript was cleaned into my scratchpad, not into `transcripts/`.

**Name corrections.** Auto-captions destroyed almost every proper noun in this talk. Verified
against a primary source unless marked.

| Caption | Correct | Verified against |
|---|---|---|
| "prismatics tabletop theory" (announcer) | **Prismatic Stable Homotopy Theory** | title of the March 2025 talk, same speaker, same content — *reconstructed* |
| Jacob Lurri | **Jacob Lurie** | — |
| piotic / piatic / ptic / "the pi world" | **p-adic** | — |
| Atia and Hibrook | **Atiyah and Hirzebruch** | — |
| bot periodicity | **Bott periodicity** | — |
| hop / hop vibrations | **Hopf / Hopf fibrations** | — |
| Adams and AIA | **Adams and Atiyah**, *K-theory and the Hopf invariant* | Quart. J. Math. **17** (1966), 31–38 — an 8-page paper, matching the talk exactly |
| Erdos | **Erdős** ("proof from the Book") | — |
| growth / "here's a growth" | **Grothendieck** | — |
| Quillin | **Quillen** | — |
| Boxet, Siang and Madson | **Bökstedt, Hsiang and Madsen** | — |
| Claus and Matthew and Morrow | **Clausen, Mathew and Morrow** | — |
| Hawkshield / Hawk shield hommology | **Hochschild homology** | — |
| cyclomic / cycllatomic / cycatomic spectra | **cyclotomic spectra** | — |
| kunith / kunth / kuni / "kun formula" | **Künneth** | — |
| tall descent | **étale descent** | — |
| coalology / komology / chology / coaly | **cohomology** | — |
| aelion | **abelian** | — |
| aphine | **affine** | — |
| "aier here" / "AIA here's a brook" | **Atiyah–Hirzebruch** | — |
| Lavine and Freedellander Suslan | **Levine and Friedlander–Suslin** | speaker's own attribution; not independently checked |
| bot mororrow and schulza / Bot Marorrow and Schultz | **Bhatt, Morrow and Scholze** | — |
| Bot and Schultz | **Bhatt and Scholze** | — |
| syntoic coalology / syntoicology | **syntomic cohomology** | — |
| eenberg mlan / island mlan / Ember Mlan / Einberg MLAN | **Eilenberg–MacLane** | — |
| bortism / complex bortism | **cobordism / complex cobordism** | — |
| Milner | **Milnor** | — |
| churn classes | **Chern classes** | — |
| brasmanians | **Grassmannians** | — |
| Hopkins morel / Hopkins morale | **Hopkins–Morel** | — |
| Carton and S's | **Cartan and Serre** | — |
| Steinrod / steamrod algebra | **Steenrod algebra** | — |
| **Carmeli and Fang / Carmel and Fang / Carmelian Fang** | **Shachar Carmeli and Tony Feng** | [arXiv:2507.13471](https://arxiv.org/abs/2507.13471), submitted 17 July 2025 — title and author list confirmed |
| Brower groups | **Brauer groups** | Carmeli–Feng abstract |
| fbanius | **Frobenius** | — |

From the **March 2025 recording only**, listed separately because none of it is in the ICM talk
and I have used almost none of it in the body: "Nickola schet" → **Nikolaus–Scholze**; "bargo's
notation" → **Bhargav** [Bhatt]; "niggard filtration" → **Nygaard filtration**; "lzard ring" →
**Lazard ring**; "atoms operations" → **Adams operations**; "Mark HOA" → **Marc Hoyois**; "Ben
antiu and Noah riggenbach" → **Ben Antieau and Noah Riggenbach**; "Dustin and aille" →
**Dustin Clausen and Akhil Mathew**; "tasos Molinos… Von toin… Rob, I forgot his first name,
Marco" → **Moulinos, Toën and Robalo** *(reconstructed; plausible from the surnames and the
subject matter, not verified)*.

**Substantive corrections beyond spelling.** Two, neither dangerous:

- The captions render the K-theory of the ring "**Z mod 4**" correctly but never name the people
  who computed it. That computation is Antieau–Krause–Nikolaus, arXiv:2405.04329, and it uses
  prismatic cohomology — which is why he chose the example. **The talk does not name them**; the
  attribution in §4.1 is mine.
- The talk describes Carmeli–Feng as proving Tate's conjecture "in the trickiest cases", and the
  2025 recording says "characteristic two". The paper's own abstract says "the last open cases"
  and describes the general result as symplectic structure on higher Brauer groups of
  even-dimensional varieties over finite fields. **I quote the paper**, and flag the difference
  in §4.8.

**Reconstructed, and what would verify each:**

- **The lecture title.** From the announcer's mangled "prismatics tabletop theory" plus the
  identical title of the March 2025 recording. The ICM programme would settle it.
- **The two-column chart (§4.3).** Layout mine; every cell is stated aloud in the talk.
- **The Atiyah–Hirzebruch E₂ page** (§4.2). Standard; he gives it in words only.
- **The multiplicative formal group law and the logarithm** (§3.5, Exercise 7.2). Entirely mine;
  the talk gives only the additive law. Verify via 1 + βF(x,y) = (1+βx)(1+βy).
- **The Eilenberg swindle** (Exercise 7.1c). Standard, not in either recording.
- **Why p = 0 makes the roots-of-unity condition automatic** (§4.10). Mine. Verify: in
  characteristic p, x^{p^n} = 1 ⟹ (x−1)^{p^n} = 0 ⟹ x = 1.

**Could not verify:**

- The pre-2000 "case of a field" for the motivic-to-K-theory spectral sequence. He says it was
  "originally written down, I think, in the case of a field earlier on" and names nobody. I did
  not supply a name.
- The identifications of "arpon and Allen" and "Sasha and Vadim" in the March 2025 recording.
  Omitted entirely rather than guessed.
- "Bachman Berkland and Jew" and their "stable homotopy category of 𝔽₁" (March 2025 only).
  Omitted.

**Gaps marked in place, with impact:**

1. **The Künneth formula for syntomic cohomology (§4.2). Moderate — the worst in the talk.** He
   says "there is a formula written here"; the slide is gone. The shape survives (motives tensor,
   therefore a Künneth formula exists in F-gauge language) and the shape is what the argument
   uses, but this is the single concrete payoff he offers for introducing F-gauges and I cannot
   show it.
2. **The relative construction of SH_prism(R) (§4.10). Moderate.** "There's a definition that you
   can write down that has all of the expected properties" is the entire content, in both
   recordings. It is the only unconditional mathematics in the last third of the talk. Recoverable
   only from arXiv:2507.13471.
3. **The construction of MU_prism from Grassmannians (§4.7). Low**, and declined by the speaker
   himself: "the details of the construction are not the thing to focus on."
4. **The Tor correction in the K-theory Künneth formula (§4.1). Low.** Nothing downstream uses it.
5. **The precise Clausen–Mathew–Morrow statement (§4.1). Low as used.** I quote his phrasing
   rather than sharpening it, because the published statements carry hypotheses the captions do
   not carry and I will not manufacture them.

**Three things I declined to teach**, following the precedent set in
`summaries/langlands-function-fields-gaitsgory.md`: **cyclotomic spectra**, **prismatic
F-gauges**, and the **higher-categorical substrate** of everything here. The first two he declined
himself, from the podium, and I have given each exactly what he gave: two structural facts, the
motivation, and the consequence. The third he never raised, and §2.4 explains why I did not
import it. All three are genuinely not learnable in a tutorial, and a smooth account would be the
kind of fabrication you could not detect from the inside.

**Length note.** Shorter than the Gaitsgory tutorial and comparable to the others. There is less
to rebuild here because the talk has one conjecture, one acceptance test and one piece of
evidence, rather than seven numbered conjectures across two settings. I did not truncate the
walkthrough; there was less walkthrough.
