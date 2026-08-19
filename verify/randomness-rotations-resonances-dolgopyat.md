# Verification — randomness-rotations-resonances-dolgopyat
verdict: MINOR
uncited_external_claims: 2
unsupported_speaker_claims: 0
title_check: PASS — introducer says verbatim "his talk is entitled Randomness, Rotations, and Resonances"; speaker's own opening ("three problems", "each problem has elementary formulation", "some ideas from dynamical systems as well as some elementary geometric considerations") matches the tutorial's framing sentence word for word.
gap_honesty: PASS — the three declared gaps (the main new theorem of part two, every displayed formula, the equal-weights attribution) are exactly where the transcript is silent, and section 7.3's gap is if anything over-declared. No gap was silently filled: every reconstruction is labelled "Reconstructed" or carries a citation.
self_report_audit: HONEST — 24/24 caption garbles and 4/4 substantive corrections confirmed against the transcript; four small under-reports, three of which under-claim support the tutorial actually has. Detail in the "Self-report audit" section.

## Progress log (written as I read)

### Transcript lines 1-90 (intro + De Moivre-Laplace + question list + non-stationary setup)
Checked against tutorial §1, §3, §4.1-4.3.

SUPPORTED:
- "three problems ... elementary formulation ... ideas from dynamical systems as well as some
  elementary geometric considerations" — quoted correctly in the tutorial header.
- De Moivre/Laplace binomial origin of the LLT; Stirling; higher-order terms giving "Gaussian
  density multiplied by certain polynomials in Z divided by powers of standard deviation"
  (= the Edgeworth series of tutorial §4.4). Present verbatim in transcript.
- Gnedenko-Stone "this is the only obstruction" — present verbatim ("local limit theorem of
  Gnedenko and Stone says that this is the only obstructions").
- Haar measure on the line vs counting measure on a lattice — present ("hard measure" = Haar).
- Kolmogorov three-series ("free series") dichotomy: bounded variance => a.s. convergence;
  unbounded variance => CLT. Present verbatim.
- The three questions as listed in tutorial §3 (non-stationary; weak dependence; non-lattice
  higher-order/three values) match the transcript's own enumeration exactly.
- Process-note caption corrections #2 ("sum of 10 terms" -> n), #3 ("each sum ends" -> summand),
  "Kolmogorov free series", "hard measure" -> Haar: ALL CONFIRMED in transcript lines 20-75.

### Transcript lines 90-430 (rest of talk) — read in full
Every named block of the tutorial's §7 maps onto a real stretch of transcript:
- §7.1 Markov chains: "the theorem which we proved with Amrit Serik" [Omri Sarig]; the four-part
  decomposition (constant / largest[=gradient] / convergent / telescoping); "William Orange is a
  closed subgroup of R" with the three cases (whole line = CLT fails/tight; trivial = ordinary LLT;
  lattice = Laplace approximation); "for Markov case the expression is slightly more complicated,
  so I don't give it". ALL present.
- §7.2 pivot: "I'm not going to discuss this kind of dynamical systems in my talk because ... it's
  quite well understood what is causing this stochastic behavior" — the tutorial quotes this
  correctly (its wording "because it's quite well understood what is causing this stochastic
  behaviour" drops one "now" but is otherwise verbatim).
- §7.3 rotations: Beck 2011, sqrt(log m), drift c*log m and "99.9% of the time", c=0 for golden mean
  and sqrt(3), nonzero for sqrt(2) and sqrt(7), "depends on some special values of some L function";
  continued fractions, bounded type ("boundary type"), even continued fractions with the
  no-long-(+2,-2,+2,-2)-subword condition; Bromberg-Tsuchigai [Ulcigrai] extension; the staircase
  ("bricks one by two by one ... half shift"), the theta-group symmetry stated aloud as
  "any matrix with determinant one such that on the diagonal you have odd entries on off diagonal
  you have even entries"; Huber Huber and Barakh Weiss; Kesten; Ben Borda "last year"; the
  k*sin(pi k alpha) resonance count; Cauchy for typical alpha; Poisson limit theorem for strong
  resonances. ALL present.
- §7.4 Edgeworth: Cramer sufficient condition, the atom-of-size n^{-R/2} necessary condition,
  "proven by SN 1945" [Esseen], d+1 values, "my student Gaston Fernandez" [Kasun Fernando],
  "10 to the minus 10", "Zeglin transform of a random lattice", universality, the marked-lattice
  definition with the character, the linear-form/multinomial-weights slide, the resonance matrices,
  Siegel transform, equidistribution vs Poisson. ALL present.
- §7.5 synthesis: the closing summary is quoted in §2.1 and §1 and matches the transcript closely.

MAIN-RESULT CHECK (§7.3, the talk's new theorem): the transcript really does give only the shape —
beta = 2*alpha - 1, sign changes in its continued fraction expansion, sublinear growth => all values
equally likely, growth slower than sqrt(n) => 50/50 positive/negative. No coauthor is named aloud.
The tutorial's gap declaration matches the transcript.

---

## Citation spot-checks (WebFetch; the session's WebSearch budget was already spent, 200/200)

| cited in tutorial | checked against | result |
|---|---|---|
| Bromberg-Ulcigrai, arXiv:1705.06484 | arXiv abstract | EXACT. Confirms alpha and beta badly approximable, arbitrary initial point, "the renormalization associated to the continued fraction algorithm and dynamical Ostrowski expansions", and reduction "to a CLT for non-homogeneous Markov chains" — the phrase the tutorial quotes. Abstract also credits Avila-Dolgopyat-Duryev-Sarig and Dolgopyat-Sarig, supporting the tutorial's "temporal limit theorem" attribution. |
| Borda, arXiv:2303.08504, J. Mod. Dyn. 21 (2025) 327-359 | arXiv abstract | EXACT title, author, volume, year, page range. Abstract confirms "compute the normalizing constant in a classical limit law for the same Birkhoff sum due to Kesten, and dispel a misconception about its dependence on the test interval". NOT confirmed from the abstract: the value sigma = 1/(3 pi), and the quoted words "the dependence is illusory" (both would live in the body). |
| Dolgopyat-Fayad, arXiv:1211.4323, Deviations II. Boxes | arXiv abstract | EXACT. Verbatim: "normalized by ln^d N, converges as N to infinity to a Cauchy distribution. The key ingredient of the proof is a Poisson limit theorem for the Cartan action on the space of d+1 dimensional lattices." The tutorial's paraphrase is faithful. |
| Borda, arXiv:2512.03884 (cited only as "consistent with that literature") | arXiv abstract | EXACT. Real paper, submitted 3 Dec 2025, "Random walks and quadratic number fields". The quoted phrase "fundamental units and special values of zeta functions" is verbatim from its abstract, and the tutorial explicitly does not claim it verifies Beck's constants. |
| Dolgopyat-Fernando, arXiv:2303.10235 | ar5iv full text (partial) + Semantic Scholar reference list | Esseen 1945 is genuinely in the reference list. The marking chi is rendered as a homomorphism — see self-report audit item 4. |

Not checkable with the tools left: Beck, Period. Math. Hungar. 60/62; Kesten, Acta Arith. 7 (1961/62) 355-380; Hooper-Hubert-Weiss, DCDS-A 33 (2013) 4341-4347; Dolgopyat-Kanigowski-Rodriguez Hertz, Ann. of Math. 199 (2024) 1225-1292; Dolgopyat-Fayad GAFA 24 (2014) 85-115 and its quoted phrase "small divisors in the Fourier series of the discrepancy function"; and every internal equation/theorem number quoted from arXiv:2109.05560 (eqs. 2.25-2.26, Thms 3.8/4.3/4.4, the bound t >= pi/(3 ess sup |f|)) and from arXiv:2303.10235 (eqs. 1.1, 1.2, 1.5, Lemma 1.2, eq. 9.1).

---

## The two unverified names — what I found

### "some fire and Zolotarev" — a real locator found, the name itself still unresolved

Transcript, near the end of part three: "if you put uh equal weights when like there is a work with by some fire and Zolotarev which says that in this case you get casting type Cauchy distribution."

I fetched the full text of Dolgopyat-Fernando (arXiv:2303.10235) and found the matching sentence in Remark 1.3:

> "It is also interesting to consider counting with equal weight. In this case the analogue of Theorem 4(c) is obtained in [19]."

So the equal-weight result IS attributed in the primary paper, as reference [19]. ar5iv truncates before the bibliography, arxiv.org/html/2303.10235v2 returns 404, and the arXiv and Semantic Scholar APIs returned HTTP 429 — but the **Crossref record for the published version (DOI 10.1093/imrn/rnad088) carries the full numbered reference list**, and item 19 is:

> **[19] J. Marklof (2000), "The n-point correlations between values of a linear form."**

That is the paper the primary source credits for the equal-weight case, and it is a genuine match on subject: values of a linear form, equal weights, a Cauchy-type limit law. **But it is a single author and it does not sound like "some fire and Zolotarev".** So one of two things is true and I cannot tell which: either the caption garbled "Marklof" beyond recognition (Marklof's 2000 paper does carry an appendix by a second author, which could explain a two-name attribution), or Dolgopyat cited a different, older result that his own paper does not reference.

Verdict: **the source of the result is now identified (Marklof 2000, via ref [19]); the two spoken names are not.** What would settle it fully: the appendix author of Marklof (2000), or Dolgopyat's own slides. The writing agent was right not to guess, but it stopped one hop short — Remark 1.3 sits in a paper it quotes five times elsewhere, and Crossref serves the reference list without a login.

### "Dabrowski and Gorodetsky" — not resolved

Transcript: "there is a theorem of Dabrowski and Gorodetsky which says that for central limit theorem the the only abstraction comes from uh our additive functional can be split into uh the constant part, gradient part and convergent part."

The session's WebSearch budget (200/200) was already exhausted before I started, and every search engine I could reach through WebFetch served a CAPTCHA. But I did scan the companion book (ar5iv render of arXiv:2109.05560) for all five candidate spellings, and the result **partly corroborates the tutorial**:

- **Dobrushin: present**, and attached to exactly the right result — "Dobrushin proved a general central limit theorem for inhomogeneous Markov chains in [Do]", with a section headed "Proof of Dobrushin's central limit theorem".
- **Dabrowski, Gorodetsky, Gorodetskii: absent.** This confirms section 13's claim that "no such pair appears in the companion book's bibliography".
- **Gordin: also reported absent** by the same fetch. The tutorial's section 13 says "the technique behind both is Gordin's martingale-coboundary decomposition". The render of a 348-page book is likely partial, so I treat this as unresolved rather than as a contradiction — but it is the weakest link in the tutorial's reasoning, and the "Gordin" half of "Dobrushin and Gordin" is now less supported than the "Dobrushin" half.

Net: the **first** name is very likely Dobrushin. The second remains unidentified. The tutorial's decision to report the pair as unverified rather than write a guess into the body text is the correct call, and its stated reasoning is sound on the Dobrushin half.

---

## Self-report audit

The section 13 process note is, on the whole, honest and unusually complete.

I checked every one of its 24 caption garbles against the transcript, and all 24 really occur there, verbatim — including the ones that would have been easiest to invent: "Amrit Serik", "Konyukhovsky", "Gaston Fernandez", "Bromberg and Tsuchigai", "Huber Huber and Barakh Weiss", "Ben Borda", "proven by SN 1945", "Zeglin transform", "Ziggurat distribution", "William Orange is a closed subgroup of R", "boundary type", "failure Lindeberg", "hard measure", "Kolmogorov free series", "after more phase", "Dabrowski and Gorodetsky", "some fire and Zolotarev". Its four substantive corrections check out too: the transcript really does say "sum of 10 terms" (for n), "each sum ends" (for summand), "10 to the 10" (for 10^-10), and "interval L to be a irrational number" — and Dolgopyat's own later sentence, "if L is rational then this always holds ... just from definition of bounded type", is in the transcript exactly as the note claims. Its resolution note for "Zeglin transform" is verifiable as well: he does say "Siegel transform" correctly later in the same passage.

It under-reported four things. None is a fabrication; three of the four make the tutorial look LESS sourced than it actually is.

1. The inference count is wrong. Section 13 says "One inference of mine, flagged." There are at least two own-inferences flagged in the body: the theta-group / even-continued-fraction link (section 5.4) and the explanation that a repeating "+2, -2" block encodes a regular partial quotient 1 (section 5.3, marked "This parenthetical explanation is mine, not his"). The second is a substantive number-theoretic claim and section 13 does not list it at all.

2. "Dolgopyat never says this" (about the theta group) is too strong. He states the group aloud: "any matrix with determinant one such that on the diagonal you have odd entries on off diagonal you have even entries." That IS {A congruent to I mod 2}. Only the NAME "theta group" and the link to the even continued-fraction algorithm are the writer's. The self-report gives away support the tutorial genuinely has.

3. The section 7.3 gap list over-declares. It says the role of the initial point is unavailable, but the transcript does give it for l = 1/2 ("the first condition with uh all values of discrepancy are asymptotically equally likely holds with probability one with respect to initial condition but the second one holds with probability zero"), and the tutorial's section 7.3 body reports this correctly. The note is harsher on the tutorial than the evidence requires.

4. One self-report claim my evidence points AGAINST. Section 13 asserts that Dolgopyat-Fernando writes "homeomorphism chi : L -> T" twice in its section 1, and calls it the paper's typo. Two independent ar5iv fetches of arXiv:2303.10235 report the word as "homomorphism" and report no occurrence of "homeomorphism". This may be a version difference (ar5iv renders the latest arXiv version; the writer may have read v1 or the IMRN text) and the ar5iv render was truncated, so I cannot settle it. It affects no mathematics — the tutorial uses "homomorphism", which is correct and which Dolgopyat says aloud ("the character, which is like homomorphism from A to the torus"). But it is the one place where the self-report makes a checkable claim about a third party that my evidence does not support.

Nothing was over-reported and nothing was hidden. I found no claim attributed to Dolgopyat that is absent from the transcript, and no theorem, rate or constant presented as external without a citation, except Finding 1 below.

---

## Findings

### 1. MINOR — uncited external mathematics: the theta group / even continued fraction correspondence
`summaries/randomness-rotations-resonances-dolgopyat.md:511-514`

> "The subgroup {A in SL(2,Z) : A congruent to I mod 2} is the theta group. Its continued-fraction algorithm is the even continued fraction algorithm. That is why section 5.3 introduced even expansions."

Why it is a problem: this is a real, known result in number theory, not something derivable from the transcript, and it carries NO citation. It is honestly flagged as the writer's own inference, but "my inference" is not a source. It is also load-bearing for the tutorial's narrative — it is the only thing that explains why even continued fractions appear at all, and the talk's main new theorem is stated in terms of them.

What would settle it: a citation to the standard reference for the even continued fraction algorithm as the CF algorithm of the theta subgroup (the Romik / Schweiger literature on even continued fractions, or the Hooper-Hubert-Weiss staircase paper the tutorial already cites).

Related, same class, smaller: `:437-441`, the parenthetical claim that a repeating "+2, -2" block in an even expansion encodes a regular partial quotient 1. Flagged as the writer's, uncited, and not listed in section 13.

### 2. MINOR — two exact values quoted from a source I could only verify at the abstract level
`summaries/randomness-rotations-resonances-dolgopyat.md:884-888`

The tutorial states Borda's constant as sigma = 1/(3 pi) for all l in (0,1), attributes it to Theorem 2 of arXiv:2303.08504, and quotes the paper as saying the apparent dependence "has been cited by several authors... we show that the dependence is illusory."

Why it is a problem: the paper, its authors, its journal, volume, year and page range are all EXACT, and its abstract does confirm the substance (Kesten's constant computed; a misconception about dependence on the test interval dispelled). But the numeric constant and the direct quotation come from the body, which I could not open. A wrong constant here would be silent.

What would settle it: read Theorem 2 of arXiv:2303.08504.

### 3. MINOR — internal equation and theorem numbers quoted from two companions, none verifiable with the tools left
`summaries/randomness-rotations-resonances-dolgopyat.md:610-660` and `:920-960`

The tutorial quotes precise locators: eqs. (2.25)-(2.26) and section 4.2.1, Theorems 3.8, 4.3, 4.4 and the bound t >= pi/(3 ess sup |f|) from arXiv:2109.05560; eqs. (1.1), (1.2), (1.5), Lemma 1.2 and eq. (9.1) from arXiv:2303.10235.

Why it is a problem: these are the single largest block of external claims in the document, and precise numbering is exactly the kind of detail that drifts. The claims are properly CITED — this is not the dangerous uncited class — but they are unchecked.

What would settle it: open the PDFs of arXiv:2109.05560 and arXiv:2303.10235 and match each locator.

### 4. INFORMATIONAL — the framing is the speaker's own, not the tutorial's invention
The caller warned that no abstract is retrievable and the subject was derived from the transcript alone, so the framing had to be scrutinised. I scrutinised it and it holds up unusually well, because the framing is quoted rather than constructed:
- "three problems, each with an elementary formulation, each needing ideas from dynamical systems as well as some elementary geometric considerations" — the speaker's own second minute, verbatim.
- The three questions in section 3 are his own enumeration, in his order.
- The closing synthesis in sections 1, 2.1 and 7.5 (most random vs most regular; two different renormalizations; a small number of resonant harmonics; the same linear action on marked lattices; a dictionary) is a close paraphrase of his final two minutes, and the tutorial quotes the load-bearing sentences directly.
- The "field: limit theorems, NOT hyperbolic dynamics" call is correct and is anchored to his explicit refusal: "I'm not going to discuss this kind of dynamical systems in my talk."
I found no framing element imported from outside the transcript.

---

## What I could not check

- Whether any mathematics in the document is TRUE. I have no papers open beyond abstracts.
- Every internal locator (equation, theorem, lemma, figure and section number) quoted from arXiv:2109.05560, arXiv:2303.10235 and arXiv:2006.11748 — including the staircase Poincare map attributed to section 8.5 / eq. (40) of the survey, and the Siegel/Rogers mean-value identity attributed to eq. (9.1).
- Beck's Period. Math. Hungar. volumes and page ranges; Kesten's two references; Hooper-Hubert-Weiss's DCDS-A reference; the Dolgopyat-Kanigowski-Rodriguez Hertz Annals reference; the Dolgopyat-Fayad GAFA 24 (2014) 85-115 reference and its quoted "small divisors" phrase.
- The identity of "Dabrowski and Gorodetsky" and of "some fire and Zolotarev" (WebSearch budget exhausted; search engines CAPTCHA-blocked through WebFetch).
- Whether the SIAM proceedings chapter really is titled with four R's and paginated 35-50 (SIAM returns 403; the tutorial says this came from Crossref metadata, which is internally consistent with the null abstract it also reports).
- Whether the constants C(golden mean) = 0, C(sqrt 3) = 0, C(sqrt 2) != 0, C(sqrt 7) != 0 are correct — the tutorial itself declares these unverified and reports them as spoken. They ARE spoken: the transcript has them verbatim.
- Whether arXiv:2303.10235 says "homeomorphism" or "homomorphism" in its section 1 (see self-report audit item 4).

---

## Late addition: section 12 (self-test) checked
Lines 1376-1511 read in full after the first pass. All ten answer blocks restate material already
established and cited earlier in the document. No new external theorem, rate or constant is
introduced, and no new speaker attribution appears. Answer 4 correctly states Beck's hypothesis as
"l RATIONAL", i.e. it carries the correction rather than reverting to the caption's "irrational".
No change to the verdict.

---

# Round 2 — companion formula check, 2026-08-18

Round 1 was a transcript-and-citation-list check. This round fetched **both** companions via
ar5iv — Dolgopyat–Fayad, *Deviations of ergodic sums for toral translations*, `arXiv:2006.11748`
(part two) and Dolgopyat–Sarig, *Local limit theorems for inhomogeneous Markov chains*,
`arXiv:2109.05560` (part one) — and compared every passage the tutorial marks as quoted.

**Result: every quoted passage is correct**, and in one place the tutorial silently repairs a
typo in its own source. No change to the verdict.

## Part two — checked against `arXiv:2006.11748` §8.5 ("An application")

The section number and the figure number are both right: §8.5 is titled "An application" and
Figure 4 is captioned "Staircase surfaces."

| Tutorial `:458-470` | Survey §8.5 | Verdict |
|---|---|---|
| 2×1 rectangles, next brick's bottom-left at the **centre of the top edge** of the previous | "an infinite pile of 2×1 rectangles so that the left bottom corner of the next rectangle is attached to the center of the top of the previous one" | **correct** |
| sides differing by **2 units** horizontally or vertically identified | verbatim | **correct** |
| indexed by z ∈ ℤ, symmetry **G(x,y) = (x+1, y+1)**, **St/G is a torus** | verbatim, eq. before (40) | **correct** |
| credited to **Hooper, Hubert and Weiss** | the survey credits "[53]", which its bibliography gives as Hooper P., Hubert P., Weiss B., *Dynamics on the infinite staircase* | **correct** |
| cross-section Σ = union of the top edges, identified with 𝕋 × ℤ | verbatim | **correct** |
| Poincaré map `(x,z) ↦ (x + α, z + 𝟙_{[1/2,1)}(x) − 𝟙_{[0,1/2)}(x))`, `α = (tan θ + 1)/2` | same display, **with one typo** — see below | **correct as printed by the tutorial** |
| `ψ_A(p,z) = (Ap, z + τ(p))` | eq. (40), `ϕ(p,z) = (Ap, z + τ(p))` | **correct** (symbol renamed) |
| brick index `Σ_{j=1}^{m} τ(A^{-j} q)` | `z(ϕ^{-m}q̄) = a − Σ_{j=1}^{m} τ(ϕ_A^{-j} q)` | **correct**; on the torus coordinate ϕ_A acts as A, so `τ(ϕ_A^{-j}q) = τ(A^{-j}q)`. The tutorial says "quoted in form", which is the honest label |
| `m ≍ log N / log λ`, "a sum of m ≍ log N terms" | "m ≈ ln N / ln λ" | **correct** |
| the √log N conclusion: fluctuation is the square root of the number of renormalization steps | "a(x)/√m is approximately normal with zero mean and variance σ²" | **correct** |

### The tutorial is more correct than its source

The survey prints the Poincaré map as

    (x,z) = (x + α, z + χ_{[1/2,1]}(x) − χ_{[0,1/2)}(z))

with the **second indicator evaluated at z**, which cannot be right — z is the integer brick
index, the two indicators must test the same circle coordinate, and Figure 5's caption says so
in words ("Orbits starting from [1/2,1] go up while orbits starting from [0,1/2) have to go
down"). The tutorial prints `𝟙_{[0,1/2)}(x)`, i.e. it **fixed the typo**.

That is the right call, and it is the opposite of the failure mode this project worries about.
But `:476` introduces the display as "*Quoted from* Dolgopyat–Fayad, arXiv:2006.11748 §8.5",
and a silent repair inside a quotation is still a silent repair. One clause — "correcting an
evident typo in the source" — would make it airtight. Compare the companion-of-`gerard`
situation in the ranked fix list, where the same class of decision went the other way.

## Part one — checked against `arXiv:2109.05560`

`:613-627` quotes the three obstructions. **All three match the source clause for clause**, as
does the definition preceding them:

- *Algebraic range* — tutorial: "the smallest closed subgroup G ⊆ ℝ such that, after
  subtracting constants, f_n(X_n, X_{n+1}) ∈ G almost surely for every n". Source: "the
  smallest closed additive subgroup G ≤ ℝ for which there are c_n ∈ ℝ so that
  f_n(X_n,X_{n+1}) − c_n ∈ G almost surely for all n". **Correct.**
- **(I) Lattice behaviour**, G_alg = tℤ. **Correct.**
- **(II) Center-tightness.** Source: "Var(S_N) does not tend to infinity … in this case
  Var(S_N) must be bounded." Tutorial: "There are constants m_N with {S_N − m_N} tight.
  Equivalently Var(S_N) ↛ ∞." **Correct**, and the tutorial gives the tightness form the
  source's own name for the property implies.
- **(III) Reducibility**, f = g + c with c center-tight and G_alg(g) strictly smaller.
  **Correct.**
- `:625` "If none of the three occurs, all the classical asymptotics hold. That is the book's
  main theorem." Source: "One of our main results is that (1)–(3) hold whenever (I), (II),
  (III) fail." **Correct**, including the claim that the list is *complete* — the source says
  "a complete set of obstructions".

## What this round did not check

`arXiv:1211.4323`, `arXiv:1705.06484`, `arXiv:2303.08504` and `arXiv:2303.10235`, all cited
inline. The SIAM proceedings chapter `10.1137/25m1806971` remains unreachable (403), so the
talk's own written version is still unread by anyone in this verification chain.
