---
title: "Maestro Jean-Pierre Serre"
speaker: Peter Sarnak (Princeton University / Institute for Advanced Study)
source: https://www.youtube.com/watch?v=NK7R4Nnz2mg
video_id: NK7R4Nnz2mg
channel: Simons Foundation
event: ICM 2026 Plenary Lecture (special lecture)
date: 2026-08-17
paper: none — companion for the final third: https://arxiv.org/abs/1807.11700 (Serre's own Bourbaki exposé 1146)
transcript: ../transcripts/NK7R4Nnz2mg_transcript.txt
difficulty_for_you: 5/5 (the survey) — 2/5 (the final third)
reading_time: ~75 min
---

# Maestro Jean-Pierre Serre — Peter Sarnak

**Field:** not Sarnak's. This is a tribute lecture. Sarnak spends the hour surveying
**Jean-Pierre Serre's** work, from the 1951 thesis to a paper Serre published last year,
ahead of Serre's hundredth birthday on **15 September 2026**. Sarnak's own subjects —
arithmetic quantum chaos, the Selberg trace formula, spectral gaps, thin groups — appear
exactly twice, both times as footnotes to something of Serre's.

**Difficulty against your background: 5 out of 5 for most of it, 2 out of 5 for the last
twenty minutes.** That split is real and it is the reason this tutorial is worth reading.
Nine tenths of the lecture is algebraic topology, algebraic geometry, Galois
representations and modular forms — every one of them on your "do not have" list, stacked
several layers deep. The final third is **classical potential theory**: transfinite
diameter, logarithmic capacity, equilibrium measures, energy integrals. That is
two-dimensional electrostatics. You own it completely.

So this document does two different jobs, and says which one it is doing at every point.

**How I adapted the template, and why.** The spec assumes a talk with one theorem, one
anchor, and one bridge. A tribute lecture has none of those. It has seventy-five years of
one person's work, sampled. I kept every section of the spec but re-pointed three of them:

- *Your anchor* covers only the final third, because that is the only part of the talk with
  an honest anchor. I say so there rather than inflating a fake one.
- *The bridge* is deliberately partial. I teach the objects that can be taught by
  deforming something you own, and I **decline to teach** three others — spectral
  sequences, coherent sheaf cohomology, and Galois cohomology in degree 1 — presenting
  each as a fact with its motivation and its consequence. Faking depth there would be
  worse than the hole.
- *The one argument* is Serre's capacity argument, in full, with the proof. It is the one
  piece of mathematics in this lecture you can follow line by line, and it is beautiful.

**Prerequisites this tutorial builds:** what a Galois representation is and why "odd" is
the whole story; what the congruence subgroup property asks; logarithmic capacity in its
three equivalent forms and its identity with electrostatics; what a resultant is and why
its integrality is the engine of the final argument.

**A note on sources.**

- **No ICM 2026 proceedings paper exists.** I checked the arXiv author listing for Sarnak
  directly (39 entries, most recent March 2026); there is nothing resembling a proceedings
  contribution, and a tribute lecture would not normally produce one.
- **The lecture title** is not on the YouTube page, which reads only "ICM 2026 Plenary
  Lecture - Peter Sarnak". "Maestro Jean-Pierre Serre" comes from Nicholas Katz's spoken
  introduction, and Sarnak repeats it. I have used it.
- **The companion for the final third is Serre's own writing**, not Sarnak's:
  [arXiv:1807.11700](https://arxiv.org/abs/1807.11700), *Distribution asymptotique des
  valeurs propres des endomorphismes de Frobenius [d'après Abel, Chebyshev, Robinson,
  ...]*, Séminaire Bourbaki exposé 1146, delivered 31 March 2018, 42 pages, in French.
  This is the exact document Sarnak reports on in the last twenty minutes. Every
  definition, theorem number and constant in §5.11 and §6 below is restored from it. **It
  is a companion, not the proceedings paper**, and it is by the subject of the lecture
  rather than the speaker.
- **Primary literature restores three more results**: Gamburd–Ghosh–Sarnak–Whang
  ([arXiv:2603.05849](https://arxiv.org/abs/2603.05849)) for the conics theorem, Alexander
  Smith ([arXiv:2111.12660](https://arxiv.org/abs/2111.12660), *Annals* 200 (2024) 71–122)
  and Orloski–Sardari–Smith ([arXiv:2401.03252](https://arxiv.org/abs/2401.03252)) for the
  trace problem. These are cited inline and are visibly distinct from the companion.
- **Everything else comes from the auto-captions alone.** Sarnak works from slides and
  writes on a board. The captions carry no formula and destroy nearly every proper noun in
  the lecture — "Sarah" for Serre, "Vy" for Weil, "growth and dick" for Grothendieck. The
  correction table is in §11. Where a statement was on the slide and not in the audio, I
  mark the gap rather than guessing.

---

## 1. What is at stake

Sarnak opens by conceding that the task is impossible. "It is impossible to give a fitting
account of the broad prolific contributions that Serre has made in one hour in a lecture
like this." What he offers instead is a **sampling** — roughly one item each from Serre's
theorems, his theories, his books, his Bourbaki reports, his conjectures, and his letters.

That structure is the point, and it is what makes the lecture more than an obituary in
advance. The question the hour actually asks is:

> How does one person produce load-bearing mathematics in algebraic topology, algebraic
> geometry, group theory, number theory, and potential theory — across seventy-five
> years — and have the work in each field still be the thing everyone builds on?

Sarnak's answer, stated in one line early and then demonstrated eleven times, is a
description of taste:

> "Serre's taste is one of very concrete problems, but to develop theories to solve those
> concrete problems."

Not theory for its own sake, and not problem-solving without theory. A concrete question
first — *are the homotopy groups of spheres finite?*, *does every finite-index subgroup of
SL₂(ℤ) come from a congruence?*, *how far can the Galois group of an elliptic curve fail to
be everything?* — and then whatever machinery the question turns out to need, built to last.

There is a second thread, quieter, about how Serre works on other people's mathematics.
It runs through the letters, the Bourbaki reports, and the books, and it is the part of
this lecture that is directly about your working life. I have pulled it out into §8.

Sarnak is South African, and opens with rugby: search for "Serre rugby" and you find
**Paul Serre** (1895–1972), a France international wing and centre, who was Jean-Pierre
Serre's uncle and, Sarnak says, a big influence on him. **Denis Serre**, who works on
nonlinear PDE at ENS Lyon, is Jean-Pierre's nephew. Both facts check out.

---

## 2. Your anchor — and an honest statement of where it does not reach

**For the first two thirds of this lecture you have no anchor, and I am not going to
manufacture one.**

The obvious temptation is to reach for the bridge the spec itself names — arithmetic
quantum chaos, where the Selberg trace formula plays the structural role of the Gutzwiller
trace formula from physics. That is a genuine correspondence, it is Sarnak's own field,
and **the talk never goes near it**. Sarnak mentions his own work exactly twice: once for
a conics theorem (§5.10) and once, in a single clause, to note that Eskin–Oh's homogeneous
dynamics went into it. Decorating this lecture with the trace formula would be putting
someone else's picture on the wall.

What you should do instead with §5.1 to §5.9 is read them the way you would read a good
history of a field you do not work in: for the shape of the questions and the mechanism
of the answers, not for technique you can carry away. I have written those sections to be
readable in exactly that mode, and I flag the places where the technique is genuinely
beyond a tutorial.

### The anchor that is real: capacity is electrostatics

The last twenty minutes are a different matter entirely, and here the anchor is exact
rather than analogical.

Sarnak's final Bourbaki report is Serre's 2018 exposé on **Galois orbits of algebraic
integers**. The central object is the **transfinite diameter**, also called the
**logarithmic capacity**, of a compact set $K \subset \mathbb{C}$. Serre gives three
equivalent definitions in his Appendix A. Here is the third one:

$$I(\mu) \;=\; \iint_{K \times K} \log|x - y| \, d\mu(x)\, d\mu(y), \qquad
\operatorname{cap}(K) \;=\; e^{\,v(K)}, \quad v(K) = \sup_{\mu} I(\mu),$$

the supremum over positive measures of mass 1 supported in $K$.

You have seen this. In two-dimensional electrostatics the potential of a unit line charge
is $-\log r$. So $-I(\mu)$ is exactly the **electrostatic energy** of a unit charge spread
on $K$ with density $\mu$, and the maximiser $\mu_K$ — Serre's **equilibrium measure** —
is exactly the **equilibrium charge distribution on a conductor**: the arrangement that
minimises energy. The Robin constant $\gamma = -v(K)$ is the self-energy, and
$\operatorname{cap}(K) = e^{-\gamma}$ is the logarithmic capacitance.

The dictionary is not partial. Every fact in Serre's appendix is a fact you can state
physically:

| Serre's statement | Your statement |
|---|---|
| $\mu_K$ is the unique measure attaining $\sup_\mu I(\mu)$ | charge settles into the unique minimum-energy configuration |
| $\operatorname{cap}$ of a disc equals $\operatorname{cap}$ of its bounding circle | charge on a conductor lives on the surface |
| $\operatorname{cap}(\lambda K) = |\lambda| \operatorname{cap}(K)$ | capacitance scales linearly with size |
| $\operatorname{cap}([-2,2]) = 1$, equilibrium measure $\tfrac{1}{\pi}\tfrac{dx}{\sqrt{4-x^2}}$ | the arcsine law — charge piles up at the ends of a strip |
| $\operatorname{cap}(f^{-1}K) = \operatorname{cap}(K)^{1/d}$ for monic $f$ of degree $d$ | a conformal-map rule for capacitance |
| $\operatorname{cap}(K) \geq \operatorname{mes}(K)/4$ for $K \subset \mathbb{R}$ | a set of zero length can still hold charge |

The Fekete points in Serre's first definition — the $n$ points of $K$ maximising
$\prod_{i \neq j} |x_i - x_j|$ — are precisely the equilibrium positions of $n$ repelling
point charges confined to $K$. That is a problem you have solved numerically.

**Why this matters for reading the talk.** The last third of the lecture is a genuine
theorem of Serre's about abelian varieties over finite fields, and its entire mechanism
is potential theory. You do not need to understand abelian varieties to understand the
mechanism. You need to understand that a polynomial with integer coefficients cannot have
all its roots crammed into a set that is too small to hold charge — and *that* is a
sentence about capacitors.

---

## 3. The bridge: four things, and three refusals

### 3.1 A Galois representation, and why "odd" is the whole story

This appears in §5.5, §5.6, §5.7 and §5.8, so it is worth the paragraph.

Take a polynomial with rational coefficients, say $x^3 - 2$. Its roots are
$\sqrt[3]{2}, \omega\sqrt[3]{2}, \omega^2\sqrt[3]{2}$. The **Galois group** is the group of
symmetries of the set of roots that respect every algebraic relation among them. It is a
finite group. Now let it act on all algebraic numbers at once: $G_{\mathbb{Q}} =
\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$, an infinite compact group.

A **Galois representation** is a homomorphism $\rho: G_{\mathbb{Q}} \to \operatorname{GL}_2(A)$
for some ring $A$ — complex matrices, or matrices over $\mathbb{Z}/n\mathbb{Z}$, or over a
finite field. That is all. It is the same move as representing a symmetry group by
matrices in quantum mechanics, and it is made for the same reason: the abstract group is
unmanageable, and matrices are not.

Two pieces of data attach to such a $\rho$ and you need both.

**Frobenius.** For each prime $p$ not dividing the "level", there is a distinguished
conjugacy class $\operatorname{Frob}_p \subset G_{\mathbb{Q}}$ — morally, "raising to the
$p$-th power". Its image $\rho(\operatorname{Frob}_p)$ is a conjugacy class of matrices, so
its **trace** and **determinant** are well-defined numbers. Those numbers are the
representation's observable spectrum, one number per prime.

**Oddness.** Complex conjugation $c$ is an element of $G_{\mathbb{Q}}$ of order 2, so
$\rho(c)$ is a $2 \times 2$ matrix squaring to the identity, and $\det \rho(c) = \pm 1$.
Call $\rho$ **odd** if $\det \rho(c) = -1$ and **even** if $\det \rho(c) = +1$.

That single sign controls everything in §5.6 to §5.8. Odd representations come from
**holomorphic** modular forms and are now essentially understood. Even representations —
"half the guys in the world", as Sarnak puts it — are expected to come from **Maass
forms**, and are essentially not understood at all. §5.8 explains why the sign matters so
much, and the reason is one you will recognise instantly from PDE.

### 3.2 The congruence subgroup property, in plain terms

$\operatorname{SL}_n(\mathbb{Z})$ is the group of $n \times n$ integer matrices of
determinant 1. For each $N$, reducing entries mod $N$ gives a homomorphism onto
$\operatorname{SL}_n(\mathbb{Z}/N\mathbb{Z})$; its kernel $\Gamma(N)$ is the **principal
congruence subgroup of level $N$**. Any subgroup containing some $\Gamma(N)$ is called a
**congruence subgroup**.

Congruence subgroups are the ones number theory hands you, because they are defined by
arithmetic conditions on the entries. But a group also has finite-index subgroups for
purely group-theoretic reasons. The question is whether those two supplies coincide.

> **Congruence subgroup property (CSP):** is every finite-index subgroup a congruence
> subgroup?

For $n \geq 3$ the answer is yes, and it is a theorem. For $n = 2$ the answer is
emphatically no, and the reason is one line of group theory (§5.4). This is one of the
cleanest "the small case is the hard case" phenomena in mathematics.

### 3.3 Logarithmic capacity, properly

Serre's Appendix A gives three definitions and states that they agree — a theorem of
Fekete (1923) and Szegő (1924). All three are worth having in your head because the
argument in §6 uses two of them and the exercises in §7 use the third.

**A.1 — transfinite diameter.** For $n > 1$,
$$d_n(K) \;=\; \sup_{x_1, \ldots, x_n \in K} \Big( \prod_{i \neq j} |x_i - x_j| \Big)^{1/(n(n-1))}.$$
Note $d_2(K)$ is the ordinary diameter. The sequence $d_n$ is non-increasing, and
$\operatorname{cap}(K) = \lim_{n \to \infty} d_n(K)$.

**A.2 — Chebyshev constant.** Let $T_n$ be the monic degree-$n$ complex polynomial
minimising $\|P\|_K = \sup_K |P|$. Then
$$\operatorname{cap}(K) \;=\; \lim_{n \to \infty} \|T_n\|_K^{1/n}.$$
This is the definition you already use, under the name "the Chebyshev problem".

*[Erratum in the companion: Serre's displayed equation (A.2.1) writes $\operatorname{cap}(K)
= \inf_n c_n(K)^{1/n} = \lim c_n(K)^{1/n}$ having already defined $c_n(K) = \inf_P
\|P\|_K^{1/n}$. The exponent $1/n$ is applied twice. It happens not to change the answer for
his worked example $K = [-2,2]$, but it does in general: for the circle of radius $r$ the
correct value is $r$ and the doubled exponent gives 1. The intended statement is
$\operatorname{cap}(K) = \lim_n c_n(K)$, i.e. the display above.]*

**A.3 — energy.** As in §2: $\operatorname{cap}(K) = e^{v(K)}$ with
$v(K) = \sup_\mu \iint \log|x-y| \,d\mu\,d\mu$.

Three numbers you should memorise, all in Serre's appendix:

- circle or disc of radius $r$: $\operatorname{cap} = r$;
- interval of length $\ell$: $\operatorname{cap} = \ell/4$ (so $[-2,2]$ has capacity exactly 1);
- $[-b,-a] \cup [a,b]$: $\operatorname{cap} = \tfrac{1}{2}\sqrt{b^2 - a^2}$.

### 3.4 The resultant, and why it is an integer

Given two polynomials $P, Q$ with $P$ monic of degree $d$ and roots $z_1, \ldots, z_d$,
the **resultant** is
$$\operatorname{Res}(P, Q) \;=\; \prod_{i=1}^{d} Q(z_i).$$
It is a polynomial expression in the coefficients of $P$ and $Q$ with integer
coefficients — it is a determinant of the Sylvester matrix — so **if $P$ and $Q$ have
integer coefficients then $\operatorname{Res}(P,Q)$ is an integer**. It vanishes exactly
when $P$ and $Q$ share a root.

That sentence is the entire engine of §6. Hold on to it.

### 3.5 Three things I am not going to teach you

Following the spec's own instruction that some things cannot be taught in a tutorial:

**Spectral sequences.** Serre's thesis invented a spectral sequence for fibrations and
used it to compute homotopy groups of spheres. A spectral sequence is a bookkeeping
device for a filtered computation that converges in stages, each page correcting the last.
Explaining it properly needs homological algebra you do not have, and explaining it
improperly would give you a false feeling of understanding. **Fact, motivation,
consequence:** it computes the cohomology of a fibre bundle from the cohomology of the
base and the fibre; Serre built it because he wanted a specific number; the consequence is
in §5.1 and is completely comprehensible without the machine.

**Coherent sheaf cohomology and GAGA.** Same treatment in §5.2. I will tell you exactly
what GAGA asserts and exactly what it buys, and I will not try to build sheaves.

**Galois cohomology $H^1(K, G)$.** Same treatment in §5.9. I will tell you what its
elements *are* — they classify a family of geometric objects — and what vanishing means.
I will not construct the cohomology.

---

## 4. Reading map

The eleven items Sarnak samples, with what each one costs you:

| § | Item | Year | Cost to you |
|---|---|---|---|
| 5.1 | Spectral sequence, homotopy groups of spheres | 1951 | read for shape |
| 5.2 | FAC and GAGA | 1955–56 | read for shape |
| 5.3 | Serre and Weil | 1950s–60s | free, and funny |
| 5.4 | Congruence subgroup property | 1964–70 | followable |
| 5.5 | Open image theorem | 1972 | followable |
| 5.6 | Deligne–Serre, weight-one forms | 1974 | read for shape |
| 5.7 | Serre's modularity conjecture | 1987 | read for shape |
| 5.8 | The even case, and Maass forms | open | **followable, and it is a PDE story** |
| 5.9 | Galois cohomology, Conjectures I and II | 1962 | read for shape |
| 5.10 | Density of conics with a rational point | 1990 → 2026 | followable |
| 5.11 | Galois orbits of algebraic integers | 2018 → now | **yours** |
| 5.12 | The quaquaversal group and quantum gates | 2009 | **yours** |

---

## 5. The talk, rebuilt

### 5.1 Coming out of the blocks: 1951

Nicholas Katz introduces Sarnak; Sarnak begins with Serre as a student in 1949.

Serre won the Fields Medal in 1954, at 27. Sarnak notes, correctly, that the record has
just survived another cycle: **Serre is still the youngest Fields medallist to date.**
Hermann Weyl's laudation at the 1954 Amsterdam congress — 72 years before this lecture —
said of him: *"Never before have I witnessed such a brilliant ascension of a star in the
mathematical sky as yours."*

The work was in algebraic topology. Leray had invented spectral sequences; Serre built one
adapted to **fibrations**, giving a calculus for the homology and cohomology of a fibre
space in terms of the base, the fibre, and the projection. Sarnak is candid that this is
not his area — "it's not things that I'm that familiar with" — and moves quickly to the
application.

The application is the **homotopy groups of spheres**, $\pi_i(S^n)$: the set of continuous
maps $S^i \to S^n$ up to continuous deformation, which is a group, and abelian for
$i \geq 2$. Serre proved:

> $\pi_i(S^n)$ is **finitely generated** for all $i$, and determined exactly which are
> finite. The rank is 1 in precisely two situations — $i = n$ (where the group is
> $\mathbb{Z}$, detected by the degree of the map) and $i = 4m-1$, $n = 2m$. Every other
> $\pi_i(S^n)$ with $i > n$ is **finite**.

The smallest case of the second family is $m = 1$: $\pi_3(S^2) = \mathbb{Z}$, generated by
the **Hopf fibration**. The higher cases are generalised Hopf fibrations. Serre also gave
detailed information on the $p$-primary components, though not the full finite abelian
group.

Sarnak's postscript is the best moment in the section. He points at the ICM 2022 lecture
of **Guozhen Wang and Zhouli Xu**, *Stable homotopy groups of spheres and motivic homotopy
theory*, and pulls out one consequence. Milnor showed $S^7$ carries exotic smooth
structures — more than one way to be a smooth 7-sphere. What has emerged since is that
among **odd-dimensional** spheres, the ones with a *unique* smooth structure are exactly
$S^1$, $S^3$, $S^5$ and **$S^{61}$**. That is the complete list. Sarnak calls it "just
quite incredible", and it is. The even-dimensional case remains open.

### 5.2 FAC and GAGA: 1955 and 1956

Two papers Sarnak says "changed the direction of algebraic geometry". Everyone calls them
by abbreviations of their French titles: **FAC** (*Faisceaux algébriques cohérents*, 1955)
and **GAGA** (*Géométrie algébrique et géométrie analytique*, 1956).

The setting. Sheaf cohomology had been developed by Leray, Henri Cartan — Serre's
advisor — and Serre, with earlier contributions from Oka. The word **coherent** imposes a
finiteness condition that makes the theory computable. Cartan and Serre had the theory for
complex analytic spaces.

FAC does the same thing **algebraically**, over any algebraically closed field, with no
analysis available. That is the foundational move.

GAGA is then the comparison theorem, and it is decisive. Take a projective variety
$X \subset \mathbb{P}^n(\mathbb{C})$ defined by polynomial equations. You now have two
cohomology theories on it — the analytic one and the algebraic one. **They coincide**, and
Serre gives the full description of the equivalence.

Sarnak highlights two consequences.

**Chow's theorem, reproved.** Every compact complex submanifold of projective space is
already algebraic. Sarnak makes the remark that a physicist will appreciate: an
analysis-to-algebra theorem must have analysis hidden somewhere, and here it is buried in
the Cartan–Serre work, in a compact operator descending from Schwartz, and in Cartan's
Theorems A and B on affine space.

**Weil's question about conjugate varieties.** Take $X$ defined over a number field $K$
and apply a Galois automorphism $\sigma$ to the coefficients of its defining polynomials.
You get a new variety $X^\sigma$. Weil asked: do $X$ and $X^\sigma$ have the same **Betti
numbers**? By GAGA the answer is yes — and in fact the same Hodge numbers. Weil cared
because the Weil conjectures tie the arithmetic of a variety over a finite field to the
topology of its complex points, so those Betti numbers had better be well defined.

And then the sting: $X$ and $X^\sigma$ need **not** be homeomorphic. Serre gave the first
examples, with different fundamental groups. Same Betti numbers, different topology.

Sarnak notes that this line is alive in the room. The Bakker–Brunebarbe–Tsimerman
**o-minimal GAGA**, and a conjecture of Griffiths, came up several times at this congress —
the same move of proving something analytic is secretly algebraic, in a new setting.

### 5.3 Serre and Weil

Serre's first exposure to serious mathematics was Weil lecturing in Paris in the late
1940s on his proof of the Riemann hypothesis for curves over finite fields. Sarnak's
version: "he didn't know what the guy was talking about, but he just understood, this is
really something I want to get involved in." He did.

When Serre visited Princeton in the late 1950s and 1960s, Weil was there, and Serre calls
him his mentor. Sarnak shows a photograph — Serre second from left, Weil on the right,
Serre "looking at Weil aggressively", with **Taniyama** and **Tamagawa** also in frame.

Three vignettes, all of which check out:

**The acknowledgement.** In *Algebras with involutions and the classical groups* (J. Indian
Math. Soc. 24, 1960), Weil writes that he is greatly indebted for the main idea of Part I
to "Mr. P. Serre, the famous winner of many cocycle races." A cyclo-cross joke about
Galois cohomology.

**The tease.** When Weil thought Serre had proved something false, he would say: "Ah, so
you think you've proved the Riemann hypothesis" — the point being that a false statement
implies everything, including the Riemann hypothesis. He deployed it on Serre's
counterexample to lifting: is every smooth projective variety in characteristic $p$ the
reduction of one in characteristic 0? Serre produced a counterexample. Weil was sure it was
false. It was correct.

**The propagandist.** On the Weil conjectures themselves — the higher-dimensional Riemann
hypothesis for smooth projective varieties over finite fields — Serre says he acted "simply
as a propagandist", particularly towards **Grothendieck**, whose cohomology theory made the
resolution possible. Sarnak points at the 294-page 2001 volume of the Grothendieck–Serre
correspondence and recommends reading it: "you will see how profoundly they impact each
other."

Then the thread that becomes §8 of this tutorial:

> "Serre writes many letters. I've got many letters from him and I'm sure many people here
> have too. And he demands the same quality of writing from you as he demands of himself.
> So he will always find errors and corrections and want you to improve it. And there are
> many people who know very well that their papers have improved dramatically after getting
> a letter from Serre. In the old days he would write to anybody who was writing anything
> interesting that he saw — handwritten."

### 5.4 The congruence subgroup property

Now the lecture becomes concrete, and you can follow it.

Start with the **modular group** $\operatorname{SL}_2(\mathbb{Z})$, which Sarnak calls
"the mother of all arithmetic groups". As an abstract group there is a clean answer,
easy to prove and known to Fricke and Klein:
$$\operatorname{SL}_2(\mathbb{Z})/\{\pm I\} \;\cong\; \mathbb{Z}/2 * \mathbb{Z}/3,$$
the **free product** of a group of order 2 and a group of order 3.

A free product is an enormously floppy object. Counting its finite-index subgroups against
the supply of congruence subgroups shows immediately that **most finite-index subgroups of
$\operatorname{SL}_2(\mathbb{Z})$ are not congruence subgroups.** So the answer for $n=2$ is
no, and it is no for a soft reason.

Which is why it was "quite a shock" when, simultaneously and independently,
**Bass–Lazard–Serre** and **Mennicke** proved:

> For $n \geq 3$, **every** finite-index subgroup of $\operatorname{SL}_n(\mathbb{Z})$ is a
> congruence subgroup.

Sarnak sketches the Bass–Lazard–Serre mechanism, and it is a nice piece of soft topology.
Put two topologies on $\Gamma = \operatorname{SL}_n(\mathbb{Z})$: one with all finite-index
subgroups as a basis of neighbourhoods of the identity, one with only the congruence
subgroups. Complete in each. You get the **profinite completion** $\hat{\Gamma}$ and the
**congruence completion** $\overline{\Gamma}$. The congruence topology is coarser, so there
is a continuous surjection $\hat{\Gamma} \to \overline{\Gamma}$. Its kernel $C$ is the
**congruence kernel**, and

$$\text{CSP holds} \iff C \text{ is trivial}.$$

They compute $C$ using cohomology with coefficients — this is where Lazard enters, via
$\operatorname{SL}_2(\mathbb{Z}_p)$, the $p$-adic integers — and show it is trivial.

The reframing is the real prize, and Sarnak says so explicitly: once you ask not "does CSP
hold?" but "**what is $C$?**", you can pose the problem for any arithmetic group over any
ring, and the trichotomy *trivial / finite / infinite* organises everything. Infinite
means CSP fails. Finite means you understand the failure completely.

**Bass–Milnor–Serre** (1967) then solved it in general over rings of $S$-integers, for
$\operatorname{SL}_n$ with $n \geq 3$ and for $\operatorname{Sp}_{2n}$.

That left $\operatorname{SL}_2$, and Serre settled it himself in a paper Sarnak calls
beautiful. Instead of $\operatorname{SL}_2(\mathbb{Z})$, work with
$\operatorname{SL}_2(R)$ where $R$ is a ring of $S$-integers — you are allowed to invert
some primes, or work in a quadratic extension. Serre computes the congruence kernel
completely:

> $C$ is **finite if and only if the group of units $R^\times$ is infinite.**

That is a clean statement resting on Dirichlet's unit theorem, and by Sarnak's account
the proof is anything but clean — the "if and only if" needs a great deal of topology,
including hyperbolic 3-manifolds. A structural ingredient throughout, in Serre's proof
and the earlier ones, is the presence of **unipotent elements** in the group.

**The open challenge.** Sarnak addresses this one to the young people in the room, and it
is the simplest unsolved case. Take the Hamilton quaternions $H$. Look at $H^*(R)$:
quaternions with coordinates in $R$ whose inverses also have coordinates in $R$. Over
$\mathbb{Z}$ this is a finite group. Invert **one** prime and the group acts on a tree —
and Bass–Serre theory of groups acting on trees lets you read off the structure and show
CSP **fails**. Invert **two or more** primes and Serre conjectures CSP **holds**. That is
wide open.

Sarnak also mentions a broader Serre conjecture on when CSP should hold, "almost completely
solved", with progress by Kneser, Raghunathan, Prasad, Platonov and Rapinchuk.

### 5.5 The open image theorem, 1972

Serre's interest in modular forms began in 1953 and has not stopped: his most recent papers,
from last year, are still about modular forms. Sarnak quotes Serre on why: the subject's
"most attractive statements want, and prove, to be true."

The 1972 paper — dedicated to André Weil, and among Serre's most cited — quantifies a
principle Sarnak states as a slogan: **Galois groups want to be big.**

Setup. Let $E$ be an elliptic curve over $\mathbb{Q}$. Its $n$-torsion points $E[n]$, with
coordinates in $\overline{\mathbb{Q}}$, form a group isomorphic to
$(\mathbb{Z}/n\mathbb{Z})^2$. The Galois group $G_{\mathbb{Q}}$ permutes them, respecting
the group structure, so you get
$$\rho_{E,n}: G_{\mathbb{Q}} \longrightarrow \operatorname{GL}_2(\mathbb{Z}/n\mathbb{Z}).$$
The question is how big the image is.

There is a class of curves where it is genuinely small: those with **complex
multiplication**, meaning the lattice defining $E$ over $\mathbb{C}$ is preserved by
multiplication by some non-real number. These are special and well understood.

> **Open image theorem.** If $E/\mathbb{Q}$ does **not** have complex multiplication, then
> the index $[\operatorname{GL}_2(\mathbb{Z}/n\mathbb{Z}) : \operatorname{im} \rho_{E,n}]$
> is bounded by a constant **independent of $n$**, depending only on $E$.

*(Sarnak misspeaks here and corrects himself aloud: "independent of $E$, independent of
$n$ — but depending on $E$, my apologies." The correct statement is the one above.)*

Equivalently: the image in $\operatorname{GL}_2(\hat{\mathbb{Z}})$ is **open**. The typical
elliptic curve has as much Galois symmetry as it could possibly have, up to bounded error.

Sarnak then poses the natural sharpening, which is Serre's uniformity question: can the
bound be made **independent of the curve**? Concretely, take $n = \ell$ a prime, so the
image sits in $\operatorname{GL}_2(\mathbb{F}_\ell)$. The largest prime for which any
non-CM $E/\mathbb{Q}$ is known to have non-surjective mod-$\ell$ representation is
$\ell = 37$. So: is surjectivity automatic for every $\ell > 37$? Work of **Bilu, Parent
and Rebolledo** makes good progress under some hypotheses.

Sarnak notes Faltings' theorem generalises the open image theorem to abelian varieties by a
different method.

### 5.6 Deligne–Serre: weight one, 1974

Here is the section where the captions and I part company most: the mathematics was on the
board. I state what is recoverable and mark the rest.

A **modular form of weight $k$** for a congruence subgroup $\Gamma'$ is a holomorphic
function $f$ on the upper half plane satisfying
$$f\!\left(\frac{az+b}{cz+d}\right) = (cz+d)^k f(z)$$
for all $\begin{psmallmatrix} a & b \\ c & d \end{psmallmatrix} \in \Gamma'$, plus growth
conditions at the cusps.

**Weight one is the mysterious case.** For weight $\geq 2$, Riemann–Roch computes the
dimension of the space of such forms. At weight one the index is exactly zero and
Riemann–Roch gives **nothing**. Sarnak enjoys the coincidence: Serre gave a new proof of
the classical Riemann–Roch theorem in FAC, so "we can call it the Riemann–Roch–Serre
theorem", and it is the one theorem that refuses to answer this question.

The right refinement is to work with the **Hecke congruence group** $\Gamma_0(N)$ —
matrices whose lower-left entry is divisible by $N$ — and to allow a **Dirichlet
character** $\varepsilon$ in the transformation law. Since $z \mapsto z+1$ is in the group,
$f$ has a Fourier expansion $f(z) = \sum_{n \geq 1} a_n q^n$; the theory of Hecke operators
makes the $a_n$ multiplicative; normalise $a_1 = 1$.

> **Deligne–Serre (1974, dedicated to André Weil).** Such an $f$ of weight one corresponds
> to an **odd, irreducible, two-dimensional complex Galois representation** $\rho$: there
> is a finite Galois extension $K/\mathbb{Q}$ and $\rho: \operatorname{Gal}(K/\mathbb{Q})
> \to \operatorname{GL}_2(\mathbb{C})$ with
> $$a_p = \operatorname{tr}\rho(\operatorname{Frob}_p), \qquad
> \varepsilon(p) = \det \rho(\operatorname{Frob}_p)$$
> for all $p$ outside the ramified set. Odd means $\det\rho(c) = -1$ for complex
> conjugation $c$.

The complexity of $\rho$ at the ramified primes is measured by the **Artin conductor**, an
invariant Artin introduced for exactly this purpose.

**The converse** — that every odd irreducible two-dimensional $\rho$ arises this way — is
equivalent to **Artin's conjecture**, that the Artin $L$-function $L(s, \rho)$ is entire
for irreducible $\rho$. Sarnak notes that Weil did not point this out but Langlands did:
it follows from Weil's converse-theorem arguments. It is the analogue of the
Shimura–Taniyama conjecture, with Galois representations in place of elliptic curves.

And here is a design observation Sarnak makes that is worth pulling out, because §8
returns to it:

> The converse theorem specifies **the exact level at which you will find the modular
> form**, because the level is the conductor. "It's very falsifiable, and the minute a
> conjecture is very falsifiable you can check it, and it's more likely when you check it
> that it's true — that you've put it through some kind of real test."

**How the proof starts.** One step is recoverable from the audio and it is the one you
should keep, because it is exactly what breaks in §5.8. The product of two holomorphic
functions is holomorphic, and the product of two modular forms is a modular form **of the
sum of the weights**. So take your weight-one $f$ and multiply it by an explicit
**Eisenstein series** whose coefficients you can control modulo $p$. You land in higher
weight, where a rich theory exists — Shimura, Grothendieck, Deligne — which constructs the
field $K$ and, by reduction mod a prime above $p$, produces a mod-$p$ Galois
representation $\bar\rho_f$ attached to any holomorphic form of level $N$ with $p \nmid N$.
Then you assemble.

> *[Gap: Sarnak writes the transformation law, the Fourier expansion, the Hecke
> multiplicativity relation and the conductor formula on the board. The captions carry no
> formula. I have restored the standard statements above from the literature; the specific
> normalisations Sarnak used are not recoverable. **Impact: low** — the shape of the
> correspondence carries the lecture and is stated.]*

**The knee-surgery story**, which Sarnak tells knowing that Deligne is in the room and that
Serre may not be watching. Around 1973, Serre had his first knee surgery. Lying in
hospital waiting for the anaesthetist, thinking about all the theorems he could prove,
he gets a call from Deligne. Serre talks. Deligne tries to get a word in. Eventually he
manages: *I've proved the Weil conjectures.* — *What? Really?* Deligne explains the idea:
take a Lefschetz pencil, use monodromy and high tensor powers to locate the zeros in a
family, and deduce the conjectures for each member individually. Ten minutes later the
anaesthetist arrives: *Are you ready, Mr Serre?* — "I'm completely relaxed and ready. I can
prove the Weil conjectures. Put me under."

Sarnak warns in advance that he will probably embellish it and that both parties may deny
it.

### 5.7 Serre's modularity conjecture, 1987

Serre studied **congruences between modular forms** — as you vary the level and the weight,
different forms become congruent modulo $p$ — and distilled the pattern into one very
sharp conjecture.

Setup. Let $\bar\rho: G_{\mathbb{Q}} \to \operatorname{GL}_2(\mathbb{F})$ with $\mathbb{F}$
a finite field of characteristic $p$, irreducible over $\overline{\mathbb{F}}$, and **odd**.
Serre attaches to it two numbers:

- $N(\bar\rho)$, the prime-to-$p$ part of the **Artin conductor** — the level;
- $k(\bar\rho)$, a **weight**, read off from the restriction of $\bar\rho$ to the inertia
  group at $p$ by an explicit recipe.

> **Serre's conjecture.** Every such $\bar\rho$ is the mod-$p$ reduction of a holomorphic
> modular form of level $N(\bar\rho)$ and weight $k(\bar\rho)$ — and $k(\bar\rho)$ is the
> **least** weight in which the congruence can be satisfied.

Note what makes it valuable: it does not say "some form exists somewhere". It names the
level and the weight, so you can search a finite space and be refuted. Sarnak repeats the
falsifiability point here.

The history Sarnak gives:

- Started in **1975**; the exact form required "a lot of adjustments" and a lot of
  computation, some done for Serre by Mestre; published **1987**.
- Refined further by **Edixhoven**, using **Nick Katz's** geometric definition of modular
  forms mod $p$ — not naive reduction mod $p$ but a cohomological one. *(Katz is the person
  who just introduced Sarnak.)*
- The conjecture **implies Fermat's Last Theorem** and **implies Artin's conjecture for
  odd two-dimensional Galois representations.**

And the proof chain, which Sarnak runs through quickly:

1. That a variant of Serre's conjecture implies Fermat is due to **Hellegouarch** and to
   the decisive insight of **Gerhard Frey** (the Frey curve).
2. **Ribet** proved the "epsilon" part of Serre's conjecture, reducing Fermat to the
   Shimura–Taniyama conjecture for elliptic curves.
3. **Wiles**, and **Taylor–Wiles**, introduced **modularity lifting** and established
   modularity of semistable elliptic curves — and with it, Fermat.
4. Those techniques then went far beyond their original purpose. Important contributions by
   **Kisin**, and then the complete solution of Serre's conjecture by **Khare and
   Wintenberger**.

Sarnak mentions running into Khare, who has written a book he calls beautiful and has
started reading: *Chasing a Conjecture*, an account of the proof with Wintenberger. It
exists — *Chasing a Conjecture: Inside the Mind of a Mathematician*, Juggernaut.

### 5.8 The even case: where algebraic geometry stops being friendly

**This is the section to read carefully, because the obstruction is a PDE fact.**

Everything above needed $\bar\rho$ **odd**. What about even — $\det\rho(c) = +1$? "Those
are half the guys in the world."

Sarnak: "then algebraic geometry seems not to be so friendly." The expectation is that an
even classical Artin representation corresponds not to a holomorphic form — not to a
solution of a first-order equation — but to a **Maass form**: a real-analytic
eigenfunction of the hyperbolic Laplacian on the modular surface, with eigenvalue exactly
$1/4$. Those eigenvalues are "outside a quarter", probably transcendental, and we know
much less about them. **The conjecture is not known in general and we do not know how to
approach it.**

Now the reason, and Sarnak states it in one sentence:

> "If you take the product of two holomorphic functions, it's holomorphic. But if you take
> a product of two [Maass] functions, it's not anything particularly friendly. And that
> does make a big difference. For example, the Deligne–Serre argument doesn't start."

You should recognise this immediately. **Holomorphic modular forms form a graded ring;
Laplace eigenfunctions do not form a ring at all.** Multiply two eigenfunctions of
$\Delta$ with eigenvalues $\lambda_1, \lambda_2$ and you do not get an eigenfunction —
you get a function whose spectral decomposition spreads over the whole spectrum. That is
the same fact that makes nonlinear PDE hard and linear PDE easy. The entire Deligne–Serre
machine started with "multiply your weight-one form by an Eisenstein series". On the
Maass side there is nothing to multiply by.

What *is* known in the even case, via **Artin's conjecture** rather than modularity: take
the representation into $\operatorname{PGL}_2(\mathbb{C})$. Its finite subgroups are
classified — they are the symmetry groups of the classical solids: cyclic, dihedral,
tetrahedral, octahedral, icosahedral. All but the last are **solvable**. For solvable
image the conjecture is known, thanks to **Saito–Shintani** base change and, most
importantly, **Langlands**.

> The **icosahedral** case, the only non-solvable one, "is the one that is holding us up."

*(Sarnak names Saito–Shintani and Langlands, which covers the tetrahedral case. The
octahedral case is Tunnell's, building on Langlands. Sarnak did not say this; I add it.)*

### 5.9 Galois cohomology: Bourbaki 1995, on a 1962 conjecture

Serre was an early Bourbaki member and gave more than a dozen exposés, the first in
1949–50, as a **student**, on extensions of locally compact groups after Iwasawa and
Gleason. Sarnak's aside deserves quoting because it is a claim about scientific
communication:

> "Séminaire Bourbaki are absolutely the great things. We should really introduce them much
> more broadly. They really explain math properly."

A Bourbaki exposé is always a report on **someone else's** work. Sarnak picks two, and the
choice is deliberate: it shows Serre operating in the mode of a reader rather than an
author, and it shows that Serre's readings generate new mathematics.

The first, from 1995, reviews progress on Galois cohomology. Sarnak states the purpose in
one line you can hold onto:

> **Galois cohomology is a tool for proving Hasse principles.**

The model result is **Hasse–Minkowski**: a quadratic form has a nontrivial rational zero if
and only if it has one over $\mathbb{R}$ and over $\mathbb{Q}_p$ for every $p$. Local
solvability everywhere implies global solvability. "Those are the kind of theorems we
love."

The generalisation. Let $G$ be a connected linear algebraic group over a perfect field $K$,
acting on a variety. A **principal homogeneous space** (a torsor) is one where the
stabiliser over the algebraic closure is a single point — the variety looks like a copy of
$G$ that has forgotten where its identity element is. The set of these, up to isomorphism,
is exactly the cohomology set $H^1(K, G)$, and the **trivial class corresponds to having a
$K$-rational point**. So $H^1(K, G) = 1$ *is* a Hasse principle.

The **cohomological dimension** $\operatorname{cd}(K)$ is the smallest $n$ such that Galois
cohomology of $K$ in degrees above $n$ vanishes for all finite modules. Serre introduced it
(it also appears in work of Tate).

> **Conjecture I (Serre, 1962).** $H^1(K, G) = 1$ for every connected linear algebraic
> group $G$ $\iff$ $\operatorname{cd}(K) \leq 1$.
>
> **Conjecture II (Serre, 1962).** The same for every **simply connected** semisimple $G$,
> when $\operatorname{cd}(K) \leq 2$.

Status as Sarnak gives it:

- Conjecture I: solved by **Steinberg**, 1965, "in a beautiful paper", very soon after.
- Conjecture II: solved over number fields; a large literature. Breakthroughs by
  **Merkurjev and Suslin** (Sarnak says 1985), and a complete solution **for classical
  groups** by **Bayer-Fluckiger and Parimala**, 1995 — which is the result Serre's exposé is
  reporting on. Established for some exceptional groups; **open in general**.

### 5.10 The conics problem: Serre 1990, answered 2026

Sarnak's first of two appearances in his own lecture, and a clean statement.

A plane conic over $\mathbb{Q}$ is a ternary quadratic form — three variables, so **six
coefficients**. Sometimes it has a rational point and sometimes it does not, and by
Hasse–Minkowski you know exactly when: it needs a point everywhere locally. But there are
infinitely many primes to check, so the local-to-global criterion does not immediately give
you a **density**.

> **Serre's question (1990).** Order integral ternary quadratic forms by the size of their
> coefficients. What fraction of them are isotropic — that is, have a nontrivial rational
> zero?

Serre proved an upper bound with the large sieve; Hooley proved a matching lower bound of
the same order. The exact asymptotic resisted for 35 years.

Sarnak: "this was resolved recently by Gamburd, Ghosh, myself and Whang, and we used
homogeneous dynamics."

Restored from the paper — [Gamburd, Ghosh, Sarnak, Whang, *On indefinite integral ternary
quadratic forms*, arXiv:2603.05849](https://arxiv.org/abs/2603.05849), v1 6 March 2026,
v2 2 June 2026 — the theorem is:

> **Theorem 1.3.** $\operatorname{ISO}_{\mathrm{prim}}(X\Omega) \sim \varpi \cdot
> \operatorname{Vol}(\Omega^{\mathrm{iso}}) \cdot \dfrac{X^6}{\sqrt{\log X}}$ as
> $X \to \infty$, with $\varpi$ an explicit constant given by an Euler product of $p$-adic
> probabilities.

$X^6$ is the total count of forms in the dilated region — six coefficients — so the
**density of conics with a rational point decays like $1/\sqrt{\log X}$**. Vanishingly
slowly, but vanishing. The same paper also resolves a 1990 problem of Margulis on the
Markoff spectrum: $\operatorname{MAR}(X) \sim \gamma X \log X$ (Theorem 1.1).

What changed after 35 years is the method: **homogeneous dynamics and equidistribution
instead of sieves**. Sarnak notes that the work of **Eskin and Oh** goes into it — the same
Hee Oh whom he introduced earlier at this congress.

### 5.11 Galois orbits of algebraic integers: Bourbaki 2018, and now

**This is your section.** Sarnak flags the shift himself: "if you haven't followed what
I've said, I'm going to be much more elementary now — so listen." He is right, and the
laugh in the room is at the audience's expense as much as anyone's.

Everything from here is restored against Serre's own text, [Bourbaki exposé 1146,
arXiv:1807.11700](https://arxiv.org/abs/1807.11700).

#### The classical theorem

> **Fekete (1923).** Let $K \subset \mathbb{C}$ be compact. If $K$ contains infinitely many
> algebraic integers of growing degree all of whose conjugates also lie in $K$, then
> $\operatorname{cap}(K) \geq 1$.

Equivalently, in Serre's phrasing (his Corollary 1.2.10, citing Fekete's Satz XI): **if
$\operatorname{cap}(K) < 1$, there are only finitely many monic integer polynomials with
all roots in $K$.** A set that cannot hold charge cannot hold algebraic integers.

The converses:

> **Fekete–Szegő (1955).** If $K \subset \mathbb{C}$ is compact, conjugation-invariant, and
> $\operatorname{cap}(K) \geq 1$, then every **neighbourhood** $U$ of $K$ contains
> infinitely many algebraic integers totally in $U$.
>
> **Robinson (1964).** If $E \subset \mathbb{R}$ is a **finite union of closed intervals**
> with $\operatorname{cap}(E) > 1$, then there are infinitely many algebraic integers
> totally in $E$ — no neighbourhood fudge — and moreover their root measures converge to the
> equilibrium measure $\mu_E$ (Serre's Theorem 1.6.2).

Sarnak's version — "a converse due to Raphael Robinson if $K \subset \mathbb{R}$, and due to
Szegő in general" — is accurate in substance, and the difference between the two is exactly
the neighbourhood. Robinson's proof, which occupies Serre's entire §2, runs through
hyperelliptic curves, the **Pell–Abel equation**, and Chebyshev polynomials. Serre calls it
"very interesting for the different arguments it brings into play", and that is the source
of the exposé's subtitle, *d'après Abel, Chebyshev, Robinson*.

Serre also notes he had most of §1 twenty years earlier, lectured on it repeatedly, and
never published the proofs. The Bourbaki seminar was the occasion to fill the gap.

#### What Serre does with it: abelian varieties over a finite field

Now the arithmetic input, and this is the part you take on faith.

Fix a finite field $F$ with $q$ elements. To an abelian variety $A$ over $F$ attach $P_A$,
the **characteristic polynomial of its Frobenius endomorphism**. It is monic, of degree
$2\dim A$, with **integer coefficients**, and by Weil's theorem — the theorem whose lecture
started Serre's career — all its complex roots lie on the circle $C$ of radius
$\sqrt{q}$ centred at 0. Conversely, by **Honda–Tate theory**, essentially every such
polynomial comes from an abelian variety (Serre's Lemma 1.8.1: up to a power).

So: put a Dirac mass at each root, normalise to total mass 1, get a probability measure
$\mu_A$ on the circle. Let $A$ vary. **What are the possible limit measures?**

Sarnak first gives the contrast. If you restrict to **Jacobians of curves** with genus
growing, the zeros must become dense on the circle — a theorem of Tsfasman and Vlăduţ. The
answer is boring in the best way: essentially only measures supported on the whole circle,
with continuous density.

Allow **general abelian varieties** and the answer changes completely.

> **Serre, Theorem 1.7.8 with Proposition 1.8.2.** Let $E \subset C$ be closed and
> conjugation-invariant. $E$ is the support of a diffuse limit measure **if and only if**
> $E$ is *reduced* and
> $$\operatorname{cap}(E) \;\geq\; q^{1/4}.$$
> Moreover there are such $E$ of **Lebesgue measure zero**.

Sarnak states exactly this, including the number: "as long as the capacity of your subset of
the circle is bigger than $q$ to the quarter, then you can find a sequence of abelian
varieties whose zeros are stuck in those points... the capacity of the circle of radius
$\sqrt{q}$ is $\sqrt{q}$, and this new set can be $q$ to the quarter — much, much smaller,
quite a thin set."

**Where $q^{1/4}$ comes from, and you will like this.** Serre's §1.7 maps the circle to an
interval by $f(z) = z + \bar{z}$. On $|z| = r$ with $r^2 = q$, we have $\bar z = q/z$, so
$$f(z) \;=\; z + \frac{q}{z},$$
which is the **Joukowski transform**. It sends $C$ onto $I = [-2r, 2r]$. Serre's (1.7.3)
says capacity transforms as
$$\operatorname{cap}(E) \;=\; r^{1/2}\operatorname{cap}(E_I)^{1/2},$$
where $E_I = f(E)$. So the condition $\operatorname{cap}(E_I) \geq 1$ on the interval side —
Fekete's threshold — becomes $\operatorname{cap}(E) \geq r^{1/2} = q^{1/4}$ on the circle.
The exponent $1/4$ is a square root applied twice: once because the circle double-covers
the interval, once because capacity is a geometric mean.

**The Cantor set example** (Serre §1.6.5) is worth knowing. The triadic Cantor set $E$ has
capacity at least $1/9$; numerically it appears to be $0.22094\ldots$. It is *reduced*. So
scale it by $\lambda > 1/\operatorname{cap}(E)$, say $\lambda > 9$, and Serre's criterion
applies. You get a limit measure whose support has **Lebesgue measure zero** — the measure
and $dx$ are mutually singular. Frobenius eigenvalues can accumulate on a Cantor dust.

Sarnak adds the practical warning: "it's hard to compute capacities, by the way." He is
right, and the fact that the Cantor set's is only known numerically is the proof.

#### Serre's question, and the answer

Then the move that Sarnak calls "pulling a bunch of things out of just magic". Serre asks a
question about **general** compact $K$, not just circles.

Take algebraic integers of growing degree, all of whose conjugates lie in a fixed compact
$K$. Put a Dirac mass at each conjugate, normalise, take weak limits. **Which measures
arise?**

There is an obvious necessary condition, which Serre attributes to **Chris Smyth**, who
introduced this technique in 1984 for estimating traces of totally positive algebraic
integers:

$$\int \log|Q(x)| \, d\mu(x) \;\geq\; 0 \qquad \text{for every nonzero } Q \in \mathbb{Z}[X].$$

§6 proves this. Serre asks: **is it also sufficient?**

> Answered **yes**, by **Alexander Smith** when $K \subset \mathbb{R}$
> ([arXiv:2111.12660](https://arxiv.org/abs/2111.12660), *Annals of Mathematics* **200**
> (2024), 71–122), and by **Orloski and Sardari** for general $K$
> ([arXiv:2302.02872](https://arxiv.org/abs/2302.02872)).

That is a complete classification of the possible limit measures, in terms of a family of
linear inequalities. Sarnak notes that Serre asked precisely because he saw an application
coming.

#### The application: the Schur–Siegel–Smyth trace problem

The cleanest statement in the lecture, and one you can explain to anyone.

An algebraic integer is **totally positive** if all its conjugates are positive real
numbers. For such an $\alpha$ of degree $n$, form
$$\frac{\operatorname{tr}(\alpha)}{\deg(\alpha)} \;=\; \frac{\alpha_1 + \cdots + \alpha_n}{n},$$
the average of the conjugates. **What is $\liminf$ of this over all totally positive
algebraic integers?**

For about 70 years, the best explicit constructions gave the value **2**, and Siegel had
already written that down. Whether the true answer was below 2 was open, and it is the
kind of question where the barrier looks structural: the interval $[0,4]$ has capacity
exactly 1, and its equilibrium measure has mean 2.

Serre's insight was that if his conjecture on limit measures is true, you can construct
sequences pushing the $\liminf$ **below 2**. Smith proved the conjecture, and with it:

> **Smith (2024).** There are infinitely many totally positive algebraic integers $\alpha$
> with $\operatorname{tr}(\alpha) < 1.89831 \cdot \deg(\alpha)$.

And from the other side:

> **Orloski, Sardari and Smith** ([arXiv:2401.03252](https://arxiv.org/abs/2401.03252))
> improved the best lower bound to **1.80203**, by adding constraints to Smyth's linear
> programming method that reduce the number of variables and speed convergence — recovering
> Schur's bound in the simplest case and Siegel's in the second.

So the answer lies in $[1.80203,\ 1.89831]$ and the gap is now small. Sarnak: "you can see
they're quite close." And then, on Schur, Siegel, Smyth, Smith, Sardari — and himself:
"It seems this is a problem that if your surname starts with an S, it's for you."

### 5.12 The quaquaversal group, and your quantum computer

From Serre's *Œuvres* volume V, which appeared a few weeks before this lecture and covers
1998–2025: not a theorem or a conjecture but an **Oberwolfach report**.

Conway and Radin, studying aperiodic tilings of $\mathbb{R}^3$, produced a group generated
by **two rotations about perpendicular axes**. It had "all sorts of wonderful properties
and nobody understood why."

Serre's observation: pass to the simply connected double cover $\operatorname{SU}(2)$ — the
rotation group $\operatorname{SO}(3)$ is not simply connected — and the resulting group is
**$S$-arithmetic**. Subtle to see, and it "unmasks all the structure that people were
finding."

And the group you land on is the **Clifford+T group**. Sarnak, dryly: "if you ever buy a
quantum computer — which by the way doesn't do much right now, as far as I know — but if you
buy an IBM quantum computer and want to code something, you will have to code with these
universal gates called Clifford and T, which is the same group."

Verified: Serre, *Le groupe quaquaversal, vu comme groupe $S$-arithmétique*, Oberwolfach
Report **6** (2009), no. 2, 1421–1426. The quaquaversal group is generated by a rotation of
order 6 and a rotation of order 4 about perpendicular axes. The connection to quantum gate
synthesis is now a small industry, and Sarnak has his own paper in it —
Parzanchevski–Sarnak, *Super-Golden-Gates for PU(2)*
([arXiv:1704.02106](https://arxiv.org/abs/1704.02106)).

This is the lecture's clearest instance of the pattern Sarnak keeps naming: someone finds
a structure empirically, Serre identifies which classical object it actually is, and the
mystery evaporates.

### 5.13 The books, and the ending

"Each of Serre's twenty or more books is a masterpiece in exposition." Sarnak names the
range: *Corps Locaux* (**Local Fields**), 1962 first edition, 1968 second, his most cited
book; and the recent *Lectures on $N_X(p)$*, on how the number of points of a variety $X$
modulo $p$ varies with $p$ — the theme that runs back through zeta functions and the Weil
conjectures, now asking a fresh set of questions.

Milnor, reviewing Serre's collected works volumes I–III, wrote that Serre is one of the
masters of mathematical exposition: **in many cases the first account of a topic appears in
one of his papers and remains the best.** *(The captions render the reviewer's name
unclearly; Milnor is my reading and I flag it in §11.)* The book Sarnak singles out is
*Abelian $\ell$-adic Representations and Elliptic Curves*, "which many of us were brought up
on."

Some joint papers — notably with **Armand Borel** — appear in Borel's collected works rather
than Serre's five volumes. Sarnak's line on the two relationships: **Weil was Serre's
mathematical mentor and father; Borel was his older brother.** And it was Borel who
communicated Leray's work on spectral sequences to Serre — *after Serre had dropped out of
Leray's class.*

> "So for those who drop out of a class, you can still make it — and even in the topic that
> the lecture was famous for."

The close:

> "It is clear that Serre's star in the mathematical sky continues to shine bright.
> September 15th, 2026 will mark his hundredth birthday, and I believe I speak for all of us
> here, as well as mathematicians around the world, in thanking Serre for his profound and
> continued gifts in shaping modern mathematics."

---

## 6. The one argument: why integer polynomials cannot hide in a small set

The lecture has no single theorem. But it has one argument that is short, complete,
and entirely within your reach, and it is the engine of §5.11. Here it is in full, from
Serre's §1.3–1.4.

**Claim.** Let $\mu$ be a weak limit of root-counting measures of monic integer polynomials
whose roots all lie in a compact $K \subset \mathbb{C}$. If $\mu$ has no atoms, then
$$\operatorname{cap}(\operatorname{Supp}\mu) \;\geq\; 1.$$

### Step 1 — the resultant is an integer

Let $P \in \mathbb{Z}[X]$ be monic of degree $d$ with roots $z_1, \ldots, z_d$ (in $K$).
Write $\delta_P = \frac{1}{d}\sum_i \delta_{z_i}$ for its root measure. Let
$Q \in \mathbb{Z}[X]$ be nonzero. Then

$$\delta_P(\log|Q|) \;=\; \frac{1}{d}\sum_{i=1}^{d} \log|Q(z_i)|
\;=\; \frac{1}{d}\log\Big|\prod_{i=1}^{d} Q(z_i)\Big|
\;=\; \frac{1}{d}\log\big|\operatorname{Res}(P, Q)\big|.$$

The resultant is an **integer** (§3.4). Therefore it is either 0 — which happens exactly
when $P$ and $Q$ share a root — or its absolute value is **at least 1**. So

$$\delta_P(\log|Q|) \;=\; -\infty \quad\text{or}\quad \delta_P(\log|Q|) \;\geq\; 0.$$

That is Serre's Lemma 1.3.1, and it is the whole trick. An analytic quantity has been
forced to be non-negative by an **integrality** constraint. There is no room to be slightly
negative, because there is no integer strictly between 0 and 1.

### Step 2 — pass to the limit

Weak limits preserve non-strict inequalities of this kind (Serre's (1.1.4), using upper
semicontinuity of $\mu \mapsto \int F \, d\mu$ for upper semicontinuous $F$ — and
$\log|Q|$ is upper semicontinuous with values in $\mathbb{R} \cup \{-\infty\}$).

Taking $n$ large enough that $Q$ is not divisible by any of the remaining irreducible
polynomials, Serre gets his Lemma 1.3.4:

$$\mu(\log|Q|) \;\geq\; 0 \qquad \text{for all nonzero } Q \in \mathbb{Z}[X].$$

**This is Smyth's condition from §5.11.** It is not an extra hypothesis; it is what
integrality leaves behind in the limit.

### Step 3 — upgrade to two variables

Run the same argument with $Q \in \mathbb{Z}[X, Y]$ and two measures. For a single
irreducible $P$ with roots $z_i$, set $H_P(Y) = \prod_i Q(z_i, Y)$ — a nonzero polynomial in
$Y$ with **integer** coefficients, because it is symmetric in the roots of an integer
polynomial. Then by Fubini and Step 2,

$$\iint \log|Q(x,y)|\, d\delta_P(x)\, d\nu(y) \;=\; \frac{1}{d}\int \log|H_P(y)|\, d\nu(y)
\;\geq\; 0.$$

Take linear combinations and limits. That is Serre's Lemma 1.3.7. The case we want is
$Q(X,Y) = X - Y$:

$$\boxed{\;I(\mu) \;=\; \iint_{K \times K} \log|x - y| \, d\mu(x)\, d\mu(y) \;\geq\; 0.\;}$$

### Step 4 — read off the capacity

By definition A.3, $\operatorname{cap}(S) = e^{v(S)}$ with $v(S) = \sup_\mu I(\mu)$ over
probability measures supported in $S$. We have exhibited a $\mu$ supported in
$S = \operatorname{Supp}\mu$ with $I(\mu) \geq 0$. Hence $v(S) \geq 0$ and

$$\operatorname{cap}(S) \;\geq\; e^0 \;=\; 1. \qquad \blacksquare$$

### What this says physically

$I(\mu) \geq 0$ says the equilibrium self-energy is non-positive: the charge distribution
is not stressed. A set that is too small forces the charges too close together, the
logarithmic energy blows up, and $I(\mu) < 0$ for every $\mu$ — which is exactly
$\operatorname{cap} < 1$. So:

> **A monic integer polynomial cannot cram all its roots into a set that is too small to
> hold a unit charge comfortably.** The roots repel, and integrality says they cannot
> compromise.

Two corollaries fall out immediately:

- **Fekete (Corollary 1.2.10).** If $\operatorname{cap}(K) < 1$, only finitely many monic
  integer polynomials have all roots in $K$.
- **Kronecker.** On the unit circle, $\operatorname{cap} = 1$ exactly, so we are at the
  boundary. The algebraic integers with all conjugates on the unit circle are precisely the
  **roots of unity**, and the corresponding irreducible polynomials are the cyclotomic
  $\Phi_n$. Serre's §1.5 works this case out completely: the only diffuse limit measure is
  $\frac{1}{2\pi}d\phi$, and every limit measure has the form
  $c_0 \cdot \frac{d\phi}{2\pi} + \sum_{n\geq 1} c_n \delta_{\Phi_n}$ with
  $\sum_{n \geq 0} c_n = 1$.

Also, Step 4 has a rigidity clause worth noting (Serre's 1.2.8): **if
$\operatorname{cap}(S) = 1$ exactly, then $\mu$ must be the equilibrium measure of $S$.** At
the threshold there is no freedom left. That is what makes $[0,4]$, capacity 1, the natural
barrier in the trace problem — and what makes Smith's result, breaking below 2, surprising.

---

## 7. Do this by hand

Three exercises. The first two are half an hour with pen and paper. The third is
twenty minutes and gives you a number Serre states without proof.

### 7.1 The capacity of an interval (15 minutes)

Show that $\operatorname{cap}([-2,2]) = 1$, and deduce that an interval of length $\ell$ has
capacity $\ell/4$.

<details>
<summary>Solution</summary>

Use the Chebyshev definition A.2: $\operatorname{cap}(K) = \lim_n \|T_n\|_K^{1/n}$ where
$T_n$ is the monic degree-$n$ polynomial with smallest sup-norm on $K$.

On $[-2,2]$ the extremal polynomial is characterised by
$$T_n(t + t^{-1}) = t^n + t^{-n},$$
equivalently $T_n(2\cos\theta) = 2\cos n\theta$. (These are the classical Chebyshev
polynomials rescaled from $[-1,1]$ to $[-2,2]$; the substitution $x = 2\cos\theta$ is the
one you already use.) Check monicity by induction from
$T_{n+1}(x) = x\,T_n(x) - T_{n-1}(x)$.

Since $|2\cos n\theta| \leq 2$ with equality attained,
$$\|T_n\|_{[-2,2]} = 2 \quad \text{for every } n,$$
so $\operatorname{cap}([-2,2]) = \lim_n 2^{1/n} = 1$.

Now scaling. Definition A.1 makes it obvious that
$\operatorname{cap}(\lambda K) = |\lambda| \operatorname{cap}(K)$: every distance
$|x_i - x_j|$ scales by $|\lambda|$, and the exponent $1/(n(n-1))$ is chosen so that the
$n(n-1)$ factors give exactly one power of $|\lambda|$. Capacity is also
translation-invariant. An interval of length $\ell$ is $\frac{\ell}{4}$ times a translate of
$[-2,2]$, so its capacity is $\ell/4$.

**Sanity check against the physics.** The equilibrium measure of $[-2,2]$ is
$\frac{1}{\pi}\frac{dx}{\sqrt{4-x^2}}$ — the arcsine law, charge piling up at the ends of a
conducting strip, exactly as electrostatics predicts. And $\operatorname{cap} = \ell/4$
against $\operatorname{cap} = r$ for a circle of radius $r$ says a segment of length $\ell$
has the capacitance of a disc of radius $\ell/4$: flattening a disc into a segment costs you
a factor of 4 in effective radius.

</details>

### 7.2 The integrality trick, on a case you can check (20 minutes)

Let $P \in \mathbb{Z}[X]$ be monic with all roots in the open interval $(-2, 2)$.

(a) Take $Q(X) = X$. What does Step 2 of §6 give you, and what does it say about the
product of the roots?

(b) Now prove Fekete's corollary in this concrete setting: show that only **finitely many**
monic $P \in \mathbb{Z}[X]$ have all roots in a fixed closed interval $[-a, a]$ with
$a < 2$.

<details>
<summary>Solution</summary>

**(a)** With $Q(X) = X$, $\operatorname{Res}(P, Q) = \prod_i z_i = \pm P(0)$, an integer.
So either some root is 0, or $\left|\prod z_i\right| \geq 1$: the geometric mean of the
absolute values of the roots is at least 1. A monic integer polynomial cannot have all its
roots small. Concretely, no monic $P \in \mathbb{Z}[X]$ of degree $d$ has every root in
$(-1, 1)$ unless 0 is a root — the constant term would be a nonzero integer of absolute
value $< 1$.

**(b)** Fix $a < 2$ and let $P$ be monic of degree $d$ with all roots in $[-a, a]$. The
coefficients of $P$ are, up to sign, the elementary symmetric functions of the roots, so
$$|c_k| \;\leq\; \binom{d}{k} a^{d-k}\quad\text{—}$$
bounded. So for each fixed degree $d$ there are only finitely many such $P$: finitely many
integers in each coefficient range. The content of Fekete's theorem is that **the degrees
are bounded too**.

For that, use §6. Suppose there were infinitely many, of unbounded degree. Their root
measures live on the compact set $[-a,a]$, so a subsequence converges weakly to some $\mu$.
By Steps 1–3, $I(\mu) \geq 0$. By definition A.3, $\operatorname{cap}([-a,a]) \geq
e^{I(\mu)} \geq 1$. But by 7.1, $\operatorname{cap}([-a,a]) = 2a/4 = a/2 < 1$. Contradiction.

*(The one gap in this sketch: the limit $\mu$ could a priori be atomic, and §6 Step 4 as I
stated it assumed no atoms. Serre closes this properly — his Theorem 1.2.11 decomposes any
limit measure into an atomic part supported on roots of finitely many fixed irreducible
polynomials plus a diffuse part, and the atomic part contributes only finitely many $P$.
For $a < 2$ the diffuse part is forced to vanish, which is the conclusion.)*

**Where the threshold bites.** $a = 2$, i.e. the interval $[-2,2]$ of capacity exactly 1,
is the boundary — and there the algebraic integers are infinite in number: they are exactly
the numbers $\zeta + \zeta^{-1}$ for $\zeta$ a root of unity, i.e. $2\cos(2\pi k/n)$. Serre
works this out in §1.5. Push to length $> 4$ and Robinson's theorem gives you infinitely
many again, but now with genuine freedom in where they accumulate.

</details>

### 7.3 Serre's necessary condition for the uniform measure (20 minutes)

Serre asks (his 1.6.8) whether the **uniform** (normalised Lebesgue) measure $\nu_E$ on an
interval $E$ of length $L$ can be a limit of root measures. He says a necessary condition
is $I(\nu_E) \geq 0$, and states without proof that an elementary computation gives

$$I(\nu_E) \;=\; \log L - \tfrac{3}{2}.$$

Verify it, and read off the bound on $L$.

<details>
<summary>Solution</summary>

Take $E = [0, L]$ and $\nu_E = \frac{dx}{L}$. Then
$$I(\nu_E) \;=\; \frac{1}{L^2}\int_0^L\!\!\int_0^L \log|x-y| \,dx\,dy.$$

Substitute $x = Lu$, $y = Lv$ with $u, v \in [0,1]$:
$$I(\nu_E) \;=\; \int_0^1\!\!\int_0^1 \big(\log L + \log|u-v|\big)\,du\,dv
\;=\; \log L \;+\; \int_0^1\!\!\int_0^1 \log|u-v|\,du\,dv.$$

For the remaining integral, fix $u$ and split:
$$\int_0^1 \log|u-v|\,dv = \int_0^u \log(u-v)\,dv + \int_u^1 \log(v-u)\,dv
= \int_0^u \log t\,dt + \int_0^{1-u}\log t\,dt.$$
Since $\int_0^s \log t \, dt = s\log s - s$,
$$\int_0^1 \log|u-v|\,dv \;=\; u\log u - u + (1-u)\log(1-u) - (1-u)
\;=\; u\log u + (1-u)\log(1-u) - 1.$$

Integrate over $u \in [0,1]$, using $\int_0^1 u \log u \, du = -\tfrac14$ (and the same for
the reflected term):
$$\int_0^1\!\!\int_0^1 \log|u-v|\,du\,dv \;=\; -\tfrac14 - \tfrac14 - 1 \;=\; -\tfrac{3}{2}.$$

Hence $I(\nu_E) = \log L - \tfrac32$, as Serre states.

**The bound.** $I(\nu_E) \geq 0$ requires $L \geq e^{3/2} = 4.4817\ldots$

*(Serre prints $e^{3/2} = 4{,}816\ldots$ in the exposé. That is a typo — $e^{3/2} =
4.4817$, and $4.816$ is not $e$ to any half-integer power. The inequality and its role are
unaffected; only the printed decimal is wrong. Verify it yourself: $e^{1.5} = 4.48169$.)*

The point Serre is making is that this is **strictly stronger than the obvious bound**
$L > 4$ coming from $\operatorname{cap}(E) = L/4 > 1$. The uniform measure is not the
equilibrium measure — it does not pile up at the ends — so it wastes energy, and needs a
longer interval to compensate. Serre adds a second refinement: if $E$ is centred at 0, then
$\int_E \log|x| \, d\nu \geq 0$ (take $Q(X) = X$) forces $L \geq 2e = 5.4366\ldots$. He
thinks the true answer is that $\nu_E$ is never a limit measure.

**Why this exercise is the right one.** You have just used the Smyth condition as a
*computational* tool: pick a polynomial $Q$, integrate $\log|Q|$ against a candidate
measure, and if you get a negative number the measure is impossible. That is exactly the
linear-programming method Smyth invented in 1984 and that Orloski–Sardari–Smith refined to
get 1.80203. Each choice of $Q$ is one linear constraint; the trace problem is what you get
when you optimise over them.

</details>

---

## 8. What is actually useful to you

Four items. The first is mathematical, the rest are about how work gets done — which is,
underneath the survey, what this lecture is actually about.

### 8.1 Integrality as a hard oracle

The argument in §6 is worth internalising as a *pattern*, not a theorem.

You have a soft, continuous quantity — an integral of $\log|Q|$ against a measure — that
could in principle be any real number. You then observe that on the discrete objects
generating your problem, that quantity equals $\frac{1}{d}\log|N|$ for an **integer** $N$.
Integers have a gap: there is nothing between 0 and 1. So the quantity is either $-\infty$
or $\geq 0$, with no middle. Then you take limits, and the rigidity survives.

This is the same structural move as Kontorovich's Lean compiler in
[`shape-of-math-kontorovich.md`](shape-of-math-kontorovich.md): a **hard, discrete oracle
attached to a soft, continuous process**, which converts "approximately right" into
"right or wrong, no third option". Kontorovich's version is a type checker. Serre's is
$\mathbb{Z}$.

For your own systems the transferable question is: *where in this pipeline is the
quantity that is secretly discrete?* If a check can be made to return an integer rather
than a score, the gap between 0 and 1 does work that no amount of threshold tuning will.
A test that passes or fails is a resultant. A confidence score is not.

### 8.2 Falsifiability as a design property of a specification

Sarnak makes this point twice, in two different centuries of Serre's work, and both times
he is describing what makes a *statement* good rather than what makes a proof good.

On the converse theorem (§5.6):

> "The converse theorem specifies the exact level at which you're going to find the modular
> form, because there's a level in there which is the conductor. And so it's very
> falsifiable — and the minute a conjecture is very falsifiable you can check it, and it's
> more likely when you check it that it's true, that you've put it through some kind of real
> test."

On Serre's modularity conjecture (§5.7), the same virtue in sharper form: the conjecture
does not say "a modular form exists". It names $N(\bar\rho)$ and $k(\bar\rho)$ — the exact
level and the exact minimal weight. That turns an existence claim into a **finite search**,
which means it can be run by machine and can fail loudly.

Serre paid a real price for this. Sarnak notes the conjecture "required a lot of
adjustments", with computations done for Serre by Mestre, over the twelve years from 1975
to 1987, and that Edixhoven refined the weight further afterwards. Twelve years of tuning
a *statement*, not a proof.

The transfer to your work is direct and I do not think it is a stretch. A specification you
hand an agent has the same two forms:

- **Weak:** "make the tests pass", "handle the error case". Satisfiable by a system that
  narrows the task, and unfalsifiable until a human reads the output.
- **Serre-strength:** name the exact level and weight. *This function, called with this
  input, returns this value; this file, after the change, contains no call to X.* Now the
  check is finite and mechanical, and a wrong answer is loud.

The cost is the same cost Serre paid: getting the exact level right is most of the work,
and it takes iterations. The benefit is the same benefit: once the statement is sharp, the
verification is cheap and everything downstream can rely on it.

### 8.3 What a good reviewer actually does

The single most quotable thread in the lecture is not about theorems.

> "He demands the same quality of writing from you as he demands of himself. So he will
> always find errors and corrections and want you to improve it. And there are many people
> who know very well that their papers have improved dramatically after getting a letter
> from Serre. In the old days he would write to anybody who was writing anything interesting
> that he saw — handwritten."

Three properties, all deliberate:

1. **Unsolicited.** He wrote to people who had not asked. The review was not gated on a
   request.
2. **Symmetric standard.** He demanded of others what he demanded of himself. Not a
   different bar for the reviewed.
3. **Specific.** Errors and corrections, not a verdict. The output was a diff, not a score.

Set that against the default behaviour of a review agent, which is unsolicited *(good)*,
holds a standard it does not apply to its own output *(bad)*, and produces a verdict with a
severity rating *(bad)*. The Serre pattern says: the deliverable of a review is a list of
specific corrections that the author can apply, produced by something that would accept the
same corrections applied to itself.

There is also a nice closing of the loop with Kontorovich's lecture in this same playlist.
Kontorovich names **Peter Sarnak and Henryk Iwaniec** as the two mathematicians who never
learned TeX — Iwaniec having held out long enough that he now writes by hand, photographs
it, and has an AI typeset it. Sarnak is here reporting on Serre's handwritten letters. The
whole adoption-threshold argument in
[`shape-of-math-kontorovich.md`](shape-of-math-kontorovich.md) §4.12 — the Knuth factor
crossing 1 around 1990 — has one of its named holdouts giving this lecture.

### 8.4 Exposition and canonization are the same job

Sarnak's claim about the books is stronger than a compliment:

> Milnor, reviewing the collected works: "In many cases the first account of the topic
> appears in one of his papers and remains the best."

That is the definition of **canonization** from Kontorovich's lecture — finding the right,
most general, most reusable form of a result and filing it where everything downstream can
build on it — applied to twenty books over seventy years. Sarnak's whole lecture is a case
study in what canonization buys: FAC and GAGA are load-bearing in 2026 because they were
built to be built on, not to reach one theorem.

The two lectures agree from opposite ends. Kontorovich says canonization is the bottleneck
and models cannot do it. Sarnak spends an hour showing what a career of doing it looks
like. Read them together; the pair is worth more than either.

Also, on format: Sarnak's aside that Séminaire Bourbaki exposés "really explain math
properly" and "we should really introduce them much more broadly" is a concrete claim about
a document type. A Bourbaki exposé is a report on *someone else's* recent work, written by
an expert who did not do it, at full technical depth, with a fixed length. Serre's 1146 is
the proof: 42 pages, and it both explains Robinson's 1964 theorem properly *and* contains
new results Serre had never published. Reviewing someone else's work carefully is
generative.

---

## 9. Where to read next

1. **Serre, *Distribution asymptotique des valeurs propres des endomorphismes de Frobenius
   [d'après Abel, Chebyshev, Robinson, ...]*.**
   [arXiv:1807.11700](https://arxiv.org/abs/1807.11700), Séminaire Bourbaki 1146, 42 pages,
   in French. **Read §1.1–1.4 and Appendix A.** That is 15 pages, it is the whole of §6 and
   §7 above in the original, and it is a model of exposition — Serre defines everything he
   uses and cites everything he does not prove. Appendix B, by Oesterlé, makes the link to
   potential theory explicit, which is your entry point.

2. **Gamburd, Ghosh, Sarnak, Whang, *On indefinite integral ternary quadratic forms*.**
   [arXiv:2603.05849](https://arxiv.org/abs/2603.05849). The 2026 resolution of Serre's 1990
   conics question and Margulis's Markoff-spectrum question. Read the introduction for the
   two theorem statements; the body is homogeneous dynamics and is a real commitment.

3. **Smith, *Algebraic integers with conjugates in a prescribed distribution*.**
   [arXiv:2111.12660](https://arxiv.org/abs/2111.12660), *Annals of Mathematics* **200**
   (2024), 71–122. The answer to Serre's question, and the source of the 1.89831 bound.
   Pair with [arXiv:2401.03252](https://arxiv.org/abs/2401.03252) (Orloski–Sardari–Smith)
   for the 1.80203 lower bound, which is the more readable of the two.

*(Deliberately not listed: anything on spectral sequences, GAGA, or Galois representations.
Those would each be a semester, and this lecture is not the right doorway into any of them.)*

---

## 10. Self-test

<details>
<summary>1. What kind of lecture is this, and how much of it is about Sarnak's own field?</summary>

A tribute lecture on Jean-Pierre Serre, ahead of Serre's hundredth birthday on 15 September
2026. Sarnak's own work appears twice: the conics theorem of §5.10 (Gamburd–Ghosh–Sarnak–
Whang, arXiv:2603.05849) and a one-clause mention that Eskin–Oh's homogeneous dynamics feeds
into it. Nothing on arithmetic quantum chaos or trace formulae.
</details>

<details>
<summary>2. State the three equivalent definitions of logarithmic capacity, and give the capacity of an interval of length ℓ.</summary>

(A.1) Transfinite diameter: $\lim_n \sup_{x_i \in K} \big(\prod_{i \neq j}|x_i -
x_j|\big)^{1/(n(n-1))}$.
(A.2) Chebyshev constant: $\lim_n \|T_n\|_K^{1/n}$, $T_n$ the minimal-sup-norm monic
polynomial of degree $n$.
(A.3) Energy: $e^{v(K)}$ with $v(K) = \sup_\mu \iint \log|x-y|\,d\mu\,d\mu$.

An interval of length $\ell$ has capacity $\ell/4$; $[-2,2]$ has capacity exactly 1. A disc
or circle of radius $r$ has capacity $r$.
</details>

<details>
<summary>3. Why is ∫log|Q| dμ ≥ 0 for every nonzero integer polynomial Q? Where does the inequality actually come from?</summary>

For a single monic integer polynomial $P$ with roots $z_i$, $\frac{1}{d}\sum \log|Q(z_i)| =
\frac{1}{d}\log|\operatorname{Res}(P,Q)|$, and the resultant is an **integer**. So it is 0
(shared root, giving $-\infty$) or has absolute value at least 1 (giving $\geq 0$). The
inequality is not analytic — it comes from the fact that there is no integer strictly
between 0 and 1. It survives weak limits by upper semicontinuity.
</details>

<details>
<summary>4. Why must the support of a diffuse limit measure have capacity at least 1?</summary>

Apply the previous item with $Q(X,Y) = X-Y$ in two variables, which gives $I(\mu) = \iint
\log|x-y|\,d\mu\,d\mu \geq 0$. Since $\operatorname{cap}(S) = e^{\sup_\mu I(\mu)}$ and we
have exhibited $\mu$ with $I(\mu) \geq 0$, we get $\operatorname{cap}(S) \geq e^0 = 1$.
Physically: a set too small to hold a unit charge comfortably cannot hold all the roots of a
monic integer polynomial, because the roots repel and integrality forbids compromise.
</details>

<details>
<summary>5. Where does the exponent q^{1/4} come from in Serre's abelian-varieties theorem?</summary>

Frobenius eigenvalues lie on the circle $C$ of radius $r = \sqrt{q}$ (Weil). Map $C$ to
$[-2r, 2r]$ by $f(z) = z + \bar z = z + q/z$ — the Joukowski transform. Capacity transforms
as $\operatorname{cap}(E) = r^{1/2}\operatorname{cap}(f(E))^{1/2}$. So Fekete's threshold
$\operatorname{cap} \geq 1$ on the interval side becomes $\operatorname{cap}(E) \geq
r^{1/2} = q^{1/4}$ on the circle. Two square roots: one for the double cover, one because
capacity is a geometric mean. Note $q^{1/4}$ is far below $\operatorname{cap}(C) = \sqrt{q}$,
so very thin supports — even Cantor sets of Lebesgue measure zero — are allowed.
</details>

<details>
<summary>6. What is the Schur–Siegel–Smyth trace problem, and where does it stand?</summary>

For $\alpha$ a totally positive algebraic integer (all conjugates positive real), what is
$\liminf \operatorname{tr}(\alpha)/\deg(\alpha)$? For ~70 years the best constructions gave
2, and $[0,4]$ having capacity exactly 1 made 2 look like a structural barrier. Serre saw
that his conjecture on limit measures would break it. Smith (Annals 2024) proved the
conjecture for $K \subset \mathbb{R}$ and produced infinitely many $\alpha$ with
$\operatorname{tr}(\alpha) < 1.89831\deg(\alpha)$. Orloski–Sardari–Smith pushed the lower
bound to 1.80203. Answer in $[1.80203, 1.89831]$.
</details>

<details>
<summary>7. What is the congruence subgroup property, and why is SL₂ the hard case?</summary>

Is every finite-index subgroup of $\operatorname{SL}_n(\mathbb{Z})$ a congruence subgroup —
i.e. does it contain some $\Gamma(N)$? For $n \geq 3$ yes (Bass–Lazard–Serre; Mennicke
independently), proved by showing the congruence kernel $C = \ker(\hat\Gamma \to
\bar\Gamma)$ is trivial. For $n = 2$ no, because
$\operatorname{SL}_2(\mathbb{Z})/\{\pm I\} \cong \mathbb{Z}/2 * \mathbb{Z}/3$ is a free
product with far more finite-index subgroups than there are congruence subgroups. Serre
settled $\operatorname{SL}_2$ over rings of $S$-integers: $C$ is finite iff the unit group is
infinite.
</details>

<details>
<summary>8. What does the open image theorem say, and what is the number 37 doing in it?</summary>

For $E/\mathbb{Q}$ without complex multiplication, the index of the image of
$\rho_{E,n}: G_{\mathbb{Q}} \to \operatorname{GL}_2(\mathbb{Z}/n\mathbb{Z})$ is bounded by a
constant depending on $E$ but **not on $n$** — the adelic image is open. Serre's uniformity
question asks whether the bound can be made independent of $E$ too. The largest prime
$\ell$ for which a non-CM $E/\mathbb{Q}$ is known to have non-surjective mod-$\ell$
representation is 37, so the conjecture is that surjectivity is automatic beyond it.
Bilu–Parent–Rebolledo made progress under hypotheses.
</details>

<details>
<summary>9. Why does the even case of the Artin conjecture resist, in one sentence a PDE person would give?</summary>

Odd representations correspond to holomorphic modular forms, which form a **graded ring** —
you can multiply a weight-one form by an Eisenstein series and land in higher weight, where
the theory exists. Even representations correspond to Maass forms, which are Laplace
eigenfunctions, and eigenfunctions do not multiply into eigenfunctions. So the Deligne–Serre
argument has no first step. Known for solvable projective image (Langlands, via
Saito–Shintani base change); the icosahedral case is open.
</details>

<details>
<summary>10. What does Serre's modularity conjecture assert, and what makes it a good conjecture rather than merely a true one?</summary>

Every odd irreducible $\bar\rho: G_{\mathbb{Q}} \to \operatorname{GL}_2(\mathbb{F})$,
$\operatorname{char}\mathbb{F} = p$, is the mod-$p$ reduction of a holomorphic modular form
of level $N(\bar\rho)$ (prime-to-$p$ Artin conductor) and weight $k(\bar\rho)$ (explicit
from inertia at $p$), with $k(\bar\rho)$ minimal. It is a good conjecture because it names
the exact level and weight, turning an existence claim into a **finite, mechanically
checkable search** — Sarnak's "very falsifiable". It implies Fermat and Artin for odd
2-dimensional representations. Proved by Khare–Wintenberger, with Kisin's contributions.
</details>

<details>
<summary>11. What did Serre notice about the Conway–Radin group, and why should you care?</summary>

The group generated by two rotations about perpendicular axes, arising from Conway and
Radin's aperiodic tilings of $\mathbb{R}^3$, has properties nobody could explain. Serre
observed that lifted to the double cover $\operatorname{SU}(2)$ it is **$S$-arithmetic** —
which explains all of them. It is the same group as the **Clifford+T** universal gate set
used to program quantum computers. Serre, *Le groupe quaquaversal, vu comme groupe
$S$-arithmétique*, Oberwolfach Report 6 (2009) no. 2, 1421–1426.
</details>

---

## 11. Note on the tutorial process

### 11.1 Whether the difficulty matched the reputation

**No, in an unusual direction.** Sarnak's reputation would predict a talk on analytic
number theory, spectral theory, or thin groups — difficulty 4 to 5, with the arithmetic
quantum chaos anchor sitting ready. That prediction is wrong twice over. The talk is not
about Sarnak's field at all; and the part of it that is closest to *your* background is not
close to Sarnak's either. The last twenty minutes are classical potential theory, which is
in your first-year toolkit and is nobody's idea of a Sarnak topic.

The brief I was given said the talk *might* be a tribute to Serre and warned that this was
second-hand and unconfirmed. It is confirmed, from the first ninety seconds of the
transcript: Katz's introduction names the title, and Sarnak says "my talk from now on will
be about Jean-Pierre Serre".

The brief also suggested the Selberg/Gutzwiller anchor if the talk turned out to be
technical. I rejected it — see §2 — for the reason the spec gives about the Gaitsgory
brief: the talk does not support it, and decorating a lecture with a bridge it never builds
is a form of fabrication. I named it as absent instead.

### 11.2 Name corrections

Auto-captions destroyed nearly every proper noun. Every entry below was checked against a
primary or authoritative source.

| Caption | Correct | Check |
|---|---|---|
| "Peter Sarnac" | Peter **Sarnak** | speaker |
| "Sarah", "sir", "Siri", "Sarah" | **Serre** (Jean-Pierre) | subject of the lecture |
| "Vy", "Vay", "V", "Vade", "Bay", "ve" | **Weil** (André) | context throughout |
| "growth and dick", "growth and deacons" | **Grothendieck** | 294-page correspondence volume |
| "her vile", "homeman vi" | Hermann **Weyl** | 1954 laudation |
| "LA", "Laray" | **Leray** | spectral sequences |
| "carton" | Henri **Cartan** | Serre's advisor |
| "Milner" (exotic spheres) | **Milnor** | $S^7$ exotic structures |
| "Milton" (reviewer of the Œuvres) | **Milnor** *(reconstructed — see 11.4)* | — |
| "Wang and Woo" | Guozhen **Wang** and Zhouli **Xu** | ICM 2022, *Stable homotopy groups of spheres and motivic homotopy theory* |
| "Baker Brun and Timman" | **Bakker, Brunebarbe, Tsimerman** | o-minimal GAGA |
| "Beck" | **Bakker** | same |
| "Griffith" | **Griffiths** | the conjecture named |
| "Charles theorem", "charow" | **Chow's** theorem | compact complex submanifolds of $\mathbb{P}^n$ |
| "fa and klein" | **Fricke and Klein** | structure of $\operatorname{SL}_2(\mathbb{Z})$ |
| "bass lazard sir" | **Bass, Lazard, Serre** | CSP for $\operatorname{SL}_n$, $n \geq 3$ |
| "yens minica", "Manica" | Jens **Mennicke** | independent proof |
| "basil ner" | **Bass–Milnor–Serre** | 1967, general $S$-integer case |
| "Kesa Raganathan Prasad Platonov Rapinchukski" | **Kneser, Raghunathan, Prasad, Platonov, Rapinchuk** | *(Kneser reconstructed)* |
| "quonians", "ctonians", "couttonians" | **quaternions** | Hamilton |
| "belu parent and rebolledo" | **Bilu, Parent, Rebolledo** | Serre uniformity progress |
| "Tanyyama" | **Taniyama** | in the photograph |
| "Tamagawa" | **Tamagawa** | correct as heard |
| "delene", "Delen" | **Deligne** (Pierre) | Deligne–Serre 1974 |
| "hecka group" | **Hecke** congruence group $\Gamma_0(N)$ | — |
| "directly character" | **Dirichlet** character | — |
| "reman rock" | **Riemann–Roch** | — |
| "Arton", "art and conductor" | **Artin** conductor, Artin conjecture | — |
| "hel g" | **Hellegouarch** | — |
| "gart fry" | Gerhard **Frey** | the Frey curve |
| "ribbit" | **Ribet** | the epsilon conjecture |
| "wilds", "Taylor wilds" | **Wiles**, **Taylor–Wiles** | modularity lifting |
| "Kissen" | **Kisin** (Mark) | — |
| "K and Winter Bene", "Winton Burge" | **Khare and Wintenberger** | complete proof of Serre's conjecture |
| "Idex" | **Edixhoven** (Bas) | refinement of $k(\bar\rho)$ |
| "Nick Katz" | Nicholas **Katz** | who introduced Sarnak; also the mod-$p$ modular forms |
| "mass form" | **Maass** form | eigenvalue $1/4$ |
| "iicosahhedral" | **icosahedral** | — |
| "Saito and Shintani" | **Saito–Shintani** | base change |
| "hessa and manovsky" | **Hasse–Minkowski** | — |
| "Kurjv Morurv and Suslan" | **Merkurjev and Suslin** | Conjecture II progress |
| "Baflukiga and Parimala" | **Bayer-Fluckiger and Parimala** | 1995, classical groups |
| "Steinberg" | **Steinberg** | correct as heard; 1965 |
| "Gambert Gosh and myself and Wang" | **Gamburd, Ghosh, Sarnak, Whang** | arXiv:2603.05849 |
| "Eskin and O" | **Eskin and Oh** (Hee Oh) | *(reconstructed from context)* |
| "fkata", "faga" | **Fekete** | 1923 |
| "tego" | **Szegő** | 1924, and Fekete–Szegő 1955 |
| "Rafael Robinson" | **Raphael M. Robinson** | 1964 |
| "Vlad and Drenfell" | **Tsfasman and Vlăduţ** | *(see 11.4)* |
| "Smith" (the log-integral condition) | **Smyth** (Chris) | 1984 — a *different person* |
| "Alexander Smith" (the solution) | **Alexander Smith** | Annals 2024 |
| "Oroski" | **Orloski** (Bryce Joseph) | arXiv:2302.02872 |
| "Sardari", "Saridari" | Naser T. **Sardari** | — |
| "Shure Ziggel and Smith" | **Schur, Siegel, Smyth** | the trace problem |
| "Honda tape" | **Honda–Tate** theory | — |
| "Piatic", "profite" | **$p$-adic**, **profinite** | — |
| "Conway and Raiden" | **Conway and Radin** | quaquaversal tiling |
| "Bubaki", "buba keys" | **Bourbaki**, Séminaire Bourbaki | — |
| "Borrell", "Aman Borell" | **Armand Borel** | — |
| "Iwasau and Gleon" | **Iwasawa and Gleason** | 1949–50 exposé |
| "a billion" (repeatedly) | **abelian** | — |
| "coology", "kmology", "comeology" | **cohomology** | — |
| "chief", "sheath", "fol" | **sheaf**, *faisceau* | — |
| "aphine" | **affine** | — |
| "holorphic", "holmorphic" | **holomorphic** | — |
| "gwa", "galway", "gola", "gullomology" | **Galois**, Galois cohomology | — |
| "sero conjecture", "Serak conjecture" | **Serre's** conjecture | — |

### 11.3 Substantive corrections, not just spellings

- **Sarnak misstates the open image theorem and corrects himself mid-sentence** (§5.5). The
  captions preserve the confusion: "independent of $E$, independent of $n$, but depending on
  $E$, my apologies." The correct statement is that the index bound depends on $E$ and is
  independent of $n$. I state the corrected version.
- **"Smith" is two people.** The transcript uses one caption spelling for **Chris Smyth**,
  who introduced the $\int\log|Q|\,d\mu \geq 0$ technique in 1984 (Serre cites him as [Sm 84]
  in a footnote), and for **Alexander Smith**, who resolved Serre's question in 2024. They
  are unrelated. Conflating them would make the section incoherent — Smyth's condition is
  the *necessary* half, Smith proved it *sufficient*. Corrected throughout.
- **Fekete–Szegő versus Robinson.** Sarnak says "a converse due to Raphael Robinson if
  $K \subset \mathbb{R}$, and due to Szegő in general". Serre's text makes the distinction
  precise and it matters: Fekete–Szegő (1955) gives algebraic integers in every
  *neighbourhood* of $K$; Robinson (1964) gives them **in $E$ itself**, for finite unions of
  real intervals. The neighbourhood version is not strong enough for Serre's application.
  Stated precisely in §5.11.

### 11.4 Errors found in the companion document

The spec is right that the companion is not infallible. Two, both checked:

1. **Serre's (A.2.1)** applies the exponent $1/n$ twice — he defines $c_n(K) = \inf_P
   \|P\|_K^{1/n}$ and then writes $\operatorname{cap}(K) = \lim_n c_n(K)^{1/n}$. This
   happens to give the right answer for his example $K = [-2,2]$ but is wrong in general:
   for the circle of radius $r$ the correct capacity is $r$ and the doubled exponent gives 1.
   Flagged in §3.3, with the correct statement.
2. **Serre prints $e^{3/2} = 4{,}816\ldots$** in §1.6.8. The correct value is
   $e^{3/2} = 4.4817\ldots$. The inequality $L \geq e^{3/2}$ and its role are unaffected;
   only the decimal is wrong. Flagged in §7.3.

Neither error is load-bearing. I record them because a reader working through the exposé
alongside this tutorial will otherwise lose time on them.

### 11.5 Reconstructed, and unverified

**Reconstructed** (rebuilt from spoken narration or context, verifiable as noted):

- The Deligne–Serre and Serre-conjecture statements in §5.6 and §5.7. Sarnak wrote the
  transformation law, the Fourier expansion and the conductor formula on the board; the
  captions carry no formula. I restored the standard statements from the literature. **What
  would verify them:** Deligne–Serre, *Formes modulaires de poids 1*, Ann. Sci. ENS 7
  (1974); Serre, *Sur les représentations modulaires de degré 2 de
  $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$*, Duke Math. J. 54 (1987).
- The proof sketch in §6 and every statement in §5.11 are **not** reconstructed — they are
  restored verbatim from Serre's exposé 1146, with theorem numbers given.
- "Kneser" in the CSP progress list (§5.4) — the caption reads "Kesa", and Kneser is the
  standard first name in that list. Reconstructed.
- "Eskin and Oh" (§5.10) — the caption reads "Eskin and O", and Sarnak says he introduced
  "O" earlier at the congress, which fixes it as Hee Oh. Reconstructed but near-certain.

**Could not verify:**

- **The 1953 lecture that started Serre on modular forms.** The caption reads "he heard a
  lecture I think by GMA" and no plausible name matches. Omitted rather than guessed.
- **Milnor as the reviewer of Serre's Œuvres I–III.** The caption reads "Milton". Milnor is
  the obvious reading and Milnor did review Serre's work, but I could not confirm this
  specific review. Flagged in place at §5.13.
- **Tsfasman–Vlăduţ.** The caption reads "a theorem of Vlad and Drenfell". Serre's exposé
  cites the relevant result as Tsfasman–Vlăduţ [TV 97], with a companion reference [Se 97].
  Drinfeld and Vlăduţ have a famous joint bound in the same area, so the caption may
  faithfully record Sarnak saying "Drinfeld–Vlăduţ". I have used Tsfasman–Vlăduţ, which is
  what the companion supports, and flag the ambiguity here.
- **Mestre** doing computations for Serre's conjecture (§5.7). The caption reads "master".
  Jean-François Mestre is named in Serre's acknowledgements in exposé 1146 for help with
  §2, which makes the reading plausible but does not confirm it for the 1987 conjecture.
  Stated with the name; treat as reconstructed.
- **The exact wording of Weyl's 1954 laudation.** Widely quoted in the form Sarnak gives;
  I have not checked the printed proceedings.

### 11.6 Where the gaps are, and how much they cost

| Gap | Impact |
|---|---|
| §5.1 — no proof or mechanism for the spectral sequence | **Low.** The theorem statement is complete and the machine is declared untaught by design. |
| §5.2 — GAGA stated, not proved or defined | **Low.** Sarnak also states it without proof. What it buys is fully recoverable. |
| §5.6, §5.7 — all formulas on the board | **Moderate.** I restored the standard statements from the primary literature, so nothing is missing, but I cannot certify that Sarnak's normalisations match mine. The two Serre-conjecture invariants $N(\bar\rho)$ and $k(\bar\rho)$ are named and their roles are exact; the **recipe for $k(\bar\rho)$ from inertia is not given** — Sarnak says explicitly he will not give it, and I follow him. |
| §5.9 — the definition of $H^1(K,G)$ is described, not constructed | **Low by design.** Declining to teach it, per the spec. |
| §5.10 — Sarnak names the theorem but no statement | **None.** Fully restored from arXiv:2603.05849. |
| §5.11, §6 — the mathematics | **None.** Fully restored from Serre's own exposé, with theorem numbers. |
| §5.12 — which rotation orders generate the group | **Low.** Sarnak says only "two rotations"; the standard quaquaversal group is $G(6,4)$, which I state with a source. The mathematical content — $S$-arithmeticity, and the identity with Clifford+T — is exact. |

The single most consequential caveat in the whole lecture, and Sarnak gives it one sentence,
is in §5.8: **we do not know how to approach the even case at all.** Half of all
two-dimensional Artin representations are outside every technique described in this hour,
and the reason is a fact about products of eigenfunctions. That is a moderate-impact gap in
the *lecture*, not in this tutorial — I have said everything Sarnak said about it and added
the one attribution he omitted.

### 11.7 Sibling tutorials

This tutorial deliberately does not re-derive material covered elsewhere in `summaries/`:

- **Canonization, exposition as research, and adoption thresholds** are treated at length in
  [`shape-of-math-kontorovich.md`](shape-of-math-kontorovich.md) §4.9 and §4.12. §8.4 above
  cites it and moves on. The two lectures are a genuinely good pair — one names the
  bottleneck, the other shows seventy years of someone clearing it — and Sarnak is named in
  Kontorovich's talk as a TeX holdout.
- **The Langlands programme** as a framework, of which the Artin conjecture material in
  §5.6–5.8 is the two-dimensional edge, is covered in
  [`langlands-function-fields-gaitsgory.md`](langlands-function-fields-gaitsgory.md). Read
  that first if you want the frame; this tutorial gives only what Sarnak gives.
