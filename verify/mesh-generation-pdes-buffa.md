# Verification - mesh-generation-pdes-buffa
verdict: MINOR
uncited_external_claims: 0
unsupported_speaker_claims: 0
title_check: PASS - chair Susanne Brenner introduces "Annalisa Buffa from EPFL" who "will present a plenary lecture on new challenges in numerical approximation of PDEs". Front-matter title matches exactly.
gap_honesty: PASS - both [Gap:] blocks sit where the captions are genuinely silent or hesitant; no gap was silently filled, and every reconstruction carries an italic "this is mine / this is from paper X" marker.

## Summary of evidence gathered
Sources fetched and read in full: ar5iv.labs.arxiv.org/html/2307.06265 (Hinz-Buffa companion),
arxiv.org/html/2501.12965v2 (Marcinno et al. application paper, incl. Tables 2-4), arxiv.org/abs metadata
for 6 further arXiv ids, Crossref for 2 journal references, and the full 51 KB caption transcript.
Result: 8 of 8 arXiv ids resolve to exactly the paper described; 2 of 2 journal citations exact; every
number copied from Tables 2-3 exact; every sampled speaker quote present in the captions.

## Findings

### F1 (MINOR) - `summaries/mesh-generation-pdes-buffa.md:465-467`: quoted eq (33) is truncated inside the very gap it is meant to fill
The [Gap:] block declares "the scaling of the penalty weights in $h$" unrecoverable, then quotes companion
eq (33)'s penalty as `eta sum_j int_{gamma_j} [[grad x_i]] : [[grad phi_i]] dGamma`. The paper's eq (33)
carries a `1/h(gamma_jl)` weight on that integral - i.e. the h-scaling the gap says is missing is printed
in the equation being quoted, and was dropped in transcription. The paper also states the practical value
`eta = 10` ("facing geometries with characteristic length scales of O(1)"), unreported.
Why it matters: a reader implementing Method A takes the gap at face value and re-derives a weight that was
available. Also, quoting a displayed equation with a factor removed weakens the file's other verbatim
claims by association.
What would settle it: it is settled - arXiv:2307.06265 eq (33), reproduced in full in the evidence log below.

### F2 (MINOR) - `summaries/mesh-generation-pdes-buffa.md:907-916`: dropped term in the tutorial's own §8.1 exercise
The exercise sets rho = 1 + (a/delta)*1_{s>1-delta} but then integrates rho as a/delta inside the layer,
omitting the +1. The exercise's headline answers survive intact (sigma = 1+a, xi* = (1-delta)/(1+a), node
fraction (a+delta)/(1+a) ~ 34%), but the bad integral is at :907, the displayed map x(xi) for xi > xi* at :910 and the claimed inside slope at :916
delta(1+a)/a is wrong; the correct slope is delta(1+a)/(delta+a). Ironically the correct value is the one
that makes the tutorial's own stated principle ("the slope ratio is exactly the ratio of monitor values")
come out exactly, since (1+a)/[delta(1+a)/(delta+a)] = 1 + a/delta = rho_in/rho_out.
Why it matters: it is a worked solution presented for the reader to check, and it is off. It is the
tutorial's own mathematics, not a claim about the talk, so it is an internal-consistency defect rather than
a provenance defect.
What would settle it: it is settled - recompute int_0^x rho for x > 1-delta.

### F3 (MINOR) - `summaries/mesh-generation-pdes-buffa.md:63-65` and `:1246-1248`: "consistently" overstates the caption damage
The tutorial says the captions render Hessian as "action" "consistently, throughout the entire technical
core" and "in every sentence describing the method". The substitution is real and the correction is right
(4 occurrences, incl. "the Miranda-Talenti estimate ... says that the action can be controlled by the
Laplace"), but the captions also spell "Hessian" correctly 6 times, in exactly some of the passages the
tutorial rebuilds ("I penalize the jumps of the gradients and the Hessian"; "I define uh Ritz
representation for the gradients, for the Hessian"; "the determinant of the Hessian uh equal to F").
Why it matters: it inflates the claimed reconstruction burden, and a reader checking the transcript will
immediately find counterexamples to a stated-as-absolute claim.
What would settle it: `grep -oi Hessian transcripts/D2_RHzeWcgk_transcript.txt | wc -l` returns 6.

### F4 (COSMETIC) - `summaries/mesh-generation-pdes-buffa.md:258-259`: misdescribes why the Cordes inequality is absent from the companion
"The companion paper states the condition and the normalizer ... but the fetched HTML does not render the
inequality cleanly." The companion names the condition ("the so-called Cordes condition [37]", spelled
Cordes with an acute accent in the paper; ref [37] = Maugeri-Palagachev-Softova, Wiley-VCH 2000) and gives
gamma(B) := tr(B)/||B||_F^2 in eq (15), but it never displays any Cordes inequality at all - it defers to
[37]. So the inequality is absent, not badly rendered. The substance is unaffected: the inequality is
correctly sourced to Smears-Suli, cited exactly right.

### F5 (COSMETIC) - `summaries/mesh-generation-pdes-buffa.md:319`: Winslow functional missing its 1/2
Given as `int tr(G)/det J`; companion eq (8) is `(1/2) int_{hatOmega} tr(G)/det J dxi`. Irrelevant to a
minimiser, noted only for completeness.

### Not findings (checked and clean)
- Every theorem/rate/constant not in the transcript carries a citation. Zero uncited external claims.
- Zero unsupported speaker claims across ~25 sampled block quotes.
- Zero fabricated citations. The riskiest-looking id in the file, arXiv:2607.15024 (a July-2026 preprint),
  resolves to a real paper by the named author with the stated date.
- The numeric class the caller flagged - Tables 2-3 of arXiv:2501.12965 - is exact on all six figures.

## Self-report audit
The writing agent's §12 "Note on the tutorial process" is, on the whole, HONEST AND SUBSTANTIALLY COMPLETE.
Independently verified as true:
- All 11 rows of its caption-correction table are real caption text (I found each in the transcript).
- Its claim that Rado-Kneser-Choquet and Winslow come from the companion and not the podium: TRUE - both
  names occur zero times in the transcript, and she really does say only "one of the fundamental theorem of
  analysis".
- Its four "reconstructed, and how to verify" items are each marked in the body text as well as in §12, and
  each is what it says it is (Smears-Suli for the Cordes inequality; its own derivation for
  (tr A)^2 - |A|_F^2 = 2(det J)^2; its own one-line derivations for the square/ball Neumann conditions;
  classical for the Miranda-Talenti two-liner).
- Its six-row gap table matches the six [Gap:]/marked spots in the body; no seventh undeclared gap surfaced.
- It declares the alphorn maker's name unverified rather than guessing - correct, the captions say "Gerard"
  and credit Le Temps, and that is all that is recoverable.
- Its §2.1 "absences" (FEEC/de Rham, defeaturing, h-adaptive hierarchical splines) check out: none of those
  topics appear in the transcript, and all four supporting arXiv ids are genuine Buffa papers on those
  topics.

It UNDER-REPORTS in three places:
1. **F1** - §12's gap table repeats the claim that the penalty h-scaling is unrecoverable and credits
   companion eq (33) with supplying only "the gradient-jump half". Eq (33) in fact supplies the h-scaling
   too (1/h(gamma_jl)) and the paper supplies the practical eta = 10. The self-report inherits, rather than
   catches, the transcription loss.
2. **F2** - the §8.1 algebra slip is nowhere acknowledged. §12 lists what was reconstructed and what was
   gapped, but has no category for "my own worked exercise may contain an error", so an incorrect displayed
   formula ships unflagged in a section that invites the reader to check the work by hand.
3. **F3** - §12 re-states the "consistently / in every sentence" claim about the Hessian mistranscription
   and adds "Anyone reading the raw transcript will be lost at exactly this point." That is an OVER-report
   of the damage (and therefore of the value added), not an under-report of a gap, but it is the one place
   where the self-report is measurably at odds with the transcript.

Nothing in the self-report is a fabrication, and nothing it claims to have taken from a source was taken
from somewhere else. The three items above are omissions and overstatement, not misattribution.

## What I could not check
- Anything that was on a slide and not in the captions: the exact discrete H^2 norm and penalty exponents
  of the Method A coercivity theorem, the explicit form of the discrete Hessian H_h, the discrete
  Monge-Ampere system, the singular-value sweep plot. The tutorial marks these itself; I can confirm the
  captions are silent, not what the slides showed. Only the video frames would settle it.
- Whether the mathematics is TRUE (per the brief). I checked sourcing, not correctness - with the single
  exception of F2, where the tutorial's own displayed integral contradicts its own displayed definition and
  no external knowledge is needed.
- The alphorn maker's identity and the Le Temps article. Same position the tutorial takes.
- Whether Buffa has an ICM 2026 proceedings paper. The tutorial says there is none on arXiv; I did not
  search arXiv exhaustively (session web-search budget exhausted) and cannot confirm or refute the negative.
(Peruso/Dirichlet item resolved - see below, moved out of this list.)

### RESOLVED - arXiv:2607.15024 IS the Dirichlet problem, tutorial :796-800 - PASS
Abstract: "we introduce and analyze a finite element framework for smooth solutions of the Dirichlet
Monge-Ampere equation in two dimensions. The proposed schemes combine a discrete Hessian reconstruction
with a local projection..." - matches the tutorial's description exactly, including "Dirichlet" and the
discrete-Hessian apparatus it says is shared with §3-5. Correctly labelled "somebody else's paper, not
hers, and it is Dirichlet."

---

## Detailed evidence log

### VERBATIM CHECK at :375 — PASS (with one notation substitution)
Claim: "Restored verbatim from the companion paper, arXiv:2307.06265, equations around (9)–(11)."
Fetched ar5iv.labs.arxiv.org/html/2307.06265. The paper has, verbatim:
- (10) `\Delta_x \xi = 0 in \hatOmega, s.t. x = F on \partial\hatOmega` — tutorial :361 matches.
- (11) `i\in{1,2}: A(\partial_\xi x) : H(x_i) = 0, s.t. x = F on \partial\hatOmega` — tutorial :364 matches,
  except the tutorial writes `D^2 x_i` where the paper writes `H(x_i)`. The paper defines
  `H(y)_{ij} = \partial^2 y/\partial\xi_i\partial\xi_j`, so this is a symbol swap, not a content change.
- `A(\partial_\xi x) := ((g22, -g12),(-g12, g11))` — tutorial :370-371 matches character-for-character.
- `g_{ij} = \partial_{\xi_i} x \cdot \partial_{\xi_j} x` (defined just before eq (7)) — tutorial :373 matches.
Verdict on the verbatim claim: substantively HONEST. The only deviation is D^2 for H, which the tutorial
uses consistently for the Hessian throughout.

### CROSS-CHECK — Theorem 1 (Radó-Kneser-Choquet), tutorial :332-336 — PASS
Paper: "Theorem 1 (Radó-Kneser-Choquet). The harmonic extension of a homeomorphism from the boundary of a
Jordan domain Omega ⊂ R^2 onto the boundary of a convex domain \hatOmega ⊂ R^2 is a diffeomorphism in
Omega." Tutorial block-quote at :334-336 is word-for-word identical. PASS.
Also: paper states "the same result is no longer true in R^3 [33]", corroborating the tutorial's :352 quote
of the speaker's 2D-only caveat.

### CROSS-CHECK — eq (33) interior penalty, tutorial :465-466 — number correct, formula TRUNCATED
Paper eq (33) is
  L^DG_eta(B,x,phi) := sum_k int_{\hatOmega_k} \Delta phi_i B : H(x_i) dxi
                      + eta sum_{gamma_jl in Gamma^I} (1/h(gamma_jl)) int_{gamma_jl} [[grad x_i]] : [[grad phi_i]] dGamma
The tutorial quotes the penalty as `eta sum_j int_{gamma_j} [[grad x_i]] : [[grad phi_i]] dGamma` and DROPS
the `1/h(gamma_jl)` weight. It drops it inside a [Gap:] block whose stated content is "the scaling of the
penalty weights in h" — i.e. the tutorial declares a gap that the very source it cites in the same sentence
fills. The paper also fixes eta = 10 in practice ("facing geometries with characteristic length scales of
O(1), we utilise eta = 10"), which the tutorial does not report.

### CROSS-CHECK — Cordes condition attribution, tutorial :44 and :256-259 — SUBSTANTIALLY CORRECT
(I first scored this an overclaim because a plain grep for "Cordes" hit only two bibliography entries.
That was my error: the paper body spells it "Cordés", with an acute accent. Corrected below.)
Tutorial :44 lists "the Cordes condition" among things the companion paper "contains, by name". TRUE:
paper §2.2 reads "as long as B satisfies the so-called Cordés condition [37]. In R^2 the Cordés condition
is implied by (14)", where [37] is Maugeri-Palagachev-Softova, *Elliptic and Parabolic Equations with
Discontinuous Coefficients*, Wiley-VCH 2000, and (14) is plain uniform ellipticity.
Tutorial :262 normalizer: paper eq (15) is exactly `gamma(B) := tr(B)/||B||_F^2`. Exact match.
One small inaccuracy remains at :258-259: "the fetched HTML does not render the inequality cleanly."
The paper never displays a Cordes inequality at all — it names the condition and defers to [37]. So the
inequality is absent, not badly rendered. This does not change the substance: the tutorial correctly
sources the inequality itself to Smears-Süli, and that citation checks out exactly against the companion's
ref [40]: "I. Smears, E. Süli, Discontinuous Galerkin finite element approximation of nondivergence form
elliptic equations with Cordes coefficients, SIAM J. Numer. Anal. 51 (4) (2013) 2088-2106."
Severity: cosmetic.

### NUMERIC CHECK — "Tables 2-3" of arXiv:2501.12965, tutorial :609-614 — ALL EXACT
Fetched arxiv.org/html/2501.12965v2 (ar5iv had no copy). Tables 2 and 3 exist and are exactly what the
tutorial says they are: "Comparison between our approach, VMTK and Gmsh" for the single branch test case
(Table 2) and the bifurcation test case (Table 3).
Every figure the tutorial copies matches the source to the digit:
| tutorial claim | paper | match |
| single branch, ours: SJ min/mean/max 0.785 / 0.979 / 0.999 | Table 2 "ours (~570k)": 0.785, 0.979, 0.999 | EXACT |
| 99.5% of cells in [0.9,1] | §4.1.1: "99.5% of the cells have a value between 0.9 and 1" | EXACT |
| bifurcation, ours: 0.488 / 0.907 / 0.999 | Table 3 "ours (~64k)": 0.488, 0.907, 0.999 | EXACT |
| "more than 80% of structured cells have negligible skewness" | "More than 80% of all structured cells exhibit minuscule skewness" | EXACT |
| "more than 30% of VMTK and Gmsh cells exceeding the preferred skewness limit of 0.5" | "both VMTK and Gmsh create meshes wherein more than 30% of the cells exceed the preferred skewness limit of 0.5" | EXACT |
No transposition, no rounding drift, no mislabelled column. This is the risk class the caller flagged and it
is clean. The tutorial also correctly distinguishes these published per-case statistics from the talk's
spoken population-scale figures, and marks the discrepancy in a [Gap:] block at :616-620 rather than
blending them.

### SPEAKER-QUOTE SPOT CHECKS — all verified against transcripts/D2_RHzeWcgk_transcript.txt
Every block quote I sampled is present in the captions, word-for-word or with only filler/stutter removed
(the tutorial removes "uh", "I mean", doubled words — legitimate and non-substantive):
- :495-498 "three or four parameters ... random numbers out of my code" — present verbatim.
- :528 "a few pages" proof, localization + approximation of A by a constant per chart — present:
  "It's a few pages proof which is based on localization first, approximation of A via constant in each
  chart, and then well-pose..."
- :541 "this problem is open. I cannot prove the stability on the local charts" — present verbatim.
- :545-547 "But, I am a numerical person..." — present verbatim.
- :561-562 "That's the only way I can sort of prove it ... I'm confident" — present.
- :558 "no singular value falls below a fixed positive threshold — the blue line" — present:
  "refining the mesh and basically no no singular values for the three patches goes below the blue line".
- :573 Jacobian "from 1 to 5" — present: "The Jacobian goes from one to five so this is an admissible mesh".
- :523-524 second-order vs fourth-order equation and "makes my matrices much worse" — present verbatim.
- :576-578 "they perform in a similar way ... I really prefer the second one" — present.
- :473-474 "the patches can float and the Miranda-Talenti estimate cannot be true" — present verbatim.
- :453 "no way around it ... my space will just be too big" — present.
- :662-663 tokamak "fourth-order finite difference scheme for the reduced Braginski system" and full
  tensor product / no singular points — present verbatim.
unsupported speaker claims found in this pass: 0.

### CAPTION-CORRECTION CLAIM at :62-65 ("Hessian" -> "the action") — TRUE but OVERSTATED
The substitution is real and the tutorial's correction is right. The captions contain, e.g.,
"the Miranda-Talenti estimate ... says that the action can be controlled by the Laplace" — unambiguously
the Hessian. "the action" occurs 4 times in that sense.
But the tutorial says the captions do this "consistently, throughout the entire technical core." They do
not: "Hessian" is correctly transcribed 6 times, including in exactly the passages the tutorial rebuilds
("I penalize the jumps of the gradients and the Hessian"; "I define uh Ritz representation for the
gradients, for the Hessian"; "the determinant of the Hessian uh equal to F"). So the captions alternate.
The correction is sound; the word "consistently" overstates the damage. Cosmetic.

### CITATION AUDIT — every arXiv id in the file resolved; ZERO fabrications
Checked each against arxiv.org/abs citation metadata:
- 2307.06265 — Hinz & Buffa, PDE-Based Parameterisation Techniques for Planar Multipatch Domains. Confirmed.
- 2501.12965 — Marcinnó, Hinz, Buffa, Deparis, spline-based hexahedral mesh generator for patient-specific
  coronary arteries. Confirmed (fetched full text).
- 2607.15024 (:799) — "Fully discrete least-squares splitting scheme for the Monge-Ampère equation: finite
  element analysis and convergence", Peruso, Anna, 2026/07/16. Author, date and topic all EXACT, including
  the tutorial's "submitted 16 July 2026". This was the riskiest-looking id in the file (a 2026 preprint)
  and it is real.
- 2209.12500 (:487) — Gallistl, Dietmar; Tian, Shudan, "Continuous finite elements satisfying a strong
  discrete Miranda--Talenti identity", 2022/09/26. Title EXACT as the tutorial paraphrases it.
- 2107.02023 (:157) — Buffa, Gantner, Giannelli, Praetorius, Vázquez, "Mathematical foundations of adaptive
  isogeometric analysis". Matches "whose mathematical foundations she co-authored".
- 2007.11525, 2312.15968, 2512.20124 (:151-153) — all real Buffa defeaturing / a posteriori estimator
  papers (2020, 2023, 2025-12). Matches the "her 2020-2026 output is full of it" claim.
- Smears & Süli, SIAM J. Numer. Anal. 51 (2013) 2088-2106 — matches companion ref [40] exactly.
Each is properly labelled as external ("that reference is mine, not hers", "somebody else's paper, not
hers"). uncited_external_claims from this pass: 0.

### CROSS-CHECK — Mahendiran credit, tutorial :589-591 — PASS
arXiv:2501.12965: "a fast and robust deep learning based algorithm (the one presented in Mahendiran et al.
2024) segments the selected vessel tracts in each frame, computing the centerline and vessel diameter for
each projection. The epipolar lines of these two ICA projections..." — the tutorial's summary is accurate,
including the epipolar-intersection detail.

### NUMERIC CHECK — §7.6 test numbers against the transcript — ALL PRESENT
- Young's modulus 1000 everywhere, 1 on the smile (:840-841) — "the Young's modulus is 1,000 everywhere
  except on the smile, where it becomes one". EXACT.
- "two orders of magnitude" gain, uniform-mesh error "stagnates" (:846-847) — "the error stagnates ... I
  basically gain two order of magnitudes". EXACT.
- conductivity 1000 outside / 1 inside, 32^3 mesh, monitor = conductivity (:854-856) — "a Laplace with a
  conductivity that is 1,000 outside the blob and one inside ... on a 32 by 32 by 32 mesh both Cartesian
  and adapted via optimal transport where I use as monitor the conductivity itself". EXACT.
- "reminiscent of a cancer growth model ... definitely not yet" (:853) — present verbatim.
- "completely spurious" on the uniform mesh, no error plot because "this geometry is too complex to
  compute the right solution" (:858-861) — present.
- cofactor matrix positive definite (:833) — "I just need to design iteration so that the cofactor is
  positive definite, otherwise I may get out of my well-posedness context". EXACT.
- nested/"two embedded" Newton converging quadratically (:834) — present.
- "it's a choice to make my life simple. I could definitely have taken other choices" (:966-967) — present.

### SMALL ALGEBRA SLIP in the tutorial's OWN exercise, §8.1 at :906-916 — MINOR
The exercise defines rho(s) = 1 + (a/delta) * 1_{s > 1-delta}, so inside the layer rho = 1 + a/delta.
The solution then writes, for x > 1-delta, "int_0^x rho = (1-delta) + (a/delta)(x-(1-delta))" — it drops
the "1" part of rho inside the layer. Correct value: (1-delta) + (1 + a/delta)(x - (1-delta)).
Downstream consequences:
- sigma = 1 + a — still CORRECT ((1-delta)*1 + delta*(1+a/delta) = 1+a).
- xi* = (1-delta)/(1+a) — still CORRECT (uses only the outside branch).
- node fraction (a+delta)/(1+a), "about 34% of the nodes in 1% of the domain" for a=0.5, delta=0.01 —
  still CORRECT (0.51/1.5 = 0.34).
- The displayed x(xi) for xi > xi* at :910 and the "slope delta(1+a)/a inside" claim at :915-916 are the
  affected pieces. With the correct integral the inside slope is delta(1+a)/(delta+a), whose ratio to the
  outside slope (1+a) is 1 + a/delta = rho_in/rho_out — i.e. the stated PRINCIPLE ("the slope ratio is
  exactly the ratio of monitor values") is right and only the displayed formula is off by the dropped 1.
  For delta << a the two agree to leading order, which is presumably how it slipped through.
This is the tutorial's own pen-and-paper exercise, not a claim about the talk or a source, so it is an
internal-consistency defect rather than a provenance defect. Everything the exercise concludes is correct.

### §12 CAPTION-CORRECTION TABLE (:1231-1244) — every row verified in the transcript
| tutorial's claimed caption text | found in transcript? |
| "the action" (Hessian) | YES — "the discrete action", "the action piece by piece minus a jump term", "we can control the patch by patch action with the Laplace patch by patch plus a jump". All three phrases the tutorial quotes at :1246-1248 are present verbatim. |
| "the brainy theorem" | YES — "we have the brainy theorem that tells us that such a minimizer exists and it is a gradient of a convex functional of a complex of a complex potential" |
| "a convex functional of a complex potential" | YES — same sentence |
| "inf sub condition" | YES — "what in applied mathematics we call an inf sub condition. So, I have a specific test function that is the Laplace of U" (also confirms the :213-215 quote) |
| "failed fields modeling" | YES — "the failed fields modeling. Failed fields modeling it's nowadays there are phase fields models..." — the tutorial's stated basis (she says "phase fields" correctly moments later) is exactly right |
| "Suzanne Brenner" | YES — "I'm Suzanne Brenner from Louisiana State University". Correction to Susanne C. Brenner (LSU) is right |
| "quasi-linear PDEs in the divergence form" | YES — verbatim; and "a second-order uh PDE in non-divergence form where A is a piecewise regular matrix" also present, so the tutorial's substantive correction at :383-387 is confirmed twice over (companion eq (11) says "nondivergence form" explicitly) |
| "Willis circle" | YES — "This is the Willis circle" |
| "Swiss corns" / "cone" | YES — "Gerard is a producer of Swiss corns... played in the Swiss Alps"; "optimize the shape of my cone" |
| "Braginsky" | YES — "the drift reduced Braginsky equation"; note the captions also get "Braginskii" right at first mention |
| "L minus one where L is the degree" | YES — "bring the regularity up to L minus one where L is the degree of the polynomial" |
Also verified: "Radó-Kneser-Choquet" and "Winslow" appear ZERO times in the transcript, confirming :1256-1257
("named from the companion paper, not from the podium"), and she does say "one of the fundamental theorem
of analysis that tells me that if omega hat is convex, in fact, X can be chosen as the inverse of an
harmonic map" — the :329-330 quote is faithful. "Gerard" and "Le Temps" both present, and the tutorial
correctly flags the name as unverified.

### GAP HONESTY — PASS
Both [Gap:] blocks sit where the captions really are silent or ambiguous:
- :461-467 (Method A discrete norm, penalty scaling, mu_1/mu_2 ranges): the captions carry the shape of the
  theorem ("coercive in this uh discrete norm where I have the action patch by patch and then I also have a
  control on the jump") and no formula. Correctly marked.
- :616-620 (cohort figures): correctly describes the captions as hesitant. Transcript: "We have 12,000 we
  have a database of 12,000 patients with around 1,000 meshable vessels" — she does restart the sentence,
  exactly as claimed, and the numbers 12,000 / ~1,000 / "successful over 99% of the vessel" / "97% of the
  elements have a Jacobian that goes from 0.9 to 1" / "the skewness of the element is also very small" are
  all present verbatim, matching :600-606.
No silently-filled gap found. Where the tutorial supplies mathematics the talk did not, it says so in an
italic parenthetical every time (:256-259, :375-377, :410-412, :487-490, :786-788), and §12 re-lists them.
Two open problems (nonlinear-Neumann Monge-Ampère well-posedness; Method B stability on jump charts) are
correctly treated as the speaker's own content, not as caption failures — both are verbatim in the captions.

### REMAINING CITATION CHECKS — both EXACT
- Budd, Huang, Russell, "Adaptivity with moving grids", Acta Numerica 18 (2009) 111-241 (:715-717, :1067):
  Crossref confirms title, journal, vol 18, pp 111-241, 2009-05, authors Budd/Huang/Russell. EXACT.
- "CMAME 445, October 2025" for arXiv:2501.12965 (:51-53, :1071): Crossref confirms Computer Methods in
  Applied Mechanics and Engineering, vol 445, article 118153, 2025-10, Marcinnó/Hinz/Buffa/Deparis. EXACT.

---

## Round 2 — exercises re-derived, 2026-08-18

Both worked solutions re-derived by hand.

**§8.1 — the known error is confirmed.** With `ρ = 1 + (a/δ)·1_{s>1−δ}`, the integral across
the layer must use the full monitor value `1 + a/δ`, not `a/δ`. The correct inside slope is
`δ(1+a)/(δ+a)`, exactly as `verify/README.md` records.

**Two things to add to that entry.** First, the headline is safe: the node fraction
`1 − ξ* = (a+δ)/(1+a)` does not involve the mis-integrated term, so **34% of nodes in 1% of the
domain is correct**. Second, the error propagates into the sentence that explains the exercise.
The file says "the slope ratio is exactly the ratio of monitor values" — which is true for the
corrected slope (`(1+a)` over `δ(1+a)/(δ+a)` is `1 + a/δ`, the monitor ratio) and **false** for
the printed one (which gives `a/δ`). Fixing the slope repairs the moral; leaving it breaks it.

**§8.2 is correct.** `ρ(x(ξ))·det J(ξ) = σ` follows from arbitrariness of `ω̂`, Brenier's
`x = ∇φ` gives `J = D²φ`, and `ρ(∇φ) det D²φ = σ`. The d = 1 reduction to §8.1's equation is
right, and so is the degrees-of-freedom count that motivates the transport ansatz.
