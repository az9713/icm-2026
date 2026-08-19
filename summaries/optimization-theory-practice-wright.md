---
title: "Optimization in Theory and Practice"
speaker: Stephen J. Wright (University of Wisconsin–Madison)
source: https://www.youtube.com/watch?v=Ep1TzZDOHnU
video_id: Ep1TzZDOHnU
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2510.15734
transcript: ../transcripts/Ep1TzZDOHnU_transcript.txt
difficulty_for_you: 1/5 (frame) — 3/5 (the post-2015 frontier)
reading_time: ~50 min
---

# Optimization in Theory and Practice — Stephen J. Wright

**Field:** continuous optimization. Linear programming, and unconstrained minimization
of smooth functions.

**Difficulty against your background: inverted.** You already own the frame. So this
tutorial does not teach you gradient descent, convexity, condition number, or the
simplex method. It spends its length on **what has changed since your training** — most
of it since 2015, some of it since last year.

**Sources.** The talk and the paper
([arXiv:2510.15734](https://arxiv.org/abs/2510.15734), Wright, submitted 17 October
2025, revised 2 December 2025, ICM 2026 proceedings) cover the same ground. The paper's
sections are: Introduction, Formulations and Optimality Conditions, Convergence and
Complexity, Linear Programming, Unconstrained Optimization, Discussion. Where I quote a
number that appears only in the talk I say so.

**Names.** The auto-captions mangle almost every proper noun in this talk. I verified
each one and give the correct spelling. Where I could not verify, I say so.

---

## 1. The thesis

Wright's claim is a single sentence, and the whole hour is evidence for it:

> Theory and practice in optimization **continually drive each other**. Practical
> experience inspires new questions in complexity theory; theoretical insight inspires
> new algorithms and new techniques inside algorithms.

He is careful to say the loop runs badly in both directions too. There are algorithms
that are excellent in practice with no theory explaining why. There are algorithms with
better worst-case bounds than their rivals that behave badly in practice and nobody uses.

He closes on Roger Fletcher's preface to *Practical Methods of Optimization* (1980s),
which he and Jorge Nocedal also quoted in the foreword to *Numerical Optimization*:

> "Optimization is a fascinating blend of theory and computation, heuristics and rigor."

His verdict forty years later: still true. **Practice does not wait for theory.** Theory
certifies practice after the fact, and occasionally illuminates a technique that turns
out to matter.

---

## 2. Calibration: what you can skip

You know all of this. It is here so you can confirm we are using the same words, then
move to §3.

**Two problem classes.**

*Linear programming:* minimize cᵀx over {Ax = b, x ≥ 0}, with A an m×n matrix. May be
infeasible or unbounded. If a solution exists, at least one is a vertex of the polytope.

*Smooth unconstrained minimization:* minimize f(x) over x ∈ ℝⁿ, with ∇f Lipschitz
(constant L).

**The complexity convention.** Cost is counted in **oracle calls**, not flops. An oracle
returns one unit of information about f — a function value, a gradient, an unbiased
gradient estimate. This is the Nemirovski–Yudin model (Russian edition 1979). Yurii
Nesterov gave the Gauss lecture at this congress on the same framework.

**Two ways to say the same thing.** Track a quantity t_k (either f(x_k) − f\* or
‖∇f(x_k)‖). Either state the decay rate, t_k ≤ C/√k, or invert it and state the
iteration count, k ≥ C²ε⁻². Wright uses both.

**Baseline gradient descent**, x_{k+1} = x_k − (1/L)∇f(x_k):

| f is | measure | iterations to ε |
|---|---|---|
| smooth, non-convex | ‖∇f‖ ≤ ε | O(ε⁻²) |
| convex | f − f\* ≤ ε | O(ε⁻¹) |
| strongly convex | f − f\* ≤ ε | O(κ log(1/ε)) |

κ is the ratio of upper to lower bounds on the curvature — the condition number of the
Hessian. Wright: "I could prove each of these results to you in about half a slide."

That is the whole prerequisite. Everything below is the part that is new.

---

## 3. Linear programming: three eras, and where the frontier is now

### 3.1 Simplex — 80 years, and the theory still does not explain it

George Dantzig, 1940s. Walk vertex to vertex along edges, always downhill in cᵀx. The
choice of which adjacent vertex to move to is the **pivot rule**, and it is where all the
variants live.

The empirical fact: simplex needs a **modest multiple of n** iterations — 2n or 3n is
typically enough.

The theoretical fact, known since the early 1970s: there exist linear programs requiring
**exponentially many** pivots. Not polynomial. Exponential.

And after fifty years of searching, **no provably polynomial pivot rule is known.**

Wright's point about that failure is the first instance of his thesis, and it is not the
obvious one. The search failed at its stated goal and succeeded at another: hunting for
provably good pivot rules produced a stream of better heuristics, and the commercial
software kept improving. *The search for theory improved practice even though the theory
never arrived.*

### 3.2 Why simplex works: smoothed analysis, and the 2025 improvements

**First attempt — Karl-Heinz Borgwardt, 1980s.** Assume the LP data is drawn from a
probability distribution. Then the expected number of simplex iterations is polynomial.

The objection, which Wright states from experience: **random LPs look nothing like real
LPs.** So the result explains little about practice.

**The breakthrough — Daniel Spielman and Shang-Hua Teng, 2004: smoothed analysis.** A
genuinely different move. You bring *your* LP — your A, b, c. They are allowed to add
small Gaussian perturbations of variance σ² to the entries. Then they prove the expected
number of pivots is polynomial in the dimension **and in 1/σ**.

This is the interesting hybrid: not worst case, not average case over a fake
distribution, but worst case *followed by a small random smear*.

**What is new (this is the part that postdates most textbooks).** Eleon Bach and Sophie
Huiberts and collaborators have sharply improved the σ dependence. In the talk Wright
puts it as reducing the polynomial dependence on 1/σ from **about 30 to about 1.5**. The
current published result is an upper bound of

> O(σ^{−1/2} · d^{11/4} · log(n)^{7/4}) pivot steps

improving the previous strongest bound of O(σ^{−3/2} · d^{13/4} · log(n)^{7/4}) due to
Huiberts, Lee and Zhang — with a matching high-probability lower bound, so the noise
dependence is **optimal among simplex methods** up to polylogarithmic factors
([arXiv:2504.04197](https://arxiv.org/abs/2504.04197)).

**And then the result Wright calls enormously significant.** Roughly nine months before
the talk, the same group showed you can get polynomial expected behaviour by perturbing
**only b and c — leaving A alone**
([arXiv:2510.21613](https://arxiv.org/abs/2510.21613), "Beyond Smoothed Analysis:
Analyzing the Simplex Method by the Book").

Why that matters is a practitioner's reason, not a theorist's. In real LPs **A is
extremely sparse** — it usually has a network adjacency matrix buried in it. Classical
smoothed analysis requires you to replace every structural zero in A with a little
Gaussian. That destroys exactly the structure the whole solver is built to exploit. The
new analysis leaves A intact, so the theorem finally applies to the object people
actually solve.

*Read that as a general lesson: a theorem whose hypotheses destroy your problem's
structure is not a theorem about your problem.*

### 3.3 Provably polynomial: ellipsoid, Karmarkar, interior point

**Leonid Khachiyan, 1979.** Took the ellipsoid method — already known for general
constrained optimization, from Yudin and Nemirovskii — and showed that applied to an LP
it runs in polynomial time. A genuine breakthrough; several prizes.

And useless in practice. When implemented it **essentially always attains its worst-case
bound**, and is far slower than simplex. A clean instance of Wright's reverse failure
mode: good theory, bad practice.

**Narendra Karmarkar, 1984, AT&T.** The projective algorithm. Polynomial *and*, he
claimed, practically good. It reached the *New York Times* and *Time*.

Wright's assessment: the practical performance was not actually that great. But the
excitement it generated caused the field to find, very quickly, methods inspired by it
that genuinely had both — **primal–dual interior point methods**.

**How primal–dual IPMs work,** because the mechanism is worth having exactly.

The optimality certificate for an LP is a set of linear (in)equalities. Find x, λ ∈ ℝᵐ,
s ∈ ℝⁿ with

- Ax = b  (primal feasibility)
- Aᵀλ + s = c  (dual feasibility)
- x ≥ 0, s ≥ 0
- xᵢsᵢ = 0 for every i  (**complementarity**)

Now **relax the last condition**: replace 0 with a parameter μ > 0, so xᵢsᵢ = μ. As μ
ranges over the positive reals, the solutions trace out the **central path** through the
interior of the polytope.

The algorithm follows that path. Fix μ. Apply two or three steps of Newton's method to
the nonlinear system {Ax = b, Aᵀλ + s = c, xᵢsᵢ = μ}, curtailing each step so x and s
stay positive. Decrease μ. Repeat.

Wright notes with evident satisfaction that this is polynomial **and** the analysis is
elementary — an end-to-end complexity result you can teach in one or two lectures of a
graduate course.

**Classical complexity: O(n^{3.5}).** That is O(√n) iterations, each requiring you to
form and solve an n×n linear system at O(n³).

### 3.4 The current frontier: chasing the matrix-multiplication exponent

Seven or eight years ago the theoretical computer science community asked whether n^{3.5}
could be beaten. It could.

The picture Wright shows (credited to **Yin-Tat Lee**, now at OpenAI) plots year against
the exponent on n. Two curves:

- **Blue: the exponent ω for multiplying two n×n matrices.** Classically 3. Reduced
  since the 1960s; currently **ω ≈ 2.371339**. It is believed it may one day reach 2.
- **Red: the exponent for interior point methods on LP.** Falling toward the blue curve.

The punchline: **if ω were 2, there is an interior point method running in
O(n^{2 + 1/18}).**

Sit with that. The cost of *solving a linear program* of dimension n has been driven to
within a positive constant, in the exponent, of the cost of *multiplying two matrices* of
the same size.

**What the new IPMs do differently:**

- Compute Newton steps only **approximately**.
- Exploit the fact that consecutive Newton systems are nearly identical — apply **low-rank
  updates** rather than re-solving.
- Use **weighted central paths**.
- Some work only for special LP classes, such as max-flow on networks.

And the detail Wright singles out as fascinating: these methods pay careful attention to
the **memory hierarchy** and to **updating matrix factorizations**. Those were regarded as
grungy scientific-computing concerns for three or four decades. They are now essential
components of methods advancing the *theoretical* frontier of linear programming.

**Honest caveat, which he gives:** these methods are **not yet practical**. The constants
hidden in the O(·) are large. What they have changed is the mathematical frontier.

### 3.5 First-order LP: the one that actually shipped

The newest practically important class, and it comes from a different direction.

Reformulate the LP as a **min–max saddle problem**:

$$\min_{x \ge 0}\ \max_{\lambda}\ c^\top x + \lambda^\top (b - Ax)$$

The reasoning, which is worth doing once. Hold x fixed and maximize over λ. If Ax ≠ b you
can drive the bilinear term to +∞ by sending λ in the right direction. So the inner max is
finite **only if Ax = b**, and in that case it collapses to cᵀx. Now minimize over x ≥ 0
and you have recovered the original LP exactly.

The workhorse method is **PDHG** (primal–dual hybrid gradient): alternate a gradient step
in x with a gradient step in λ, with momentum built into the λ step. Production
implementations add heavy preconditioning to improve conditioning, plus restarting and
other tricks.

**Why it won, and it is purely an architecture argument.** The only work per iteration is
a multiplication by A and by Aᵀ.

1. If A is sparse — and it is — that multiplication is cheap.
2. Those multiplications run **extremely efficiently on GPUs**.

So despite needing many more iterations, these methods entered commercial LP packages
very quickly and are **competitive with simplex and interior point on very large
problems**.

And here, unusually, **theory tracks practice well.** The convergence theory is based on
the **Hoffman constant** for a certain formulation of the LP optimality conditions, and it
does a decent job of predicting the iteration count you actually observe.

---

## 4. Smooth minimization: what changed after the textbook

### 4.1 Silver step sizes — the same direction, better steps

The question: can you beat the baseline rates in §2 while still moving in the **negative
gradient direction every iteration**, changing only the step lengths α_k?

Answer, and it is recent: **yes**. Jason Altschuler and Pablo Parrilo, **silver step
sizes**. (The transcript renders the second name as "and pillo"; Parrilo is the
reconstruction, consistent with the published work.)

The idea is a change of objective, and it is the transferable part. Standard step-size
rules ask for the **best decrease in f over a single iteration**. Altschuler and Parrilo
argue that is the wrong question. Ask instead: over a horizon of 10 or 100 iterations,
what *sequence* of α_k gives the best possible improvement?

You get a completely different answer. The schedule is **non-uniform**, and increasingly
so as the conditioning worsens. Occasionally — in Wright's example with condition number
64, roughly every 8th or 16th step — you take a step **much longer than all the others**.

That long step **may go uphill**. Monotone decrease is given up. Over the full horizon you
obtain the provably better reduction.

The gain, strongly convex case:

> O(κ log(1/ε))  →  O(κ^{0.786} log(1/ε))

**Why this is worth your attention beyond the constant.** The whole of classical
line-search theory is built on enforcing decrease at every iteration. This result says
that constraint was costing you, and that the greedy per-step objective was never the
right one.

### 4.2 Nesterov's momentum, and why silver does not beat it

Nesterov, 1983. Take the search direction as a combination of the current negative
gradient and an extrapolation along the direction you just moved.

That much was known for **quadratic** f since the 1950s. What was not proved was that it
helps for general convex f. Nesterov's trick was small and decisive: **evaluate the
gradient at the extrapolated point**, not at x_k. With that, for convex f:

> O(ε^{−1/2})  — versus O(ε⁻¹) for plain gradient descent

Note the ordering Wright draws out: momentum beats silver step sizes, because **silver
uses no momentum**. Two independent levers; momentum is the stronger one.

### 4.3 PEP: designing algorithms by solving an optimization problem

This is the most transferable idea in the talk, and it has been building since about 2010.

**PEP — the Performance Estimation Problem.** (Wright says "protocol" from the podium;
the established term is Problem.)

Fix a horizon T, a class of functions, and a class of algorithms. Then:

- **Inner maximization.** Given a specific algorithm — say, fixed step lengths α and
  momentum β — what is the *worst* function in the class, the one giving the least
  improvement over T iterations?
- **Outer minimization.** Now choose the algorithm's parameters to make that worst case
  as small as possible.

So you solve a **min–max problem to design the algorithm.**

The obvious objection is that you cannot maximize over an infinite-dimensional class of
functions. The resolution is the clever part: **parameterize f by the iterates x_k and
the gradient values g_k.** That turns the inner problem into a finite matrix optimization
problem. Once you have found optimal g_k and x_k, you **interpolate** to recover an actual
function f in the class.

Result: a tractable finite problem whose solution *is* a new optimization method with a
proven worst-case guarantee.

Wright notes that this framework plugs naturally into AI-assisted workflows. At **ICML, a
couple of weeks before this talk**, a workflow was presented that wraps around PEP: you
describe your function class and which variant of gradient method you want, and it finds
the optimal step lengths.

**The reframe worth taking:** algorithm design stops being invention-then-analysis and
becomes a solvable optimization problem in its own right.

### 4.4 Lower bounds, and the one construction to remember

An upper bound alone never tells you a method is good. You need the matching lower bound.

A lower bound statement has this shape: *there is a problem in the problem class for which
**every** algorithm in the algorithm class needs at least N(ε) oracle calls.*

Wright gives the structural insight that unifies these constructions:

> Worst-case functions are functions where the algorithm learns information about f only
> **gradually**, in a systematic way. Most of the information is hidden and revealed one
> piece at a time.

**The canonical construction** — the one proving Nesterov's method optimal. Take f
quadratic, with a **positive-definite tridiagonal Hessian**, plus a linear term whose
coefficient vector is e₁. The solution x\* has all components nonzero. But start a gradient
method at the zero vector, and the tridiagonal structure means successive iterates **fill
in one component at a time**: x₁ has only its first component nonzero, x₂ its first two,
and x_k its first k. (The transcript says "last n−k components nonzero"; that is a caption
slip — those components are **zero**, which is exactly what makes the argument work.)

So you can lower bound ‖x_k − x\*‖ by the norm of the last n−k components of x\* alone,
since the corresponding components of x_k are still zero. For any method whose iterates
lie in the span of the gradients seen so far, this yields

> f(x_k) − f\* ≥ c / k²

Nesterov's accelerated gradient achieves an upper bound of C/k². **They match to within a
constant.** Nesterov's method is therefore **optimal** for smooth convex minimization among
gradient methods whose iterates lie in the span of observed gradients.

This argument has been extended to parallel and randomized algorithms, coordinate descent,
and higher-order methods.

---

## 5. Optimization for machine learning: where theory is losing

### 5.1 The finite-sum problem and SGD

$$f(x) = \frac{1}{N}\sum_{j=1}^{N} f_j(x)$$

N can be in the **billions**. x is the model weights — arcs of a network, or the matrices
in a transformer. f_j measures how badly the model fits training item j; zero if the
prediction matches the label.

Computing one full gradient means back-propagating over the entire dataset. Prohibitive.

So: pick one term j_k at random, and use ∇f_{j_k}(x_k) as a proxy for ∇f(x_k). It is an
**unbiased** estimate with **enormous variance** — it typically looks nothing like the true
gradient. Step in its negative direction.

**Robbins and Monro, 1951.** Wright's note: one of those ideas that lay forgotten for
forty or fifty years before turning out to be indispensable.

Theory exists: for convex f, expected optimality gap below ε in O(ε⁻²) iterations, with
analogous bounds for strongly convex and non-convex. Expected, because the algorithm is
random.

### 5.2 Adam, and the honest admission

Practice adds batching (10³ to 10⁶ terms, not one), momentum, adaptive scaling, step-size
and warm-up schedules, layer normalization, and much more. Armies of people at technology
companies work on it.

**Adam** (2015) is used overwhelmingly. It applies an **adaptive diagonal scaling** to the
update direction g_k — it tracks previous g_k values, effectively learns how the variables
are scaled, and weights each component accordingly. Also called preconditioning.

Wright: look it up on Google Scholar and it has **over a quarter of a million citations**.

Then the admission, stated plainly:

> There are variants of Adam with provable convergence, but the rates are **generally not
> much better than SGD**. You can identify a few special problem classes where Adam is
> provably better. In general it is not provably faster. It is used because in practice it
> is a lot better.

### 5.3 Muon, and the matrix sign

Proposed in a **blog post at the end of 2024**. Competitive with, and on some datasets
better than, Adam.

The mechanism, which is genuinely interesting:

1. **Reshape** the weights from a long vector into a **matrix**. Natural for transformers
   and neural nets, where the unknowns already aggregate that way. The gradient is then
   also a matrix.
2. Form a stochastic estimate of that matrix gradient, combined across iterations with
   momentum. Call it B_k.
3. **Take the SVD:** B_k = U Σ Vᵀ.
4. **Throw away Σ.** Use **U Vᵀ** as the search direction.

Step 4 is the **matrix sign** function. Discarding the singular values sounds mad. The
justification: it is a **trust region method whose radius is defined in the spectral
matrix norm**. Under that geometry, U Vᵀ is the right step.

The practical objection is obvious — X may have trillions of entries and the SVD is
impossible. The answer: an **iterative approximation**, good enough, and it runs on GPUs.

Theory is already appearing. Wright refers to a talk given a few days earlier at the same
congress by **Weijie Su** *(reconstructed — the captions render this as "way Sue")*.

### 5.4 The verdict

> "In modern machine learning, the theory is running far behind the practice. The practice
> is throwing up very interesting issues faster than the theory can address them."

And the sociological observation: the algorithms used in ML over the last fifteen years
have **overwhelmingly come from practitioners**, not theorists.

His statement of the open problem: *what is the right theory for large-scale training of
neural networks — for stochastic-gradient-based methods minimizing non-convex, non-smooth
functions?*

---

## 6. Benign non-convexity

### 6.1 From hopeless to local

**Nemirovski and Yudin** (Russian edition 1979) essentially threw up their hands: for a
non-convex f, even a smooth one, finding the **global** minimum costs work exponential in
the dimension. Hopeless.

**Nesterov and Polyak, 2006**, changed the target. Do not ask for the global minimum. Ask
for an **ε-approximate local minimum**:

- ‖∇f(x)‖ ≤ ε
- λ_min(∇²f(x)) ≥ −ε

With that target, complexity is **polynomial in 1/ε**. Their method is **cubic
regularization** — which had actually been proposed by **Andreas Griewank** in the 1980s,
not for complexity reasons but because it worked well in practice, which it does.

That 2006 paper spawned an industry: take a method known to work well, add small
enhancements, and equip it with a complexity theory. Wright says he worked on this
extensively.

**But the bound is still pessimistic.** At ε = 10⁻⁶ you are talking about thousands of
iterations, and practical methods routinely converge far faster.

### 6.2 The phenomenon

Problems that are **bona fide non-convex** and yet on which your favourite method reliably
converges to a **global** minimizer.

Observed first and most clearly in **low-rank matrix optimization**: the unknown is a
matrix that is low rank at the solution, which you parameterize in a way that makes the
formulation non-convex — and gradient descent finds the global solution anyway.

Then found elsewhere: **AC power flow** in electrical grids, and **phase retrieval**.

### 6.3 The taxonomy — there is no single reason

Wright is explicit that this is a *family* of unrelated mechanisms, not one theorem:

1. **All local minima are global.** Every local minimum has the same function value. Find
   one, you are done. (Common in the matrix problems.)
2. **Strict saddles.** At every saddle point — gradient zero, not a minimizer — the Hessian
   has a **strictly negative** eigenvalue. That eigenvector is an escape direction, so the
   saddle cannot trap you.
3. **The Polyak–Łojasiewicz (PL) condition.** As you move away from the minimizing set,
   the gradient grows reasonably fast. Consequence: a gradient step is guaranteed to be
   **big enough** to make real progress toward the set.

Leveraging any of these gives much tighter complexity bounds than the generic theory.

### 6.4 Overparameterized networks

Enough weights to fit the training data **exactly** — the current regime, with trillions of
weights.

The loss surface, from contour plots projected to three dimensions, is genuinely nasty:
non-smooth, ridges, local minima everywhere.

And yet run SGD long enough and it frequently reaches **zero loss**. Moreover the solution
found — typically one point on a whole manifold of solutions, in fact **disconnected**
manifolds — tends to **predict well on unseen data**.

Explanations Wright cites:

- **Double descent.** Keep iterating past the point of fitting the data and SGD moves to a
  different solution with better prediction properties.
- **Implicit bias / implicit regularization.** The optimization method does not find *any*
  solution; it is biased toward ones that generalize. (Peter Bartlett's plenary the
  previous day.)
- **Neural tangent kernel.** Make a convolutional network's layers wide enough and it
  starts behaving like a **kernel method** — and kernel method performance is well
  understood. **Weinan E** gave a plenary at the previous ICM on exactly this.
- **Mean-field analysis and PDE.** Wright cites **Chizat and Bach**, and **Weinan E** and
  collaborators. He has worked in this area.
- **Very recent:** SGD iterates bounce between local minima but are **attracted to the ones
  with lower function values**. The author defended his thesis a few weeks before the talk.

### 6.5 The methods with no matching theory

Worth stating flatly, because it is a list of things you probably use:

**Newton's method. Quasi-Newton. Limited-memory quasi-Newton (L-BFGS). Nonlinear conjugate
gradient.**

All used successfully and broadly. And for **every one of them** there exist worst-case
functions on which they are **as slow as plain gradient descent**. Excellent practice,
mediocre worst-case theory. Recent work has narrowed the function classes and added
enhancements to close some of the gap, but the gap remains.

---

## 7. AI as a collaborator in optimization theory

Wright's argument for why optimization is unusually well matched to AI assistance:

1. The questions are **very precise**.
2. The techniques are **very technical** — papers carry 40- or 50-page appendices.
3. But those techniques are **used over and over again**.

Precise, technical, repetitive. That should be a good fit, and he reports that it is.

**Results from the last year:**

- **Ernest Ryu** (now at OpenAI): the classical convergence result for Nesterov's
  accelerated gradient is stated for the **average of all iterates seen so far**. It is now
  shown that the **last iterate** converges to the minimizer — a far more natural
  statement. Proved with the help of **GPT Pro**.
- **Ryu and collaborators**, using **ChatGPT**: for **Nesterov flow**, the continuum limit
  of the method, the trajectory converges to a minimizer — but the **path length can be
  infinite**. It may spiral a great deal before arriving.
- **About a month before the talk**: sharp first-order **lower bounds** for f at different
  levels of smoothness. The ε⁻¹ ᐟ ² bound under Lipschitz gradient was known; going higher —
  Lipschitz Hessian, Lipschitz third derivatives — gives different lower bounds, now
  verified using AI. *(The author's name is unrecoverable from the captions; I have not
  guessed it.)*
- The **AI-assisted PEP workflow** from §4.3, for designing optimal gradient methods.

**The pattern worth extracting.** Look at where AI succeeded: **lower bounds**. Wright says
so directly — constructing lower-bound functions is essentially constructing
**counterexamples**, and that is what these systems turn out to be good at.

That is a sharper claim than "AI helps with math." It says: point the model at *find the
adversarial instance*, not at *prove my theorem*.

---

## 8. The open challenges he names

1. **The theory–practice gap in machine learning.** The largest one.
2. **New models of complexity.** The oracle model and the flop model are both blind to the
   machine. Wright suggests models that account for the **memory hierarchy, parallelism,
   and GPUs**. People have begun this. *(Note how this rhymes with §3.4 — those same
   concerns are already load-bearing in cutting-edge LP theory.)*
3. **Better theory for successful non-convex algorithms.**
4. **AI as a collaborator.**

---

## 9. Do this by hand

### 9.1 Derive the min–max LP reformulation (10 minutes)

From §3.5, verify for yourself that

$$\min_{x \ge 0}\ \max_{\lambda}\ c^\top x + \lambda^\top(b - Ax)$$

is exactly the original LP.

<details>
<summary>Check</summary>

Fix x. If Ax ≠ b, then b − Ax ≠ 0, so choosing λ = t(b − Ax) gives an inner objective of
cᵀx + t‖b − Ax‖², which → +∞ as t → ∞. So the inner max is +∞ unless Ax = b.

If Ax = b, the λ term vanishes identically and the inner max is cᵀx.

So the outer minimization sees +∞ on infeasible x and cᵀx on feasible x. It therefore
minimizes cᵀx over {Ax = b, x ≥ 0}. ∎

Now notice what the reformulation bought: the only appearance of A is in the products Ax
and Aᵀλ. That is the entire reason first-order LP solvers run on GPUs.
</details>

### 9.2 The tridiagonal lower bound (20 minutes, pen)

Take f(x) = ½xᵀTx − e₁ᵀx with T the n×n tridiagonal matrix having 2 on the diagonal and −1
on the off-diagonals. Start at x₀ = 0.

Compute ∇f(x) = Tx − e₁. Now check by hand: what is ∇f(x₀)? Which components are nonzero?
Take one gradient step and compute ∇f(x₁). Which components are nonzero now?

<details>
<summary>What you should find, and why it matters</summary>

∇f(0) = −e₁, nonzero in component 1 only. So x₁ is a multiple of e₁.

Then Tx₁ is nonzero in components 1 and 2 (the tridiagonal band spreads support by exactly
one position per multiplication). So ∇f(x₁) has support {1,2}, and x₂ has support {1,2}.

By induction, **x_k has support contained in the first k components**, for *any* method
whose iterates lie in the span of the gradients observed so far.

The solution x\* has **all** components nonzero. So ‖x_k − x\*‖² is bounded below by the sum
of squares of the last n − k components of x\* — a quantity the algorithm has not been able
to touch. Turning that into a bound on f(x_k) − f\* gives the c/k² lower bound.

The mechanism to remember: the **band structure of the Hessian rations out information at
one component per iteration**. This is the "information revealed gradually" principle of
§4.4 made completely concrete.
</details>

---

## 10. What is actually useful to you

### 10.1 PEP — turn tuning into a solvable min–max problem

The single most portable idea here. You do not have to invent a method and then analyze
it. Write down

> min over algorithm parameters, of max over the problem class, of the worst-case
> performance over a horizon T

and **solve it**. The trick that makes it finite is parameterizing the function by the
iterates and gradients you would observe, then interpolating back to a real function.

The reframe applies well beyond gradient methods: whenever you have a parameterized
procedure and a characterized class of inputs, *worst-case-optimal parameters are
computable, not guessable.* And there is now an AI workflow wrapping it.

### 10.2 Optimize over the horizon, not the step

Silver step sizes (§4.1) generalize past step-size schedules. The classical rule enforces
improvement at **every** iteration. Altschuler and Parrilo showed that constraint is
**costly**: allow an occasional step that goes uphill, and the horizon-level result
improves provably — κ^{0.786} instead of κ.

Any greedy per-step acceptance criterion is a candidate for this treatment. The question to
ask is: *am I paying for monotonicity I never actually needed?*

### 10.3 Point AI at counterexamples, not theorems

The concrete finding from §7: AI's successes in optimization this year are concentrated in
**lower bounds** — that is, in constructing worst-case instances. Wright's explanation is
that lower bounds are counterexample construction, and these systems are good at it.

Actionable version: when you hand a model a specification or a claim, the higher-yield
instruction is **"construct the instance where this fails"** rather than **"show this
holds."** This is the same lesson Kontorovich reports from a different direction — the
AlphaProof trick of searching for a statement *and its negation* caught his specification
errors, not his mathematical ones.

Two ICM plenary speakers, two fields, same finding: **models are better adversaries than
advocates.** Use them that way.

### 10.4 A hypothesis whose conditions destroy your structure is not about your problem

The Bach–Huiberts result (§3.2) is the clean case. Classical smoothed analysis required
perturbing A, which means replacing every structural zero with a Gaussian — annihilating
the sparsity that the entire solver exists to exploit. The theorem was true and did not
apply to any LP anyone solves. Getting the same conclusion while **leaving A alone** is what
made it a result about real linear programs.

Read your guarantees for this failure. The question is not whether the hypotheses hold, but
whether anything you care about survives them.

### 10.5 The failed search that paid

Fifty years of hunting for a provably polynomial pivot rule produced no such rule. It
produced better heuristics and steadily better commercial LP software (§3.1). Similarly,
the new-generation interior point methods are **not practical** — large constants — yet they
moved the frontier and are now the reason anyone knows LP sits a constant away from matrix
multiplication in the exponent.

Wright's framing is the useful one: **practice does not wait for theory; theory certifies
practice after the fact and occasionally illuminates a technique.** Neither direction is
the primary one.

---

## 11. Where to read next

1. **Wright, *Optimization in Theory and Practice*.**
   [arXiv:2510.15734](https://arxiv.org/abs/2510.15734) — the written version of this talk.
2. **Bach and Huiberts, *Optimal Smoothed Analysis of the Simplex Method*.**
   [arXiv:2504.04197](https://arxiv.org/abs/2504.04197) — the σ^{−1/2} bound and matching
   lower bound.
3. **Bach, Huiberts et al., *Beyond Smoothed Analysis: Analyzing the Simplex Method by the
   Book*.** [arXiv:2510.21613](https://arxiv.org/abs/2510.21613) — the perturb-b-and-c-only
   result.
4. **Nocedal and Wright, *Numerical Optimization*** — his own book; the reference for
   everything in §2 and the §6.5 list.

---

## 12. Self-test

<details>
<summary>1. What is smoothed analysis, and what did the 2025 work change?</summary>

You supply a worst-case LP; the analyst adds small Gaussian perturbations of variance σ²
and proves the expected pivot count is polynomial in the dimension and 1/σ (Spielman–Teng,
2004). Bach–Huiberts reduced the 1/σ exponent — Wright says from about 30 to about 1.5 —
reaching O(σ^{−1/2}d^{11/4}log(n)^{7/4}) with a matching lower bound. Then, crucially, they
obtained the result perturbing **only b and c**, leaving the sparse matrix A intact.
</details>

<details>
<summary>2. Sketch a primal–dual interior point method in four lines.</summary>

Write the LP optimality conditions: Ax = b, Aᵀλ + s = c, x,s ≥ 0, xᵢsᵢ = 0. Relax the last
to xᵢsᵢ = μ > 0, which traces the central path. Fix μ, take two or three Newton steps on
that nonlinear system, curtailing to keep x,s positive. Decrease μ and repeat. Classical
complexity O(n^{3.5}) = O(√n) iterations × O(n³) per solve.
</details>

<details>
<summary>3. Why did first-order LP methods reach production so fast?</summary>

The min–max reformulation means the only per-iteration work is multiplication by A and Aᵀ.
That is cheap for sparse A and extremely efficient on GPUs. They need many more iterations
but are competitive with simplex and IPM on very large problems. Their theory, via the
Hoffman constant, also tracks practice well.
</details>

<details>
<summary>4. What do silver step sizes give up, and what do they buy?</summary>

They give up monotone decrease — an occasional very long step may go uphill. They buy
O(κ^{0.786} log(1/ε)) instead of O(κ log(1/ε)) in the strongly convex case, by optimizing
the step sequence over a horizon rather than per iteration. They still lose to Nesterov's
momentum, which they do not use.
</details>

<details>
<summary>5. What is PEP and what makes it finite?</summary>

Performance Estimation Problem: min over algorithm parameters of max over the function
class of worst-case performance over a horizon T. It becomes finite because you
parameterize f by the iterates x_k and gradients g_k rather than by the function itself,
giving a matrix optimization problem; then you interpolate to recover an actual f in the
class.
</details>

<details>
<summary>6. What is the structure shared by all worst-case functions for lower bounds?</summary>

Information about f is revealed only gradually. The canonical instance: a quadratic with
tridiagonal positive-definite Hessian and linear term e₁, started at 0, so the band
structure lets each iterate fill in exactly one more component. This gives
f(x_k) − f\* ≥ c/k², matching Nesterov's C/k² upper bound and proving his method optimal.
</details>

<details>
<summary>7. What does Muon do with the SVD, and why?</summary>

It reshapes weights into a matrix, forms a momentum-combined stochastic gradient estimate
B_k, computes B_k = UΣVᵀ, **discards Σ**, and uses UVᵀ — the matrix sign — as the search
direction. Justification: it is a trust region step under the spectral matrix norm. At
scale the SVD is approximated iteratively on GPUs.
</details>

<details>
<summary>8. Name the three mechanisms behind benign non-convexity.</summary>

(1) All local minima are global. (2) Strict saddles — every saddle's Hessian has a strictly
negative eigenvalue giving an escape direction. (3) The Polyak–Łojasiewicz condition — the
gradient grows fast enough away from the minimizing set that a gradient step makes real
progress. Wright stresses these are unrelated mechanisms, not one theorem.
</details>

<details>
<summary>9. Which widely used methods have no matching theory?</summary>

Newton, quasi-Newton, L-BFGS, and nonlinear conjugate gradient. Each has worst-case
functions on which it is as slow as plain gradient descent. Also Adam, whose provable rates
are generally no better than SGD despite dominating practice.
</details>

<details>
<summary>10. Where has AI actually succeeded in optimization theory, and why?</summary>

In **lower bounds** — constructing worst-case functions, which is counterexample
construction. Wright attributes the fit to optimization's questions being precise, its
techniques technical but highly repetitive. Examples: Ryu's last-iterate convergence for
Nesterov's method (GPT Pro), the infinite-path-length result for Nesterov flow (ChatGPT),
and sharp first-order lower bounds under higher-order smoothness.
</details>

---

## 13. Note on the tutorial process

**Template adaptation for a Tier-0 talk.** The standard template devotes its middle to
building background. Here that section (§2) is a one-page calibration you can skip, and the
length went to the post-2015 frontier instead. For talks in your own field, the tutorial's
job is not the bridge — it is the delta.

**Where the transcript failed and I repaired it.** Auto-captions destroy proper nouns in
this talk more than in Kontorovich's. Corrections made, all verified against the paper or
the primary literature except where noted:

| Caption | Correct |
|---|---|
| Danig | Dantzig |
| Borgart | Borgwardt |
| Spielman and Tang | Spielman and Teng |
| Elon Bach, Sophie Hibbitz | Eleon Bach, Sophie Huiberts |
| Kacion | Khachiyan |
| Kamakar | Karmarkar |
| Neestro / Nestrob | Nesterov |
| Nearoski and Uden | Nemirovski and Yudin |
| Grevak | Griewank |
| Robins and Monroe | Robbins and Monro |
| Yintatly | Yin-Tat Lee |
| Wayne and her | Weinan E |
| Chisard and Bach | Chizat and Bach |
| polyac | Polyak (–Łojasiewicz) |

**Reconstructed, not verified:** "and pillo" → **Parrilo** (consistent with the published
silver-step-size work); "way Sue" → **Weijie Su**. The author of the recent higher-order
lower-bound paper is rendered only as "Joe" and I have not guessed it.

**One transcript error I corrected in substance,** not just spelling: in §4.4 the captions
say the iterate has its "last n−k components nonzero." That is backwards — they are zero,
and that is precisely what makes the lower bound work. Corrected in the text and flagged
there.

**Tier check, applied this time before writing** (the correction from talk 1): title and
opening minutes read first. Wright's talk is what his field says it is, so the reputation
and the content agreed here. That will not always hold.
