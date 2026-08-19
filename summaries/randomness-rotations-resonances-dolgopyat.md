---
title: "Randomness, Rotations, and Resonances"
speaker: Dmitry Dolgopyat (University of Maryland, College Park)
source: https://www.youtube.com/watch?v=lwY_jFRy7O8
video_id: lwY_jFRy7O8
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: "chapter exists but is not retrievable — https://doi.org/10.1137/25m1806971 (SIAM returns 403; null abstract on Crossref, Semantic Scholar, OpenAlex) — companions: https://arxiv.org/abs/2109.05560 (part one) and https://arxiv.org/abs/2006.11748 (part two)"
transcript: ../transcripts/lwY_jFRy7O8_transcript.txt
difficulty_for_you: 3/5 overall — 2/5 (the probability) / 4/5 (the space of lattices)
reading_time: ~70 min
---

# Randomness, Rotations, and Resonances — Dmitry Dolgopyat

**Field:** limit theorems. Not hyperbolic dynamics, which is what Dolgopyat is famous for —
see §13. The talk is about when a sum of many terms is Gaussian, when it is not, and what
the answer has to do with number theory. He sets it up himself in the second minute: three
problems, "each problem has elementary formulation," and each one needs "some ideas from
dynamical systems as well as some elementary geometric considerations."

**Difficulty against your background: 3 overall, and it splits cleanly.**

- **The probability spine is a 2.** Central limit theorem, local limit theorem, Edgeworth
  expansions, Kolmogorov's three-series theorem, characteristic functions, the Lindeberg
  condition. You own every one of these objects or can absorb the one new one — the *local*
  limit theorem — in twenty minutes. §4 is the calibration; skim it.
- **The machinery he reduces everything to is a 4.** The **space of lattices**
  SL(d,ℝ)/SL(d,ℤ), the **Siegel transform**, equidistribution and Poisson statistics for a
  diagonal flow on that space, translation surfaces and their affine symmetry groups. These
  are objects from homogeneous dynamics and you have none of them. §5 builds the ones the
  talk actually uses and declines the rest, and §6 is where the two halves meet.

Sections 4 and 7.1 carry the 2. Sections 5.4, 5.5, 7.3 and 7.4 carry the 4.

**What this tutorial builds:** the local limit theorem and its lattice obstruction;
discrepancy of an orbit; continued fractions, bounded type, and *even* continued fractions;
special (suspension) flows and the staircase translation surface; Markov partitions, just
far enough to use them; the space of unimodular lattices and marked lattices, the Siegel
transform, and what "equidistribution of a diagonal orbit" buys you; Edgeworth series and
why they fail.

**A note on sources — read this before you trust any formula below.**

- **There is no retrievable ICM proceedings paper.** A proceedings chapter exists — SIAM,
  DOI `10.1137/25m1806971`, pages 35–50, titled ***Randomness, Rotations, Renormalization,
  and Resonances*** (four R's; the talk was announced with three). SIAM returns HTTP 403 to
  automated fetching, and Crossref, Semantic Scholar and OpenAlex all return a null
  abstract. **I have not read one word of it.** Nothing below comes from it. The one thing
  its title tells us is that the fourth R, renormalization, is in the chapter too — and the
  talk's closing summary is precisely about renormalization, so the chapter and the talk
  are at least pointed the same way.
- **Companion for part one:** Dolgopyat and **Omri Sarig**, *Local Limit Theorems for
  Inhomogeneous Markov Chains*, Springer Lecture Notes in Mathematics **2331** (2023), 348
  pages; free preprint [arXiv:2109.05560](https://arxiv.org/abs/2109.05560). **This is a
  companion, not the ICM paper.** It earns the label: the theorem Dolgopyat states aloud as
  "what we proved with Omri Sarig several years ago" is this book's main structure theorem,
  and §7.1 below restores that theorem from it, statement numbers and all.
- **Companion for part two:** Dolgopyat and **Bassam Fayad**, *Limit theorems for toral
  translations*, Proc. Sympos. Pure Math. **89** (2015) 227–277;
  [arXiv:2006.11748](https://arxiv.org/abs/2006.11748). A survey by the speaker on exactly
  the rotations material, including §8.5 on the staircase surface, which is the picture he
  showed and did not have time to explain. Also a companion, not the ICM paper.
- **Part three is restored from its own primary paper:** Dolgopyat and **Kasun Fernando**,
  *An error term in the Central Limit Theorem for sums of discrete random variables*,
  [arXiv:2303.10235](https://arxiv.org/abs/2303.10235), IMRN **2023** no. 21, 18664–18713.
  Every formula in §7.4 is quoted from it.
- **Individual results are restored from their own papers**, cited inline by name: Beck,
  Bromberg–Ulcigrai, Kesten, Borda, Hooper–Hubert–Weiss, Dolgopyat–Fayad's two *Deviations*
  papers, Esseen. These are primary literature for one theorem each and are visibly
  distinct from the two companions.
- **The talk's own main new result has no locatable preprint.** See §7.3 and the gap
  ledger in §13. This is the most consequential hole in the document.
- **No formulas survive in the captions.** Everything was on slides. Every display below is
  either quoted from a located paper and cited, reconstructed from spoken narration and
  labelled, or marked as a gap.

**Names.** The auto-captions destroy almost every proper noun, including two that matter
("Amrit Serik" is Omri Sarig; "Gaston Fernandez" is Kasun Fernando). Full table in §13.
Two names I could **not** verify are reported as unverified rather than guessed.

---

## 1. What is at stake

Here is the whole talk in one question.

> You add up a great many numbers. When is the answer Gaussian — and when it is not, what
> is it instead, and what decides?

You already believe a version of the answer: add independent, identically distributed,
finite-variance random variables, subtract the mean, divide by √n, and you get a Gaussian.
That is the central limit theorem, and it is so robust that it is easy to stop asking
questions.

Dolgopyat asks three, and all three break the theorem.

**Question one: what if the terms have different distributions?** Not identically
distributed, just independent and bounded. The central limit theorem mostly survives. The
*local* limit theorem — the finer statement about landing in an interval of length 1 rather
than of length √n — does not, and what obstructs it is **arithmetic**: whether the values
sit on a lattice. That is already a probability question with a number-theoretic answer.

**Question two: what if the terms are not random at all?** Take a completely deterministic
sequence. Not chaotic-deterministic like a hyperbolic map, where you can honestly say
"unpredictable" — the *most regular* deterministic system there is, a rigid rotation of a
circle. Count how often the orbit visits a fixed arc, subtract the expected count, and ask
for the fluctuation. There is nothing random anywhere. And you still get a central limit
theorem — with **√log N** in place of √N, and sometimes a Gaussian and sometimes a Cauchy
distribution, depending on the arithmetic of the rotation number.

**Question three: how good is the Gaussian approximation, exactly?** The classical answer
is the Edgeworth series: correct the Gaussian by powers of n^(−1/2) with Hermite
polynomials. For a random variable with three or more atoms, that series fails at a
predictable order — and the coefficient at which it fails turns out to be a random variable
whose law is a **universal** object built from random lattices, with the property that
knowing your model's parameters to ten decimal places tells you nothing about it.

The unifying claim is his closing summary, and it is worth having in front of you from the
start:

> Independent sums are the *most random* sequence you can write down. Quasi-periodic sums
> are the *most regular*. Both are studied by **renormalization**. In both, the answer is
> controlled by a **small number of resonant harmonics**. And on the Fourier side, the two
> renormalizations turn out to be *the same linear action on marked lattices* — which is
> why the same limiting distributions appear on both ends of the spectrum.

That is the talk: two opposite extremes, one dictionary.

---

## 2. Your anchor

You get two, and Dolgopyat hands you both from the podium. Take them in this order.

### 2.1 The central limit theorem is a renormalization-group fixed point

This is the anchor, and it is his, not mine. Here is what he says in the summary, verbatim
apart from caption noise:

> "Both systems can be studied by renormalization transformation. But these renormalization
> transformations are different. For if we want to sum 2n random variables, how can we do
> it? We first sum the first n random variables, then we sum the second. Then we already
> get something which is close to universal distribution, and then we sum the two random
> variables which we got. And so the renormalization transformation in this case looks as
> follows: you start with some random variable S, you consider its convolution with itself
> and maybe some scaling."

Read that as an operator on probability distributions:

$$\mathcal{R}[\mu] \;=\; \big(\mu * \mu\big)\ \text{rescaled by } \tfrac{1}{\sqrt{2}}$$

Adding 2n variables = adding n twice, then adding the two blocks. **That is block-spin
decimation.** The Gaussian is the attracting fixed point of 𝓡; finite variance is the
condition for lying in its basin; the stable laws are the other fixed points; and √n is the
scaling exponent that makes the fixed point non-trivial. Universality means "all these
microscopic models flow to the same fixed point," and it means exactly that here.

You know this construction from statistical mechanics. If you want it developed at length,
the Quastel tutorial in this folder (`random-interface-growth-quastel.md`, §7.2) runs an
explicit renormalization-group flow between two fixed points and is the better place to
re-read the general theory. I will not rebuild it here.

What is *new* is the second half of the sentence. For a quasi-periodic system there is a
**different** renormalization, and it is geometric rather than probabilistic:

> "For a quasi-periodic map, where this is some rotation of some torus, and the torus is
> ℝ^d over a lattice, what is convenient to do is just to change this lattice by applying
> some linear map."

So: renormalize a *sum* by convolving; renormalize a *rotation* by deforming the lattice
that defines the torus. Two completely different-looking operations. The punchline of the
talk is that on the Fourier side they are the same linear action, and §7.5 is where that
lands.

### 2.2 Small divisors

The second anchor is perturbation theory in classical mechanics, and it is exact rather than
decorative.

Count visits of the orbit {x + nα} to the arc [0, ℓ). Expand the indicator function of the
arc in a Fourier series, and sum the resulting geometric series in n. The k-th harmonic
picks up a denominator

$$\big|e^{2\pi i k \alpha} - 1\big| \;=\; 2\,\bigl|\sin \pi k \alpha\bigr|$$

and the indicator's own Fourier coefficient contributes another 1/k, so the size of the
k-th contribution is governed by

$$\frac{1}{k\,|\sin \pi k\alpha|}$$

*(Reconstructed shape. Dolgopyat says aloud: "you have some expression, but what you have in
the numerator is k times sine pi k alpha." The full displayed expression was on the slide.
The **denominator** k·sin(πkα) is verbatim from him and it is the only part I use.)*

A term is large exactly when kα is close to an integer — when the harmonic is nearly
**resonant** with the rotation. That is the small-divisor problem, in the same form you met
it in perturbation theory for near-integrable Hamiltonians, and the condition that saves you
is the same one: a **Diophantine condition**, here called *bounded type*, which says
k·‖kα‖ ≥ c for all k. Dolgopyat–Fayad's own paper on the subject uses the words: the proof
rests on "a correspondence between the **small divisors** in the Fourier series of the
discrepancy function and lattices with short vectors" (GAFA 24 (2014) 85–115, abstract).

**One honest limitation, stated because the spec demands it.** *KAM theory itself never
appears in this talk.* Not the theorem, not the name, not invariant tori. The small-divisor
*apparatus* is here — Diophantine conditions, continued fractions, resonance counting,
renormalization — and it is doing the same job it does in KAM. But if you go in expecting
tori to survive a perturbation you will be looking for something that is not there. What
survives here is not a torus; it is a limit law.

### 2.3 Two anchors that do not apply, named so you stop looking for them

- **Billiards and the Lorentz gas: absent.** My brief suggested them, reasonably — they are
  Dolgopyat's field and they are literally statistical mechanics. The talk mentions neither,
  not once.
- **Transfer operators and "Dolgopyat's method": absent.** His most famous contribution, the
  one the introducer spends a sentence on, does not appear. He explicitly declines the whole
  subject: *"I'm not going to discuss this kind of dynamical systems in my talk, because in
  this case it's quite well understood what is causing this stochastic behaviour."* See §13.

---

## 3. The three questions, as he poses them

Before the bridge, here is the skeleton, so you know what the vocabulary is for.

He starts from De Moivre and Laplace, 300 years ago: a sum of n coin flips, and the
approximation

$$\sigma_n\,\mathbb{P}\big(S_n = k\big) \;\approx\; \varphi\!\left(\frac{k - \mathbb{E}S_n}{\sigma_n}\right),
\qquad \varphi(z) = \tfrac{1}{\sqrt{2\pi}}e^{-z^2/2}$$

*(Reconstructed from his verbal statement: "the probability that the sum takes value k, once
we multiply it by standard deviation, is approximately equal to Gaussian density computed at
the point obtained from k by subtracting the mean and dividing by standard deviation." The
formula was on the slide.)*

Sum that over k up to a threshold and you get the central limit theorem. Push Stirling's
approximation to higher order instead of just the leading term and you get an asymptotic
expansion in powers of 1/σ_n with polynomial coefficients — the Edgeworth series.

So the three-hundred-year-old story already contains all three of his questions, and he asks
what happens when you relax each hypothesis:

1. **Non-stationary.** Terms independent but not identically distributed.
2. **Dependent.** Terms not independent — and then, the extreme case, terms not random.
3. **Higher order.** The lattice case admits an expansion to any order. What about the
   non-lattice case — three atoms instead of two?

"Each of these questions commands a vast literature," he says. "One can give a graduate
course for each." What he does instead is take the simplest non-trivial case of each and
show the new phenomenon it exposes.

---

## 4. The bridge, part one: the probability (this is the 2)

Skim this if the vocabulary is already yours. Only §4.2 is likely to be new.

### 4.1 Central limit theorem, stated the way he uses it

X₁, …, X_n independent, mean zero, finite variance, S_n their sum, σ_n² = Var(S_n). Then

$$\mathbb{P}\!\left(\frac{S_n}{\sigma_n} \le z\right) \longrightarrow \Phi(z) = \int_{-\infty}^{z}\varphi(y)\,dy$$

His gloss is the operational one: **on intervals of length comparable to σ_n, the hitting
probability is universal.** It agrees with a Gaussian of the same mean and variance, and
nothing else about the model matters.

### 4.2 Local limit theorem — the new object

Now shrink the interval. Take (a, b) of length **O(1)**, not O(σ_n), sitting near the point
z·σ_n. Expand the Gaussian to first order across such a short interval and you get

$$\mathbb{P}\big(S_n - z\sigma_n \in (a,b)\big) \;\approx\; \frac{\varphi(z)}{\sigma_n}\,(b-a)$$

*(This one you can derive in a line: the density is essentially constant across an interval
of length O(1) when the scale is σ_n → ∞.)*

When this holds we say the system satisfies the **non-lattice local limit theorem**.

Dolgopyat's way of putting it is the one to keep, because the rest of the talk is a
variation on it:

> **Zoom in around a point not far from the mean, and what you see is Lebesgue measure —
> which is Haar measure on the real line.**

The local limit theorem is a statement that the fine-scale structure of the sum is the
translation-invariant measure of ℝ. Every failure in this talk is a failure of that
sentence, with Haar measure on ℝ replaced by Haar measure on some *smaller* group.

**The obvious obstruction.** If every X_i is integer-valued, and (a, b) contains no integer,
the probability is exactly zero and no such asymptotic can hold. **Gnedenko and Stone**:
that is the *only* obstruction in the i.i.d. case. Either the non-lattice local limit theorem
holds, or, after a shift, the variables take values in a sublattice tℤ — and then the local
picture is Haar measure on that shifted subgroup, i.e. counting measure on a
one-dimensional lattice.

Notice the shape of the statement, because the whole talk has it: *classify the closed
subgroups of ℝ.* There are only three kinds — {0}, tℤ, and ℝ — and each one names a regime.

### 4.3 Non-stationary independent sums

Independent, uniformly bounded, mean zero, different distributions. V_n = Var(S_n).

**Does the CLT hold?** He attributes the answer to **Kolmogorov's three-series theorem**
(this setting is essentially the main case of it). Two possibilities:

- **V_n bounded** ⟹ S_n converges almost surely. There is no fluctuation to normalize.
- **V_n unbounded** ⟹ the central limit theorem holds.

So the *only* obstruction to the CLT is almost-sure convergence of the sum. Clean.

**Does the local limit theorem hold?** Assume the CLT. Two possibilities again:

- The local distribution is Lebesgue measure on ℝ. Business as usual.
- There is a **local obstruction**: for some a > 0, the projection of S_n to the torus ℝ/aℤ
  *converges in distribution*, after a **time-dependent change of origin** on the torus.
  (Dolgopyat: *"like in dynamical systems, we need to introduce some normal form — we need to
  change origin on the torus at different times."*) Then the local distribution is invariant
  only under translations by aℤ, and the limiting object is the law of the limiting random
  variable Y on that torus.

The point of the second bullet, and he says it explicitly: **a purely probabilistic question
about local distributions has an answer that depends on the arithmetic nature of the support
of the measure.** That is the first interaction of probability and number theory in the
talk, and there are two more coming.

### 4.4 Edgeworth series

Keep going past the leading term. The **order-r Edgeworth series** is

$$E_r(z) \;=\; \Phi(z) \;+\; \varphi(z)\sum_{k=1}^{r}\frac{P_k(z)}{n^{k/2}}$$

with P_k polynomials (built from Hermite polynomials and the cumulants). The polynomials are
*defined* by matching Fourier transforms: the characteristic function of S_n/(σ√n) and the
Fourier transform of E_r must agree to o(n^(−r/2)). We say S_n **admits an order-r Edgeworth
expansion** if

$$\lim_{n\to\infty} n^{r/2}\left[\mathbb{P}\!\left(\frac{S_n}{\sigma\sqrt n}\le z\right) - E_r(z)\right] = 0
\qquad\text{for every } z$$

*(Quoted from Dolgopyat–Fernando, arXiv:2303.10235, eq. (1.1) and the display above it.)*

Dolgopyat's remark about this definition is the seed of part three:

> The series is **a priori only formal**, because it is built by matching the characteristic
> function **at zero only**. It ignores every other resonance.

Hold onto that. Matching at ξ = 0 is a local condition on the characteristic function; the
Edgeworth series knows nothing about what happens at other frequencies where |φ̂(ξ)| is close
to 1. Those other frequencies are the resonances, and they are what breaks it.

---

## 5. The bridge, part two: the geometry (this is the 4)

Five objects. Each is defined by deforming something you have.

### 5.1 Discrepancy

Given a map f : X → X, a point x, and a target set I, the **discrepancy** is

$$D_N(I, f, x) \;=\; \#\{\,0 \le n < N : f^n(x) \in I\,\} \;-\; N\,|I|$$

Visits minus expected visits. This is the "sum" in parts two and three of the talk: an
ergodic (Birkhoff) sum of the centred indicator function 𝟙_I − |I|.

**Borel's example, which Dolgopyat uses to set the tone.** Let f(x) = 10x mod 1 on [0,1).
In decimal notation this map **erases the first digit**. If x is uniform, the digits are
i.i.d. uniform on {0,…,9}; so if you count how often the digit 3 appears among the first N
digits and subtract N/10, that discrepancy divided by √N satisfies a central limit theorem.
This is Borel, about 100 years ago, and it is the prototype of the whole subject:

> **a completely deterministic system with genuinely random behaviour.**

He is careful about why the statistical description is *legitimate* rather than a
convenience: if you know x only to 10^(−10) — ten digits — then after ten iterations you know
nothing at all about the state. Determinism plus finite precision equals randomness, and the
mechanism is **exponential divergence of nearby orbits**: two points at distance 10^(−n) are
at distance 1 after n steps.

### 5.2 The systems he sets aside, and why you should know their names anyway

**Hyperbolic toral automorphisms.** Take A ∈ SL(2,ℤ) with real eigenvalues off the unit
circle — one expanding (λ > 1), one contracting — and let it act on 𝕋² = ℝ²/ℤ². Arnold's cat
picture: iterate a portrait a few times and the phase space is uniformly grey. Completely
deterministic, explicitly solvable in eigencoordinates, statistically indistinguishable from
noise.

**Markov partitions and symbolic dynamics.** Chop the torus into pieces Π₁, …, Π_K. Record
which piece the orbit is in at each time: an *itinerary*, a sequence of symbols. If the
resulting process is a Markov chain when x is uniform, the partition is a **Markov
partition**. **Adler and Weiss** (about 50 years ago) proved that every hyperbolic toral
automorphism in dimension 2 has one, with elements that are parallelograms whose sides are
parallel to the stable and unstable eigenvectors. The construction was extended by **Sinai,
Bowen, Young, Sarig** and many others; Dolgopyat points at **Jérôme Buzzi's** lecture at the
same congress for recent results. In higher generality the partition elements are fractal,
but they still work.

This is the machinery that turns a deterministic map into a Markov chain, and therefore into
§4.3's setting. **Remember that it exists — §7.3 uses it.**

And then he puts it all down:

> "I'm not going to discuss this kind of dynamical systems in my talk, because it's quite
> well understood what is causing this stochastic behaviour, which is exponential divergence
> of nearby orbits. So I'm going to consider **the opposite end of the spectrum**."

The opposite end is the circle rotation x ↦ x + α mod 1. An **isometry**. Zero divergence of
nearby orbits. Nothing chaotic anywhere. And limit theorems all the same.

### 5.3 Continued fractions and bounded type

$$\alpha \;=\; a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{\ddots}}}$$

**Regular expansion:** a₀ ∈ ℤ, and a_k a *positive integer* for k ≥ 1.

**Bounded type** (he says "bounded type"; the captions render it "boundary type"
throughout): there is C = C(α) with

$$|q\alpha - p| \;\ge\; \frac{C}{|q|}\qquad\text{for all integers } p,\ q \ne 0$$

Equivalently: the partial quotients a_k are bounded. This is the Diophantine condition of
§2.2 — α is badly approximable by rationals. Quadratic irrationals are of bounded type, by
Lagrange's theorem (eventually periodic expansion ⟹ bounded partial quotients).

**Even continued fractions.** He then introduces a variant, and it looks arbitrary until §7.3
explains it. Require every partial quotient to be **even**, and non-zero from the second one
on. (Partial quotients may now be negative — that is what makes an even expansion possible.)
Lagrange's theorem still holds: quadratic irrationals have eventually periodic even
expansions.

Bounded type in the even expansion needs **an extra condition**, and it is the one his main
theorem is about:

> the entries must be bounded, **and** there must be no arbitrarily long alternating blocks
> `+2, −2, +2, −2, …`.

*(Verbatim in substance from the transcript. Why the alternating block is bad: `+2, −2`
repeating is the even-expansion way of encoding a partial quotient 1 in the regular
expansion, so long alternating blocks are the even expansion's way of hiding an unbounded
regular partial quotient.* **This parenthetical explanation is mine, not his** *— he states
the condition and moves on. I include it because it makes the condition memorable, and I
flag it because he did not say it.)*

### 5.4 Special flows and the staircase surface

A **special flow** (or suspension flow) over a map T with roof function r: take the region
under the graph of r over the base, and flow straight up at unit speed; when you hit the
graph, return to the base at the point T(x). Conversely, a flow on a surface plus a
transversal cross-section gives you a map — the **Poincaré map** — plus a return time. The
move Dolgopyat makes is the second direction: **replace a map by a flow on a surface**,
because surfaces have symmetries that maps do not.

The surface is the **staircase** St, and it is the one picture in the talk I can fully
restore, because Dolgopyat–Fayad's survey draws it (arXiv:2006.11748, Figure 4, §8.5) and
credits it to **Hooper, Hubert and Weiss**:

- Take 2 × 1 rectangles ("bricks"). Stack them so that the bottom-left corner of the next
  brick sits at the *centre of the top edge* of the previous one — each brick is offset by
  half a brick. The pile is infinite in both directions; index the bricks by z ∈ ℤ.
- Identify sides that differ by **2 units** horizontally or vertically. The result is a
  translation surface.
- There is a translation symmetry G(x, y) = (x + 1, y + 1) — climb one step — and
  **St/G is a torus**. So the staircase is a **ℤ-cover of a torus**, and the covering index
  z is a *height*: which step you are on.

Now flow in a straight line of slope β. Take Σ = the union of the top edges of the bricks as
your cross-section, and identify Σ with 𝕋 × ℤ. Then the Poincaré map is

$$(x, z) \;\longmapsto\; \Big(x + \alpha,\ \ z + \mathbb{1}_{[1/2,\,1)}(x) - \mathbb{1}_{[0,\,1/2)}(x)\Big),
\qquad \alpha = \frac{\tan\theta + 1}{2}$$

*(Quoted from Dolgopyat–Fayad, arXiv:2006.11748 §8.5, where
this display appears with tan θ = β. Dolgopyat says in the talk "we consider a line with
constant slope β = 2α − 1", which is the same relation solved the other way.)*

**Stare at that map for a second, because it is the entire trick.** The first coordinate is
just the rotation by α. The second coordinate goes **up** when x is in the right half of the
circle and **down** when x is in the left half. So after n steps,

$$z_n \;=\; z_0 + D_n\big([1/2, 1),\, R_\alpha,\, x\big) \;-\; D_n\big([0,1/2),\, R_\alpha,\, x\big)$$

which, up to the trivial identity D + D′ = 0 for a partition into two halves, is exactly
**twice the discrepancy of the rotation with respect to the half-circle**.

> **The height on the staircase *is* the discrepancy.** A question about counting visits of a
> circle rotation to an arc has become a question about how a straight line climbs an
> infinite staircase.

That is the "passing to a special flow" step he names and does not have time to draw.

**And now the symmetries.** The staircase has more than the deck transformation G. Following
Hooper–Hubert–Weiss (the survey's citation [53]), St is a **Veech surface**:

> For every A ∈ SL(2,ℤ) with **A ≡ I mod 2** — odd on the diagonal, even off it — there is a
> unique automorphism ψ_A of St which commutes with G, fixes the singularities, has
> derivative A at every non-singular point, and has **zero drift**. In coordinates,
> ψ_A(p, z) = (Ap, z + τ(p)) with ∫_{𝕋²} τ = 0.

*(Quoted in substance from arXiv:2006.11748, eq. (40) and the sentence above it. Dolgopyat
states exactly this from the podium — "on the diagonal you have odd entries, off diagonal you
have even entries… derivative equal to this matrix A… we have zero drift, meaning that on
average our orbit is equally likely to go up and down, and they commute with the deck
transformations.")*

The subgroup {A ∈ SL(2,ℤ) : A ≡ I mod 2} is the **theta group**. Its continued-fraction
algorithm is the **even** continued fraction algorithm. *That* is why §5.3 introduced even
expansions: they are the symbolic dynamics of the staircase's own symmetry group. Dolgopyat
does not say this; it is forced by putting his two slides next to each other, and I flag it
as my inference.

### 5.5 The space of lattices, and the Siegel transform

This is the object you do not have, and it is worth twenty minutes.

A **unimodular lattice** in ℝ^d is L = Aℤ^d with det A = 1. Two matrices give the same
lattice exactly when they differ by right multiplication by an element of SL(d,ℤ) (a change
of ℤ-basis). So

$$\mathcal{M}_d \;=\; \{\text{unimodular lattices in } \mathbb{R}^d\} \;\cong\; \mathrm{SL}(d,\mathbb{R})/\mathrm{SL}(d,\mathbb{Z})$$

This is a finite-volume (but non-compact) homogeneous space carrying a natural **Haar
measure**, normalized to a probability measure. Non-compact because a lattice can have an
arbitrarily short vector and run off to infinity in the space; that non-compactness is not a
nuisance here, it is where the heavy tails come from.

**Why you should find this familiar.** It is a phase space with a group acting on it by
translations, and the dynamics is a one-parameter subgroup acting on the right — the
**diagonal** (or Cartan) flow diag(e^t, …, e^t, e^{−(d−1)t}). For d = 2 this is literally the
geodesic flow on the modular surface. If you want the general framework of Γ\G, right
translations as flows, and mixing implying equidistribution, built at length, read
`lens-of-circles-oh.md` in this folder — Hee Oh's tutorial constructs Γ\PSL₂(ℂ) as a phase
space and develops exactly that machinery. I need only the special case and only two facts
about it.

**Fact one: the Siegel transform and its mean.** For a nice compactly supported
g : ℝ^d → ℝ, define

$$S(g)(L) \;=\; \sum_{w \in L \setminus \{0\}} g(w)$$

— evaluate g at every non-zero lattice point and add. This is a function on the space of
lattices. Its average over Haar measure is the integral of g:

$$\mathbb{E}_L\big[S(g)\big] \;=\; \int_{\mathbb{R}^d} g(w)\,dw$$

*(Quoted from Dolgopyat–Fernando eq. (9.1), where it is attributed to Rogers; it is the
classical Siegel mean-value identity.)* In particular, for a set B with 0 ∉ B,
ℙ(L ∩ B ≠ ∅) ≤ Vol(B). This is the tool for "how many lattice points land in this box" —
which is exactly "how many resonances are there".

**Fact two: marked lattices.** A **marked lattice** is a pair (L, χ) where χ : L → 𝕋 is a
homomorphism (a character) — every lattice point carries a phase. The space of these is

$$\mathcal{M} \;\cong\; \big(\mathrm{SL}_d(\mathbb{R}) \ltimes \mathbb{R}^d\big)\big/\big(\mathrm{SL}_d(\mathbb{Z}) \ltimes \mathbb{Z}^d\big)$$

with its own Haar measure — pick a lattice at random, then pick the phases independently and
uniformly. *(Quoted from Dolgopyat–Fernando §1. The paper writes "homeomorphism χ : L → 𝕋";
that is a typo for **homomorphism** — see §13.)*

Marked lattices are what the talk ends on. Keep the picture: **a lattice of harmonics, each
carrying a phase, with a linear map acting on the lattice.**

---

## 6. What the three parts have in common, stated once

Before the walkthrough, the pattern, so you can see each part as an instance:

| | part one (non-stationary sums) | part two (rotations) | part three (Edgeworth) |
|---|---|---|---|
| the sum | S_N of independent or Markov terms | discrepancy D_N of a rotation | S_n of i.i.d. terms with d+1 atoms |
| "resonance" means | ξ where the characteristic function does not → 0 | k with k·‖kα‖ small | k with all c_j k near integers to within n^(−1/2) |
| resonances form | a closed subgroup of ℝ | continued-fraction denominators | short vectors in a lattice |
| the answer is decided by | which subgroup: {0}, tℤ, or ℝ | how many resonances, and their signs | equidistribution of a lattice in 𝓜 |
| normalization | √Var | √log N or log N | n^(−d/2) |
| limit | Gaussian, or Haar on a subgroup | Gaussian, or Cauchy | random Siegel transform |

Every row is the same sentence: **find the resonances, count them, and look at their
geometry.**

---

## 7. The talk, rebuilt

### 7.1 Part one — inhomogeneous Markov chains, and the group of resonances

He moves from independent to dependent by the shortest possible route: a **non-stationary
Markov chain**, in the simplest setting where anything can be said.

**The setting**, as he states it: for each n there is a background measure μ_n on the state
space; the transition probability with respect to μ_n has a density **uniformly bounded above
and below** (this is *uniform ellipticity*); the observable is an **additive functional**
depending on two consecutive states,

$$S_N \;=\; \sum_{n=1}^{N} f_n(X_n, X_{n+1}), \qquad \sup_n \|f_n\|_\infty < \infty$$

Why two states and not one? Because that is where the new phenomenon lives, and he shows you
immediately: if f_n(X_n, X_{n+1}) = g_{n+1}(X_{n+1}) − g_n(X_n) — a **gradient** — the sum
telescopes, S_N stays bounded, and there is no central limit theorem no matter how large the
individual variances are. A functional of one variable cannot do that.

**The theorem** ("what we proved with Omri Sarig several years ago"), stated as he states it:
either the classical local limit theorem holds, or f_n decomposes into **four** parts —
a constant part, a lattice part, a convergent part, and one more part that exists only
because the variables are dependent.

Now let me restore that properly, because the companion book states it in a form you can
actually use, and it is a genuinely elegant classification.

**The three obstructions** *(Dolgopyat–Sarig, arXiv:2109.05560, §1.2 — quoted)*. Define the
**algebraic range** G_alg to be the smallest closed subgroup G ⊆ ℝ such that, after
subtracting constants, f_n(X_n, X_{n+1}) ∈ G almost surely for every n. Then the complete
list of obstructions to the local limit theorem is:

1. **Lattice behaviour.** G_alg = tℤ for some t > 0.
2. **Center-tightness.** There are constants m_N with {S_N − m_N} tight. Equivalently
   Var(S_N) ↛ ∞.
3. **Reducibility.** f = g + c, where c is center-tight and G_alg(g) is *strictly smaller*
   than G_alg(f).

**If none of the three occurs, all the classical asymptotics hold.** That is the book's main
theorem and it is exactly the shape of Gnedenko–Stone, one level up in generality.

**Characterizing (2), which is the gradient story made precise** *(Theorem 3.8 of the book)*:

> Var(S_N) is bounded ⟺ f is center-tight ⟺ **f = ∇a + h**, where a is a uniformly bounded
> potential and h has summable variance.

There is the "constant part, gradient part, convergent part" he says aloud, in three symbols.
The book notes that this characterization "seems to be new" in the inhomogeneous setting, and
that the *summable-variance* term is genuinely new — in the stationary homogeneous world it
cannot occur unless the functional is constant.

**Now the resonances, which is the part he spends his time on.** He defines resonant points
by first defining non-resonant ones: ξ is non-resonant if the characteristic function of S_N
at ξ tends to 0. But that is too crude, and he gives the counterexample himself: let every
term be integer-valued except the first, which is uniform on [0,1]. Then the characteristic
function vanishes at ξ = 2π because of the *first term alone*, forever — and yet the system
is morally lattice. So he wants **stably** non-resonant: the characteristic function should
tend to 0 even after deleting the first few terms. The complement of that set is the set of
**resonances**.

The companion book's version of this is a genuinely computable quantity, and it is worth
seeing because it makes "resonance" concrete. Take a **hexagon**: two three-step paths
x_{n−2} → x_{n−1} → x_n → y_{n+1} and x_{n−2} → y_{n−1} → y_n → y_{n+1} sharing their
endpoints. The **balance** Γ(P) is the value of the additive functional along the first path
minus its value along the second. The **structure constants** are

$$d_n(\xi)^2 \;=\; \mathbb{E}\Big[\big|e^{i\xi\Gamma(P)} - 1\big|^2\Big]$$

and the **co-range** is

$$H(X, f) \;=\; \Big\{\xi \in \mathbb{R} \;:\; \sum_{n\ge3} d_n(\xi)^2 < \infty\Big\}$$

*(Quoted from arXiv:2109.05560, eqs. (2.25)–(2.26) and §4.2.1.)* Read it: d_n(ξ) measures how
far ξ·Γ is from 2πℤ — how nearly the two paths are *indistinguishable at frequency ξ*.
Summable means the frequency ξ never gets destroyed. **The co-range is Dolgopyat's group of
resonances**, written down as a convergent series in computable quantities. And the summation
from n = 3 is precisely his "after we maybe remove the first few terms."

**The trichotomy.** He says from the podium: the resonance group is a closed subgroup of ℝ,
so there are three possibilities, and each names a regime. The book's Theorems 4.3 and 4.4
give them exactly:

| resonance group H(X, f) | what it means | what happens |
|---|---|---|
| **ℝ** | f is center-tight | S_N is tight; **no CLT**, no universal behaviour |
| **{0}** | irreducible, non-lattice | **the usual local limit theorem**, essential range ℝ |
| **tℤ**, t > 0 | arithmetic resonance | lattice local limit theorem on the sublattice (2π/t)ℤ |

with a quantitative bound in the lattice case: t ≥ π/(3 ess sup |f|), so the resonance
spacing cannot be arbitrarily fine.

In the third case, he says, "we can just use the Laplace approximation to compute the
contribution of these resonances," giving a formula like the independent one — but with an
extra complication, and here is the one place he explicitly declines to write the formula:

> "For the Markov case the expression is slightly more complicated, so I don't give it,
> because now to identify fibers at different points you need to modify not only the change
> which depends on time, but also it depends on the state of your Markov chain."

*[Gap: the reducible-case asymptotic formula for the Markov setting was not shown. It is
Theorem 6.2 / Chapter 6 of the companion book. **Impact: low** — the structure is fully
stated and the shape (Gaussian × a periodic correction) is clear; only the explicit
correction factor is missing, and it is available in the book.]*

**One name I cannot verify.** He attributes the CLT characterization to "a theorem of
Dabrowski and Gorodetsky" (captions). No such pair appears anywhere in the companion book.
What the book does attribute: the central limit theorem for uniformly elliptic inhomogeneous
Markov arrays is **Dobrushin's** (their Theorem 3.10, following the martingale proof of
Sethuraman–Varadhan); the "constant + gradient + convergent" characterization is their own
Theorem 3.8; and the method behind both is **Gordin's** martingale–coboundary decomposition.
"Dobrushin" and "Gordin" are the phonetically plausible readings, and I am not going to write
them down as if I had checked them. See §13.

### 7.2 The pivot: from most random to most regular

He now flips the sign of the whole talk. §5.1 and §5.2 above are his interlude — Borel's
digits, the cat map, Markov partitions — and they exist to establish one contrast:

- **Exponentially unstable systems** behave randomly, and we understand why.
- **Rotations** are isometries. Orbits neither converge nor diverge. Nothing is unstable.

> "And surprisingly, during the last two decades there were several papers about central
> limit theorems for rotations."

### 7.3 Part two — rotations

**Beck's theorem** (**József Beck**, *Randomness of the square root of 2 and the giant leap*,
Period. Math. Hungar. Part I: **60** (2010) 137–242, Part II: **62** (2011) 127–246). As
stated in the Dolgopyat–Fayad survey (Theorem 8(b)):

> Let α be a **quadratic irrational**, ℓ **rational**, x = 0. Let M be uniformly distributed
> on {1, …, N}. Then there are constants C(α, ℓ) and σ(α, ℓ) with
>
> $$\frac{D_M\big([0,\ell],\ \alpha,\ 0\big) \;-\; C(\alpha,\ell)\log N}{\sqrt{\log N}}
> \;\xrightarrow{\ d\ }\; \mathcal{N}\big(0, \sigma^2(\alpha,\ell)\big)$$

**Substantive caption correction.** The transcript says "you take interval L to be a
irrational number." It must be **rational**. Two independent confirmations: the survey's
Theorem 8(b) says ℓ rational; and Bromberg–Ulcigrai's abstract describes Beck's case as "α
quadratic irrational, β **rational**, and the initial point the origin" — their whole
contribution is extending it to irrational β, which would be vacuous otherwise. Corrected in
the text; flagged in §13.

Note the *source of the randomness*: the initial point is fixed at 0 and α is fixed. The only
random object is **the time N**. Dolgopyat calls this out — "it seems there are no free
parameters, but you can change n." Limit theorems of this kind are called **temporal** limit
theorems, a term Bromberg–Ulcigrai credit to Dolgopyat and Sarig.

**Two things are surprising, and he says so.**

1. **The normalization is √log M, not √M.** If M is uniform on {1, …, N} then a typical M is
   of order N. For a hyperbolic toral automorphism the scaling would be √N. Here it is
   √log N — *exponentially smaller fluctuations*. The isometry is far more equidistributed
   than a chaotic map.
2. **There is a drift.** The discrepancy is already centred — the mean was subtracted in its
   definition. You would expect it to be equally likely positive or negative. Instead it
   sits around C(α, ℓ)·log M, which is *much larger* than the fluctuation √log M. So if
   C > 0, **the discrepancy is positive 99.9% of the time.** The constant may or may not
   vanish: he says it is **zero for the golden mean and for √3**, and **non-zero for √2 and
   for √7**, and that it "depends on some special values of some L-function."

   *[The L-function claim is stated aloud and not elaborated. Beck's own papers are titled
   around quadratic fields; the constant being expressible through special values attached to
   the real quadratic field ℚ(α) is consistent with that literature — see Borda,
   arXiv:2512.03884, which ties analogous constants to "fundamental units and special values
   of zeta functions" of ℚ(α). **I have not verified the specific values C(golden mean) = 0,
   C(√3) = 0, C(√2) ≠ 0, C(√7) ≠ 0.** They are reported as spoken. **Impact: low** — they are
   illustrations, not load-bearing.]*

**Bromberg–Ulcigrai** (**Michael Bromberg** and **Corinna Ulcigrai**, *A temporal Central
Limit Theorem for real-valued cocycles over rotations*, [arXiv:1705.06484](https://arxiv.org/abs/1705.06484),
Ann. Inst. H. Poincaré Probab. Statist. **54** (2018) 2304–2334). Three relaxations of Beck:

- α of **bounded type**, not necessarily quadratic (so: bounded partial quotients, not
  eventually periodic ones).
- ℓ of **bounded type with respect to α**: ‖qα − ℓ‖ ≥ C/q. Rational ℓ satisfies this
  automatically when α is of bounded type. The set of such ℓ is uncountable and has
  **Hausdorff dimension 1**.
- **arbitrary initial point**, not just 0.

The conclusion is still a central limit theorem, with one change: the centring and scaling
constants **oscillate** — they no longer equal C·log M and √(C·log M) but wander between
C₁ log M and C₂ log M. Losing periodicity of the continued fraction costs you exact
constants and nothing else.

And their method is the bridge back to part one, in their own words: continued-fraction
renormalization plus dynamical Ostrowski expansions gives "a suitable symbolic coding
framework which allows us to reduce the main result to a **CLT for non-homogeneous Markov
chains**."

**From central to local.** Those results give the probability that the discrepancy lands in
an interval of size √log M. Dolgopyat then asks for the probability that it takes a **fixed
value k** — the local limit theorem — and says it holds with a Gaussian approximation. One
consequence he draws out: if the drift constant C = 0, the discrepancy is **uniformly
distributed** in the sense that any two values k₁ and k₂ are attained with the same
asymptotic frequency.

**The main new result.** This is the talk's own contribution to part two, and it is where my
sourcing runs out.

> Let α be of bounded type, let **β = 2α − 1**, and take the **even** continued fraction
> expansion of β. Then:
>
> - **all values of the discrepancy are asymptotically equally likely** ⟺ the number of
>   **sign changes** in that expansion grows **sublinearly** in n;
> - the discrepancy is **positive half the time and negative half the time** ⟺ the number of
>   sign changes grows **slower than √n**.

The second condition is much more restrictive than the first, and he stresses that this is
*not* an artefact:

> "This may be not — because even if you consider a random walk, for a random walk it is also
> the same thing. Local time at two nearby points converges to one, but a random walk does
> **not** spend 50% of the time on the positive axis and 50% on the negative axis."

That is the **arcsine law**, and it is exactly right: for simple random walk the local times
at two nearby sites are asymptotically equal, but the fraction of time spent positive is
arcsine-distributed, not concentrated at 1/2. So "every value equally likely" and "signs
balanced" are genuinely different statements, and the rotation reproduces the random walk's
dichotomy. Specializing to ℓ = 1/2 — count visits to the left half-circle minus visits to the
right half — and taking the starting point x random, he states: **the first condition holds
with probability one, the second with probability zero.**

*[Gap, and it is the big one. This theorem has no locatable preprint: it is not on arXiv (I
enumerated all Dolgopyat arXiv entries through May 2026) and not on his publication page. He
names **no coauthors** for it — he says only "we". The precise meaning of "sublinearly", the
exact definition of "sign change" for the even expansion, the role of the initial point x
(the criterion as stated depends only on α, yet the conclusion is stated for random x), and
the statement for general ℓ are all unavailable. **Impact: moderate-to-structural.** This is
the newest mathematics in the talk and I can convey only its shape. Everything around it —
Beck, Bromberg–Ulcigrai, the proof strategy, the Cauchy theorem — is fully sourced.]*

**The proof, in four moves.** He says "the proofs are kind of long, so I don't have time to
show it — you can ask maybe your virtual assistant" and then shows pictures. Here is what the
pictures say, restored from the survey's §8.5.

1. **Suspend.** Pass to the staircase surface of §5.4 and the linear flow of slope
   β = 2α − 1. The height coordinate is the discrepancy. A statement about N steps of the
   rotation becomes a statement about a straight line segment of length ~N on the staircase,
   and the question is: **which brick does it end on?**
2. **Renormalize using the surface's symmetries.** The line is very long and the brick is
   small — hopeless directly. But the affine automorphisms ψ_A of §5.4 exist, they act with
   derivative A, and a suitable A contracts along the direction of the line. So apply ψ_A^{−m}
   until the segment has length of order 1. Since A expands by a factor λ each time,
   **m ≍ log N / log λ**. Now the question is about a unit segment: *after m renormalization
   steps, what is the probability of ending on brick k?*
3. **The height becomes a Birkhoff sum over a hyperbolic map.** Because
   ψ_A(p, z) = (Ap, z + τ(p)), each renormalization step shifts the level by τ evaluated at
   the current base point, and the base dynamics is the **hyperbolic toral automorphism A**.
   So the brick index is
   $$\sum_{j=1}^{m} \tau\big(A^{-j} q\big)$$
   *(quoted in form from arXiv:2006.11748 §8.5).* A sum of **m ≍ log N** terms.
4. **Now use part one.** A is hyperbolic, so it has a Markov partition (§5.2), so this sum is
   an additive functional of a Markov chain, so the theorems of §7.1 apply and give a CLT and
   a local limit theorem for it.

**And there is the √log N.** The discrepancy is not a sum of N things; it is a sum of
**log N** things, one per renormalization step. Its fluctuation is the square root of that.
The exponent was never mysterious — it is counting renormalization steps.

**Where bounded type is used.** He is precise about this, and it is the hinge of the last
part:

> The assumption that α is of bounded type is used many times, but the most important use is
> that the additive functional τ is **uniformly bounded**. Because it is uniformly bounded it
> satisfies the **Feller–Lindeberg condition** — each term is small compared to the whole sum.
> And that condition **fails** for a typical α.

*(Captions: "failure Lindeberg condition" → **Feller–Lindeberg**.)*

**Typical α: the Cauchy theorem.** So take α random too. Dolgopyat and **Bassam Fayad**
(*Deviations of ergodic sums for toral translations II. Boxes*,
[arXiv:1211.4323](https://arxiv.org/abs/1211.4323), Publ. Math. IHÉS **132** (2020) 293–352):

> Let n be uniform on {1, …, N} and α uniform on the torus. Then the normalization is
> **log N**, not √log N, and the limit is the **Cauchy distribution**, not the Gaussian.

*(He dates it "around 5 years ago." The paper's abstract states the d-dimensional version:
discrepancy relative to a random box, normalized by ln^d N, converges to Cauchy, and "the key
ingredient of the proof is a **Poisson limit theorem** for the Cartan action on the space of
d+1 dimensional lattices." The talk states the d = 1 case.)*

This extends **Kesten** (*Uniform distribution mod 1*, Ann. of Math. **71** (1960) 445–471,
and Acta Arith. **7** (1961/62) 355–380), whose theorem randomizes α and the initial point but
keeps **N deterministic**:

$$\frac{D_N\big([0,\ell],\ \alpha,\ x\big)}{\sigma \log N} \;\xrightarrow{\ d\ }\; \text{standard Cauchy},
\qquad (\alpha, x) \text{ uniform on } \mathbb{T}^2$$

Kesten's explicit formula for σ involved an integral whose *domain of integration depended on
whether ℓ was rational or irrational* — so the constant appeared to depend on ℓ. Dolgopyat
reports that "last year, **Bence Borda** computed this integral and showed that it does not
depend on ℓ." Verified, and here is the number:

> **Borda** (*Equidistribution of continued fraction convergents in SL(2, ℤ_m) with an
> application to local discrepancy*, J. Mod. Dyn. **21** (2025) 327–359,
> [arXiv:2303.08504](https://arxiv.org/abs/2303.08504), Theorem 2): Kesten's limit law holds
> with **σ = 1/(3π)** for **all** ℓ ∈ (0,1). The paper's own phrasing: the apparent dependence
> "has been cited by several authors… we show that the dependence is illusory."

**Why √log for bounded type and log for typical α.** This is the heart of the talk and it
gets its own section — §8.

### 7.4 Part three — Edgeworth expansions and random lattices

Back to i.i.d. sums, and the question of how good the Gaussian approximation is.

**The necessary condition nobody can improve.** E_r(z) is a smooth function of z. So if the
distribution of S_n/(σ√n) has **atoms of size much larger than n^(−r/2)**, the order-r
expansion cannot hold: at a jump, a smooth function cannot approximate both the value before
and the value after to accuracy o(n^(−r/2)).

For r = 1, jumps of size 1/√n occur exactly in the lattice case, and **Esseen** proved in 1945
that this is the *only* obstruction: S_n admits an order-1 Edgeworth expansion iff X is
non-lattice. (C.-G. Esseen, *Fourier analysis of distribution functions*, Acta Math. **77**
(1945) 1–125 — reference [6] of Dolgopyat–Fernando. The captions render this as "proven by SN
in 1945".) For higher orders, he says, much less is understood. **Cramér's** sufficient
condition — moments to order r+2 and a density — is "far from being necessary."

**The simplest non-trivial case.** Let X take **d+1 values** a₁, …, a_{d+1} with probabilities
p₁, …, p_{d+1}, mean zero. Two values (d = 1) is the lattice case and already fails at order 1.
So take d ≥ 2.

Then S_n takes the values Σ m_i a_i over compositions with Σ m_i = n, and

$$\mathbb{P}(S_n \le z) \;=\; \sum_{\substack{m_i \ge 0,\ \sum m_i = n \\ \sum m_i a_i \le z}}
\frac{n!}{m_1!\cdots m_{d+1}!}\; p_1^{m_1}\cdots p_{d+1}^{m_{d+1}}$$

*(Quoted from Dolgopyat–Fernando eq. (1.2).)* The multinomial term is a **local central limit
theorem for a ℤ^d random walk** — the walk that steps to e_i with probability p_i and stays
put with probability p_{d+1}. That local limit theorem says the multinomial coefficient, times
n^{d/2}, is bounded below in the bulk. So:

> **P(S_n ≤ z) has jumps of size ≍ n^(−d/2)**, hence the order-d Edgeworth expansion **never**
> holds, for any parameters.

The whole of §4.2 was setting up this one paragraph: the local limit theorem is what converts
"the values are discrete" into "the jumps have size exactly n^(−d/2)".

**The Dolgopyat–Fernando result** (with his student **Kasun Fernando** — captions: "Gaston
Fernandez"). Two halves:

- **Order d−1 does hold**, for almost every choice of the atoms. Precisely (their Theorem 1),
  if a is β-Diophantine — meaning max_j dist(b_j s, 2πℤ) ≥ K/|s|^β for |s| > 1, where
  b_j = a_j − a₁ — and 2R < 1/β + 1, then n^R (P − E_{d−1}) → 0. Almost
  every a is β-Diophantine as soon as β > 1/(d−1). **The same Diophantine condition as the
  rotations story, in a different costume.**
- **The failure at order d is by exactly n^(−d/2) — the smallest possible — but the
  coefficient is wild.** This is the striking part, and it is his Theorem 2. Put a smooth
  probability density on the parameters (a, p) — you know your model only approximately, say
  to 10^(−10). Then, for each fixed z, the error becomes a random variable, and

$$\frac{e^{z^2/2}\, n^{d/2}}{\Lambda(a,p)}\left[E_d(z) - \mathbb{P}\!\left(\frac{S_n}{\sigma\sqrt n} \le z\right)\right]
\;\xrightarrow{\ d\ }\; \mathcal{X}$$

  where *(their eq. (1.5))*

$$\Lambda(a,p) \;=\; \frac{|a_{d+1} - a_1|}{2^d\,\pi^{\,d+\frac12}\sqrt{\det(D_{a,p})}\ \sigma(a,p)}$$

  and 𝓧 is the **random Siegel transform** *(their Lemma 1.2, quoted exactly)*:

$$\mathcal{X}(L, \chi) \;=\; \lim_{R\to\infty}
\sum_{\substack{w \in L\setminus\{0\} \\ \|w\| \le R}} \frac{\sin\big(2\pi\chi(w)\big)}{y(w)}\; e^{-\|x(w)\|^2}$$

  Here (L, χ) is a **marked unimodular lattice** in ℝ^d (§5.5), distributed according to Haar
  measure on 𝓜; y(w) is the **first** coordinate of w and x(w) the remaining d−1. The sum does
  **not** converge absolutely — it is conditionally convergent, and the paper proves the limit
  exists for almost every (L, χ) by any reasonable summation method.

**The two properties that make this worth knowing:**

> **The law of 𝓧 depends neither on the density you put on the parameters, nor on z.** It is
> universal.

and its practical consequence, which he states in exactly these terms:

> **If you know your atoms and probabilities to ten decimal places, you still do not know the
> error in the expansion for large n.** The information you are missing is not more decimal
> places. It is the *arithmetic* of the parameters, and no finite precision resolves it.

That is a genuinely useful thing to have been told.

**Where the lattice comes from — the dynamical correspondence.** He shows this and it is
clean enough to reconstruct.

By scaling, assume the first value is 0 and the last is 2π. Then the characteristic function
can be close to 1 only near integer points, and, writing c₁, …, c_{d−1} for the remaining
rescaled values, a **resonance** is an integer k for which every c_j k is close to an integer
— close to within **n^(−1/2)**.

*Why n^(−1/2)?* He gives the reason in one line: cos θ = 1 − θ²/2 + …, so a phase error θ costs
a factor (1 − θ²/2) per term, and over n terms that is negligible exactly when nθ² ≲ 1, i.e.
θ ≲ n^(−1/2). **The resonance width is set by the number of terms.**

Now record each resonance by the integer vector (k, m₁, …, m_{d−1}) where m_j is the nearest
integer to −c_j k. Apply the unipotent matrix with 1's on the diagonal and the c_j in the last
column — this maps the vector to (m_j + c_j k)_j and k, i.e. to the *distances* rather than the
integers. Then apply the diagonal matrix with √n in the first d−1 slots and n^(−(d−1)/2) in the
last, which has determinant 1 and puts everything on the right scale (the distances must be
measured at scale n^(−1/2); k ranges up to n^{d−1}).

The result: **the set of resonances is the set of lattice points of a specific unimodular
lattice inside a fixed box** — first d−1 coordinates bounded by R, last coordinate in [0,1].
Counting them is applying the Siegel transform of an indicator function.

> **So the resonances of an i.i.d. sum *are* the short vectors of a lattice, and the lattice
> is determined by the parameters.**

The proof of the limit law is then **equidistribution**: as the parameters vary with a smooth
density, the image lattice equidistributes in the space of lattices with respect to Haar
measure, and the limiting random variable is the Siegel transform of a random lattice. For
Kesten-type Cauchy laws you use the same action but replace mixing/equidistribution with a
**Poisson limit theorem** — "again we use the chaotic nature of the dynamics of these
**diagonal flows** on the space of lattices."

*[Gap: one slide passed quickly — the statement that when the random variable takes several
values, the possible values of the sum are values of a **linear form in d variables**, weighted
by multinomial coefficients, and that with **equal weights** you get a Kesten-type Cauchy
distribution instead. He attributes the equal-weight result to a pair of authors that the
captions render as "some fire and Zolotarev". **I could not identify either name and I do not
guess.** **Impact: low** — it is a remark on a special case, not part of the main line.]*

### 7.5 The synthesis

He closes by putting the two ends of the spectrum side by side, and this is the passage that
justifies the four R's in the proceedings title.

| | i.i.d. sums | quasi-periodic sums |
|---|---|---|
| character | the **most random** sequence | the **most regular** sequence |
| growth of the sum | ≍ √n | ≍ (log n)^power |
| renormalization | S ↦ S * S, rescaled — **convolution** | 𝕋^d = ℝ^d/L, L ↦ AL — **change the lattice** |
| what dominates | a few resonant harmonics | a few resonant harmonics |
| individual contribution | Laplace, 200 years ago | Laplace, 200 years ago |
| what is still needed | the **geometry** of the resonances | the **geometry** of the resonances |

And then the punchline:

> "If we pass to the Fourier transform and look at how renormalization acts on Fourier
> harmonics, we see that **this action is exactly the same**. We have marked lattices, so each
> lattice point has a certain phase associated with it, and we have a linear action on this.
> This allows us to build a **dictionary** between these two problems."

The evidence he gives for the dictionary being useful rather than decorative is historical:
**the random Siegel transform appeared first** in the study of discrepancy for toral
translations, and then turned out to describe the Edgeworth error for **independent**
sequences. A tool built at one end of the spectrum solved a problem at the other.

His own summary of why any of this is possible: the two families "are opposite ends of the
spectrum, one most random and the other most regular, but what we have in common is that we
have **a lot of hidden symmetries** which allow us to do computation."

And the open problem he leaves: **the conditions for uniform distribution of the discrepancy
when α is not of bounded type are unknown.**

---

## 8. The one argument: why √log N for bounded type and log N for typical α

This is the single calculation in the talk that you can do yourself, it explains the most
striking fact in it, and Dolgopyat presents it as the explanation. It is his §"why we have
different scaling", restored.

**Setup.** The discrepancy's k-th Fourier harmonic contributes an amount governed by

$$\frac{1}{k\,|\sin \pi k \alpha|}$$

and only harmonics with **k ≲ N** matter. He gives the reason for the cutoff: for k > N the
denominator can be small, of order 1/k, but then the numerator is small too, "so you will not
get any improvement in your sum."

Call k a **resonance at level ε** if k·|sin πkα| ≲ ε. Since |sin πkα| ≍ ‖kα‖ (distance to the
nearest integer), this says k·‖kα‖ ≲ ε.

**Case 1: α of bounded type.** By definition k‖kα‖ ≥ c > 0 for every k. So

> **k·|sin πkα| is uniformly bounded below.** There are no strong resonances at all.

The harmonics that come closest to resonance are the **continued-fraction denominators** q_j
(he calls them "prime resonances"), the best rational approximations. For bounded type these
grow at least geometrically, so the number of them below N is

$$\#\{j : q_j \le N\} \;\asymp\; \log N$$

Each contributes an amount of order 1, with a sign. Some are positive, some negative, and the
signs behave like a weakly dependent sequence — which is exactly what §7.3's renormalization
argument proves. Hence **cancellation**, hence

$$D_N \;\sim\; \sqrt{\log N}$$

**Case 2: α uniform on the torus.** Now kα is equidistributed mod 1, so for fixed k,
ℙ(‖kα‖ ≤ ε/k) ≈ 2ε/k. First-moment count:

$$\mathbb{E}\,\#\{k \le N : k\|k\alpha\| \le \varepsilon\}
\;\approx\; \sum_{k \le N} \frac{2\varepsilon}{k} \;\approx\; 2\varepsilon \log N$$

**Choose ε so that this count is of order 1**: ε ≍ 1/log N. Then there are **O(1)** harmonics
with k·‖kα‖ ≍ 1/log N, and each of them contributes an amount of order

$$\frac{1}{k\|k\alpha\|} \;\asymp\; \log N$$

So instead of log N terms of size 1 that cancel down to √log N, you have **O(1) terms of size
log N** and nothing to cancel against. The sum is dominated by a *bounded number of large
contributions*, and the number of them is asymptotically **Poisson**.

$$D_N \;\sim\; \log N$$

**And the limit law follows from the shape of that sum.** A sum dominated by a few terms whose
sizes are 1/(small quantity), with the small quantity roughly uniform, is a sum of
reciprocals of near-uniform variables — the classic recipe for a **stable law of index 1**,
which is the Cauchy distribution. That is why Kesten and Dolgopyat–Fayad get Cauchy and Beck
gets Gaussian. As he says: **"the key step in the proof of the Cauchy limit theorem is a
Poisson limit theorem for the number of strong resonances."**

**State the general principle, because it is the transferable one.**

> **Many comparable contributions ⟹ Gaussian, with cancellation, at scale √(number).
> A bounded number of dominant contributions ⟹ heavy-tailed, no cancellation, at the scale of
> the largest.**

The Feller–Lindeberg condition is precisely the formal statement of "no single term
dominates," and §7.3 told you exactly where it fails: bounded type keeps the additive
functional bounded, and a typical α does not.

---

## 9. Do this by hand

Three exercises. The first is the one that must land.

### 9.1 The resonance count (25 minutes, pen)

**(a)** Let α be of bounded type, so k‖kα‖ ≥ c for all k ≥ 1. Show that the number of
continued-fraction denominators q_j ≤ N is O(log N), and that it is also ≳ log N. *(Use the
recursion q_{j+1} = a_{j+1} q_j + q_{j−1} with 1 ≤ a_j ≤ A.)*

**(b)** Let α be uniform on [0,1). For fixed k ≥ 1, compute ℙ(‖kα‖ ≤ δ) exactly.

**(c)** Using (b), estimate the expected number of k ≤ N with k‖kα‖ ≤ ε. Then choose ε so
that this expectation is 1, and say how large the corresponding harmonic's contribution
1/(k‖kα‖) is.

**(d)** Explain in one sentence each why (a) gives √log N and (c) gives log N.

<details>
<summary>Solutions</summary>

**(a)** From q_{j+1} = a_{j+1} q_j + q_{j−1} ≥ q_j + q_{j−1} we get q_{j+1} ≥ q_j + q_{j−1},
so q_j grows at least like the Fibonacci numbers: q_j ≳ φ^j with φ the golden ratio. Hence
q_j ≤ N forces j ≲ log N / log φ. For the lower bound, boundedness of the partial quotients
gives q_{j+1} ≤ (A+1) q_j, so q_j ≤ (A+1)^j and j ≳ log N / log(A+1). Both bounds are
constant multiples of log N, so the count is **≍ log N**. Note that the *upper* bound holds
for every irrational α; it is the **lower** bound that needs bounded type. That asymmetry is
the whole point: for a general α the denominators can jump, and a single enormous partial
quotient a_{j+1} means q_j approximates α extraordinarily well — one huge resonance.

**(b)** ‖kα‖ ≤ δ means kα mod 1 lies in [0,δ] ∪ [1−δ, 1). Since α ↦ kα mod 1 pushes the
uniform measure on [0,1) to the uniform measure on [0,1) (it wraps k times), the probability
is exactly **2δ** for δ < 1/2.

**(c)** Set δ = ε/k in (b): ℙ(k‖kα‖ ≤ ε) = 2ε/k. Sum over k ≤ N:

$$\sum_{k=1}^{N}\frac{2\varepsilon}{k} \;=\; 2\varepsilon\big(\log N + \gamma + o(1)\big) \;\approx\; 2\varepsilon\log N$$

Setting this equal to 1 gives **ε ≈ 1/(2 log N)**. Such a harmonic contributes
1/(k‖kα‖) ≍ 1/ε ≍ **log N**.

**(d)** Bounded type: ≍ log N resonant harmonics, each of size O(1), signs varying — a sum of
log N comparable weakly-dependent terms, so the CLT applies and the total is ≍ **√log N**.
Typical α: O(1) harmonics of size ≍ log N with nothing to cancel them, so the total is
≍ **log N**, and because the count of near-resonances is Poisson and the sizes are
reciprocals of near-uniform quantities, the limit is **Cauchy** rather than Gaussian.

**The thing to take away.** The exponent was never exotic. √log versus log is the difference
between *many small contributions that cancel* and *a few large ones that do not*, and the
Diophantine condition is exactly the statement that no contribution is allowed to be large.
</details>

### 9.2 Why an Edgeworth expansion of order d is impossible (15 minutes, pen)

Let X take d+1 values a₁, …, a_{d+1} with probabilities p₁, …, p_{d+1} and mean zero.

**(a)** Write P(S_n ≤ z) as a sum over (m₁, …, m_{d+1}) with Σ m_i = n. Which multinomial
terms appear?

**(b)** Consider the ℤ^d random walk that jumps to e_i with probability p_i (i = 1, …, d) and
stays at 0 with probability p_{d+1}. What does the *local* central limit theorem say about the
probability that it is at a given site after n steps, in the bulk?

**(c)** Deduce that P(S_n ≤ z) has jumps of size ≍ n^{−d/2}.

**(d)** Conclude that the order-d Edgeworth expansion cannot hold — and say why order d−1 is
not immediately excluded by the same argument.

<details>
<summary>Solutions</summary>

**(a)** The terms are the multinomial probabilities

$$\frac{n!}{m_1!\cdots m_{d+1}!}\,p_1^{m_1}\cdots p_{d+1}^{m_{d+1}}$$

summed over all compositions of n with Σ m_i a_i ≤ z. Note S_n is determined by the *counts*
m_i, and the constraint Σ m_i = n means the state lives in a d-dimensional lattice, not a
(d+1)-dimensional one. **That d is the d in n^{−d/2}.**

**(b)** The vector (m₁, …, m_d) after n steps is a d-dimensional random walk with mean n·p and
covariance of order n. The local CLT says the probability of any particular site within O(√n)
of the mean is ≍ n^{−d/2} — a d-dimensional Gaussian density (∝ n^{−d/2}) times the unit cell
volume 1. This is exactly Dolgopyat–Fernando's observation that

$$n^{d/2}\,\frac{n!}{m_1!\cdots m_{d+1}!}\,p_1^{m_1}\cdots p_{d+1}^{m_{d+1}}$$

is uniformly bounded **below** when Σ m_i a_i = n Σ a_i p_i + O(√n).

**(c)** Each attainable value of S_n therefore carries mass ≍ n^{−d/2}, so the distribution
function P(S_n ≤ z) — as a function of z — has jumps of that size at each attainable value.

**(d)** E_d(z) is smooth in z. At a jump point of size c·n^{−d/2}, a smooth function cannot be
within o(n^{−d/2}) of both the left and the right limit; the two differ by c·n^{−d/2}. So the
order-d expansion fails for every parameter choice. It does **not** exclude order d−1, because
the requirement there is only o(n^{−(d−1)/2}), and n^{−d/2} = o(n^{−(d−1)/2}). The jumps are
one power of √n too small to matter at order d−1 — which is exactly why Dolgopyat and Fernando
can prove order d−1 holds for almost every parameter, and why the failure at order d is by
*precisely* the smallest amount the jump argument allows.
</details>

### 9.3 The staircase is the discrepancy (10 minutes, paper and pencil)

Draw four bricks of the staircase (2 × 1 rectangles, each offset half a brick to the right and
one unit up relative to the previous). Take the Poincaré map on the top edges from §5.4:

$$(x, z) \;\longmapsto\; \Big(x + \alpha,\ z + \mathbb{1}_{[1/2, 1)}(x) - \mathbb{1}_{[0, 1/2)}(x)\Big)$$

**(a)** Iterate from (x₀, 0) and write z_n as a sum.

**(b)** Express z_n in terms of the discrepancy D_n(I, R_α, x₀) of the rotation with respect to
I = [1/2, 1).

**(c)** The affine automorphism ψ_A has *zero drift*, ∫τ = 0. What is the probabilistic
content of that condition, and what would go wrong without it?

<details>
<summary>Solutions</summary>

**(a)** z_n = Σ_{j=0}^{n−1} [𝟙_{[1/2,1)}(x₀ + jα) − 𝟙_{[0,1/2)}(x₀ + jα)], since the first
coordinate is just the rotation.

**(b)** Every term is ±1, and the two indicator counts sum to n. Writing V_n for the number of
visits to [1/2, 1), we get z_n = V_n − (n − V_n) = 2V_n − n = 2(V_n − n/2) = **2·D_n([1/2,1),
R_α, x₀)**, since |I| = 1/2. So the brick index is exactly twice the discrepancy for the
half-circle. This is why ℓ = 1/2 is the case the staircase handles, and why other ℓ needs
either a different surface or the continued-fraction/Ostrowski route of Bromberg–Ulcigrai.

**(c)** Zero drift means the renormalization step is, on average, **level-preserving**: the
orbit is equally likely to be pushed up or down the staircase. If ∫τ ≠ 0 the Birkhoff sum
Σ_{j≤m} τ(A^{−j}q) would have a linear-in-m mean, i.e. a term of order log N with a
deterministic coefficient, which would swamp the √log N fluctuation entirely. Zero drift is
what makes the fluctuation the leading interesting object rather than a correction. (Compare
Beck's constant C(α,ℓ)·log N: a genuine drift term does appear there, from the geometry of the
arc rather than from the renormalization, and it does exactly what I just described — it
dominates the fluctuation and forces a definite sign 99.9% of the time.)
</details>

---

## 10. What is actually useful to you

Six things, in order of how often you will reach for them.

### 10.1 The scaling exponent counts renormalization steps

The most memorable fact in the talk is that the discrepancy of a circle rotation fluctuates
like √log N. It looks exotic until you see §7.3: the argument reduces N steps of the rotation
to **log N steps of a renormalization map**, and then applies the ordinary central limit
theorem to a sum of log N terms. √log N is just √(number of terms).

Generalize the move: **when you see an unusual exponent, ask what is being counted.** A
√log means something logarithmic is being summed. A log N without a square root means the
sum is dominated by O(1) terms rather than log N of them. The exponent is a census, not a
mystery.

### 10.2 Gaussian versus heavy-tailed is a question about domination, and it is diagnosable

§8 is a diagnostic you can run on any aggregate quantity — a latency distribution, a cost
metric, an eval score averaged over a suite:

- **Many comparable contributions that partially cancel ⟹ Gaussian, scale √(count).**
- **A bounded number of dominant contributions ⟹ heavy-tailed, scale = size of the largest.**

The formal version is the Feller–Lindeberg condition: no single term is large compared to the
total. And the talk shows the two regimes are separated by an *arithmetic* condition on a
parameter — the same system is Gaussian or Cauchy depending on how well a number is
approximable by rationals. That is worth internalizing: **the tail behaviour of an aggregate
can be controlled by a structural property of the system that has nothing to do with any
individual term's distribution.**

Applied to your work: if an agent-system metric has a heavy tail, "the average case got
worse" is usually the wrong model. The right question is which small set of inputs dominates
the sum, and what property of those inputs makes them dominant.

### 10.3 Classify the obstructions instead of assuming them away

This is the methodological idea I would take out of §7.1, and it is a genuinely different way
of writing a theorem.

The conventional form is: *assume A, B, C; conclude the limit theorem.* Dolgopyat and Sarig
instead **enumerate a complete list of the ways the conclusion can fail** — lattice,
center-tight, reducible — prove the list is complete, and then supply a **computable test**
(the structure constants d_n(ξ), built from the transition kernels and the observable) that
decides which obstruction is present.

The difference in practice is large:

- A sufficient condition tells you when you are safe. A complete obstruction list tells you
  what to *check*, and tells you what happens in each failure mode instead of leaving you
  with nothing.
- The test is computable from the model's data, not from the answer.

For agent systems the translation is direct. "Here are the conditions under which the pipeline
is correct" is weaker and less useful than "here are the four ways it can fail, here is a
check that tells you which one you are in, and here is what each failure actually produces."
The second is a debuggable specification; the first is a hope.

### 10.4 Finite precision does not resolve arithmetic

§7.4 has a claim you should be able to state to someone else: for a sum of i.i.d. variables
with three or more atoms, **knowing the atoms and probabilities to ten decimal places tells
you nothing about the error term for large n**. The error's limit law is universal and depends
on the parameters only through where they sit relative to a lattice — a property that no finite
number of decimal places determines.

This is a sharper version of an intuition you already have about chaotic systems, and it is
sharper in a useful direction: it is not that small errors *grow*, it is that the quantity you
want is **not a continuous function of the parameters at all**. More precision does not
converge on the answer. If you find yourself adding significant figures and the output keeps
jumping, consider that you may be measuring a discontinuous functional and no amount of
precision will help.

### 10.5 Build a dictionary between the two extremes of your problem

The structural achievement of the talk is that the *most random* and the *most regular*
systems turn out to have the same renormalization action on the Fourier side, so a tool built
for one solves problems in the other — the random Siegel transform was invented for rotations
and now describes Edgeworth errors for i.i.d. sums.

The general move: when you have two regimes that look opposite, **look for the object each
one's renormalization acts on, and check whether the actions coincide.** Otto's talk at the
same congress makes the same point from the other side — singular SPDE and stochastic
homogenization look opposite and are the same problem — and §8.5 of
`geometric-concepts-pde-otto.md` in this folder develops it. Two plenaries, one lesson: the
opposite of your problem is often your problem.

### 10.6 The two remarks about agents, reported because he made them

He opened with:

> "I think maybe next ICM most people would send their digital agents to record the talks
> during weekends, but now it's nice to see a live audience."

and, when he ran out of time to present the proof of the main new theorem:

> "The proofs are kind of long, so I don't have time to show it. **You can ask maybe your
> virtual assistant.**"

Both are jokes. The second is also a fact about this document: the proof he declined to give
is the one part of the talk I could not restore, because it exists in no paper I can find
(§7.3). The assistant's honest answer is that it does not know either.

---

## 11. Where to read next

1. **Dolgopyat and Sarig, *Local Limit Theorems for Inhomogeneous Markov Chains*,** Springer
   LNM **2331** (2023); free at [arXiv:2109.05560](https://arxiv.org/abs/2109.05560). The
   companion for part one, and the most self-contained item in the list — it has appendices
   with background, worked examples, and a historical account. Chapters 3 and 4 are the ones
   §7.1 restores. Start here if you want *one* thing.
2. **Dolgopyat and Fayad, *Limit theorems for toral translations*,** Proc. Sympos. Pure Math.
   **89** (2015) 227–277; [arXiv:2006.11748](https://arxiv.org/abs/2006.11748). The companion
   for part two: Beck's theorem, Kesten's theorem, the staircase surface in §8.5, and — this
   is its distinctive feature — **fifty-six open questions**, numbered, several of which are
   the ones the talk says are still open. Read it for the questions if nothing else.
3. **Dolgopyat and Fernando, *An error term in the Central Limit Theorem for sums of discrete
   random variables*,** [arXiv:2303.10235](https://arxiv.org/abs/2303.10235), IMRN **2023**
   no. 21, 18664–18713. Part three in full, thirty-odd pages, and the place to see the random
   Siegel transform constructed rather than asserted. §9 of that paper is where Rogers'
   mean-value identity does the work.

---

## 12. Self-test

<details>
<summary>1. What does the local limit theorem say that the central limit theorem does not, and what is the only obstruction in the i.i.d. case?</summary>

The CLT controls the probability of landing in an interval of length comparable to the
standard deviation σ_n. The **local** limit theorem controls intervals of length **O(1)**,
asserting P(S_n − zσ_n ∈ (a,b)) ≈ φ(z)(b−a)/σ_n. Dolgopyat's gloss: zoom in near the mean and
you should see **Lebesgue measure = Haar measure on ℝ**. The only obstruction (Gnedenko–Stone)
is the lattice one: if the variables live on a shifted lattice tℤ, no interval avoiding the
lattice can have the predicted mass, and the local picture is Haar measure on the shifted
subgroup instead of on ℝ.
</details>

<details>
<summary>2. In the inhomogeneous Markov setting, what are the three obstructions, and what is the "resonance group"?</summary>

**(I) Lattice behaviour** — the algebraic range is tℤ. **(II) Center-tightness** — S_N minus
centring constants is tight, equivalently Var(S_N) stays bounded; equivalently (Theorem 3.8 of
the companion) f = ∇a + h with a a bounded potential and h of summable variance. **(III)
Reducibility** — f = g + c with c center-tight and the range of g strictly smaller. If none
occurs, all the classical asymptotics hold.

The resonance group is the **co-range** H(X,f) = {ξ : Σ_n d_n(ξ)² < ∞}, where the structure
constants d_n(ξ)² = E|e^{iξΓ(P)} − 1|² measure how far the frequency ξ is from being killed by
the chain. It is a closed subgroup of ℝ, hence ℝ (center-tight, no CLT), {0} (ordinary LLT),
or tℤ (lattice LLT on the sublattice (2π/t)ℤ).
</details>

<details>
<summary>3. Why is a circle rotation the "opposite end of the spectrum" from a hyperbolic toral automorphism, and why is a limit theorem for it surprising?</summary>

A hyperbolic toral automorphism separates nearby orbits **exponentially**, which is the
standard explanation for why a deterministic system behaves randomly — finite precision is
destroyed at an exponential rate. A rotation is an **isometry**: distances between orbits are
constant forever, nothing is unstable, and the standard mechanism is entirely absent. It is
surprising that a central limit theorem holds at all; it is more surprising that the
normalization is √log N rather than √N, i.e. the fluctuations are exponentially smaller.
</details>

<details>
<summary>4. State Beck's theorem, and name the two things about it Dolgopyat calls surprising.</summary>

For α a quadratic irrational, ℓ **rational**, initial point 0, and M uniform on {1,…,N}:
(D_M([0,ℓ],α,0) − C(α,ℓ)log N)/√(log N) converges to a centred Gaussian with variance
σ²(α,ℓ). Randomness comes only from the **time** M — a *temporal* limit theorem.

Surprise one: the normalization is **√log N**, not √N. Surprise two: there is a **drift**
C(α,ℓ)·log N even though the mean was already subtracted, and it is much larger than the
fluctuation — so if C > 0 the discrepancy is positive 99.9% of the time. C vanishes for some
quadratic irrationals (he says the golden mean and √3) and not others (√2, √7), and depends on
special values of an L-function.
</details>

<details>
<summary>5. Where does √log N come from, mechanically?</summary>

From renormalization. Pass to the staircase surface, where the discrepancy is the height
(brick index) of a straight line of slope β = 2α−1. Apply the surface's affine automorphism
ψ_A^{−1} repeatedly to shrink a length-N segment to length 1; since ψ_A expands by λ each time,
this takes **m ≍ log N/log λ** steps. The height is then a Birkhoff sum Σ_{j≤m} τ(A^{−j}q)
over the hyperbolic toral automorphism A — a sum of **log N** weakly dependent terms. Its
fluctuation is √(log N). The exponent is the number of renormalization steps.
</details>

<details>
<summary>6. Why does a typical α give log N and Cauchy instead of √log N and Gaussian?</summary>

Resonance counting. The k-th harmonic contributes ≍ 1/(k|sin πkα|). For α of **bounded type**
k‖kα‖ ≥ c, so no term is large; the ≍ log N continued-fraction denominators below N each
contribute O(1) with varying signs, and cancellation gives √log N (CLT). For **uniform** α,
E#{k ≤ N : k‖kα‖ ≤ ε} ≈ 2ε log N; taking ε ≍ 1/log N makes this O(1), so there are **O(1)
harmonics each of size ≍ log N** and nothing cancels. The count of strong resonances is
**Poisson**, the sizes are reciprocals of near-uniform quantities, and the limit is the
**Cauchy** distribution at scale log N. Formally: bounded type keeps the additive functional
bounded, hence the Feller–Lindeberg condition holds; a typical α breaks it.
</details>

<details>
<summary>7. Why does a distribution with d+1 atoms never admit an order-d Edgeworth expansion?</summary>

S_n's values are Σ m_i a_i with Σ m_i = n, and the multinomial weights are the transition
probabilities of a d-dimensional lattice random walk. The **local** CLT for that walk says
each attainable value carries mass ≍ n^{−d/2}, so the distribution function has jumps of size
≍ n^{−d/2}. But E_d(z) is smooth in z, and a smooth function cannot approximate both sides of
a jump of size c·n^{−d/2} to accuracy o(n^{−d/2}). Order d−1 survives, because n^{−d/2} is
o(n^{−(d−1)/2}).
</details>

<details>
<summary>8. What is the random Siegel transform, and what is universal about it?</summary>

A **marked unimodular lattice** is a pair (L, χ) with L ⊂ ℝ^d of covolume 1 and χ : L → 𝕋 a
character; the space of these is (SL_d(ℝ) ⋉ ℝ^d)/(SL_d(ℤ) ⋉ ℤ^d) with Haar measure. The random
variable is

𝓧(L,χ) = lim_{R→∞} Σ_{w ∈ L\{0}, ‖w‖≤R} sin(2πχ(w))/y(w) · e^{−‖x(w)‖²},

with y(w) the first coordinate and x(w) the other d−1; the sum converges conditionally. It is
the limit law of the (rescaled) failure of the order-d Edgeworth expansion, and it is
**universal**: its distribution depends neither on the density placed on the model's
parameters nor on the point z. Concretely, knowing your atoms and probabilities to ten decimal
places tells you nothing about the error for large n.
</details>

<details>
<summary>9. What is the "dynamical correspondence" that turns resonances into lattice points?</summary>

Normalize the first value to 0 and the last to 2π. A resonance is an integer k for which every
rescaled remaining value c_j satisfies dist(c_j k, ℤ) ≲ n^{−1/2} — the width is n^{−1/2}
because cos θ ≈ 1 − θ²/2 and n·θ² ≲ 1. Encode a resonance by (k, m₁, …, m_{d−1}) with m_j the
nearest integer, apply the unipotent matrix with 1's on the diagonal and the c_j in the last
column (turning integers into distances), then the determinant-one diagonal matrix
diag(√n, …, √n, n^{−(d−1)/2}). Resonances become **lattice points of a unimodular lattice inside
a fixed box**; counting them is the Siegel transform of an indicator; and the limit law follows
from **equidistribution** of that lattice in the space of lattices (or, for Cauchy-type laws, a
**Poisson limit theorem** for the same diagonal action).
</details>

<details>
<summary>10. What is the single structural claim the whole talk argues for?</summary>

That i.i.d. sums (the most random sequence) and quasi-periodic sums (the most regular) are
governed by **the same object**. Both are studied by renormalization — convolution-and-rescale
for sums, change-of-lattice for rotations — and although the two renormalizations look
unrelated, on the **Fourier** side both are the same **linear action on marked lattices**: a
lattice of harmonics, each carrying a phase. That correspondence is a dictionary, and the
evidence that it is real rather than cosmetic is historical: the random Siegel transform was
invented to describe discrepancy for toral translations and turned out to describe the
Edgeworth error for independent sums. In both cases the leading contribution comes from a
**small number of resonant harmonics**; Laplace handled one harmonic 200 years ago; what is
new is the **geometry of the set of resonances**.
</details>

---

## 13. Note on the tutorial process

**Difficulty versus reputation: Rule 1 fires, hard.** Dolgopyat is famous for **Dolgopyat's
method** — exponential decay of correlations for Anosov flows, transfer operators, spectral
methods for hyperbolic systems. His introducer spends a full sentence on it. **None of it
appears in the talk.** He mentions hyperbolic systems only to set them aside, in as many
words: *"I'm not going to discuss this kind of dynamical systems in my talk, because it's
quite well understood what is causing this stochastic behaviour."* Reputation would have
predicted a difficulty-5 talk on transfer operators and spectral gaps. The actual talk is a
probability talk about limit theorems, whose hardest object is the space of lattices, and
whose first third is very close to material the reader already owns. Predicted 3; delivered
3, but for entirely different reasons than a reputation-based guess would have given.

**Anchors: what I used and what I rejected.**

- **Used, and handed over by the speaker:** the central limit theorem as a
  **renormalization-group fixed point** — his own closing summary describes 𝓡[μ] = (μ * μ)
  rescaled, in words, as the renormalization transformation for sums. This is the
  best-supported anchor in the talk and it is his, not mine.
- **Used, supported by the primary literature:** **small divisors**. The denominators
  k·sin(πkα) are spoken aloud; Dolgopyat–Fayad's GAFA abstract uses the phrase "the small
  divisors in the Fourier series of the discrepancy function".
- **Rejected: billiards and the Lorentz gas.** My brief proposed them as the statistical-
  mechanics bridge. They are absent from the talk — not mentioned once. I have not used them.
- **Rejected: transfer operators and hyperbolic dynamics as a subject.** Present only as a
  tool inside one proof (§7.3 needs a Markov partition for a cat map) and explicitly declined
  as a topic.
- **Named as absent: KAM theory.** The small-divisor apparatus is genuinely here and it is the
  reader's natural association, so §2.2 states plainly that KAM itself — the theorem, the
  name, invariant tori — never appears. Decorating the talk with it would have been the
  subtler kind of fabrication.

**Name corrections.** Auto-captions destroy essentially every proper noun. Each correction
below is anchored to a located publication, except the two marked *unverified*.

| Caption | Correct | how it was resolved |
|---|---|---|
| "Amrit Serik" | **Omri Sarig** | co-author of LNM 2331, the theorem he describes |
| "Konyukhovsky" | **Adam Kanigowski** | Dolgopyat–Kanigowski–Rodriguez Hertz, *Exponential mixing implies Bernoulli*, Ann. of Math. **199** (2024) 1225–1292 |
| "Rodriguez Hertz" | **Federico Rodriguez Hertz** | same paper |
| "Gaston Fernandez" | **Kasun Fernando** | arXiv:2303.10235, the Edgeworth paper |
| "Bromberg and Tsuchigai" | Michael Bromberg and **Corinna Ulcigrai** | arXiv:1705.06484 |
| "Joseph Beck" | **József Beck** | Period. Math. Hungar. 60/62 |
| "Huber Huber and Barakh Weiss" | **Hooper, Hubert and Weiss** | *Dynamics on the infinite staircase*, DCDS-A **33** (2013) 4341–4347 (survey ref. [53]) |
| "Ben Borda" | **Bence Borda** | J. Mod. Dyn. **21** (2025) 327–359 |
| "proven by SN in 1945" | **Esseen** (Carl-Gustav Esseen) | Acta Math. **77** (1945) 1–125, ref. [6] of Dolgopyat–Fernando |
| "Zeglin transform", "Ziggurat distribution" | **Siegel** transform | he says "Siegel transform" correctly later in the same passage |
| "Jerôme Buzzi" | **Jérôme Buzzi** | ICM 2026 lecture, named from the podium |
| "Adler and Weiss" | Roy **Adler** and Benjamin **Weiss** | Markov partitions, ~1967 |
| "Kolmogorov free series theorem" | Kolmogorov **three-series** theorem | — |
| "hard measure" | **Haar** measure | — |
| "failure Lindeberg condition" | **Feller–Lindeberg** condition | — |
| "boundary type" (throughout) | **bounded type** | standard term; matches the stated inequality |
| "after more phase", "total after more phase" | **automorphism**, **toral automorphism** | — |
| "Edgeworth extension" | Edgeworth **expansion** | — |
| "Cramer" | **Cramér** | — |
| "Dabrowski and Gorodetsky" | ***unverified*** | see below |
| "some fire and Zolotarev" | ***unverified*** | see below |
| "William Orange is a closed subgroup of ℝ" | ***garbled beyond recovery*** | the object is unambiguous from context — the group of resonances, i.e. the co-range — but I cannot recover the words |

**The two names I did not guess.**

- **"Dabrowski and Gorodetsky."** Attributed by Dolgopyat to a theorem saying the only
  obstruction to the CLT is a decomposition into constant + gradient + convergent parts. No
  such pair appears in the companion book's 200-item bibliography. What the book *does*
  attribute: the CLT for uniformly elliptic inhomogeneous Markov arrays is **Dobrushin's**
  (their Theorem 3.10, proved following Sethuraman–Varadhan); the constant + gradient +
  summable-variance characterization is **their own Theorem 3.8**, which they explicitly call
  new for the inhomogeneous setting; and the technique behind both is **Gordin's**
  martingale–coboundary decomposition. "Dobrushin and Gordin" is the phonetically plausible
  reading. It is a coin flip and I have not written it into the text.
- **"Some fire and Zolotarev."** Attributed a Kesten-type Cauchy limit for the equal-weight
  case of the linear-form picture in part three. I could not identify either name. Reported as
  a gap in §7.4.

**Substantive caption corrections, not just spellings.**

1. **Beck's theorem: "interval L to be a irrational number" → ℓ RATIONAL.** This is the
   important one, because the whole later structure depends on it. Two confirmations: the
   Dolgopyat–Fayad survey's Theorem 8(b) states ℓ rational; and Bromberg–Ulcigrai's abstract
   describes Beck's hypotheses as "α quadratic irrational, β rational and the initial point
   the origin," their contribution being to cover irrational β. Internal consistency clinches
   it: Dolgopyat says of the Bromberg–Ulcigrai condition "if L is rational then this always
   holds… just from the definition of bounded type", which only makes sense if rational ℓ is
   the *already known* case.
2. **"the sum of 10 terms converges to the Gaussian"** → the sum of **n** terms. Caption
   mis-hearing of "n".
3. **"each sum ends take only two values"** → each **summand** takes only two values.
4. **"we know the initial condition up to error 10 to the 10"** → 10^(−10). He immediately
   glosses it as "we know the first 10 digits," which fixes the sign of the exponent.

**Where the mathematics is unrecoverable, and how bad it is.**

- **The main new theorem of part two (§7.3): sign changes in the even continued fraction
  expansion of β = 2α−1.** No preprint on arXiv (I enumerated every Dolgopyat arXiv entry
  through May 2026), nothing on his publication page, **no coauthors named aloud**. I have the
  shape of both conditions (sublinear growth of sign changes; growth slower than √n) and the
  random-walk analogy he gives, and nothing else — not the precise definition of a sign
  change, not the role of the initial point, not the general-ℓ statement. **Impact:
  moderate-to-structural.** This is the newest result in the talk and it is the one thing here
  a reader cannot follow up.
- **Every displayed formula on every slide.** The talk showed the De Moivre–Laplace
  approximation, the Edgeworth polynomials, the reducible-case Markov formula, the discrepancy
  Fourier expansion, the staircase picture, the Poincaré map, the resonance matrices, and the
  Siegel-transform definition. **The caption track carries none of them.** Where I display a
  formula it is (i) quoted from a located paper with the citation attached, (ii) reconstructed
  from spoken narration and labelled as such, or (iii) marked as a gap. I have restored more
  than usual — the co-range and structure constants from LNM 2331, the staircase Poincaré map
  and the affine-automorphism property from the survey, the entire Siegel-transform apparatus
  from arXiv:2303.10235 — but each restoration is from a *paper*, never from a guess.
- **Beck's drift constant vanishing for the golden mean and √3 and not for √2 and √7, and its
  connection to L-functions.** Stated aloud; not verified. **Impact: low** — illustration only.
- **The reducible-case asymptotic formula for Markov chains.** He explicitly declines to write
  it. **Impact: low** — it is Chapter 6 of the companion.
- **The equal-weights linear-form slide and its attribution.** Passed over quickly; attribution
  unverifiable. **Impact: low.**

**Where the companion is not infallible.** Dolgopyat–Fernando (arXiv:2303.10235) defines the
marking χ as a "**homeomorphism** χ : L → 𝕋" — twice, in §1. A homeomorphism from a discrete
lattice to a circle does not exist; the intended word is **homomorphism**, i.e. a character,
which is what the surrounding text (linear functional χ̃, "characters", the action of (ℝ^d)*)
makes unambiguous. Dolgopyat says "the character, which is like a homomorphism from L to the
torus" from the podium, which settles it. I use *homomorphism* in §5.5 and note the paper's
typo here.

**One inference of mine, flagged.** §5.4 observes that the staircase's affine symmetry group
is the theta group {A ≡ I mod 2} and that the even continued fraction algorithm is the
continued-fraction algorithm of that group — which is why §5.3's even expansions appear at all.
Dolgopyat never says this. It is forced by putting two of his statements side by side, and it
is labelled as my inference in the text rather than as his.

**Cross-references rather than rebuilds.** The renormalization-group background for §2.1 is in
`random-interface-growth-quastel.md` §7.2 and I do not reproduce it. The general framework of
homogeneous spaces Γ\G, flows as right translations, and mixing implying equidistribution — the
setting my §5.5 needs a special case of — is built at length in `lens-of-circles-oh.md`, and
§5.5 cites it and takes only the two facts it needs. The "two opposite problems are the same
problem" methodological point in §10.5 is developed in `geometric-concepts-pde-otto.md` §8.5.

**Length and shape.** The split rating drove the layout. §4 is compressed calibration for the
probability half (difficulty 2), §5 is the full bridge for the geometry half (difficulty 4),
and §7 walks the talk in Dolgopyat's own order — three problems, then his synthesis. §8 breaks
the usual pattern by promoting a *calculation* rather than a theorem to "the one argument",
because the talk's most striking fact (√log N versus log N) has a two-line explanation that he
gives and that the reader can verify in twenty minutes. That felt like the highest-value
possible use of that section.
