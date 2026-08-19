# Verification — random-interface-growth-quastel
verdict: MINOR
uncited_external_claims: 7 (2 with no source at all; 1 attributed by bare surname with no work cited; 4 carried on author+year with no title/id)
unsupported_speaker_claims: 1 ("nine minutes in" — a timestamp the caption-only transcript cannot support)
title_check: PASS — Quastel says aloud "so the talk's about um random interface growth"; front-matter title matches, and the tutorial itself flags the title as reconstructed from that sentence (lines 48-53).
gap_honesty: PASS — the three [Gap] markers sit where the transcript is genuinely silent, and both substantive caption corrections (GOE->GUE, t~n^2 inversion) are declared in place and again in §11; no silent fill found.

## Findings

(Most severe first. No invented theorem, no wrong title, no fabricated citation was found —
hence MINOR, not MAJOR.)

**F1 — `summaries/random-interface-growth-quastel.md:998` and `:1616`. Multi-time formulas
attributed to named people with no work cited, and the self-report claims otherwise.**
Line 998 credits multi-time space-time formulas for the KPZ fixed point to "Johansson and
Rahman" and "[Zhipeng] Liu". No arXiv id, DOI, title or year appears there or anywhere else in
the file (grep confirms; the only other hits are the two caption-correction rows at 1528-1529).
Line 1616 then asserts of exactly this class of results that "each is a pointer to a paper, and
the papers are cited". Problem: the reader is told a source exists that does not. Settled by
adding the Johansson-Rahman and Liu references, or by softening line 1616.

**F2 — `:1032` and `:994`. Two external claims with no citation at all.**
Line 1032: the KPZ fixed point "taking values in upper semicontinuous functions" — a technical
state-space claim from Matetski-Quastel-Remenik, stated inside the tutorial's own summary
Claim with no reference on the line. Line 994: "Pfaffians rather than determinants is the
signature of a boundary; it is the same GOE/GSE-versus-GUE distinction" — an interpretive claim
about symmetry classes, not spoken and not sourced. Settled by a citation each, or by marking
them as the writer's own reading.

**F3 — `:594-595`, `:314`, `:457-459`. Four external results carried on author+year only.**
Logan-Shepp and Vershik-Kerov 1977 (LIS ~ 2*sqrt(n)) and Baik-Deift-Johansson 1999 (fluctuation
n^{1/6}) are the two numbers that make §5.6's "t^{1/3} recovered from combinatorics" check work,
and neither carries a title, arXiv id or DOI. Same for "Murray Eden, 1961" (:314) and for
"Sasamoto (2005) and Borodin, Ferrari, Prahofer and Sasamoto (2007) solved it essentially by
linear algebra" (:457-459), where the added phrase "essentially by linear algebra" is a
characterisation of a method, not just an attribution. All four are well-known and plausible;
the brief asks for author+title+year, and title is missing. Settled by adding titles/ids.

**F4 — `:1058` vs `:466`, `:475`, `:1423`. Internal contradiction: epigraph vs hypograph.**
§6 step 3 says the biorthogonal family is expressed through "the probability that a random walk
hits the **epigraph** of the initial data". §4.4, §4.5 and §10 Q6 all say the region *under* h0,
i.e. the **hypograph**. Epigraph is the region above. The two passages describe the same step and
contradict each other; the tutorial does not notice. (A reflected parametrisation — TASEP
particle positions vs the height function are flips of each other — could in principle make
both wordings defensible in their own frames, but not as written here, where both claim to
describe the same object.) Settled by checking arXiv:1701.00018 / arXiv:2205.01433 §3.

**F5 — `:1480-1481`. "Quastel drops the KPZ equation nine minutes in."**
The transcript is a single unbroken caption block with no timestamps, and no other claim in the
tutorial is time-indexed. The number cannot come from the sources listed in the front matter.
Not necessarily wrong — but unsourced, and it sits inside the section whose job is to declare
what is and is not verified. Settled by watching the video or dropping the number.

**F6 — exponent/constant audit (the check the task asked for): PASS.**
Every exponent and constant in the tutorial is either spoken or cited on its own line.
Spoken: c*t linear growth, t^{1/3}, t^{2/3}, epsilon^{-3/2} time scaling, 1:2:3, 1:2:4
(Edwards-Wilkinson), "critical dimension" for 2+1, "like 10" solvable models. Cited, each on its
own line: the KP-II coefficients 1/2, 1/12, 1/4 (arXiv:1908.10353 eq. 1.7), the KdV reduction
(ibid. eq. 1.8), the matrix-KP commutator form (ibid. eq. 1.6), the Hopf-Lax/Airy-sheet formula
(ibid. eq. 1.3), the rescaling h_eps (ibid. eq. 1.2), the coefficient flow
(lambda, eps^{1/2}nu, eps^{1/4}sigma) (ibid. §1, and independently re-derived in §7.2), the
Lax/conjugation equations (arXiv:2205.01433 eqs. 5.1, 5.2), the scattering operator (ibid. 4.2),
the fixed-point Fredholm formula (ibid. 4.3). I found NO exponent or constant that is neither
spoken nor cited. The Tracy-Widom ensemble assignment (GUE narrow wedge / GOE flat) is corrected
against the captions and cited twice.

**F7 — speaker attribution audit: PASS apart from F5.**
Every "Quastel says / shows / stresses" I checked resolves to the transcript, including all
sixteen blockquotes. Where the tutorial goes beyond the podium it says so in the sentence itself
("It goes further than he says aloud", "the attribution in §5.7 is mine", "Where the two
disagree, I am quoting the thesis", "in your own vocabulary"). The two honest NEGATIVE claims —
he never says "stochastic Burgers equation", the talk never mentions Cole-Hopf or the stochastic
heat equation — both check out against the full transcript.

### Running log (sections 1-4)

- §1 (lines 104-113). Exponents t^{1/3}, t^{2/3}, linear growth c*t: ALL spoken. Transcript:
  "growing like a constant times t ... the fluctuations are of this size t to the 1/3 ...
  that's called kinetic roughening ... that process it lives on a scale of t to the 2/3".
  SUPPORTED.
- §1 line 111-113. "predicted in 1977 by Forster, Nelson and Stephen for the stochastic Burgers
  equation using the dynamic renormalization group, and extended in 1986 by Kardar, Parisi and
  Zhang". NOT in transcript (he only says "already known in the 70s ... dynamic renormalization
  group"). CITED to Remenik arXiv:2205.01433 §1. Acceptable — external, cited.
- §1 line 117. Quote "When they do that they can't tell you what that object is..." — verbatim in
  transcript. SUPPORTED.
- §2.1 lines 148-163. Brownian 1:2 scaling, "fixed points are a good place to look for
  integrability", exact formulas as Gaussian integrals: all spoken. SUPPORTED.
- §2.2 line 181. Scattering-transform quote: matches transcript closely ("you lift up your initial
  data to an operator here this runin scattering transform"). SUPPORTED.
- §2.2 line 189-192. Kernel conjugation formula and Lax equation. NOT spoken. CITED
  (Remenik arXiv:2205.01433 eq. 5.1). External + cited.
- §2.2 line 198-200. KP-II, "reducing to KdV itself for flat initial data". Transcript has KP-II
  ("it's a famous PD it's the ketam pas equation KP2") and the hierarchy remark, but does NOT
  contain the KdV-reduction-for-flat-data claim. CITED (Quastel-Remenik arXiv:1908.10353 Thm 1.1,
  eq. 1.8). External + cited. Cannot verify the equation numbers.
- §2.3 line 217. Hopf-Lax / Airy-sheet variational formula. NOT spoken as a formula (he says the
  sup of two narrow wedges, and names the "area sheet" = Airy sheet). CITED (arXiv:1908.10353
  eq. 1.3). External + cited; the tutorial correctly says "It goes further than he says aloud."
- §2.3 line 225-227. "he never once says 'stochastic Burgers equation' — only 'integrated
  Burgers'". CONFIRMED against transcript. Honest negative claim.
- §2.4 lines 229-242. "The talk never mentions Cole-Hopf / stochastic heat equation."
  CONFIRMED — no occurrence in transcript. Honest negative claim.
- §3 line 267. KPZ equation displayed with constants nu/2, lambda/2, sigma. Not spoken (no formulas
  survive). Standard textbook form, attributed inline to "Kardar, Parisi, Zhang, 1986". The
  coefficient normalisation is a convention, not a claim; low risk.
- §3 lines 271-284. Three-mechanism walkthrough incl. sqrt(1+(dh)^2) and "magic ... I'll take
  (d_x h)^2": verbatim in transcript. SUPPORTED. Hairer-Quastel arXiv:1512.07845 attached to the
  universality-of-nonlinearity claim — external, cited.
- §3 lines 286-300. White-noise/Brownian-invariance miracle quote: verbatim. The sharpened
  statement "drifted two-sided Brownian motions are invariant modulo overall height" is external
  and CITED (Gu-Quastel arXiv:2409.08465), with an honest note that this is primary literature
  for one sentence, not a companion.
- §3 line 314. "The Eden model (Murray Eden, 1961)". Date/first name NOT in transcript and NOT
  cited by arXiv id or title. Minor uncited external attribution (widely known, low risk). FLAG-1.
- §4.1 lines 334-383. 1:2:3 derivation. Labelled explicitly as the writer's own derivation
  (line 337-339). Inputs (Brownian middle, spreading parabola, epsilon^{-3/2} time, "t^{1/3} is
  just this epsilon^{1/2}") are ALL spoken. Final scaling display cited to arXiv:1908.10353
  eq. (1.2). Well handled.
- §4.2 lines 386-404. "Non-intersecting lines produce determinants" quote verbatim. The
  Lindstrom-Gessel-Viennot / Karlin-McGregor name and the determinant display are external,
  marked "(Standard; not in the captions.)" — named authors, no arXiv id. Acceptable labelling.
- §4.3 line 416. Fredholm determinant expansion, marked "(Standard definition; not in the
  captions.)" Acceptable.

### Running log (sections 4.4-5.13)

- §4.4 lines 439-459. TASEP definition, Charlier polynomials, shift by "position of the k-th
  particle minus its label": all spoken in transcript ("they're called charlier polomials ...
  the E polomial is shifted by the position of the E particle minus its name"). SUPPORTED.
  The added side condition "2^{-x}Psi_k(x) must be a polynomial of degree k" is external; it
  sits under the §3 citation to Remenik arXiv:2205.01433 at line 444. Thin but covered.
- §4.4 line 457-459. "Sasamoto (2005) and Borodin, Ferrari, Prahofer and Sasamoto (2007)".
  Transcript names only "Sasimoto and Bordon and their collaborators" and "around 2007".
  The 2005 date, the Ferrari/Prahofer names and "solved it essentially by linear algebra" are
  external, cited only as author+year with no title/arXiv/DOI. FLAG-2 (minor).
- §4.4 lines 461-469. The biorthogonalisation trick (random-walk hitting probabilities of the
  region under the initial data). Spoken almost exactly: "you ask for its hitting distribution
  of the initial data by that random walk and that actually can be used to buy orthogonalize
  these polomials". SUPPORTED. Marked as a quote-styled blockquote though it is a paraphrase;
  it is introduced as "the one Quastel states from the podium", which is fair.
- §4.5 lines 477-500. Brownian scattering operator, the conjugated limit, the Lax equation, the
  spatial companion identity. NONE spoken (no formulas survive). ALL cited to companion
  eq. (4.2), §5 eq. (5.1), eq. (5.2), plus arXiv:1908.10353. External + cited, and explicitly
  labelled "transcribed" from the companion.
- §5.1-5.5. Undirected vs directed split, the "won't even mention SPDEs" promise, delta Bose gas,
  the mathematician-before-physicist remark, the four PNG rules, narrow wedge: every item is in
  the transcript. SUPPORTED. Note the tutorial's "delta Bose gas ... completely diagonalizable"
  matches "delta boza gas which is actually a equation which is completely diagonalizable".
- §5.6 lines 588-590. [Gap] on "t equals about n^2 points in the box". The transcript really does
  say that, and the tutorial inverts it to n ~ t^2 and says so explicitly, both here and in §11.
  This is a caption-arithmetic correction, openly declared, not a silent fill. HONEST.
- §5.6 lines 592-597. LIS ~ 2*sqrt(n) (Logan-Shepp, Vershik-Kerov 1977) and fluctuation n^{1/6}
  (Baik-Deift-Johansson 1999). NOT in transcript. Cited by author+year only, no title or id.
  FLAG-3 (minor). These are the load-bearing numbers behind the "t^{1/3} recovered from
  combinatorics" claim, so a title would have been better.
- §5.7 line 612. "This is the Prahofer-Spohn multi-line PNG construction; he does not name it in
  the captions, and I flag the attribution as mine." Correct — no such name in the transcript.
  HONEST self-flag.
- §5.7 lines 615-618. "Gessel, 1990 — Symmetric functions and P-recursiveness, JCTA 53, 257-285
  ... Toeplitz determinant". Transcript has only "such a formula was derived by Gel in 1990".
  Name reconstruction Gel -> Gessel is well founded and full bibliographic data is given.
  ACCEPTABLE. The added characterisation ("generating function for permutations with bounded
  longest increasing subsequence as a Toeplitz determinant") is external and rests on that one
  citation; I cannot check that Gessel's paper states it in that form. Noted under "could not
  check".
- §5.7 lines 633-639. GUE/GOE correction. Transcript genuinely says "Gaussian unitary ensemble"
  twice, "GU trace width distribution", then "which is this GOE Tracy Wind distribution".
  The tutorial's description of the caption is ACCURATE, the correction is flagged in-line and
  again in §11, and it is cited (arXiv:1908.10353 §1; arXiv:2205.01433 §§2,4). HONEST.
- §5.8. Airy sheet, non-independence, loss of the multi-line structure, TASEP as
  "Bethe ansatz solvable / free fermion / Yang-Baxter". All spoken. SUPPORTED.
- §5.9 lines 676-681. [Gap] "he does not display the formula" — transcript confirms ("I won't
  show you the formula. I was warned not to show you the formula"). The replacement pointer is
  cited (Matetski-Quastel-Remenik, Acta Math. 227 (2021) 115-203, arXiv:1701.00018). HONEST.
- §5.10 line 689. KPZ fixed point Fredholm formula. Not spoken; cited (companion eq. 4.3).
  The four listed properties (Markov, 1:2:3 invariant, Brownian invariant measure modulo height,
  conjectural universality with "driven diffusive systems, polymer free energies") are all
  spoken. SUPPORTED.
- §5.11. Three reasons for exact formulas; Takeuchi liquid crystal + laser. Spoken. The added
  GUE-circular / GOE-flat experimental geometry claim is external and CITED
  (arXiv:1108.2118, arXiv:1203.2530).
- §5.12 lines 739, 746, 754. KP-II with coefficients 1/2, 1/12, 1/4; the KdV reduction; the
  matrix-KP equation with commutator. NOT spoken (he refuses to show formulas). ALL cited to
  arXiv:1908.10353 eqs. (1.7), (1.8), (1.6). This is the exact-constants risk the task named,
  and each display carries its own citation on its own line. GOOD.
- §5.12 lines 763-774. "please somebody tell me why it's true ... How pathetic is that?" —
  verbatim. The published Remark 1.2.1 quotation is cited. SUPPORTED.
- §5.12 lines 776-784. Rodriguez thesis. Transcript says only "the thesis of one of my students"
  and "like 10 of them". The student's NAME (C. Alexander Rodriguez), the thesis title, the
  "eighteen models across four scaling regimes" count and arXiv:2509.16316 / arXiv:2209.02643
  are all external, cited, AND the tutorial explicitly says where it departs from the podium
  ("Quastel says 'like 10 of them' ... Where the two disagree, I am quoting the thesis").
  This is exactly the failure mode the task warned about, handled correctly. HONEST.
- §5.13. Stochastic integrable systems: the open-question framing, "we don't quite know yet",
  "I'm going to propose something", nothing conserved, transition probabilities as the
  integrable object, three-step lift/evolve/return. All spoken. SUPPORTED. The Fokker-Planck
  reframing is labelled as the writer's translation ("in your own vocabulary"), not as Quastel's.

### Running log (sections 5.14-7.2)

- §5.14 lines 826-838. (lambda, eps^{1/2}nu, eps^{1/4}sigma) and Edwards-Wilkinson 1:2:4. The
  1:2:4 name and exponent ARE spoken ("Edward's Wilkinson model and that thing has a 124
  scaling"). The coefficient transformation is external, CITED (arXiv:1908.10353 §1), and
  independently re-derived in §7.2 with the algebra shown. Exemplary handling.
- §5.14 lines 843-848. The long "these tools kind of exist down there / perturbation around this
  Gaussian fixed point" quote: verbatim in transcript including the "well, maybe not ever" hedge.
  SUPPORTED. The gloss at lines 858-861 (subcriticality = nonlinearity irrelevant at small
  scales) is the writer's own structural claim, presented as a takeaway not as Quastel's.
- §5.15 lines 877-895. Corwin-Hammond Brownian Gibbs; Aggarwal-Huang characterisation
  ("the only line ensemble with the Brownian Gibbs property which looks parabolic at infinity").
  Both spoken. The Aggarwal-Huang bibliographic entry (arXiv:2308.11908, Invent. Math. 2025) is
  external and cited. SUPPORTED.
- §5.15 lines 908-915. Dauvergne/Virag reconstruction from captions "Duncan Diver and Bound Ber",
  cited to arXiv:1812.00309. The chain ASEP -> KPZ equation (1:2:4) -> KPZ fixed point (1:2:3)
  matches "back and forth versions of the TAP which are known to converge to the KPZ equation
  under the 124 scaling". SUPPORTED; "ASEP" is a name reconstruction from "back and forth
  versions of the TAP" (see §11 check below).
- §5.16 lines 927-931. Mount Fuji / 2D spatial white noise / Quastel-Ramirez-Virag. Spoken
  ("with uh Ver and Ramirez ... a 2D model with just a spatial white noise ... Mount Fuji").
  Identification as the *planar stochastic heat equation* is an inference from the cited paper
  title (arXiv:2210.13607). CITED.
- §5.16 lines 944-950. Aggarwal on the 1D Toda lattice, "the talk was given yesterday": spoken.
  The bracketed detail — Gaussian limit for current fluctuations, Brownian motion for a single
  trajectory, two-point correlations decaying like 1/t, Doyon-Spohn scaling functions — is
  entirely external and rests on one citation (Aggarwal-Nicoletti arXiv:2604.14346). Cited but
  unverifiable from here; listed under "could not check".
- §5.18 lines 989-994. Half-space KPZ fixed point. Neumann boundary condition, arbitrary forcing
  parameter, Pfaffian formulas: ALL spoken. The student's NAME "Xincheng Zhang" is NOT spoken;
  it is external and cited (arXiv:2409.09974). The trailing sentence "Pfaffians rather than
  determinants is the signature of a boundary; it is the same GOE/GSE-versus-GUE distinction" is
  an UNCITED external interpretive claim. FLAG-4 (minor).
- §5.18 line 998. "due to Johansson and Rahman and to [Zhipeng] Liu". Captions give "Johansson
  and Roman bike and leu". Names are reconstructed (Liu's first name is bracket-marked), but
  NO citation of any kind is attached — no arXiv id, no title, no year. This is the only
  multi-author attribution in the tutorial with zero source. FLAG-5 (minor-to-moderate: it is a
  name attribution, not a mathematical claim, but it is exactly the class the brief calls
  dangerous).
- §5.18 lines 1006-1011. polaron -> polariton correction, flagged in-line and deferred to §11.
  Transcript really says "polaron condensates". HONEST.
- §6 line 1032. "taking values in upper semicontinuous functions" — external technical detail from
  Matetski-Quastel-Remenik, not spoken, and not cited on its own line (the surrounding claim is
  attributed to MQR by name only). FLAG-6 (minor).
- §6 line 1058. "the probability that a random walk hits the **epigraph** of the initial data".
  §4.4 and §4.5 both say the region *under* / the **hypograph**. Internal inconsistency
  (epigraph = region above). One of the two is wrong. FLAG-7 (minor, but it is a mathematical
  word, not a typo of style).
- §7.1, §7.2. Both are the writer's own derivations, explicitly framed as exercises, and both
  land on numbers that are either spoken (t^{1/3}, t^{2/3}, 1:2:3, 1:2:4) or cited
  (arXiv:1908.10353 §1). The white-noise covariance step and the three exponent tables check out
  internally. No provenance problem.

### Running log (sections 8-10)

- §8.1-8.6 and §10 are re-statements of material already checked above. Two re-checks:
  §10 Q5 repeats the GUE correction with the caption error flagged in place (consistent with
  §5.7 and §11). §10 Q6 says "random walk hits the region **under** the initial data curve" and
  "hypograph" — consistent with §4.4/§4.5 and therefore confirms §6 line 1058 ("epigraph") is
  the odd one out.
- §8.6 line 1315. "It is published in Forum of Mathematics, Pi." External; §9 item 3 supplies
  the full reference (Forum Math. Pi 10 (2022) e10). Covered.
- §9 line 1348 says "Read Remark 1.2"; §5.12 line 774 cites "Remark 1.2.1". Trivial numbering
  inconsistency, not a provenance problem.

## Self-report audit

The writing agent's self-report is §11, "Note on the tutorial process". Judged against what I
actually found, it is **substantially honest and unusually thorough — but it under-reports in
exactly one place, and that place is a factual mis-statement about its own citation coverage.**

**What it reports correctly, and I confirmed:**
- The title is reconstructed from Quastel's own opening sentence. Confirmed; no programme title
  in the transcript.
- The GOE-for-narrow-wedge caption error and the correction to GUE. The transcript really does
  read that way; the correction is flagged in three separate places (§5.7, §10 Q5, §11).
- The "t equals about n^2 points" inversion. The transcript really says that; the correction to
  n ~ t^2 is flagged with a [Gap] marker and repeated in §11.
- "polaron condensates" -> polariton. Transcript confirms "polaron".
- Prahofer-Spohn attribution for multi-line PNG declared as the writer's own, not the speaker's.
  Confirmed absent from the transcript.
- The 1:2:3 derivation in §4.1 declared as the writer's own. Confirmed: the transcript has the
  three inputs but not the algebra.
- Both unnamed students (Xincheng Zhang, C. Alexander Rodriguez) identified from published work
  and openly labelled as such, including the "like 10 of them" vs "eighteen models" discrepancy.
- "No theorem is stated from the podium with hypotheses"; every formula comes from a paper.
  Confirmed against the transcript, which contains no formula at all.
- The introducer's prize list declared unreconcilable and therefore not reproduced.
- The name-correction table (49 rows) is accurate everywhere I spot-checked against the captions.

**What it UNDER-REPORTS — one item, and it is a claim about its own sourcing:**

1. **§11 line 1615-1616 states: "The half-space Pfaffian formulas, the multi-time formulas, and
   the discrete Hirota equations are named but never displayed. Impact: low — each is a pointer
   to a paper, and **the papers are cited**." That last clause is FALSE for the multi-time
   formulas.** §5.18 line 998 attributes them to "Johansson and Rahman" and "[Zhipeng] Liu" with
   **no arXiv id, no title, and no year** — and `grep` over the whole file confirms no such
   citation exists anywhere else in the document (the only other occurrences are the two
   caption-correction rows at lines 1528-1529). The half-space claim is cited
   (arXiv:2409.09974) and the Hirota claim is cited (arXiv:2509.16316, arXiv:2209.02643); the
   multi-time one is not. The self-report asserts coverage it does not have.

**Smaller things the self-report is silent on (I do not count these as dishonesty, but they are
gaps in the gap-list):**

2. The **epigraph / hypograph** inconsistency between §6 step 3 and §4.4 / §4.5 / §10 Q6. §11
   claims the construction is "recoverable from the cited published sources"; one of the two
   words is wrong and the self-report does not notice.
3. Four external results are carried on **author + year only, with no title, arXiv id or DOI**:
   Murray Eden 1961 (§3 line 314); Logan-Shepp and Vershik-Kerov 1977 and Baik-Deift-Johansson
   1999 (§5.6 lines 594-595 — these two are the load-bearing numbers for the "t^{1/3} recovered
   from combinatorics" check); Sasamoto 2005 and Borodin-Ferrari-Prahofer-Sasamoto 2007 with the
   added characterisation "essentially by linear algebra" (§4.4 lines 457-459). §11's blanket
   sentence "Each equation above carries its citation" is true of the displayed equations but not
   of these inline numerical results.
4. Two fully uncited interpretive additions: "Pfaffians rather than determinants is the signature
   of a boundary; it is the same GOE/GSE-versus-GUE distinction" (§5.18 line 994), and "taking
   values in upper semicontinuous functions" (§6 line 1032).
5. **"Quastel drops the KPZ equation nine minutes in"** (§11 line 1480-1481). The transcript has
   no timestamps and none of the tutorial's other claims are time-indexed. This number cannot be
   checked from the sources named in the front matter; it must have come from the video itself,
   which the self-report never says it consulted. Not wrong, but unsourced.

**Verdict on the self-report: HONEST, and complete on every substantive mathematical gap and
every name reconstruction — with one false statement about citation coverage (item 1) and four
smaller omissions from the gap-list (items 2-5). It over-claims its own thoroughness rather than
hiding a mathematical invention.** Nothing it declared was found to be a cover for a silent fill;
the opposite pattern (declaring more uncertainty than it needed to) is what dominates.

## What I could not check

- Whether any cited paper actually says what it is cited for. I do not have the papers. Every
  equation-number reference (Remenik eqs. 4.2, 4.3, 5.1, 5.2; Quastel-Remenik eqs. 1.2, 1.3, 1.6,
  1.7, 1.8, Thm. 1.1, Remark 1.2.1) is unverified. The task brief states independently that all
  40 arXiv instances resolve to real papers, so fabrication is ruled out; correct ATTACHMENT of a
  real citation to the right claim is not.
- The KP-II coefficients 1/2, 1/12, 1/4 and the matrix-KP commutator term. Not spoken; each
  carries its own citation on its own line, which is what the task asked me to check, and that
  check PASSES. Whether the constants match arXiv:1908.10353 eq. (1.7) I cannot confirm.
- The Aggarwal-Nicoletti detail in §5.16 (Gaussian current fluctuations, 1/t two-point decay,
  Doyon-Spohn scaling functions). Entirely from arXiv:2604.14346; unverifiable here.
- Gessel 1990's characterisation as a Toeplitz determinant for bounded-LIS permutations.
- Slide content. The transcript is caption-only, one unbroken line, no timestamps, no formulas,
  no figures. Everything Quastel wrote is invisible to me, exactly as it was to the writer.
- The two cross-referenced tutorials (otto, wright) — I did not open them, so the section numbers
  in §5.14, §8.2 and §8.5 are unchecked.

---

# Round 2 — companion formula check, 2026-08-18

The round-1 report above closes with "Remenik eqs. 4.2, 4.3, 5.1, 5.2 … is unverified." This
round fetched the companion — Remenik, *Integrable fluctuations in the KPZ universality class*,
`arXiv:2205.01433`, via `ar5iv.labs.arxiv.org/html/2205.01433` — and compared each cited
equation against the tutorial. **One is misstated, and it is the file's central formula.**

Verdict change: **MINOR to MAJOR.** A displayed equation that says "transcribed" is not a
transcription.

## MAJOR — `summaries/random-interface-growth-quastel.md:481` misstates companion eq. (4.2)

**The tutorial prints:**

    K_t^{hypo(h)} = lim_{ℓ1→−∞, ℓ2→∞}  e^{−(1/3)ℓ1³ + ℓ1∂²}  P^{Hit h}_{ℓ1,ℓ2}  e^{(1/3)ℓ2³ − ℓ2∂²}

and labels it *"(Companion eq. (4.2), transcribed.)"*

**The companion's eq. (4.2) reads:**

    K_t^{hypo(h)} = lim_{ℓ1→−∞, ℓ2→∞}  e^{−(1/3)t∂³ + ℓ1∂²}  P^{Hit h}_{ℓ1,ℓ2}  e^{(1/3)t∂³ − ℓ2∂²}

The exponent `t∂³` has become `ℓ1³` in the left factor and `ℓ2³` in the right factor. Three
things go wrong at once:

1. **The operator became a scalar.** `∂³` is a third derivative; `ℓ1³` is a number. The whole
   point of the expression is conjugation by the Airy propagator `e^{−(t/3)∂³}`.
2. **The time variable disappeared from the right-hand side.** The left side is `K_t`, and the
   companion even calls this "the (t-dependent) Brownian scattering operator". As printed in
   the tutorial, the right side depends only on the truncation parameters ℓ1, ℓ2 — which are
   then sent to ∓∞ — so the definition would carry no t at all.
3. **The two factors stopped matching.** In the companion, `t∂³` is the *same* in both; the
   ℓ-dependence sits entirely in the `∂²` terms, which is what makes the limit a conjugated
   one. The tutorial's ℓ1³ / ℓ2³ breaks that symmetry.

**Why this one matters more than a typo.** It is the definition the whole of §4.5 rests on,
and it directly undercuts the section's own punchline. The tutorial states at `:491` — from
companion §5 — that `K_t = e^{−(t/3)∂³} K_0 e^{(t/3)∂³}`, i.e. that time and initial data
decouple. **That statement is read off from eq. (4.2) by pulling the t-conjugation outside the
limit.** With `t∂³` deleted from (4.2), the decoupling has no source.

**What is correct:** the paragraph either side of it. The `P^{No hit}` / `P^{Hit} = I − P^{No hit}`
setup at `:477-479` matches the companion exactly, including the diffusion coefficient 2. And
the file is right that the existence of the limit is a theorem, not an observation — the
companion says so in as many words ("The fact that the right hand side of (4.2) makes sense is
far from obvious") and gives the same [QR19] attribution the tutorial gives as `arXiv:1908.10353`.

**Fix:** replace `ℓ1³` by `t∂³` and `ℓ2³` by `t∂³` — the same term in both exponents.

## The other three cited equations are correct

| Cited as | Companion | Verdict |
|---|---|---|
| `:188` `K_t^{hypo(h0)} = e^{−(t/3)∂³} K_0^{hypo(h0)} e^{(t/3)∂³}` | §5, immediately above (5.1) | **correct**, verbatim |
| `:493` `∂_t K_{t,ext} = [−⅓∂³, K_{t,ext}]` | eq. (5.1) | **correct**, including the subscript |
| `:497-499` "a companion identity in the spatial variables involving ∂²_u — a heat operator rather than an Airy operator" | eq. (5.2) | **correct** as stated. Deliberately not transcribed, which turns out to be the right call — the ar5iv rendering of (5.2) itself prints `(∂²_{u_j} − ∂²_{u_j})`, obviously a typo for `(∂²_{u_i} − ∂²_{u_j})`, so a literal transcription would have propagated a source error |

One wording slip, not a defect: `:192` attributes the Lax equation to `K_t`, while the
companion states (5.1) for the *extended* kernel `K_{t,ext}`. The tutorial gets this right at
`:493`, so the two displays disagree with each other by a subscript.

## Also confirmed from the companion

- The Brownian-motion-hits-the-**hypograph** reading is the companion's own word, used
  repeatedly. This settles the round-1 finding at `:1058`, where the tutorial says **epigraph**:
  that line is wrong, and `:466`, `:475`, `:1423` and the companion all agree on hypograph.
- Companion eq. (4.4), the extended kernel, and eq. (4.5)-(4.6), the narrow-wedge specialization
  to the Airy₂ process, are both present and match the tutorial's description of them.

## What this round did not check

The Quastel–Remenik equation references (`arXiv:1908.10353` Thm. 1.1, eqs. (1.2), (1.3), (1.6),
(1.7), (1.8)), including the KP-II coefficients 1/2, 1/12, 1/4. Only the Remenik companion was
fetched.
