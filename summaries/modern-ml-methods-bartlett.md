---
title: "Modern Machine Learning Methods: Large Scale Optimization, Implicit Bias and Benign Overfitting"
speaker: Peter L. Bartlett (UC Berkeley; Google DeepMind)
source: https://www.youtube.com/watch?v=l-29P4oEXKE
video_id: l-29P4oEXKE
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: "none — companion: https://arxiv.org/abs/2103.09177"
transcript: ../transcripts/l-29P4oEXKE_transcript.txt
difficulty_for_you: 2/5 (the mathematics) — 3/5 (the statistical-learning frame)
reading_time: ~55 min
---

# Modern Machine Learning Methods — Peter Bartlett

**Field:** statistical learning theory, aimed squarely at deep learning. Three results, in
three simple settings: logistic regression, homogeneous parameterizations, and linear
regression.

**Difficulty against your background: 2 out of 5 for the mathematics, 3 out of 5 for the
frame.** Every mathematical object in this talk is one you own — gradient flow, forward
Euler, Hessian eigenvalues, Taylor's theorem, Euler's homogeneous-function theorem, KKT
conditions, the spectral decomposition of a covariance operator, the Moore–Penrose
pseudoinverse, ridge regression. What you do not own is the *statistical* half: excess
risk, uniform convergence, complexity control, margin bounds, effective rank. So this
tutorial inverts the usual shape twice over. The optimization background is compressed to
a calibration page you can skip. The statistical vocabulary gets a real bridge. And the
length goes to the three results, which are from 2019, 2024 and 2025.

**What this tutorial builds:** the three-way decomposition of a learning method and which
of its three classical answers modern practice broke; excess risk and why it is not
training loss; the margin bound and why it is dimension-free; positive homogeneity and
near-homogeneity of a parameterized family; the two effective ranks of a covariance
operator; and the mechanism by which an interpolating estimator is secretly a ridge
estimator.

**A note on sources — read this one.** There is **no ICM 2026 proceedings paper for this
talk.** A sweep of arXiv found no preprint under Bartlett's name matching the lecture, and
the SIAM proceedings volume does not surface one. So the highest-preference source in the
spec does not exist here.

What I used instead:

- **The companion, and it is a companion, not the proceedings paper:** Bartlett,
  Montanari and Rakhlin, *Deep learning: a statistical viewpoint*, Acta Numerica 30 (2021)
  87–201, [arXiv:2103.09177](https://arxiv.org/abs/2103.09177). This is the speaker's own
  survey on this exact topic, and **he names it from the podium** — "there's a review
  paper, an Acta Numerica paper, that covers this" — when introducing the
  simple-plus-spiky decomposition in part three. It covers parts two and three of the talk
  well. It **predates part one entirely**: the large-stepsize work is 2024–2025 and is not
  in it.
- **Primary literature for the specific theorems**, which is not the same thing as a
  companion document. Where I state a rate, a threshold or a definition that the
  auto-captions could not carry, it comes from the paper that proved it, and I name that
  paper inline. The four that matter are
  [arXiv:2402.15926](https://arxiv.org/abs/2402.15926) (part one),
  [arXiv:2006.06657](https://arxiv.org/abs/2006.06657) and
  [arXiv:2502.16075](https://arxiv.org/abs/2502.16075) (part two), and
  [arXiv:1906.11300](https://arxiv.org/abs/1906.11300) (part three).

**Auto-captions and this talk.** The captions destroyed the Greek. The step size η is
transcribed throughout as "eater", and the rate 1/(ηt) is transcribed as "one over e to
t" — which reads as an exponential and is not one. Every proper noun is mangled. The
corrections are tabulated in §12. Two names I could not verify, and I have not guessed
them.

**Cross-references.** Wright's plenary the following day covered the same terrain from the
optimizer's side. Where the two talks overlap I point at
`optimization-theory-practice-wright.md` rather than rewriting it.

---

## 1. What is at stake

Bartlett opens with a frame you can use on any learned system, and the whole hour is
organised by it. Designing a statistical learning method involves three questions, and
classically they are **modular** — you can answer them one at a time.

1. **Approximation.** You restrict yourself to a class of functions. How well can anything
   in that class model the relationship you care about?
2. **Optimization.** Given a finite training sample, can you efficiently find parameters
   that fit it well?
3. **Statistics.** You do not actually care about the fit to the sample. You care that
   good fit on the sample *implies* accurate prediction at deployment. Does it?

On the left, the classical answer you would find in any textbook written before about 2015.
On the right, what practitioners actually do — and every row is broken.

| | Classical | Modern practice |
|---|---|---|
| Approximation | Rich non-parametric function classes. | Still rich, but the richness comes from **depth and composition**, and from mechanisms like attention. |
| Optimization | Parameterize linearly, use a convex loss, exploit convexity. | The parameterization is "really ugly": composing parameterized functions makes the problem badly non-convex even with a convex loss. Simple gradient methods find very good solutions anyway — apparently *because* the parameter space is high-dimensional. |
| Optimization | Use stable algorithms — time discretizations of stable differential equations. | Use step sizes **large enough that the algorithm is locally unstable**, and get better performance for it. |
| Statistics | **Explicitly** control the complexity of the prediction rule; regularize so it lives in a bounded-complexity set. | Nothing explicitly controls complexity. Whatever control exists is supplied **implicitly by the optimizer**. |
| Statistics | Use uniform convergence: inside such a set, sample averages converge to expectations uniformly, so good training performance implies good deployment performance. | The solutions fit **noisy** data perfectly, so uniform convergence cannot apply. "Too good to be true" — and prediction is good anyway. |
| Statistics | Assume the data are i.i.d. from a fixed distribution. | Nowhere near i.i.d. Models are trained on the internet and deployed on mathematics. |

Bartlett is careful about the word for the fifth row. A perfect fit to noisy data *is*
overfitting, in the plain sense that the fit is too good to be true. But the overfitting
turns out to be **benign** — it does not cost you predictive accuracy. He calls that "a
genuinely new statistical phenomenon."

The talk takes three of these breakages and shows an accessible mathematical result for
each, in the simplest setting where the phenomenon still occurs.

---

## 2. Calibration: what you can skip

Skim this and go to §3. It is here only to fix notation.

**The problem.** Parameters w ∈ ℝ^d, a training set (x₁,y₁),…,(x_n,y_n), and an empirical
loss L(w) = (1/n)∑ᵢ ℓ(w; xᵢ, yᵢ). Gradient descent with a fixed step size η:

$$w_{t+1} = w_t - \eta \nabla L(w_t)$$

**Gradient descent is forward Euler.** The continuous object is gradient flow,

$$\dot{w} = -\nabla L(w),$$

and the update above is explicit Euler applied to it with time step η. Bartlett draws
exactly this picture (he credits the figure to Francis Bach's website): a red gradient-flow
curve, and a polygonal Euler path shadowing it.

**The stability boundary, by Taylor.** Expand L around w_t along the step −η∇L(w_t):

$$L(w_{t+1}) \le L(w_t) - \eta\|\nabla L(w_t)\|^2 + \tfrac{1}{2}\eta^2 \lambda_{\max}\|\nabla L(w_t)\|^2$$

where λ_max bounds the largest eigenvalue of the Hessian on the segment between w_t and
w_{t+1}. The bracket −η + η²λ_max/2 is negative — a strict decrease unless you are already
at a stationary point — exactly when

$$\eta < \frac{2}{\lambda_{\max}}.$$

For a quadratic L this is an if-and-only-if: gradient descent is then a linear recurrence
w_{t+1} = (I − ηH)w_t, and it is stable precisely when ηλ_max < 2. You know this as the
absolute-stability interval of explicit Euler on the negative real axis. It is the same
inequality, and it is the CFL-style limit you would impose on a stiff ODE.

**Logistic regression, the running example.** Covariates x ∈ ℝ^d, labels y ∈ {+1,−1},
linear predictor f̂_w(x) = ⟨w, x⟩, prediction sign(⟨w,x⟩). The probability model is
P(y=1|x) = 1/(1+e^{−f̂(x)}), and the loss is the negative log-likelihood:

$$L(w) = \frac{1}{n}\sum_{i=1}^{n} \ln\!\left(1 + \exp(-y_i\langle w, x_i\rangle)\right)$$

Convex in w. Bartlett notes this is the same loss used to train large language models —
multiclass rather than binary, and over a vastly more complex parameterized family, but
the same convex loss.

**Separable data.** Assume ‖xᵢ‖ ≤ 1, and that some unit vector w\* classifies every
training point with margin γ > 0: ⟨yᵢxᵢ, w\*⟩ ≥ γ. Then pushing w arbitrarily far in the
w\* direction drives L to zero. **The minimizer is at infinity.** That is not a pathology;
Bartlett notes it is what you see in the high-dimensional regime.

That is the whole prerequisite for parts one and two. Part three needs only the spectral
decomposition of a covariance matrix and the pseudoinverse.

---

## 3. The bridge: the five words you do not already own

This is the part that is genuinely new for you, so it gets real space.

**3.1 Excess risk is not training loss.** Let (x,y) come from a distribution P. The *risk*
of a predictor is its expected loss under P — what happens at deployment. The *empirical
risk* is the average over your n training points — what you can actually compute. The
**excess risk** of an estimator θ̂ is

$$R(\hat\theta) = \mathbb{E}\,(\langle \hat\theta, x\rangle - y)^2 - \mathbb{E}\,(\langle \theta^*, x\rangle - y)^2$$

that is, how much worse θ̂ predicts than the best possible parameter θ\*. You want it near
zero. Everything statistical in this talk is a bound on this quantity. Note what it is not:
it is not the training loss, and driving the training loss to zero says nothing about it
directly.

**3.2 Statistical complexity, and uniform convergence.** The classical machinery for
connecting the two runs as follows. Restrict your predictors to a set F. If F is
"small" in a suitable sense, then

$$\sup_{f \in F} \left| \text{(empirical risk of } f) - \text{(risk of } f)\right| \to 0$$

as n grows — *uniformly over F*, which is the crucial word, because your estimator was
chosen using the data and so is not a fixed f. The measure of "small" is the **statistical
complexity** of F — VC dimension, covering numbers, Rademacher complexity, or the parameter
count — and classically you keep it small *explicitly*, with a regularizer, a norm
constraint or a bandwidth.

Notice why this cannot survive a perfect fit to noisy data. If the class contains a rule
with zero empirical risk on partly random labels, it is rich enough to realize any
labelling, and the supremum above does not go to zero. Uniform convergence here is not
loose; it is unavailable.

**3.3 Margin, and the one bound that is dimension-free.** For linearly separable data
define

$$\hat{w} = \arg\min \|w\| \quad \text{subject to} \quad y_i \langle w, x_i\rangle \ge 1 \ \ \forall i.$$

This is the hard-margin support vector machine. Rescaling shows it is the same as
maximizing the distance from the decision boundary to the nearest training point — hence
"maximum margin".

The result Bartlett calls "work from the last millennium" says: with probability at least
1 − δ over an i.i.d. sample, the misclassification probability of the classifier
sign⟨ŵ, ·⟩ is bounded by a quantity depending on **‖ŵ‖² / n** — the squared norm of that
solution over the sample size — plus a term in log(1/δ) for the chance that the sample was
unrepresentative.

> *[Gap: the exact form — constants, logarithmic factors, the role of the radius bound
> ‖xᵢ‖ ≤ 1 — was on the slide. The captions carry only the ratio ‖ŵ‖²/n. The shape above
> is what the talk states verbally.]*

Now the point, and it is the whole reason to care. The classical bound for a
d-dimensional linear class scales as **d/n**, which is vacuous when d ≫ n. The margin
bound does not mention d at all. So in a very high-dimensional setting, if the optimizer
hands you a large-margin classifier — small ‖ŵ‖ — you get a good guarantee *even though
the dimension exceeds the sample size*. This is why Bartlett calls the max-margin property
"statistical complexity control": ‖ŵ‖² is playing the role that the parameter count plays
classically.

**3.4 Implicit bias.** When the parameter space is high-dimensional, the set of parameters
achieving small loss is enormous. From the optimizer's point of view they are
interchangeable — all of them are good solutions. From the statistician's point of view
they are wildly different — some predict well, some do not. **Implicit bias** is the
observation that a gradient method does not return an arbitrary member of that set. It
returns a *particular* one, determined by the algorithm and the initialization, and that
choice is what supplies the complexity control that nobody wrote down. Part two of the
talk identifies which one.

**3.5 Benign overfitting.** A perfect (interpolating) fit to noisy training data that
nevertheless predicts well. Part three of the talk gives a complete characterization of
when this happens in linear regression.

---

## 4. Part one — large step sizes, and the edge of stability

*Joint work with Jingfeng Wu, Yuhang Cai, Pierre Marion, Michael Lindsey, Song Mei, Bin Yu
(all Berkeley) and Matus Telgarsky (formerly NYU; the talk says he is now at OpenAI).*

### 4.1 The anchor: you already believe the opposite of this

Here is the correspondence, and it is not decorative. §2 gave you η < 2/λ_max, and you
know it as the absolute-stability condition for explicit Euler. Every instinct you have
from numerical analysis says: violate it and the scheme blows up. You choose the step size
to *stay inside* the stability region; that is the entire discipline of integrating a stiff
system explicitly.

Bartlett's first result says that for logistic regression on separable data, running
**deliberately outside the stability region is not merely survivable — it is necessary**
for the best rate. That is the whole of part one, and it should feel wrong to you. It is
worth understanding why it is not.

### 4.2 The phenomenon

Bartlett shows a training-loss curve for a digit-classification network: iterations of
gradient descent on the x-axis, training loss on the y-axis, two step sizes. The green
curve uses a small step size and decreases monotonically. The red curve uses a step size
clearly violating η ≤ 2/λ_max — we know this because the loss is *not* monotone; it spikes.

And the red curve ends up **lower**. The spikes are not a failure to be tolerated; the run
that spikes reaches a smaller loss later.

This is not a curiosity of one network. Bartlett: this instability "is really quite
ubiquitous" in neural networks trained this way. The phenomenon has a name — the **edge of
stability** — for running with η near or above the critical value 2/λ_max.

### 4.3 The theorem

Setting: logistic regression, linearly separable data, ‖xᵢ‖ ≤ 1, margin γ > 0, **fixed**
step size η, gradient descent from w₀.

> **Theorem (Wu, Bartlett, Telgarsky, Yu, COLT 2024;**
> **[arXiv:2402.15926](https://arxiv.org/abs/2402.15926)).**
> **For every η > 0**, gradient descent has two phases.
>
> **Edge-of-stability phase.** For all t, the *average* of the losses of the iterates so
> far satisfies
>
> $$\frac{1}{t}\sum_{k<t} L(w_k) \;=\; \tilde{O}\!\left(\frac{1}{\gamma^2\eta t}\right)$$
>
> up to logarithmic factors and an additive term in η. This inequality holds throughout
> training, but it is the useful statement in the early phase where the loss may be
> bouncing around.
>
> **Transition.** Gradient descent leaves the non-monotone phase within
> τ = O( max{η, n} / γ² ) steps, up to logarithmic factors.
>
> **Stable phase.** Once L(w_s) ≤ 1/η, the loss decreases monotonically from then on, at
> rate Õ(1/(γ²η(t−s))).

Read the first three words again. **For every η > 0.** It does not matter how large you
make the step size. Bartlett: "any step size is okay, which is kind of an extraordinary
thing."

From the podium he states the rate as "one over ηt, and the constant turns out to be one",
suppressing the γ² and the logarithms that the written theorem carries. The transcript
renders "one over ηt" as "one over e to t", which reads as an exponential decay and is
wrong by a wide margin; see §12.

### 4.4 Why "for every η" is not absurd

The captions give no mechanism. Here it is, restored from the paper; it is the property
the paper calls **self-boundedness**, and once you see it the theorem stops being
surprising.

Write z = y⟨w,x⟩ for a margin, σ(z) = 1/(1+e^{−z}), and ℓ(z) = ln(1+e^{−z}). The Hessian
of the logistic empirical loss is

$$\nabla^2 L(w) = \frac{1}{n}\sum_{i=1}^n \sigma'(z_i)\, x_i x_i^\top, \qquad \sigma'(z) = \sigma(z)\big(1-\sigma(z)\big).$$

Now the key inequality. For z ≥ 0,

$$\sigma'(z) \;\le\; 1-\sigma(z) \;=\; \frac{1}{1+e^{z}} \;\le\; e^{-z} \;\le\; \frac{\ell(z)}{\ln 2},$$

the last step because ln(1+u) ≥ u ln 2 for u ∈ [0,1], applied with u = e^{−z}. So, once all
training points are correctly classified and ‖xᵢ‖ ≤ 1,

$$\lambda_{\max}\big(\nabla^2 L(w)\big) \;\le\; \frac{1}{\ln 2}\, L(w).$$

**The curvature is bounded by the loss.** So the stability condition η < 2/λ_max is
implied by

$$L(w) \;<\; \frac{2\ln 2}{\eta},$$

which is a threshold that scales as 1/η — exactly the paper's "once L(w_s) ≤ 1/η, the loss
decreases monotonically." The mechanism is now transparent:

- On a quadratic, λ_max is a constant. Exceed 2/λ_max and you diverge forever.
- On the logistic loss with separable data, λ_max **shrinks as the loss falls**. The
  stability boundary is not fixed; it moves toward you. So a step size that is unstable at
  the start becomes stable of its own accord once the loss has dropped below ≈ 2ln2/η. A
  bigger η simply means you must wait longer, and the theorem's τ = O(max{η,n}/γ²) is that
  wait.

*Marked: the algebra above is my derivation from the standard logistic-loss identities. It
is not in the captions. It is consistent with the paper's Assumption 3C (self-boundedness,
g ≤ Cβℓ) and reproduces the paper's 1/η threshold. What would verify it: Lemma-level
statements in [arXiv:2402.15926](https://arxiv.org/abs/2402.15926). You will also derive it
yourself in §7.1.*

### 4.5 The payoff: acceleration with no momentum

Now the trade-off Bartlett draws out. A larger η buys a better constant in the asymptotic
1/(ηt) rate, and costs a longer unstable phase. Both effects are explicit, so you can
optimize the exchange.

Suppose you have a **budget of T steps**. Choose η large as a function of T so that you
spend roughly the first half of the budget bouncing and the second half in monotone decay.
The paper's choice is η := γ²T/120, and the conclusion is

$$L(w_T) = O\!\left(\frac{\ln^2 T}{T^2}\right).$$

Sit with that. Gradient descent, one fixed step size, no momentum, no schedule, and the
final loss falls like **1/T²**.

1/T is the classical convex rate for gradient descent. 1/T² is the *accelerated* rate — the
one you get from Nesterov's method, which Bartlett notes goes back to the 1980s and whose
author, Yurii Nesterov, gave the Gauss Prize lecture earlier at this same congress. Nesterov's
method is naturally read as a discretization of a **second-order** ODE. Here the same
exponent falls out of plain first-order gradient descent, purely by choosing the step size
badly on purpose.

### 4.6 And the instability is not optional

The obvious question: is the instability doing the work, or is it incidental? Bartlett
answers it.

> **Theorem (same paper, Theorem 3).** If gradient descent with a constant step size
> maintains a monotone decrease of the loss, then L(w_t) ≥ c₀/t.

So the 1/T² rate is unreachable inside the stability region. Non-monotonicity is not a side
effect you tolerate; **it is the source of the acceleration**. (Bartlett attaches a
non-triviality condition — you must not have started at a point where the gradient direction
already solves the problem, and you must not be allowed to take one arbitrarily large step
that drives the loss to zero by itself.)

### 4.7 The same moral, twice at this congress

This is worth flagging explicitly because it is a genuine convergence of two independent
lines of work at the same meeting.

Wright's plenary (see `optimization-theory-practice-wright.md`, §4.1) covers **silver step
sizes** — Altschuler and Parrilo. There, one asks for the step *sequence* that gives the
best improvement over a horizon of many iterations rather than the best improvement at each
step. The answer is a non-uniform schedule containing occasional very long steps that **may
go uphill**, and it improves the strongly convex rate from O(κ log(1/ε)) to
O(κ^{0.786} log(1/ε)).

Different setting, different mechanism, different proof. Same moral:

> The classical requirement that the loss decrease at every iteration is a constraint you
> are *paying for*. Drop it and you provably do better.

Two ICM plenaries, one day apart, arriving at that from opposite directions. If you take one
thing from part one, take that.

### 4.8 How far it extends

Bartlett is careful about scope. The clean theorem is for linear predictors with logistic
loss. It has been pushed outward:

- **Neural tangent kernel regime** — linearize the network in parameter space around
  initialization and analogous results follow. (For what NTK is, see
  `optimization-theory-practice-wright.md` §6.4.)
- **Genuinely nonlinear** settings, with restricted network families and extra conditions on
  the training data.
- **Deep networks satisfying a mild condition on the parameterization** — near-homogeneity,
  the subject of part two. In the stable phase the convergence behaviour is similar.
- **Minimizer at finite distance.** Everything above assumed the optimum is at infinity, as
  in the separable high-dimensional case. If it is instead a finite point, the acceleration
  still appears, now as the speed-up for smooth strongly convex optimization: Õ(κ)
  iterations improved to Õ(√κ) ([arXiv:2506.02336](https://arxiv.org/abs/2506.02336), Wu,
  Marion and Bartlett).

He mentions further recent advances and declines to spend time on them.

---

## 5. Part two — implicit bias: the optimizer chooses the solution

*Joint work with, among others, Sham Kakade (Harvard) and Kangjie Zhou (Columbia).*

Part one was about optimization: how fast the loss falls. Part two asks the statistical
question about the same setting. In a rich parameterization, a huge set of parameters
achieve small loss. **Which one does gradient descent return, and is it a good one?**

### 5.1 The linear answer: direction converges to max margin

Recall that on separable data the logistic minimizer is at infinity, so ‖w_t‖ → ∞. The
parameter diverges. But the *direction* does not.

> **Theorem (Soudry, Hoffer, Nacson, Gunasekar and Srebro).** Run gradient flow, or gradient
> descent with a small step size, on the logistic loss over linearly separable data. Then
> w_t/‖w_t‖ converges to ŵ/‖ŵ‖, where ŵ solves
>
> $$\min \|w\| \quad \text{s.t.}\quad y_i\langle w, x_i\rangle \ge 1 \ \forall i$$
>
> — the maximum-margin classifier of §3.3.

Nothing in the logistic objective mentions margins. Nothing in gradient descent mentions
norms. The algorithm nevertheless selects, out of the infinitely many directions that drive
the loss to zero, the one with the smallest norm at unit margin.

And by §3.3, that is precisely the direction with a **dimension-free generalization bound**.
So the answer to "why does an unregularized method in a huge parameter space still
generalize?" is: it was regularized after all, by the optimizer, and the regularizer it
implements is ‖w‖.

That is the entire content of the phrase *implicit regularization*, made concrete in the
simplest possible case. Wright cites this result in his §6.4 list of explanations for
overparameterized generalization, and attributes it to this talk; here is the actual
statement.

### 5.2 The anchor: Euler's homogeneous-function theorem

Bartlett's next move is to ask what property of the linear model made that work. It is not
linearity. It is **homogeneity**, and here you have a real anchor.

A function f is **positively m-homogeneous** if f(αθ) = α^m f(θ) for all α > 0. For smooth f
this is equivalent — and Bartlett says so explicitly, crediting Euler — to

$$\langle \nabla f(\theta), \theta \rangle = m\, f(\theta).$$

This is Euler's homogeneous-function theorem, and you already use it constantly. In
thermodynamics, internal energy U(S,V,N) is 1-homogeneous in the extensive variables, and
Euler's identity applied to it is exactly

$$U = \left(\frac{\partial U}{\partial S}\right)S + \left(\frac{\partial U}{\partial V}\right)V + \left(\frac{\partial U}{\partial N}\right)N = TS - pV + \mu N,$$

the Euler relation, from which Gibbs–Duhem follows by differentiating. The identity
Bartlett writes on the board and the identity behind U = TS − pV + μN are the same identity.
Here the "extensive variables" are the network weights, and the "extensivity" is a scaling
property of the architecture rather than of matter.

**Homogeneity of a parameterized family.** We care about scaling in the *parameters*, not
the input. Examples:

- A linear predictor ⟨θ, x⟩ is 1-homogeneous in θ. Trivially.
- Write a linear function in a redundant, layered way as a product of L parameter blocks.
  Scaling every block by α scales the output by α^L. That family is **L-homogeneous**.
- ReLU, u ↦ max(u,0), is 1-homogeneous. So an L-layer network alternating linear maps with
  ReLU, and no bias terms, is **L-homogeneous** in its parameters.

**And it is brittle.** Replace the linear layers with affine ones — add biases — and
L-homogeneity is lost. Bartlett flags this as the reason to want something weaker.

### 5.3 The homogeneous answer: KKT points

> **Theorem (Ji and Telgarsky, NeurIPS 2020;**
> **[arXiv:2006.06657](https://arxiv.org/abs/2006.06657)).** Run gradient flow on the
> logistic loss with an m-homogeneous parameterized family. Once the loss drops below a
> threshold, the parameter direction converges — not to *the solution* of the margin problem,
> but to a **KKT point** of it.

The weakening is exactly what you would expect from losing convexity. The margin
maximization problem is no longer convex in θ, so first-order necessary conditions are the
most you can ask for. KKT — Karush–Kuhn–Tucker — is the constrained analogue of ∇f = 0: at
the limit direction, the gradient of the objective lies in the cone spanned by the gradients
of the active constraints. (The captions render this as "kushka points".)

Bartlett notes the extra technical hypothesis, which is unusual enough to be worth naming:
the family must be **definable in an o-minimal structure**. This is a condition from model
theory guaranteeing that systems of equations built from your functions have only finitely
many solutions on finite intervals — enough to rule out infinite oscillation and so to get
genuine *directional* convergence rather than endless wandering. He calls it very mild for
the function families used in deep learning, and it is: polynomials, exponentials, and
piecewise-linear maps are all definable. He also notes that he is attributing to Ji and
Telgarsky the endpoint of a whole line of work (Lyu and Li's *Gradient descent maximizes the
margin of homogeneous neural networks*, [arXiv:1906.05890](https://arxiv.org/abs/1906.05890),
is the other principal reference).

### 5.4 Near-homogeneity, and why it is the right notion

Homogeneity is too brittle — one bias term destroys it. The fix is to require the Euler
identity only *approximately*, with the error allowed to grow, but more slowly than the
leading term.

> **Definition (Cai, Zhou, Wu, Mei, Lindsey, Bartlett, Kakade, Yu, ICML 2025;**
> **[arXiv:2502.16075](https://arxiv.org/abs/2502.16075), Definition 1).** A network f(θ,x)
> is **near-M-homogeneous** if there exist polynomials p, q of degree at most M such that,
> for every data point and every θ, with h in the Clarke subdifferential of f in θ:
>
> $$\big|\langle h, \theta\rangle - M f(\theta, x)\big| \le p'(\|\theta\|), \qquad \|h\| \le q'(\|\theta\|), \qquad |f(\theta,x)| \le q(\|\theta\|).$$

The first inequality is the one to read. The left side is exactly the defect in Euler's
identity. It is allowed to be nonzero, but bounded by p′ — the derivative of a
degree-M polynomial, hence of degree at most **M − 1**. That is Bartlett's phrase from the
podium: the two sides are "close as some suitable degree m minus one polynomial in the scale
of the parameters." An exactly M-homogeneous function has defect zero, so it is
near-M-homogeneous with p ≡ 0. The affine-layer network is not homogeneous, but its defect
grows one degree too slowly to matter.

**The homogenization.** Given a near-M-homogeneous f, define

$$f_{\mathsf{H}}(\theta, x) := \lim_{r\to\infty} \frac{f(r\theta, x)}{r^M},$$

its growth at infinity. This is exactly M-homogeneous, and the paper bounds
|f − f_H| ≤ p_a(‖θ‖) uniformly, with p_a explicit in terms of the p from the definition.

**Then the theorem transfers.** Take the margin-maximization problem, replace the network by
its homogenization, and the directional-convergence-to-KKT-points result of §5.3 holds for
near-homogeneous families. Concretely: gradient methods on logistic loss over the deep
architectures actually used in practice converge in direction to KKT points of the
max-margin problem *for the homogenized network*.

Bartlett stresses the practical part: there is a **calculus** of near-homogeneous functions.
Compose near-homogeneous pieces, apply the standard transformations, and near-homogeneity is
preserved with computable degrees. So you can certify an architecture by inspecting its
layers, which is what makes the notion usable rather than merely correct.

### 5.5 The attention gap

Then the honest caveat, which is the single most important sentence in part two for anyone
working with transformers:

> **It does not cover attention.**

Bartlett's stated reason: the squashing function in the attention mechanism is "a sort of
nearly zero-homogeneous function", and **M = 0 is problematic** in this framework. You can
see why from the definition — with M = 0 the bound p′ is the derivative of a degree-0
polynomial, and the homogenization divides by r⁰ = 1, so the whole scaling apparatus
degenerates. He calls this "an interesting gap".

So the state of play is: we have a clean account of implicit bias for essentially every
architectural component of deep learning **except the one that defines the transformer**.

*[Gap: the talk gives the reason in one sentence and moves on. The captions carry no further
mechanism, and I have not reconstructed one beyond the degenerate-M observation above, which
follows from the definition.]*

---

## 6. Part three — benign overfitting

*Joint work with Philip Long (Google), Gábor Lugosi (Pompeu Fabra), Alexander Tsigler
(then a Berkeley PhD student), Niladri Chatterji (then a Berkeley PhD student), Spencer Frei
and Gal Vardi (postdocs), Nathan "Nati" Srebro (TTI Chicago), Alexander "Sasha" Rakhlin
(MIT) and Andrea Montanari (Stanford). One postdoc first name in the caption track,
"Louis", I could not resolve; see §12.*

### 6.1 The observation that started it

A group at Google — Zhang, Bengio, Hardt, Recht and Vinyals, *Understanding deep learning
requires rethinking generalization*, ICLR 2017 — found that deep networks can be trained to
near-zero training loss and still predict accurately. On its own, Bartlett says, that is not
so surprising from a learning-theory viewpoint.

The surprising part was what happened when they added **label noise**. Take the training set
and randomly flip a fraction of the labels; at the far end of that axis the labels carry no
information at all. Plot test error against the noise fraction, for three different
architectures. The result was a **graceful degradation**: test error rose smoothly with the
noise level rather than collapsing.

Every one of those runs achieves a perfect fit to the training data. So every one of them
has necessarily memorized all of the injected noise. And they still predict.

### 6.2 The classical picture, and the bookshelf

Bartlett puts up a photograph of his own bookshelf and two quotations from textbooks on it.
The classical wisdom is a trade-off: on one axis the fit to the training data, on the other
the complexity of the prediction rule — parameter count, or the norm of a parameter vector as
in §3.3, or the bandwidth of a smoothing kernel. You balance them, and you tell
undergraduates: **do not interpolate; an interpolating fit will not predict well.**

There is no trade-off available in the plots above. Every run sits at zero training loss, so
the classical axis has collapsed to a point — and prediction accuracy still varies smoothly
with something.

> *[Gap: the two textbook quotations are legible on the slide and are not spoken. I do not
> have them.]*

### 6.3 The intuition: simple plus spiky

From the Acta Numerica review (Bartlett, Montanari and Rakhlin, 2021 —
[arXiv:2103.09177](https://arxiv.org/abs/2103.09177)), and this is where he names it: in
every case we understand, the interpolating prediction rule **decomposes into two pieces**.

1. A **simple** component that does the predicting, and is low-complexity in the entirely
   classical sense of §3.2.
2. A **spiky** component that does the memorizing. It fits the noisy examples. It plays no
   role in prediction — it is neither helpful nor harmful.

Bartlett is emphatic that the cartoon of a spiky one-dimensional curve is only a cartoon:
benign overfitting is "very much a high-dimensional phenomenon" and does not occur in one
dimension. The intuition covers nearest-neighbour rules, kernel regression, kernel smoothing
and linear regression as sample size and dimension grow together.

The rest of part three makes "simple plus spiky" precise in the simplest setting where it
happens.

### 6.4 The setting

Covariates x in a high-dimensional space, real-valued response y, both mean zero, with nice
tails. The problem is **well-specified linear**: E[y | x] = ⟨θ\*, x⟩. Write σ² for the noise
variance — the prediction error of θ\* itself. The talk also imposes a **small-ball
condition** on x, ensuring the distribution is not too concentrated. (The PNAS paper states
its assumptions as sub-Gaussian coordinates in the eigenbasis plus a lower bound on the
conditional noise variance; the small-ball formulation is the talk's.)

Let Σ = E[xxᵀ] with eigenvalues λ₁ ≥ λ₂ ≥ …, so λ₁ is the variance along the
highest-variance direction. The criterion is the excess risk R(θ̂) of §3.1.

**Which interpolator?** With d > n there is an affine subspace of parameters achieving a
perfect fit. We want the one a gradient method finds. Run gradient flow on squared error
starting from θ = 0. Every gradient of the squared loss lies in the row space of X, so the
iterate never leaves that span, and the limit is the **minimum-norm interpolator**:

$$\hat\theta = X^\top (XX^\top)^{-1} y = X^{+} y,$$

where X is the n × d matrix of training covariates and y the vector of responses. (Bartlett
writes it as (XᵀX)⁺Xᵀy; with the Gram matrix XXᵀ invertible these agree, and the
Gram-matrix form is the one used in the analysis.)

So the estimator studied is not an arbitrary interpolator. It is the one gradient descent
from zero actually produces — part two's implicit bias, now in the regression setting, where
the implicit regularizer is again the norm.

### 6.5 The two effective ranks

Here is the new vocabulary, and it is the crux. For a covariance operator Σ and an integer
k, drop the k largest eigenvalues and look at what is left in the orthogonal complement:

$$r_k(\Sigma) = \frac{\sum_{i>k}\lambda_i}{\lambda_{k+1}}, \qquad R_k(\Sigma) = \frac{\left(\sum_{i>k}\lambda_i\right)^2}{\sum_{i>k}\lambda_i^2}.$$

Bartlett's own gloss: r_k is the one-norm over the infinity-norm of the tail — "the number
of times you can fit the largest one into all the rest". R_k is the one-norm squared over
the two-norm squared. Both measure how many directions the tail *effectively* occupies. If
the tail has m equal eigenvalues, both equal m. If one eigenvalue dominates, both are ≈ 1.

Now define the **effective dimension**

$$k^* = \min\{k \ge 0 : r_k(\Sigma) \ge bn\}$$

for a universal constant b. In words: k\* is the smallest number of leading directions you
must set aside so that what remains looks nearly isotropic in a space of effective dimension
large compared with the sample size.

### 6.6 The one argument: the characterization, and why it is really ridge regression

> **Theorem (Bartlett, Long, Lugosi and Tsigler, PNAS 2020;**
> **[arXiv:1906.11300](https://arxiv.org/abs/1906.11300), Theorem 4).** Under the
> assumptions of §6.4, if k\* < n/c₁ then with probability at least 1 − δ the minimum-norm
> interpolator satisfies
>
> $$R(\hat\theta) \;\le\; c\,\|\theta^*\|^2\|\Sigma\| \max\!\left\{\sqrt{\tfrac{r_0(\Sigma)}{n}},\ \tfrac{r_0(\Sigma)}{n},\ \sqrt{\tfrac{\log(1/\delta)}{n}}\right\} \;+\; c\log(1/\delta)\,\sigma_y^2\left(\frac{k^*}{n} + \frac{n}{R_{k^*}(\Sigma)}\right).$$
>
> The first term is the **bias**, the second the **variance**. Bartlett notes a matching
> **lower bound**, under additional independence and symmetrization assumptions, showing you
> cannot improve the upper bound by more than a constant factor without excluding ordinary
> distributions — the Gaussian case among them.

Read only the variance term; it is where the phenomenon lives.

$$\frac{k^*}{n} + \frac{n}{R_{k^*}(\Sigma)}$$

Both pieces must be small. The first says the effective dimension must be **small compared
with the sample size**. The second says the tail effective rank must be **large compared
with the sample size**. The two are not in conflict — they are conditions on different parts
of the spectrum. You need a small number of important directions, and a very large number of
unimportant ones. That is what "overparameterization is essential" means quantitatively.

**Now the mechanism, and this is the anchor for part three.** Split the eigenbasis into a
head (the top k\* directions) and a tail. Split the data matrix correspondingly,
X = [X_H  X_T]. The Gram matrix is a sum:

$$XX^\top = X_H X_H^\top + X_T X_T^\top.$$

Suppose the tail is effectively isotropic, so that the n × n matrix of tail inner products
is close to a multiple of the identity:

$$X_T X_T^\top \approx \gamma I_n, \qquad \gamma \approx \sum_{i > k^*}\lambda_i .$$

Then the head component of the minimum-norm interpolator is

$$\hat\theta_H = X_H^\top\big(X_H X_H^\top + \gamma I\big)^{-1} y = \big(X_H^\top X_H + \gamma I\big)^{-1} X_H^\top y,$$

the second equality by the push-through identity. **That is ridge regression on the head,
with penalty γ.** Nobody wrote a penalty. The tail supplied it.

This is your Tikhonov regularization appearing for free, and it is worth naming as such: a
regularizer you did not add, generated by a large number of nearly equal, individually
negligible directions. The estimator behaves like ordinary least squares in k\* dimensions —
hence a k\*/n variance term, exactly the classical rate — while the bias behaves as if the
tail had simply been estimated as zero. And the noise? It goes into the tail coefficients,
which are the spiky component of §6.3: individually tiny, collectively able to absorb
arbitrary residuals, and orthogonal to everything that does the predicting.

That is "simple plus spiky", derived. The simple part is least squares in k\* dimensions. The
spiky part is the tail, and the price it charges is the n/R_{k\*} term — which is small
precisely when the tail is long and flat enough that no single unimportant direction can
distort the prediction.

The second effective rank R_{k\*} is doing the work of asking "is the tail *really* isotropic
enough for that approximation?" If the tail's mass concentrates on a few directions, R_{k\*}
is small, n/R_{k\*} is large, and the free ridge penalty becomes a distorting one instead.

### 6.7 What followed

Bartlett lists the follow-on work briefly: **ridge regression** across the full range of
explicit regularization parameters, which places the interpolator on a continuum rather than
treating it as a special case; **stochastic** gradient descent for linear and logistic
regression; and **early-stopped** gradient methods, another route to implicit
regularization — stop before you interpolate, and the stopping time sets the effective
penalty.

---

## 7. Do this by hand

Two exercises. The first is the mechanism of part one; the second is the mechanism of part
three. Between them they contain the two ideas most worth owning.

### 7.1 Why any step size works on the logistic loss (20 minutes, pen)

Take the one-dimensional per-example logistic loss ℓ(z) = ln(1 + e^{−z}), where z = y⟨w,x⟩ is
the margin.

1. Compute ℓ′(z) and ℓ″(z). Show ℓ″(z) = σ(z)(1 − σ(z)) where σ(z) = 1/(1+e^{−z}).
2. Show that for z ≥ 0, ℓ″(z) ≤ e^{−z}.
3. Show that for z ≥ 0, ℓ(z) ≥ (ln 2)·e^{−z}. *Hint: ln(1+u) ≥ u ln 2 for u ∈ [0,1].*
4. Conclude a bound on λ_max(∇²L(w)) in terms of L(w), for ‖xᵢ‖ ≤ 1 and all margins
   non-negative.
5. Now substitute into η < 2/λ_max. What condition on L(w) does it give? How does the
   threshold depend on η?

<details>
<summary>Solution</summary>

**1.** ℓ′(z) = −e^{−z}/(1+e^{−z}) = −(1 − σ(z)) = −σ(−z). Differentiating,
ℓ″(z) = σ(z)(1 − σ(z)) = σ′(z). It is positive, so ℓ is convex — as it must be.

**2.** σ(z)(1 − σ(z)) ≤ 1 − σ(z) = 1/(1 + e^{z}) ≤ e^{−z}.

**3.** ln(1+u) is concave with ln(1+0)=0 and ln(2) at u=1, so on [0,1] it lies above the
chord u·ln 2. Put u = e^{−z} ≤ 1 (valid since z ≥ 0): ℓ(z) = ln(1+e^{−z}) ≥ (ln 2)e^{−z}.

**4.** ∇²L(w) = (1/n)∑ᵢ ℓ″(zᵢ) xᵢxᵢᵀ. Since ‖xᵢ‖ ≤ 1, each xᵢxᵢᵀ has spectral norm ≤ 1, so

λ_max(∇²L) ≤ (1/n)∑ᵢ ℓ″(zᵢ) ≤ (1/n)∑ᵢ e^{−zᵢ} ≤ (1/(ln 2))·(1/n)∑ᵢ ℓ(zᵢ) = L(w)/ln 2.

**5.** The stability condition η < 2/λ_max is implied by η < 2 ln 2 / L(w), i.e.

$$L(w) < \frac{2\ln 2}{\eta}.$$

**The threshold scales as 1/η.** Which is the whole story. On a quadratic, λ_max is fixed and
a step size beyond 2/λ_max diverges forever. Here the curvature is *bounded by the loss*, so
as the loss falls the stability boundary moves toward you and any fixed η eventually becomes
stable. Larger η simply means a lower threshold and a longer wait — and the wait is the
edge-of-stability phase.

Compare the paper: the stable phase is entered once L(w_s) ≤ 1/η
([arXiv:2402.15926](https://arxiv.org/abs/2402.15926), Theorem 1). Same 1/η scaling, up to
the constant.

**What to notice.** The classical stability analysis assumes a fixed curvature bound. That
assumption is doing all the work, and it is false for this loss. Whenever a stability
argument rests on a global Lipschitz or curvature constant, ask whether the true constant
is *coupled to the quantity you are decreasing*. If it is, the classical conclusion may be
inverted.
</details>

### 7.2 The interpolator is a ridge estimator (15 minutes)

Let X = [X_H  X_T] be the n × d data matrix split into a head block (first k columns in the
eigenbasis) and a tail block. Assume d > n and XXᵀ is invertible.

1. Write the minimum-norm interpolator θ̂ = Xᵀ(XXᵀ)⁻¹y and split it into head and tail
   components.
2. Assume X_T X_Tᵀ = γI_n exactly. Write θ̂_H.
3. Use the push-through identity Aᵀ(AAᵀ + γI)⁻¹ = (AᵀA + γI)⁻¹Aᵀ to rewrite it. What
   estimator is it?
4. Where did the noise go?

<details>
<summary>Solution</summary>

**1.** θ̂_H = X_Hᵀ(XXᵀ)⁻¹y and θ̂_T = X_Tᵀ(XXᵀ)⁻¹y, with XXᵀ = X_HX_Hᵀ + X_TX_Tᵀ.

**2.** θ̂_H = X_Hᵀ(X_HX_Hᵀ + γI)⁻¹y.

**3.** By push-through, θ̂_H = (X_HᵀX_H + γI)⁻¹X_Hᵀy. **Ridge regression on the head block
with penalty γ.** Verify push-through directly if you have not before: multiply
Aᵀ(AAᵀ + γI) = (AᵀA + γI)Aᵀ — both sides equal AᵀAAᵀ + γAᵀ — then invert on each side.

**4.** Into θ̂_T. The tail has many directions, each with tiny variance, so tiny
coefficients spread over a great many of them can reproduce arbitrary residuals — including
pure label noise. Their contribution to a prediction ⟨θ̂, x⟩ on a fresh x is small precisely
because the tail eigenvalues are small. That is Bartlett's "spiky component": it is what
achieves interpolation, and it is invisible at prediction time.

**Now see the two conditions.** k\*/n small is exactly "the head is a classical
low-dimensional least-squares problem". n/R_{k\*} small is exactly "the tail really is
isotropic enough for step 2 to be a good approximation". Neither condition is about
regularization you chose. Both are properties of the covariance spectrum of your data.

γ ≈ ∑_{i>k\*} λ_i, the trace of the tail covariance. So the strength of the free
regularization is set by how much variance is hiding in the unimportant directions.
</details>

---

## 8. What is actually useful to you

### 8.1 The procedure selects the solution, not the objective

This is the transferable idea, and it is the one to carry out of the talk.

When your parameter space is rich enough that many configurations achieve your stated
objective, **the objective no longer determines what you get. The search procedure does.**
Gradient descent on logistic loss does not return an arbitrary separator; it returns the
maximum-margin one. Gradient flow from zero on squared error does not return an arbitrary
interpolator; it returns the minimum-norm one. Neither of those properties appears anywhere
in the loss function.

Your version: when many prompts, scaffolds, or tool sequences all pass your evaluation, the
evaluation has stopped being the specification. The thing that actually picks the winner is
your search — the order you try things in, where you started, when you stop. If you want a
particular kind of solution out of an underdetermined spec, you must either tighten the spec
or **deliberately choose a search procedure whose implicit bias points where you want**.
Bartlett's field spent a decade discovering that the second option was already operating,
unnoticed, and was the reason anything worked.

The practical diagnostic: for any system you build, ask *how many distinct configurations
would pass?* If the answer is "many", then go and identify what is actually breaking the tie.
It is never nothing.

### 8.2 Ask whether your stability constant is coupled to your progress

§7.1 is the whole lesson in one exercise: the classical step-size rule assumes a fixed
curvature bound, and for the logistic loss the curvature is bounded *by the loss itself*.

So the generalizable question is **whether the constant in your safety condition is
independent of the quantity you are driving down, or coupled to it.** If coupled, the
conservative rule derived from the worst case is strictly costing you — which applies to
retry budgets, timeouts, and any control loop whose "safe" parameter was fixed at the start
of the run.

### 8.3 Monotone improvement is a constraint you are paying for

Part one's Theorem 3 is flat: a constant-step-size gradient method that never lets the loss
increase cannot beat 1/t. Allowing it to increase gets you 1/T². And, as §4.7 notes, Wright's
plenary reached the same conclusion from a completely different direction with silver step
sizes.

For your work: any loop with a "reject the step if the score got worse" gate is implementing
the small step size. That gate feels like safety and is sometimes exactly that. But it is a
choice with a cost, and the cost is now provable in two settings. Where you can afford a
horizon-level acceptance criterion instead of a per-step one — accept a batch of ten
attempts if the batch improved, not each attempt — the theory says you should expect to do
better. See `optimization-theory-practice-wright.md` §10.2 for the same point made from the
step-size side.

### 8.4 Memorization is not automatically harmful — it depends on where it lives

Benign overfitting has a precise mechanism and it generalizes as a way of thinking. The
noise is absorbed by a very large number of directions that carry almost no variance, so it
is present in the fitted parameters and invisible in the predictions.

The condition for that to be safe is *quantitative*, and both halves matter: few important
directions (k\*/n small) **and** many unimportant ones, spread evenly (n/R_{k\*} small). If the
memorization lands in a few directions instead of many, it stops being benign.

The transfer: a system that memorizes specifics is not thereby broken. The question is
whether the memorized content sits in a subspace that influences the outputs you care about.
"It memorized the training examples" is not a finding. "It memorized them into the same
channel it predicts through" is.

### 8.5 The three-way decomposition is a working diagnostic

Approximation / optimization / statistics. When a learned or agentic system underperforms,
the failure is one of three things and they have different fixes. **Approximation:** nothing
in the reachable space of behaviours does the job — change the architecture, tools or
affordances. **Optimization:** a good configuration exists and your search does not find it —
change the search. **Statistics:** you found a configuration that scores well on your sample
and it does not transfer — change the evaluation, or how you select from it.

The value is that it forces "which one is this?" before "what should I change?".

### 8.6 The honest gap he leaves open

Two, and both are your regime. **Attention is not covered** (§5.5): the implicit-bias theory
is clean for fully-connected, convolutional and residual architectures and does not reach
the mechanism that defines the transformer. And **the i.i.d. assumption is gone with nothing
to replace it** — Bartlett names the break in the opening frame and does not return to it,
while every theorem in the talk still assumes an i.i.d. sample from a fixed distribution. If
you build on foundation models, none of this technically applies to your setting, and he
would be the first to say so.

---

## 9. Where to read next

1. **Bartlett, Montanari and Rakhlin, *Deep learning: a statistical viewpoint*.**
   [arXiv:2103.09177](https://arxiv.org/abs/2103.09177) — Acta Numerica 30 (2021) 87–201.
   The companion. His own survey, named from the podium. Parts two and three of the talk, at
   length. Not the ICM proceedings paper; nothing on part one.
2. **Wu, Bartlett, Telgarsky and Yu, *Large Stepsize Gradient Descent for Logistic Loss*.**
   [arXiv:2402.15926](https://arxiv.org/abs/2402.15926) — COLT 2024. Part one in full: the
   two phases, the 1/T² corollary, and the Ω(1/t) lower bound for monotone descent.
3. **Bartlett, Long, Lugosi and Tsigler, *Benign Overfitting in Linear Regression*.**
   [arXiv:1906.11300](https://arxiv.org/abs/1906.11300) — PNAS 117 (2020) 30063–30070. Part
   three, with the effective-rank characterization and the matching lower bound.

---

## 10. Self-test

<details>
<summary>1. Name the three questions in the classical decomposition, and the classical answer to each.</summary>

Approximation (use rich non-parametric classes), optimization (parameterize linearly, use a
convex loss, exploit convexity, use stable algorithms that discretize stable ODEs), and
statistics (explicitly control complexity via regularization, use uniform convergence over a
bounded-complexity set, assume i.i.d. data). Modern practice breaks all three: the
parameterization is non-convex, the step sizes are deliberately unstable, complexity control
is only implicit, the fit to noisy data is perfect so uniform convergence is unavailable, and
the data are not i.i.d. The talk repairs three of those breakages. It does not repair the
last one: every theorem in it still assumes an i.i.d. sample from a fixed distribution.
</details>

<details>
<summary>2. What is the classical stability condition for fixed-step-size gradient descent, and where does it come from?</summary>

η < 2/λ_max, where λ_max bounds the largest Hessian eigenvalue on the segment between
iterates. It comes from a second-order Taylor expansion: the decrease −η‖∇L‖² must beat the
curvature term η²λ_max‖∇L‖²/2. For a quadratic it is an if-and-only-if, and it is exactly the
absolute-stability limit of explicit Euler applied to gradient flow.
</details>

<details>
<summary>3. State the two-phase theorem for logistic regression with a fixed step size.</summary>

For separable data and **every** η > 0: the average loss over the first t iterates is
Õ(1/(γ²ηt)); the non-monotone phase ends within Õ(max{η,n}/γ²) steps; and once L ≤ 1/η the
loss decreases monotonically at Õ(1/(γ²η(t−s))). Wu, Bartlett, Telgarsky and Yu, COLT 2024.
</details>

<details>
<summary>4. Why does an arbitrarily large step size not diverge here, when it would on a quadratic?</summary>

Because the logistic loss is self-bounding: λ_max(∇²L(w)) ≤ L(w)/ln 2 when the data are
correctly classified and ‖xᵢ‖ ≤ 1. The curvature shrinks as the loss falls, so the stability
threshold L(w) < 2ln2/η is eventually met for any fixed η. On a quadratic the curvature is
constant and there is no such escape.
</details>

<details>
<summary>5. How do you get an accelerated 1/T² rate without momentum, and what does the lower bound say?</summary>

Given a budget of T steps, choose η = Θ(γ²T) — large enough that you spend roughly the first
half of the budget in the unstable phase and the second half decaying at 1/(ηt). The final
loss is O(ln²T / T²). The matching lower bound (Theorem 3 of the same paper) says any
constant-step-size gradient descent that maintains a monotone decrease has L(w_t) ≥ c₀/t. So
the instability is necessary, not incidental.
</details>

<details>
<summary>6. What does gradient descent on logistic loss converge to, in direction, on separable data — and why does that answer the generalization question?</summary>

The parameter norm diverges, but the direction converges to that of the maximum-margin
solution ŵ = argmin‖w‖ subject to yᵢ⟨w,xᵢ⟩ ≥ 1 (Soudry et al.). That matters because the
classical margin bound controls misclassification probability by roughly ‖ŵ‖²/n — with **no
dependence on the dimension d** — whereas the classical linear bound scales as d/n and is
vacuous when d ≫ n. So the optimizer supplies exactly the complexity control that nobody
wrote down.
</details>

<details>
<summary>7. Define near-M-homogeneity, and say what it fixes.</summary>

f is M-homogeneous if f(αθ) = α^M f(θ), equivalently (Euler) ⟨∇f(θ),θ⟩ = M f(θ). That is
brittle — adding bias terms to an L-layer ReLU network destroys it. Near-M-homogeneity
requires only |⟨h,θ⟩ − M f(θ,x)| ≤ p′(‖θ‖) for a polynomial p of degree ≤ M, so the defect
in Euler's identity may be nonzero but must grow at degree ≤ M−1. Homogenize by
f_H(θ,x) = lim_{r→∞} f(rθ,x)/r^M and the KKT result transfers. A calculus of near-homogeneous
functions lets you certify architectures layer by layer.
</details>

<details>
<summary>8. Which architecture is not covered, and why?</summary>

Attention. Bartlett's stated reason: the squashing function used there is nearly
zero-homogeneous, and M = 0 is degenerate in the framework — the bounding polynomial p′ has
degree −1 and the homogenization divides by r⁰. He calls it "an interesting gap". So the
theory covers essentially every component of deep learning except the one that defines the
transformer.
</details>

<details>
<summary>9. Define the two effective ranks and the effective dimension k*, and state the variance condition for benign overfitting.</summary>

r_k(Σ) = (∑_{i>k}λᵢ)/λ_{k+1}, the tail's one-norm over its infinity-norm. R_k(Σ) =
(∑_{i>k}λᵢ)²/∑_{i>k}λᵢ², the one-norm squared over the two-norm squared. k\* = min{k :
r_k(Σ) ≥ bn}. The variance term of the excess risk is proportional to k\*/n + n/R_{k\*}(Σ),
so you need the effective dimension small compared with n **and** the tail effective rank
large compared with n — few important directions, many unimportant ones.
</details>

<details>
<summary>10. Why is the minimum-norm interpolator secretly a ridge estimator?</summary>

Split the eigenbasis, X = [X_H X_T], so XXᵀ = X_HX_Hᵀ + X_TX_Tᵀ. If the tail is effectively
isotropic, X_TX_Tᵀ ≈ γI with γ ≈ ∑_{i>k\*}λᵢ, and push-through gives
θ̂_H = X_Hᵀ(X_HX_Hᵀ + γI)⁻¹y = (X_HᵀX_H + γI)⁻¹X_Hᵀy — ridge on the head with a penalty the
tail supplied. Head = the simple component that predicts; tail = the spiky component that
absorbs the noise and contributes negligibly to predictions.
</details>

---

## 11. Note on the tutorial process

**Length.** This runs longer than the two earlier tutorials in `summaries/`. The talk carries
three independent results with three different anchors and three different source papers,
rather than one thesis with supporting evidence, so the walkthrough (§§4–6) is three
walkthroughs. I compressed the optimization background to one page and trimmed the framing
sections rather than cut any of the three.

**Difficulty against reputation.** Bartlett's reputation is statistical learning theory, and
that is exactly what the talk was — no inversion of the Kontorovich kind. But the *shape* of
the difficulty was not what the field label predicts. Every mathematical object in the talk
is standard applied mathematics: Taylor's theorem, explicit-Euler stability, Euler's
homogeneous-function theorem, KKT conditions, spectral decomposition, the pseudoinverse, the
push-through identity, ridge regression. What is unfamiliar is the *statistical framing* —
excess risk, uniform convergence, complexity control, margin bounds. So I rated it 2/5 on the
mathematics and 3/5 on the frame, and split the document accordingly: a one-page calibration
section for the optimization background (§2), a real bridge for the statistics (§3).

**No proceedings paper.** I searched arXiv and the SIAM ICM 2026 proceedings listings and
found nothing matching this lecture under Bartlett's name. Per the spec I fell back to his
most recent survey **on this specific topic** — the Acta Numerica review, which he names from
the podium — and labelled it a companion in both the front matter and the header. The four
research papers cited inline are primary literature for individual theorems, not companions,
and I have kept that distinction visible throughout. Where I quote a rate or a definition
from one of them, I name it in the sentence.

**Name corrections.** The auto-captions destroy every proper noun in this talk, and also the
Greek.

| Caption | Correct |
|---|---|
| eater | η (eta), the step size |
| oil (discovered this equivalence) | Euler |
| kushka points | KKT (Karush–Kuhn–Tucker) points |
| om minimality | o-minimality |
| sudri at al | Soudry et al. |
| gian tasks / G and Taskski | Ji and Telgarsky |
| Estherovv | Nesterov |
| Francis Bark | Francis Bach |
| Jingfong | Jingfeng Wu |
| Yuang | Yuhang Cai |
| Matus | Matus Telgarsky |
| Michael, Song, Bin | Michael Lindsey, Song Mei, Bin Yu |
| Sham (from Harvard) | Sham Kakade |
| Kungji (from Columbia) | Kangjie Zhou |
| Nadri | Niladri Chatterji |
| Spencer, Gal | Spencer Frei, Gal Vardi |
| Nati (at TTI Chicago) | Nathan Srebro |
| Sasha (at MIT) | Alexander Rakhlin |
| Gaba Lugosi at Pompeo Fabra | Gábor Lugosi at Pompeu Fabra |
| Alex (PhD student) | Alexander Tsigler |
| Phil Long at Google | Philip M. Long |
| act in numeric America paper | Acta Numerica paper |
| banana overfitting | benign overfitting |
| hessen, igen value | Hessian, eigenvalue |
| coariance, coariants | covariance, covariates |
| mclassification | misclassification |
| aphine | affine |
| Hbert space | Hilbert space |
| polomial | polynomial |
| asmtoic | asymptotic |
| peacewise | piecewise |

**Substantive caption error, corrected in the text.** The captions render the convergence
rate as "one over e to t", which reads as an exponential 1/e^t. The actual rate is
**1/(ηt)** — "one over eta t" — a *polynomial* rate, and the entire point of §4 is the
interplay between η and t in that expression. Reading it as an exponential would make the
talk incoherent: there would be no trade-off to optimize and no reason to care about the step
size. Corrected throughout §4.

**Reconstructed, and labelled where it appears.** The self-bounding derivation in §4.4 and
§7.1 — λ_max(∇²L) ≤ L(w)/ln 2, giving a stability threshold that scales as 1/η — is mine. The
captions carry no formula for it; Bartlett states only that "once the loss gets sufficiently
small then we're in the stable phase." My derivation reproduces the paper's threshold
(L(w_s) ≤ 1/η, Theorem 1 of arXiv:2402.15926) up to the constant, and rests only on standard
logistic-loss identities you can check in fifteen minutes. What would verify it exactly: the
corresponding lemma in that paper.

**Names I could not verify — not guessed.** Two:

- **"Jason from Berkeley"**, named as a new collaborator in part two. The author list of the
  near-homogeneity paper (arXiv:2502.16075) is Cai, Zhou, Wu, Mei, Lindsey, Bartlett, Kakade,
  Yu — no Jason. The other two names in the same sentence, Sham Kakade and Kangjie Zhou,
  match that paper exactly, so the reference is almost certainly to it and "Jason" is a
  caption corruption of one of the Berkeley authors. I have not guessed which.
- **"Louis"**, named as a postdoc collaborator in part three alongside Spencer Frei and Gal
  Vardi. I could not resolve it against any Bartlett co-authorship and have omitted it.

**Gaps, and how bad they are.** Three, all marked in place, and none of them structural:

1. **The margin bound's exact form** (§3.3). The captions carry only "the ratio between the
   norm squared of the solution and the sample size". The constants and logarithmic factors
   were on the slide. The shape — dimension-free, controlled by ‖ŵ‖²/n — is what carries the
   argument, and that is stated. Low impact.
2. **The two textbook quotations** on his bookshelf slide (§6.2). Not spoken. Purely
   rhetorical. No impact.
3. **The mechanism of the attention failure** (§5.5). He gives one sentence — the squashing
   function is nearly zero-homogeneous and M = 0 is problematic — and moves on. I extended it
   only as far as the definition itself licenses (p′ of a degree-0 polynomial; division by
   r⁰) and marked the rest as absent. Moderate impact, because this is the most consequential
   caveat in the talk.

Beyond those, the mathematics is unusually well recovered for a caption-only source, because
all three results are published and I could restore each rate, threshold and definition from
its own paper rather than reconstructing it.
