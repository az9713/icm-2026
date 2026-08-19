---
title: "Structure of sets with an unexpected number of arithmetic patterns"
speaker: Tamar Ziegler (Hebrew University of Jerusalem)
source: https://www.youtube.com/watch?v=czHiX0pYTDg
video_id: czHiX0pYTDg
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: "none — companion: https://arxiv.org/abs/1404.0775 (her ICM 2014 survey, covers roughly the first two-thirds)"
transcript: ../transcripts/czHiX0pYTDg_transcript.txt
difficulty_for_you: 3/5
reading_time: ~65 min
---

# Structure of sets with an unexpected number of arithmetic patterns — Tamar Ziegler

**Field:** additive combinatorics, ergodic theory and analytic number theory, braided
together. The specific subject is **higher-order Fourier analysis**: what you do when the
Fourier transform stops seeing the thing you are trying to count.

**Difficulty against your background: 3 out of 5.** A real gap, and a crossable one. Every
object in this talk is built by deforming something you already own — the Fourier
transform, a measure-preserving flow, an eigenfunction, a finite difference, an entropy.
Nothing here needs algebraic geometry, representation theory, or category theory. What it
needs is a willingness to follow one idea ("a wrong count means hidden structure") through
four increasingly refined incarnations. I did not split the rating: the talk is one
continuous argument, and the second half is not harder than the first, only newer.

The reason it is a 3 and not a 2 is vocabulary density. In fifty minutes she uses
Kronecker factors, characteristic factors, nilmanifolds, nilsequences, Gowers norms,
inverse theorems, the Liouville function, topological entropy, and logarithmic averaging.
Each is a small idea. There are nine of them and they stack.

**Prerequisites this tutorial builds:** the balanced function and what a "random count"
means; Roth's dichotomy and the density-increment loop; the Furstenberg correspondence
principle; characteristic factors and why the Kronecker factor is the spectral theorem in
disguise; the skew shift and the finite-difference identity that kills linear Fourier
analysis; nilsystems and nilsequences in one paragraph each; Gowers norms as iterated
multiplicative derivatives; the two inverse theorems; the Liouville function; topological
entropy as block growth.

**A note on sources.** There is **no ICM 2026 proceedings paper.** No arXiv preprint flagged
as an ICM write-up exists, and no chapter for this talk was found in the deposit for the
plenary volume. The lecture title above is the one the chair reads from the podium and the
one Ziegler repeats in her second sentence, so it is confirmed from the talk itself, not
from the announcement.

The **companion** — clearly labelled as a companion, not the proceedings paper — is her
**ICM 2014 sectional-lecture survey**, [*Linear equations in primes and dynamics of
nilmanifolds*, arXiv:1404.0775](https://arxiv.org/abs/1404.0775), submitted 3 April 2014.
It is the right choice for an unusual reason: it follows the first two-thirds of the 2026
talk almost beat for beat — Roth, Szemerédi, Furstenberg, characteristic factors, the skew
shift, the Heisenberg nilsystem, Gowers norms, both inverse theorems, linear equations in
primes — and it carries the formulas that the auto-captions destroyed. Her other candidate,
the 2013 EMS Lecture Series notes, is older and covers the same ground.

The companion **stops in 2014**. Everything in the talk's last third — Chowla, Sarnak,
logarithmic averaging, the Liouville subshift, sign patterns, the multidimensional frontier
— postdates it entirely. That material is restored here from the **primary papers for each
result**, cited inline by name and arXiv number, and kept visibly separate from the
companion. Where the talk and a paper differ, I say which one I am quoting.

**On formulas.** As always in this playlist, the auto-captions carry none. Every displayed
equation below comes from the companion or from a named primary paper, or is marked
**reconstructed** with a one-line check you can run yourself.

---

## 1. What is at stake

Take a set. Count the patterns in it. Compare the count to what you would get from a coin
flip. If the two agree, the set is boring in the only sense that matters here. If they
disagree — in either direction — **something is generating that discrepancy, and the
discrepancy tells you what.**

That is the whole talk, and Ziegler states it as a slogan two minutes in:

> "Our guiding principle will be that if we have an uncommon count or an unexpected count
> then this should reveal some structure on the set E."

Concretely. Fix an ambient structured set *X* — a vector space over 𝔽₃, or ℤ/Nℤ, or the
integers. Fix a subset *E* ⊆ *X* of density δ, meaning |*E*| = δ|*X*|. An **arithmetic
pattern** is a small configuration that inherits the ambient structure: a line inside a
vector space, an arithmetic progression inside the integers. Ask two questions:

1. Does *E* contain any such patterns?
2. **How many?**

Question 1 is the famous one — Roth, Szemerédi, Green–Tao. Question 2 is the one this talk
is actually about, and it is strictly harder and strictly more useful. Question 1 gives a
lower bound; question 2 gives an asymptotic, and asymptotics are what let you do number
theory.

The baseline is easy to compute. Build a random *E* by flipping a δ-biased coin at every
element of *X*. In a vector space *V* over 𝔽₃, a line is exactly a 3-term arithmetic
progression *x*, *x*+*d*, *x*+2*d*. There are |*V*|² pairs (*x*, *d*), and for *d* ≠ 0 the
three membership events are independent, so the expected count is

> **δ³ · |V|²**

That number is the yardstick. Everything else in the talk is a theory of what it means to
miss it.

And you cannot dismiss the possibility of missing it, because the simplest structured set
misses it badly. Let *E* be a **subspace** of density δ. Now if *x* and *x*+*d* are both in
*E*, then *x*+2*d* = 2(*x*+*d*) − *x* is automatically in *E*. So instead of paying δ three
times you pay it twice:

> **δ² · |V|²**  — which for small δ is enormously more than δ³|V|².

So structure inflates the count. The content of the subject is the converse: **inflation
(or deflation) implies structure**, and you can say which structure.

Why anyone should care beyond the aesthetics: this machinery is what produces the
asymptotic count of *k*-term arithmetic progressions among the primes, and — twenty years
later, and to the speaker's visible delight — what produces a theorem about the sign
patterns of the Liouville function, a negative answer to Hilbert's tenth problem for
finitely generated rings, and the construction of infinitely many rank-two elliptic curves
over ℚ. None of it was designed for those.

---

## 2. Your anchor: this is precisely where the Fourier transform goes blind

The anchor is not an analogy. It is the literal subject of the talk, and Ziegler hands it to
you from the podium in two sentences that bracket the whole hour.

At the start, on how to detect an unexpected count of 3-term progressions:

> "The way to detect this is using Fourier analysis. … If you start with a function *f*
> which is 1_E minus delta — this is called the balanced function — then if I deviate from
> random count, this formula coming from the Fourier transform will tell me that this
> function will have a large Fourier coefficient."

And later, introducing the Gowers norms, on what the family of norms measures:

> "For *k* equals 1 this number is just the absolute value of the average of *f*. And for
> *k* equals 2 you can do kind of a short Fourier argument [which] will tell you that this
> is associated to the largest Fourier coefficient. And we want to think of general *k* as
> kind of saying something about *k*-th order structure."

That is the anchor, in her words: **the Gowers norm U^k is the k-th member of a family
whose second member is the sup of the Fourier coefficients.** U¹ is the mean. U² is the
Fourier transform. U³, U⁴, … are the things that see what the Fourier transform cannot.

You own the U² rung completely. Here is the whole of it, and you can verify it in ten
minutes (I put it in §7 as an exercise). For *f* : ℤ/Nℤ → ℂ with
*f̂*(*r*) = 𝔼ₓ *f*(*x*) e(−*xr*/N):

> ‖*f*‖⁴_{U²} = Σ_r |*f̂*(*r*)|⁴ = ‖*f̂*‖⁴_4,  and  ‖*f̂*‖⁴_4 ≤ ‖*f̂*‖²_∞ · ‖*f̂*‖²_2.

So for a 1-bounded *f*, ‖*f*‖_{U²} ≥ η forces ‖*f̂*‖_∞ ≥ η². (Companion, §5, immediately
after Definition 5.1.) A large U² norm *is* a large Fourier coefficient. Nothing more.

**Now the failure.** Fourier analysis counts 3-term progressions because the trilinear form
diagonalizes:

> 𝔼_{x,d} *f*(*x*) *g*(*x*+*d*) *h*(*x*+2*d*) = Σ_r *f̂*(*r*) *ĝ*(−2*r*) *ĥ*(*r*)

*(reconstructed — this is the standard three-line computation; expand each function in
characters and read off the two constraints a+b+c ≡ 0 and b+2c ≡ 0. The companion asserts
the consequence without displaying the identity.)*

The right-hand side is a single sum over one frequency, so one large Fourier coefficient
controls it. Try the same for **four**-term progressions and the character orthogonality
gives you a *two*-parameter family of surviving frequencies; the form does not collapse to a
single sum, and no bound on ‖*f̂*‖_∞ controls it. This is not a technical annoyance. There
are explicit 1-bounded functions with **vanishing** Fourier coefficients and a **maximally
wrong** 4-term count. §4.5 builds one for you in four lines.

The reason is one you can state in your own vocabulary: the Fourier transform expands in
**linear** phases e(αx). A 4-term progression is sensitive to **quadratic** phases e(αx²),
and a quadratic phase is spread evenly across all linear frequencies. Your tool has a
blind spot with a name, and higher-order Fourier analysis is the theory of what lives in it.

**Two more things you already own, both load-bearing.**

**The spectral theorem.** The first ergodic-theoretic object in the talk, the *Kronecker
factor*, is built out of eigenfunctions of the Koopman operator: functions with
ψ(*Tx*) = λψ(*x*). The companion (§3) constructs it exactly that way. When Ziegler says
"the obstruction comes from an abelian dynamical system", she means: the point spectrum of
the shift operator is nontrivial, and that spectrum is a compact abelian group, and rotation
on that group is the obstruction. This is your spectral decomposition of a unitary operator,
read as dynamics.

**Entropy as block growth.** In the last third she needs topological entropy. She defines it
for subshifts exactly as you would want: count the number *S*(*k*) of distinct length-*k*
blocks that occur, and take the exponential growth rate, lim (1/*k*) log *S*(*k*). The full
shift on {±1} gives log 2. A periodic sequence gives 0. Zero entropy means subexponential
block growth. This is the same counting-of-microstates that gives you the Boltzmann entropy;
the "microstates" are the words you can see through a window of width *k*.

---

## 3. The bridge

Nine ideas. Each one is defined by deforming something you have. Read this section slowly;
§4 assumes all of it.

### 3.1 The balanced function, and what "unexpected" means

Let *E* ⊆ *X* have density δ. The **balanced function** is

> *f* = 1_E − δ.

It has mean zero by construction. Every count of a pattern in *E* is a multilinear form in
1_E = δ + *f*; expanding, you get the pure-δ term (which is the random prediction) plus a
pile of terms each containing at least one *f*. So "*E* has an unexpected count" is exactly
"some multilinear form in *f* is large", and the entire subject is a theory of when
multilinear forms in a mean-zero function can be large.

Small but useful observation: the terms containing **exactly one** *f* vanish outright,
because 𝔼*f* = 0 and the other slots are constants. The action starts at two.

### 3.2 Roth's dichotomy, and the loop that it powers

Ziegler gives two versions, one in each ambient group.

**In a vector space over 𝔽₃** — the *Roth–Meshulam* dichotomy (Roth 1953; R. Meshulam,
*On subsets of finite abelian groups with no 3-term arithmetic progressions*, J. Combin.
Theory Ser. A 71 (1995), 168–172). For *E* ⊆ *V* of density δ, **either** *E* has
essentially the random number δ³|*V*|² of lines, **or** *E* has density at least δ + *c*(δ)
on an affine hyperplane.

**In ℤ/Nℤ** — Roth's original. **Either** *E* has essentially δ³N² three-term progressions,
**or** *E* has density at least δ + *c*(δ) on an arithmetic progression of length about
N^{1/3}. (Companion §2, which also records *c* as a decreasing positive function and notes
Sanders' subsequent improvement of the density threshold to 1/(log N)^{1−o(1)}.)

**The loop.** This is the part worth internalizing, because it is a control structure and
not a theorem. Suppose you want to prove that every dense set contains *some* progression.
Run the dichotomy. If the first branch fires, you are done — you have many progressions. If
the second fires, restrict to the sub-object and repeat: your density has gone up by *c*(δ),
and a hyperplane is again a vector space, a long progression is again "a bit like a cyclic
group". Density is bounded by 1, so the loop **cannot run more than about 1/c(δ) times**. It
must exit through the first branch, or bottom out at density 1 where progressions are free.

Ziegler: *"we can't — our density can't go beyond one. So at the end of the day … we end up
with a subspace which definitely contains lines."* This is a termination argument with a
monotone bounded potential. Hold onto it; §8 comes back to it.

**Where the Fourier transform enters.** The second branch is produced, not assumed. If the
count is wrong, the balanced function has a large Fourier coefficient (§2). A large
coefficient means *f* correlates with a character e(α·*x*). Over 𝔽₃ⁿ a character is the
exponential of a **linear form**, so its level sets are literally affine hyperplanes and you
read the hyperplane straight off the correlation. Over ℤ/Nℤ it takes one extra step:
equidistribution of {*xr*/N} mod 1 gives you a progression of length ~N^{1/3} on which the
phase is nearly constant. Ziegler flags the difference explicitly — in the vector space
"we can really easily see which is the hyperplane from this correlation."

**Vocabulary:** call this **first-order** or **linear** structure. It is the only kind
ordinary Fourier analysis can see.

### 3.3 Szemerédi, and the accident that started ergodic Ramsey theory

Roth is 1953 and covers three terms. The general statement — every set of positive upper
density in ℤ contains arbitrarily long arithmetic progressions — is **Szemerédi's theorem**,
1975 (Acta Arith. 27, 299–345), and it took twenty years.

Ziegler skips the proof and tells the story instead, because the story is the pivot of the
talk. In 1975–76 the newly formed Israel Institute for Advanced Studies ran a special year
on ergodic theory, organised by **Benjamin Weiss**, **Hillel Furstenberg** and **Yitzhak
Katznelson**. A visitor, the German mathematician **Konrad Jacobs**, offered an off-topic
talk on a combinatorics theorem he had heard about. Furstenberg, sitting in the audience,
realised he might have a dynamical proof. He did, and the field it opened is now called
**ergodic Ramsey theory**.

The mathematical content of that realisation is the next item.

### 3.4 The Furstenberg correspondence principle: change the category

This is a genuine change of subject, and it is the kind of move you should enjoy.

> **Theorem (Furstenberg correspondence principle).** Let *E* ⊆ ℕ have positive upper
> density. There exists a probability measure-preserving system (*X*, ℬ, μ, *T*) and a
> measurable set *A* with μ(*A*) > 0 such that for any integers *n*₁, …, *n*_k,
>
> > μ(*A* ∩ *T*^{−n₁}*A* ∩ … ∩ *T*^{−n_k}*A*) > 0
>
> implies d̄(*E* ∩ (*E*−*n*₁) ∩ … ∩ (*E*−*n*_k)) > 0; in particular there is an integer *x*
> with *x*, *x*+*n*₁, …, *x*+*n*_k ∈ *E*.

*(Companion, Theorem 3.1. A measure-preserving system is a probability space with an
invertible measurable T pushing μ to itself.)*

The dictionary is worth writing out, because it is the whole trick:

| combinatorics, in ℤ | dynamics, in (*X*, ℬ, μ, *T*) |
|---|---|
| a subset *E* of positive density | a set *A* of positive measure |
| translating by *n* | applying *T*ⁿ |
| a pattern *x*, *x*+*n*, …, *x*+*kn* inside *E* | multiple recurrence: returning to *A* at times *n*, 2*n*, …, *kn* |

Ziegler's example: take *E* = the even numbers. The correspondence produces the two-point
system {0,1} with *T* = "add 1 mod 2", uniform measure, and *A* = {0}. Start with an
arbitrary *E* and you get an arbitrary *A* of positive measure — no free lunch, the system is
as unknown as the set was.

**So why is this progress?** Because in a measure-preserving system you can prove and use
**structure theorems**, and there is nothing analogous available for an arbitrary set of
integers. The rest of the ergodic half of the talk consists of structure theorems.

What Furstenberg then proves:

> **Furstenberg multiple recurrence theorem (1977).** For any measure-preserving system,
> any *A* with μ(*A*) > 0 and any *k* > 0,
>
> > liminf_{N→∞} (1/N) Σ_{n ≤ N} μ(*A* ∩ *T*^{−n}*A* ∩ … ∩ *T*^{−kn}*A*) > 0.

*(Companion, Theorem 3.2, from Furstenberg, J. Analyse Math. 31 (1977), 204–256. From the
podium Ziegler states the weaker form "there exists n > 0 with the intersection of positive
measure" — enough for Szemerédi. The averaged form is the one that generalizes, and the one
the rest of the talk uses.)*

She also flags the right way to see it: **k = 1 is the Poincaré recurrence theorem.** So
Szemerédi's theorem is Poincaré recurrence for a whole orbit-arithmetic progression at once.
That reframing is the reason the ergodic route exists.

### 3.5 Characteristic factors: the smallest quotient that knows the answer

Here is the central technical device, and it is a compression idea.

A **factor** of a system *X* is the image of a morphism of systems — a measure-preserving
map that intertwines the two transformations. Think: a quotient that forgets some
information but stays dynamical.

You want to evaluate

> (1/N) Σ_{n≤N} ∫ *f*₀(*x*) *f*₁(*T*ⁿ*x*) ⋯ *f*_k(*T*^{kn}*x*) dμ  … (★)

in a system you know nothing about. Say a factor π : *X* → *Y* is **k-characteristic** if
(★) is asymptotically unchanged when you replace each *f*_i by its projection π\**f*_i and
compute in *Y* instead. *(Companion, Definition 3.3.)* Two trivial remarks fix the idea:
*X* is *k*-characteristic for every *k* (project onto yourself), and the one-point system is
1-characteristic (that is the mean ergodic theorem). The content is in finding the
**smallest** one, and — crucially — in it being **universal**: a factor of every other
characteristic factor, hence canonical.

**Conventions, fixed once for the whole document.** The caption track drifts between two
indexings; I use one throughout:

> **(k+1)-term progressions ⟷ the average (★) with k+1 functions ⟷ the U^k norm ⟷
> (k−1)-step nilsystems.**

Sanity check at the bottom rung: 3-term progressions ⟷ U² ⟷ 1-step = abelian rotation ⟷
linear phases. That is §3.2, and everything above it is the same statement one order up.

### 3.6 The Kronecker factor is the point spectrum

For 3-term progressions (*k* = 2), Furstenberg's answer:

> The **Kronecker factor** *Z*(*X*) — a compact abelian group *Z* with Haar measure and the
> rotation *T_Z*(*z*) = *z* + α — is the universal 2-characteristic factor.

To evaluate the 3-term average in an arbitrary system, project everything to a **group
rotation** and compute there. And in a group rotation the computation is trivial for exactly
the reason the subspace example was easy: *z* + 2*nα* is determined by *z* and *z* + *nα*.
Two points fix the third.

**Why this is your spectral theorem.** The companion constructs *Z*(*X*) from
**eigenfunctions**. If ψ(*Tx*) = λψ(*x*), then |ψ| is *T*-invariant, hence constant by
ergodicity, hence ψ can be normalised to the unit circle — and a normalised eigenfunction
*is* a morphism from *X* to a circle rotation by λ. Assemble all of them and you get
*Z*(*X*). So:

> **Kronecker factor = the point spectrum of the Koopman operator, packaged as a group
> rotation.**

If there are no nontrivial eigenfunctions the factor is a point, the system is called
**weakly mixing**, projection is just integration, and

> (1/N) Σ_{n≤N} ∫ *f*(*x*)*f*(*T*ⁿ*x*)*f*(*T*^{2n}*x*) dμ → (∫*f* dμ)³ = μ(*A*)³,

the random answer. *(Companion §3.)* Compare this with the δ³|V|² of §1. It is the same
statement in the other category. That correspondence — δ³ on the combinatorial side, μ(*A*)³
on the dynamical side — is the reason the two halves of the talk are one talk.

### 3.7 The skew shift: your first quadratic obstruction, in four lines

Now the failure, made concrete. Take the two-dimensional torus with

> *T*(*z*, *w*) = (*z* + α, *w* + 2*z* + α),  α irrational.

Iterate and you get, by an induction you should actually do (it is Exercise 7.2):

> *T*ⁿ(*z*, *w*) = (*z* + *n*α, *w* + 2*n z* + *n*²α).

The **n² is the entire story.** Now verify, in the additive notation of the torus:

> *y* = 3*T*ⁿ*y* − 3*T*^{2n}*y* + *T*^{3n}*y*

*(Companion §4. The identity is the vanishing of the third finite difference of a quadratic:
Σ_{j=0}^{3} (−1)^j C(3,j) T^{jn} y = 0. You know this operator.)*

So in this system **three points of a four-term progression determine the fourth**, exactly
as two determined the third in a group rotation — but one order up, and by a relation that
no linear structure can express.

The witness is explicit. Let φ(*z*, *w*) = e^{2πi w}. Then

> φ(*Ty*) = e^{2πi(w + 2z + α)} = ψ(*y*) φ(*y*),  where ψ(*z*,*w*) = e^{2πi(2z+α)},

and ψ is an *ordinary* eigenfunction (ψ(*Ty*) = e^{4πiα} ψ(*y*)). A function whose
multiplier is itself an eigenfunction is called a **second-order eigenfunction**. From the
finite-difference identity,

> φ(*y*) = φ³(*T*ⁿ*y*) · φ^{−3}(*T*^{2n}*y*) · φ(*T*^{3n}*y*),

so choosing *f*₀ = φ̄, *f*₁ = φ³, *f*₂ = φ̄³, *f*₃ = φ makes the four-term average
**identically 1** for every *n*. And yet each *f*_i **projects to zero on the Kronecker
factor**, because ∫ e^{2πi k w} d*w* = 0 for *k* ≠ 0. *(Companion §4.)*

Read that again in Fourier language: a function with no first-order content at all, whose
four-term count is maximally non-random. That is the blind spot of §2, exhibited.

### 3.8 Nilsystems and nilsequences

Second-order eigenfunctions are not the end of it. The companion gives the system that has
the same rigidity with **no** nontrivial second-order eigenfunctions: the **Heisenberg
nilsystem**. Take

> *G* = upper unitriangular real 3×3 matrices, Γ = the same with integer entries,
> *Y* = *G*/Γ,

Haar measure, and *T*(*g*Γ) = *a g*Γ for a fixed *a* ∈ *G* (Ziegler's *a* has α and β in the
two super-diagonal slots). Topologically *Y* is a circle bundle over a 2-torus. Again
*g*Γ is determined by *aⁿg*Γ, *a*^{2n}*g*Γ, *a*^{3n}*g*Γ — but not by any equation you can
write down as simply as the skew shift's. *(Companion §4, including the remark that the
absence of second-order eigenfunctions follows from Leibman's equidistribution theorem for
polynomial orbits on nilmanifolds.)*

**General definition.** A ***s*-step nilsystem** is (*G*/Γ, Haar, *g*Γ ↦ *ag*Γ) where *G*
is an *s*-step nilpotent Lie group and Γ a lattice. A **pro-nilsystem** is an inverse limit
of these. "*s*-step nilpotent" means the lower central series terminates: [*G*,[*G*,…]] = 1
after *s* brackets. Abelian is *s* = 1, so a group rotation is a 1-step nilsystem, and the
whole hierarchy is one deformation of the Kronecker factor.

A ***s*-step nilsequence** is what you get by sampling: fix *x* ∈ *G*/Γ, *a* ∈ *G*, and a
continuous (Lipschitz) *F* : *G*/Γ → ℂ, and take

> *n* ↦ *F*(*aⁿ x* Γ).

For *s* = 1 this is *F*(*x* + *n*α) on a circle — a linear phase, dressed. For *s* = 2 you
get things behaving like e(α*n*²). Nilsequences are the higher-order analogue of characters,
and that is the only sentence you need about them.

### 3.9 The Gowers norms

Now the combinatorial detector. Let *G* be a finite abelian group and *f* : *G* → ℂ. Define
the **multiplicative discrete derivative** in direction *h*:

> Δ_h *f*(*x*) = *f*(*x*+*h*) · conj(*f*(*x*)).

Differentiate in *k* directions and average everything:

> ‖*f*‖^{2^k}_{U^k} = 𝔼_{x, h₁,…,h_k} Δ_{h₁} ⋯ Δ_{h_k} *f*(*x*).

*(Companion, Definition 5.1. The exponent is 2^k because each derivative doubles the number
of copies of f in the product.)* Three calibration facts, all in the companion:

- For 1-bounded *f*, ‖*f*‖_{U^k} = 1 **iff** *f*(*x*) = e^{2πi q(x)} with *q* a polynomial
  of degree < *k*. The norm is exactly a polynomial-phase test: differentiating a degree-*d*
  polynomial phase *d*+1 times kills it.
- If *f* correlates with such a phase, ‖*f*‖_{U^k} is large. (Repeated Cauchy–Schwarz.)
- A random ±1 function has ‖*f*‖_{U^k} = o(1).

**Why the norm is the right detector.** Two statements, both from the companion §5:

> |AP_k(*f*) − AP_k(*g*)| ≪_k ‖*f* − *g*‖_{U^k[N]},  where AP_k(*f*) = 𝔼_{x,d} *f*(*x*)*f*(*x*+*d*)⋯*f*(*x*+*kd*)

and, far more generally,

> **Proposition.** For 1-bounded *f*₁,…,*f*_m and affine linear forms *L*₁,…,*L*_m in *d*
> variables with integer coefficients, no two affinely dependent, there is a *k* with
>
> > |𝔼_{**x** ∈ [N]^d} *f*₁(*L*₁(**x**)) ⋯ *f*_m(*L*_m(**x**))| ≪ min_j ‖*f*_j‖_{U^k[N]}.

This is the *generalized von Neumann inequality*, proved by repeated Cauchy–Schwarz, and it
is where the technical hypothesis "no two forms affinely dependent" is born. Ziegler's
framing from the podium is the one to keep:

> "This norm is kind of an analytic detector of an uncommon count of patterns — in this case
> arithmetic progressions, but as I said, many more patterns."

**One detector, an entire family of patterns.** That is the design property, and §8 argues it
is the transferable one.

So the combinatorial chain is now: *unexpected count of (k+1)-term progressions* ⟹ *the
balanced function has large U^k norm*. And the remaining question is the one you would ask:
**what does a large U^k norm actually mean?**

### 3.10 The two inverse theorems

Motivated by the ergodic-theoretic answer — pro-nilsystems — Green and Tao conjectured in
2006 that the combinatorial answer should be algebraic in the same way. It is.

**Over 𝔽_pⁿ.** If ‖*f*‖_{U^{s+1}} ≥ δ for 1-bounded *f*, then *f* correlates with a
polynomial phase of degree ≤ *s*. For *s* = 1 this is the Fourier statement of §2.

> **Caveat, and this is where the companion beats the talk.** The naive form of this
> conjecture is **false**: a counterexample for U⁴(𝔽₂ⁿ) was found independently by Green–Tao
> and by Lovett–Meshulam–Samorodnitsky (STOC 2008). The correct statement, proved by
> **Bergelson–Tao–Ziegler (GAFA 19 (2010), 1539–1596)** and **Tao–Ziegler (Anal. PDE 3
> (2010); Ann. Comb. 16 (2012))**, replaces "polynomial" with **non-classical polynomial** —
> the companion's word is "non-standard" — meaning any *P* with Δ_{h₁}⋯Δ_{h_s}*P* ≡ 1. When
> the characteristic exceeds *s* the two classes coincide; in low characteristic the
> non-classical class is strictly larger. From the podium Ziegler says "polynomial phase
> function" without the caveat. *(Companion, Theorem 8.3 and the discussion before it.)*

**Over ℤ (the U^{s+1}[N] norm).** If ‖*f*‖_{U^{s+1}[N]} ≥ δ for 1-bounded *f* : [N] → ℂ,
then there is an *s*-step nilmanifold *G*/Γ from a finite list depending only on (*s*, δ), a
*g* ∈ *G*, and a Lipschitz *F* with

> |𝔼_{n ∈ [N]} *f*(*n*) · conj(*F*(*gⁿ x*Γ))| ≥ *c*(*s*, δ).

**Theorem (Green–Tao–Ziegler, Ann. of Math. 176 (2012), 1231–1372; arXiv:1009.3998).** This
holds. *(Companion, Conjecture 8.1 and Theorem 8.4.)* The converse direction is the easy one
and follows from Cauchy–Schwarz.

Ziegler's slogan, verbatim:

> "If you have large U^{k+1} norm then you correlate with some *k*-th order structure. Over
> finite fields this is polynomial phases; over the integers this is nilsequences. And this
> is kind of the additive combinatorial analogue of what happens in the ergodic world."

Two footnotes worth having. Gowers' original proof of Szemerédi's theorem gave a **local**
inverse theorem: large U^k gives correlation with a degree-(*k*−1) polynomial phase on a
progression of length N^t, *t* < 1, not on all of [N]. Global structure needed nilsequences,
which is exactly the gap the ergodic theory predicted. And both inverse theorems are
**qualitative**: making them quantitative is, in the companion's words, "a major open
question".

---

## 4. The talk, rebuilt

Her order, not the companion's.

### 4.1 The frame (00:00–08:00)

Arithmetic pattern = a subset inheriting the ambient structure: a line in a variety, a
progression in ℤ. Question: given *E* ⊆ *X* of density δ, does *E* contain patterns, and how
many? Random baseline by δ-coin flip: δ³|*V*|² lines in 𝔽₃ⁿ. Guiding principle: **an
unexpected count reveals structure.** §1 above.

### 4.2 First obstruction: linear structure (08:00–15:00)

Subspaces overshoot at δ²|*V*|². Roth–Meshulam says that is the only mechanism: either the
random count, or density increment on a hyperplane. Roth in ℤ/Nℤ: either the random count,
or density increment on a progression of length ~N^{1/3}. Both branches produced by the
Fourier transform on the balanced function. Both iterate into a terminating loop. §3.2.

### 4.3 Szemerédi, and the corridor conversation (15:00–20:00)

Twenty years from Roth to Szemerédi 1975. Ziegler skips the proof — "although it was very
influential and introduced many important tools in graph theory" — because for her story
what mattered was the *statement*: Konrad Jacobs' off-topic talk at the 1975–76 Israel IAS
special year, and Furstenberg realising mid-lecture that dynamics could do it. §3.3.

### 4.4 The correspondence principle and multiple recurrence (20:00–25:00)

Sets become measure spaces, translations become iterates, patterns become multiple
recurrence. *k* = 1 is Poincaré. §3.4.

### 4.5 k = 2: the Kronecker factor is the complete obstruction (25:00–30:00)

"If my points were asymptotically independent on average, I would expect the limit to be
μ(*A*)³. If this doesn't happen, the obstruction comes from a nontrivial morphism to an
abelian dynamical system." The Kronecker factor is **characteristic** (project, then compute)
and **universal** (a factor of any other characteristic factor). If it is trivial, you get
μ(*A*)³ — the random answer. §3.6.

### 4.6 k = 3: new obstructions, and the two-level picture (30:00–36:00)

For four-term progressions, Furstenberg–Weiss in the 1980s found obstructions from **2-step
nilpotent** systems. Ziegler shows the Heisenberg example, then makes a point the slides
carried and the captions nearly lost: the picture has **two levels**, not one.

There is a natural map *G*/Γ → 𝕋², the **abelianization**, landing on the off-diagonal
entries. Four points upstairs map to *z*, *z*+*n*(α,β), *z*+2*n*(α,β), *z*+3*n*(α,β)
downstairs — a genuine progression on the torus, giving the constraints you already knew
about. **On top of that** there is an extra constraint living purely at the nilmanifold
level, invisible downstairs. That layering is the geometric content of "second order".

Then the classification for four terms:

> **Theorem (Conze–Lesigne; Furstenberg–Weiss).** The universal characteristic factor for
> four-term progressions is a **2-step pro-nilsystem** — an inverse limit of 2-step
> nilsystems. Single nilsystems are not enough.

*(Companion, Theorem 4.1.)* Ziegler is explicit from the podium that the inverse limit is
necessary; the captions render it as "nil systems is not enough, you need to take inverse
limits of those."

### 4.7 General k: Host–Kra and Ziegler (36:00–39:00)

> **Theorem (Host–Kra 2005; Ziegler 2007).** For an ergodic measure-preserving system, the
> universal *k*-characteristic factor is a **(k−1)-step pro-nilsystem**.

*(Companion, Theorem 6.1, citing Host–Kra, Ann. of Math. 161 (2005), 397–488, and Ziegler,
J. Amer. Math. Soc. 20 (2007), 53–97, the latter growing out of her 2003 Hebrew University
thesis.)*

The companion also records what this buys: an actual **limit formula** for the averages, as
an integral over a sub-nilmanifold *H*Γ^{k+1}/Γ^{k+1} of (*G*/Γ)^{k+1} where *H* is an
explicit subgroup built from the derived series *(Companion, Theorem 6.2, Ziegler 2005)*.
That is the difference between "the count is positive" and "here is the count".

Ziegler stops here to say the thing worth hearing:

> "If you take a step back and think about it, it's rather surprising that for these very
> general averages what really determines the behaviour is this very rigid structure of
> nilsystems."

Two remarks she does not make and the companion does. First, the Furstenberg–Zimmer
structure theorem already gave a tower of factors *Z*_k(*X*) that are characteristic; they
are simply **not universal** for *k* > 1, and universality is what makes classification
possible at all. Second, the proofs go through a functional equation — the **Conze–Lesigne
equation**

> σ(*z*+*b*) − σ(*z*) = *c*(*b*) + *F_b*(*z*+α) − *F_b*(*z*)

— whose solvability is where 2-step nilpotency literally appears: the condition says a
certain commutator [(α,σ),(*b*,*F_b*)] is central. *(Companion §4.)*

### 4.8 Crossing to combinatorics: the Gowers norms (39:00–44:00)

The detector, the control of linear forms, the two inverse theorems. §3.9 and §3.10.

Her framing of the crossing is worth quoting because it is the architecture of the whole
subject: the ergodic theory *predicted* the answer, and the combinatorics then had to prove
it independently. "Motivated by the results in ergodic theory that I described before, Green
and Tao conjectured that the underlying reason should be algebraic."

### 4.9 First application: counting progressions in the primes (44:00–48:00)

Green–Tao says the primes contain arbitrarily long progressions. This machinery **counts**
them:

> The number of *k*-term arithmetic progressions in a box of size *N* is asymptotically
> **σ_k · N² / (log N)^k**, with σ_k an explicit constant (an Euler product, the singular
> series).

This is a special case of Green–Tao–Ziegler's theorem on affine linear forms: for *k* affine
linear forms ψ₁,…,ψ_k in *m* variables with integer coefficients, no two affinely dependent,

> |{**x** ∈ [0,N]^m : ψ₁(**x**), …, ψ_k(**x**) all prime}| ~ 𝔖(**ψ**) · N^m / (log N)^k.

*(Companion, Theorem 1.1, from Green–Tao, Ann. of Math. 171 (2010), 1753–1850; Green–Tao,
Ann. of Math. 175 (2012), 541–566; Green–Tao–Ziegler, Ann. of Math. 176 (2012), 1231–1372.
Arithmetic progressions are the case m = 2, variables x and d.)*

Ziegler insists on a specific reading of this theorem, and it is the right one:

> "The way I want you to think of this theorem is: this tells us that the **primes are
> unstructured for this question**."

Because the primes have density 1/log N, a random set of that density would produce exactly
N²/(log N)^k progressions. There are obvious local obstructions — *x* prime makes *x*+1
almost never prime — and those are absorbed into the constant σ_k. Once you have divided
them out, the primes behave like a random set.

**The proof strategy, in her words and in three steps:**

1. An unexpected count implies a large Gowers norm.
2. A large Gowers norm implies correlation with a nilsequence (the inverse theorem).
3. So it suffices to show that the primes **do not correlate with nilsequences**.

She then flags her own oversimplification, out loud: *"it's a bit of a cheat — the whole
theory is done for positive density, not for density 1/log N which is approximately zero.
But there is a technology developed by Green and Tao that allows you to push these theorems
to this context as well."* That technology is the transference/decomposition machinery: you
write the weighted prime indicator as *g* + *h* with *g* bounded and *h* Gowers-uniform, and
run the positive-density theory on *g*. *(Companion §7 and §8, which also names the
W-trick — pre-sieving by W = Π_{p<w} p to remove the periodic contributions before you
start.)*

### 4.10 The pivot: "I could have told this story fifteen years ago" (48:00)

Explicit turn in the talk. Everything so far dates to 2012 or earlier. What follows was not
designed for this machinery.

### 4.11 The Liouville function (48:00–52:00)

> λ(*n*) = (−1)^{Ω(n)}, where Ω(*n*) is the number of prime factors of *n* **with
> multiplicity**.

Example from the podium: 12 = 2·2·3 has Ω = 3, so λ(12) = −1. It is **completely
multiplicative**: λ(*mn*) = λ(*m*)λ(*n*), so it is determined by its value −1 on each prime.

Why it matters, in two lines she gives and you should keep:

- Σ_{n≤N} λ(*n*) = *o*(N) **is equivalent to the prime number theorem**. The trivial bound is
  N, since λ = ±1; any cancellation at all is already the PNT.
- Σ_{n≤N} λ(*n*) = *O*(N^{1/2+ε}) **is equivalent to the Riemann hypothesis**. Ziegler's
  gloss: RH says the cancellation is what you would get from a **random walk**. Square-root
  cancellation, exactly as in your CLT.

So λ is the canonical object for the vague principle that *the Möbius/Liouville function
should not correlate with anything structured*. The trouble with that principle is that
"structured" is undefined. Ziegler: *"you could say, show me a sequence, I'll tell you if
it's structured."*

### 4.12 Sarnak's conjecture: a definition of "structured" (52:00–56:00)

Sarnak's 2010 proposal formalises it with **zero topological entropy**.

A **topological dynamical system** is a compact space *X* with a continuous *T* : *X* → *X*.
A sequence *arising from* the system is *a*(*n*) = *F*(*T*ⁿ*x*) for a fixed point *x* and
continuous *F*.

> **Sarnak's conjecture (2010).** For every topological dynamical system of **zero
> topological entropy**, every *x* and every continuous *F*,
>
> > (1/N) Σ_{n ≤ N} λ(*n*) *F*(*T*ⁿ*x*) = *o*(1).

**Entropy, defined the way she defines it.** Work in the sequence space {±1}^ℕ with the
left shift (drop the first coordinate). Take a closed shift-invariant subset *X*. Count
*S*_X(*k*), the number of distinct length-*k* blocks appearing in points of *X*. Topological
entropy is the exponential growth rate of *S*_X(*k*). The full shift gives log 2; a periodic
sequence gives boundedly many blocks and entropy 0. **Zero entropy = subexponential block
growth = low complexity.**

Ziegler's reaction on first seeing it, which is a useful calibration for the reader:

> "I remember seeing this conjecture in 2010, and I thought it looked great, but very
> surprising. Why would you think that something like this would be true?"

The answer: it follows from **Chowla's conjecture**, a much older and widely believed
statement about self-correlations of λ:

> For distinct integers *a*₁, …, *a*_m, (1/N) Σ_{n≤N} λ(*n*+*a*₁) ⋯ λ(*n*+*a*_m) = *o*(1).

Sarnak proved Chowla ⟹ Sarnak.

### 4.13 The trap: Sarnak forces the Liouville system to have positive entropy (56:00–59:00)

This is the prettiest self-contained argument in the talk, and it needs nothing beyond the
last two paragraphs. It gets its own box in §6.

Build the **Liouville subshift**: regard λ ∈ {±1}^ℕ as a single point, take its shift-orbit
closure *X*_λ. Let *S*_λ(*k*) be the number of length-*k* sign patterns occurring in it. Let
*f*₀ be the continuous function "read coordinate zero". Then *f*₀(*T*ⁿλ) = λ(*n*) — the
Liouville sequence exhibits *itself* as an orbit observable. But then

> Σ_{n≤N} λ(*n*) *f*₀(*T*ⁿ λ) = Σ_{n≤N} λ(*n*)² = N,

no cancellation whatsoever. So if *X*_λ had zero entropy, Sarnak's conjecture would be
false. **Hence, if Sarnak is true, the Liouville subshift has positive entropy** — its sign
patterns must grow exponentially. Chowla would say more: all 2^k patterns occur, with the
correct frequencies.

An open conjecture, applied to a system nobody chose, forces an unconditional-looking
structural prediction about the primes. That is worth sitting with.

### 4.14 Logarithmic averaging, and why it helps (59:00–61:00)

The **logarithmic** version weights the *n*-th term by 1/*n*. The trivial bound is then
log N rather than N, so the assertion becomes *o*(log N).

> **Theorem (Tao 2016).** The logarithmically averaged Chowla and Sarnak conjectures are
> **equivalent** to each other, and to the "local Gowers uniformity" of λ.
> *(T. Tao, "Equivalence of the logarithmically averaged Chowla and Sarnak conjectures",
> arXiv:1605.04628, 16 May 2016. The proof uses the entropy decrement argument together with
> the Green–Tao–Ziegler inverse theorem — this machinery, again.)*

Ziegler's caution, which is exactly right and easy to miss: the logarithmic version could be
true while the unaveraged one is false. But for the entropy application it does not matter,
because only the block-growth rate is at stake.

### 4.15 Progress, and a corollary you can feel (61:00–65:00)

> **Theorem (Frantzikinakis–Host, Ann. of Math. 187 (2018), 869–931; arXiv:1708.00677).**
> The logarithmic Sarnak conjecture holds for a large class of zero-entropy systems,
> including **all uniquely ergodic** ones. (Uniquely ergodic = exactly one invariant
> probability measure.)

What it is built on, in Ziegler's own accounting: the first half of her talk — higher-order
Fourier analysis and the nilstructure of characteristic factors — plus two genuinely new
ingredients:

- **Matomäki–Radziwiłł** (Ann. of Math. 183 (2016); arXiv:1501.04585), on multiplicative
  functions in **short intervals** — new hard data about λ, not about dynamics.
- **Tao's entropy decrement argument.**

And the corollary, by the trap of §4.13 run in reverse: if *S*_λ(*k*) grew slower than
linearly, the Liouville subshift would satisfy the theorem's hypotheses, and you would get
the same contradiction. So

> **Corollary.** *S*_λ(*k*) grows **superlinearly**.

Ziegler pauses on this, and the pause is the honest measure of the difficulty:

> "Think about how ignorant we were until, I don't know, ten years ago. We didn't know that
> the number of sign patterns even grows faster than linear."

Then her own recent work pushes it further:

> **Theorem (Matomäki, Radziwiłł, Tao, Teräväinen, Ziegler, Ann. of Math. 197 (2023),
> 739–857; arXiv:2007.15644).** *S*_λ(*k*) grows **superpolynomially** — faster than *k^A*
> for every fixed *A*.

*(The paper's own framing: it establishes higher-order uniformity of bounded multiplicative
functions in short intervals on average, extending the previously known linear-phase case to
degree-k nilsequences for every fixed k, and deduces the superpolynomial sign-pattern bound
plus an averaged form of Chowla along polynomial progressions.)*

### 4.16 The method for the sign-pattern theorem (65:00–68:00)

Ziegler walks the argument, and it is the three-step strategy of §4.9 with one new
ingredient bolted on. The point of the walk is that you should recognise every step.

Chowla predicts cancellation in Σ_n λ(*n*+*a*₁)⋯λ(*n*+*a*_m) for a **fixed** shift tuple.
That is out of reach. So relax it: put an **extra average over shifts**, letting the shift
range over an interval of length N^θ for a small fixed θ. Now:

1. If those sums are large, then many **local Gowers norms at scale N^θ** are large.
2. Throw higher-order Fourier analysis at them: many correlations, on many short intervals,
   with nilsequences.
3. **New ingredient required.** You now need input about λ *as a multiplicative function* to
   contradict step 2. The base case is Matomäki–Radziwiłł on short intervals.

**How far is this from the real thing?** She is precise about the gap, and this is the most
useful minute of the last third:

> **Theorem (Walsh; M. N. Walsh, "Stability under scaling in the local phases of
> multiplicative functions", arXiv:2310.07873, 11 October 2023; Invent. Math. 2025).**
> **Assuming GRH**, the Fourier uniformity conjecture (the *m* = 2, linear-phase case) holds
> for intervals of length at least (log X)^{ψ(X)}, with ψ(X) → ∞ arbitrarily slowly.

*(From the podium Ziegler says "conditioned on the Riemann hypothesis … reduce to log n to
some large power." The paper says GRH, and (log X)^{ψ(X)} with ψ growing arbitrarily slowly,
which is slightly stronger than "a large power". I am quoting the paper.)*

And the target: pushing the interval length down to (log X)^ε for **every** ε > 0, and doing
it for **every** *m* rather than only *m* = 2, would give the logarithmic Chowla conjecture
outright. Doing it for every *m* is precisely the step that needs higher-order Fourier
analysis in place of ordinary Fourier analysis — nilsequences instead of linear phases.

> "So we're almost there — except the hypothesis, and the gap."

Two named obstacles, neither hidden.

### 4.17 The unexpected applications (68:00–70:00)

Three, named quickly from the podium as evidence that the technology has escaped its
original purpose:

- **Hilbert's tenth problem** — decidability of Diophantine equations. *(Koymans–Pagano,
  "Hilbert's tenth problem via additive combinatorics", arXiv:2412.01768, give a negative
  answer for all infinite finitely generated rings, combining additive combinatorics with
  2-descent on elliptic curves with full rational 2-torsion.)*
- **Infinitely many rank-two elliptic curves over ℚ** — *(Zywina, "There are infinitely many
  elliptic curves over the rationals of rank 2", arXiv:2502.01957. He proves a family all
  has rank exactly 2 by 2-descent, and gets infinitude by applying the **Tao–Ziegler**
  polynomial Szemerédi theorem for primes — that is, her own theorem, Acta Math. 201 (2008),
  213–305.)*
- **PTE** — from context, the Prouhet–Tarry–Escott problem.
  > *[Gap: she names PTE in three words and moves on. I could not identify the paper, and I
  > will not guess one. Impact: low — it is one item in a list of three, and the other two
  > are verified.]*

### 4.18 The multidimensional frontier (70:00–end)

Everything above is one-dimensional: an abelian group, patterns inside it. The proposal for
the next decade is **G^m**.

The simplest open example she gives is the **square** in *G*²: the four points
(*x*,*y*), (*x*+*d*,*y*), (*x*,*y*+*d*), (*x*+*d*,*y*+*d*). Corners and some other
configurations are understood; *"even the square we don't know."*

> *[My reading, marked as such: bare existence of squares in a dense subset of ℤ² is not the
> open part — the multidimensional Szemerédi theorem of Furstenberg–Katznelson already gives
> a homothetic copy of any finite configuration. What is open, and what the talk's whole
> framing points at, is the **inverse theory**: which structures explain an unexpected
> count. She does not say this sentence; I am supplying the reading because without it the
> claim sounds wrong.]*

The tools are the expected deformations:

- **Directional Gowers norms** — differentiate along various subgroups instead of along all
  of *G*. Then ask the inverse question: large directional norm ⟹ what structure?
- **Dynamical cubes** — the same question with two commuting transformations *T* and *S*,
  studying limits of averages along *T*ⁿ and *S*ⁿ.
- And, she notes, "today we know many times to go back and forth between these questions
  using versions of the correspondence principle." The bridge of §3.4 is now routine
  infrastructure in both directions.

Her closing sentence is the talk's thesis restated at one level of generality up: *"in
several dimensions, what structures will appear, and where will they lead? This is for us to
see in the next ICMs."*

---

## 5. The one argument

Strip the vocabulary and one derivation carries the talk, in two settings. Here it is with
every symbol defined.

**Setup.** *E* ⊆ [N] with balanced function *f* = 1_E − δ, or λ the Liouville function.
AP_k(*f*) = 𝔼_{x,d ∈ [N]} *f*(*x*)*f*(*x*+*d*)⋯*f*(*x*+*kd*), the normalised count of
(*k*+1)-term progressions. ‖·‖_{U^k[N]} the Gowers norm of §3.9. A *s*-step nilsequence is
*n* ↦ *F*(*aⁿx*Γ) on an *s*-step nilmanifold *G*/Γ.

**Step 1 — a wrong count forces a large norm.**

> |AP_k(*f*) − AP_k(*g*)| ≪_k ‖*f* − *g*‖_{U^k[N]}

with the generalized von Neumann inequality behind it (§3.9). Contrapositive: if the count
deviates from the random prediction by more than *c*(δ), then ‖*f*‖_{U^k[N]} ≫ *c*(δ)^{O(1)}.
This step is Cauchy–Schwarz, repeated *k* times. Nothing deep, and it is why the norm was
defined that way in the first place.

**Step 2 — a large norm forces algebraic structure (the inverse theorem).**

> ‖*f*‖_{U^{s+1}[N]} ≥ δ ⟹ |𝔼_{n∈[N]} *f*(*n*) conj(*F*(*gⁿx*Γ))| ≥ *c*(*s*,δ)
> for some *s*-step nilsequence of complexity bounded in terms of (*s*, δ).

**Green–Tao–Ziegler, Ann. of Math. 176 (2012).** Over 𝔽_pⁿ the corresponding statement is
Bergelson–Tao–Ziegler / Tao–Ziegler, with *non-classical* polynomial phases. This step is the
hard one: it is where fifteen years of work sits, and it is qualitative — no effective
bounds.

**Step 3 — the arithmetic input: the object of interest does not correlate.**

> For the primes: after the W-trick, 𝔼(1̃_{W,b,P}(*n*) − 1) *F*(*gⁿx*Γ) = *o*(1) for every
> bounded-complexity nilsequence. **Green–Tao, Ann. of Math. 175 (2012), 541–566** ("the
> Möbius function is strongly orthogonal to nilsequences").
>
> For λ in short intervals: the corresponding non-correlation statement, at scale N^θ,
> **Matomäki–Radziwiłł–Tao–Teräväinen–Ziegler, Ann. of Math. 197 (2023)**.

**Conclusion.** Steps 1 and 3 contradict each other unless the count is the random one. So
the count is the random one, and you have an asymptotic:

> **primes in [1,N] contain ~ σ_k N²/(log N)^k arithmetic progressions of length k**
>
> **λ has no unexpected local correlations at scale N^θ, hence *S*_λ(*k*) grows
> superpolynomially**

**The shape, which is the part to remember.** The argument is a **three-link chain**:

> *statistical anomaly* → *analytic certificate* → *algebraic structure* → *contradiction
> with an arithmetic fact*

Link 1 is soft (Cauchy–Schwarz). Link 2 is the inverse theorem and is where all the
mathematics lives. Link 3 is arithmetic input specific to the object you care about. Change
the object — primes, Liouville, polynomial progressions, Gaussian primes — and **only link 3
changes.** That modularity is why one machine produced results in 2012 and 2023 for
questions that look nothing alike, and it is the reason Ziegler could say the applications
were not designed for.

**Honesty check.** Every step above is a theorem. What is *not* known: quantitative forms of
step 2; step 3 for λ at intervals shorter than N^θ (that is the Walsh/Pilatte frontier of
§4.16); and anything at all in the multidimensional setting of §4.18.

---

## 6. The boxed derivation: Sarnak ⟹ the Liouville sequence is complex

This one is fully restorable from the transcript alone, needs nothing from §5, and is the
best short argument in the talk.

> **Claim.** If Sarnak's conjecture holds, then the Liouville subshift *X*_λ has **positive**
> topological entropy: the number *S*_λ(*k*) of length-*k* sign patterns of λ grows
> exponentially in *k*.
>
> **Proof.** Regard λ as a point of the compact space {±1}^ℕ with the left shift *T*. Let
> *X*_λ be the closure of {*T*ⁿλ : *n* ≥ 0}. It is compact, shift-invariant, and *T* is
> continuous, so (*X*_λ, *T*) is a topological dynamical system.
>
> Let *f*₀ : {±1}^ℕ → ℝ read off the zeroth coordinate. It is continuous. Then
> *f*₀(*T*ⁿλ) = λ(*n*) up to an index shift.
>
> Suppose *X*_λ had zero topological entropy. Sarnak's conjecture would apply to the point λ
> and the function *f*₀, giving
>
> > (1/N) Σ_{n≤N} λ(*n*) *f*₀(*T*ⁿλ) = *o*(1).
>
> But λ(*n*)² = 1 for every *n*, so that average is exactly 1. Contradiction. Hence *X*_λ
> has positive entropy, i.e. lim (1/*k*) log *S*_λ(*k*) > 0. ∎

Two remarks Ziegler makes and you should keep.

**Chowla says more.** It would give all 2^k patterns, each with the correct frequency — the
Liouville sequence would look exactly like a fair coin at every finite window.

**Unconditionally, this is now a theorem twice over, in weaker form.** Frantzikinakis–Host
give superlinear growth; Matomäki–Radziwiłł–Tao–Teräväinen–Ziegler give superpolynomial. The
argument in both cases is the same contradiction run against a *proved* fragment of Sarnak
rather than the full conjecture: assume slow growth, deduce that *X*_λ satisfies the
hypotheses of the theorem you have, apply it, and hit λ² = 1 again.

---

## 7. Do this by hand

Two exercises. The first lands exactly on the anchor. The second shows you, by arithmetic
you can do in your head, why the anchor's tool breaks.

### 7.1 The U² norm is the Fourier transform (25 minutes, pen)

Work on ℤ/Nℤ. Convention: e(*t*) = e^{2πi t}, *f̂*(*r*) = 𝔼_{x} *f*(*x*) e(−*xr*/N), so
*f*(*x*) = Σ_r *f̂*(*r*) e(*xr*/N) and Parseval reads Σ_r |*f̂*(*r*)|² = 𝔼_x |*f*(*x*)|².

1. Write out ‖*f*‖⁴_{U²} from Definition §3.9 as a four-fold average, and show
   ‖*f*‖⁴_{U²} = Σ_r |*f̂*(*r*)|⁴.
2. Deduce that for a 1-bounded *f*, ‖*f*‖_{U²} ≥ η implies ‖*f̂*‖_∞ ≥ η².
3. Show 𝔼_{x,d} *f*(*x*)*g*(*x*+*d*)*h*(*x*+2*d*) = Σ_r *f̂*(*r*) *ĝ*(−2*r*) *ĥ*(*r*).
4. Let *E* ⊆ ℤ/Nℤ have density δ and put *f* = 1_E − δ. Show that the 3-term progression
   count of 1_E differs from δ³ by at most 7‖*f̂*‖_∞ · δ, and conclude the quantitative form
   of the first branch of Roth's dichotomy.
5. Now try to run step 3 for **four**-term progressions. Where exactly does it fail?

<details>
<summary>Solutions</summary>

**(1)** By definition
‖*f*‖⁴_{U²} = 𝔼_{x,h₁,h₂} *f*(*x*) conj(*f*(*x*+*h*₁)) conj(*f*(*x*+*h*₂)) *f*(*x*+*h*₁+*h*₂).
Substitute *f*(*x*) = Σ_a *f̂*(*a*) e(*ax*/N) in all four slots. The *x*-average forces
*a* − *b* − *c* + *d* ≡ 0; the *h*₁-average forces *b* = *d*; the *h*₂-average forces
*c* = *d*. Hence *a* = *b* = *c* = *d* and the whole thing collapses to
Σ_a *f̂*(*a*) conj(*f̂*(*a*)) conj(*f̂*(*a*)) *f̂*(*a*) = Σ_a |*f̂*(*a*)|⁴. ∎

**(2)** Σ_r |*f̂*(*r*)|⁴ ≤ (sup_r |*f̂*(*r*)|)² · Σ_r |*f̂*(*r*)|² = ‖*f̂*‖²_∞ · 𝔼|*f*|² by
Parseval. For 1-bounded *f* the last factor is ≤ 1. So η⁴ ≤ ‖*f*‖⁴_{U²} ≤ ‖*f̂*‖²_∞, giving
‖*f̂*‖_∞ ≥ η². This is the companion's inequality chain ‖*f*‖⁴_{U²} = ‖*f̂*‖⁴_4 ≤
‖*f̂*‖²_∞‖*f̂*‖²_2 written out. ∎

**(3)** Expand all three in characters. The *x*-average forces *a*+*b*+*c* ≡ 0; the
*d*-average forces *b*+2*c* ≡ 0. Solve: *b* = −2*c*, *a* = −*b*−*c* = *c*. So the sum is
Σ_c *f̂*(*c*) *ĝ*(−2*c*) *ĥ*(*c*). ∎

**(4)** Write 1_E = δ + *f* and expand the trilinear form into 2³ = 8 terms. The all-δ term
is δ³. The three terms with *f* in **exactly one** slot vanish, since the other two slots are
constants and 𝔼*f* = 0. Each remaining term has *f* in at least two slots; apply (3) with
*f* in the first and third slots and bound
|Σ_r *f̂*(*r*)*ĝ*(−2*r*)*ĥ*(*r*)| ≤ ‖*f̂*‖_∞ Σ_r |*f̂*(*r*)||*ĥ*(*r*)| ≤ ‖*f̂*‖_∞ ‖*f*‖₂‖*h*‖₂
by Cauchy–Schwarz and Parseval, with ‖*f*‖₂² = δ(1−δ) ≤ δ. Summing the at most 7 nonzero
mixed terms gives the stated bound. Hence a deviation of *c*(δ) from δ³ forces
‖*f̂*‖_∞ ≫ *c*(δ)/δ: **a large Fourier coefficient**. Feed that into equidistribution of
{*xr*/N} and you get the density increment on a progression of length ~N^{1/3}.

**(5)** Repeat the character expansion for 𝔼_{x,d} *f*₁(*x*)*f*₂(*x*+*d*)*f*₃(*x*+2*d*)*f*₄(*x*+3*d*).
The two averages give **two** linear constraints on **four** frequencies, so the surviving
set is a **two-parameter** family, not a one-parameter one. The identity becomes a double
sum, and no bound on a single sup of |*f̂*| controls a double sum. There is no diagonal to
collapse to. That is the failure, and §7.2 turns it from "the proof does not work" into "the
statement is false".

</details>

### 7.2 The skew shift kills linear Fourier analysis (25 minutes, pen)

On the 2-torus 𝕋² (write it additively, coordinates mod 1), let

> *T*(*z*, *w*) = (*z* + α, *w* + 2*z* + α),  α irrational.

1. Prove by induction that *T*ⁿ(*z*,*w*) = (*z* + *n*α, *w* + 2*nz* + *n*²α).
2. Verify *y* − 3*T*ⁿ*y* + 3*T*^{2n}*y* − *T*^{3n}*y* = 0 for all *n* and all *y*. Say which
   classical operator this is and why the answer is zero.
3. Let φ(*z*,*w*) = e(*w*). Show φ(*Ty*) = ψ(*y*)φ(*y*) with ψ an ordinary eigenfunction, and
   give ψ's eigenvalue.
4. Show that φ and all its nonzero powers have **zero** projection onto the Kronecker factor
   of this system. (Take as given that the Kronecker factor is the base circle rotation
   *z* ↦ *z*+α.)
5. Exhibit four functions *f*₀,…,*f*₃, each 1-bounded, each with vanishing Kronecker
   projection, whose four-term average
   (1/N)Σ_n ∫ *f*₀(*y*)*f*₁(*T*ⁿ*y*)*f*₂(*T*^{2n}*y*)*f*₃(*T*^{3n}*y*) d*y* equals 1, not 0.
   Say in one sentence what this proves about the U² norm.

<details>
<summary>Solutions</summary>

**(1)** *n* = 1: the formula gives (*z*+α, *w*+2*z*+α) ✓. Inductive step:
*T*(*z*+*n*α, *w*+2*nz*+*n*²α) = (*z*+(*n*+1)α, *w*+2*nz*+*n*²α + 2(*z*+*n*α) + α)
= (*z*+(*n*+1)α, *w* + 2(*n*+1)*z* + (*n*²+2*n*+1)α) ✓. ∎

**(2)** Second coordinate: 3−3+1 = 1 for *w*; for *z*, 6−12+6 = 0; for α,
3·1 − 3·4 + 9 = 0. First coordinate: 3−3+1 = 1 for *z*, and 3−6+3 = 0 for *n*α. So the
combination returns *y* exactly.

The operator is the **third finite difference** Δ³ with weights (1, −3, 3, −1) applied along
the orbit at step *n*. It vanishes because every coordinate of *T*^{jn}*y* is a **quadratic
polynomial in j**, and the third difference annihilates polynomials of degree ≤ 2. That is
the whole content of "second-order structure". ∎

**(3)** φ(*Ty*) = e(*w* + 2*z* + α) = e(2*z*+α) · e(*w*) = ψ(*y*)φ(*y*) with
ψ(*z*,*w*) = e(2*z*+α). And ψ(*Ty*) = e(2(*z*+α)+α) = e(2α) ψ(*y*), so ψ is an ordinary
eigenfunction with eigenvalue e(2α). ∎

**(4)** The Kronecker factor is functions of *z* alone; the projection is the conditional
expectation, i.e. integration over *w*. For *k* ≠ 0, ∫₀¹ e(*kw*) d*w* = 0. So φ^k projects
to 0 for every *k* ≠ 0. ∎

**(5)** From (2), the same weights (1, −3, 3, −1) applied to the multiplicative
eigenfunction give φ(*y*) = φ³(*T*ⁿ*y*) φ^{−3}(*T*^{2n}*y*) φ(*T*^{3n}*y*). Take
*f*₀ = conj(φ), *f*₁ = φ³, *f*₂ = conj(φ)³, *f*₃ = φ. Then the integrand is
conj(φ(*y*)) · φ³(*T*ⁿ*y*) φ^{−3}(*T*^{2n}*y*) φ(*T*^{3n}*y*) = conj(φ(*y*)) · φ(*y*) = 1
pointwise, for every *n*. So the average is 1.

**What it proves.** Each *f*_i is a 1-bounded function invisible to first-order analysis —
zero Kronecker projection, and in the combinatorial mirror, zero Fourier coefficients — yet
the four-term correlation is as far from the random value 0 as it can possibly be. **A small
U² norm does not control four-term progressions.** You need a norm that survives one more
differentiation, and that is U³. This is the exact point where Ziegler's hierarchy becomes
necessary rather than decorative. *(The identity, the eigenfunction, and the orthogonality
are all in the companion, §4; the induction in (1) and the arithmetic in (2) are mine, and
you have just checked them.)*

</details>

---

## 8. What is actually useful to you

The number theory will not transfer. Four things will, and one of them is a control
structure you already write.

### 8.1 The density-increment loop is a termination proof, and you write these

Read §3.2 again as pseudocode:

```
loop:
    if count(E) ≈ random_count(E):   return SUCCESS
    else:                            E ← restrict(E)   # density(E) += c(δ)
```

The proof of termination is that the potential (density) is monotone increasing by a
**definite amount** and **bounded above** by 1. Therefore the loop runs at most 1/*c*(δ)
times. That is the entire argument, and it is exactly the discipline missing from most agent
loops: a retry loop that "tries again with more context" has no monotone bounded potential,
so it has no termination proof, so it runs until a timeout kills it.

The transferable design rule: **when you build a loop that reacts to failure by narrowing
scope, name the potential it improves and its bound.** If you cannot name them, the loop is
a while-true with extra steps. Roth's argument is a hundred-line proof whose entire content
is that the potential exists.

Note also *what* the dichotomy buys: it converts "I failed" into "I made measurable
progress". Every iteration of the loop is either a success or a *strictly better starting
position*. That is a much stronger contract than "retry".

### 8.2 One detector, a whole family of failures

The Gowers norm is not a test for arithmetic progressions. It is a single scalar whose
largeness certifies deviation for **every** system of affine linear forms of bounded
complexity at once (§3.9, the generalized von Neumann inequality). One quantity, and the
class of patterns it controls is characterized rather than enumerated.

Contrast the usual eval design: one metric per behaviour, twenty metrics, no statement
relating them. The Gowers design says — find the quantity such that *bounding it bounds
everything in a stated class*, and then prove the class. The proof obligation is real work;
the payoff is that you stop adding metrics.

The corollary matters too: when your detector *does* fire, you want it to tell you **what**
went wrong, not merely **that** it did. That is the inverse theorem, and it is the expensive
half. A norm without an inverse theorem is an alarm without a diagnosis.

### 8.3 The hierarchy move: when the tool is blind, go up an order — do not patch

The instinctive response to "Fourier analysis misses quadratic patterns" is to add epicycles
to Fourier analysis. What actually worked was to identify the **exact structural reason** for
the blindness (the trilinear form diagonalizes; the quadrilinear one does not), and then
build a **new object at the next order** — U³ from U², nilsystems from group rotations,
nilsequences from characters — with the old theory sitting inside as the bottom rung.

The tell that you are in this situation: your tool fails on a class of inputs you can
**characterize**, not merely enumerate. If you can characterize it, the failure is structural
and deserves a new level, not a patch. If you can only enumerate it, you have a bug list.

Everything in this talk is one deformation of the rung below it. That is what makes the
hierarchy learnable at all, and it is a design property, not an accident: each new level was
constructed so the old one was its *s* = 1 case.

### 8.4 A correspondence principle is a change of category to get better theorems

Furstenberg's move (§3.4) is: the objects on side A admit no structure theory; the objects on
side B do; find a functor. The set *E* was arbitrary and so is *A*, but *A* sits in a
category where you can prove decomposition theorems, and *E* does not.

The operational version, for your work: when a property is stated over an object with no
useful invariants, look for a faithful translation into a category that *has* invariants,
even if the translation loses information — as long as it preserves the property you care
about. The correspondence principle loses almost everything about *E*; it preserves exactly
the pattern-containment statements, which is all that was needed.

Ziegler's closing remark on this is the mature version: by now the field moves "back and
forth between these questions using versions of the correspondence principle" routinely, in
**both** directions. A translation that only runs one way is a lossy export; one that runs
both ways is an equivalence you can compute in.

### 8.5 And the meta-observation she makes explicitly

She spends the last five minutes on the fact that this machinery, built to count arithmetic
progressions, produced results on Hilbert's tenth problem, elliptic curve ranks, and the sign
patterns of the Liouville function — *"applications this was not designed for."*

The structural reason, from §5: the argument is a chain in which only **link 3** is
domain-specific. Links 1 and 2 are a general-purpose engine converting statistical anomalies
into algebraic structure. New application = new arithmetic input for link 3, everything else
reused.

If you are building tooling that you want to outlive its first use case, that is the
factorization to aim at: a generic core with exactly one clearly-marked slot for
domain-specific input. It is also a decent test of whether you have understood your own
system — can you say which link is which?

---

## 9. Where to read next

Ordered. The first is by far the best entry point.

1. **Ziegler, *Linear equations in primes and dynamics of nilmanifolds*.**
   [arXiv:1404.0775](https://arxiv.org/abs/1404.0775) — her ICM 2014 survey, 23 pages, and
   the companion for this tutorial. It covers §§3.1–3.10 and §4.1–4.9 with all the formulas,
   including the skew-shift computation, the Heisenberg nilsystem, and both inverse theorems.
   Read it with this document open; it stops in 2014.
2. **Matomäki, Radziwiłł, Tao, Teräväinen, Ziegler, *Higher uniformity of bounded
   multiplicative functions in short intervals on average*.**
   [arXiv:2007.15644](https://arxiv.org/abs/2007.15644), Ann. of Math. 197 (2023), 739–857 —
   the last third of the talk. The introduction alone is worth it: it states the local
   uniformity conjecture, the relation to Chowla and Sarnak, and the superpolynomial
   sign-pattern corollary.
3. **Tao, *Higher order Fourier analysis*.** AMS Graduate Studies in Mathematics 142, 2012,
   available free from Tao's blog — the textbook treatment of §§3.9–3.10, from a 2010
   graduate course. This is the one to read if you want to be able to *use* the machinery
   rather than follow it.

If you want the conceptual half rather than the analytic half: Frantzikinakis and Host,
*The logarithmic Sarnak conjecture for ergodic weights*,
[arXiv:1708.00677](https://arxiv.org/abs/1708.00677), Ann. of Math. 187 (2018), 869–931.

---

## 10. Self-test

<details>
<summary>1. State the guiding principle of the talk in one sentence, and give the two numbers that make it concrete.</summary>

An unexpected count of arithmetic patterns in a set reveals structure in that set. Concretely
in a vector space *V* over 𝔽₃: a random set of density δ contains about δ³|*V*|² lines; a
**subspace** of density δ contains about δ²|*V*|², because if *x* and *x*+*d* are in it then
*x*+2*d* automatically is. The Roth–Meshulam dichotomy says that mechanism — increased
density on a hyperplane — is the *only* one.
</details>

<details>
<summary>2. What is the balanced function, and why is it the right object?</summary>

*f* = 1_E − δ, which has mean zero. Every pattern count is a multilinear form in
1_E = δ + *f*; expanding, the pure-δ term is the random prediction and every other term
contains at least one *f*. The terms with exactly one *f* vanish because 𝔼*f* = 0. So
"unexpected count" is precisely "some multilinear form in the balanced function is large".
</details>

<details>
<summary>3. In what precise sense is the U² norm the Fourier transform, and what breaks at U³?</summary>

‖*f*‖⁴_{U²} = Σ_r |*f̂*(*r*)|⁴, and by ‖*f̂*‖⁴_4 ≤ ‖*f̂*‖²_∞‖*f̂*‖²_2 plus Parseval, a
1-bounded *f* with ‖*f*‖_{U²} ≥ η has a Fourier coefficient of size ≥ η². Three-term
progression counts are controlled because the trilinear form diagonalizes to a **single**
sum Σ_r *f̂*(*r*)*ĝ*(−2*r*)*ĥ*(*r*). For four terms the character expansion leaves a
**two-parameter** family of surviving frequencies, so no bound on a single Fourier
coefficient suffices — and the skew shift gives a function with vanishing first-order content
and a maximally wrong four-term count. You need a norm that survives one more
differentiation.
</details>

<details>
<summary>4. State the Furstenberg correspondence principle and give the three-line dictionary.</summary>

For *E* ⊆ ℕ of positive upper density there is a measure-preserving system (*X*,ℬ,μ,*T*) and
*A* with μ(*A*) > 0 such that μ(*A* ∩ *T*^{−n₁}*A* ∩ … ∩ *T*^{−n_k}*A*) > 0 implies
d̄(*E* ∩ (*E*−*n*₁) ∩ … ∩ (*E*−*n*_k)) > 0. Dictionary: positive density ↔ positive measure;
translation by *n* ↔ *T*ⁿ; a pattern *x*, *x*+*n*, …, *x*+*kn* in *E* ↔ multiple recurrence
to *A* at times *n*, 2*n*, …, *kn*. The payoff is that measure-preserving systems admit
structure theorems and arbitrary sets of integers do not.
</details>

<details>
<summary>5. What is a characteristic factor, and why does universality matter?</summary>

A factor π : *X* → *Y* is *k*-characteristic if the multiple average with *k*+1 functions is
asymptotically unchanged when you project all functions to *Y* and compute there — a
compression with a correctness guarantee. *X* itself is always characteristic, so the content
is finding the smallest. Universality (being a factor of every characteristic factor) makes
it canonical and therefore classifiable: Furstenberg's tower *Z*_k(*X*) is characteristic but
not universal for *k* > 1, which is why classification had to wait.
</details>

<details>
<summary>6. Give the classification of universal characteristic factors, with the convention.</summary>

Convention: (*k*+1)-term progressions ↔ the average with *k*+1 functions ↔ the U^k norm ↔
(*k*−1)-step nilsystems. Then: *k* = 2 (three-term) is the **Kronecker factor**, a compact
abelian group rotation, i.e. 1-step — Furstenberg. *k* = 3 (four-term) is a **2-step
pro-nilsystem** — Conze–Lesigne and Furstenberg–Weiss; single nilsystems do not suffice, you
need inverse limits. General *k* is a **(k−1)-step pro-nilsystem** — Host–Kra (2005) and
Ziegler (2007).
</details>

<details>
<summary>7. State both inverse theorems, and the caveat the talk omits.</summary>

Over ℤ: if ‖*f*‖_{U^{s+1}[N]} ≥ δ for 1-bounded *f*, then *f* correlates (at level *c*(*s*,δ))
with an *s*-step **nilsequence** *n* ↦ *F*(*gⁿx*Γ) of bounded complexity — Green–Tao–Ziegler,
Ann. of Math. 176 (2012). Over 𝔽_pⁿ: correlation with a polynomial phase of degree ≤ *s*.
**Caveat:** the naive finite-field statement is *false* — a counterexample for U⁴(𝔽₂ⁿ) is due
independently to Green–Tao and to Lovett–Meshulam–Samorodnitsky. The correct statement uses
**non-classical** polynomials (Bergelson–Tao–Ziegler; Tao–Ziegler), which coincide with
ordinary ones only when the characteristic exceeds *s*. Ziegler says "polynomial phase" from
the podium without the caveat; the companion's Theorem 8.3 has it.
</details>

<details>
<summary>8. Give the three-step strategy for counting progressions in the primes, and say which step is domain-specific.</summary>

(1) An unexpected count forces a large Gowers norm — generalized von Neumann, i.e. repeated
Cauchy–Schwarz. (2) A large Gowers norm forces correlation with a nilsequence — the inverse
theorem, where all the difficulty lives. (3) Show the object does **not** correlate with
nilsequences — for the primes this is Green–Tao's "the Möbius function is strongly orthogonal
to nilsequences", after the W-trick removes periodic obstructions. Only step 3 is
domain-specific; that is why the same engine later produced the Liouville sign-pattern
theorem. Result: ~σ_k N²/(log N)^k progressions of length *k* in [1,N], which says the primes
are *unstructured* for this question.
</details>

<details>
<summary>9. Why does Sarnak's conjecture force the Liouville sequence to be complex?</summary>

Take the orbit closure *X*_λ of λ inside {±1}^ℕ under the shift, and the continuous function
*f*₀ reading coordinate zero, so *f*₀(*T*ⁿλ) = λ(*n*). If *X*_λ had zero topological entropy,
Sarnak would give (1/N)Σ λ(*n*)*f*₀(*T*ⁿλ) = *o*(1); but that sum is Σ λ(*n*)² = N. So
Sarnak implies *X*_λ has positive entropy — sign patterns growing exponentially. Chowla would
give all 2^k patterns with correct frequencies. Unconditionally: superlinear growth
(Frantzikinakis–Host 2018), improved to superpolynomial (Matomäki–Radziwiłł–Tao–Teräväinen–Ziegler
2023).
</details>

<details>
<summary>10. What exactly separates the current results from the logarithmic Chowla conjecture?</summary>

Two gaps. **Interval length:** the sign-pattern results work with an extra average over
shifts in an interval of length N^θ for fixed θ > 0; you need to push down to (log X)^ε for
every ε > 0. **Order:** Walsh gets close to the target length — under **GRH**, intervals of
length (log X)^{ψ(X)} with ψ → ∞ arbitrarily slowly — but only in the *m* = 2, linear-phase
case. Doing it for every *m* is what requires higher-order Fourier analysis, nilsequences in
place of linear phases. Both together would give logarithmic Chowla, hence logarithmic Sarnak
by Tao's 2016 equivalence. Ziegler: "we're almost there, except the hypothesis and the gap."
</details>

<details>
<summary>11. What is the multidimensional frontier, and what is the simplest open case?</summary>

Patterns in *G*^m rather than *G*. The simplest example she names is the **square** in *G*²:
(*x*,*y*), (*x*+*d*,*y*), (*x*,*y*+*d*), (*x*+*d*,*y*+*d*). Corners and some other
configurations are understood; the square is not. The tools are **directional Gowers norms**
(differentiate along subgroups rather than the whole group) with their own inverse question,
and, on the dynamical side, **cubes** for two commuting transformations *T* and *S* — with
correspondence principles now moving results in both directions.
</details>

---

## 11. Note on the tutorial process

**Difficulty against reputation: matched, roughly.** Ziegler is known for exactly this —
higher-order Fourier analysis, the inverse theorem, linear equations in primes — and the talk
is that subject, delivered at survey level with the recent Liouville work appended. Rule 1
did not fire. What the transcript *did* settle is that the difficulty is a 3 and not a 4: the
talk contains no object that cannot be reached by deforming something in a standard graduate
analysis or probability course, and she consistently chose the concrete illustration (the
δ²|*V*|² subspace count, the two-point system for the even numbers, λ(12) = −1) over the
general statement.

**Companion status.** No ICM 2026 proceedings paper exists, and I looked for one. The
companion is her **ICM 2014 sectional survey**, arXiv:1404.0775 (3 April 2014), clearly
labelled as such throughout and never presented as the proceedings paper. It is unusually
good for this purpose because it tracks the talk's first two-thirds in order. It **does not
cover** the Chowla/Sarnak/Liouville third, which is 2016–2023 material; that section is
restored from primary papers, each cited by name and arXiv number at the point of use. Her
2013 EMS Lecture Series notes are older than the companion and cover the same ground, so I
did not use them. **arXiv:2512.00697** ("Polynomial bounds for Birch's theorem", Lampert–
Snowden–Ziegler) is recent work of hers but the talk never touches it, so it does not appear
above.

**She does not name a survey from the podium.** I scanned for it, per the usual heuristic —
she cites collaborators by name repeatedly but never a paper title or journal. So the
companion came from search, not from the talk.

**Name corrections.** Auto-captions destroyed almost every proper noun. Each correction below
is verified against the companion, a primary paper, or a search; the two I could not verify
are listed separately.

| Caption | Correct | Source |
|---|---|---|
| "Tamar Ziggler" | **Tamar Ziegler** | speaker |
| "Hail Fenberg", "fenberg", "first shows" | **Hillel Furstenberg** | companion, acknowledgements; her thesis advisor |
| "sami", "sarity", "seed theorem" | **Szemerédi**, Szemerédi's theorem | companion [44] |
| "Roth Mishulan dichotomy" | **Roth–Meshulam** | R. Meshulam, JCTA 71 (1995), 168–172 |
| "Benji Vice", "advice" | **Benjamin Weiss** (Furstenberg–Weiss) | companion [16] |
| "Izzy Katenerstone" | **Yitzhak Katznelson** | search; 1975–76 Israel IAS organiser |
| "Conrad Jacobs" | **Konrad Jacobs** | search; German ergodic theorist |
| "chronicer factor", "chronograph factor" | **Kronecker factor** | companion §3 |
| "kwansine" | **Conze–Lesigne** | companion [10,11,12], Theorem 4.1 |
| "host Cryan myself" | **Host, Kra and Ziegler** | companion Theorem 6.1 |
| "gow's norms", "gowowers" | **Gowers norms** | companion Definition 5.1 |
| "green and conjecture" | **Green and Tao conjectured** | companion Conjecture 8.1 |
| "childless conjecture", "trialless", "chala", "cha" | **Chowla** | Tao arXiv:1605.04628 |
| "sirenx", "sarnac", "sx conjecture", "song conjecture" | **Sarnak** | Tao arXiv:1605.04628 |
| "Leoville", "leavville" | **Liouville** | standard |
| "franchikinakis and host" | **Frantzikinakis and Host** | arXiv:1708.00677 |
| "Matumaki Razil", "mataki radi" | **Matomäki and Radziwiłł** | arXiv:1501.04585 |
| "Terodina" | **Teräväinen** | arXiv:2007.15644 |
| "toao", "tow", "tao" | **Tao** | arXiv:1605.04628, 2007.15644 |
| "Walsh" | **Miguel N. Walsh** | arXiv:2310.07873 |
| "reman hypothesis" | **Riemann hypothesis** | standard |
| "ponare", "panker recurrence" | **Poincaré recurrence** | companion §3 |
| "diapanta equations" | **Diophantine equations** | context |
| "Jordi Williamson" | **Geordie Williamson** | search; ICM 2026 Structure Committee |
| "erotic / argotic / orotic theory" | **ergodic theory** | throughout |
| "aelion", "abilionization" | **abelian**, **abelianization** | companion §4 |
| "foyer / 4year / fyear / fa analysis" | **Fourier analysis** | throughout |
| "nil po twostep nil potent le group" | **2-step nilpotent Lie group** | companion §4 |
| "Erdor Prize" | **Erdős Prize** (Israel Mathematical Union, 2011) | search |

**Could not verify — not guessed.** Two of the three slide-advancing volunteers Ziegler
thanks at the start: the captions give **"Cecile Gashon"** and **"Danny Castle"**. The third
is Geordie Williamson, confirmed. I found no reliable match for the other two and have
deliberately not guessed; plausible-looking guesses were available and would have been
exactly the failure mode the brief warns against. Impact: nil, they are acknowledgements.

**Substantive caption issues corrected in the text, not just spellings.** Four:

1. **The indexing convention drifts.** At one point she says "let's start with the case
   *k* = 4 … for four-term progressions"; elsewhere the same talk uses "*k*+1-term
   progressions ↔ *k*−1 step nilsystems", which requires *k* = 3 for four terms. I fixed a
   single convention in §3.5 and used it throughout, and flagged the drift here. The
   companion is internally consistent and I followed it.
2. **"Fenberg shows that for any subset A there exists an n > 0 so that …"** — the transcript's
   version of the multiple recurrence theorem is the plain-existence form. The companion's
   Theorem 3.2 is the stronger averaged form with a positive liminf. I state the averaged
   form and note the difference in §3.4, because everything downstream is about the averages.
3. **"correlate with a polynomial phase function"** over 𝔽_pⁿ — as stated, false in low
   characteristic. The companion's Theorem 8.3 requires **non-classical** polynomials
   (its word: "non-standard"), with an explicit counterexample for U⁴(𝔽₂ⁿ). Corrected in
   §3.10 with the caveat marked as coming from the companion.
4. **Walsh's hypothesis.** The talk says "conditioned on the Riemann hypothesis" and "log n to
   some large power". The paper (arXiv:2310.07873) says **GRH** and (log X)^{ψ(X)} with ψ → ∞
   arbitrarily slowly. I quote the paper and note the difference in §4.16.

**Reconstructed, with what would verify each:**

- **The three-term counting identity** 𝔼 *f*(*x*)*g*(*x*+*d*)*h*(*x*+2*d*) = Σ_r *f̂*(*r*)*ĝ*(−2*r*)*ĥ*(*r*)
  (§2, §7.1(3)). Standard, but the companion asserts only the consequence. Verify by expanding
  in characters: the two averages force *a*+*b*+*c* ≡ 0 and *b*+2*c* ≡ 0.
- **The failure at four terms** as a two-parameter frequency family (§2, §7.1(5)). Mine; the
  talk says only that new obstructions appear. Verify by the same expansion with four
  functions.
- **The induction** *T*ⁿ(*z*,*w*) = (*z*+*n*α, *w*+2*nz*+*n*²α) (§7.2(1)) is stated in the
  companion §4; the induction itself is mine and is one line.
- **The identification of the third-difference operator** behind the skew-shift identity
  (§3.7, §7.2(2)). The companion gives the identity, not the reading. Verify: every coordinate
  of *T*^{jn}*y* is quadratic in *j*, and Δ³ annihilates degree ≤ 2.
- **The reading of the multidimensional open problem** (§4.18) — that existence of squares is
  not the open part, the inverse theory is. Marked in place as my inference, with the reason
  (Furstenberg–Katznelson multidimensional Szemerédi). She does not say it.
- **The pseudocode framing of the density increment** (§8.1). Mine entirely; the mathematics
  is the companion's §2.

**Gaps, and how bad each is.**

1. **PTE (§4.17) — low impact.** She names it in three words as one of three surprising
   applications. I could not identify the paper and did not guess. The other two applications
   (Koymans–Pagano arXiv:2412.01768; Zywina arXiv:2502.01957) are verified, and Zywina's
   explicitly uses her own Tao–Ziegler theorem, which is the point she was making.
2. **The multidimensional section (§4.18) — low impact.** Roughly five minutes of a
   seventy-minute talk, delivered as an outlook. No theorem is stated precisely enough to
   restore, and no companion covers it. The directional-Gowers-norm framing is recorded as she
   gave it.
3. **All slides — moderate impact, and unavoidable.** Every displayed formula in the talk lived
   on the slides. The companion recovers the first two-thirds essentially completely, which is
   the best outcome available for a talk with no proceedings paper. For the last third I have
   the primary papers, which state the theorems but of course not her chosen presentation of
   them. Where a slide clearly carried a picture I could not reconstruct — the two-level
   nilmanifold/torus diagram of §4.6 — I described it in words from her narration and said so.
4. **The Conze–Lesigne equation is stated, not explained (§4.7).** The companion says
   explicitly that solving it "is beyond the scope of this paper", and it is beyond the scope
   of this tutorial too. I give the equation, its interpretation as a centrality condition,
   and stop. Deliberate: this is the Gaitsgory rule — present the object with its motivation
   and its consequence rather than faking depth.

**Where the companion beats the talk.** Three places, all recorded above: the non-classical
polynomial caveat (§3.10), the averaged form of multiple recurrence (§3.4), and the
Furstenberg–Zimmer tower plus the explicit limit formula of Ziegler (2005), which is the
statement that turns "there are many progressions" into "here is how many" (§4.7). None of
the three fit in a fifty-minute talk; all three matter for reading the literature.

**Cross-references.** No sibling tutorial in `summaries/` overlaps this one materially. The
nearest structural relative is `langlands-function-fields-gaitsgory.md`, whose central
argument is also a three-link chain that runs unchanged in several settings, and whose anchor
is also "this is a Fourier transform, one level up" — a coincidence worth noticing, since the
two talks share no mathematics whatsoever.
