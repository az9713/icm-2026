# Verification — optimization-theory-practice-wright
verdict: MINOR
uncited_external_claims: 3
unsupported_speaker_claims: 0
title_check: PASS — Wright from the podium: "I'd like to talk about optimization in its both theoretical and practical aspects."
gap_honesty: PASS — no `[Gap:` markers; the file instead names three unrecoverable items in §13 and does not guess them.

Round 2, 2026-08-18. This file was written and self-verified by the session that produced it
and was **not** covered by the 15-file tier 3 run. This is its first independent check.
Method: full read of `summaries/optimization-theory-practice-wright.md` against
`transcripts/Ep1TzZDOHnU_transcript.txt`. Companion `arXiv:2510.15734` not fetched.

## Findings

### 1. `summaries/optimization-theory-practice-wright.md:298` — a rate restated in a form the talk never used, uncited

The file prints, under the heading **"The gain, strongly convex case"**:

> O(κ log(1/ε)) → O(κ^{0.786} log(1/ε))

The podium says something different. Wright compares **convex** rates, and states the silver
result as an epsilon exponent, not a condition-number exponent:

> "he was able to prove that you get epsilon accuracy for a convex function in order epsilon
> to the minus one half iteration. So this improves over the epsilon to the minus 1 that you
> get just from naive gradient descent. It also improves on what you get from the silver step
> size result which is epsilon to the .786."

Both statements are real Altschuler–Parrilo results, and 0.786 is the same exponent
(log_{1+√2} 2 = 0.7864) in both. But the strongly-convex κ form is **not in this talk**, and
the file carries no citation for it — no arXiv id, no paper title. This is the uncited-external
class the brief calls the dangerous one, even though the claim is almost certainly true.

Repeated at `:1291` (self-test question 4) and `:1104` (§10.2), so a reader meets it three times.

**What would settle it:** cite Altschuler and Parrilo, *Acceleration by Stepsize Hedging*
(arXiv:2309.07879), and say which of the two rates came from the podium.

### 2. `summaries/optimization-theory-practice-wright.md:224` — a constant sharpened past the podium, uncited

File: "currently **ω ≈ 2.371339**". Transcript: "currently that exponent stands at about 2.37".
The extra four digits are external. They are consistent with the published value, but no source
is given. Low impact — nobody's belief changes — but it is the same class as finding 1.

### 3. `summaries/optimization-theory-practice-wright.md:214-216` — a perturbation set stated wider than the podium

File, on smoothed analysis: "You bring *your* LP — your A, b, c. They are allowed to add small
Gaussian perturbations of variance σ² to the entries."
Transcript: "give us your A, B, and C. We're allowed to make random small Gaussian
perturbations to the elements of **A and B**."

The file then builds its §3.2 punchline on perturbing "only b and c — leaving A alone", which
the transcript does support. So the drift is in the setup sentence only, and it slightly
overstates what classical smoothed analysis perturbs. Cosmetic, but it sits directly under the
contrast the section exists to draw.

## What I checked and found supported

Every one of these is in the transcript, in the tutorial's own words or close to them:

- The thesis sentence, and the Roger Fletcher quotation, "Optimization is a fascinating blend
  of theory and computation, heuristics and rigor" — verbatim.
- Smoothed analysis 1/σ dependence "from about 30 to about 1.5" — verbatim, including both numbers.
- "if you could reduce matrix multiplication to order n², there is an interior point method that
  takes order n^{2 + 1/18}" — verbatim, the exponent included.
- Adam's "over a quarter of a million" citations — verbatim.
- The Hoffman constant as the basis of first-order LP convergence theory — verbatim.
- Muon's discarded Σ justified as "a trust region method where you define the radius … in the
  spectral norm" — supported.
- Double descent, implicit bias (credited to Bartlett's plenary "yesterday"), and Weinan E's
  plenary "at the last ICM" — all three supported.
- The PL condition, including the "step will be big enough" consequence — supported.
- Griewank's cubic regularization predating the complexity motivation — supported.
- Nemirovski and Yudin "throw up their hands" on global non-convex minimization — supported.
- The ICML AI-assisted PEP workflow "a couple of weeks ago" — supported.
- Silver's long step at condition number 64, "every 8th or 16th step", possibly uphill — supported.

**The §13 correction table is honest.** 14 caption corrections, and the file separates
"verified" from "reconstructed" (Parrilo, Weijie Su) and names one it refuses to guess (the
higher-order lower-bound author, rendered "Joe"). It also records one **substantive** transcript
repair — the captions say the iterate has its "last n−k components nonzero", which is backwards
— and flags it in place at `:381`. That repair is correct: the components are zero, and that is
what makes the lower bound work.

## Exercises re-derived

Both worked solutions were re-derived by hand. **Both correct.**

- **§9.1 min–max LP reformulation.** λ = t(b − Ax) drives the inner objective to +∞ exactly when
  Ax ≠ b; on the feasible set the λ term vanishes. The stated conclusion follows.
- **§9.2 tridiagonal lower bound.** ∇f(0) = −e₁, so x₁ ∝ e₁; Tx₁ = α(2e₁ − e₂), so ∇f(x₁) has
  support {1,2}; induction gives supp(x_k) ⊆ {1..k}. And x\* = T⁻¹e₁ has (x\*)ᵢ = (n+1−i)/(n+1),
  every component nonzero, so the discarded tail is genuinely nonzero. The argument is sound as
  written.

## What I could not check

- The companion paper `arXiv:2510.15734` was not fetched, so paper-only claims — the six-section
  list at `:24`, and anything the file marks as "in the paper" — rest on the writing agent.
- Whether the two smoothed-analysis bounds are transcribed correctly from `arXiv:2504.04197`.
  They are cited, which is what this check tests; their exactness is not.
- Whether "Eleon Bach" is the right reconstruction of "Elon Bach". The file lists it under
  *verified*; I did not re-verify it.
- Clock claims. There are none in this file — it makes no assertion about where anything sits in
  the recording, which puts it outside the `CROSS-FILE.md` §1b defect entirely.
