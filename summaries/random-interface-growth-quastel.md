---
title: "Random Interface Growth"
speaker: Jeremy Quastel (University of Toronto)
source: https://www.youtube.com/watch?v=B5OhjD222w0
video_id: B5OhjD222w0
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: none — companion: https://arxiv.org/abs/2205.01433
transcript: ../transcripts/B5OhjD222w0_transcript.txt
difficulty_for_you: 2/5 (the physics and the scaling) — 3/5 (the integrable machinery)
reading_time: ~65 min
---

# Random Interface Growth — Jeremy Quastel

**Field:** probability. Interacting particle systems, stochastic PDE, and the branch now
called *integrable probability* — the part of probability that borrows machinery from
classical integrable systems.

**Difficulty against your background: split, and the split is clean.**

- **The physics half is nearly yours.** Surface growth, an interface that fluctuates like
  t^{1/3} with correlations on scale t^{2/3}, a nonlinear PDE forced by white noise, a
  renormalization-group fixed point, universality classes, scaling exponents. You have all
  of this. **Difficulty 2** — you need one new scaling (1:2:3 instead of 1:2) and one new
  fixed point, and both take an afternoon.
- **The integrable half is a real gap.** Fredholm determinants, determinantal point
  processes, biorthogonalization of shifted Charlier polynomials, the Brownian scattering
  transform, the Airy line ensemble, and the fact that the answer solves the
  Kadomtsev–Petviashvili equation. **Difficulty 3.** You have the prerequisites — you know
  inverse scattering for KdV, you know what a trace-class operator is, you know Hopf–Lax —
  but the specific machine is new. That half gets the bridge.

**What this tutorial builds.** The 1:2:3 scaling derived rather than asserted; Fredholm
determinants and why non-intersecting paths produce them; the biorthogonalization problem
and the trick that solved it; the Brownian scattering transform and its Lax equation; the
KP equation the answer satisfies; and the Airy line ensemble route that replaces formulas
by an axiom.

**A note on sources — read this before you trust anything below.**

- **There is no ICM 2026 proceedings paper for this talk.** I searched arXiv (Quastel's
  most recent posting is arXiv:2409.08465, September 2024, on a different question) and the
  SIAM listing for *Proceedings of the ICM 2026, Volume 2: Plenary Lectures*, whose
  contents page returns HTTP 403 and which I could not open. Nothing with a matching title
  exists in any index I could reach.
- **The title is the speaker's own description, not a confirmed programme title.** The
  introducer never states a title. Quastel's first sentence is "so the talk's about random
  interface growth," and that is where the title above comes from. The IMU speaker listing
  and the ICM 2026 speaker page both give his name with no lecture title. Treat the title
  as reconstructed. *(Contrast Otto's talk in this folder, where the title is stated twice
  on the video.)*
- **The companion is
  [arXiv:2205.01433](https://arxiv.org/abs/2205.01433), Daniel Remenik, *Integrable
  fluctuations in the KPZ universality class*** (3 May 2022; Proc. ICM 2022, Vol. 6,
  4426–4450). **This is a companion, not the proceedings paper, and it is not by the
  speaker.** It earns the label anyway: it is a survey of exactly this talk's spine, by
  Quastel's principal collaborator, and its abstract reads like the talk's outline — the
  KPZ fixed point, its construction through TASEP, "how the construction reveals the KPZ
  fixed point as a stochastic integrable system," and the KP equation. Every formula I
  quote from it is cited.
- **Quastel's own lecture notes on the same construction** are
  [arXiv:1710.02635](https://arxiv.org/abs/1710.02635), Quastel and Remenik, *From the
  totally asymmetric simple exclusion process to the KPZ fixed point* (PCMI graduate summer
  school, 2017). Older, and it predates the KP result, but it is the speaker's own.
- **Primary literature is used heavily and kept visibly separate.** Where the talk states a
  published result, I recover the mathematics from *its own* paper and name it inline. Those
  are one-theorem citations, not a substitute for a proceedings paper.
- **No formulas survive in the captions.** Everything Quastel wrote was on slides, and at
  one point he says out loud "I won't show you the formula. I was warned not to show you the
  formula." Every displayed equation below is either (i) taken from a cited published source,
  (ii) a derivation I did from exponents he spoke aloud and labelled as such, or (iii) marked
  as a gap. Nothing is filled in by guessing.

**Names.** The auto-captions destroy almost every proper noun, including the speaker's own
("Jeremy Quest", "Jeremy Quaster"). Full correction table in §11.

**One cross-reference.** The talk spends about two minutes on singular stochastic PDE and
renormalization, and takes a strong position on what those tools can and cannot reach.
`summaries/geometric-concepts-pde-otto.md` §4 builds that machinery at length — white-noise
scaling, subcriticality, Cameron–Martin, Malliavin derivatives, regularity structures,
counterterms. I do not rebuild it. I state Quastel's verdict on it in §5.13 and say what it
means. The two tutorials point at each other: Otto's §4.2 explicitly names *this* talk as
the place you watch scale invariance by zooming **out**, where his own construction zooms
**in**.

---

## 1. What is at stake

The first slide is a photograph of a wildfire and a photograph of lichen. The burnt region
grows into the unburnt; the lichen grows into the bare rock. The two pictures are separated
by many orders of magnitude in size and share no physics whatsoever, and the boundary
between the invaded and the invading phase **looks the same in both**.

That observation is a century old in spirit and thirty years old as a research programme.
What is new — and it is the whole content of the talk — is that the object the two pictures
share has now been **written down**.

Here is the precise shape of the claim. Turn the wildfire picture on its side so the burnt
region is the region under a graph, and call that graph the height function h(t, x). Then:

- The height **grows linearly**: h ≈ c·t, and c depends on every microscopic detail — the
  wind, the fuel, the lattice, the reaction rates. Nobody cares about c.
- The height **fluctuates like t^{1/3}**. Not t^{1/2}. This is what the physics literature
  calls **kinetic roughening**.
- Those fluctuations are **correlated over a distance of order t^{2/3}** in space.

Two exponents, 1/3 and 2/3, in place of the diffusive 1/2 you would get from a sum of
independent things. That much was predicted in 1977 by Forster, Nelson and Stephen for the
stochastic Burgers equation using the **dynamic renormalization group**, and extended in
1986 by Kardar, Parisi and Zhang to a large class of models (Remenik, arXiv:2205.01433, §1).
Quastel's assessment of what that method delivered is blunt and it is the hinge of the whole
lecture:

> "When they do that they can't tell you what that object is. It's not much more than saying
> well, there's something there."

Renormalization group tells you a nontrivial limit exists. It does not tell you what the
limit *is*. You cannot sample from "there's something there", you cannot compare it against
an experiment, and you cannot discover that it satisfies a differential equation.

So the question of the talk is:

> **What is the universal random object that all of these interfaces converge to, written
> explicitly enough that you can compute with it?**

The answer has a name — the **KPZ fixed point** — and the talk is the story of how it was
constructed, why it turned out to be an integrable system, and which parts of the
universality claim remain completely open. On the last point Quastel is unusually candid:
for the very first model he shows you, the Eden model, and for the ballistic-deposition
movie he shows you, **nobody can prove any of this**, and he explains exactly where the
proof gets stuck.

---

## 2. Your anchors

Quastel hands you both of them from the podium. Neither needs to be invented, and per Rule 2
that makes them better than anything a search would produce.

### 2.1 Anchor one: the KPZ fixed point is the central limit theorem for surfaces

He builds it explicitly, and slowly, in the middle of the talk. Take Brownian motion. It has
one property that makes it matter:

> B(ε^{-1}x) has the same law as ε^{-1/2}B(x).

Rescale space by ε^{-1}, rescale height by ε^{1/2}, and Brownian motion is unchanged. It is
the **fixed point of the 1:2 scaling**. That is exactly why it is the limit of essentially
every random walk with independent increments, short-range correlations and a couple of
moments — his words. The central limit theorem is the statement that the 1:2 scaling has a
fixed point, and that the fixed point attracts everything generic.

Now the second half of the observation, which is the one to keep:

> "Fixed points are a good place to look for integrability."

Brownian motion has **exact formulas** — the probability that it sits in prescribed places
at prescribed times is a finite-dimensional Gaussian integral. Random walks generally do
not. The fixed point is more symmetric than any of the models attracted to it, and the extra
symmetry is what makes it solvable.

That is the entire strategy of the talk, one level up: **don't solve the growth model, solve
its fixed point.** The scaling is 1:2:3 rather than 1:2 because there is now a time
direction. The fixed point is not Gaussian. And the exact formulas are Fredholm determinants
rather than Gaussian integrals. Everything else is the same story.

### 2.2 Anchor two: this is inverse scattering, and it lands on KP

You know how KdV is solved. You do not integrate the nonlinear equation. You

1. map the initial data to spectral data (the forward scattering transform),
2. evolve the spectral data by a **linear**, in fact trivial, flow,
3. map back (the inverse transform).

Quastel describes his own machine in exactly these three steps, and he calls it a
**scattering transform** himself:

> "You lift up your initial data to an operator — this Brownian scattering transform. And now
> there's some linear evolution which I showed you which gets you the thing at time t and
> these positions x and heights r, and the Fredholm determinant just pulls you back to your
> solution."

The correspondence is not decorative. In the published construction the operator
K_t^{hypo(h₀)} satisfies

$$K_t^{\mathrm{hypo}(h_0)} \;=\; e^{-\frac{t}{3}\partial^3}\, K_0^{\mathrm{hypo}(h_0)}\, e^{\frac{t}{3}\partial^3}$$

— conjugation by the propagator of ∂³, which is the linear part of KdV — equivalently the
**Lax equation** ∂_t K_t = [−⅓∂³, K_t] (Remenik, arXiv:2205.01433, eq. (5.1)). The
dependence on time is completely decoupled from the dependence on the initial data, and the
time flow is linear at the level of kernels. Then the Fredholm determinant is the inverse
transform.

And the punchline closes the circle: the one-point distribution of the resulting process
satisfies the **Kadomtsev–Petviashvili equation, KP-II**, the two-dimensional generalization
of KdV, reducing to KdV itself for flat initial data (Quastel–Remenik,
[arXiv:1908.10353](https://arxiv.org/abs/1908.10353), Thm. 1.1 and eq. (1.8)). You started
with a growth model. You ended in the Sato theory of the KP hierarchy.

### 2.3 The Burgers anchor: real, but smaller than you would expect

Your brief proposed the stochastic Burgers equation as the anchor. Test it against the talk.

**Supported.** Quastel says of the KPZ equation: "you should really think about the thing as
two parts. There's the integrated Burgers equation or Hamilton–Jacobi equation or whatever.
There's that part which is sort of the simplest nonlinear PDE which we understand very
well." And the Hamilton–Jacobi structure shows up visibly: "you can see from this thing the
Burgers part, which just tells you that the solution is just the envelope of a bunch of
parabolas." That is the **Hopf–Lax formula**, and you can see it in his simulation.

It goes further than he says aloud. The KPZ fixed point inherits a Hopf–Lax formula
literally:

$$\mathfrak{h}(t,x) \;\overset{\text{dist}}{=}\; \sup_{y\in\mathbb{R}}\Big\{ t^{1/3}\mathcal{A}\big(t^{-2/3}x,\,t^{-2/3}y\big) \;-\; \frac{(x-y)^2}{t} \;+\; h_0(y)\Big\}$$

(Quastel–Remenik, arXiv:1908.10353, eq. (1.3)). The −(x−y)²/t is the Hopf–Lax cost you know
from Hamilton–Jacobi; the object 𝒜 is the **Airy sheet**, and it is the noise. Quastel shows
you exactly this in the talk without writing it, when he takes two narrow wedges and says
"the height function now at t and x is actually just the sup of the height functions of the
two ones coming from two different narrow wedges."

**Not supported.** He never discusses shocks, viscosity solutions, entropy conditions, or
turbulence, and he never once says "stochastic Burgers equation" — only "integrated
Burgers." Do not import that machinery; it is not what the talk is doing.

### 2.4 The Cole–Hopf transformation and the stochastic heat equation are absent

Your brief also proposed the Cole–Hopf transformation, KPZ ↔ stochastic heat equation, as an
anchor. **The talk never mentions it.** Not the transformation, not the multiplicative
stochastic heat equation, not the continuum directed polymer. I am naming the route so you
know it exists and know it is not what this lecture does.

It exists and it is standard: setting Z = exp(h) formally linearizes the KPZ nonlinearity
into a multiplicative-noise heat equation, and this is the definition of "Hopf–Cole solution"
of KPZ used, for instance, in Hairer and Quastel's own *A class of growth models rescaling to
KPZ* ([arXiv:1512.07845](https://arxiv.org/abs/1512.07845)). Quastel simply does not go
there, because the talk's route to exact formulas is through discrete models and
determinants, not through the continuum equation. Decorating his talk with the Cole–Hopf
picture would misdescribe the argument.

---

## 3. Calibration: what you can skip

Skim this, confirm we are using the same words, and go to §4.

**Universality class.** A collection of microscopically different models whose large-scale
fluctuation behaviour coincides. Microscopic detail survives only in non-universal constants
(the growth speed c, and one or two more). Quastel's version of the "it doesn't matter what
you choose" test is unusually direct: when he defines the Eden model he says a neighbour is
whatever you want it to be, and "this thing is supposed to be extremely universal, so it
would make no difference how you did that." When he shows a growth rule he says "if you
didn't catch it, make your own rule of this nature. It's supposed to also be in the class."

**Scaling exponents and the fixed point.** Same as your statistical mechanics. Rescale, take
a limit, get a fixed point of the rescaling; the fixed point has more symmetry than any
member of the class; membership of the class is the statement that you flow to it.

**The exponents here.** Height fluctuation t^{1/3}, spatial correlation length t^{2/3},
against the diffusive t^{1/2} and t^{1/2}. Compactly, 1:2:3 — height : space : time.

**The KPZ equation** (Kardar, Parisi, Zhang, 1986):

$$\partial_t h \;=\; \tfrac{\nu}{2}\,\partial_x^2 h \;+\; \tfrac{\lambda}{2}\,(\partial_x h)^2 \;+\; \sigma\,\xi$$

with ξ space-time white noise. Three mechanisms, and Quastel walks through each:

- **ξ** — the random deposition. Space-time white noise means the forcing at two distinct
  space-time points is *independent*. That independence is the whole content.
- **∂_x²h** — smoothing, "supposed to keep the interface from just becoming something
  completely crazy."
- **(∂_x h)²** — the nonlinearity, and his explanation of it is the physical one. The
  interface grows **normal to itself**; it "doesn't know what direction is up." So the
  vertical component of growth is a nonlinear function of the slope, and geometrically that
  function should be √(1 + (∂_x h)²). "But there's a kind of magic in this thing that it
  actually doesn't care what nonlinear function. It says no, no, no, I'll take (∂_x h)²."

That magic is a theorem, and it is his own: Hairer and Quastel, *A class of growth models
rescaling to KPZ* ([arXiv:1512.07845](https://arxiv.org/abs/1512.07845)), shows a large class
of continuous growth models with general nonlinearities converges to Hopf–Cole solutions of
KPZ. You will see in §7.2 why only the quadratic term survives the rescaling.

**White noise, and the reason it has to be white noise.** Quastel anticipates the obvious
objection — space-time white noise is a horrible object, it makes the equation hard to even
define, why not smooth it? — and gives the answer:

> "It's only if you start with space-time white noise that Brownian motion stays invariant
> when you add the nonlinear term. And this you should really consider a miracle. This is
> something that shouldn't happen. And all the calculations I'm going to show you are in
> some sense consequences of this miracle and miracles like it."

Precisely: drifted two-sided Brownian motions are invariant measures **modulo the overall
height** for the KPZ equation. That is the content of Gu and Quastel,
[arXiv:2409.08465](https://arxiv.org/abs/2409.08465), *Integration by parts and invariant
measure for KPZ* (v2, April 2025), which proves it by Stein's method plus Gaussian
integration by parts. *(This is the paper your brief flagged as a possible companion. It is
primary literature for one sentence of the talk, not a companion for the talk.)*

**The reversible / irreversible split, in your language.** Quastel decomposes the equation
the way a statistical mechanic would:

- **∂_x²h + ξ together** are the Langevin dynamics — reversible with respect to Brownian
  motion, "stuff fluctuating back and forth", designed so Brownian motion is invariant.
- **(∂_x h)²** is the non-reversible part. "This is non-reversible non-equilibrium processes
  which we understand very poorly, which we're trying to probe here."

And he places the whole problem in a frame you will recognize from engineering: "There's a
box, a nonlinear box, and you pump into it some white noise, or some noise you understand,
and out the other end comes some other noise, and you'd like to understand that."

**The Eden model** (Murray Eden, 1961). A subset of ℤ², growing by neighbours joining
independently at rate 1. Undirected — there is no time axis, so there is no height function,
which turns out to matter enormously (§5.14).

**Ballistic deposition with sticky particles.** Particles rain down onto a 1+1-dimensional
substrate and stack up — but they are **sticky**, so a falling particle attaches to the side
of the neighbouring column on the way past. Quastel's remark on this is the one to keep:
"this stickiness makes all the difference. If they weren't sticky, then it would just be a
kind of trivial problem where stacks would grow up. But now the growth is *out*." Sticking
sideways is what couples neighbouring columns and produces the lateral growth that the
(∂_x h)² term models.

That is the whole prerequisite. Everything in §4 onwards is new.

---

## 4. The bridge

Five things. The first you can derive yourself; the rest are genuinely new machinery.

### 4.1 The 1:2:3 scaling, derived rather than asserted

Quastel derives this on the fly and says "I hope it's clear that there's only one choice."
The captions carry the conclusion but not the algebra, so here is the algebra. *(This
derivation is mine, assembled from three statements he makes aloud; it reproduces exactly
the exponents he states, which is the check that it is the argument he had in mind.)*

Watch his polynuclear-growth simulation from narrow-wedge initial data. Two things are
visible on the screen and he points at both.

**One.** The profile is "roughly like a random walk minus a parabola," and the parabola is
spreading, "getting shallower and shallower" as x²/t. This is Hopf–Lax again: from a point
source, the deterministic envelope is a parabola opening linearly in time.

**Two.** In the middle, once you squash the vertical axis by the right amount, the interface
**looks like a Brownian motion**. He makes this point by re-plotting the same simulation with
a compressed vertical axis and saying "all I did is squish the vertical axis, and now you see
in the middle it really looked the same." His aside is worth having: it does not look
Brownian at first "because our visual system is designed to just see the volatility."

Now put the two together.

The Brownian appearance fixes the **height : space** ratio. If the spatial process is locally
Brownian, then rescaling space by ε^{-1} forces rescaling height by ε^{1/2}. That is 1:2, and
you have no freedom.

The parabola then fixes **time**. Under x ↦ ε^{-1}x̂ the parabola term becomes

$$\frac{(\varepsilon^{-1}\hat{x})^2}{t} \;=\; \varepsilon^{-2}\,\frac{\hat{x}^2}{t}$$

For the parabola to remain visible at the same magnification as the fluctuations — neither
swamping them nor flattening to nothing — its size must match the height scale ε^{-1/2}. Set
t = ε^{-3/2}T:

$$\varepsilon^{-2}\,\frac{\hat{x}^2}{\varepsilon^{-3/2}T} \;=\; \varepsilon^{-1/2}\,\frac{\hat{x}^2}{T}$$

which is exactly ε^{-1/2}. So **t must scale as ε^{-3/2}**, and there is no other choice.

The scaling is therefore

$$h_\varepsilon(t,x) \;=\; \varepsilon^{1/2}\Big[\, h\big(\varepsilon^{-3/2}t,\ \varepsilon^{-1}x\big) \;-\; C\varepsilon^{-3/2}t \,\Big]$$

(the published form: Quastel–Remenik, arXiv:1908.10353, eq. (1.2)). The subtraction is the
deterministic linear growth c·t, which under this magnification "goes shifting away from you
and you have to pull it back down."

Read the three numbers off the exponents: height ε^{1/2}, space ε^{-1}, time ε^{-3/2}, i.e.
**1 : 2 : 3**. And the fluctuation exponent falls out: at t of order ε^{-3/2}, the height
fluctuation is of order ε^{-1/2} = t^{1/3}. Quastel says exactly this — "t^{1/3} is just this
ε^{1/2}."

### 4.2 Non-intersecting paths make determinants

This is the mechanism behind every exact formula in the talk, and Quastel states it in one
sentence:

> "Non-intersecting lines produce determinants. If you have a bunch of Markov chains in one
> dimension on ℤ and you ask that they go from here to here but that they don't ever
> intersect each other, that's just given by the determinant of their transition
> probabilities."

This is the **Lindström–Gessel–Viennot lemma** in its probabilistic form, also known as the
Karlin–McGregor formula. The reason it is a determinant is an inclusion–exclusion argument
you can reconstruct: sum over all path families, weight each by the sign of the permutation
matching starts to ends, and every family in which two paths cross cancels against the family
obtained by swapping the two paths after their first crossing. Only the non-crossing families
survive, all with sign +1.

$$\mathbb{P}\big(\text{paths } x_i \to y_i,\ \text{non-intersecting}\big) \;=\; \det\big[\, p_t(x_i, y_j) \,\big]_{i,j=1}^{n}$$

*(Standard; not in the captions. Stated because §5.7 uses it.)*

So: **if you can rewrite your growth model as a family of non-intersecting paths, you get a
determinant for free.** That is the entire reason a "menagerie" of about ten growth models is
exactly solvable and the rest are not.

### 4.3 Fredholm determinants, and why they are the right object

Once n is large — and you always need n → ∞ — an n×n determinant of complicated entries is
useless. The object that survives the limit is a **Fredholm determinant**: the determinant of
I − K where K is a trace-class operator on a function space. Its expansion is

$$\det(I - K)_{L^2(X)} \;=\; \sum_{n \ge 0} \frac{(-1)^n}{n!} \int_{X^n} \det\big[\,K(x_i,x_j)\,\big]_{i,j=1}^n \; dx_1\cdots dx_n$$

*(Standard definition; not in the captions.)*

Two facts make it the natural object here.

**It is a gap probability.** For a determinantal point process with kernel K, the probability
that no point falls in a set A is det(I − K)_{L²(A)}. And "the height is below r" is exactly a
gap statement in the associated point process. That is why every distribution function in
this subject is a Fredholm determinant.

**The kernel is where the model lives, and it is small.** The n×n determinant of §4.2 has all
its information spread across n² entries. In the Fredholm form, all of it is compressed into a
single two-variable function K(u, v). The limit n → ∞ is then a limit of *kernels*, which is a
tractable analysis problem, rather than a limit of growing matrices, which is not. Quastel puts
the difficulty exactly this way: "you're going to have to take a limit, a large n limit, of
matrices — very complicated matrices — and it's not exactly clear how to do such a thing."

### 4.4 The biorthogonalization problem — the technical obstruction, and the trick

This is the one place where I can tell you precisely what the hard step was, because Quastel
describes it in words at some length and the companion states it formally.

For TASEP — the totally asymmetric simple exclusion process, particles on ℤ hopping right at
rate 1 into empty sites — the multipoint distribution reduces to a Fredholm determinant whose
kernel is built from two families of functions. One family is explicit. It is a family of
**Charlier polynomials**, the orthogonal polynomials for the Poisson weight, **shifted by the
initial data**: the k-th function is displaced by the position of the k-th particle minus its
label (Remenik, arXiv:2205.01433, §3).

The kernel needs the **biorthogonal** family: functions Ψ_k such that ⟨Φ_j, Ψ_k⟩ = δ_{jk},
subject to a side condition (2^{-x}Ψ_k(x) must be a polynomial of degree k).

Quastel's account of the obstruction is the most human moment in the talk:

> "You might think, well, their biorthogonal pairs are just the shifted orthogonal
> polynomials. You try it, it doesn't work, and then you realize you don't have a second
> idea."

For the special **step / narrow-wedge** initial data the shift is trivial and the Charlier
polynomials biorthogonalize themselves. That is why the narrow wedge was solved first and why
everything for two decades was about the narrow wedge. For **flat** initial data Sasamoto
(2005) and Borodin, Ferrari, Prähofer and Sasamoto (2007) solved it essentially by linear
algebra. For **general** initial data there was no idea at all.

The trick, from Matetski–Quastel–Remenik, is the one Quastel states from the podium and it is
worth stating carefully because it is completely unobvious:

> Take a random walk — in general, the invariant measure of the solvable process — and ask
> for the probability that this walk, started at x, **hits the region under the initial data
> curve**. Those hitting probabilities biorthogonalize the shifted polynomials.

So the initial height profile enters the formula not as a function but as **the boundary of a
region that a random walk is killed on**. That is the germ of the scattering transform.

### 4.5 The Brownian scattering transform

Take the 1:2:3 limit of the above. The random walk becomes a Brownian motion; the discrete
hitting probabilities become Brownian hitting probabilities of the **hypograph** of h₀ — the
region below the initial height profile. Formally (Remenik, arXiv:2205.01433, §4):

Let P^{No hit h}_{ℓ₁,ℓ₂}(u₁, du₂) be the transition density of a Brownian motion with diffusion
coefficient 2 that stays strictly above h on [ℓ₁, ℓ₂], let P^{Hit h} = I − P^{No hit h}, and
define the **Brownian scattering operator** as a conjugated limit,

$$K_t^{\mathrm{hypo}(h)} \;=\; \lim_{\ell_1\to-\infty,\ \ell_2\to\infty} e^{-\frac{1}{3}\ell_1^3 + \ell_1\partial^2}\; P^{\mathrm{Hit}\,h}_{\ell_1,\ell_2}\; e^{\frac{1}{3}\ell_2^3 - \ell_2\partial^2}$$

*(Companion eq. (4.2), transcribed. The existence of this limit is a theorem, not an
observation — Quastel and Remenik proved it for a restricted class in
[arXiv:1908.10353](https://arxiv.org/abs/1908.10353) and references therein.)*

In words, and this is Quastel's word for it: it is a **scattering transform**. It computes an
asymptotic transition density for a Brownian motion on the whole line, killed unless it hits
the region under h. The initial height profile is probed by Brownian motions, and what you keep
is not the profile but the record of how Brownian motions collide with it.

And then the payoff, already quoted in §2.2:

$$K_t^{\mathrm{hypo}(h_0)} = e^{-\frac{t}{3}\partial^3} K_0^{\mathrm{hypo}(h_0)} e^{\frac{t}{3}\partial^3}, \qquad \partial_t K_{t,\mathrm{ext}} = \big[-\tfrac{1}{3}\partial^3,\; K_{t,\mathrm{ext}}\big]$$

*(Companion §5, eq. (5.1).)* The time dependence and the initial-data dependence are
**completely decoupled**, and the time evolution is **linear**. There is a companion identity
in the spatial variables involving ∂²_u — a heat operator rather than an Airy operator
(companion eq. (5.2)). Quastel's phrasing: "you just adjust these linear dials. You solve some
linear PDEs, which is sort of an elementary thing to do, and you evolve around this kernel."

---

## 5. The talk, rebuilt

In his order.

### 5.1 The pictures, and the one distinction that matters

Wildfire, lichen, the Eden model on ℤ², and a movie of sticky ballistic deposition. Quastel
draws one line through this set, and it will govern the rest of the lecture:

- **Undirected models** (Eden, first-passage percolation, a burning region spreading in the
  plane): two space dimensions, no time axis, **no height function**.
- **Directed, or "1+1 dimensional" models** (ballistic deposition, polynuclear growth, TASEP):
  one space dimension plus time, and therefore **an actual height function h(t, x)**.

Everything provable in the talk is about the directed models. Everything unprovable — and he
says so twice — is about the undirected ones.

### 5.2 The KPZ equation, and then a promise to drop it

He writes the equation, explains the three terms as in §3, delivers the white-noise miracle,
and then says something you should take at face value:

> "After this we won't even mention stochastic partial differential equations, so don't get
> worried."

The KPZ equation is the **name** of the class and the reason it has a name. It is not the route
to the answer. It comes back only at the very end (§5.13), as a hard theorem to be proved
rather than a tool to prove with.

### 5.3 Brownian motion, the 1:2 fixed point, and why probabilists chase fixed points

Covered in §2.1. Two sentences to carry forward: fixed points let you describe vast basins of
fluctuation behaviour using one object, and fixed points are where integrability lives.

### 5.4 Two routes: quantum integrable systems, and stochastic ones

Physicists attack KPZ through generating functions that satisfy **quantum integrable systems**
— specifically the **delta Bose gas**, which is completely diagonalizable — and from that
construct divergent series and try to extract distributions.

Mathematicians take a different route: special **discretizations** of KPZ that turn out to be a
new kind of object, which Quastel calls **stochastic integrable systems** (§5.12).

And then a sociological remark he clearly enjoys:

> "This is a fun business, because unusually, instead of the mathematicians coming and proving
> the physicists' conjecture — actually it's not even working like that. There are even examples
> where a mathematician discovered and proved a thing, and then the physicists came up with a
> non-rigorous proof afterwards."

### 5.5 Polynuclear growth, defined completely

This is the model he asks you to keep, and it takes four sentences to define exactly. The height
function h(t, x) is **integer valued** on ℝ. Then:

1. Every **up-step** moves **left** at speed 1, deterministically.
2. Every **down-step** moves **right** at speed 1, deterministically.
3. **Up–down pairs are created at rate 1**, at every height, driven by a space-time Poisson
   process behind the picture.
4. When an up-step and a down-step meet, they **annihilate**.

Step heights need not be 1; a step of height 8 just moves as a unit. Note what is and is not
random: the motion is deterministic, and the only randomness is the Poisson creation of new
pairs. Quastel is pleased with this and says so: "I hope, unlike the KPZ equation, it's just
completely clear what it is."

**Narrow wedge initial data**: h₀(0) = 0 and h₀ = −∞ everywhere else. Nothing can nucleate off
to the sides because there is nothing there yet, so the picture is a spreading parabola with
fluctuations on top — which is where §4.1 came from.

### 5.6 PNG from a point *is* the longest increasing subsequence

A genuinely beautiful reduction, and the picture argument is complete in the captions.

Turn the space-time picture on its side and keep only the Poisson points and the lifetimes of
the created pairs. The points of a space-time Poisson process in a box, read as a bijection
between the ordering in one coordinate and the ordering in the other, **encode a uniformly
random permutation**. And:

> The height at time t at position 0 — the top right corner of the box — is exactly the
> **length of the longest increasing subsequence** of that permutation.

Quastel: "you can see the longest increasing subsequence in green, right, with your eye."

*[Gap: the caption says "we've got t equals about n² points in the box." That is inverted. The
relevant space-time box has area of order t², so the number of Poisson points n is of order t²,
i.e. t ≈ √n. I have corrected it; see §11.]*

With the correction the classical numbers line up, and this is a check worth doing yourself.
For a uniform random permutation of n letters the longest increasing subsequence has length
≈ 2√n (Logan–Shepp and Vershik–Kerov, 1977). With n ≈ t², that gives height ≈ 2t — linear
growth, as promised. Its fluctuations are of order n^{1/6} (Baik–Deift–Johansson, 1999), and
n^{1/6} = (t²)^{1/6} = **t^{1/3}**. The KPZ exponent, recovered from a combinatorics theorem
about permutations.

### 5.7 Multi-line PNG, the watermelon, and GUE Tracy–Widom

Now the construction that produces the determinant. PNG will accept **any** set of space-time
points as input, not just a Poisson process. So build a stack of lines:

- Line 1 is ordinary PNG driven by the Poisson process.
- Line 2 is a PNG line started one unit below, driven by the points where line 1's pairs
  **annihilated**.
- Line 3 is driven by line 2's annihilations. And so on.

Every line eats the collisions of the line above it. Quastel concedes this "perhaps you think
is a kind of baroque construction," and then delivers the point: **the lines stay ordered**.
They never cross. *(This is the Prähofer–Spohn multi-line PNG construction; he does not name it
in the captions, and I flag the attribution as mine.)*

Non-intersecting ⟹ determinant (§4.2). A determinantal formula for the height at time t at 0
was in fact available since **Gessel, 1990** — *Symmetric functions and P-recursiveness*, J.
Combin. Theory Ser. A **53**, 257–285, which expresses the generating function for permutations
with bounded longest increasing subsequence as a Toeplitz determinant. Quastel's dry note: "it
took a while for mathematicians to realize what to do with it."

Apply the 1:2:3 scaling to Gessel's formula — no spatial scaling needed, since you only look at
x = 0 — and the limit is the **GUE Tracy–Widom distribution**: the fluctuation law of the
largest eigenvalue of a Gaussian unitary ensemble matrix, i.e. a Hermitian n×n matrix with
entries as independent as Hermiticity allows.

**The picture that makes it unsurprising.** Multi-line PNG is essentially a family of
non-intersecting random walks. Take the continuum version: n Brownian motions all starting at 0
and all ending at 1, conditioned never to intersect. Draw it and you get the **watermelon** —
Quastel's word, and the shape is obvious. Now cut the watermelon vertically in the middle and
read off the n crossing heights. **Those n numbers have exactly the law of the eigenvalues of a
GUE matrix.** So the top line of the watermelon is the top eigenvalue, and rescaling it gives
Tracy–Widom.

> **Correction, and it is substantive.** The captions have Quastel saying "Gaussian unitary
> ensemble" twice and then, in the same breath, "which is this **GOE** Tracy–Widom
> distribution." That is wrong and it is the opposite of the truth: narrow wedge gives **GUE**
> Tracy–Widom, and **flat** initial data gives **GOE** (Quastel–Remenik, arXiv:1908.10353, §1;
> Remenik, arXiv:2205.01433, §§2 and 4). Everything else in the paragraph — GUE matrix, top
> eigenvalue, the watermelon cut — is consistent with GUE. I have corrected it in the text.
> Flagged again in §11.

### 5.8 Other initial data, and why it was hard for twenty years

Take **two** narrow wedges instead of one. Each grows a parabola; the parabolas merge. The
answer is a variational formula — the height is the sup of the two — which looks like it
trivializes the problem.

It does not, and Quastel's explanation is precise. The two contributions are **not
independent**: "in the middle, of course, they're using the same noise." So the input to the
variational problem is a **two-parameter stochastic process** — the **Airy sheet** 𝒜(x, y) —
whose joint distribution is unknown. Quastel: "you actually don't know its distributions. You
don't know how they depend on each other."

And the multi-line structure, the thing that gave you the determinant, **does not survive**.
"That was just a special thing that exists in the one initial data. If there are things like
multi-line here, they're much more complicated, hard to understand, hard to see."

So the route has to change. Move to **TASEP**, which is solvable for a different reason —
"Bethe ansatz solvable, or if you like free fermion, or if you like you could use the
Yang–Baxter; they're sort of the same thing" — and which gives you an n×n determinant for the
transition probabilities from any n-particle configuration to any other. Correct, complete, full
of contour integrals, and effectively unusable, because you need the n → ∞ limit.

### 5.9 The partial solution (≈2007) and the full one

Sasamoto and Borodin and their collaborators did flat initial data around 2007, and reduced the
general case to the biorthogonalization problem of §4.4. Quastel and his coauthors solved that
problem by the random-walk hitting trick.

The result is a **Fredholm determinant formula for the height function of polynuclear growth at
time t at any collection of positions, starting from any initial data**, with the initial data
entering through hitting probabilities. And the property he stresses:

> "One of the things about this theorem is that there's **no conditions**. It's true for **any**
> initial data."

*[Gap: he does not display the formula. "I won't show you the formula. I was warned not to show
you the formula." Impact: **low**. The structure — Fredholm determinant, kernel, initial data
encoded via hitting probabilities — is fully described in words and is exactly the published
Thm. in Matetski–Quastel–Remenik, Acta Math. 227 (2021) 115–203,
[arXiv:1701.00018](https://arxiv.org/abs/1701.00018). Nothing about the argument depends on the
symbols.]*

### 5.10 The KPZ fixed point

Now rescale by 1:2:3 and take the limit. What emerges is the object the whole lecture is for.

**The KPZ fixed point** is the Markov process h(t, x) with

$$\mathbb{P}_{h_0}\big(\mathfrak{h}(t,x_1)\le r_1,\ldots,\mathfrak{h}(t,x_m)\le r_m\big) \;=\; \det\!\Big(I - \chi_r\, K^{\mathrm{hypo}(h_0)}_{t,\mathrm{ext}}\, \chi_r\Big)_{L^2(\{x_1,\ldots,x_m\}\times\mathbb{R})}$$

*(Companion eq. (4.3); χ_r is the projection encoding the levels r.)*

Its properties, as Quastel lists them:

- It is a **Markov process** — the finite-dimensional distributions above define a transition
  kernel.
- It is **invariant under the 1:2:3 scaling**. That is what "fixed point" means.
- Its **invariant measure is Brownian motion**, modulo the overall height. Start it from a
  Brownian profile, run it, and you get a Brownian profile again — shifted upward, and, he
  notes, "correlated in a very bizarre way, which one can compute", with the one you started
  from.
- It is conjecturally **the** 1:2:3 limit of every model in the class, and the class is huge:
  "driven diffusive systems, polymer free energies."

### 5.11 Three reasons the exact formulas matter

Quastel asks the question himself — "why do we care so much if there's exact formulas?" — and
gives three answers. They are the most portable part of the talk.

**One: you cannot take the limit without them.** The dynamic renormalization group of the 1970s
told you a nontrivial fixed point existed. It could not tell you what it was. Quastel: "the
point is, if you have formulas we can actually take the limit. You really need the formulas to
take a limit. **No one's ever been able to take these limits really without some input of exact
formulas.**"

**Two: experiments need something to compare against.** Kazumasa Takeuchi, in Japan, takes a
**liquid crystal** that exists in two states — one centimetre square — fires a laser pulse into
it to nucleate the stable phase, and watches the interface grow. He repeats it many times and
measures the distribution precisely. Quastel's point is the methodological one: "you need to
match them to something. You want to match them to something, you need exact formulas. You need
to know exactly what you're matching against to see if this is true." *(Takeuchi and Sano's
liquid-crystal turbulence experiments confirmed not just the exponents but the Tracy–Widom
distributions themselves, and the geometry dependence — circular growth giving GUE, flat growth
GOE. See Takeuchi and Sano, and Takeuchi et al.,
[arXiv:1108.2118](https://arxiv.org/abs/1108.2118) and
[arXiv:1203.2530](https://arxiv.org/abs/1203.2530).)*

**Three: you can find structure in a formula that you could never have guessed.** Which is §5.12.

### 5.12 KP: a physical law obtained by grinding

Take the one-point distribution of the KPZ fixed point:

$$F(t,x,r) \;=\; \mathbb{P}_{h_0}\big(\mathfrak{h}(t,x)\le r\big)$$

Take its logarithm. Take **two** derivatives in r — the variable that is the height threshold,
not a space or time variable. Call the result φ. Then φ satisfies the **KP-II equation**:

$$\partial_t\varphi \;+\; \tfrac{1}{2}\,\partial_r\!\left(\varphi^2\right) \;+\; \tfrac{1}{12}\,\partial_r^3\varphi \;+\; \tfrac{1}{4}\,\partial_r^{-1}\partial_x^2\varphi \;=\; 0$$

*(Quastel and Remenik, arXiv:1908.10353, Thm. 1.1, eq. (1.7).)*

For **flat** initial data φ has no x dependence and the last term drops, leaving the
Korteweg–de Vries equation:

$$\partial_t\varphi \;+\; \tfrac{1}{2}\,\partial_r\!\left(\varphi^2\right) \;+\; \tfrac{1}{12}\,\partial_r^3\varphi \;=\; 0$$

*(Same paper, eq. (1.8).)*

For several space points there is a **matrix KP** equation, with a commutator term. Quastel says
so from the podium — "it's matrix versions of the KP equation, which are also known integrable
systems" — and the published statement is

$$\partial_t q + \tfrac{1}{2}D_r q^2 + \tfrac{1}{12}D_r^3 q + \tfrac{1}{4}D_x^2 Q + \tfrac{1}{2}[q, D_xQ] = 0$$

with Q = ((I − K)^{-1}K)(0,0) an n×n matrix-valued function, q = D_r Q, and D_r log F = tr Q
(*ibid.*, eq. (1.6)).

And the Tracy–Widom distributions themselves reappear as **special self-similar solutions of KP
and KdV** (*ibid.*, §1.2). GUE Tracy–Widom is what you get from narrow-wedge initial data; GOE
from flat.

Now the part that makes this the most quotable minute of the lecture. **Nobody knows why.**
Quastel describes the proof — take third and second derivatives of the log of the Fredholm
determinant, generate an enormous string of operator traces, watch the nonlinear terms merge,
and observe that the whole thing equals zero. It is done by hand. And then:

> "This is the universal equation for random interface growth. And please somebody tell me why
> it's true. All we can do is prove it. How pathetic is that?"

The published version of the same admission is worth setting alongside it: "The result was
unexpected. We do not have physical intuition why it is true; it follows by, essentially,
algebra... **and we believe it is the first example of a physical law having been obtained in
such a fashion**" (arXiv:1908.10353, Remark 1.2.1).

And this generalizes across the solvable menagerie. There are about ten models like PNG that can
be solved exactly, and — this is the thesis of Quastel's student **C. Alexander Rodriguez**
(Toronto) — each corresponds to an **integrable discretization of KP**, a **discrete Hirota**
equation. For polynuclear growth specifically it is the **2D Toda lattice**. See Rodriguez,
[arXiv:2509.16316](https://arxiv.org/abs/2509.16316); the thesis, *Non-abelian Hirota–Miwa
equations for the KPZ universality*, covers eighteen models across four scaling regimes.
*(Quastel says "like 10 of them" from the podium. Where the two disagree, I am quoting the
thesis.)* The PNG ↔ 2D Toda correspondence is Quastel and Remenik's *Polynuclear growth and the
Toda lattice*, [arXiv:2209.02643](https://arxiv.org/abs/2209.02643).

### 5.13 What is a stochastic integrable system?

This is the conceptual centre of the lecture, and Quastel presents it explicitly as an open
question with a proposal attached, not as a settled definition:

> "You can ask, what's a stochastic integrable system? And the answer is, I think we don't quite
> know yet. But I'm going to propose something, and you're welcome to propose something else,
> and somehow there should be a discussion."

Here is the difficulty, in his framing. In a **classical** integrable system you have enough
conserved quantities to resolve the dynamics. Here there is nothing conserved. The dynamics is a
Markov process; it does not conserve anything. So integrability cannot mean what it usually
means.

His proposal:

> **The random dynamics is not the integrable object. The transition probabilities are.**

Transition probabilities are *deterministic* quantities. They form a flow. And that flow is
completely integrable, in the exact classical sense: it is **linearized by a transform**.

1. Lift the initial height function to an operator, via the Brownian scattering transform (§4.5).
2. Evolve linearly — conjugate by e^{±t∂³/3} in time, a heat-type operator in space (§4.5).
3. Come back down via the Fredholm determinant.

Read against §2.2: this is inverse scattering, applied not to the trajectories of the system but
to the deterministic object the system induces on distributions.

This is worth pausing on in your own vocabulary, because you already own the pattern under a
different name. A stochastic differential equation induces a **deterministic** linear evolution
on its densities — the Fokker–Planck / Kolmogorov equation. Quastel's proposal is: call the
process integrable when *that* deterministic linear evolution is a completely integrable system,
solvable by a scattering transform. Nothing about the individual random trajectories has to be
solvable, and here nothing about them is.

### 5.14 The KPZ equation itself, and the ceiling on perturbative methods

Now the harder theorem: does the **KPZ equation** — not PNG, not TASEP — converge to the KPZ
fixed point?

First, do the rescaling on the equation itself. Under h_ε(t,x) = ε^{1/2}h(ε^{-3/2}t, ε^{-1}x)
the three coefficients (λ, ν, σ) transform to (λ, ε^{1/2}ν, ε^{1/4}σ) — the nonlinearity is
**invariant**, and both the viscosity and the noise strength go to zero (arXiv:1908.10353, §1).
You derive this yourself in §7.2. Quastel's comment on the naive reading:

> "As ε goes to zero, well, it looks pretty silly. It looks like it just goes to the Burgers
> equation. But that's much too naive. That's not true. And of course the Burgers equation
> itself is not well posed."

Second, look at the other end. Send the coupling λ → 0 and the equation becomes Gaussian — the
**Edwards–Wilkinson** model, whose scaling is **1:2:4**, not 1:2:3. So there are two fixed points
in this universe: a trivial Gaussian one and the nonlinear KPZ one. **The KPZ equation is the
road between them.**

Third — and this is the passage that concerns your other tutorial — Quastel places the singular
SPDE toolkit on this map, and his placement is unflattering:

> "We have some tools which have been invented over the past maybe 20 years — stochastic analysis
> for singular stochastic partial differential equations. These tools kind of exist **down
> there**. In a sense, they're all **perturbation around this Gaussian fixed point**. And you're
> just not, using those tools, ever going to be — well, maybe not ever, but at least now — able
> to probe up into this world, which as far as we can tell we can only really get to by exact
> formulas, by algebra."

That is a sharp and falsifiable claim about the reach of a whole research programme, and it is
the direct point of contact with **`summaries/geometric-concepts-pde-otto.md` §4**, which builds
that machinery in full: white-noise scaling and subcriticality, the Cameron–Martin space, the
Malliavin derivative and the spectral gap inequality, regularity structures as charts and
transition maps of a solution manifold, and renormalization by counterterms. Read that section
if you want the machinery. The point to take here is the **structural** one, and it is a good
one to carry around:

> Every perturbative method perturbs around *some* fixed point, and it can only reach the basin
> of that fixed point. Subcriticality — the condition that makes regularity structures work — is
> precisely the statement that the nonlinearity is *irrelevant* at small scales, i.e. that you
> are near the Gaussian fixed point. The nonlinear fixed point is by construction out of reach.

Otto's talk and Quastel's talk are the two halves of one disagreement about method, delivered at
the same congress. Otto's tutorial notes the mirror: Otto's construction sees scale invariance by
zooming **in**, where Quastel's is seen by zooming **out**.

### 5.15 The geometric route: the Airy line ensemble and a characterization

So how *do* you prove the KPZ equation converges to the fixed point, if it is not integrable?
Quastel shows a route that is "a bit more geometric," and it is the most consequential recent
development in the talk.

Go back to the watermelon (§5.7). Look at the top of it, in a window of KPZ size — recall
t ≈ n², so the KPZ window at the top of an n-line watermelon is exactly the right window. Rescale.
The limit is a determinantal process called the **Airy line ensemble**.

The Airy line ensemble has a remarkable property, found by **Ivan Corwin and Alan Hammond**: the
**Brownian Gibbs property**. Quastel demonstrates it by animation and it is easy to state.

1. Choose an interval, and erase the pieces of all the curves inside it.
2. Now paste back independent Brownian bridges, conditioned to match the curves at the two
   endpoints of the interval, and conditioned not to intersect each other or anything else.
3. **The result has exactly the same law as what you erased.**

That is a Gibbs property in exactly your sense: the conditional law inside a window, given
everything outside, is the "free" measure — here, non-intersecting Brownian bridges — subject
only to the boundary data.

And then the recent theorem, which Quastel calls "an amazing work":

> **Aggarwal and Huang.** The Airy line ensemble is the **only** line ensemble with the Brownian
> Gibbs property whose top curve is parabolic at infinity.

*(Amol Aggarwal and Jiaoyang Huang, *Strong characterization for the Airy line ensemble*,
[arXiv:2308.11908](https://arxiv.org/abs/2308.11908), Invent. Math., 2025.)*

Quastel spells out why this matters, and it is the most transferable single sentence in the
lecture:

> "That's finally a **characterization** of a KPZ universal object which doesn't just depend on
> formulas."

A formula-based definition transfers only to models that have that formula — the ten solvable
ones. An axiom-based definition transfers to **anything that satisfies the axiom**. So the proof
strategy inverts: instead of computing a limit, show your model's limit has the Brownian Gibbs
property and parabolic asymptotics, and the characterization identifies it for you.

Combined with methods of **Duncan Dauvergne and Bálint Virág** — his Toronto colleagues — for
passing between the Airy line ensemble and the Airy sheet (the noise in the Hopf–Lax formula of
§2.3; see Dauvergne, Ortmann and Virág, *The directed landscape*,
[arXiv:1812.00309](https://arxiv.org/abs/1812.00309), Acta Math. **229** (2022)), the chain now
closes:

**ASEP** (the two-directional version of TASEP) → **KPZ equation** under 1:2:4 scaling →
**KPZ fixed point** under 1:2:3.

So the KPZ equation converges to the KPZ fixed point, via a model that is not exactly solvable.

### 5.16 The frontier

Quastel then lists what can and cannot be done now.

**What is provable, "a bit lower down."** Models that live in the world of stochastic analysis
can be shown to converge to the KPZ *equation*, and then a double limit sends the KPZ equation to
the fixed point. Examples he names:

- The **planar (2D) stochastic heat equation** with spatial white noise — an *undirected* model.
  Solutions from a Dirac initial condition "look sort of like a Mount Fuji," and cuts of that
  Mount Fuji have KPZ-equation fluctuations. This is Quastel, Ramírez and Virág, *KPZ fluctuations
  in the planar stochastic heat equation*,
  [arXiv:2210.13607](https://arxiv.org/abs/2210.13607), Duke Math. J. **174** (2025) 1261–1340.
- **Stochastic Hamilton–Jacobi equations** and **directed random polymers** under 1:2:4 scaling.

**What is expected and mostly not provable.** In one dimension, take **interacting spins** —
spatial discretizations of the nonlinear Schrödinger equation, say. These have invariant measures
that look Brownian. Started from those, one expects KPZ universal fluctuations. Here physics has
introduced a **dichotomy**:

| the model is | you should see |
|---|---|
| **non-integrable** | KPZ universal fluctuations, at long times, in the right window |
| **integrable** | ordinary **diffusive** fluctuations |

The integrable side has just been proved for one case: **Amol Aggarwal**, who spoke the day before
at the same congress, established that the 1D **Toda lattice** — an integrable case — does **not**
show KPZ fluctuations. *(Aggarwal and Nicoletti, *Fluctuations for the Toda lattice*,
[arXiv:2604.14346](https://arxiv.org/abs/2604.14346), shows diffusive scaling with an explicit
Gaussian limit for the current fluctuations, Brownian motion for a single trajectory, and
two-point correlations decaying like 1/t with the scaling functions predicted by Doyon and
Spohn.)*

The non-integrable side, Quastel says, is "extremely hard to prove, because these are
**non-stochastic dynamics**, and you're supposed to see over very long space-time scales these
KPZ fluctuations."

**What nobody can do at all.** The undirected models. The Eden model. First-passage percolation.
"Nobody has much idea how to prove that."

### 5.17 Why universality is genuinely hard — the one obstruction he explains

He gives one reason among many, and it is a good one because it is completely concrete.

Suppose you want to prove sticky ballistic aggregation — the movie from the first slide — is in
the KPZ class. The rule is simple. It is not hard to prove the process **has invariant measures**.

> "The problem is that any proof we have that it has invariant measures is **non-constructive**,
> and we just don't know what that invariant measure is."

And now note the containment. A sub-problem of proving the 1:2:3 scaling limit is proving it **at
time zero**, started from the invariant measure. So:

> The full universality statement is **strictly harder** than proving that the invariant measure
> of ballistic aggregation looks like Brownian motion on large scales.

And that easier statement is itself open. Quastel's aside is characteristic: "people claim it
does — I don't know, if you look at pictures it's not so clear — but of course we all believe it
does."

Sit with the shape of this. An existence proof that yields no description of the object is a
**wall**, not a step. The theory can prove the measure exists and can prove nothing about it. That
is the obstruction.

### 5.18 Directions, in his order

- **Build new solvable models on purpose.** They now understand the *mechanism* that makes exact
  formulas work: the determinants have to satisfy the **Kolmogorov backward equations**, and they
  can now explain *why* they do, "well enough that you can actually just attempt to build new ones
  from scratch."
- **Half-space.** Quastel's student **Xincheng Zhang** constructed the **half-space KPZ fixed
  point** — the universal growth model on [0, ∞) with a Neumann boundary condition at 0 carrying an
  arbitrary forcing parameter — with exact **Pfaffian** formulas for the transition probabilities.
  (Zhang, *TASEP in half-space*, [arXiv:2409.09974](https://arxiv.org/abs/2409.09974); Toronto PhD
  under Quastel.) Pfaffians rather than determinants is the signature of a boundary; it is the same
  GOE/GSE-versus-GUE distinction.
- **Multi-time formulas.** All the formulas above are fixed-time: transition probabilities from one
  time to another. In principle that determines everything, since the process is Markov and you can
  chain via Chapman–Kolmogorov. But there are also direct formulas for arbitrary space-time point
  configurations, due to **Johansson and Rahman** and to **[Zhipeng] Liu**. Quastel's verdict: "these
  formulas are so complicated that nobody knows what to do with them, but they exist." His reading of
  their existence is the interesting part — it "points to the fact that there's even more integrable
  structure than we had imagined."
- **2+1 dimensions.** "Much harder — of course." *(Laughter from the room.)* It is the **critical
  dimension**; things get much more irregular; "even understanding what's the analogue of the KPZ
  equation turns out to be an enormously difficult problem." There has been progress, some of it
  reported at this congress.
- **The physics deluge.** "There's this deluge of physics papers coming every week claiming KPZ
  fluctuations in some physical system — polariton condensates and things like that — by measuring
  various observables." And the caution: "it's not completely clear they are KPZ. They might be sort
  of like KPZ, or they might really be KPZ, and one has to really understand this." *(Caption reads
  "polaron condensates"; polariton condensates are the systems in which KPZ phase-ordering has been
  reported. Marked as reconstructed in §11.)*

### 5.19 The last slide

He closes with the carpet on the floor of his house. A carpet is a **random Riemannian metric**,
statistically homogeneous in space. Ants walk on it; look at where they get after time 2, 3, 4, 5,
6. The frontier of where-you-can-get-by-time-t on a random metric is a growing interface.

> "Well, that's supposed to be KPZ, if anybody can prove it."

Which is first-passage percolation, in a continuum dress. The talk opens with a wildfire nobody
can analyze and closes with a carpet nobody can analyze, and everything provable sits in between.

---

## 6. The one argument, stated precisely

The talk is not organized around a theorem, so here is the claim it argues for, in the sharpest
form the sources support.

> **Claim (Matetski–Quastel–Remenik, and its consequences).** There is a Markov process
> h(t, x) — the **KPZ fixed point** — taking values in upper semicontinuous functions, invariant
> under the 1:2:3 scaling, with Brownian motion as its invariant measure modulo height, whose
> transition probabilities are given **explicitly and for arbitrary initial data** by
>
> $$\mathbb{P}_{h_0}\big(\mathfrak{h}(t,x_1)\le r_1,\ldots,\mathfrak{h}(t,x_m)\le r_m\big) \;=\; \det\!\Big(I - \chi_r\, K^{\mathrm{hypo}(h_0)}_{t,\mathrm{ext}}\, \chi_r\Big)$$
>
> where K^{hypo(h₀)} is the Brownian scattering operator: the initial data enters only through the
> probabilities that a Brownian motion hits the region below h₀.
>
> This process is a **stochastic integrable system** in the following sense: the flow of transition
> kernels is **linearized** by the scattering transform, satisfying the Lax equation
> ∂_t K_{t,ext} = [−⅓∂³, K_{t,ext}], with the t-dependence completely decoupled from the initial
> data.
>
> As a consequence, φ = ∂²_r log F for the one-point distribution F satisfies the **KP-II
> equation**, reducing to **KdV** for flat initial data, with the GUE and GOE Tracy–Widom
> distributions arising as self-similar solutions.

**How the proof goes, at honest depth.**

1. TASEP's transition probabilities have an n×n determinantal form (Bethe ansatz / free fermion
   / Yang–Baxter).
2. That form reduces to a Fredholm determinant whose kernel is built from shifted Charlier
   polynomials and their biorthogonal partners (Sasamoto; Borodin–Ferrari–Prähofer–Sasamoto, via
   Gelfand–Tsetlin patterns and the Eynard–Mehta theorem — companion §2).
3. The biorthogonal family is unknown in general. **It is found by expressing it through the
   probability that a random walk hits the epigraph of the initial data.** This is the new
   ingredient (companion §3).
4. Rescale by 1:2:3. The random walk becomes Brownian; hitting probabilities of a discrete curve
   become hitting probabilities of the hypograph of h₀; the kernel converges to the Brownian
   scattering operator.
5. Read off the Lax structure from the conjugation e^{∓t∂³/3}, and grind the derivatives of
   log det to obtain KP.

**What is *not* proved, and Quastel is explicit about it.** That every model in the class converges
to this process. That is the universality problem, and §5.17 is the obstruction. What exists is:
convergence for TASEP and its relatives (exactly solvable), and, via the Airy line ensemble
characterization, convergence for ASEP and hence the KPZ equation. Everything else — Eden, ballistic
deposition, first-passage percolation, non-integrable spin chains, the wildfire, the carpet — is
conjecture.

*[Gap: the talk displays no formula anywhere. Every equation in this tutorial comes from a cited
published source or is labelled as my own derivation. Impact: **low to moderate**. Low for the
construction, because the published statements are exactly what he describes in words. Moderate for
one thing only — the spatial evolution equations for the kernel, which he calls "linear dials" and
which I have stated only in the schematic form given in the companion (eqs. (5.1)–(5.2)); the
precise operators were on the slide.]*

---

## 7. Do this by hand

### 7.1 Derive the 1:2:3 scaling (15 minutes, pen)

You saw the argument in §4.1. Do it yourself with the pieces stated bare, because the whole
lecture rests on this and it is three lines.

**Given:**
- (i) The interface is locally **Brownian** in space: increments over distance ℓ are of size ℓ^{1/2}.
- (ii) From a point source, the deterministic profile is a **parabola** of the Hopf–Lax form x²/t.

**Find:** the exponents a, b in the rescaling h_ε(t, x) = ε^{a}·[h(ε^{-b}t, ε^{-1}x) − c·ε^{-b}t]
that produces a nontrivial limit.

<details>
<summary>Solution</summary>

**Step 1 — height from space.** Rescale space by ε^{-1}. By (i), the fluctuation of the interface
over that distance is (ε^{-1})^{1/2} = ε^{-1/2}. To keep it order one, multiply the height by
ε^{1/2}. So **a = 1/2**.

**Step 2 — time from the parabola.** Substitute x = ε^{-1}x̂ into (ii):

$$\frac{(\varepsilon^{-1}\hat{x})^2}{t} = \varepsilon^{-2}\frac{\hat{x}^2}{t}$$

Set t = ε^{-b}T:

$$\varepsilon^{-2+b}\frac{\hat{x}^2}{T}$$

For this to survive multiplication by ε^{1/2} — i.e. to be visible at the same magnification as the
fluctuations, neither vanishing nor blowing up — we need ε^{-2+b}·ε^{1/2} = ε^0, so

$$b = \tfrac{3}{2}$$

So **height : space : time = ε^{1/2} : ε^{-1} : ε^{-3/2}**, which is 1 : 2 : 3. ∎

**Now the two consequences, which are the exponents from the first slide.**

At time t, the height fluctuation is ε^{-1/2} where t = ε^{-3/2}, so ε^{-1/2} = t^{1/3}. And the
spatial correlation scale is ε^{-1} = t^{2/3}.

**The thing to notice.** There is **exactly one** free choice in the whole derivation, and it is
already made for you: the local Brownianity of the interface. Once the invariant measure is
Brownian, the exponents 1/3 and 2/3 are forced by dimensional analysis. That is why Quastel spends
a full minute on the white-noise "miracle" in §3 — the invariance of Brownian motion is not a
curiosity, it is the input that determines the exponents.
</details>

### 7.2 Renormalization-group flow between the two fixed points (25 minutes, pen)

This is your own material — the relevance of an operator under rescaling — applied to KPZ. It
recovers, from scratch, the sentence in §5.14 that the 1:2:3 scaling sends (λ, ν, σ) to
(λ, ε^{1/2}ν, ε^{1/4}σ).

Take

$$\partial_t h = \tfrac{\nu}{2}\partial_x^2 h + \tfrac{\lambda}{2}(\partial_x h)^2 + \sigma\xi$$

with ξ space-time white noise on ℝ × ℝ. Define h_ε(t, x) = ε^{β}h(ε^{-z}t, ε^{-1}x).

**(a)** Show that space-time white noise satisfies ξ(ε^{-z}t, ε^{-1}x) =^{law} ε^{(z+1)/2}ξ(t, x).

**(b)** Find the equation satisfied by h_ε, i.e. the three new coefficients as powers of ε.

**(c)** Put β = 1/2, z = 3/2 (the KPZ scaling). What happens to each term as ε → 0? Reconcile with
Quastel's "it looks pretty silly, it looks like it just goes to the Burgers equation."

**(d)** Put β = 1/2, z = 2 (the **Edwards–Wilkinson** scaling). Which terms are preserved? What
happens to the nonlinearity? What does that tell you about which of the two fixed points is
attracting at large scales?

<details>
<summary>Solutions</summary>

**(a)** White noise has covariance 𝔼[ξ(t,x)ξ(t′,x′)] = δ(t−t′)δ(x−x′). Under the substitution,

$$\mathbb{E}\big[\xi(\varepsilon^{-z}t,\varepsilon^{-1}x)\,\xi(\varepsilon^{-z}t',\varepsilon^{-1}x')\big] = \delta\big(\varepsilon^{-z}(t-t')\big)\,\delta\big(\varepsilon^{-1}(x-x')\big) = \varepsilon^{z}\varepsilon^{1}\,\delta(t-t')\delta(x-x')$$

using δ(ax) = |a|^{-1}δ(x). A centred Gaussian field is determined by its covariance, so the field
equals ε^{(z+1)/2}ξ in law. ∎

**(b)** Write the original equation at the rescaled arguments and multiply through by ε^{β−z}:

- ∂_t h_ε = ε^{β−z}(∂_t h), so the left side is exactly ∂_t h_ε.
- ∂_x²h_ε = ε^{β−2}(∂_x²h), so (∂_x²h) = ε^{2−β}∂_x²h_ε, contributing ε^{β−z}·ε^{2−β} = **ε^{2−z}**.
- (∂_x h_ε)² = ε^{2β−2}(∂_x h)², so (∂_x h)² = ε^{2−2β}(∂_x h_ε)², contributing
  ε^{β−z}·ε^{2−2β} = **ε^{2−z−β}**.
- The noise contributes ε^{β−z}·ε^{(z+1)/2} = **ε^{β−(z−1)/2}**.

So

$$\partial_t h_\varepsilon = \tfrac{\nu}{2}\varepsilon^{2-z}\,\partial_x^2 h_\varepsilon + \tfrac{\lambda}{2}\varepsilon^{2-z-\beta}\,(\partial_x h_\varepsilon)^2 + \sigma\,\varepsilon^{\beta - (z-1)/2}\,\xi$$

**(c) KPZ scaling, β = 1/2, z = 3/2.**

| term | exponent | value |
|---|---|---|
| viscosity | 2 − z = 1/2 | **ε^{1/2}** → 0 |
| nonlinearity | 2 − z − β = 0 | **1** — invariant |
| noise | β − (z−1)/2 = 1/2 − 1/4 = 1/4 | **ε^{1/4}** → 0 |

So (λ, ν, σ) ↦ (λ, ε^{1/2}ν, ε^{1/4}σ), which is exactly the published statement
(arXiv:1908.10353, §1). **The nonlinearity is the only term preserved by the 1:2:3 scaling.** That
is why the class is named after it and why the exponents are what they are.

Formally, ε → 0 kills both the viscosity and the noise, leaving ∂_t h = ½λ(∂_x h)², the inviscid
Hamilton–Jacobi / Burgers equation — Quastel's "looks pretty silly." Why it is wrong: the limit is
singular. The noise coefficient goes to zero but the noise itself is a distribution of unbounded
size, and the viscosity going to zero makes the deterministic equation ill posed at exactly the same
rate. The two vanishing terms do not vanish; they conspire. The correct limit is the KPZ fixed point,
which is not the solution of any PDE.

**(d) Edwards–Wilkinson scaling, β = 1/2, z = 2.**

| term | exponent | value |
|---|---|---|
| viscosity | 2 − 2 = 0 | **1** — invariant |
| nonlinearity | 2 − 2 − 1/2 = −1/2 | **ε^{−1/2}** → ∞ |
| noise | 1/2 − 1/2 = 0 | **1** — invariant |

The **linear** equation ∂_t h = ½ν∂_x²h + σξ is exactly scale invariant under 1:2:4. That is the
Gaussian, or Edwards–Wilkinson, fixed point.

And the nonlinearity is **relevant** there: its effective coupling grows like ε^{−1/2} as you zoom
out. So the Gaussian fixed point is **unstable** in the direction of the nonlinearity. Switch on λ,
however small, and the flow leaves the Gaussian fixed point and heads for the KPZ fixed point, which
is the one that governs the large-scale behaviour.

**Now read §5.14 again with this in hand.** Quastel's claim that singular-SPDE methods are
"perturbation around the Gaussian fixed point" and cannot climb to the KPZ fixed point is precisely a
statement about this flow. Subcriticality — the working hypothesis of regularity structures, and the
thing `summaries/geometric-concepts-pde-otto.md` §4.2 spends a page on — is the requirement that the
nonlinearity be **irrelevant as you zoom in**. That is the same computation with the arrow reversed,
and it puts you on the stable manifold of the Gaussian fixed point by hypothesis. The KPZ fixed point
is the place the flow goes when you zoom **out**, and it is not in the domain of the method.

That is the cleanest way to see why the two ICM plenaries at issue reach the same object from two
directions and only one of them arrives.
</details>

---

## 8. What is actually useful to you

Six items, in order of how often you will reach for them.

### 8.1 An existence theorem you cannot compute with is a wall, not a step

§5.17 is the sharpest instance of this I have seen stated from a podium. Ballistic aggregation
provably **has** invariant measures. Every proof of that fact is non-constructive. And so the entire
universality programme for that model is blocked — not by a missing technique, but by the fact that
the object it needs is known only to exist.

The general form: **an existence proof that yields no handle on the object bounds what you can ever
prove downstream.** When you are choosing between a construction and a soft existence argument, that
is a real cost, not a stylistic preference.

The same principle drives the other direction of the talk. "You really need the formulas to take a
limit. No one's ever been able to take these limits really without some input of exact formulas."
Twenty-five years of work in this field is the story of what changes when a soft statement becomes an
explicit one.

### 8.2 Characterize by axiom, not by formula — that is what makes results transfer

§5.15 is the clean case, and it is worth reading twice.

The KPZ fixed point was defined by a **formula**. That is why the theory could only prove convergence
for the ten models that have a formula. Then Corwin and Hammond found that the Airy line ensemble has
the **Brownian Gibbs property**, and Aggarwal and Huang proved that this property, plus parabolic
asymptotics, **uniquely characterizes it**. Quastel: "that's finally a characterization of a KPZ
universal object which doesn't just depend on formulas."

The consequence is not incremental. Convergence proofs stopped being "compute the limit" and became
"verify two properties." That immediately reached ASEP and hence the KPZ equation, neither of which is
exactly solvable.

Translate this to your work directly. A component specified by its **implementation** binds every
consumer to that implementation. A component specified by **invariant properties that pin it down
uniquely** admits any implementation satisfying them, and — the part usually missed — lets you *prove
things about implementations you have not seen*. The valuable artefact is the uniqueness theorem, not
the construction.

*(This is the same move as `summaries/geometric-concepts-pde-otto.md` §8.4 — uniqueness by postulate,
where Otto's counterterm is pinned down by four invariance requirements rather than computed. Two
plenaries, same lesson.)*

### 8.3 Solve the fixed point, not the model

§2.1. Do not try to solve the object in front of you. Identify the rescaling under which the family
of objects is closed, find its fixed point, and solve *that*. The fixed point is more symmetric than
anything in its basin, and the extra symmetry is usually what makes it tractable. Brownian motion has
exact formulas that no individual random walk has; the KPZ fixed point has Fredholm determinants that
no individual growth model has.

The corollary is the operational one: **when you see a hard family of problems, ask what invariance
the hard part is approximately preserving, and study the exactly invariant object instead.**

### 8.4 A stochastic system can be integrable in its distributions while its trajectories are hopeless

§5.13, and this is a genuinely new reframe rather than a restatement.

The obstruction to calling a Markov process "integrable" is that nothing is conserved. Quastel's
answer is to move the question to the deterministic object the process induces — its transition
probabilities — and to ask whether *that* flow linearizes under a transform. For the KPZ fixed point
it does, by the Brownian scattering transform, with the Lax equation ∂_t K = [−⅓∂³, K].

You already know one half of this pattern: an SDE with unsolvable paths still induces a linear
Fokker–Planck evolution on densities. What Quastel adds is that this induced evolution can be
**completely integrable in the classical sense**, solvable by inverse scattering, even when nothing
about the sample paths is.

The transferable question: **when a system resists analysis, is there a deterministic flow it induces
— on distributions, on aggregates, on statistics — that is better behaved than the system?** And is
*that* flow the one to attack?

### 8.5 Know which fixed point your method perturbs around

§5.14 and §7.2(d). Every perturbative method is a perturbation around some fixed point, and it can
only reach that fixed point's basin. Regularity structures require subcriticality, which is exactly
the statement that the nonlinearity is irrelevant at small scales — that is, that you are near the
Gaussian fixed point. So the KPZ fixed point, which is what the flow reaches when you zoom **out**,
is structurally outside the method's reach, and Quastel says so.

This is not a criticism of the method. It is a statement about what a hypothesis buys and what it
costs, and it generalizes past mathematics: check whether the assumption that makes your tool work is
the same assumption that excludes the regime you care about. *(Compare
`summaries/optimization-theory-practice-wright.md` §10.4 — a theorem whose hypotheses destroy your
problem's structure is not a theorem about your problem. Different field, same failure mode.)*

### 8.6 Proof is not understanding, and saying so is a service

The KP result was obtained by taking derivatives of the log of a Fredholm determinant, generating an
enormous string of operator traces, and observing that it all cancels. It is correct. It is
verified. It is published in *Forum of Mathematics, Pi*. And:

> "This is the universal equation for random interface growth. And please somebody tell me why it's
> true. All we can do is prove it. How pathetic is that?"

The published version is the same admission in formal register: "We do not have physical intuition why
it is true; it follows by, essentially, algebra... and we believe it is the first example of a physical
law having been obtained in such a fashion."

Two things to take from this. First, the practical one: **a verified result whose mechanism you do not
understand is a legitimate deliverable, provided you say which it is.** Quastel labels the gap from the
podium of the ICM. That label is what lets a room of specialists know where the open problem is.

Second, and this bears directly on machine-assisted work: this is exactly the shape of an
algebra-verified result with no available narrative. The field's response was not to discard it — it
was to publish it, flag the gap, and go looking for the reason. That is the right protocol, and it is
worth having a name for.

---

## 9. Where to read next

1. **Remenik, *Integrable fluctuations in the KPZ universality class*.**
   [arXiv:2205.01433](https://arxiv.org/abs/2205.01433) — 19 pages, ICM 2022 proceedings, and the
   companion to this talk. Start here. It is the talk's spine written down: the history, TASEP, the
   biorthogonalization, the Brownian scattering operator, the Lax equation, and the KP result, with
   every formula stated.
2. **Matetski, Quastel and Remenik, *The KPZ fixed point*.**
   [arXiv:1701.00018](https://arxiv.org/abs/1701.00018), Acta Math. **227** (2021) 115–203 — the paper
   the introducer names as the main achievement. This is where the biorthogonalization is solved and
   the fixed point is constructed.
3. **Quastel and Remenik, *KP governs random growth off a one dimensional substrate*.**
   [arXiv:1908.10353](https://arxiv.org/abs/1908.10353), Forum Math. Pi **10** (2022) e10 — 19 pages,
   and the source of every KP formula above. Read Remark 1.2 in particular; it is the honest account of
   a result the authors do not understand.

*(If you want the singular-SPDE machinery Quastel dismisses in one sentence, do not go to a fourth
paper — go to `summaries/geometric-concepts-pde-otto.md` §4, which builds it from your background.)*

---

## 10. Self-test

<details>
<summary>1. Derive the 1:2:3 scaling from two facts about the picture.</summary>

(i) The interface is locally Brownian in space, so rescaling space by ε^{-1} forces rescaling height
by ε^{1/2} — that is the 1:2 part, and there is no freedom in it. (ii) From a point source the
deterministic profile is a Hopf–Lax parabola x²/t; under x ↦ ε^{-1}x̂ it becomes ε^{-2}x̂²/t, and for
that to sit at the height scale ε^{-1/2} you need t ∼ ε^{-3/2}. Hence height : space : time =
1 : 2 : 3, giving fluctuations t^{1/3} and correlation length t^{2/3}.
</details>

<details>
<summary>2. Why must the KPZ equation be driven by space-time white noise specifically?</summary>

Because it is the only forcing for which **Brownian motion remains invariant once the nonlinearity is
switched on** — precisely, drifted two-sided Brownian motions are invariant measures modulo the
overall height (Gu and Quastel, arXiv:2409.08465). Quastel calls this a miracle and says every
calculation in the talk is a consequence of it and miracles like it. Structurally it matters because
the Brownian invariant measure is exactly the input that forces the exponents (see question 1).
</details>

<details>
<summary>3. Why does the exact form of the nonlinearity not matter?</summary>

Geometrically the growth is normal to the interface, so the vertical growth rate should be
√(1 + (∂_x h)²). Under the 1:2:3 rescaling only the quadratic term is scale invariant — the constant
is absorbed into the linear growth you subtract, and the higher terms carry strictly positive powers
of ε (see §7.2(b): the term of degree k picks up ε^{2−z−(k−1)β}, which is ε^{0} only at k = 2). This
is a theorem, not a heuristic: Hairer and Quastel, *A class of growth models rescaling to KPZ*
(arXiv:1512.07845).
</details>

<details>
<summary>4. Define polynuclear growth completely, and say what its height at 0 has to do with permutations.</summary>

h is integer valued on ℝ; up-steps move left at speed 1 and down-steps move right at speed 1,
deterministically; up–down pairs are created at rate 1 by a space-time Poisson process; steps
annihilate on meeting. From narrow-wedge initial data (h₀(0)=0, −∞ elsewhere), the Poisson points in
the space-time box encode a uniform random permutation, and **the height at time t at position 0 is
the length of the longest increasing subsequence** of that permutation. The box has area of order t²,
so n ≈ t², and the classical results L_n ≈ 2√n with fluctuations n^{1/6} give height ≈ 2t with
fluctuations t^{1/3}.
</details>

<details>
<summary>5. How does multi-line PNG produce a determinant, and what is the watermelon?</summary>

Each line below the first uses, as its creation points, the **annihilation** points of the line above.
The lines then stay ordered — they never intersect. Non-intersecting Markov chains have transition
probabilities given by a determinant of individual transition probabilities (Lindström–Gessel–Viennot
/ Karlin–McGregor), so you get a determinantal formula — available since Gessel, 1990. The continuum
analogue is n Brownian motions from 0 to 1 conditioned never to intersect: the **watermelon**. Cutting
it in the middle gives n heights distributed exactly as the eigenvalues of a GUE matrix, so the top
line rescales to **GUE Tracy–Widom**. *(The captions say GOE at this point; that is wrong — GOE is the
flat-initial-data answer.)*
</details>

<details>
<summary>6. What was the biorthogonalization obstruction, and how was it solved?</summary>

TASEP's Fredholm kernel is built from Charlier polynomials **shifted by the initial data**, and needs
their biorthogonal family. For step/narrow-wedge data the Charlier polynomials biorthogonalize
themselves; for flat data Sasamoto and Borodin–Ferrari–Prähofer–Sasamoto did it by linear algebra
around 2007; in general nobody had an idea. Quastel: "you try it, it doesn't work, and then you
realize you don't have a second idea." The solution (Matetski–Quastel–Remenik): the biorthogonal
functions are expressed through the probability that a **random walk hits the region under the initial
data curve**. In the 1:2:3 limit this becomes Brownian hitting probabilities of the hypograph of h₀ —
the Brownian scattering transform.
</details>

<details>
<summary>7. In what sense is the KPZ fixed point an integrable system, given that nothing is conserved?</summary>

The random dynamics is not the integrable object; the **transition probabilities** are, and they are
deterministic. The flow of kernels is linearized by the Brownian scattering transform:
K_t^{hypo(h₀)} = e^{−t∂³/3} K_0^{hypo(h₀)} e^{t∂³/3}, equivalently the Lax equation
∂_t K_{t,ext} = [−⅓∂³, K_{t,ext}], with the time dependence completely decoupled from the initial
data. Lift initial data to an operator, evolve linearly, come back down by a Fredholm determinant —
the three steps of inverse scattering. Quastel presents this as a proposal for what "stochastic
integrable system" should mean, explicitly inviting alternatives.
</details>

<details>
<summary>8. State the KP result and say why Quastel is unhappy about it.</summary>

For F(t,x,r) = P_{h₀}(h(t,x) ≤ r), the function φ = ∂²_r log F satisfies the KP-II equation
∂_tφ + ½∂_r(φ²) + (1/12)∂_r³φ + ¼∂_r^{-1}∂_x²φ = 0, reducing to KdV for flat initial data, with a
matrix KP equation for several space points. The Tracy–Widom distributions are self-similar solutions.
He is unhappy because there is no reason for it: the proof is a long computation on the Fredholm
determinant that happens to cancel. "All we can do is prove it. How pathetic is that?" The published
remark calls it "the first example of a physical law having been obtained in such a fashion."
</details>

<details>
<summary>9. What is the Brownian Gibbs property, and why did characterizing the Airy line ensemble change the field?</summary>

Erase all the curves of the line ensemble inside an interval, then paste back independent Brownian
bridges matching the boundary values and conditioned not to intersect anything; the law is unchanged
(Corwin and Hammond). Aggarwal and Huang proved this property, plus parabolic asymptotics at infinity,
**uniquely characterizes** the Airy line ensemble (arXiv:2308.11908). This replaced a formula-based
definition by an axiomatic one, so convergence proofs became verifications of two properties rather
than computations of a limit — which immediately reached ASEP, and hence the KPZ equation, neither of
which is exactly solvable.
</details>

<details>
<summary>10. Why can nobody prove the Eden model or ballistic aggregation is in the KPZ class?</summary>

Several reasons; the one Quastel explains is decisive. Ballistic aggregation provably has invariant
measures, but **every proof of that is non-constructive** and nobody knows what the measure is. A
sub-problem of proving the 1:2:3 limit is proving it at time zero started from the invariant measure —
so the full statement is strictly harder than showing that invariant measure looks Brownian on large
scales, and even that is open. Separately, the Eden model is **undirected**: two space dimensions and
no time axis, so there is no height function at all, and none of the machinery applies.
</details>

---

## 11. Note on the tutorial process

**Difficulty versus reputation.** Reputation predicts this one correctly, which is not the norm in this
playlist. Quastel is famous for KPZ and the talk is about KPZ. But reputation would have predicted the
**wrong difficulty**. From the outside "KPZ" reads as singular stochastic PDE — the hardest thing in
the neighbourhood, and the thing Otto's talk builds machinery for. In fact Quastel drops the KPZ
equation nine minutes in ("after this we won't even mention stochastic partial differential equations,
so don't get worried") and spends the lecture on determinants, orthogonal polynomials and integrable
systems. The gap for your background is not SPDE. It is integrable probability. That is why the rating
is split 2 / 3 rather than a flat 4.

**The Tier-0 inversion, applied to one half.** The physics half gets a compressed calibration (§3) you
can skim, because you own universality classes, RG fixed points, Langevin dynamics, white noise and
Hopf–Lax. The integrable half gets a full bridge (§4) and the walkthrough carries the length.

**Anchors: which of the brief's held up.**

| suggested anchor | verdict |
|---|---|
| surface growth model | supported — it is the opening slide, but it is setup, not an anchor |
| stochastic Burgers, shocks, turbulence | **partly**. He says "integrated Burgers or Hamilton–Jacobi" and shows the envelope of parabolas. He never says "stochastic Burgers", never mentions shocks or turbulence. Used narrowly, in §2.3 |
| universality class in the statistical-mechanics sense; 1/3 and 2/3 not 1/2 | strongly supported, and stated repeatedly |
| Cole–Hopf ↔ stochastic heat equation | **absent from the talk entirely.** Named as absent in §2.4 rather than imported |
| Tracy–Widom links to random matrices | strongly supported — the watermelon-cut-equals-GUE picture is his |

The anchors actually used are the two the **speaker hands over**: the KPZ fixed point as the central
limit theorem for surfaces (he draws the analogy himself, saying fixed points are "a good place to look
for integrability"), and the construction as an **inverse scattering transform** (he names his own
machine "the Brownian scattering transform" and the answer solves KP). Per the template's guidance, a
speaker-supplied anchor beats a searched one.

**Name corrections.** The captions destroy nearly every proper noun. All corrections below are verified
against the companion, the cited primary literature, or the speaker's publication list.

| Caption | Correct |
|---|---|
| Jeremy Quest / Jeremy Quaster / Questell | **Jeremy Quastel** |
| Carter Puer Jiang / KPZ | **Kardar–Parisi–Zhang** |
| Vadan | S. R. S. **Varadhan** (PhD adviser, Courant, 1990) |
| Chuck Newman | Charles ("Chuck") **Newman** |
| Constantine Mateeski | Konstantin **Matetski** |
| Daniel Rmenik | Daniel **Remenik** |
| Gel (1990) | Ira **Gessel** (1990) |
| Sasimoto | Tomohiro **Sasamoto** |
| Bordon | Alexei **Borodin** |
| charlier polomials | **Charlier** polynomials |
| Takushi | Kazumasa **Takeuchi** |
| Corwin and Hammond | Ivan **Corwin** and Alan **Hammond** ✓ |
| Agrawal and Huang | Amol **Aggarwal** and Jiaoyang **Huang** |
| Mol Argawal | Amol **Aggarwal** |
| Duncan Diver | Duncan **Dauvergne** |
| Bound Ber | Bálint **Virág** |
| Ver and Ramirez | **Virág** and **Ramírez** (Alejandro Ramírez) |
| Johansson and Roman bike | **Johansson** and **Rahman** (Kurt Johansson, Mustazee Rahman) |
| leu | **Liu** (Zhipeng Liu) |
| delta boza gas | **delta Bose gas** |
| beta anzot solvable | **Bethe ansatz** solvable |
| back baxter | **Yang–Baxter** |
| free fermon | **free fermion** |
| TAP | **TASEP** |
| "back and forth versions of the TAP" | **ASEP** (the two-directional exclusion process) |
| PNG | **polynuclear growth** |
| ketam pas equation / KP2 | **Kadomtsev–Petviashvili**, KP-II |
| discrete hi herota equations | discrete **Hirota** equations |
| 2D totalis | 2D **Toda** lattice |
| Edward's Wilkinson | **Edwards–Wilkinson** |
| Koma backward / kamoga of backward equations | **Kolmogorov** backward equations |
| Chapman Koma grav | **Chapman–Kolmogorov** |
| fafian formulas | **Pfaffian** formulas |
| area sheet / ary sheet | **Airy sheet** |
| area line ensemble | **Airy line ensemble** |
| Bernie Gibbs / brand and Gibbs property | **Brownian Gibbs** property |
| Jeffrey Williams prize | **Jeffery–Williams** Prize (CMS) |
| fred holm determinant | **Fredholm** determinant |
| igen value | **eigenvalue** |
| herian | **Hermitian** |
| plus on process | **Poisson** process |
| lelassian | **Laplacian** |
| langan dynamics | **Langevin** dynamics |
| marov / markup chains | **Markov** chains |
| determinal formula | **determinantal** formula |
| bythogonalize / biothogonal | **biorthogonalize** / **biorthogonal** |
| polaron condensates | **polariton** condensates *(reconstructed — see below)* |

**Students named but not named.** Quastel refers to two of his students without giving names. Both are
identified here from published work, not guessed:

- "my student in his thesis was able to construct the half-space KPZ fixed point" → **Xincheng Zhang**,
  *TASEP in half-space*, [arXiv:2409.09974](https://arxiv.org/abs/2409.09974); Toronto PhD thesis *The
  totally asymmetric exclusion process and the KPZ fixed point in the half-space*, supervised by
  Quastel.
- "this is the thesis of one of my students" (the menagerie of solvable models ↔ discrete Hirota
  equations) → **C. Alexander Rodriguez**, [arXiv:2509.16316](https://arxiv.org/abs/2509.16316);
  Toronto PhD thesis *Non-abelian Hirota–Miwa equations for the KPZ universality*, supervised by
  Quastel. Note the discrepancy: he says "like 10 of them" from the podium, the thesis abstract says
  **eighteen** models across four scaling regimes. I quote the thesis and flag it.

**Reconstructed, not verified.**

- The **title**. He describes the talk as being about "random interface growth"; no programme listing I
  could reach gives a title, and the SIAM proceedings contents page returns HTTP 403.
- The introducer's name — "Thanks Pablo" — is the only clue. Not reconstructed; omitted.
- "polaron condensates" → **polariton** condensates. Polariton condensates are the systems in which KPZ
  phase-ordering has been reported in the physics literature; "polaron" is the closest phonetic
  neighbour and is not such a system. Marked as reconstructed in §5.18.
- The **multi-line PNG** construction is due to Prähofer and Spohn. Quastel does not name them in the
  captions; the attribution in §5.7 is mine, from the literature.
- The **derivation of the 1:2:3 scaling** in §4.1 is mine, assembled from three statements he makes
  aloud (Brownian in the middle, the spreading parabola, "you're absolutely forced to look at times of
  order ε^{-3/2}"). It reproduces his stated exponents exactly, which is the check.
- The introducer's prize list is partly unverifiable from the captions ("the poly prize in 24 and the
  polani award in 26"). The published record gives: CRM–Fields–PIMS Prize 2018, CMS Jeffery–Williams
  Prize 2019, EMS Paul Lévy Prize in Probability 2024, NSERC John C. Polanyi Award 2025, FRSC 2016,
  FRS 2021. I have not reproduced the introducer's version because I cannot reconcile the years.

**Substantive caption errors corrected, not just spellings.** Two, and both matter.

1. **"GOE Tracy–Widom" for the narrow wedge** (§5.7). In the same paragraph he correctly says
   "Gaussian unitary ensemble" twice, and then the caption has him conclude "this GOE Tracy–Widom
   distribution." That is the wrong ensemble and the reverse of the truth: narrow wedge → **GUE**, flat
   → **GOE** (Quastel–Remenik, arXiv:1908.10353 §1; Remenik, arXiv:2205.01433 §§2, 4). Corrected in the
   text with the correction flagged in place. **Impact if uncorrected: high** — the whole watermelon
   picture is a GUE picture and the paragraph would be self-contradictory.
2. **"t equals about n² points in the box"** (§5.6). Inverted. The space-time box has area of order t²,
   so the number of Poisson points is n ≈ t², i.e. t ≈ √n. With the correction, L_n ≈ 2√n gives height
   ≈ 2t and n^{1/6} gives fluctuation t^{1/3}; with the caption as written, neither works. Corrected
   with a gap marker in place. **Impact if uncorrected: moderate** — it breaks the exponent check,
   which is the whole point of the reduction.

**Where the mathematics is unrecoverable, and how bad it is.**

- **Every formula in the talk.** Quastel explicitly declines to display the main formula — "I was warned
  not to show you the formula" — and the rest lived on slides invisible to the caption track. **Impact:
  low.** Almost everything is recoverable from the cited published sources, because the talk follows the
  companion's outline closely. Each equation above carries its citation.
- **The "linear dials"** — the exact linear PDEs by which the kernel is evolved in the spatial and
  height variables. I have given only the schematic Lax form and the spatial identity as stated in the
  companion (eqs. (5.1)–(5.2)). The precise operators he pointed at were on the slide. **Impact:
  moderate**, and it is the one place where a reader wanting to implement the formula must go to the
  papers.
- **The half-space Pfaffian formulas, the multi-time formulas, and the discrete Hirota equations** are
  named but never displayed. **Impact: low** — each is a pointer to a paper, and the papers are cited.
- **No theorem is stated from the podium** with hypotheses. §6 assembles the claim from the published
  sources and says so.

**Length.** Comparable to the two model tutorials, and shorter than the Otto one. The talk is a single
argument rather than two half-talks, so the walkthrough carries most of the weight and the bridge is
one section rather than a whole document.

**What the write-up cannot carry.** This lecture was driven by **animations**. The sticky ballistic
deposition movie, the polynuclear growth simulation with the vertical axis squashed and unsquashed, the
watermelon, and the Brownian-Gibbs resampling animation — erase, paste back, unchanged — each did work
that no sentence does. Two of the arguments in this tutorial (§4.1 and §5.15) are reconstructions of
things he showed rather than said. Where a section here feels thinner than it should, that is where a
picture was carrying the argument.
