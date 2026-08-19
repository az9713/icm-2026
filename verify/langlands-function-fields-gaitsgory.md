# Verification — langlands-function-fields-gaitsgory
verdict: MINOR
uncited_external_claims: 1
unsupported_speaker_claims: 0
title_check: PASS — the introducer says "who will tell us about local and global Langlands conjectures over function fields", and the paper `arXiv:2509.24902` carries the same title.
gap_honesty: PASS — 3 `[Gap:` / discrepancy blocks, and where the talk and the paper disagree the file quotes **both** rather than choosing.

Round 2, 2026-08-18. Written and self-verified by the session that produced it; **not** in the
15-file tier 3 run. First independent check. Method: full read of
`summaries/langlands-function-fields-gaitsgory.md` against
`transcripts/aeZ0TpVvM5w_transcript.txt`. Companion `arXiv:2509.24902` not fetched.

This file is unusual in the corpus: the captions carry **no formula at all**, and the file
says so at `:56` and then sources every displayed statement to a numbered paper section. That
makes the provenance question sharper than usual and, on this reading, it is answered well.

## Findings

### 1. `summaries/langlands-function-fields-gaitsgory.md:1548` — the citation checker now fails on this file, and the failure is benign

`python verify/check_citations.py` exits 1 with:

```
100 arXiv IDs, 4 DOIs; 1 unresolved
  UNRESOLVED arXiv:2020.02998
    cited at summaries\langlands-function-fields-gaitsgory.md:1548
```

That is **not a defect in the tutorial**. Lines `:1548-1550` read:

> "**One error found in the paper.** Its bibliography lists [Zhu1] as arXiv:2020.02998, not a
> valid identifier (there is no month 20). The correct one is **arXiv:2008.02998** — X. Zhu,
> *Coherent sheaves on the stack of Langlands parameters*, 7 August 2020."

The file is quoting a bad identifier **in order to correct it**, and its reasoning is right:
arXiv ids are YYMM and there is no month 20.

**Consequence for the repo, and it matters after close-out.** `HANDOFF.md` says "Exit 1 means
a citation stopped resolving." That is now false — exit 1 is the steady state, and a future
reader will either chase a non-bug or start ignoring the checker. Either the string needs an
allowlist in `check_citations.py` with a comment pointing here, or the HANDOFF line needs to
change. Recorded in `verify/INTERNAL-CONSISTENCY.md` and in the round-2 summary.

### 2. `summaries/langlands-function-fields-gaitsgory.md:487` — the file overrules the speaker on an attribution, correctly and in the open

The talk says, verbatim: "the idea to consider this category goes back to **Jean-Pierre
Serre 40 years ago**, and then it came back to prominence 10 years ago in the work of David
Ben-Zvi, David Nadler."

The file keeps Ben-Zvi and Nadler and **replaces Serre with G. Laumon**, citing the paper's
Remark 1.1.8 and a 1987 *Duke* paper, with the substitution flagged in place and again in the
process note.

I am recording this as a finding not because it is wrong — the paper outranks a caption
track, and this is exactly what the file should do — but because it is the only place in the
five files I checked in round 2 where a tutorial **contradicts an audible, unmangled
statement by the speaker**. "Jean-Pierre Serre" is not a caption corruption; it is what the
transcript says. A reader watching the video will hit the mismatch. The flag is there and it
is honest; a one-clause note that the speaker *said* Serre would close it completely.

### 3. `summaries/langlands-function-fields-gaitsgory.md:1160-1163` — an uncited pointer

"The full classification of isocrystals (**Dieudonné–Manin** for GL_n, **Kottwitz's B(G)** in
general) is not discussed in either the talk or the paper." Correct as far as I know, and
explicitly labelled as outside both sources — but it is an external claim with no citation,
in a file where everything else carries a locator.

## What I checked and found supported

Every one of these is in the caption track, verbatim or near-verbatim:

- The opening self-deprecation: "It may be too technical the way I prepared it. So I'll go
  twice as slow, three times as slow as planned and I might not be able to cover even the
  third of what's in the slides."
- **The Fourier anchor**, which the file makes its §2 and which is the speaker's own: "what's
  relevant here is really ℤ and 𝔾_m … some algebraic version of Fourier transform. And in
  general, the phenomenon of Langlands correspondence should be seen as some sort of
  **non-abelian Fourier transform**."
- The epoch joke's best line: "as society progressed, humans realized that if some objects
  can be organized in a family, they should."
- "It's not quite a scheme, it's not algebraic variety, it's what's called a **stack**."
- The étale fundamental group "as was defined by Grothendieck and Ray[naud] in the '60s" —
  the file's Raynaud reconstruction is marked as such.
- The ℚ̄_ℓ passage, near-verbatim, including "we have to take coefficients to be something
  that has something pro-finite inside".
- **Theorem 1 and the nine authors**: "it's the result of this series of papers by nine
  authors. I should say the names. I'm sure I'll omit somebody. Let me just not say the names
  because **I'm too jet-lagged**." The file reports the jet lag and declines to guess a
  nine-name list. That is the right call — AGKRRV has six authors and Gaitsgory–Raskin two,
  overlapping, so nine cannot be reconstructed from the repo.
- The discoverers of LS^restr: "independently by **Peter Scholze**, **Shen Wei Zhu** [Xinwen
  Zhu] and the authors of this paper. So, it's **Arinkin, myself, Kazhdan, Raskin, Rosenblum,
  Varshavsky**" — the file's six-name list is the speaker's own.
- The Hecke refusal: "I'm not going to say what Hecke operators are in this talk because it
  would take me just too long." The file's `[Gap:` at §4.6 is exactly this.
- For 𝔾_m, "this Bun G is just a Picard stack, and the subcategory consists of sheaves that
  are locally constant."
- The isocrystal origin: "I first realized it discussing with **Vincent Lafforgue** and then
  it was rediscovered by **Fargues and Scholze**, but in the analytic framework."
- **Arnaud Eteve** ("Arnaud Etam") for the finite-dimensional analogue.
- The Conjecture 7 peroration, verbatim: "this conjecture seven in some sense is the ultimate
  answer to the Langlands program over function fields. Langlands asked just describe the
  space of automorphic functions in terms of the spectral side. We can't quite do this. We
  performed a bunch of modifications, but at the end of the day we arrive at this conjecture
  seven."
- Independent proposal by "Shin Won Joon" = **Xinwen Zhu**, and the closing line "**And
  miraculously I've covered all my material. I wasn't even intending to.**" — both verbatim,
  and both the last words on the tape.
- "Park Shultz conjecture" = **Fargues–Scholze**, which the file records in its caption note.

**The talk-versus-paper discipline holds throughout.** Where the paper says more than the
podium — the characteristic-0 and GL_n cases of Theorem 1.4.6 (§4.4), the Chan–Kaletha–Zhu
independent method (§4.12), the Bernstein-centre caveat of Remark 2.6.11 (§4.11 and §7.4) —
the file says so in the sentence. Where the two constructions of Autom^enh differ, §4.13
quotes **both** and states what would settle it. That is the correct handling of a
discrepancy and it is rare in this corpus.

## Exercises re-derived

Both worked solutions were re-derived by hand. **Both correct.**

- **§6.1 the 𝔾_m case.** Funct_c(ℤ) has basis {δ_n} and countable dimension; δ_n ↦ tⁿ is a
  bijection onto ℚ̄_ℓ[t,t⁻¹] = 𝒪(𝔾_m); ℚ̄_ℓ^× is uncountable, so no isomorphism with a direct
  sum indexed by it exists. All four parts correct, and the continuous-spectrum reading in
  part (4) is a fair statement of the analogy rather than an overclaim.
- **§6.2(a) the basis-free trace.** 1 ↦ Σᵢ eᵢ ⊗ eⁱ ↦ Σᵢ T(eᵢ) ⊗ eⁱ ↦ Σᵢ eⁱ(T(eᵢ)) = Σᵢ Tᵢᵢ.
  Correct, and the list of ingredients it did *not* use is right.
- **§6.2(b) Lang's theorem and its failure.** Correct in both halves, and this is the single
  most valuable reconstruction in the file.
  Finite case: for abelian H, h⁻¹ g Frob(h) = g·h^{q−1}; x ↦ x^{q−1} is surjective on 𝔽̄_q^×
  because the field is algebraically closed, so there is one orbit; the stabilizer is
  μ_{q−1} = 𝔽_q^×. Loop case: Frobenius acts coefficientwise and fixes t, so for
  h = Σ aᵢtⁱ with lowest nonzero coefficient a_m, Frob(h) has lowest nonzero coefficient
  a_m^q ≠ 0 — hence v(Frob(h)) = v(h) and v(Frob(h)/h) = 0. So v is constant on
  twisted-conjugacy orbits, and v(t) = 1 ≠ 0 = v(1) gives more than one orbit. Lang fails.
  The file marks the whole computation as its own — "neither the talk nor the paper works it
  out; both simply assert that Lang's theorem fails" — and states the one step to check.
  That is exactly right, and the step it names is the step that carries the argument.

## What I could not check

- The companion `arXiv:2509.24902` was not fetched. **This is the heaviest such gap in the
  corpus**, because the file states outright that every displayed formula comes from the
  paper. Specifically unverified here: Lemmas 1 and 2 (§1.5.2), Corollary 1.5.8, Theorem
  1.2.3, Theorem 1.4.6, Conjecture 1.4.4, Remarks 1.5.4 / 1.5.9 / 2.6.11 / 3.5.10,
  Proposition 1.5.6, the LS^restr definition at §1.3.1, and Conjectures 2.5.12 / 2.6.10 /
  2.7.9 / 3.1.5 / 3.4.4 / 3.5.9.
- **The talk-to-paper numbering map** in §4.15 is labelled a reconstruction, and I could not
  test it: it is exactly the artefact that needs the paper.
- Whether the file's correction `arXiv:2008.02998` is the right identifier for Zhu's *Coherent
  sheaves on the stack of Langlands parameters*. `check_citations.py` resolves that id
  elsewhere in the corpus, which is weak supporting evidence, not proof.
- AGKRRV1 Theorems 1.4.5, 14.4.3 and 24.1.4, cited by number.
- Whether the mathematics is true. Unchanged: this is a provenance check, and this file is
  the one where that limit bites hardest — it is 5/5 material stated almost entirely on the
  authority of a paper nobody in the verification chain has opened.
