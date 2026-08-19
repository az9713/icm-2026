# Verification — geometric-concepts-pde-otto
verdict: MINOR
uncited_external_claims: 1
unsupported_speaker_claims: 0
title_check: PASS — the introducer announces "geometric concepts in partial differential equations" and Otto repeats it: "I'll be talking about geometric concepts in partial differential equation."
gap_honesty: PASS — 2 `[Gap:` markers, both at genuine slide-only content, plus a full unrecoverable-mathematics ledger in §11 that names five more holes and grades each.

Round 2, 2026-08-18. Written and self-verified by the session that produced it; **not** in the
15-file tier 3 run. First independent check. Method: full read of
`summaries/geometric-concepts-pde-otto.md` against `transcripts/K8-O-FdUzGs_transcript.txt`.
Companion `arXiv:2401.05935` not fetched.

**This is the most carefully sourced file I checked in round 2.** Every displayed equation in
it is labelled as reconstructed, cited, or marked a gap. The finding below is the only one.

## Findings

### 1. `summaries/geometric-concepts-pde-otto.md:660` — a date and a description attached to a paper the talk names without either

File: "they found the idea in an **unpublished paper by Naddaf and Spencer**, a **1998
preprint on variance estimates in homogenization built on a spectral gap inequality**."

Transcript, in full: "that's what Antoine Gloria and I used when we started thinking about
quantitative homogenization and this basic idea we found in an unpublished paper by Naf
Spencer."

The year, the subject line and the mechanism are the file's, not the speaker's, and carry no
source. The claim is almost certainly right — the Naddaf–Spencer preprint is a real and
well-known object — but an unpublished 1998 preprint is exactly the sort of citation nobody
can check later, and the file elsewhere is scrupulous about this distinction.

**What would settle it:** cite the preprint by title, or drop the year and the description and
keep what Otto said.

### 2. `summaries/geometric-concepts-pde-otto.md:1361` — a correction-table row for a name the file never uses

The §11 table corrects "Terrence Tao" to "Terence **Tao**". Tao appears nowhere else in the
file. Harmless, but it means the correction table is not a table of corrections *made*.

## What I checked and found supported

The auto-captions in this talk destroy every proper noun including the speaker's own, so each
of these was located by idea and then matched to the mangled string:

- "kind of a **personal tour**" and the elementary-geometry-in-infinite-dimensions framing — verbatim.
- Arnold's geodesic reading, Gauss's theorem, negative sectional curvature, unpredictability.
- **Shnirelman** ("Alexander Schneerman") and non-existence of shortest geodesics in three
  dimensions and higher; **Brenier**'s relaxation.
- The variational time discretization, "we still have ill-posedness at this stage, minimizers
  will not exist", and the weak convergence to volume fractions.
- The relaxed dissipation as "the sum of the square of two metrics, weighted by the mobilities"
  — which is exactly why the file writes w₁, w₀ as symbols instead of numbers.
- **Almgren** ("Angrin") and **Luckhaus** ("Lucaus") for motion by mean curvature, before De
  Giorgi named minimizing movements.
- "**there's a minus sign missing here**" — verbatim, and the file's refusal to reproduce the
  formula is correct: the formula is not in the captions.
- The mixing zone "opens linearly in time", with profile and speed depending "in a very
  characteristic way on these mobilities" — verbatim.
- The non-convexity passage and the **Peter Bartlett** connection — verbatim, including "it's
  not always the best to choose the smallest time step size" and "we've inverted the order of
  relaxation. We first relax and then we let the time step size go to zero."
- The CMU / **Rich Jordan** / **Kinderlehrer** origin story, with the Kullback–Leibler energy
  and the Fokker–Planck conclusion, told as the *sequel* — verbatim, and the file's §3.7 point
  that the two-phase problem came first is Otto's own ordering, not the file's.
- The **Stephen Wright** neural-network reference at the end of part one.
- The **cast** image — verbatim: "we want to take a cast … the impressions which are the
  charts … and then discard the differential operator."
- **Jeremy Quastel**'s plenary invoked for the zoom-*out* contrast — verbatim.
- **Felix Klein's** philosophy for the transition maps — verbatim.
- **Armstrong and Smart** as the source of the low-regularity / high-order-approximability idea.
- The coherence remark, "gives rise to a new condition in low dimensions, not in high
  dimensions, and is well known in the field" — verbatim.
- "satisfies all the axioms to the last **iota**" ("to the last Yoda" in captions) — verbatim.
- The closing thermal-noise / quenched-noise summary — verbatim.

**The §11 ledger is the model the other 19 files should have followed.** It states what is
lost, how bad each hole is, and which exponents are spoken versus slide-only — and it is right
that the exponents are spoken: α, α−2, d/2, α+d/2, α+d/2−2 and the coherence condition all
appear in the caption track.

**Collaborator reconstruction is anchored, not guessed.** "Pablo, Marcos and Pablo" →
Linares, Tempelmayr, Tsatsoulis and "Luca and Marcus" → Broux, Tempelmayr are each tied to a
located publication, and the Oberwolfach report the file could not retrieve is recorded as a
404 rather than quoted.

## Exercises re-derived

Both worked solutions were re-derived by hand. **Both correct**, and §7.2 is the strongest
exercise in the corpus because it is fully checkable from the caption track alone.

- **§7.1 Fokker–Planck from the JKO scheme.** δE/δρ = log ρ + 1 + V; ρ∇(log ρ + V) = ∇ρ + ρ∇V;
  so ∂ₜρ = ∇·(∇ρ + ρ∇V) = Δρ + ∇·(ρ∇V). Correct, signs included. The closing remark — run it
  in flat L² and you get ∂ₜρ = −(log ρ + 1 + V), not a PDE — is also correct and is the point
  of the exercise.
- **§7.2 exponent bookkeeping, all four parts.** (a) α − 2 = −d/2 gives α = 2 − d/2; d=3 gives
  1/2, d=4 gives 0. Correct. (c) subtract 2: α + d/2 − 2. Correct. (d) α + (α + d/2 − 2) > 0,
  equivalently 2α > 2 − d/2, equivalently **α > 1 − d/4**. Correct. The table (3/4, 1/2, 1/4,
  0, negative) is arithmetically right at every row, and the conclusion that it binds only in
  low dimensions matches Otto's spoken remark. The bonus check is also right: substituting
  α = 2 − d/2 into α + d/2 − 2 gives exactly 0 for every d.

One thing the exercise does not say, and a reader might trip on it: at d = 1 the tabulated
threshold 3/4 cannot bind for **white noise**, because white noise there gives α = 3/2, outside
the file's own 0 < α < 1 window. The table is about general dilation-invariant ensembles, which
is correct, but the two paragraphs sit next to each other.

## What I could not check

- The companion `arXiv:2401.05935` was not fetched. Its abstract is quoted at `:55-60` as
  supporting the charts-and-transition-maps identification, and that quotation is unverified here.
- Whether "Saffman–Taylor" is the right reconstruction of "suffment … instability". The file
  marks it reconstructed, names Rayleigh–Taylor as the competing candidate, and does not
  assert. That is the correct handling; it just leaves the question open.
- The claim that no ICM proceedings paper exists. The file says it searched arXiv and the MPI
  MIS list. `HANDOFF.md` independently records that only 7 of 20 talks have an arXiv companion,
  which is consistent, but I did not re-run the search.
- The publication data in §3.7 (SIAM J. Math. Anal. 29 (1998) 1–17; CPAM 52 (1999) 873–915) and
  the Oberwolfach Report 33/2025 number.
- Whether the mathematics is true. Unchanged from the whole project: this is a provenance check.
