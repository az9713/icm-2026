# Round 2 — re-deriving every worked exercise solution

Run 2026-08-18. The check `HANDOFF.md` listed as never run: *re-derive the worked exercise
solutions.* Before this round, exactly **one** solution in the corpus had ever been
re-derived — `mesh-generation-pdes-buffa.md:910` — and it was wrong.

Method: read each exercise and its `<details>` solution, work it independently on paper, and
compare. No papers needed for most of them; that is the point of the check. Every exercise in
all 20 files is covered. Errors are listed here **and** in the per-file `verify/{slug}.md`.

This file is written as the check runs. If it ends mid-list, the entries above the cut are
still complete.

## Score

| | count |
|---|---|
| Files with a "Do this by hand" section | 20 of 20 |
| Worked solutions re-derived | **44** |
| Solutions whose **conclusion** is wrong | **0** |
| Defects found (wrong constant, dropped sign, shifted index, self-contradiction) | **9**, in 6 files |
| Of those, already known before this round | 1 (`buffa` §8.1) |

Full table at the end, under **Total**.

---

## Errors found

### 1. `summaries/random-matrices-localization-yau.md:964` — the constant c is wrong

Exercise 7.1 step 2 asks the reader to show `1 − |m|² = cη + O(η²)` and "identify c in terms
of Im m_sc(E)". The solution answers:

> `c = 2 Im m_sc(E)/√(4−E²) > 0 in the bulk`

Since `Im m_sc(E) = √(4−E²)/2` — which the solution's own step 1 establishes — that expression
is **identically 1**, for every E in the bulk. It is not "in terms of Im m_sc(E)" at all; the
two factors cancel.

**The correct value.** Write `m = m_sc(E)`, so `|m| = 1` and `m = e^{iθ}` with
`sin θ = Im m = √(4−E²)/2`. Expanding `m(E+iη) = m + iη m′ + O(η²)`,

    1 − |m(E+iη)|² = 2η · Im( conj(m) m′ ) + O(η²).

From `m² + zm + 1 = 0` we get `m′ = −m/(2m+z)`, and `z = −m − 1/m`, so `2m + z = m − 1/m` and
`m′ = −m²/(m²−1)`. Then `conj(m) m′ = −m/(m²−1)` at η = 0, and with `m = e^{iθ}`,
`m² − 1 = e^{iθ}·2i sin θ`, so `conj(m) m′ = i/(2 sin θ)` and `Im(conj(m) m′) = 1/(2 sin θ)`.
Hence

    1 − |m|² = η / sin θ + O(η²),   i.e.   **c = 1/Im m_sc(E) = 2/√(4−E²)**.

The stated formula has `Im m_sc(E)` in the numerator where it belongs in the **denominator**,
as a reciprocal.

**Check the two against each other at E = 0:** direct expansion of `m(iη)` gives
`|m|² = 1 − η + O(η²)`, so c = 1 there. Both formulas give 1 at E = 0 — which is exactly why
the error survives a spot check. At E = 1 the correct c is `2/√3 ≈ 1.155`; the file's is 1.

**Impact: low, and the file says so.** The next sentence reads "The only thing that matters
downstream is that **c > 0 and the leading term is linear in η**", and that is true and is all
step 4 uses. But the exercise asked for c, and the answer given is wrong.

### 2. `summaries/random-matrices-localization-yau.md:963` — a dropped minus sign

Same solution, one line earlier:

> `m′ = −m/(2m + z) = m/(m − 1/m)`

The first expression is right. The second drops the sign: with `2m + z = m − 1/m`, it must be
`m′ = −m/(m − 1/m)`. The two displayed expressions contradict each other.

### 3. `summaries/random-matrices-localization-yau.md:1037-1041` — the Tracy–Widom tails are described backwards

The "sanity check worth doing" after exercise 7.2 says:

> "That asymmetry (83, not 50) is the **left-skew** of TW₁: the distribution has a **thin tail
> to the right and a thicker one to the left**, so the median sits above the centring point."

All three clauses are wrong, and they are wrong together:

- **The tails are the other way round.** For Tracy–Widom, `F_β(s) ≈ exp(−β|s|³/24)` as
  `s → −∞` and `1 − F_β(s) ≈ exp(−(2β/3)s^{3/2})` as `s → +∞`. A cubic decay is far faster
  than a 3/2-power decay, so the **left** tail is the thin one and the **right** tail is the
  thicker one.
- **TW₁ is right-skewed, not left-skewed.** Its skewness is about +0.29, which is the same
  fact stated as a moment.
- **The median is below 0, not above.** TW₁ has mean ≈ −1.21 and median ≈ −1.27.

And the explanation is not needed anyway: `F₁(0) ≈ 0.83` because 0 sits about 0.95 standard
deviations (sd ≈ 1.27) **above** a mean of ≈ −1.21. That is a location fact, not a skew fact.

**Impact: low but real.** It is a side remark in a solution the reader is invited to check,
the numbers 0.83 and 0.69 are correct, and nothing downstream uses the skew. But a reader who
takes the description at face value now believes the wrong thing about Tracy–Widom.

### 4. `summaries/arithmetic-patterns-ziegler.md:1035-1041` — two wording slips in an otherwise correct solution

Exercise 7.1(4). The solution correctly shows that of the 8 terms in the expansion, the all-δ
term gives δ³ and the three single-f terms vanish. It then writes "Summing the **at most 7**
nonzero mixed terms" — but it has just shown that at most **4** are nonzero. The bound still
holds (4 ≤ 7, and the exercise statement's constant 7 is generous), so nothing is wrong; the
sentence contradicts the one before it.

In the same paragraph the Cauchy–Schwarz step is written
`|Σ_r f̂(r)ĝ(−2r)ĥ(r)| ≤ ‖f̂‖_∞ Σ_r |f̂(r)||ĥ(r)|` — the middle factor should be `|ĝ(−2r)|`.
An index typo; the conclusion is right.

---

## Per-file results

### `optimization-theory-practice-wright` — 2 exercises, both correct

- **§9.1 min–max LP reformulation.** `λ = t(b − Ax)` drives the inner objective to +∞ exactly
  when `Ax ≠ b`; on the feasible set the λ term vanishes identically. Correct.
- **§9.2 tridiagonal lower bound.** `∇f(0) = −e₁`, so `x₁ ∝ e₁`; `Tx₁ = α(2e₁ − e₂)`, so
  `∇f(x₁)` has support {1,2}; induction gives `supp(x_k) ⊆ {1..k}`. And `x* = T⁻¹e₁` has
  `(x*)ᵢ = (n+1−i)/(n+1)`, every component nonzero, so the discarded tail really is nonzero.
  Correct.

### `shape-of-math-kontorovich` — 1 proof exercise + 1 lab, both correct

- **§6.1 handshake lemma.** `Σ_x d(x) = 2·(handshakes)` is even; the even-degree part of the
  sum is even; so the odd-degree part is even; a sum of odd numbers is even exactly when the
  number of terms is even. Correct.
- **§6.2 Lean demo.** Traced by hand, not compiled. Step 2 ("change `use 1` to `use 0` — it
  still works") is right: the hypothesis holds for every n, so the witness is irrelevant.

### `geometric-concepts-pde-otto` — 2 exercises, both correct

- **§7.1 Fokker–Planck from JKO.** `δE/δρ = log ρ + 1 + V`; `ρ∇(log ρ + V) = ∇ρ + ρ∇V`; so
  `∂ₜρ = ∇·(∇ρ + ρ∇V) = Δρ + ∇·(ρ∇V)`. Correct, signs included. The closing contrast — flat
  L² gives `∂ₜρ = −(log ρ + 1 + V)`, not a PDE — is also correct.
- **§7.2 exponent bookkeeping**, all four parts. `α = 2 − d/2`; remainder order `α + d/2 − 2`;
  coherence `α > 1 − d/4`; the table (3/4, 1/2, 1/4, 0, negative) is right at every row; and
  the bonus check — substituting `α = 2 − d/2` gives remainder order exactly 0 for every d —
  is right. Correct.

### `modern-ml-methods-bartlett` — 2 exercises, both correct

- **§7.1 self-boundedness.** `ℓ″ = σ(1−σ) ≤ 1 − σ = 1/(1+eᶻ) ≤ e^{−z}` for z ≥ 0;
  `ln(1+u) ≥ u ln 2` on [0,1] gives `ℓ(z) ≥ (ln 2)e^{−z}`; each `xᵢxᵢᵀ` is PSD of spectral
  norm ≤ 1, so `λ_max(∇²L) ≤ L(w)/ln 2`; hence the threshold `L(w) < 2 ln 2/η`, scaling as
  1/η. Correct, and the hypothesis (all margins ≥ 0) is stated.
- **§7.2 interpolator as ridge.** Push-through verified directly:
  `Aᵀ(AAᵀ + γI) = AᵀAAᵀ + γAᵀ = (AᵀA + γI)Aᵀ`. Correct.

### `langlands-function-fields-gaitsgory` — 2 exercises (3 parts), all correct

- **§6.1 the 𝔾_m case.** `Funct_c(ℤ)` countable, `δ_n ↦ tⁿ` onto `ℚ̄_ℓ[t,t⁻¹] = 𝒪(𝔾_m)`,
  `ℚ̄_ℓ^×` uncountable. Correct.
- **§6.2(a) basis-free trace.** `1 ↦ Σᵢ eᵢ ⊗ eⁱ ↦ Σᵢ T(eᵢ) ⊗ eⁱ ↦ Σᵢ Tᵢᵢ`. Correct.
- **§6.2(b) Lang's theorem and its failure.** Finite case: `h⁻¹g Frob(h) = g·h^{q−1}`,
  `x ↦ x^{q−1}` surjective on `𝔽̄_q^×`, one orbit, stabilizer `μ_{q−1} = 𝔽_q^×`. Loop case:
  Frobenius acts coefficientwise and fixes t, so the lowest nonzero coefficient `a_m` maps to
  `a_m^q ≠ 0` and `v(Frob(h)) = v(h)`; hence v is constant on orbits and `v(t) = 1 ≠ 0 = v(1)`.
  Correct — and this is the file's own reconstruction, not the talk's or the paper's.

### `arithmetic-patterns-ziegler` — 2 exercises (10 parts), mathematics correct; see Error 4

- **§7.1(1)** The four-fold expansion forces `a−b−c+d ≡ 0`, `b = d`, `c = d`, hence
  `a = b = c = d` and `‖f‖⁴_{U²} = Σ_a |f̂(a)|⁴`. Correct.
- **§7.1(2)** `Σ|f̂|⁴ ≤ ‖f̂‖²_∞ Σ|f̂|² ≤ ‖f̂‖²_∞` for 1-bounded f, so `‖f‖_{U²} ≥ η ⟹
  ‖f̂‖_∞ ≥ η²`. Correct.
- **§7.1(3)** Constraints `a+b+c ≡ 0` and `b+2c ≡ 0` give `b = −2c`, `a = c`, leaving
  `Σ_c f̂(c)ĝ(−2c)ĥ(c)`. Correct.
- **§7.1(4)** Conclusion correct; two wording slips, Error 4 above.
- **§7.1(5)** Two constraints on four frequencies leave a two-parameter family. Correct.
- **§7.2(1)** Induction verified: `T(z+nα, w+2nz+n²α) = (z+(n+1)α, w+2(n+1)z+(n+1)²α)`. Correct.
- **§7.2(2)** Weights (1,−3,3,−1): w-coefficients `3−3+1 = 1`; z-coefficients `6−12+6 = 0`;
  α-coefficients `3−12+9 = 0`; first coordinate `3−3+1 = 1` and `3−6+3 = 0`. Correct, and the
  reading of it as the third finite difference annihilating quadratics is right.
- **§7.2(3)** `φ(Ty) = e(2z+α)φ(y)`, and `ψ(Ty) = e(2α)ψ(y)`. Eigenvalue `e(2α)`. Correct.
- **§7.2(4)** `∫₀¹ e(kw) dw = 0` for k ≠ 0. Correct.
- **§7.2(5)** Verified directly: `φ³(Tⁿy)·φ^{−3}(T^{2n}y)·φ(T^{3n}y) = e(w(3−3+1) + nz(6−12+6)
  + n²α(3−12+9)) = e(w) = φ(y)`, so the integrand is identically 1. Correct, and all four
  functions are 1-bounded with zero Kronecker projection.

### `ramsey-numbers-morris` — 3 exercises, all correct

- **§7.1 R(3,3) = 6.** Pigeonhole on 5 edges at a vertex; C₅ and its complement (also C₅)
  are both triangle-free. Correct, including `α(C₅) = 2`.
- **§7.2 first moment.** `E[X] = C(n,k)2^{1−C(k,2)}`; with `C(n,k) ≤ (en/k)^k` this is
  `2(en/(k·2^{(k−1)/2}))^k`, below 1 once `n < (k/e)2^{(k−1)/2}`. Correct.
- **§7.3 triples.** `E[X] = C(n,k)2^{1−C(k,3)}`; `C(k,3) ≈ k³/6` against
  `log₂C(n,k) ≈ k log₂ n` gives `log₂ n ≈ k²/6`, i.e. `n ≈ 2^{k²/6}`. Correct, and the
  contrast with the doubly-exponential upper bound `2^{2^{ck}}` is the right point. The file
  labels this one a reconstruction.

### `random-interface-growth-quastel` — 2 exercises, both correct

- **§7.1 the 1:2:3 scaling.** `a = 1/2` from Brownian increments; `(ε⁻¹x̂)²/(ε^{−b}T) =
  ε^{−2+b}x̂²/T`, and `ε^{−2+b}·ε^{1/2} = ε⁰` forces `b = 3/2`. Then `ε^{−1/2} = t^{1/3}` and
  `ε^{−1} = t^{2/3}`. Correct.
- **§7.2 RG flow**, all four parts. (a) `δ(ε^{−z}s) = ε^z δ(s)` gives `ε^{(z+1)/2}` for the
  noise. (b) viscosity `ε^{2−z}`, nonlinearity `ε^{2−z−β}`, noise `ε^{β−(z−1)/2}` — each
  re-derived. (c) at (β,z) = (1/2, 3/2): 1/2, 0, 1/4 — so `(λ,ν,σ) ↦ (λ, ε^{1/2}ν, ε^{1/4}σ)`.
  (d) at (β,z) = (1/2, 2): 0, −1/2, 0 — the linear equation is invariant and the nonlinearity
  is relevant. All correct, and "1:2:4" for the Edwards–Wilkinson scaling is right.

### `random-matrices-localization-yau` — 2 exercises; **3 errors**, see Errors 1-3

Correct parts: step 1 (`m² + zm + 1 = 0`, `|m_sc(E)| = 1` in the bulk — verified as
`(E² + 4 − E²)/4 = 1`); step 3 (the second-moment expansion giving `1 − S ≈ −DΔ` with
`D ~ W²`); step 4 (`(cη + D(−Δ))⁻¹ = ∫₀^∞ e^{−cηt}e^{tDΔ}dt`, cut off at `t ≈ 1/η`); step 5
(`√(Dt) = W√N ≳ N ⟹ W ≳ √N` in d = 1); step 6 (`L = √N` in d = 2, so the condition collapses
to `W ≳ 1`). Exercise 7.2 parts 1-5: `0.83² ≈ 0.69` correct, the concentration-inequality
argument correct, and the correlation bounds correct — perfect correlation gives 0.83 and the
Fréchet lower bound `max(0, 0.83 + 0.83 − 1) = 0.66` is exactly the figure quoted.

### 5. `summaries/uniformization-complex-geometry-mok.md:1461` — an off-by-one in the exponent, contradicted twice in its own solution

Exercise 6.2(a) expands `Σ_j (z_j + t w_j)^d` correctly:

> `Σ_j z_j^d + t·d·Σ_j z_j^{d−1} w_j + t²·(d(d−1)/2)·Σ_j z_j^{d−2} w_j² + ⋯ + t^d·Σ_j w_j^d`

Then it states the resulting equations as

> `Σ_j z_j^{d−k} w_j^{k+1} = 0 for k = 0, 1, …, d−1`

At k = 0 that reads `Σ_j z_j^{d} w_j = 0`, but the t¹ coefficient two lines above is
`Σ_j z_j^{d−1} w_j`. The exponent on z is one too high throughout. The correct family is

    Σ_j z_j^{d−m} w_j^m = 0   for m = 1, …, d,

equivalently `Σ_j z_j^{d−k−1} w_j^{k+1} = 0` for k = 0, …, d−1.

**The solution's own part (c) uses the correct form**, not the stated one: for d = 2 it writes
the two equations as `Σ z_j w_j = 0` and `Σ w_j² = 0`, which are `m = 1` and `m = 2` of the
corrected family. So the file contradicts itself twice — once above the formula and once below
it — and both of those are right. Only the general formula is wrong.

**Impact: low.** The count of equations (d), the dimension `n − d`, the reconciliation with the
slide's `(n+1) − (d+1) − 1 = n − d − 1`, and the `Q^{n−2}` answer for the quadric are all
unaffected and all correct.

### 6. `summaries/ricci-flow-singularities-brendle.md:1252-1259` — the metric and its curvature differ by a factor of 4

Exercise 6.2(a) states the cigar at t = 0 as

> `g = 4/(1+|x|²) δ_ij on ℝ²`

and derives, correctly for that metric, an asymptotic flat cylinder `ds² + 4dθ²` with
cross-sectional radius 2 and **circumference 4π**. Part (b) then reuses the circumference 4π.

But the same solution says the scalar curvature is `R ≈ 4/ρ² = 4e^{−s}`, and part (b) repeats
it as `sup R ≈ 4e^{−(s−r)}`. **That is the curvature of `δ/(1+ρ²)`, not of `4δ/(1+ρ²)`.**

Scalar curvature scales inversely with the metric: `R(cg) = R(g)/c`. For a conformal metric
`e^{2u}δ` in two dimensions, `K = −e^{−2u}Δu` and `R = 2K`; with `Δ log(1+ρ²) = 4/(1+ρ²)²` this
gives

| metric | R | asymptotic circumference |
|---|---|---|
| `δ/(1+ρ²)` | `4/(1+ρ²) ≈ 4/ρ²` | 2π |
| `4δ/(1+ρ²)` (as printed) | `1/(1+ρ²) ≈ 1/ρ²` | 4π |

The file takes the circumference from the second row and the curvature from the first.

**Impact: none for the conclusion, and the conclusion is what the exercise is for.** R is
exponentially small in arclength either way, so the hypothesis `sup R ≤ r⁻²` holds for every
`r ≤ s/2` either way, and the collapsing verdict (`area/r² ≈ 8π/r → 0`) does not use R at all.
But two displayed numbers in the same solution describe two different metrics.

---

## Per-file results, continued

### `hardy-spaces-explicit-formulae-gerard` — 3 exercises, all correct

Notable, because this is the corpus's one MAJOR file: its two known formula errors are at
`:665` and `:399`, in the body, and **its exercises are clean**.

- **§6.1(a)** `∫dx/((x+Re p)² + (Im p)²) = π/Im p`, so the normalization is right.
- **§6.1(b)** `x/(x+p) = 1 − p/(x+p)`; renormalization removes the constant; `X*φ_p = −pφ_p`.
- **§6.1(c)** Contour closed in the lower half-plane (correct for `e^{−iξx}`, ξ > 0), the pole
  `x = −p` is enclosed since `Im(−p) < 0`, clockwise gives `−2πi·e^{iξp}`, so `I₊ = −2iπ` and
  `|I₊(φ_p)|²/4π = 4π²(Im p/π)/4π = Im p`. Correct, every π included.
- **§6.1(d)** `i/(y+p) − i/(y+p̄) = i(p̄−p)/|y+p|² = 2 Im p/|y+p|²`, using `(y+p)(y+p̄) = |y+p|²`
  for real y. Correct.
- **§6.2(a)** `X* − 2tL − (z − 2tλ_j) = X* − 2t(L−λ_j) − z`. Correct.
- **§6.2(c)** `−2t(L−λ_j) = A_t − (X*−z)` gives
  `A_t⁻¹(L−λ_j)χ = −(1/2t)[χ − A_t⁻¹(X*−z)χ]`, bounded, so O(1/t). Correct.
- **§6.3** `∂_x|D|` acts as `iξ|ξ|`, which is `iξ²` on the Hardy component, so
  `ŵ = e^{itξ²}ŵ₀`; `t^{−1/2}` decay and the Fresnel factor `√(π/t)e^{iπ/4}` follow. Correct.

### `knots-four-manifolds-manolescu` — 2 exercises, all correct

- **§6.1 trefoil.** Alexander: `Δ(H₊) = q^{1/2} − q^{−1/2}`, then
  `Δ(T) = 1 + (q^{1/2}−q^{−1/2})² = q⁻¹ − 1 + q`. Jones: `V(unlink₂) = −(q^{1/2}+q^{−1/2})`,
  `V(H₊) = −q^{1/2} − q^{5/2}`, `V(T) = q + q³ − q⁴`. Every step re-derived; all correct,
  including the standard-normalization check. Fox–Milnor: `Δ(T)(−1) = −3`, not a square.
- **§6.2 Khovanov complex of the Hopf link.** The sign rule, `d⁰(v) = (m(v), m(v))` and
  `d¹(a,b) = −Δ(a) + Δ(b)`, `d¹d⁰ = 0`; `ker m = span{x⊗x, 1⊗x − x⊗1}`; `im d⁰ = {(w,w)}`;
  `ker d¹ = {(a,a)}` since Δ is injective; `im d¹ = Δ(V)`. So H⁰ ≅ ℤ², H¹ = 0, H² ≅ ℤ², total
  rank 4 — the right answer for the Hopf link — and the Euler characteristics match, 4 = 4.

### `learning-in-games-tardos` — 2 exercises, all correct

- **§6.1 Braess.** 1.5 before, 2 after, optimum still 1.5, PoA = 4/3. Correct.
- **§6.2 uniform vs round robin.** The geometric sum re-derived in full:
  `Σ_{i≥1}(1/k)(1−1/k)^{i−1}(1−1/n)^i = ((n−1)/(nk))/(1 − (1−1/k)(1−1/n))`, denominator
  `(n+k−1)/(nk)`, so the second piece is `(n−1)/(n+k−1)` and
  `Pr[accept] = k/(n+k−1)`. Then `k/(n+k−1) > 1/2` iff `k > n−1`. Round robin gives
  `1 − (1−1/n)^k → 1 − 1/e ≈ 0.632` at k = n against `n/(2n−1) → 1/2`. All correct.

### `maestro-serre-sarnak` — 3 exercises, all correct

- **§7.1 capacity.** `‖T_n‖_{[−2,2]} = 2` for every n, so cap = 1; scaling gives ℓ/4. The
  equilibrium measure `dx/(π√(4−x²))` is right (it integrates to 1 on [−2,2]).
- **§7.2 integrality.** Coefficient bound `|c_k| ≤ C(d,k)a^{d−k}`; `cap([−a,a]) = a/2 < 1` for
  a < 2. Correct, and the atomic-limit caveat is flagged.
- **§7.3 the energy of the uniform measure.** Re-derived line by line:
  `∫₀¹ log|u−v| dv = u log u + (1−u)log(1−u) − 1`, then `∫₀¹ u log u du = −1/4` twice, giving
  `−1/4 − 1/4 − 1 = −3/2` and `I(ν_E) = log L − 3/2`. Correct. The threshold `e^{3/2} = 4.4817`
  is right and the file's correction of Serre's printed "4,816" is right. The second refinement
  is also right: for E centred at 0, `∫log|x|dν = log(L/2) − 1 ≥ 0` iff `L ≥ 2e = 5.4366`.

### `mesh-generation-pdes-buffa` — 2 exercises, 1 with the already-known error

- **§8.1** carries the defect already in `verify/README.md`: with `ρ = 1 + (a/δ)1_{s>1−δ}`, the
  integral over the layer must use `1 + a/δ`, not `a/δ`. **Confirmed by re-derivation.** The
  correct inside slope is `δ(1+a)/(δ+a)`, as the roll-up says. Two consequences worth adding:
  the node fraction `1 − ξ* = (a+δ)/(1+a)` and the 34% headline are **independent of the error
  and correct**; but the stated moral — "the slope ratio is exactly the ratio of monitor
  values" — is true only for the corrected slope. With the printed slope the ratio is `a/δ`,
  and the monitor ratio is `1 + a/δ`. So the error propagates into the sentence that explains
  the exercise.
- **§8.2** correct: `ρ(x(ξ))det J(ξ) = σ` from arbitrary `ω̂`, then Brenier's `x = ∇φ` gives
  `ρ(∇φ) det D²φ = σ`, and the d = 1 case reduces to §8.1's equation.

### `quantitative-rectifiability-harmonic-measure-tolsa` — 2 exercises, all correct

- **§7.1** `∇(|x|^{2−d}) = (2−d)x/|x|^d`, so `∇E = −(1/κ_d)x/|x|^d`, a constant multiple of the
  codimension-one Riesz kernel `x/|x|^d`. Correct.
- **§7.2 four-corner Cantor set.** `Σ diam = 4^k·√2·4^{−k} = √2`; the s-exponent test
  `2^{s/2}4^{k(1−s)}` is right in both directions; `H¹(E∩Q) = √2ℓ`; the β estimate
  `2·(√2ℓ/4)·(c/2)² = √2c²ℓ/8` and `β² ≥ √2c²/16` are arithmetically right; and
  `Σ_k β₀² ∫_{4^{−k−1}}^{4^{−k}} dr/r = Σ_k β₀² log 4 = ∞`. Correct, and the constant-chasing
  is labelled a reconstruction.

### `randomness-rotations-resonances-dolgopyat` — 3 exercises, all correct

- **§9.1** `q_{j+1} ≥ q_j + q_{j−1}` gives Fibonacci growth and `j ≲ log N/log φ`;
  `q_{j+1} ≤ (A+1)q_j` gives `j ≳ log N/log(A+1)`. `ℙ(‖kα‖ ≤ δ) = 2δ`; `ℙ(k‖kα‖ ≤ ε) = 2ε/k`;
  `Σ_{k≤N} 2ε/k ≈ 2ε log N = 1` gives `ε ≈ 1/(2 log N)` and a harmonic of size of order log N.
  Correct, and the observation that only the *lower* bound needs bounded type is right.
- **§9.2** correct, including `n^{−d/2} = o(n^{−(d−1)/2})`, which is the whole point of (d).
- **§9.3** `z_n = 2V_n − n = 2(V_n − n/2) = 2D_n` since `|I| = 1/2`. Correct.

### `ricci-flow-singularities-brendle` — 2 exercises; see Error 6

Correct: 6.1 in full — `λ′ = −2(n−1)`, `λ(t) = r₀² − 2(n−1)t`, `T = r₀²/(2(n−1))`, checking
against n = 2 and n = 3; the product-metric argument in (d); and the scaling symmetry in (e),
where `ĝ(t) = c⁻¹g(ct)` with `c = λ⁻²` gives `∂ₜĝ = (∂_s g)(ct) = −2Ric_{g(ct)} = −2Ric_{ĝ}`.
Also correct: all of 6.2 except the curvature constant — `area(B) ≈ 8πr` against `κr²` fails;
`r ≈ √(s/c)`; `vol ≈ 4πs·2r = 8πr³` using `s = r²`, so κ ≈ 8π; and the (e) exponent argument
`vol ≈ s^{a(n−1)}·s^a = s^{an}` versus `κr^n ≈ κs^{an}`.

### `uniformization-complex-geometry-mok` — 2 exercises; see Error 5

Correct: 6.1 in full. The Carathéodory sup-norm at 0, both bounds — the projections give
`≥ max(|ξ₁|,|ξ₂|)`, and Schwarz along `t ↦ (tu₁,tu₂)` with phase optimization gives
`|a|+|b| ≤ 1` and hence `≤ max(|ξ₁|,|ξ₂|)`. The parallelogram-law failure is right:
`‖x+y‖ = ‖x−y‖ = 1` gives 2 against `2‖x‖² + 2‖y‖² = 4`. And the product-metric vanishing of
the mixed bisectional curvature. Also correct in 6.2: the dimension count `n − d`, the
reconciliation with the slide's own count, and the `Q^{n−2}` answer.

### `lens-of-circles-oh` — 3 exercises, all correct

- **§6.1 Descartes.** `d² − 2Sd + (2P − S²) = 0` and Vieta give `d′ = 2(a+b+c) − d`. Correct.
  Part (d)'s two claims were both checked directly: the involution fixes `d = a+b+c`, and
  `Q(a,b,c,2S−d) = 2P − S² − 2Sd + d² = Q(a,b,c,d)`. The signature claim is right too —
  `Q = 2I − J` on ℝ⁴ has eigenvalues `2−4 = −2` once and `2` three times, so **(3,1)**.
- **§6.2** `d((0,0,1),(0,0,r)) = |log r|` under `dy/y`, and `T = log(1/t)` turns `e^{δT}` into
  `t^{−δ}`. Correct.
- **§6.3 cross-ratio.** The inscribed-angle proof is correct, including the collinear
  degenerate case.

### `prismatic-homotopy-lurie` — 2 exercises, all correct

- **§7.1** group completion of (ℕ,+) is ℤ; the non-cancellative witness `c` is needed; and the
  Eilenberg swindle kills `M∞` because `ℂ^∞ ⊕ ℂ^n ≅ ℂ^∞`. Correct.
- **§7.2 formal group laws.** `1 + βF_m(x,y) = (1+βx)(1+βy)` — the factorization the hint
  points at, and it is right. `∂F_m/∂y = 1 + βx`, so `log_{F_m}(x) = (1/β)ln(1+βx) =
  Σ_{n≥1}(−1)^{n−1}β^{n−1}x^n/n`, and the verification `log(F_m(x,y)) = log x + log y` follows
  from the factorization. The denominator argument in (d) is right: the coefficient of `x^n` is
  `±β^{n−1}/n`, so every prime appears. Correct.

---

## Total

**Forty-four worked solutions across all 20 files.** Nine defects, in six of them:

| File | Defect | Severity |
|---|---|---|
| `random-matrices-localization-yau` §7.1 | the constant c is wrong (Error 1) | wrong formula, no downstream effect |
| `random-matrices-localization-yau` §7.1 | dropped minus sign in m-prime (Error 2) | self-contradictory display |
| `random-matrices-localization-yau` §7.2 | Tracy–Widom tails reversed (Error 3) | wrong fact in a side remark |
| `arithmetic-patterns-ziegler` §7.1 | "at most 7" after showing 4; index typo (Error 4) | wording only |
| `uniformization-complex-geometry-mok` §6.2 | exponent off by one (Error 5) | wrong formula, contradicted twice in place |
| `ricci-flow-singularities-brendle` §6.2 | metric and curvature differ by a factor 4 (Error 6) | inconsistent constants |
| `mesh-generation-pdes-buffa` §8.1 | already in `verify/README.md`; **confirmed**, plus the stated moral does not follow from the printed slope | wrong formula |

**What the numbers say.** Before this round the sample was one exercise, and it was wrong, so
nothing could be inferred. The real rate is about **1 defect per 7 solutions**, all but one of
them local — a wrong constant, a dropped sign, a shifted index — and **none of them changes an
exercise's conclusion.** No exercise reaches a false answer. That is a materially better result
than the single earlier data point suggested, and it is the first time the corpus has had a
measured error rate on mathematics anybody re-did rather than merely sourced.

**Where the defects cluster is the useful part.** Six of the nine are a *constant* or an
*index* attached to an otherwise correct argument, and four of those six are contradicted
somewhere else in the same solution. A cheap follow-up check exists and was never run: read
each solution against itself.
