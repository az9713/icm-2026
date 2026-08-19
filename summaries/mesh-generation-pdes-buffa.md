---
title: "New Challenges in Numerical Approximation of PDEs"
speaker: Annalisa Buffa (EPFL)
source: https://www.youtube.com/watch?v=D2_RHzeWcgk
video_id: D2_RHzeWcgk
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: none — companion: https://arxiv.org/abs/2307.06265
transcript: ../transcripts/D2_RHzeWcgk_transcript.txt
difficulty_for_you: 1/5 (the frame) — 2/5 (the non-divergence-form machinery)
reading_time: ~50 min
---

# New Challenges in Numerical Approximation of PDEs — Annalisa Buffa

**Field:** numerical analysis of PDEs. But the talk is not about approximating the
*solution* of a PDE. It is about **generating the mesh** — and about using PDEs to do it.

**Difficulty against your background: inverted, and split.** The frame is your own
field. Finite elements, interpolation error, elliptic regularity, optimal transport,
Newton and Picard iteration: you own all of it. So this tutorial does not teach any of
that. The one thing that is genuinely new to a classically trained numerical analyst is
the **non-divergence-form** discretization machinery — the Cordes condition, the
Miranda–Talenti estimate, and the discrete Hessian. That is a real afternoon of new
definitions, which is why the second number is 2 and not 1.

**What this tutorial builds.** A one-page calibration you can skip, then a full
walkthrough of both halves of the talk, with the mathematics restored from the companion
paper and from the primary literature on non-divergence-form finite elements. Two
exercises you can do with pen and paper in half an hour, both of which are the actual
mechanism of the talk rather than illustrations of it.

**Note on sources — read this before you trust any equation below.**

- There is **no ICM 2026 proceedings paper** for this lecture on arXiv.
- She **never names a survey or a review from the podium.** I scanned the transcript for
  "my survey", "our review", "the paper with", journal names and book titles. Nothing.
  Her closing slide thanks collaborators generically.
- The **companion** I am using is
  [arXiv:2307.06265](https://arxiv.org/abs/2307.06265), Hinz and Buffa, *PDE-Based
  Parameterisation Techniques for Planar Multipatch Domains* (submitted 12 July 2023,
  revised 21 July 2023). It is **not the ICM paper and not a survey** — it is the primary
  research paper for the first half of the talk. It contains, by name, the Radó–Kneser–
  Choquet theorem, the Winslow formulation, the Cordes condition, the non-divergence
  system, both the Picard and Newton iterations, the interior jump penalty, and the
  discrete-Hessian recovery. Every one of those appears in the talk. The match is close.
- The **application half of part one** is
  [arXiv:2501.12965](https://arxiv.org/abs/2501.12965), Marcinnó, Hinz, Buffa and
  Deparis, *A spline-based hexahedral mesh generator for patient-specific coronary
  arteries* (submitted 22 January 2025, revised 10 July 2025; published in *Computer
  Methods in Applied Mechanics and Engineering* 445, October 2025). This is **primary
  literature for one application**, not a substitute for a proceedings paper.
- **Part two of the talk — the optimal-transport half — has no paper at all.** She says so
  from the podium: *"it's a work in progress so I don't really have results to show to
  you."* I searched arXiv for Buffa or Hinz with Monge–Ampère or optimal transport and
  found nothing. Everything in §6 below comes from the transcript, plus background
  literature by **other people** which I label as such every time.
- Where I restore a formula that was on the slide and not in the captions, I say so and
  say which paper it came from.

**Names.** The auto-captions damage fewer proper nouns here than in the Wright or Otto
talks, but they do something worse: they mistranscribe a *mathematical object* — the
**Hessian** — as "the action", consistently, throughout the entire technical core. Read
naively, the method is incomprehensible. The correction table is in §12.

---

## 1. What is at stake

The number that organizes the whole lecture is this one:

> On average it takes **70% of the engineering time** to construct a tessellation — not to
> run the model, but to construct a suitable tessellation.

That is the thesis. In industrial simulation, the mesh is the bottleneck, not the solver.
The solver is a solved problem in a way the mesh is not.

Buffa's framing of a numerical simulation is three steps:

1. **Geometric data.** It arrives as medical imaging (an angiogram with contrast injected
   into the coronary arteries), as a CAD boundary representation (a machined part), or as
   a point cloud (reverse engineering).
2. **Processing that data into a tessellation.** Split the *volume*, not just the surface,
   into tetrahedra or into hexahedra. This is the 70%.
3. **Designing a discrete, computable model of the physics.** Navier–Stokes at moderate
   Reynolds number for the arteries, closed with a 1D circuit model because the inflow and
   outflow pressures are unknown; nonlinear nearly-incompressible elasticity, fracture,
   plasticity and fast dynamics for the mechanical part; the drift-reduced **Braginskii**
   system for the plasma edge in a tokamak.

Her own field — and the field the mathematical community has poured effort into for
twenty years — is step 3. Her claim is that step 3 was never the binding constraint:

> "The effort until now [has] been on the efficient use of splines to represent physical
> quantities. So, for the third step of the numerical simulation. And now I want to go
> back and understand if that's enough. **It turns out that it is not enough.**"

What made her go back was not a theorem. It was two customers arriving within months of
each other, both asking for the same thing and both unable to buy it:

- The **EPFL imaging centre and the university hospital** wanted to extract geometry from
  angiographic projections and run fast simulations at population scale. They needed
  **structured, parametric** meshes of coronary arteries. They came to her because *"they
  could not find a ready-on-the-shelf tool to produce such a mesh."*
- The **Swiss Plasma Center** wanted to improve their tokamak simulations. Their existing
  mesh is a torus with a rectangular cross-section — but that is not the shape of the
  machine. They wanted a **fully tensor-product** mesh, merely deformed to the true
  machine cross-section, and they wanted it to extend to **stellarators** later.

So the problem: given a 2D cross-section boundary, produce a structured spline
parametrization of the interior that never folds, robustly, without human intervention,
and then extrude. And then — the second half — produce not merely *a* valid mesh but the
*right* one.

---

## 2. Calibration: what you can skip

You know all of this. It is here so we are using the same words. Go to §3.

**Tessellation and discrete space.** Write $\mathcal{T}_h$ for the tessellation. On it you
build piecewise polynomials of degree $p$ with global regularity $C^{e}$. (The captions
render the degree as "L" and the regularity as "e"; I use $p$ and $e$.) The parameter $e$
is the one that matters in this talk.

**Simplices versus cuboids, and why she cares.** Tetrahedral meshing of an arbitrary
domain is easy; hexahedral meshing is hard. But on a generic tetrahedral mesh the
achievable global regularity is $e = 0$ or $e = -1$ — continuous or discontinuous. Getting
more is very hard. On a **regular tensor-product** mesh, splines give you $e = p - 1$
essentially for free. That is the entire trade: you accept the harder meshing problem to
buy smoothness, and smoothness buys degrees of freedom.

> "If we can do that, we save a lot of computational effort when we solve a problem. So,
> when the construction is possible, spline-based methods outperform other methods."

Hence the research programme: *push the boundary of when the construction is possible.*

**The multipatch setting, which is the setting for the whole talk.** A reference domain
$\hat\Omega$ made of several patches. Inside each patch the mesh is tensor-product and the
spline space is $C^{p-1}$. Across patch interfaces the space is only $C^0$. She notes that
$C^1$ multipatch constructions exist but *"are not so friendly computationally speaking"*.
A map $\mathbf{x} : \hat\Omega \to \Omega$ carries this to the physical domain.

Every "patchwise" qualifier later in the talk comes from that single fact: **the Hessian
does not exist across the blue lines.**

**The approximation estimate.** For $u$ in a Sobolev class and $\Pi_h u$ its projection,
locally on element $K$,

$$\|u - \Pi_h u\|_{L^2(K)} \;\lesssim\; C\, h_K^{s}\, |u|_{H^{s}(\hat K)}$$

with $h_K$ the element size and $\hat K$ the patch of elements around $K$. She calls this
*"the easiest one I wrote for you"* and it is all she needs. Two consequences she draws:
elements must be **small where derivatives are large**, and the constant $C$ **blows up if
the mesh is badly shaped**. Both are load-bearing in the second half.

**Mesh quality measures.** The **scaled Jacobian** — close to 1 is good — and the
**skewness**. Standard, and used as the score throughout.

### 2.1 The anchor the brief expected, and why it is not this talk

If you know Buffa's name you know isogeometric analysis, and you probably know the pitch:
*use the same spline space for the CAD geometry and for the analysis basis, so the meshing
step disappears.* That pitch is not in this lecture, and the lecture is in a sense a
correction to it. She keeps the isoparametric principle — the map $\mathbf{x}$ and the
unknowns live in the same spline space — but she is spending an hour on the step the pitch
waved away. **A CAD file gives you the boundary. It does not give you a valid
parametrization of the interior.** Finding one is the surface-to-volume problem, and it is
itself a hard PDE problem. That is the honest relationship between her reputation and this
talk.

Two other things her reputation would predict are simply **absent**, and you should know
they are absent rather than wonder where they went:

- **Finite element exterior calculus and discrete de Rham complexes.** She is one of the
  people who built the isogeometric de Rham sequence. Not one word here. No differential
  forms, no cohomology, no structure preservation.
- **Defeaturing and a posteriori error estimation.** Her 2020–2026 output is full of it
  (arXiv [2007.11525](https://arxiv.org/abs/2007.11525),
  [2312.15968](https://arxiv.org/abs/2312.15968),
  [2512.20124](https://arxiv.org/abs/2512.20124)). Absent.
- And a subtler absence: this talk's adaptivity is **r-adaptivity** — move the nodes, keep
  the connectivity — not the **h-adaptivity** of hierarchical spline refinement, whose
  mathematical foundations she co-authored
  ([arXiv:2107.02023](https://arxiv.org/abs/2107.02023)). She never mentions that work.

---

## 3. The bridge: elliptic PDEs in non-divergence form

This is the one section with genuinely new content for you, and it is short. Everything
else in the talk you can read at sight.

### 3.1 What "non-divergence form" means and why it changes everything

You are trained on

$$-\nabla \cdot (A \nabla u) = f$$

You multiply by $v \in H^1_0$, integrate by parts once, and get a bilinear form
$\int A\nabla u \cdot \nabla v$ that is coercive on $H^1_0$ as soon as $A$ is uniformly
positive definite. Lax–Milgram closes it. The whole finite element edifice — Céa's lemma,
Galerkin orthogonality, conforming $C^0$ elements — follows.

Non-divergence form is

$$A : D^2 u \;=\; \sum_{i,j} A_{ij}\, \partial_{ij} u \;=\; f$$

with $A$ **inside** the second derivative rather than under a divergence. If $A$ is
smooth the two forms are equivalent up to lower-order terms. **If $A$ is merely bounded
and measurable, they are not**, and the divergence-form weak formulation does not exist:
there is nothing to integrate by parts onto.

This is not a technicality manufactured for the talk. It is where the equation genuinely
lives, as you will see in §5.1: $A$ there is built from the Jacobian of the unknown map,
so it is exactly as rough as the map, which is a $C^0$ multipatch spline.

The natural space is $H^2 \cap H^1_0$, and the natural question is whether

$$L : H^2 \cap H^1_0 \longrightarrow L^2, \qquad L u = A : D^2 u$$

is an isomorphism. Two ingredients answer it.

### 3.2 The Miranda–Talenti estimate — verify this in two lines

For $u \in H^2 \cap H^1_0(\Omega)$ with $\Omega$ **convex**,

$$\|D^2 u\|_{L^2(\Omega)} \;\le\; \|\Delta u\|_{L^2(\Omega)}$$

The mechanism is one you already have. For $u \in C_c^\infty$, integrate by parts twice:

$$\int u_{ii}\,u_{jj} \;=\; -\int u_{iij}\,u_{j} \;=\; \int u_{ij}\,u_{ij}$$

Sum over $i,j$ and you get $\int (\Delta u)^2 = \int |D^2u|^2$ — an *identity*, not an
inequality. For $u$ vanishing on $\partial\Omega$ but not compactly supported, the same
computation leaves a boundary term proportional to the **curvature of $\partial\Omega$**,
and convexity makes that term have the right sign. Hence the inequality.

That is the whole content: *on a convex domain the Laplacian controls the full Hessian in
$L^2$.* You can therefore use $\Delta u$ as a test function and get $H^2$ stability out.
Buffa says exactly this from the podium — *"I have a specific test function that is the
Laplace of $u$"* — and calls the resulting bound *"what in applied mathematics we call an
inf-sup condition"* (the captions say "inf sub").

### 3.3 The Cordes condition — and a computation worth doing

Miranda–Talenti handles $A = I$. To get from there to general $A$ you need $A$ to be
*close enough to a multiple of the identity, uniformly.* That closeness is the **Cordes
condition**. In $\mathbb{R}^n$, for symmetric positive definite $A$, it asks for an
$\varepsilon \in (0,1]$ with

$$\frac{|A|_F^2}{(\operatorname{tr} A)^2} \;\le\; \frac{1}{n - 1 + \varepsilon}
\qquad \text{a.e.}$$

*(Restored from the primary literature on non-divergence FEM — Smears and Süli, SIAM J.
Numer. Anal. 51 (2013) 2088–2106 — not from the slide. The companion paper states the
condition and the normalizer $\gamma = \operatorname{tr}A / |A|_F^2$ but the fetched HTML
does not render the inequality cleanly.)*

Here is why that particular ratio, and it is a five-line calculation. Set
$\gamma = \operatorname{tr}A / |A|_F^2$ and measure how far $\gamma A$ is from the
identity:

$$|\gamma A - I|_F^2 \;=\; \gamma^2 |A|_F^2 - 2\gamma \operatorname{tr}A + n
\;=\; \frac{(\operatorname{tr}A)^2}{|A|_F^2} - 2\frac{(\operatorname{tr}A)^2}{|A|_F^2} + n
\;=\; n - \frac{(\operatorname{tr}A)^2}{|A|_F^2}$$

Cordes says $(\operatorname{tr}A)^2/|A|_F^2 \ge n - 1 + \varepsilon$, so

$$|\gamma A - I|_F \;\le\; \sqrt{1 - \varepsilon} \;<\; 1$$

The dimension cancels. **Cordes is precisely the statement that after one scalar
renormalization, $A$ is a uniform contraction away from the identity.** The rest is a
Banach fixed point: the map $u \mapsto u - \gamma(A : D^2u - f)$ is a contraction on
$H^2 \cap H^1_0$ by Miranda–Talenti, so $L$ is bijective. That is the well-posedness she
quotes as *"mathematics again comes to help."*

Note what did **not** happen. There is no coercive bilinear form on $H^1_0$, no Céa lemma,
no conforming $C^0$ element. The stability is an inf-sup in $H^2$, and the discrete space
must reproduce it. That is the entire source of difficulty in §5.

### 3.4 The discrete Hessian, and why it is needed

On a $C^0$ multipatch spline space, $D^2 v_h$ does not exist across patch interfaces. Two
repairs, and Buffa presents both because they behave very differently:

- **Piecewise Hessian plus a penalty.** Define $D_h^2$ patchwise, then add jump penalties
  to stop the patches from drifting apart. This is the $C^0$ interior-penalty idea.
- **Lifted (or recovered) Hessian.** Define $D_h^2 v_h$ as the $L^2$ projection of the
  *distributional* Hessian onto the discrete space — that is, integrate by parts twice and
  keep the interface terms, which appear as jump-times-average contributions. No parameter
  appears.

She calls the second object *"the Ritz representation of the Hessian in the sense of
distributions"*. It is the discrete-Hessian-recovery approach, and the companion paper
(§3.1.3) has it.

That is the whole bridge. Everything below is a talk you can read.

---

## 4. The talk rebuilt, part one: meshes from harmonic maps

### 4.1 The problem, stated exactly as she states it

Find a bijective map

$$\mathbf{x} : \hat\Omega \to \Omega
\qquad\text{with}\qquad
0 < c \le \det J(\mathbf{x}) \le C < \infty$$

with $\mathbf{x}$ a spline. The determinant bound is not decoration — it is the
requirement that **no element flips**, that every image cell has positive area. She is
blunt about why splines: *"I know that splines will give me quite an advantage."*

The naive approach, and the one the field mostly uses, is to write down a mesh-quality
functional and minimize it — the Winslow functional
$\int \operatorname{tr}(G)/\det J$, for instance. She rejects it:

> "Instead of running an optimization technique trying to construct $\mathbf{x}$ as a
> minimum of a certain functional, **I want to use mathematics.**"

### 4.2 The anchor: a classical theorem replaces a heuristic

This is the first place the speaker hands you the anchor, and it is a good one because the
theorem is one you can state from complex analysis.

> "One of the fundamental theorems of analysis tells me that if $\hat\Omega$ is convex,
> $\mathbf{x}$ can be chosen as the **inverse of a harmonic map**."

The theorem is **Radó–Kneser–Choquet**, and the companion paper states it as its Theorem 1:

> The harmonic extension of a homeomorphism from the boundary of a Jordan domain
> $\Omega \subset \mathbb{R}^2$ onto the boundary of a **convex** domain
> $\hat\Omega \subset \mathbb{R}^2$ is a diffeomorphism in $\Omega$.

*(She does not say the name aloud. I take it from the companion paper, which does.)*

Read the direction carefully, because it is the crux. The **harmonic** map runs from the
complicated physical domain $\Omega$ into the **convex** parametric domain $\hat\Omega$.
Harmonicity plus convexity of the *target* is what forces injectivity. The parametrization
you actually want, $\mathbf{x} : \hat\Omega \to \Omega$, is its **inverse**.

This is the classical **Winslow** construction from elliptic grid generation, named in the
companion paper. Its usual defect is exactly the inversion: solve Laplace on $\Omega$ and
you must invert the result numerically. Buffa's move is to pull the equation back and
solve for $\mathbf{x}$ directly on $\hat\Omega$, where the mesh is a nice tensor product.

She adds the caveat immediately, and it is a real limitation of the whole programme:

> "This theorem is true in dimension two and unfortunately **not** in dimension three. I
> would love to have a similar theorem in dimension three, but I don't."

That single sentence explains the architecture of the entire talk. Everything is 2D
cross-sections plus extrusion — *"2D plus a half"*, in her phrase — because the univalence
theorem exists only in the plane.

### 4.3 The equation you actually solve

Pull back $\Delta_{\mathbf{x}} \boldsymbol{\xi} = 0$ to the parametric domain and you get,
componentwise for $i = 1, 2$,

$$A(\partial_{\boldsymbol\xi}\mathbf{x}) : D^2 x_i \;=\; 0
\quad\text{in } \hat\Omega,
\qquad \mathbf{x} = \mathbf{F} \ \text{ on } \partial\hat\Omega$$

with

$$A(\partial_{\boldsymbol\xi}\mathbf{x}) \;=\;
\begin{pmatrix} g_{22} & -g_{12} \\ -g_{12} & g_{11}\end{pmatrix},
\qquad
g_{ij} \;=\; \partial_{\xi_i}\mathbf{x} \cdot \partial_{\xi_j}\mathbf{x}$$

*(Restored verbatim from the companion paper, [arXiv:2307.06265](https://arxiv.org/abs/2307.06265),
equations around (9)–(11). The talk shows the system on a slide and the captions carry no
formula.)*

So $A$ is a rearrangement of the metric tensor — exactly as she says — and the system is
**quasilinear** (the coefficient depends on the first derivatives of the unknown) and in
**non-divergence form**.

> ⚠️ **Caption correction, substantive.** The transcript says *"a system of quasi-linear
> PDEs in the divergence form"*. That is a caption slip: the system is in **non-divergence
> form**, which the companion paper states explicitly and which the rest of the talk
> repeatedly confirms (*"a second-order PDE in non-divergence form"*). If you read it as
> divergence form, nothing downstream makes sense.

**And now a small pleasure, which is my own computation and which you can check.** Why
does the Cordes condition hold for *this* $A$? Compute:

$$(\operatorname{tr}A)^2 - |A|_F^2
= (g_{11}+g_{22})^2 - (g_{11}^2 + g_{22}^2 + 2g_{12}^2)
= 2(g_{11}g_{22} - g_{12}^2) = 2\det G = 2(\det J)^2$$

So

$$\frac{(\operatorname{tr}A)^2}{|A|_F^2} \;=\; 1 + \frac{2(\det J)^2}{|A|_F^2}$$

and the 2D Cordes condition $(\operatorname{tr}A)^2/|A|_F^2 \ge 1+\varepsilon$ becomes

$$2 (\det J)^2 \;\ge\; \varepsilon\, |A|_F^2$$

**The Cordes condition for this problem says exactly: the Jacobian determinant is bounded
away from zero relative to the local stretching — the mesh does not fold.** The
analytical hypothesis and the engineering requirement are the same statement. That is why
the method can be self-certifying along the iteration: if you keep $A$ Cordes, you keep
the mesh valid, and vice versa.

*(Marked: the two displayed identities above are my derivation, combining the companion
paper's $A$ with the standard Cordes condition. Verify by expanding the square. She does
not make this remark aloud, and if she made it on a slide the captions do not show it.)*

### 4.4 Linearize: Newton or Picard

Quasilinear, so you iterate. She sets up a **weighted nonlinear residual functional** —
take the residual, multiply by a constant, and test against $\tau v$ where $\tau$ is an
operator to be chosen — and then applies either:

- **Newton**, giving local quadratic convergence; or
- **Picard**, a fixed-point iteration in which she *"regularizes the matrix $A$"*, because
  the iteration needs $A$ to stay symmetric positive definite and Cordes for the
  well-posedness of §3.3 to apply at every step.

Either way, the object at every step is the same:

> A second-order linear PDE in **non-divergence form**, with $A$ **piecewise regular**,
> symmetric positive definite, satisfying Cordes.

*"So, that's the problem that I need to solve. I want to do it fast and accurately."*

The words **piecewise regular** are the whole difficulty of the next section. $A$ is built
from $\partial\mathbf{x}$, and $\mathbf{x}$ is only $C^0$ across patch interfaces. So $A$
**jumps** across the blue lines. The classical theory assumes $A$ regular.

---

## 5. The one argument: two discretizations, one proof, and a numerical certificate

This is the mathematical core, and it is also the most interesting methodological moment
in the lecture, because she presents a method with a complete theory and a method without
one, and **prefers the one without**.

### 5.1 Method A — mimic the continuous stability, and pay for it

The continuous proof used $\Delta u$ as a test function. So do that discretely: test
$L u_h$ against $\Delta_h v_h$, where the subscript $h$ means **patchwise** — you cannot do
better on a $C^0$ space.

That does not close by itself. Patchwise operators cannot see the interfaces, so the
discrete space is effectively too large and uniqueness fails. Her word: *"There is no way
around it — if I don't control the jumps, then my space will just be too big to have
existence and uniqueness."* So add a **stabilization** penalizing the jumps of the gradient
and of the Hessian across interfaces, with parameters $\mu_1, \mu_2$.

**Theorem (Buffa, stated from the podium; exact norms and constants were on the slide).**
The resulting bilinear form is **coercive in a discrete $H^2$ norm** — the patchwise
$H^2$ seminorm plus the weighted interface jump terms. Coercivity gives stability, which
gives well-posedness of the discretely linearized problem.

> *[Gap: the precise discrete norm, the scaling of the penalty weights in $h$, and the
> admissible ranges of $\mu_1,\mu_2$ were on the slide and the captions carry no formula.
> **Impact: moderate.** The shape of the theorem is fully stated and is standard for
> $C^0$-interior-penalty methods; the exponents matter if you want to implement it. The
> companion paper's equation (33) has an interior penalty of the form
> $\eta \sum_j \int_{\gamma_j} [\![\nabla x_i]\!] : [\![\nabla \phi_i]\!]\,d\Gamma$, which
> is the gradient-jump half of it.]*

**The key lemma is a discrete Miranda–Talenti estimate.** Continuously, the Laplacian
controls the Hessian. Discretely, the *patchwise* Laplacian controls the *patchwise*
Hessian **plus the jumps** — and the jump term is not optional:

> "This jump part is needed because otherwise the patches can float and the
> Miranda–Talenti estimate cannot be true."

That is the right one-sentence explanation. Two patches whose functions differ by an
affine function have zero patchwise Hessian and zero patchwise Laplacian, but are not a
single $H^2$ function. The jump term is what removes that kernel.

The proof goes through an **enrichment operator**: construct an auxiliary discrete space
and an operator $E$ such that for any $v_h$, the Hessian of $v_h - E v_h$ is bounded by the
jumps alone. That splits the estimate into a local part and an interface part, which can
then be assembled. She declines to give details — *"I don't want to enter into the
detail"* — and so do I.

*(The enrichment-operator technique is standard in $C^0$-interior-penalty analysis; see
Gallistl and Tian, [arXiv:2209.12500](https://arxiv.org/abs/2209.12500), for continuous
finite elements satisfying a strong discrete Miranda–Talenti identity. That reference is
mine, not hers.)*

### 5.2 The objection she raises against her own theorem

This is the sentence in the talk I would put on a wall:

> "It is well known in numerical analysis that as soon as I have three or four parameters
> to play with, **I may just get random numbers out of my code**, because I choose my
> parameters and then what happens I don't know. So this is where mathematics stops and
> practice comes in. We don't want to have too many parameters."

A complete convergence theory whose constants depend on penalty parameters you must
hand-tune is a theory about a family of methods, not about the method you run. Every
number that comes out of the code is conditional on a choice nobody can justify.

### 5.3 Method B — parameter-free, fourth order down to second, no proof

The alternative defines the discrete Hessian by **integration by parts, twice, keeping the
interface terms**:

$$H_h(v_h) \;\approx\; D^2_{\text{patchwise}} v_h \;-\; \big(\text{interface term}\big),
\qquad \text{interface term} \sim \sum_{\text{faces}} [\![ \cdot ]\!]\,\{\!\!\{\cdot\}\!\!\}$$

— jump times average, in the standard DG notation. She calls $H_h$ the **Ritz
representation of the Hessian in the sense of distributions**, and constructing it is
*"just an $L^2$ projection"*. Then solve

$$\int A : H_h(u_h)\; v_h \;=\; \int f\, v_h$$

Two concrete wins, both of which matter to anyone who has assembled a matrix:

1. **It is a second-order problem, not a fourth-order one.** Method A tests against
   $\Delta_h v_h$, so the bilinear form contains second derivatives on both sides — a
   biharmonic-type operator, with the conditioning and bandwidth that implies. Method B
   has the test function undifferentiated. *"This is a second-order equation. The previous
   one was a fourth-order equation, which makes my matrices much worse."*
2. **It is parameter free.** No $\mu_1$, no $\mu_2$.

**And she cannot prove it.** The existing proof of discrete ellipticity for this kind of
scheme — she describes it as *"a few pages"* — goes: localize into charts; approximate $A$
by a **constant** on each chart; observe that with constant $A$ the local problem is
essentially a Laplace problem after integrating by parts, hence well-posed; assemble.

Her $A$ is only **piecewise** regular. So when she localizes, three kinds of chart appear:

- charts interior to a patch, where $A$ is regular — fine, the classical proof applies;
- charts straddling one interface, where $A$ takes **two** values;
- charts at a patch corner, where $A$ takes **three or four** values — the "blue cross".

On a chart where $A$ jumps, the local problem is not a Laplace problem and the classical
argument fails.

> "And this problem is **open**. I cannot prove the stability on the local charts."

### 5.4 What she does instead — and this is the transferable part

> "**But, I am a numerical person.** So now I have a local chart. This is a very confined
> problem. I can map back my local space into a fixed configuration, and now I can run a
> numerical test."

The local problem, once you have localized, is *finite-dimensional and small*. So she
computes the **smallest singular value** of the local operator on a fixed reference
configuration, sweeping over:

- the geometric configuration (she shows the diamond-shaped chart with three values of
  $A$),
- the distribution of values of $A$ across the patches meeting there,
- the mesh refinement level.

Result: **no singular value falls below a fixed positive threshold** — the blue line in
her plot — under refinement. The local problems are invertible, uniformly.

> "That's the only way I can sort of prove it, and at the end **I'm confident** that I
> actually have stability for this system."

Note what this is and what it is not. It is not a proof. It is a **finite, exhaustive,
reproducible computation covering the finite-dimensional reduction of the missing step in
a proof.** The theorem is out of reach; the certificate is not. And she says plainly which
of the two she has.

### 5.5 Do the two methods agree in practice?

Yes. Her academic test: parametric domain a circle, target a non-convex 2D shape, **initial
guess folded**. Run Picard (linear convergence) or Newton (quadratic, from close enough)
and both unfold it. Final Jacobian ranges from **1 to 5** over the mesh — bounded away from
zero and from infinity, which is precisely the admissibility condition of §4.1.

> "They perform in a similar way, but still the second method gives me much better matrices
> to invert, so I really prefer the second one — **although I don't have completely good
> mathematics for that.**"

---

## 6. The talk rebuilt, part one continued: what it was for

### 6.1 Coronary arteries

Pipeline:

1. From two near-orthogonal angiographic projections, a **deep neural network** segments
   the vessel and recovers the **centreline** and diameter. (The companion application
   paper credits Mahendiran et al. 2024 for this step and reconstructs the 3D centreline
   by intersecting the epipolar lines of the two projections.)
2. Mesh **each cross-section** with the harmonic-map method of §4–5.
3. Interpolate the sections along the vessel using a **non-rotating reference frame**
   along the centreline — the standard fix for the fact that a Frenet frame twists and
   flips at inflection points.

The extrusion, she says, is the easy part. The 2D problem was the hard part, and that is
the design consequence of the theorem being 2D-only.

**Then the number that justifies the whole enterprise.** They ran it blind on a database of
**12,000 patients** with **about 1,000 meshable vessels** — the counts as spoken; see the
caveat below — and:

- **over 99% success**, fully automatic, no human intervention;
- **97% of elements** with scaled Jacobian between **0.9 and 1**;
- skewness very small.

Compared against **VMTK** and **Gmsh**, off-the-shelf tools: they produce meshes, but with
a **spread** scaled Jacobian — a long tail of bad cells. *(The published paper reports, for
a single-branch case, min/mean/max scaled Jacobian 0.785 / 0.979 / 0.999 with 99.5% of
cells in $[0.9,1]$; for a bifurcation, 0.488 / 0.907 / 0.999. It also reports that more
than 80% of structured cells have negligible skewness, against more than 30% of VMTK and
Gmsh cells exceeding the preferred skewness limit of 0.5.
[arXiv:2501.12965](https://arxiv.org/abs/2501.12965), Tables 2–3.)*

> *[Gap: the "12,000 patients / 1,000 meshable vessels / 99% success" figures are from the
> talk only and the phrasing is hesitant in the captions — she restarts the sentence. The
> published paper predates this validation and reports per-case statistics instead. I
> quote the talk as spoken and do not reconcile the two. **Impact: low.** The claim being
> made — near-total automation at population scale — is unambiguous.]*

**Why 99% and not 95%.** Because the goal is not one simulation. It is *"to feed machine
learning with the data that we get at the end"*, scaling from a thousand patients to
several thousand. At that scale a 5% manual-repair rate is a person's full-time job; a 1%
rate is a rounding error. **Robustness is what converts a method into a data generator.**

**And because the mesh is a spline, it is parametric.** This is the payoff she flags as the
reason for insisting on splines in the first place:

> "If a patient has a stenosis, we can **move the stenosis** and run Navier–Stokes again.
> And this can help the practitioners decide if this stenosis was harmful or not."

One patient, many counterfactual anatomies, all from one parametrized mesh. You cannot do
that with an unstructured tetrahedral mesh — there is no knob to turn.

**The extra mile.** Real coronary trees bifurcate. Handling a bifurcation needs a
"butterfly" block decomposition, and choosing where to place it is a judgement call — *"we
gave up a bit on the same mathematical precision"*. It works, including for **non-planar**
bifurcations, and the quality holds. Then the same machinery meshes the **circle of
Willis**, the cerebral vascular ring.

### 6.2 The tokamak

*"In my perspective, the tokamak is just a two-dimensional section that I then need to
extrude"* — on a vessel or on a torus, she does not mind.

Their constraints were harder than the arteries':

- **No singular points allowed.** A fully tensor-product mesh, no extraordinary vertices,
  because they run a **fourth-order finite-difference** scheme for the reduced Braginskii
  system and it needs a global structured grid.
- **Aspect ratio under control**, because their time stepping is **explicit** — a very
  small element sets the CFL limit for the whole simulation.

She got it, and pays in **skewness at one corner**: *"in this corner the mesh is not
perfect, but the geometry is complex enough."* It ran on the real machine geometry. Next
target: **stellarators**, in progress.

### 6.3 The alphorn

Worth keeping because it is the cheapest possible demonstration of the point. A Swiss
alphorn maker — the captions render the instrument as "corn"/"cone" and the man's first
name as **Gerard** *(unverified; the photograph is credited to the newspaper *Le Temps*)* —
was getting an uncontrollable whistle at the end of his hand-made horns. He asked for help.
A horn is an easy geometry, so: mesh it, run acoustics, optimize the shape. It worked, and
made the newspaper.

The serious content: once meshing is automatic, the marginal cost of a new simulation
domain drops to near zero, and problems that were never worth a week of a graduate
student's meshing time become a morning.

---

## 7. The talk rebuilt, part two: which mesh, not just a mesh

### 7.1 The question

> "Shall we construct **one** mesh, or shall we construct **an optimal one**?"

Her observation from working with practitioners is that they already know what mesh they
need:

- In a coronary artery, Navier–Stokes at moderate Reynolds number develops **boundary
  layers at the vessel wall**. So concentrate elements at the wall. She does this today —
  *"but this is based on heuristics."*
- In the tokamak, the temperature field has extremely concentrated gradients across the
  **separatrix**, the field line separating plasma confined inside the machine from field
  lines that exit it. So refine near the separatrix. But **how much**, and **how**, while
  keeping the mesh quality good?

The estimate of §2 already tells you the answer in principle: $h_K$ should be small where
$|u|_{H^s(\hat K)}$ is large, and the constant degrades if the elements are badly shaped.
Buffa's move is to take that seriously as a *definition*.

### 7.2 The definition of optimal, and the 1D case you already know

Let $\rho$ be the local interpolation error on each element — or any smooth regularization
of it. She calls $\rho$ the **monitor function**, borrowing the standard term.

> **Definition (hers, stated as a choice).** The optimal mesh is the one on which the error
> is **equidistributed** — the same amount of error on every element.

In 1D this is elementary and you can write it down. Find $x(\xi)$ with

$$\int_0^{x(\xi)} \rho(s)\,ds \;=\; \xi \int_0^1 \rho(s)\,ds$$

Differentiate:

$$\rho(x(\xi))\, x'(\xi) \;=\; \sigma, \qquad \sigma = \int_0^1 \rho$$

She shows the uniform mesh above and the equidistributed mesh below, and that is all there
is to it in one dimension.

*(This is the classical equidistribution principle of adaptive grid generation. The
standard reference is Budd, Huang and Russell, "Adaptivity with moving grids", **Acta
Numerica** 18 (2009), 111–241 — a survey of r-adaptive methods including the
optimal-transport route below. She does not cite it; it is **background literature by other
people**, and I give it because the reader will want the survey she does not name.)*

### 7.3 The anchor: this is Brenier, and you already have it

In $d$ dimensions equidistribution alone does not determine a map — there are far too many
bijections with a prescribed Jacobian. She needs a selection principle, and she takes the
obvious one:

> "Among the very many solutions of this problem, I can select the one where the **mesh
> moves the least**, in the sense of quadratic transport."

That is the **Kantorovich** problem with quadratic cost, and the theorem that closes it is
**Brenier's**:

> "The Brenier theorem tells us that such a minimizer exists and it is the **gradient of a
> convex potential** $\phi : \hat\Omega \to \mathbb{R}$, and the convex potential verifies
> this equation."

> ⚠️ **Caption correction.** The transcript renders this as "the **brainy** theorem" and as
> "a convex functional of a complex potential". Both are Brenier and *convex potential*.

Substituting $\mathbf{x} = \nabla\phi$ into the Jacobian condition gives the **Monge–Ampère
equation**

$$\rho(\nabla\phi(\boldsymbol\xi))\;\det D^2\phi(\boldsymbol\xi) \;=\; \sigma$$

which is her *"determinant of the Hessian equal to $F$, where $F$ contains my monitor
function $\rho$"*. She notes there are also **regularity theorems** for Monge–Ampère,
*"very handy because when we compute we want to compute regular things."*

**You have all of this already.** The Otto tutorial in this repository
(`summaries/geometric-concepts-pde-otto.md`) builds Wasserstein-2, the Benamou–Brenier
formulation, and Brenier's polar factorization at length. I am not rebuilding it. What is
new here is only the *use*: optimal transport as a **mesh generator**, with the monitor
function playing the role of a target density.

The final map is a composition:

$$\mathbf{x}_{\text{final}} \;=\; \mathbf{x}_{\text{initial}} \circ \nabla\phi$$

where $\mathbf{x}_{\text{initial}}$ is the harmonic-map parametrization from part one, and
$\nabla\phi : \hat\Omega \to \hat\Omega$ is a self-map of the parametric domain that
redistributes the parameter lines. **The two halves of the talk compose.** Part one gives
you a valid mesh; part two moves its nodes to the right places without ever touching the
physical geometry.

### 7.4 The boundary condition, and the honest open problem

Almost all Monge–Ampère theory is for the **Dirichlet** problem. She needs something else:

> "We don't want a Dirichlet boundary condition. We just want **the boundary not to move**.
> The boundary should map a square into a square. But the parametrization of the boundary
> can be different from the identity **in the direction along** the boundary, because the
> lines can accumulate or spread out along the boundary."

So the condition is $\nabla\phi(\partial\hat\Omega) = \partial\hat\Omega$: the boundary is
invariant as a set, but points slide within it. Two cases, and the difference is the whole
problem:

- **$\hat\Omega$ a square or a cube.** On the face $\xi_1 = 0$ the image must stay on that
  face, so $\partial\phi/\partial\xi_1 = 0$ there; on $\xi_1 = 1$, $\partial\phi/\partial\xi_1 = 1$.
  A **linear, inhomogeneous Neumann condition**, face by face.
- **$\hat\Omega$ a ball of radius $R$.** The image of a boundary point must satisfy
  $|\nabla\phi| = R$. A **nonlinear** Neumann condition.

*(The general condition and the square/ball dichotomy are stated in the talk. The two
displayed special cases above follow in one line from "boundary maps to boundary" and are
**my derivation** — she shows the ball condition on a slide and the captions carry no
formula. Verify by noting that $\nabla\phi$ must land on $\partial\hat\Omega$ pointwise.)*

And then:

> "The **well-posedness under this weird Neumann condition is an open problem** to my
> knowledge. That's what I do a bit blindly at this point, but it's all that I can do."

This is content, not a gap. She is telling you the theory is not there.

It is worth knowing what *is* there, because it sharpens the statement. As of July 2026
there is a fully discrete convergence theory for finite element splitting schemes for the
**Dirichlet** Monge–Ampère problem, using exactly the discrete-Hessian-plus-discrete-
Miranda–Talenti apparatus of §3–5 (Anna Peruso,
[arXiv:2607.15024](https://arxiv.org/abs/2607.15024), submitted 16 July 2026). *That is
somebody else's paper, not hers, and it is Dirichlet.* The gap Buffa names is precisely the
boundary condition mesh generation needs and Dirichlet theory does not cover.

### 7.5 How she solves it anyway

Reuse Method B from §5.3, in vector form: define Ritz representations for the discrete
gradient and the discrete Hessian, then solve

$$\det H_h(\phi_h) \;=\; F \quad\text{in } \hat\Omega, \qquad
\text{Neumann condition imposed \emph{without} a parameter}$$

*"I decided to just add the Neumann boundary condition here without a parameter, and that's
my decision."*

Then a control question that shows the practitioner reflex:

> "How can I be sure that I'm actually imposing the Neumann boundary condition? This is very
> important to me, because **if the boundary moves, I'm not computing the mesh of the right
> object anymore.**"

She cannot analyse the imposition inside the fully nonlinear problem. So she replaces the
fully nonlinear operator by a **Laplacian**, keeps the same Neumann-imposition mechanism,
and analyses *that* problem — *"the easiest problem I cannot solve"*. There she proves
well-posedness and **optimal approximation rates both for the function and for the Neumann
condition itself**, and concludes the mechanism is sound.

This is the same intellectual move as §5.4 in a different key: **isolate the one step you
cannot justify, shrink it to something you can analyse, and analyse that.** Once as a
finite singular-value computation, once as a linearized surrogate problem.

Solving is then a **nested Newton iteration** — Newton on the Monge–Ampère system, and
inside it the non-divergence solver of part one — and each inner step is again a
second-order non-divergence-form problem. The design constraint on the iteration is that
the **cofactor matrix must stay positive definite**, or you fall out of the well-posedness
regime of §3.3. In her test she gets **quadratic convergence** of the nested Newton and the
mesh visibly equidistributes the prescribed monitor function.

### 7.6 Does it buy anything? Three tests

**Test 1 — a crude fracture model, and the number that matters.** A square with Young's
modulus 1000 everywhere except on a smile-shaped region where it drops to 1. Monitor
function: a regularization of the Young's modulus itself. Solve linear elasticity (nearly
incompressible) on (a) the uniform tensor-product mesh, (b) the Monge–Ampère-adapted mesh.
Error against an overkill reference solution:

- Uniform mesh: the error curve **stagnates**. Refinement stops paying.
- Adapted mesh: **two orders of magnitude** better.

*"I can solve this problem on a coarse mesh that is just adapted via the Monge–Ampère
adaptation. And I gain two orders of magnitude, which is very important especially when I
try to move to 3D."*

**Test 2 — 3D, and a qualitative failure that adaptation removes.** A geometry
*"reminiscent of a cancer growth model"* — she is explicit that it is not one yet. Solve a
Laplace problem with conductivity 1000 outside a blob and 1 inside (regularized), on a
$32^3$ mesh, Cartesian versus optimal-transport-adapted with the conductivity as monitor.
The exact solution should be smooth (she manufactures it as a product of sinusoids).

On the uniform $32^3$ mesh the answer is **completely spurious** — the mesh cannot resolve
the steep conductivity transition. On the adapted mesh she gets what she expects. No error
plot, because the reference solution is out of reach: *"this geometry is too complex to
compute the right solution."*

**Test 3 — the tokamak, and the honest failure.** Here the method meets its limit, and the
limit is not numerical:

> "**How do I choose my monitor function?** I don't quite know. The system is a complex
> multi-physics system."

She shows candidate meshes built on the reasoning *"I'm solving a fluid model that is right
outside and wrong inside, so I better reduce the approximation inside"* — reduce resolution
where the **model** is invalid, not where the solution is smooth. And then:

> "Here you see that the concept of optimality goes back to **I don't know exactly what to
> do.**"

Her closing technical remark on it: the strong **anisotropy** of the edge-plasma equations
calls for a more sophisticated approach to both mesh design and discretization. Isotropic
equidistribution of a scalar monitor cannot express "resolve across the separatrix, coarsen
along it". Work in progress; no results shown.

---

## 8. Do this by hand

### 8.1 The 1D equidistribution map, with a monitor you can integrate (15 minutes)

Take $\hat\Omega = [0,1]$ and a monitor function concentrated near the right endpoint —
say a caricature of a boundary layer,

$$\rho(s) \;=\; 1 + \frac{a}{\delta}\,\mathbf{1}_{\{s > 1 - \delta\}}$$

with $a, \delta > 0$ small. Find the equidistributing map $x(\xi)$ explicitly, and answer:
what fraction of the mesh nodes ends up inside the layer?

<details>
<summary>Solution</summary>

Total mass: $\sigma = \int_0^1 \rho = 1 + a$.

Equidistribution says $\int_0^{x(\xi)}\rho = \xi\sigma = \xi(1+a)$.

For $x \le 1-\delta$ the integral is just $x$, so on that range $x(\xi) = \xi(1+a)$, valid
until $x = 1-\delta$, i.e. until

$$\xi^\ast = \frac{1-\delta}{1+a}$$

For $\xi > \xi^\ast$: $\int_0^x \rho = (1-\delta) + (a/\delta)(x - (1-\delta))$, so setting
that equal to $\xi(1+a)$,

$$x(\xi) \;=\; (1-\delta) + \frac{\delta}{a}\Big(\xi(1+a) - (1-\delta)\Big)$$

**The fraction of nodes in the layer is $1 - \xi^\ast = (a+\delta)/(1+a)$.** With $a = 0.5$
and $\delta = 0.01$, that is about **34% of the nodes in 1% of the domain**.

Two things to take from the algebra. First, the map is **piecewise affine with slope
$(1+a)$ outside the layer and slope $\delta(1+a)/a$ inside** — the slope ratio is exactly
the ratio of monitor values, which is the entire content of equidistribution. Second, the
node fraction depends on $a$, the **integrated** weight of the layer, and only weakly on
$\delta$, its width. *Equidistribution allocates by total error, not by feature size* — so
a thin feature with a large monitor gets many nodes and a thin feature with a small monitor
gets almost none. That is the property you want, and it is also why the choice of monitor
is the whole game (§7.6, test 3).
</details>

### 8.2 Derive the Monge–Ampère equation from equidistribution (20 minutes)

Let $\hat\Omega \subset \mathbb{R}^d$ and let $\mathbf{x} : \hat\Omega \to \hat\Omega$ be a
bijection. Say $\mathbf{x}$ equidistributes the monitor $\rho$ if the $\rho$-weighted volume
of the image of any parametric region equals a fixed multiple of that region's volume.
Write that as a PDE, then impose Brenier's structure $\mathbf{x} = \nabla\phi$ with $\phi$
convex, and read off the equation Buffa solves.

<details>
<summary>Solution</summary>

Equidistribution over an arbitrary region $\hat\omega \subseteq \hat\Omega$ says

$$\int_{\mathbf{x}(\hat\omega)} \rho(y)\,dy \;=\; \sigma\,|\hat\omega|,
\qquad \sigma = \frac{1}{|\hat\Omega|}\int_{\hat\Omega}\rho$$

Change variables $y = \mathbf{x}(\boldsymbol\xi)$ on the left:

$$\int_{\hat\omega} \rho(\mathbf{x}(\boldsymbol\xi))\,\det J(\boldsymbol\xi)\,d\boldsymbol\xi
\;=\; \sigma \int_{\hat\omega} d\boldsymbol\xi$$

Since $\hat\omega$ is arbitrary, the integrands agree pointwise:

$$\rho(\mathbf{x}(\boldsymbol\xi))\,\det J(\boldsymbol\xi) \;=\; \sigma$$

That is the $d$-dimensional equidistribution condition — and in $d = 1$ it is exactly
$\rho(x(\xi))x'(\xi) = \sigma$ from §7.2, so the exercise above is the $d=1$ case.

Now the problem: this is **one scalar equation for $d$ unknown functions**. Underdetermined
for $d \ge 2$. Brenier supplies the missing $d-1$ conditions by minimizing the transport
cost $\int |\mathbf{x}(\boldsymbol\xi) - \boldsymbol\xi|^2$, whose minimizer is a **gradient
of a convex potential**, $\mathbf{x} = \nabla\phi$. Then $J = D^2\phi$, and

$$\boxed{\;\rho(\nabla\phi)\,\det D^2\phi \;=\; \sigma\;}$$

Convexity of $\phi$ is what makes $\det D^2\phi > 0$, so the map cannot fold — the same
requirement as §4.1, now built into the ansatz rather than enforced.

**The count is the point.** Equidistribution gives one equation; the mesh has $d$ degrees of
freedom per node; optimal transport supplies a principled way to spend the remaining
$d - 1$. Any other selection principle would give a different mesh. Buffa says so
explicitly — *"it's a choice to make my life simple. I could definitely have taken other
choices."*
</details>

---

## 9. What is actually useful to you

### 9.1 A numerical certificate where the theorem is out of reach

The methodological core of §5.4, restated so it transfers. She has a proof strategy with
one missing step. Rather than abandoning the method or claiming more than she has, she:

1. **Localizes** until the missing step is a *finite-dimensional* statement about a *small*
   configuration;
2. **Enumerates** the configuration space — geometry, coefficient values, refinement level;
3. **Computes a quantitative margin** (the smallest singular value) rather than a
   pass/fail;
4. **States clearly** that this is confidence and not proof, and ships the method anyway.

This is directly the shape of what you can do when verifying an agent system. The general
claim — "this pipeline is correct" — is not provable. But most such claims decompose into a
kernel that is finite: a bounded set of tool-call shapes, a bounded set of state
transitions, a bounded set of prompt-schema pairs. Enumerate that kernel exhaustively,
report a **margin** rather than a boolean, and be explicit about the boundary between what
was checked and what was assumed. The value is in steps 3 and 4: a margin tells you how
close you are to failure and degrades gracefully; a passing test tells you nothing.

Note also that the enumeration is only possible **because of the localization**. The work
was in reducing the claim to something finite, not in running the computation.

### 9.2 Parameters are a correctness problem, not a tuning problem

> "As soon as I have three or four parameters to play with, I may just get random numbers
> out of my code."

She has a method with a complete convergence theorem (Method A, two penalty parameters) and
a method with an open stability question (Method B, zero parameters). **She prefers B.**

The reasoning is not sloppiness, it is a claim about what a theorem is worth. A guarantee
conditional on parameters nobody can choose from first principles is a guarantee about a
family, and the member you actually ran is not identified. Method B's honest status — "I
have strong numerical evidence and no proof" — is a *cleaner* epistemic position than
Method A's "I have a proof, for some choice of $\mu_1,\mu_2$ I cannot name."

The version for your work: every configuration knob in an agent system is a hypothesis
you have not tested, multiplied by every other knob. A pipeline with a threshold, a retry
count, a temperature and a top-k has a $2^4$-corner space and you have measured one corner.
Removing a knob is worth more than tuning it, and it is worth more than proving a theorem
that holds for some setting of it.

### 9.3 Encode the practitioner's knowledge as a function, not as a hand edit

The whole second half is one idea: the engineer already knows there is a boundary layer at
the wall and a steep gradient at the separatrix. Today that knowledge enters as **manual
mesh editing** — "tedious optimizations and human interventions", her words. Buffa's
proposal is to make it enter as a **monitor function $\rho$**, and then let a PDE do the
work.

The gain is not accuracy — it is that the knowledge becomes an **input** rather than an
**intervention**. It can be versioned, swapped, computed from a previous solution,
transferred between patients. Two orders of magnitude of accuracy came along with it, but
the reason it scales to 12,000 patients is that nobody has to touch the mesh.

Every place your systems have a hand-tuned artifact — a prompt fragment, a curated example
set, a routing table — ask whether the knowledge behind it could be a function of the
input instead of a constant baked into the artifact. And note the failure mode she reports
honestly: **for the tokamak she does not know what $\rho$ should be**, and the method
therefore stalls. Encoding the knowledge does not create it.

### 9.4 Robustness is the feature that changes the category

99% automatic success is not "a bit better than 95%". It is what turns a mesh generator
into a **data generator**, which is what makes population-scale simulation possible, which
is what makes feeding a machine-learning model with simulated haemodynamics possible. The
architecture of the downstream system is determined by the failure rate of the upstream
component.

You already know this from agent pipelines — a step that needs human repair 5% of the time
cannot be chained ten deep. What is worth taking is Buffa's route to the 99%: not error
handling and retries, but a **change of formulation** so that the failure mode is excluded
by a theorem. The Radó–Kneser–Choquet route cannot produce a folded mesh, because
harmonicity onto a convex target forbids it. She did not make failures recoverable, she
made them impossible.

### 9.5 The 2D theorem is the architecture

The single most instructive structural fact in the talk: **the univalence theorem holds in
2D and not in 3D**, so the entire system is "2D plus a half" — mesh cross-sections,
extrude along a curve or a torus. That is not a compromise bolted on afterwards, it is the
system design, and it is dictated by exactly one piece of mathematics.

When a guarantee is available in a restricted regime, the highest-value design question is
usually *can I restructure the problem so that only the guaranteed regime is ever
exercised?* — rather than *can I extend the guarantee?* She takes the first branch and says
plainly that she would like the second.

---

## 10. Where to read next

1. **Hinz and Buffa, *PDE-Based Parameterisation Techniques for Planar Multipatch
   Domains*.** [arXiv:2307.06265](https://arxiv.org/abs/2307.06265) — the companion. Has
   Radó–Kneser–Choquet, Winslow, the non-divergence system with $A$ from the metric tensor,
   the Cordes condition, Picard and Newton, the interior penalty, and the discrete-Hessian
   recovery. Everything in §4–5 of this tutorial.
2. **Budd, Huang and Russell, "Adaptivity with moving grids", *Acta Numerica* 18 (2009),
   111–241.** *Not hers* — the standard survey of r-adaptivity, equidistribution, and the
   optimal-transport/Monge–Ampère route to moving meshes. This is the background she
   assumes and does not cite, and it is the fastest way into §7.
3. **Marcinnó, Hinz, Buffa and Deparis, *A spline-based hexahedral mesh generator for
   patient-specific coronary arteries*.**
   [arXiv:2501.12965](https://arxiv.org/abs/2501.12965), *CMAME* 445 (2025) — the
   application, with the quality tables and the VMTK/Gmsh comparison.

For the non-divergence-form machinery itself, if you want it properly: Smears and Süli,
*SIAM J. Numer. Anal.* 51 (2013) 2088–2106, is the origin of the Cordes-condition finite
element theory.

---

## 11. Self-test

<details>
<summary>1. What is the talk actually about, and what is it not about?</summary>

**Mesh generation** — constructing valid, structured, spline-based meshes by solving PDEs,
and then moving their nodes optimally via optimal transport. It is *not* about isogeometric
approximation of solutions, not about finite element exterior calculus or discrete de Rham
complexes, not about defeaturing or a posteriori estimators, and not about h-adaptive
hierarchical splines — all of which are things Buffa is famous for and none of which she
mentions.
</details>

<details>
<summary>2. Why does she want a harmonic map, and why is the map inverted?</summary>

The Radó–Kneser–Choquet theorem: the harmonic extension of a boundary homeomorphism onto a
**convex** target is a diffeomorphism. The convex domain must be the *target*, and the
convex domain is the parametric one $\hat\Omega$. So the harmonic map runs
$\Omega \to \hat\Omega$, and the parametrization she wants,
$\mathbf{x}: \hat\Omega \to \Omega$, is its inverse. Solving for the inverse directly on
$\hat\Omega$ is what produces the non-divergence system.
</details>

<details>
<summary>3. Write the governing system and say what A is.</summary>

$A(\partial_\xi \mathbf{x}) : D^2 x_i = 0$ in $\hat\Omega$, with
$\mathbf{x} = \mathbf{F}$ on $\partial\hat\Omega$, where
$A = \begin{pmatrix} g_{22} & -g_{12}\\ -g_{12} & g_{11}\end{pmatrix}$ and
$g_{ij} = \partial_{\xi_i}\mathbf{x}\cdot\partial_{\xi_j}\mathbf{x}$ is the metric tensor.
Quasilinear, non-divergence form. $A$ is only piecewise regular because $\mathbf{x}$ is
only $C^0$ across patch interfaces.
</details>

<details>
<summary>4. State the Cordes condition and say what it means for this A.</summary>

$|A|_F^2/(\operatorname{tr}A)^2 \le 1/(n-1+\varepsilon)$ for some $\varepsilon \in (0,1]$.
Equivalently, with $\gamma = \operatorname{tr}A/|A|_F^2$, one has
$|\gamma A - I|_F \le \sqrt{1-\varepsilon} < 1$: after one scalar renormalization $A$ is a
uniform contraction from the identity, which is what makes the Banach fixed point close.
For this particular $A$, since
$(\operatorname{tr}A)^2 - |A|_F^2 = 2\det G = 2(\det J)^2$, the condition reads
$2(\det J)^2 \ge \varepsilon |A|_F^2$ — **the mesh does not fold.**
</details>

<details>
<summary>5. What is the Miranda–Talenti estimate and why does the discrete version need a jump term?</summary>

For $u \in H^2\cap H^1_0$ on a **convex** domain, $\|D^2u\| \le \|\Delta u\|$: two
integrations by parts give the identity $\int(\Delta u)^2 = \int|D^2u|^2$ for compactly
supported $u$, and convexity gives the boundary term the right sign in general. Discretely
the operators are only patchwise, and patchwise Hessian and patchwise Laplacian both
annihilate functions that differ by an affine map across an interface — the patches
"float". The jump term removes that kernel.
</details>

<details>
<summary>6. Describe both discretizations, and say which she prefers and why.</summary>

**Method A**: test against the patchwise Laplacian, mimicking the continuous inf-sup, plus
jump penalties on the gradient and Hessian with parameters $\mu_1,\mu_2$. Coercive in a
discrete $H^2$ norm — she has a theorem. Fourth-order operator, hence bad matrices, and two
free parameters.

**Method B**: define the discrete Hessian as the $L^2$ (Ritz) representation of the
distributional Hessian, obtained by integrating by parts twice and keeping jump-average
interface terms. Second-order, better conditioned, **parameter free**. Stability on charts
where $A$ jumps is **open**.

She prefers **B**, despite having no proof, because of the parameters and the matrices.
</details>

<details>
<summary>7. What does she do about the missing proof, and what exactly does it establish?</summary>

She localizes the missing step to a small, finite-dimensional local problem on a reference
chart, then computes its smallest singular value over configurations, coefficient values
and refinement levels, checking it never falls below a fixed positive threshold. That is a
**numerical certificate**, not a proof, and she says so. It establishes uniform
invertibility of the local problems over the enumerated set, which is the step the
classical argument supplies by assuming $A$ regular.
</details>

<details>
<summary>8. What is the definition of an optimal mesh, and what does optimal transport add?</summary>

Optimal = the interpolation error (the monitor function $\rho$) is **equidistributed** over
elements. In $d$ dimensions equidistribution is one scalar equation,
$\rho(\mathbf{x})\det J = \sigma$, for $d$ unknown functions — underdetermined. Quadratic
optimal transport supplies the remaining $d-1$ conditions by asking the mesh to move as
little as possible; Brenier's theorem then says the minimizer is $\nabla\phi$ with $\phi$
convex, giving $\rho(\nabla\phi)\det D^2\phi = \sigma$, a Monge–Ampère equation.
</details>

<details>
<summary>9. What is open in part two, and what is merely unimplemented?</summary>

**Open:** well-posedness of Monge–Ampère under the "boundary does not move but points slide
along it" Neumann condition — nonlinear when $\hat\Omega$ is a ball. She says so explicitly.
**Unimplemented / unknown:** the choice of monitor function for a genuine multi-physics
problem like the tokamak edge, where she says *"the concept of optimality goes back to I
don't know exactly what to do"*, and where strong anisotropy defeats a scalar isotropic
monitor. Not open mathematics — an unsolved modelling question.
</details>

<details>
<summary>10. What do the two halves have to do with each other?</summary>

They compose. Part one gives $\mathbf{x}_{\text{initial}} : \hat\Omega \to \Omega$, a valid
non-folding parametrization. Part two gives $\nabla\phi : \hat\Omega \to \hat\Omega$, a
redistribution of the parametric coordinates. The final mesh map is
$\mathbf{x}_{\text{initial}} \circ \nabla\phi$. They also share machinery: the Monge–Ampère
solver's inner Newton step is again a second-order non-divergence-form problem, solved with
Method B from part one.
</details>

---

## 12. Note on the tutorial process

**Rule 1 fired hard, and the brief's anchors were wrong.** The brief predicted isogeometric
analysis (CAD space = analysis space), finite element exterior calculus, discrete
differential forms, defeaturing, and a posteriori estimators, and suggested anchoring on
structure-preserving discretization and de Rham cohomology. **None of that is in the talk.**
The talk is mesh generation: inverse harmonic maps in part one, optimal transport in part
two. I rejected both suggested anchors and used the two the speaker hands over from the
podium — Radó–Kneser–Choquet ("mathematics gives me the answer") and Brenier — and wrote
§2.1 to say explicitly what is absent, so the reader knows those topics exist and knows
this talk is not about them.

Her reputation predicted the **toolbox** (splines, multipatch, isogeometric machinery) but
not the **subject**. That is a milder version of the Kontorovich failure, and it still cost
the brief every one of its anchor candidates.

**Difficulty.** Split, and inverted, as the template prescribes at Tier 0–1. The frame — the
simulation workflow, interpolation estimates, Newton and Picard, optimal transport, mesh
quality — is difficulty 1 for this reader and is compressed into the one-page §2. The
non-divergence-form theory (Cordes, Miranda–Talenti, discrete Hessian) is difficulty 2: an
afternoon of definitions, not a new field. The length went to §4–7 and §9.

**Names and caption corrections.**

| Caption | Correct | Basis |
|---|---|---|
| "the **action**" (throughout §5–7) | the **Hessian** | context; the entire method is a discrete Hessian |
| "the **brainy** theorem" | **Brenier**'s theorem | context; standard OT result |
| "a convex functional of a complex potential" | the gradient of a **convex potential** | Brenier's theorem |
| "inf **sub** condition" | **inf-sup** condition | standard |
| "**failed** fields modeling" | **phase-field** modelling | she says "phase fields models" correctly moments later |
| "Suzanne Brenner" | **Susanne C. Brenner** (LSU) | session chair; published name |
| "quasi-linear PDEs in the **divergence** form" | **non-divergence** form | companion paper; her own later usage |
| "Willis circle" | **circle of Willis** | anatomy |
| "Swiss corns" / "cone" | **alphorn** (*cor des Alpes*) | context: hand-made, played in the Swiss Alps |
| "Braginsky" | **Braginskii** | drift-reduced Braginskii model |
| "L minus one where L is the degree" | $p-1$, $p$ = degree | standard spline notation |

**The one substantive correction, and it matters more than any spelling.** The captions
render **Hessian** as **"action"** consistently, in every sentence describing the method:
"the discrete action", "the action piece by piece", "I can control the patch by patch
action with the Laplace". Read literally the talk is incoherent — an "action" that is
controlled by a Laplacian and appears inside a determinant is not a thing. It is the
Hessian throughout, confirmed by the companion paper's discrete-Hessian recovery section
and by the Miranda–Talenti estimate, which is precisely a Hessian-versus-Laplacian bound.
Anyone reading the raw transcript will be lost at exactly this point.

**Reconstructed, and how to verify.**

- The **Cordes condition inequality** and the $|\gamma A - I|_F \le \sqrt{1-\varepsilon}$
  computation (§3.3): restored from Smears and Süli (2013), not from the slide. Verify by
  expanding $|\gamma A - I|_F^2$; the algebra is in the text.
- The identity $(\operatorname{tr}A)^2 - |A|_F^2 = 2(\det J)^2$ for her $A$ (§4.3): **my
  derivation**, combining the companion paper's $A$ with the standard Cordes condition. She
  does not state it aloud. Verify by direct expansion.
- The **square and ball Neumann conditions** (§7.4): the general condition is hers; the two
  special cases are my one-line derivations from "boundary maps to boundary". She shows the
  ball case on a slide; the captions carry no formula.
- The **Miranda–Talenti two-line derivation** (§3.2): classical, reproduced so the reader
  can check it. She states only the conclusion.
- **Radó–Kneser–Choquet** and **Winslow** are named from the **companion paper**, not from
  the podium. She says "one of the fundamental theorems of analysis" without a name.

**Gaps, with impact ratings.**

| Gap | Impact |
|---|---|
| Exact discrete $H^2$ norm, penalty scaling, and admissible $\mu_1,\mu_2$ in the Method A coercivity theorem (§5.1) | **Moderate** — the theorem's shape is fully stated and standard; the exponents matter only for implementation. Companion eq. (33) supplies the gradient-jump half. |
| Exact form of the discrete Hessian $H_h$ and of the discrete Monge–Ampère system (§5.3, §7.5) | **Moderate** — described precisely in words (integration by parts twice, jump-average interface terms, $L^2$ projection), never displayed. Peruso [arXiv:2607.15024](https://arxiv.org/abs/2607.15024) has the analogous Dirichlet construction. |
| The weighted nonlinear residual functional and the operator $\tau$ in it (§4.4) | **Low** — a device to reach a linearization; both linearizations are stated. |
| The enrichment operator in the discrete Miranda–Talenti proof (§5.1) | **Low** — she declines to give it, deliberately, and so do I. Standard in $C^0$-IP analysis. |
| The 12,000 / 1,000 / 99% cohort figures (§6.1) | **Low** — quoted as spoken, ambiguous phrasing flagged; the published paper's per-case tables are given alongside. |
| The interpolation estimate's exact exponents (§2) | **Low** — she calls it "the easiest one"; only the structure is used. |

Two things I am deliberately **not** treating as gaps because they are content: the
**well-posedness of the nonlinear Neumann Monge–Ampère problem**, which she calls open, and
the **stability of Method B on charts where $A$ jumps**, which she also calls open. Those
are the talk's honest statements about the limits of the theory, not caption failures.

**Unverified.** The alphorn maker's first name, rendered "Gerard" in the captions. The
photograph is credited to *Le Temps*. I could not find the article and have not guessed a
surname or a spelling.

**No companion for half the talk.** Part two exists only as spoken words plus slides. I have
labelled Budd–Huang–Russell and Peruso every time as **other people's work** supplying
background, never as hers, because presenting them otherwise would misattribute an
unpublished research programme.

**Cross-reference.** The optimal-transport background — Wasserstein-2, Benamou–Brenier,
Brenier's polar factorization — is built at length in
`summaries/geometric-concepts-pde-otto.md` and is not rebuilt here.
