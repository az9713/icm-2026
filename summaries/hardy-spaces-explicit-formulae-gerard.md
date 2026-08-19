---
title: "Hardy Spaces of Holomorphic Functions and Explicit Formulae for a Class of Integrable Partial Differential Equations"
speaker: Patrick Gérard (Université Paris-Saclay)
source: https://www.youtube.com/watch?v=7eLznYeQm7k
video_id: 7eLznYeQm7k
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: "proceedings exists but is not retrievable — https://doi.org/10.1137/25M1805497 (SIAM returns 403); worked from arXiv:2212.03139 and arXiv:2601.10488"
transcript: ../transcripts/7eLznYeQm7k_transcript.txt
difficulty_for_you: 2/5
reading_time: ~55 min
---

# Hardy Spaces of Holomorphic Functions and Explicit Formulae for a Class of Integrable Partial Differential Equations — Patrick Gérard

**Field:** dispersive PDE and integrable systems, done with harmonic analysis. Specifically:
the Benjamin–Ono equation on the line, its Lax pair on the Hardy space of the upper
half-plane, an explicit solution formula, and the proof of the soliton resolution
conjecture that the formula makes possible.

**Difficulty against your background: 2/5.** This is the closest talk in the playlist to
your training, and it is not close by accident — every ingredient is something you own.
Hardy space of the upper half-plane, Paley–Wiener, the Cauchy integral formula, the
Hilbert transform, the Dirichlet-to-Neumann map for the Laplacian on a half-plane,
unbounded self-adjoint operators and their domains, the spectral theorem with its point
and absolutely continuous parts, resolvents, Lax pairs and isospectral flows, solitons,
dispersive decay at rate $t^{-1/2}$. There is exactly **one** object in the talk that is
not already in your toolbox — an unbounded operator Gérard writes $X^*$ — and exactly
**one** mechanism built from it. So this tutorial takes the Tier-0 inversion: §2 is a
one-page calibration you can skim, and the length goes to $X^*$, the explicit formula, and
the argument that turns the formula into a theorem.

**What this tutorial builds.** The operator $X^*$ and the functional $I_+$; the
"Cauchy-like" representation formula for Hardy-space functions; the deformation of that
formula that solves Benjamin–Ono; and the mechanism Gérard calls *soliton fishing*, which
converts the spectral decomposition of the Lax operator into the asymptotic decomposition
of the solution. It does not build the Hardy space, the Lax pair, or the notion of a
soliton — see §2 for why not.

**A note on sources — read this before you trust any formula below.**

- **The ICM proceedings paper exists but I could not read it.** It is a SIAM chapter,
  DOI [10.1137/25M1805497](https://doi.org/10.1137/25M1805497), with the same title as the
  lecture. `epubs.siam.org` returned **HTTP 403** to my fetch; I confirmed that directly,
  not on report. No abstract was retrievable. Gérard refers to it twice from the podium —
  "you have proceedings, so you can check that the proceedings are containing many more
  references" — and says the proceedings also cover the **zero-dispersion limit**, which
  the talk itself does not. So there is content in the proceedings that is not in this
  document, and I cannot tell you what it is.
- **The natural companion is located but also not retrievable.** Patrick Gérard,
  *Lectures on integrable equations of Benjamin–Ono type*, **EMS Surveys in Mathematical
  Sciences** (2026), published 7 January 2026. It is cited as `[Gér26]` inside the
  soliton-resolution paper below, as the reference "for the integrable structure of the
  Benjamin–Ono equation". There is no arXiv version and the EMS text is behind the
  journal. **This is a companion, not the proceedings paper, and I have not read it.**
  I name it because it is the right next thing for you to read (§11), not because anything
  here comes from it.
- **What I actually worked from, in full text, besides the transcript**, is the primary
  literature for the two results the talk is built on:
  1. **P. Gérard, *An explicit formula for the Benjamin–Ono equation*,** Tunisian J. Math.
     **5** (2023) 593–603, [arXiv:2212.03139](https://arxiv.org/abs/2212.03139). Read in
     full from Gérard's own page. This is the "theorem I proved three years ago" in the
     talk. Every formula in §3 and §4.5 comes from here.
  2. **L. Gassot, P. Gérard, P. D. Miller, *A proof of the soliton resolution conjecture
     for the Benjamin–Ono equation*,**
     [arXiv:2601.10488](https://arxiv.org/abs/2601.10488), v1 15 January 2026, v2 6 August
     2026, 29 pages. Read in full. This is the theorem the talk announces. Everything in
     §4.3, §5 and §6 comes from here.
  These are **primary literature for specific theorems**, cited inline, and they are not a
  substitute for the proceedings paper.
- **A notation warning that matters when you go to the sources.** The same operator is
  called three things. The talk calls it $X^*$. The 2022 explicit-formula paper calls it
  $G$. The soliton-resolution paper calls it $X$ in the printed PDF and $X^*$ in the arXiv
  HTML of v2. It is one operator: the adjoint, on the Hardy space, of multiplication by
  $x$. I use the talk's $X^*$ throughout.
- **Formulas in this document are cross-checked, not transcribed once.** The captions carry
  no mathematics at all — everything was on slides. I recovered the displays from the two
  papers, and where a PDF text extraction could have silently dropped a symbol (it dropped
  every $\pi$, and it turned $X^*$ into $X$), I closed the constant by an independent
  one-soliton consistency computation. That check, and what it verified, is written out in
  §13.

**Names.** The auto-captions destroy most proper nouns, including "cubic Szegő", which
becomes "cubic Zakharov–Shabat" at one point. Full correction table in §13.

---

## 1. What is at stake

Take a nonlinear dispersive wave equation. Give it initial data. Wait a long time. What do
you see?

The physicists' answer, conjectured since the 1960s and stated in Terence Tao's book on
dispersive equations, is called the **soliton resolution conjecture**, and it is one
sentence:

> Every solution eventually looks like a finite number of solitons, travelling at
> different speeds and therefore separating from one another, plus a linear radiation term
> that spreads out and decays.

That is a strong claim about a nonlinear system. It says the long-time dynamics has a
**normal-mode decomposition** — a discrete part that keeps its shape forever and a
continuous part that disperses — even though superposition fails and no eigenfunction
expansion is available.

For the **Korteweg–de Vries** equation, this was proved decades ago by inverse scattering:
you transform the data into scattering data for a Schrödinger operator, the nonlinear flow
becomes linear motion of that scattering data, and you transform back, using a
Riemann–Hilbert problem and the Deift–Zhou nonlinear steepest-descent method to read off
the asymptotics.

For **Benjamin–Ono** this machinery fails, and it fails for a structural reason. The Lax
operator of Benjamin–Ono is not a differential operator. It contains a **non-local** term —
a Toeplitz operator on a Hardy space. As Gassot, Gérard and Miller put it in the paper, the
Cauchy problem on the line

> "lacks a justified inverse-scattering transform formulated as any kind of Riemann–Hilbert
> problem, making the large-time asymptotics inaccessible to the Deift–Zhou method."

So the standard route is not merely hard here. It is closed. **Name that explicitly to
yourself now**, because if you have seen integrable long-time asymptotics before, you have
seen it through Riemann–Hilbert, and this talk does not use it and cannot.

What Gérard does instead is the thing you would not expect to be possible. He writes down
an **explicit formula** for the solution of the nonlinear PDE, at every time, in terms of
the initial data — and then reads the long-time behaviour off the formula by elementary
means. The formula is short enough to fit on one line, and it is essentially the Cauchy
integral formula with one operator inserted.

His own summary of the arc, from the last slide:

> "We provide new explicit representation formula for a class of integrable PDEs involving
> non-local terms, with applications to long-time description of the solution."

The two things worth carrying out of this talk are: (i) the specific formula, because it is
beautiful and because it is *computable*; and (ii) the observation that the obstruction —
non-locality — is exactly what made the new method necessary, and the new method is better
than the one it replaced.

---

## 2. Calibration: what you can skip

Everything in this section you already have. Skim it to confirm we are using the same
words and normalizations, then go to §3, which is where the new material starts.

**The equation.** Benjamin–Ono, introduced by T. Brooke Benjamin in 1967 to model long
one-way internal gravity waves in a two-layer fluid of **infinite** depth — the opposite
regime to KdV's shallow water. In Gérard's normalization:

$$\partial_t u \;=\; \partial_x\big(|D|u - u^2\big), \qquad u(t,x)\in\mathbb{R}$$

Here $|D|$ is the Fourier multiplier with symbol $|\xi|$, so $|D| = H\partial_x$ where $H$
is the Hilbert transform, $\widehat{Hf}(\xi) = -i\,\mathrm{sgn}(\xi)\hat f(\xi)$. Expanded,
$\partial_t u + 2uu_x - Hu_{xx} = 0$. Gérard's Fourier convention throughout is
$\hat f(\xi)=\int e^{-i\xi x}f(x)\,dx$, $f(x)=\frac{1}{2\pi}\int e^{i\xi x}\hat f(\xi)\,d\xi$.

One remark from the podium worth keeping, because it tells you where the non-locality comes
from physically: $|D|$ **is the Dirichlet-to-Neumann operator of the Laplacian on the upper
half-plane**. Solve $\Delta \phi = 0$ above the line with boundary value $f$; then the
normal derivative at the boundary is $|D|f$. The equation is derived from Euler for an
irrotational incompressible flow, so harmonic functions in a half-plane are exactly what
you should expect to appear.

**Well-posedness, and why he does not dwell on it.** Gérard works on the Fréchet space
$H^\infty = \{f\in C^\infty(\mathbb{R},\mathbb{R}) : f \text{ and all derivatives in } L^2\}$.
Local existence is Kato's quasilinear iteration; globalization is by conservation laws, of
which an integrable equation has infinitely many, and they control every $H^s$ norm. So all
those norms are not merely finite but **uniformly bounded in $t$**. The classical reference
is Saut 1979 for $H^2$; the sharp modern result is Killip–Laurens–Vian, *Invent. Math.* 236
(2024), giving a continuous flow on $H^s(\mathbb{R})$ for every $s>-1/2$. None of this is
the point of the talk. The point begins after you know the solution exists forever and
stays bounded.

**Hardy space.** $L^2_+(\mathbb{R}) = \{f \in L^2 : \operatorname{supp}\hat f \subset
[0,\infty)\}$. Harmonic analysts call it $H^2$ of the upper half-plane; Gérard writes
$L^2_+$ because $H$ is already taken by Sobolev spaces. By Paley–Wiener these are exactly
the boundary values of functions holomorphic on $\mathbb{C}_+ = \{\operatorname{Im}z>0\}$
with $\sup_{y>0}\int_{\mathbb{R}}|f(x+iy)|^2dx<\infty$, and the extension is

$$f(z) \;=\; \frac{1}{2\pi}\int_0^{\infty} e^{iz\xi}\,\hat f(\xi)\,d\xi , \qquad z\in\mathbb{C}_+$$

which converges beautifully because $e^{iz\xi}$ decays exponentially in $\xi$ when
$\operatorname{Im}z>0$.

$\Pi$ denotes the orthogonal projector $L^2 \to L^2_+$: on the Fourier side it truncates to
$\xi>0$; on the $x$ side it is the Cauchy integral. Gérard calls it the **Szegő
projector** ("Cauchy or Riesz or Szegő — I prefer Szegő").

One line you will use constantly: if $u$ is **real-valued**, then $u = \Pi u +
\overline{\Pi u}$. So $\Pi u$ carries all the information, and $\Pi u$ is a holomorphic
function on the upper half-plane. **The unknown of the whole talk is $\Pi u$, not $u$.**

**Toeplitz operators.** For $b \in L^\infty$, multiplication by $b$ kicks you out of the
Hardy space, so project back:

$$T_b f \;=\; \Pi(bf), \qquad f \in L^2_+$$

Bounded, with $\|T_b\| = \|b\|_{L^\infty}$; self-adjoint iff $b$ is real. Introduced by Otto
Toeplitz — the talk says "1915 or something like this"; the founding paper is Math. Ann.
**70** (1911).

**Lax pair.** The one-sentence version, which is exactly right and is the one Gérard uses:
a nonlinear evolution is a **Lax pair** if it is equivalent to an *isospectral deformation*
of a family of operators. You get two operators $L_u$ (self-adjoint) and $B_u$
(skew-adjoint), and the PDE holds **if and only if**

$$\frac{d}{dt} L_{u(t)} \;=\; \big[\,B_{u(t)},\, L_{u(t)}\,\big]$$

Then solve $U'(t) = B_{u(t)}U(t)$, $U(0)=\mathrm{Id}$. Since $B$ is skew-adjoint, $U(t)$ is
**unitary**, and

$$L_{u(t)} \;=\; U(t)\, L_{u_0}\, U(t)^{*}$$

so the spectrum of $L_{u(t)}$ never moves. Gérard notes this is Lax's own proof from the KdV
case, transplanted unchanged. Peter Lax introduced Lax pairs in 1968, one year after
Gardner, Greene, Kruskal and Miura solved KdV; the talk is dedicated to him (he died in
2025) and to Claude Bardos (4 April 1940 – 16 June 2026).

**Solitons.** Travelling waves $u(t,x)=R(x-ct)$ that keep their shape. For Benjamin–Ono,
Amick and Toland (*Acta Math.* 1991) proved these are *exactly*

$$R_p(y) \;=\; \frac{2\operatorname{Im}p}{|y+p|^{2}}, \qquad c_p \;=\; \frac{1}{\operatorname{Im}p}, \qquad p\in\mathbb{C}_+$$

so a **rational** function, not a hyperbolic secant — this is the algebraic soliton, first
written down in Benjamin's 1967 paper. The peak height is $2/\operatorname{Im}p = 2c_p$:
**taller means faster**, so in a multi-soliton configuration the tallest runs ahead. Gérard's
line: "exactly the opposite of the group photo."

**Dispersive decay.** The linearization of Benjamin–Ono at $u=0$ is $\partial_t w =
\partial_x|D|w$, which on the Hardy component has Fourier symbol $i\xi^2$ — i.e. it *is* a
free Schrödinger equation on $\xi>0$. So its solutions decay in $L^\infty$ like $t^{-1/2}$,
by the standard dispersive estimate. You verify this in §9.3.

That is the entire prerequisite list. Everything in §3 onward is new.

---

## 3. The one new object: $X^*$, the adjoint of multiplication by $x$

Gérard stops the talk to introduce this and says so: "I will require all your attention
because this is something new." He is right that it is the pivot, and it is the one place
where a reader with your background has to actually learn something.

### 3.1 A symmetric operator whose adjoint is strictly bigger

Consider multiplication by $x$ on the Hardy space $L^2_+(\mathbb{R})$:

$$Xf(x) = xf(x), \qquad \mathrm{Dom}(X) = \{f \in L^2_+ \;:\; xf(x)\in L^2\}$$

On the full space $L^2(\mathbb{R})$ this operator is self-adjoint — it is the position
operator, and you know its spectral theory completely. **On the Hardy space it is not.** It
is symmetric, but its adjoint has a strictly larger domain.

That is not a technicality; it is the entire mechanism. Here is why it happens.

If $f \in L^2_+$ and $xf(x)$ is also in $L^2$, then $f\in L^1$, so $\hat f$ is continuous by
the Riemann–Lebesgue lemma. But $\hat f$ is supported in $[0,\infty)$, hence vanishes for
$\xi<0$, hence — being continuous — must satisfy $\hat f(0^+)=0$. So membership in
$\mathrm{Dom}(X)$ forces the Fourier transform to *vanish at the edge of its support*.

Most Hardy-space functions do not do that. $\hat f$ has a **jump** at $\xi=0$. Define the
size of that jump:

$$I_+(f) \;:=\; \hat f(0^+)$$

Gérard's mnemonic: "$I$ is for integral and $+$ is for coming from $\xi$ positive. But it is
not an integral, because $f$ is not integrable." That is exactly the point — it looks like
$\int f$, it would *be* $\int f$ if $f$ were integrable, and the whole subject lives in the
gap between those two statements.

**The adjoint.** $X^*$ has domain

$$\mathrm{Dom}(X^*) \;=\; \{\, f\in L^2_+ \;:\; \hat f|_{(0,\infty)} \in H^1(0,\infty)\,\}$$

and acts, on the Fourier side, as

$$\widehat{X^*f}(\xi) \;=\; i\,\frac{d}{d\xi}\hat f(\xi), \qquad \xi>0$$

which is just "multiplication by $x$ is $i\,d/d\xi$ in Fourier", restricted to the half-line.
Transforming back gives the description that actually gets used:

$$\boxed{\;X^*f(x) \;=\; x f(x) \;+\; \frac{I_+(f)}{2i\pi}\;}$$

Read that as: **$X^*$ is multiplication by $x$, renormalized by a constant**. You cannot
multiply a Hardy function by $x$ and stay in $L^2$, but you can if you subtract off the right
constant, and the right constant is the jump $I_+(f)$ divided by $2i\pi$. Gérard's phrasing:
"of course $xf(x)$ may not be in $L^2$, but if I renormalize by the constant, then it is."

> **The sentence to remember.** "The strong difference between the domain of $X$ and the
> domain of $X^*$ is precisely this constant $\lambda$. And this is the constant in which the
> whole dynamics of Benjamin–Ono is hidden."

If you want a slogan: *the defect of self-adjointness is not a defect, it is the state
variable.*

### 3.2 The example that generates everything

Take $p\in\mathbb{C}_+$ and

$$f(x)\;=\;\frac{1}{x+p}$$

This is in the Hardy space: its only pole is at $x=-p$, which lies in the **lower** half
plane, so $f$ extends holomorphically to $\mathbb{C}_+$, and it is $O(|x|^{-1})$, hence in
$L^2$. Now compute:

$$x f(x) \;=\; \frac{x}{x+p} \;=\; 1 - \frac{p}{x+p}$$

which is not in $L^2$ because of the constant $1$. Subtract it — that is the
renormalization — and you get $-p\,f$. So

$$X^* f \;=\; -p\,f, \qquad I_+(f) \;=\; -2i\pi$$

**$f$ is an eigenfunction of $X^*$**, with eigenvalue $-p$ in the upper... in fact $-p$ lies
in the lower half-plane. Gérard: "you know, it's very far from being in the domain of $X$.
But these are precisely the guys which are interesting to us."

Why interesting? Because of a two-line computation you should do once:

$$\frac{i}{y+p} + \overline{\left(\frac{i}{y+p}\right)} \;=\; \frac{i(\bar p - p)}{|y+p|^2} \;=\; \frac{2\operatorname{Im}p}{|y+p|^2} \;=\; R_p(y)$$

That is the soliton profile from §2. So

$$\Pi R_p(z) \;=\; \frac{i}{z+p}$$

**The eigenfunctions of $X^*$ are exactly the Hardy projections of the soliton profiles.**
The one genuinely new operator in the talk has, as its eigenvectors, the one family of
special solutions the whole subject is about. That is not a coincidence and it is the reason
the method works.

### 3.3 The Cauchy-like representation formula

Now the payoff, and it is the anchor for the entire lecture.

> **Proposition.** For every $z\in\mathbb{C}_+$, the operator $X^*-z$ is a bijection from
> $\mathrm{Dom}(X^*)$ onto $L^2_+$, and for every $f\in L^2_+$,
> $$f(z) \;=\; \frac{1}{2i\pi}\, I_+\!\big[\,(X^*-z)^{-1}f\,\big]$$

*(Gérard, arXiv:2212.03139, §3, stated there with $G$ for $X^*$.)*

Stare at this next to the Cauchy integral formula,

$$f(z) \;=\; \frac{1}{2i\pi}\oint \frac{f(\zeta)}{\zeta - z}\,d\zeta$$

and the correspondence is term by term. The prefactor $1/2i\pi$ is the same. The kernel
$1/(\zeta-z)$ has become the resolvent $(X^*-z)^{-1}$ — which is exactly right, because for
a plain multiplication operator the resolvent *is* multiplication by $1/(x-z)$. And the
contour integral $\oint\cdots d\zeta$ has become $I_+$, the thing that "is like an integral
but is not an integral". Gérard says this from the podium: "I called it Cauchy-like because
it starts with $1/2i\pi$, then it comes with an $I_+$ which is something like an integral,
but it's not an integral."

**This is your anchor, and the speaker handed it to you.** Everything that follows is a
deformation of the Cauchy integral formula.

He also gives a second form, which is what the proof actually uses. Let

$$\chi_\varepsilon(x) \;=\; \frac{1}{1-i\varepsilon x} \;\in\; L^2_+$$

be an "approximation of one". Then $I_+(g) = \lim_{\varepsilon\to 0}\langle g,
\chi_\varepsilon\rangle$, so

$$f(z) \;=\; \lim_{\varepsilon\to 0}\ \frac{1}{2i\pi}\,\big\langle (X^*-z)^{-1}f,\ \chi_\varepsilon \big\rangle$$

Writing $I_+$ as a limit of inner products is what makes it possible to move unitary
operators around inside it. Hold that thought until §4.6.

**The proof is three lines, and Gérard does it live** ("So how do you prove this
proposition? Exercise. So let's do this exercise."). Solve $(X^*-z)g=f$. By the description
of $X^*$ this reads $xg(x) + \lambda - zg(x) = f(x)$ for some constant $\lambda$, i.e.

$$(x-z)\,g(x) \;+\; \lambda \;=\; f(x)$$

Both sides are boundary values of functions holomorphic on $\mathbb{C}_+$, so the identity
persists there. Put $x=z$: the first term dies, and $\lambda = f(z)$. Therefore

$$g(x)\;=\;\frac{f(x)-f(z)}{x-z}$$

which is manifestly in $L^2_+$ and in $\mathrm{Dom}(X^*)$, and $\lambda = I_+(g)/(2i\pi)$ by
the definition of $X^*$. Combine: $f(z) = I_+(g)/(2i\pi)$. Done.

Notice what that computation *is*: it is the divided difference $\frac{f(x)-f(z)}{x-z}$, the
same object that appears in Newton interpolation and in every "remove the singularity"
argument you have ever run. The renormalizing constant of $X^*$ is precisely the value
$f(z)$ that makes the divided difference regular.

---

## 4. The talk, rebuilt

### 4.1 The Lax pair for Benjamin–Ono

Everything is on the Hardy space $L^2_+(\mathbb{R})$. For $u$ real-valued and smooth enough,
define

$$L_u \;=\; D - T_u, \qquad D := -i\frac{d}{dx}, \qquad \mathrm{Dom}(L_u)=H^1_+ = H^1\cap L^2_+$$

$$B_u \;=\; i\big(T_{|D|u} - T_{u^2}\big)$$

$L_u$ is self-adjoint and semi-bounded; $B_u$ is bounded and skew-adjoint. $L_u$ is a
"Schrödinger-like" operator in the sense that it is a free part $D$ minus a potential — but
the potential enters through a **Toeplitz** operator, i.e. multiply then project, which is
non-local. That single feature is what kills Riemann–Hilbert (§1).

> **Theorem (Nakamura; Bock–Kruskal; Ablowitz–Fokas, late 1970s–1983).** $u$ solves
> Benjamin–Ono **if and only if** $\frac{d}{dt}L_{u(t)} = [B_{u(t)}, L_{u(t)}]$.

Gérard stresses the "if and only if" from the podium. The paper (arXiv:2212.03139,
Theorem 2) states only the forward direction; the equivalence is standard and is what he
says aloud. *(Where the talk and the paper differ in strength, I am quoting the talk here
and telling you so.)*

There is a second, less-quoted consequence he needs, obtained by letting the Lax identity
act on the approximation of one $\chi_\varepsilon$: the equation can be **rewritten as an
evolution for $\Pi u$ itself**,

$$\partial_t \,\Pi u \;=\; i\,L_u^2(\Pi u) \;+\; B_u(\Pi u)$$

*(arXiv:2212.03139, §3, displayed there as a chain of identities rather than as a numbered
equation.)* This is the form that makes the conjugation trick in §4.6 work, and it is the
reason the unknown must be $\Pi u$ and not $u$.

### 4.2 The conjecture, stated for this equation

The soliton resolution conjecture, made concrete: with $c_{p} = 1/\operatorname{Im}p$ and
$R_p$ as in §2, and with $w(t)=e^{t\partial_x|D|}w(0)$ denoting the flow of the linearized
equation $\partial_t w = \partial_x |D| w$, one expects

$$u(t,\cdot) \;-\; \sum_{j=1}^{N} R_{p_j}(\cdot - c_{p_j}t) \;-\; e^{t\partial_x|D|}u_\infty^{\pm} \;\longrightarrow\; 0 \qquad (t\to\pm\infty)$$

Two features to notice before the theorem. First, the solitons all have **different**
velocities, so they physically separate — they stop interacting, which is why a sum of
travelling profiles can be asymptotically exact. Second, the radiation term decays in
$L^\infty$ like $t^{-1/2}$, so you see it less and less, but it **carries energy** and cannot
be dropped: "it's very important to have them, otherwise the theorem is wrong except for
very, very special solutions."

### 4.3 The theorem

> **Theorem (Gassot–Gérard–Miller 2026, arXiv:2601.10488, Thm 1.1).** Let $u_0\in
> H^1(\mathbb{R})$ be real-valued with $xu_0 \in H^1(\mathbb{R})$, and suppose there exist
> $c_0\in\mathbb{R}$ and $v_0\in L^2(\mathbb{R})$ with
> $$x^2u_0(x) \;=\; c_0 + v_0(x)$$
> Then there exist an integer $N\ge 0$, points $p_1,\dots,p_N\in\mathbb{C}_+$ with
> $\operatorname{Im}(p_1)<\cdots<\operatorname{Im}(p_N)$, and real-valued
> $u_\infty^{\pm}\in H^1(\mathbb{R})$ such that
> $$\Big\| u(t,\cdot) - \sum_{j=1}^N R_{p_j}(\cdot - c_{p_j}t) - e^{t\partial_x|D|}u_\infty^{\pm}\Big\|_{H^1} \longrightarrow 0 \quad\text{as } t\to\pm\infty$$

**Talk versus paper, explicitly.** From the podium Gérard states this with $u_0 \in
H^\infty$, $xu_0 \in H^\infty$, and convergence in $H^\infty$ — that is, every $L^2$ norm of
every derivative goes to zero. The paper states the $H^1$ version above. Both are true; the
talk's version is stronger convergence under a stronger hypothesis, and is the natural
statement for a smooth-data audience. I quote the paper's hypotheses because they are the
published ones. The decay condition $x^2u_0 = \text{const} + L^2$ is the same in both, and
Gérard flags it as possibly relaxable but flags $xu_0$ as **not**: "This is the crucial
condition. If you don't put this thing, the statement is wrong."

The hypothesis class is generous enough to be interesting: it contains every Schwartz
function, every finite sum of soliton profiles, and more generally every real rational
$u_0\in L^2$ with $xu_0\in L^2$.

### 4.4 The explicit formula

Here is the object the whole talk is built to deliver.

> **Theorem (Gérard 2023, Tunis. J. Math. 5, 593–603; arXiv:2212.03139, Thm 4).** Let $u\in
> C(\mathbb{R},H^2_r(\mathbb{R}))$ solve Benjamin–Ono with $u(0)=u_0$. Then $u = \Pi u +
> \overline{\Pi u}$, and for every $t\in\mathbb{R}$ and $z\in\mathbb{C}_+$,
> $$\boxed{\;\Pi u(t,z) \;=\; \frac{1}{2i\pi}\, I_+\!\Big[\big(X^{*} - 2t\,L_{u_0} - z\big)^{-1}\,\Pi u_0\Big]\;}$$

Compare with the Cauchy-like formula of §3.3. **The only change is $X^* \rightsquigarrow X^*
- 2tL_{u_0}$.** Time enters the solution of a nonlinear PDE by *shifting one operator inside
one resolvent*, and the shift is linear in $t$.

Three things to appreciate.

**(a) The right-hand side involves only the initial datum.** $\Pi u_0$ appears twice — once
linearly, as the vector the operator acts on, and once inside $L_{u_0}$, nonlinearly. Gérard:
"you know that $u$ depends nonlinearly on $u_0$, but here it tells you *how* nonlinearly it
depends." That decomposition — a nonlinear dependence confined to a resolvent, a linear
dependence in the vector — is precisely what makes the asymptotic analysis in §5 possible.
You decompose the vector spectrally with respect to the operator, and each piece can be
handled separately.

**(b) The resolvent exists, and is bounded uniformly.** For $z\in\mathbb{C}_+$, the operator
$-i(X^*-2tL_{u_0})$ is **maximally dissipative** (Gérard proves it on the Fourier side; the
$L^\infty\cap L^2$ perturbation by $T_{u_0}$ is skew-adjoint and bounded, so it preserves the
property). Hence $(X^*-2tL_{u_0}-z)^{-1}$ is a bounded operator with norm at most
$1/\operatorname{Im}z$, uniformly in $t$. *(The existence and maximal dissipativity are the
paper's; the resolvent bound $1/\operatorname{Im}z$ is the standard consequence and I am
stating it because §5 needs uniformity in $t$ — labelled as my inference from the paper's
statement.)*

**(c) It extends past smooth data.** Because maximal dissipativity is all that is needed,
the formula still makes sense for $u_0 \in L^\infty\cap L^2_r$, which is how the flow map gets
extended to $H^s(\mathbb{R})$, $s>-1/2$.

For orientation, the **torus** version, which came first (same paper, Thm 3): there
$L^2_+(\mathbb{T})$ has a shift operator $S=T_{e^{ix}}$, and

$$\Pi u(t,z) \;=\; \big\langle (\mathrm{Id} - z\,e^{it}e^{2itL_{u_0}}S^{*})^{-1}\Pi u_0 \,\big|\, 1\big\rangle, \qquad z\in\mathbb{D}$$

Same shape: a geometric series in a shifted operator, paired against a distinguished vector.
On the circle the distinguished vector is the constant function $1$; on the line there is no
constant function in $L^2$, and $I_+$ is what replaces pairing against it. That is the whole
difficulty of the line case in one sentence, and it is why $X^*$ had to be invented.

### 4.5 How the formula is proved

Gérard gives the proof in about four minutes, and it is worth following because the move is
reusable.

**Step 1 — write the target as an inner product.** By §3.3,

$$\Pi u(t,z)\;=\;\lim_{\varepsilon\to0}\frac{1}{2i\pi}\big\langle (X^*-z)^{-1}\Pi u(t),\ \chi_\varepsilon\big\rangle$$

**Step 2 — insert a unitary and do nothing.** Let $U(t)$ solve $U'=B_{u(t)}U$, $U(0)=\mathrm{Id}$.
Apply $U(t)^*$ to *both* slots of the inner product. Nothing changes — that is what unitary
means — and insert $U(t)U(t)^* = \mathrm{Id}$ inside the resolvent:

$$\Pi u(t,z)\;=\;\lim_{\varepsilon\to0}\frac{1}{2i\pi}\Big\langle \big(U(t)^*X^*U(t)-z\big)^{-1} U(t)^*\Pi u(t),\ U(t)^*\chi_\varepsilon\Big\rangle$$

Gérard, delivering this: "It seems to be a little bit complicated because we don't know any
of these guys. But in fact we are going to see that we know everything in terms of the data."

**This is the whole trick.** You have changed frame — moved into the frame co-rotating with
the Lax flow — and in that frame each of the three unknown objects turns into something
expressed purely in $u_0$ and $L_{u_0}$.

**Step 3 — identify the three objects.** Each is a short ODE computation using
$U(t)^*L_{u(t)} = L_{u_0}U(t)^*$ (isospectrality) plus the rewritten equation of §4.1:

| object | becomes |
|---|---|
| $U(t)^*\,\Pi u(t)$ | $e^{itL_{u_0}^2}\,\Pi u_0$ |
| $U(t)^*\chi_\varepsilon$ | $e^{itL_{u_0}^2}\chi_\varepsilon$, up to a remainder vanishing as $\varepsilon\to0$ |
| $U(t)^*X^*U(t)$ | $-2t\,L_{u_0} \;+\; e^{itL_{u_0}^2}X^*e^{-itL_{u_0}^2}$ |

The third line is the heart of it, and it comes from a commutator identity Gérard calls "a
crucial operator identity which expresses some compatibility between the shift structure of
the Hardy space and the Lax pair":

$$[\,X^*,\,B_u\,] \;=\; -2L_u \;+\; i\,[\,L_u^2,\,X^*\,]$$

*(arXiv:2212.03139, Lemma 2.)* Differentiate $U^*X^*U$ in time, substitute, and integrate:
the $-2L_u$ term integrates to $-2tL_{u_0}$, and the commutator term exponentiates into the
conjugation by $e^{itL_{u_0}^2}$. **That is where the $2t$ in the explicit formula comes
from, and it comes from a single term in a single commutator.**

**Step 4 — cancel.** Substitute all three into Step 2. The conjugating factors
$e^{\pm itL_{u_0}^2}$ appear on the operator, on the vector, and on $\chi_\varepsilon$, and
they cancel completely, leaving

$$\Pi u(t,z)\;=\;\lim_{\varepsilon\to0}\frac{1}{2i\pi}\big\langle (X^*-2tL_{u_0}-z)^{-1}\Pi u_0,\ \chi_\varepsilon\big\rangle \;=\;\frac{1}{2i\pi}I_+\big[(X^*-2tL_{u_0}-z)^{-1}\Pi u_0\big]$$

The underlying lemma — that $[X^*,T_b]$ is a **rank-one** operator, proportional to
$I_+(f)\cdot b$ — is where the non-locality is finally tamed. *(I describe rather than
display that lemma: its numerical constant did not survive my PDF text extraction, and §13
explains why I refuse to display constants I could not close.)*

---

## 5. The one argument: soliton fishing

This is the section to read slowly. It is the mechanism that converts §4.4 into §4.3, and it
is elementary — Gérard derives the soliton case on the board in about two minutes.

### 5.1 Move into the soliton's frame

Fix an eigenvalue $\lambda_j$ of $L_{u_0}$ with normalized eigenfunction $\varphi_j$. Now
evaluate the explicit formula not at $z$ but at the **shifted** point $z - 2t\lambda_j$, and
watch the algebra:

$$\Pi u(t,\,z-2t\lambda_j) \;=\; \frac{1}{2i\pi}I_+\Big[\big(X^* - 2tL_{u_0} - z + 2t\lambda_j\big)^{-1}\Pi u_0\Big] \;=\; \frac{1}{2i\pi}I_+\Big[\big(X^* - 2t(L_{u_0}-\lambda_j) - z\big)^{-1}\Pi u_0\Big]$$

The shift in the spatial variable has become a **shift of the spectral parameter of the Lax
operator**. And the operator $L_{u_0}-\lambda_j$ has a one-dimensional kernel, spanned by
$\varphi_j$.

Now split $\Pi u_0$ along that kernel — which you may do because $L_{u_0}$ is self-adjoint,
and because its eigenvalues are **simple** (Wu, *SIAM J. Math. Anal.* 48 (2016)), so the
orthogonal complement of $\varphi_j$ is exactly the range of $L_{u_0}-\lambda_j$:

$$\Pi u_0 \;=\; \underbrace{\langle \Pi u_0,\varphi_j\rangle\,\varphi_j}_{\text{parallel}} \;+\; \underbrace{(L_{u_0}-\lambda_j)\chi}_{\text{orthogonal}}$$

**On the parallel piece, $t$ disappears.** $(L_{u_0}-\lambda_j)\varphi_j=0$, so
$2t(L_{u_0}-\lambda_j)\varphi_j = 0$ and the resolvent acts as $(X^*-z)^{-1}$, with no $t$ in
it at all.

**On the orthogonal piece, $t$ appears in the denominator.** Write, adding and subtracting,

$$\big(X^*-2t(L_{u_0}-\lambda_j)-z\big)^{-1}(L_{u_0}-\lambda_j)\chi \;=\; -\frac{1}{2t}\Big[\chi - \big(X^*-2t(L_{u_0}-\lambda_j)-z\big)^{-1}(X^*-z)\chi\Big]$$

and both terms in the bracket stay bounded, because the resolvent norm is at most
$1/\operatorname{Im}z$ uniformly in $t$ (§4.4b). So the orthogonal piece is $O(1/t)$.

*(Reconstructed. Gérard states exactly this argument aloud — "imagine I have an
$L_{u_0}-\lambda$ here in front of something; of course I can complete the denominator here,
and I get a factor one over $t$" — but the algebra was on the slide. The identity above is
the unique way to "complete the denominator", so the shape is forced; the uniform resolvent
bound that makes it work is the inference labelled in §4.4b.)*

Gérard's name for this: **soliton fishing.** You renormalize by twice an eigenvalue, and the
corresponding soliton is what stays behind while everything else washes out at rate $1/t$.

**The anchor, if you want one from the lab:** this is a **lock-in amplifier**. You multiply
the signal by a reference oscillating at exactly the frequency you care about, and everything
not at that frequency averages away. Here the "reference" is the shift $z\mapsto
z-2t\lambda_j$, the "frequency" is the eigenvalue, and the averaging-away is the $1/t$.

### 5.2 What is left is exactly a soliton

Carrying out the parallel piece gives (arXiv:2601.10488, eq. (3.2))

$$\Pi u(t,\,z-2t\lambda_j) \;\xrightarrow[t\to\infty]{}\; \frac{i}{\,z - \langle X^*\varphi_j,\varphi_j\rangle\,}$$

Set

$$p_j \;:=\; -\langle X^*\varphi_j, \varphi_j\rangle$$

and the limit is $i/(z+p_j)$, which by §3.2 is **exactly $\Pi R_{p_j}(z)$**. The fishing
produced a soliton profile, on the nose, with parameter determined by a single matrix element
of $X^*$ in the eigenbasis of the Lax operator.

The spectral dictionary is completed by two identities of Wu, quoted in the paper as (2.2)
and (2.3):

$$|\langle \varphi_j, u_0\rangle|^2 = -2\pi\lambda_j, \qquad \lambda_j I_+(\varphi_j) = -\langle \varphi_j,u_0\rangle$$

$$\operatorname{Im}p_j \;=\; \frac{|I_+(\varphi_j)|^2}{4\pi} \;=\; \frac{1}{2|\lambda_j|}\;>\;0 \qquad\Longrightarrow\qquad c_{p_j} \;=\; \frac{1}{\operatorname{Im}p_j}\;=\; -2\lambda_j$$

**Read the last line.** The eigenvalues of the Lax operator are all negative (Wu), and each
one is *half the negative of a soliton velocity*. Taller solitons are faster, faster solitons
sit at more negative eigenvalues. If you know KdV, this is the same music in a different key:
there the bound states of a Schrödinger operator give the soliton amplitudes; here the
eigenvalues of $D-T_{u_0}$ give the velocities. And $\operatorname{Im}p_j$ — which fixes both
height and width — is $|I_+(\varphi_j)|^2/4\pi$, the squared jump of the eigenfunction's
Fourier transform at the edge of the Hardy support. The one number that measures failure to
lie in $\mathrm{Dom}(X)$ is the number that measures the soliton.

### 5.3 The continuous spectrum, and the radiation

The same fishing works on the absolutely continuous spectrum, and Gérard is candid that this
is the long part: "It's much more complicated. It takes several pages. You need to work a
little bit with oscillatory integrals."

The setup. For $\lambda>0$, define **generalized eigenfunctions** $m_\pm(\cdot,\lambda)\in
L^\infty(\mathbb{R})$ as the unique solutions of

$$(L_{u_0}-\lambda)\,m_\pm = 0, \qquad \lim_{x\to\pm\infty} e^{-i\lambda x}m_\pm(x,\lambda)=1$$

They are not eigenfunctions — they are bounded, not $L^2$ — and they are normalized by
looking like the free wave $e^{i\lambda x}$ at one end of the line. Setting $u_0=0$ gives
exactly $e^{i\lambda x}$, so these are deformations of plane waves by the potential. If you
have met Jost solutions in one-dimensional scattering, these are them.

The **distorted Fourier transform** is then

$$\widetilde{f}^{\,\pm}(\lambda) \;=\; \int_{\mathbb{R}} f(x)\,\overline{m_\pm(x,\lambda)}\,dx$$

with a distorted Plancherel identity (arXiv:2601.10488, eq. (2.7)) that says the discrete and
continuous pieces together account for the whole norm:

$$\sum_{j=1}^N |\langle f,\varphi_j\rangle|^2 \;+\; \int_0^{\infty}|\widetilde f^{\,\pm}(\lambda)|^2\,d\lambda \;=\; 2\pi\int_{\mathbb{R}}|f(x)|^2\,dx$$

And the radiation profiles of the theorem are just the distorted Fourier transform of the
data:

$$\widehat{u_\infty^{\pm}}(\lambda) \;=\; \widetilde{\Pi u_0}^{\,\mp}(\lambda), \qquad \lambda>0$$

Note the **index flip**: the $+$ profile uses the $-$ generalized eigenfunction. That is the
paper's convention (eq. (2.6)) and I preserve it; it is exactly the kind of thing that is easy
to transcribe wrong.

The corresponding limit statement (eq. (3.3)) is the continuous analogue of §5.2, now with a
$t^{-1/2}$ normalization and a stationary-phase factor, converging **weakly** in
$L^2(0,\infty)$:

$$(2t)^{1/2}e^{it\lambda^2}\,\Pi u(t,\,z-2t\lambda)\;\rightharpoonup\; \frac{e^{i\pi/4}}{\sqrt{2\pi}}\;e^{i\lambda z}\;\widetilde{\Pi u_0}(\lambda)$$

The $e^{i\pi/4}$ and the $(2t)^{-1/2}$ are the signature of a stationary-phase evaluation of a
Schrödinger-type oscillatory integral — precisely the constants in the free Schrödinger
propagator, which is what §2 told you the linearized equation is.

**So here is the whole theorem in one sentence.**

> The spectral decomposition of the self-adjoint operator $L_{u_0}$ into its point part and
> its absolutely continuous part **is** the asymptotic decomposition of the solution into
> solitons and radiation. Eigenvalue $\lambda_j$ ↦ soliton of velocity $-2\lambda_j$;
> continuous spectrum $[0,\infty)$ ↦ a free linear wave whose profile is the distorted
> Fourier transform of the data.

That correspondence — bound states versus scattering states — is the oldest dichotomy in
quantum mechanics, and you have used it since your first course. What is new is that it
survives intact through a nonlinear flow, and that the vehicle carrying it across is a single
explicit formula rather than an inverse-scattering transform.

### 5.4 What the paper says that the podium did not

Two things worth having, both from arXiv:2601.10488 and neither stated in the lecture.

**A clean if-and-only-if (Corollary 2.2).**

- The asymptotics are **purely radiative** ($N=0$) **iff** $L_{u_0}$ is a positive operator.
  In particular this holds whenever $u_0 \le 0$ — a sign condition on the data, no spectral
  computation needed.
- The asymptotics are **purely solitonic** in one time direction ($u_\infty^{+}=0$, or
  $u_\infty^{-}=0$) **iff** $u_0$ is *exactly* a finite sum of soliton profiles. So you cannot
  get soliton-only behaviour by approximating; you have to be sitting on the multi-soliton
  manifold.

**No scattering shift on the soliton parameters (§1 of the paper).** The parameters $p_j$
are literally the same as $t\to+\infty$ and as $t\to-\infty$. The paper contrasts this
explicitly with the Riemann–Hilbert literature, "where some non-trivial scattering map
relates the soliton parameters." Since $p_j$ encodes both the velocity
($1/\operatorname{Im}p_j$) and the position offset ($-\operatorname{Re}p_j$ at $t=0$), the
reading is that Benjamin–Ono solitons emerge from a collision with **no position shift at
all**. *(The equality of parameters is the paper's; the interpretation as "no phase shift" is
mine, and would be worth confirming against the multi-soliton literature — Sun, *Comm. Math.
Phys.* 383 (2021).)* The radiation, by contrast, does pick up a scattering phase: the paper's
Remark 2.3 gives a unimodular $\beta(\lambda)$ with $\widehat{u_\infty^+}(\lambda) =
\beta(\lambda)\widehat{u_\infty^-}(\lambda)$, so the scattering operator is a **unitary Fourier
multiplier**.

### 5.5 The numerics, and why they are the best argument in the talk

Gérard shows a movie. Yvonne Alama Bronsard (Nantes Université / CNRS, Laboratoire de
Mathématiques Jean Leray), with Xi Chen and Matthieu Dolbeault, implemented the torus version
of the explicit formula
([arXiv:2412.13480](https://arxiv.org/abs/2412.13480), *Spectrally accurate fully discrete
schemes for some nonlocal and nonlinear integrable PDEs via explicit formulas*). Initial data:
a sum of two Gaussians. Over the simulation, **four solitons** separate out, tallest and
fastest in front, with the radiation trailing on the left.

His comment on why this is remarkable is the part to keep:

> "In general, long-time simulations are very difficult because of time discretization, and
> the errors in time discretization usually are exponential in time. So nothing can be seen
> for long time. Except that here, there is no time discretization, because you are
> discretizing an explicit formula."

The paper backs this quantitatively: the scheme is exact in time and spectrally accurate in
space, the error constant grows **linearly** rather than exponentially in $t$, and the
computational cost is **independent of the final time**. You do not march to $t$; you evaluate
at $t$.

### 5.6 The rest of the programme

The last five minutes are the wider picture, and they are worth having because they show the
method is a method and not a trick.

**The cubic Szegő equation came first.** Gérard and Sandrine Grellier introduced it "almost
20 years ago":

$$i\,\partial_t u \;=\; \Pi\big(|u|^2u\big), \qquad u(t)\in L^2_+$$

— the ordinary cubic NLS nonlinearity, composed with the Szegő projector, with the unknown
living in the Hardy space. It has a Lax pair too, but with $L_u$ replaced by the **square of
the Hankel operator** $H_u$, and $B_u$ again built from a Toeplitz operator associated with
$|u|^2$. *(Shapes as Gérard states them from the podium; I have not verified the constants, so
I do not display the pair — see Gérard–Grellier, *Trans. Amer. Math. Soc.* **367** (2015)
2979–2995 for the explicit formula on the torus.)* Its long-time behaviour is **worse** and
more interesting: Sobolev norms grow, transferring energy to high frequencies — wave
turbulence. A weak soliton resolution is nonetheless proved, with Grellier, in *Soliton and
breather resolution for the cubic Szegő flow on the line*
([arXiv:2606.20775](https://arxiv.org/abs/2606.20775)). Alexander Pushnitski (King's College
London) is the collaborator on the line version of the formula.

**Who connected the two.** This is the most human moment of the talk. The cubic Szegő work
"was at that time considerably isolated from the main trend of integrable PDE. But there was
one person who knew both things, and this person was **Thomas Kappeler**" — an expert on
action-angle variables for KdV and defocusing NLS. In 2018 Kappeler told him: *"Patrick, you
should apply your techniques to Benjamin–Ono."* They did the torus case together, with Peter
Topalov, finding action-angle variables (Gérard–Kappeler, *Comm. Pure Appl. Math.* **74**
(2021) 1685–1747). Kappeler died before the explicit formula existed. The entire research
programme in this lecture began with one person noticing that two isolated literatures were
the same subject.

**The family the method covers.** Generalized Benjamin–Ono hierarchies (with Jiao He, his
colleague at Orsay — *An Explicit Formula for the Benjamin–Ono Hierarchy*,
[arXiv:2604.20464](https://arxiv.org/abs/2604.20464)); the Calogero–Moser derivative NLS
(with Enno Lenzmann, Basel — *Comm. Pure Appl. Math.* **77** (2024) 4008–4062); the half-wave
maps equation, which is the classical continuum limit of **Haldane–Shastry** quantum spin
chains. All of them share the same feature: a Lax pair built from Toeplitz or Hankel
operators on a Hardy space, and hence the same commutator compatibility that made §4.5 work.

**The open problems, in his order.**
1. Less-decaying data: possibly **infinitely many** solitons, and **modified** scattering for
   the radiation instead of free scattering — work in progress.
2. **Perturbations** of these integrable equations. Can the explicit formula support a KAM
   theory, or a Nekhoroshev-type long-time stability theorem?
3. And the one he ends on: "let's come back to the more classical PDEs. KdV, cubic NLS,
   Camassa–Holm, KP2. What about them? Are there such explicit formulae? **For the moment,
   this is completely open.**"

---

## 6. Do this by hand

Three exercises. The first two are the load-bearing ones — do them and you own the mechanism.
The third is five minutes and explains a constant.

### 6.1 The one-soliton chain, end to end (30 minutes, pen)

Fix $p\in\mathbb{C}_+$ and set $\varphi_p(x) = \sqrt{\operatorname{Im}p/\pi}\,\cdot\,
\dfrac{1}{x+p}$.

**(a)** Verify $\|\varphi_p\|_{L^2}=1$.
**(b)** Verify $X^*\varphi_p = -p\,\varphi_p$ and hence
$p = -\langle X^*\varphi_p,\varphi_p\rangle$.
**(c)** Compute $I_+(\varphi_p) = \widehat{\varphi_p}(0^+)$ by contour integration, and check
$|I_+(\varphi_p)|^2/4\pi = \operatorname{Im}p$.
**(d)** Verify $\dfrac{i}{y+p} + \overline{\left(\dfrac{i}{y+p}\right)} = R_p(y)$, i.e.
$\Pi R_p(z)= i/(z+p)$.
**(e)** Conclude: the soliton limit $i/(z-\langle X^*\varphi_j,\varphi_j\rangle)$ of §5.2 is
exactly $\Pi R_{p_j}(z)$.

<details>
<summary>Solutions</summary>

**(a)** $\int \dfrac{dx}{|x+p|^2} = \int\dfrac{dx}{(x+\operatorname{Re}p)^2 +
(\operatorname{Im}p)^2} = \dfrac{\pi}{\operatorname{Im}p}$. Multiply by
$\operatorname{Im}p/\pi$: the norm is 1.

**(b)** $x\cdot\dfrac{1}{x+p} = 1 - \dfrac{p}{x+p}$. The constant $1$ is not in $L^2$; the
renormalization removes it, so $X^*\varphi_p = -p\varphi_p$, and since $\|\varphi_p\|=1$,
$\langle X^*\varphi_p,\varphi_p\rangle = -p$.

**(c)** For $\xi>0$, $\displaystyle\int \frac{e^{-i\xi x}}{x+p}dx$: the exponential decays in
the lower half-plane, close there. The only pole is $x=-p$, and $\operatorname{Im}(-p)<0$, so
it is enclosed. Traversing clockwise contributes $-2\pi i$ times the residue $e^{i\xi p}$, so
the integral is $-2i\pi e^{i\xi p}$, and letting $\xi\to0^+$ gives $I_+\big(1/(x+p)\big) =
-2i\pi$. Hence $I_+(\varphi_p) = -2i\pi\sqrt{\operatorname{Im}p/\pi}$ and
$$\frac{|I_+(\varphi_p)|^2}{4\pi} = \frac{4\pi^2\cdot(\operatorname{Im}p/\pi)}{4\pi} = \operatorname{Im}p \quad\checkmark$$

**(d)** $\dfrac{i}{y+p} - \dfrac{i}{y+\bar p} = \dfrac{i(\bar p - p)}{|y+p|^2} =
\dfrac{i\cdot(-2i\operatorname{Im}p)}{|y+p|^2} = \dfrac{2\operatorname{Im}p}{|y+p|^2}$, using
$(y+p)(y+\bar p)=|y+p|^2$ for real $y$. And
$\overline{i/(y+p)} = -i/(y+\bar p)$, so the left side of (d) is precisely that difference.
Since $1/(z+p)$ is holomorphic on $\mathbb{C}_+$ (pole in the lower half-plane) and the other
term is anti-holomorphic, the splitting $R_p = \Pi R_p + \overline{\Pi R_p}$ identifies
$\Pi R_p(z) = i/(z+p)$.

**(e)** Immediate from (b) and (d). ∎

**Why this exercise matters beyond itself.** Steps (b), (c) and (d) are three independent
computations that all have to agree with the published relations
$p_j = -\langle X^*\varphi_j,\varphi_j\rangle$, $\operatorname{Im}p_j =
|I_+(\varphi_j)|^2/4\pi = 1/2|\lambda_j|$, and $c_{p_j}=-2\lambda_j$. They do, including
every factor of $\pi$. That is not just a study aid — it is how I recovered the constants in
§5.2 after a PDF text extraction silently deleted every $\pi$ in the source. See §13.

</details>

### 6.2 Fish out one soliton yourself (25 minutes, pen)

Assume the explicit formula of §4.4, and that $L_{u_0}$ has a simple eigenvalue $\lambda_j<0$
with normalized eigenfunction $\varphi_j$, and that
$\|(X^*-2tL_{u_0}-z)^{-1}\|\le 1/\operatorname{Im}z$ for all $t$.

**(a)** Show that evaluating at the moving point $z-2t\lambda_j$ replaces $L_{u_0}$ by
$L_{u_0}-\lambda_j$ in the resolvent.
**(b)** Write $\Pi u_0 = \alpha\varphi_j + (L_{u_0}-\lambda_j)\chi$ and justify why this is
possible.
**(c)** Show the second term contributes $O(1/t)$.
**(d)** Show the first term contributes a $t$-independent multiple of $\Pi R_{p_j}(z)$.

<details>
<summary>Solutions</summary>

**(a)** $X^* - 2tL_{u_0} - (z-2t\lambda_j) = X^* - 2t(L_{u_0}-\lambda_j) - z$. That is the
whole content: a translation in the space variable is a shift of the spectral parameter,
because $t$ enters the formula only through $2tL_{u_0}$ and $z$ enters only additively.

**(b)** $L_{u_0}$ is self-adjoint, so $L^2_+ = \ker(L_{u_0}-\lambda_j)\oplus
\overline{\mathrm{ran}}(L_{u_0}-\lambda_j)$. The eigenvalue is **simple** (Wu 2016), so the
kernel is one-dimensional. Anything orthogonal to $\varphi_j$ is (in the closure of) the
range, which is what lets you extract the factor $(L_{u_0}-\lambda_j)$ — the step Gérard
justifies aloud as "by the spectral theorem". *(A completeness caveat: for the closure of the
range you need $\chi$ in a suitable domain; the paper does this carefully in §6, and it is
where the hypotheses $xu_0\in H^1$ and $x^2u_0 = c_0+L^2$ get used.)*

**(c)** Put $A_t = X^*-2t(L_{u_0}-\lambda_j)-z$. Then $-2t(L_{u_0}-\lambda_j) = A_t -
(X^*-z)$, so $(L_{u_0}-\lambda_j)\chi = -\frac{1}{2t}\big[A_t\chi - (X^*-z)\chi\big]$ and
$$A_t^{-1}(L_{u_0}-\lambda_j)\chi = -\frac{1}{2t}\Big[\chi - A_t^{-1}(X^*-z)\chi\Big]$$
The bracket is bounded uniformly in $t$ by $\|\chi\| + \|(X^*-z)\chi\|/\operatorname{Im}z$.
So the whole thing is $O(1/t)$, and $I_+$ of it vanishes in the limit.

**(d)** $(L_{u_0}-\lambda_j)\varphi_j = 0$ kills the $t$-dependence outright, leaving
$\frac{\alpha}{2i\pi}I_+[(X^*-z)^{-1}\varphi_j] = \alpha\,\varphi_j(z)$ by the Cauchy-like
formula of §3.3 — a $t$-independent holomorphic function of $z$. Since $\varphi_j$ turns out
to be (a multiple of) $1/(x+p_j)$ in the one-soliton case, this is a multiple of
$\Pi R_{p_j}(z)$. In general the identification of the constant is exactly where the Wu
identities of §5.2 are used, and the published statement is that the limit is precisely
$i/(z+p_j)$ with $p_j = -\langle X^*\varphi_j,\varphi_j\rangle$. ∎

**The take-away.** The nonlinear long-time asymptotics reduced to: *split a vector along an
eigenvector, and note that the kernel direction is the only one where a factor $2t$ fails to
appear in a denominator.* Everything hard was already spent in producing the formula.

</details>

### 6.3 Where the $t^{-1/2}$ and $e^{i\pi/4}$ come from (5 minutes)

Show that the linearized equation $\partial_t w = \partial_x|D|w$ restricted to the Hardy
component is a free Schrödinger equation, and say why that explains both the $(2t)^{1/2}$
normalization and the $e^{i\pi/4}$ in the radiation limit of §5.3.

<details>
<summary>Solution</summary>

On the Fourier side $\widehat{\partial_x|D|w}(\xi) = (i\xi)(|\xi|)\hat w(\xi)$. On the Hardy
component $\xi>0$ this is $i\xi^2\hat w(\xi)$, so $\hat w(t,\xi) = e^{it\xi^2}\hat w_0(\xi)$
— the free Schrödinger propagator (with the opposite sign convention to
$i\partial_t\psi = -\psi_{xx}$, i.e. time-reversed). Consequences you already know: $L^\infty$
decay at rate $t^{-1/2}$, which is Gérard's "classical dispersion inequality for
Schrödinger"; and stationary phase on $\int e^{i(t\xi^2 + x\xi)}(\cdots)d\xi$ producing the
factor $\sqrt{\pi/t}\,e^{i\pi/4}$ from the Fresnel integral. Both constants in eq. (3.3) are
that Fresnel factor. ∎

</details>

---

## 7. What is actually useful to you

Five items, ordered by how often you will reach for them.

### 7.1 A closed form in $t$ is not a nicety — it changes the error model

This is the most directly transferable thing in the lecture and Gérard says it in one
sentence: time-stepping errors compound **exponentially** in $t$, so long-horizon simulation
is hopeless; evaluating a formula has **no time discretization at all**, so the error does
not compound and the cost does not grow with the horizon. The numerical paper measures it:
error constant linear rather than exponential in $t$, cost independent of final time.

The agent-systems translation is exact, and it is a design rule rather than a metaphor.
**A long-running process that carries mutable state accumulates drift; a process that
recomputes its state from the original inputs plus the elapsed parameter does not.** If you
can express "state at step $n$" as a function of the initial state and $n$, do that instead of
$n$ incremental updates — even if each individual evaluation is more expensive. The costs
compose differently: the stepping version has error that compounds, the formula version has
error that is bounded once. That is the same argument as idempotent replay versus incremental
mutation, and this talk is a clean proof that it can be worth a great deal of work to get into
the first regime.

### 7.2 Change frame to a frame where every unknown is known

§4.5 is a two-move proof: apply a unitary to both sides of an inner product — which changes
nothing — and then discover that in that frame each of the three unknown objects has a closed
form in terms of the initial data. The value came entirely from choosing *which* frame, and
the choice was dictated by the structure (the Lax flow's own propagator).

The generalizable version: **when several unknowns appear in one expression, look for a
transformation that is free (invertible, structure-preserving) and that simultaneously
simplifies all of them.** The candidates are usually generated by the symmetry you already
know the problem has. Gérard did not search for $U(t)$; the Lax pair handed it to him.

### 7.3 The defect is the state variable

$X$ is symmetric but not self-adjoint on the Hardy space, and $X^*$ has a strictly bigger
domain. The gap between the two domains is one number, $I_+(f)$, and Gérard's line is
that "this is the constant in which the whole dynamics of Benjamin–Ono is hidden."

That is a general instinct worth acquiring. When a construction *almost* works and fails by
a measurable amount, the failure is often the interesting object rather than an obstacle —
here it turns out to be simultaneously (i) the renormalizing constant that makes $X^*$
defined, (ii) the contour-integral substitute in the Cauchy formula, and (iii) via
$\operatorname{Im}p_j = |I_+(\varphi_j)|^2/4\pi$, the soliton's height and width. One number,
three jobs.

### 7.4 A blocked standard route can be better news than an open one

Benjamin–Ono on the line has no Riemann–Hilbert formulation, so Deift–Zhou was unavailable.
That obstruction is what forced the explicit-formula method — and the explicit formula
delivers strictly more than the blocked route would have: an evaluable expression at every
$t$, a spectrally accurate numerical scheme, and (per §5.4) a soliton resolution with **no
scattering shift** on the parameters, which the Riemann–Hilbert route does not give for other
equations.

The lesson is not "obstructions are good". It is: when the standard machinery does not apply,
the first question is what specific structural feature blocks it (here: non-locality of the
Lax operator), and the second is whether that same feature enables something else (here: the
commutator $[X^*,T_b]$ is rank one, which is exactly what makes the conjugation close).

### 7.5 Two isolated literatures are often one subject, and someone has to notice

Gérard worked on the cubic Szegő equation for a decade in a corner "considerably isolated
from the main trend of integrable PDE". Thomas Kappeler, who knew both the Hardy-space
techniques and classical action-angle theory for KdV, told him in 2018 to point the
technique at Benjamin–Ono. That single suggestion is the origin of this plenary lecture.
Kappeler died before seeing the explicit formula.

The transferable content is the same as Otto's closing point in
`geometric-concepts-pde-otto.md` §8.5, arrived at from a different direction: the highest
returns come from the person holding two vocabularies at once. It is worth being that person
deliberately, and worth telling people when you notice the overlap in their work.

---

## 8. Where to read next

1. **Patrick Gérard, *Lectures on integrable equations of Benjamin–Ono type*,** EMS Surveys
   in Mathematical Sciences (2026), published 7 January 2026. **The companion, and the right
   entry point** — it is the survey the research papers themselves cite for the integrable
   structure. I could not retrieve it (no arXiv version, journal paywall), so I am
   recommending it on its role rather than on having read it.
2. **P. Gérard, *An explicit formula for the Benjamin–Ono equation*,** Tunis. J. Math. **5**
   (2023) 593–603, [arXiv:2212.03139](https://arxiv.org/abs/2212.03139). **Eleven pages, and
   completely self-contained.** It contains both explicit formulae (torus and line) with full
   proofs, and the proofs are exactly the ones sketched in §4.5. If you read one thing, read
   this — it is short enough for one evening and every step is checkable.
3. **L. Gassot, P. Gérard, P. D. Miller, *A proof of the soliton resolution conjecture for
   the Benjamin–Ono equation*,** [arXiv:2601.10488](https://arxiv.org/abs/2601.10488), 29
   pages. The theorem of the talk. §§1–3 (five pages) give the statement, the spectral
   dictionary, and the strategy; the remaining twenty pages are the oscillatory-integral
   analysis of the continuous spectrum that Gérard declined to present.

---

## 9. Self-test

<details>
<summary>1. Why is the Riemann–Hilbert / Deift–Zhou route unavailable for Benjamin–Ono on the line?</summary>

Because the Lax operator $L_u = D - T_u$ is not a differential operator — the potential
enters through a **Toeplitz** operator, which is non-local. As a result the Cauchy problem on
$\mathbb{R}$ has no inverse-scattering transform formulated as a Riemann–Hilbert problem, so
nonlinear steepest descent has nothing to act on. That is stated verbatim in
arXiv:2601.10488 §1. This is *why* a new method was needed, not merely a preference for one.
</details>

<details>
<summary>2. What is $X^*$, and in what sense is it "multiplication by $x$"?</summary>

It is the adjoint, on the Hardy space $L^2_+(\mathbb{R})$, of multiplication by $x$.
Multiplication by $x$ is symmetric but not self-adjoint there, and $X^*$ has a strictly bigger
domain. Concretely $X^*f(x) = xf(x) + I_+(f)/(2i\pi)$ — multiplication by $x$ **renormalized
by one constant**, the constant being the jump $I_+(f)=\hat f(0^+)$ of the Fourier transform at
the edge of its support, divided by $2i\pi$. On the Fourier side, $\widehat{X^*f} = i\,
d\hat f/d\xi$ on $(0,\infty)$.
</details>

<details>
<summary>3. Why must $\hat f(0^+)=0$ for $f$ in the domain of $X$ itself?</summary>

If $f\in L^2_+$ and $xf(x)\in L^2$, then $f\in L^1$, so $\hat f$ is continuous by
Riemann–Lebesgue. But $\hat f$ vanishes identically on $\xi<0$ (Hardy space), so continuity
forces $\hat f(0^+)=0$. The functions we care about — the soliton projections — have
$\hat f(0^+)\ne0$, so they sit in $\mathrm{Dom}(X^*)\setminus\mathrm{Dom}(X)$.
</details>

<details>
<summary>4. State the Cauchy-like representation formula and say which piece plays the role of the contour integral.</summary>

$f(z) = \dfrac{1}{2i\pi}I_+\big[(X^*-z)^{-1}f\big]$ for $f\in L^2_+$, $z\in\mathbb{C}_+$. The
resolvent $(X^*-z)^{-1}$ plays the role of the Cauchy kernel $1/(\zeta-z)$ — correctly, since
for a multiplication operator the resolvent *is* multiplication by that kernel. The functional
$I_+$ plays the role of $\oint\cdots d\zeta$: it is "like an integral but is not one", because
the functions involved are not $L^1$.
</details>

<details>
<summary>5. Write the explicit formula, and say in one sentence how time enters.</summary>

$\Pi u(t,z) = \dfrac{1}{2i\pi}I_+\big[(X^*-2tL_{u_0}-z)^{-1}\Pi u_0\big]$, with
$u = \Pi u + \overline{\Pi u}$ since $u$ is real. Time enters by **one substitution**:
$X^*\rightsquigarrow X^*-2tL_{u_0}$ inside the resolvent of the Cauchy-like formula. Nothing
else changes.
</details>

<details>
<summary>6. Where does the factor $2t$ come from in the proof?</summary>

From the commutator identity $[X^*,B_u] = -2L_u + i[L_u^2,X^*]$. Conjugating $X^*$ by the Lax
propagator, $\frac{d}{dt}\big(U^*X^*U\big) = U^*[X^*,B_u]U$; the $-2L_u$ term integrates to
$-2tL_{u_0}$, and the commutator term exponentiates into a conjugation by
$e^{itL_{u_0}^2}$ that cancels against identical factors on the vector and on
$\chi_\varepsilon$.
</details>

<details>
<summary>7. Explain soliton fishing in three sentences.</summary>

Evaluate the explicit formula at the moving point $z-2t\lambda_j$, which turns the resolvent
into $(X^*-2t(L_{u_0}-\lambda_j)-z)^{-1}$. Split $\Pi u_0$ into its component along the
eigenfunction $\varphi_j$ and the rest: on the eigenfunction, $L_{u_0}-\lambda_j$ vanishes and
all $t$-dependence disappears; on the rest, the factor $(L_{u_0}-\lambda_j)$ can be
"completed into the denominator", producing an explicit $1/2t$ and hence $O(1/t)$ decay
(using that the resolvent norm is $\le 1/\operatorname{Im}z$ uniformly in $t$). What survives
is exactly $\Pi R_{p_j}(z) = i/(z+p_j)$ with $p_j = -\langle X^*\varphi_j,\varphi_j\rangle$.
</details>

<details>
<summary>8. Give the spectral dictionary: what does each part of the spectrum of $L_{u_0}$ become?</summary>

The eigenvalues $\lambda_1,\dots,\lambda_N$ — finitely many, simple, all negative (Wu 2016) —
each give one soliton, with parameter $p_j = -\langle X^*\varphi_j,\varphi_j\rangle$ and
velocity $c_{p_j} = -2\lambda_j$, together with
$\operatorname{Im}p_j = |I_+(\varphi_j)|^2/4\pi = 1/(2|\lambda_j|)$. The absolutely continuous
spectrum $[0,\infty)$ gives the radiation: the profiles $u_\infty^\pm$ are the distorted
Fourier transform of $\Pi u_0$ against the generalized eigenfunctions $m_\mp$, evolving under
the linear flow $e^{t\partial_x|D|}$ and decaying like $t^{-1/2}$ in $L^\infty$. It is the
bound-state / scattering-state dichotomy, carried intact through a nonlinear flow.
</details>

<details>
<summary>9. When is the long-time behaviour purely radiative, and when purely solitonic?</summary>

Purely radiative ($N=0$) **iff** $L_{u_0}$ is a positive operator — in particular whenever
$u_0\le0$. Purely solitonic in one time direction **iff** $u_0$ is exactly a finite sum of
soliton profiles $R_{\tilde p_j}$. Both from arXiv:2601.10488, Corollary 2.2; neither is
stated in the lecture.
</details>

<details>
<summary>10. Why is the numerical demonstration a strong argument rather than a decoration?</summary>

Because long-time simulation of a dispersive PDE normally fails from accumulated
**time-discretization** error, which grows exponentially in $t$. Evaluating the explicit
formula involves no time stepping, so there is no such accumulation: the error constant grows
linearly and the cost is independent of the final time (Alama Bronsard–Chen–Dolbeault,
arXiv:2412.13480). Seeing four solitons cleanly separate from two Gaussians over a long
horizon is therefore evidence about the *formula*, not just a pretty movie.
</details>

<details>
<summary>11. What did Thomas Kappeler contribute, and why is it in the talk?</summary>

Kappeler was an expert on action-angle variables for KdV and defocusing NLS who also followed
Gérard's cubic Szegő work — at the time isolated from mainstream integrable PDE. In 2018 he
told Gérard to apply the Hardy-space techniques to Benjamin–Ono. They did the torus case
together with Peter Topalov (action-angle variables; Gérard–Kappeler, *Comm. Pure Appl. Math.*
74 (2021)). He died before the explicit formula appeared. Gérard includes it because the
programme exists because one person held two vocabularies at once.
</details>

---

## 10. Note on the tutorial process

**Difficulty versus reputation.** Reputation would have got this one roughly right and for
the wrong reason. Gérard is known for microlocal analysis, concentration-compactness and
dispersive equations — a formidable list that would predict a hard talk. The actual lecture is
narrower and much more accessible than the reputation: it is one equation, one operator, one
formula, one theorem, built out of complex analysis you already own. The rating **2/5** is
driven by the fact that only $X^*$ and the fishing mechanism are new to you. I considered a
split rating (objects 1/5, mechanism 3/5) and rejected it: the spec's split cases are two
disjoint half-talks or an easy-maths/hard-frame mismatch, and this talk is one continuous
argument with a single new gadget. A single 2/5 with the Tier-0 inversion is the honest call.

**The anchors, and how they were tested.** The brief proposed two: a Lax pair as an
isospectral deformation, and soliton resolution as a nonlinear normal-mode decomposition.
**Both survived contact with the transcript**, and Gérard states both from the podium — he
derives isospectrality live from $L_{u(t)} = U(t)L_{u_0}U(t)^*$, and §5 is literally a
correspondence between the spectral decomposition of $L_{u_0}$ and the asymptotic
decomposition of $u$. But the anchor I lead with is a third one, which Gérard hands over
himself and which is stronger than either: **the explicit formula is the Cauchy integral
formula with $x$ shifted by $2tL_{u_0}$**. He says "I called it Cauchy-like because it starts
with $1/2i\pi$", and the term-by-term correspondence (kernel ↦ resolvent, contour ↦ $I_+$) is
exact rather than decorative. Following the spec's Gaitsgory precedent, I also name the
**Riemann–Hilbert / Deift–Zhou** route explicitly *as absent*, quoting the paper's own
sentence, because a reader with your background would otherwise expect it.

**Name corrections.** All verified against the two papers' bibliographies, the speakers'
institutional pages, or the primary literature.

| Caption | Correct |
|---|---|
| Professor Gerard, University Paris Saclay | Patrick **Gérard**, Université Paris-Saclay (Laboratoire de Mathématiques d'Orsay) |
| "the Zigger" / "cubic Zigger" / "cubic Zakharov-Shabat equation" | the **Szegő** projector; the **cubic Szegő equation** |
| Sondre Grolid | **Sandrine Grellier** |
| Nolins Man, professor in Basel | **Enno Lenzmann** (Universität Basel) |
| Even Boussard, from Quebec, now CNRS in Nantes | **Yvonne Alama Bronsard** (Nantes Université / CNRS, LMJL; McGill, Montréal) |
| Sichen | **Xi Chen** |
| Mathieu Dolbeault | **Matthieu Dolbeault** |
| Jauhar, my colleague at Orsay | **Jiao He** (coauthor "J. He" on the BO-hierarchy paper; Orsay) *(reconstructed — see below)* |
| Louis Gassot | **Louise** Gassot (CNRS, Université de Rennes) |
| Peter Miller, Michigan Ann Arbor | Peter D. **Miller** ✓ (correct as spoken) |
| David Kruskal | **Martin** Kruskal (with Norman **Zabusky**) |
| Gardner, Green, Kruskal, Miura | Gardner, **Greene**, Kruskal, Miura ✓ (1967) |
| Burling theorem | **Beurling**'s theorem |
| Otto Toeplitz, "1915 or something" | Otto Toeplitz, **1911** (Math. Ann. 70) |
| Nakamura, Ablowitz, Fokas | ✓ correct (Ablowitz–Fokas, *Stud. Appl. Math.* 68 (1983)) |
| Alday-Destri-Heisenberg quantum chains | **Haldane–Shastry** quantum spin chains |
| Terry Tao | Terence **Tao** |
| Jeremy Quastel | ✓ correct |
| Thomas Kappeler / Peter Topalov | ✓ correct |
| Alexander Pushnitski, King's College | ✓ correct (King's College London) |
| Claude Bardos | ✓ correct (4 April 1940 – 16 June 2026) |
| David Levermore, Jeffrey Rauch | ✓ correct (C. David Levermore; Jeffrey Rauch) |
| Merle and his group | Frank **Merle** ✓ |
| Nekhoroshev | ✓ correct |
| Camassa-Holm, KP2, Calogero-Moser | ✓ correct |

**Substantive corrections, not just spellings.**

- The talk dates John Scott Russell's canal observation to **1864**. It was **1834**, on the
  Union Canal near Edinburgh — the location as spoken is right, the year is off by thirty
  years. Corrected silently in §2 and flagged here.
- The talk says Toeplitz introduced these operators in "1915 or something like this" (he
  hedges). The founding paper is 1911.
- Both are harmless to the mathematics. I flag them because the spec requires substantive
  caption errors to be corrected in text and listed here.

**Names I could not verify.** In the closing acknowledgements Gérard lists collaborators as
"Jauhar, my colleague at Orsay, and Nolins Man, who is professor in Basel, **Sichan, Hanada,
Sredin, Ola Melon**". The first two resolve confidently (Jiao He, Enno Lenzmann). **The last
four do not resolve to anything I can source, and I have not guessed.** "Sichan" is plausibly
Xi Chen again, given the earlier mention, but I will not assert it. I have omitted these four
names from the body of the tutorial rather than inventing attributions. "Jiao He" itself is
marked *(reconstructed)*: it is anchored to a located publication — Gérard's preprint page
lists *An Explicit Formula for the Benjamin–Ono Hierarchy* with coauthor **J. He**,
arXiv:2604.20464 — and to the phonetic match plus the Orsay affiliation, but I did not find a
source spelling out the first name in this context.

**How I recovered the constants, and why you should trust them more than a single
transcription.** The caption track carries **no mathematics whatsoever** — every formula in
this talk lived on slides. So all displays here come from the two papers. Two of those texts I
read through `pdftotext`, which silently **deleted every $\pi$ character** and in one place
rendered $X^*$ as $X$. That is exactly the failure mode that produces confident,
wrong mathematics. My defence was a closed consistency chain, run by hand:

$$\varphi_p = \sqrt{\tfrac{\operatorname{Im}p}{\pi}}\tfrac{1}{x+p} \ \Rightarrow\ \|\varphi_p\|=1,\quad X^*\varphi_p=-p\varphi_p,\quad I_+(\varphi_p) = -2i\pi\sqrt{\tfrac{\operatorname{Im}p}{\pi}}$$

$$\Rightarrow\quad \frac{|I_+(\varphi_p)|^2}{4\pi} = \operatorname{Im}p, \qquad p = -\langle X^*\varphi_p,\varphi_p\rangle, \qquad \Pi R_p(z) = \frac{i}{z+p}$$

Every published relation in §5.2 — $p_j=-\langle X^*\varphi_j,\varphi_j\rangle$,
$\operatorname{Im}p_j = |I_+(\varphi_j)|^2/4\pi = 1/2|\lambda_j|$, $c_{p_j}=-2\lambda_j$, and
Wu's $|\langle\varphi_j,u_0\rangle|^2 = -2\pi\lambda_j$ — closes against this chain **with the
$\pi$'s restored**. Independently, I re-fetched the arXiv **HTML** of arXiv:2601.10488v2,
which preserves LaTeX, and confirmed the explicit formula, the soliton limit and the radiation
limit character by character. Where a constant could not be closed either way — specifically
the commutator identity $[X^*,T_b]f \propto I_+(f)\,b$ — **I describe the identity and refuse
to display it.** That is the one place where I have deliberately given you less than the
source contains. This exercise is §6.1, so you can rerun the check yourself.

**Where the gaps are, and how bad each one is.**

- **The proceedings paper — structural, and the biggest hole in this document.** SIAM DOI
  10.1137/25M1805497 returned 403; no abstract retrievable. Gérard says from the podium that
  the proceedings contain many more references *and* cover the **zero-dispersion limit** —
  "the corresponding problem to the Lax–Levermore problem for KdV in the '80s" — which the
  talk does not develop and which therefore appears nowhere in this tutorial beyond this
  sentence. If you want that material, the accessible substitutes are Blackstone–Gassot–
  Gérard–Miller, *The Benjamin–Ono equation in the small dispersion limit with rational data*
  ([arXiv:2410.17405](https://arxiv.org/abs/2410.17405), to appear in *Comm. Pure Appl.
  Math.*) and the Gérard–He hierarchy paper.
- **The EMS survey — moderate.** *Lectures on integrable equations of Benjamin–Ono type*, EMS
  Surv. Math. Sci. (2026) is the natural companion and is unretrievable. Its absence cost me
  nothing for the mathematics of this talk, because both underlying results have full-text
  primary sources, but it would have been the better-pedagogy source and it is my first
  recommendation in §8 on that basis.
- **The proof of the radiation limit — low, and deliberate.** Gérard declines to present it
  ("several pages... oscillatory integrals") and so do I. §5.3 states the setup, the objects,
  and the limit, and stops. Twenty of the paper's twenty-nine pages are that argument.
- **The Lax pair for the cubic Szegő equation — low.** I give the shape as Gérard states it
  (Hankel squared as the Lax operator) and do not display the pair, because I did not verify
  the constants.
- **The one-slide items are gone.** He points at two typos on his own slides ("$y$ should be
  $x$ here"; "I forgot the Fourier transform here, that's my second typo") — those slides are
  invisible to the caption track, and I have reconstructed the intended statements from the
  papers instead, which is why neither typo appears above.

**Labelled reconstructions.** Exactly two displays in the body are reconstructions rather than
quotations: the $O(1/t)$ identity in §5.1 (Gérard states the argument aloud; the algebra was
on the slide; the identity is the unique way to execute what he describes), and the uniform
resolvent bound $\|(X^*-2tL_{u_0}-z)^{-1}\|\le1/\operatorname{Im}z$ in §4.4b (the paper proves
maximal dissipativity; the bound is the standard consequence, and §5 needs it). Both are
marked in place.

**Talk versus paper, where they differ.** Three places, all flagged in the body: (i) the
theorem's hypotheses and convergence — $H^\infty$ from the podium, $H^1$ in the paper; (ii)
the Lax-pair characterization — "if and only if" from the podium, one direction stated in the
paper; (iii) Corollary 2.2's two if-and-only-ifs and the no-scattering-shift observation,
which are in the paper and not in the talk. The talk is not wrong in any of these; it is
stated for a lecture audience.

**Cross-references rather than duplication.** §7.5 touches the same point as
`geometric-concepts-pde-otto.md` §8.5 (two apparently opposite fields turn out to be one) and
I cite it rather than rebuilding it. Gérard also mentions Jeremy Quastel's plenary — KP2
arising out of KPZ analysis — in his opening; no tutorial for that talk exists in this folder
at the time of writing, so there is nothing to point at.
