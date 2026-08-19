# Verification — hardy-spaces-explicit-formulae-gerard
verdict: MAJOR
uncited_external_claims: 4 (all biographical/historical; zero uncited external MATHEMATICAL claims)
unsupported_speaker_claims: 0
title_check: PASS — transcript intro announces "Hardy spaces of holomorphic functions and explicit formula for a class of integrable partial differential equations"; front matter matches (front matter pluralises "formula"->"formulae" and matches the Crossref DOI title).
gap_honesty: CONCERN - gaps are real and marked, but one declared-unrecoverable constant (F3) was recoverable from the tutorial's own HTML route, and the B_u error (F2) is absent from the talk-vs-paper list.

## Findings
Most severe first. F1 and F2 are misstated formulae; F1 drives the MAJOR verdict.

### F1 — MAJOR. Misstated distorted Plancherel identity.
`summaries/hardy-spaces-explicit-formulae-gerard.md:665` (§5.3)

Tutorial displays, attributed to "arXiv:2601.10488, eq. (2.7)":

    sum_{j=1}^N |<f,phi_j>|^2 + int_0^inf |f~^pm(lam)|^2 dlam  =  2*pi * int_R |f(x)|^2 dx

Actual (2.7), read from ar5iv HTML of 2601.10488:

    sum_{j=1}^N |<f,phi_j>|^2 + int_0^inf |f~^pm(lam)|^2 dlam/(2*pi)  =  int_R |f(x)|^2 dx

The tutorial moved the 1/(2*pi) off the continuous integral and onto the right-hand
side, but did NOT apply the same factor to the discrete sum. Multiplying the paper's
identity through by 2*pi gives
`2*pi*sum |<f,phi_j>|^2 + int |f~|^2 dlam = 2*pi*int |f|^2`.
The tutorial's version is therefore FALSE as written: the discrete term is off by 2*pi.
This is exactly the class of defect the tutorial's own §10 says it defended against
(pdftotext deleting every pi). Independent cross-check: (2.2) `|<phi_j,Pi u_0>|^2 =
-2*pi*lam_j` is on the paper's scale, and the tutorial reproduces (2.2) unrescaled, so
the two displays in §5.2/§5.3 are mutually inconsistent.
Settles it: the ar5iv HTML of 2601.10488, eq. (2.7).

### F2 — Misstated Lax-pair operator B_u.
`summaries/hardy-spaces-explicit-formulae-gerard.md:399` (§4.1)

Tutorial: `B_u = i(T_{|D|u} - T_{u^2})` — Toeplitz operator with symbol u^2.
Source (arXiv:2212.03139, ar5iv HTML): `B_u = i(T_{|D|u} - T_u^2)` — the SQUARE of the
Toeplitz operator T_u. These are different operators (T_{u^2} != (T_u)^2 in general).
The transcript agrees with the paper, not with the tutorial: Gerard says "minus the
square of TU". So the tutorial contradicts BOTH of its sources on this display.
Consistent with the tutorial's own account of a lossy PDF extraction; but it is not
flagged, and §10 does not list it.

### F3 — A "refused" constant that the tutorial's own stated source supplies.
`summaries/hardy-spaces-explicit-formulae-gerard.md:557-560` (§4.5)

Tutorial: "The underlying lemma — that [X*,T_b] is a rank-one operator, proportional to
I_+(f)*b ... I describe rather than display that lemma: its numerical constant did not
survive my PDF text extraction, and §13 explains why I refuse to display constants I
could not close."
arXiv:2212.03139, Lemma 3, in the ar5iv HTML: `[G,T_b]f = (i/2*pi) I_+(f) Pi b`.
So (a) the constant was retrievable from HTML — the same rescue route §10 says was used
for the other paper — and (b) the tutorial's prose says the operator is proportional to
`b`, where the lemma has `Pi b` (the Szego projection of b). The refusal is honest in
form but the gap was avoidable, and the prose version is imprecise.

**F1 hole closed.** The paper's own definition of the distorted Fourier transform,
eq. (2.5), is `f~^pm(lam) = int_R f(x) conj(m_pm(x,lam)) dx` — NO prefactor — which is
character-for-character what the tutorial gives at line 660. So the tutorial cannot be
using a different normalization; its (2.7) is simply wrong on the discrete term.

### F4 — MINOR. Silent symbol rename in Remark 2.3.
`summaries/...:722` — tutorial: "the paper's Remark 2.3 gives a unimodular
$\beta(\lambda)$ with u^+_inf-hat = beta(lam) u^-_inf-hat". The paper writes
`u^+_inf-hat(lam) = l(lam) u^-_inf-hat(lam)`, |l(lam)|=1. Content correct; symbol renamed
without saying so, inside a sentence that reads as a quotation of the paper.

### F5 — MINOR (deviation, not an error). Inner-product argument in the Wu identities.
`summaries/...:629` — tutorial writes `|<phi_j, u_0>|^2 = -2*pi*lam_j` and
`lam_j I_+(phi_j) = -<phi_j, u_0>`. Paper (2.2) writes `Pi u_0` in both slots. These are
equal, because phi_j is in L^2_+ and conj(Pi u_0) is in L^2_-, which is orthogonal to it.
Not a mathematical error; a silent deviation from a display carrying an equation number.

### F6 — MINOR. Dropped provenance for X*.
The transcript sources X* explicitly: "this operator already appears in another paper by
Peter Lax, which is less known, which was published in 1959 in Acta Mathematica, which is
called translation invariance of spaces, and which characterized ... the famous Burling
theorem". The tutorial calls X* "the one genuinely new operator" / "The one new object"
(§3 heading, lines 240, 328) and never mentions Lax 1959 anywhere, including §10. The
tutorial's framing is defensible as "new to the reader", but a speaker-given attribution
was dropped and not listed as a cut.

### F7 — MINOR. Four uncited external claims, all biographical/historical.
None mathematical. All in §10 or §2:
- `:786` "half-wave maps ... classical continuum limit of **Haldane-Shastry** quantum spin
  chains" — this replaces the caption's "Alday-Destri-Heisenberg" and is a substantive
  identification, not a spelling fix. No source given.
- `:1219` John Scott Russell's observation redated from the talk's 1864 to **1834**, Union
  Canal near Edinburgh. Correct redating is asserted, uncited.
- `:219` / `:1206` Claude Bardos dates "(4 April 1940 - 16 June 2026)". Precise, uncited;
  the transcript says only "he passed away last uh in June".
- `:1197` Alama Bronsard given as "McGill, Montreal". Transcript says only "from Quebec".
  (Her CNRS/Nantes affiliation IS in the transcript; the McGill part is not.)

### Speaker-attributed claims: 0 unsupported.
Every quotation I spot-checked appears in the transcript, lightly cleaned of disfluency
only: "the opposite of the group photo"; "I will require all your attention because this
is something new"; "if I renormalize by the constant, then it is"; "the constant in which
the whole dynamics of Benjamin-Ono is hidden"; "I called it Cauchy-like because it starts
with 1 over 2 I pi"; "Exercise. So let's do this exercise"; "we know everything in terms
of the data"; "a crucial operator identity which expresses some compatibility between the
shift structure of the Hardy space and the Lax pair"; "It takes several pages ...
oscillatory integrals"; the numerics quote (verbatim); the closing-slide quote (verbatim);
"This is the crucial condition"; "Patrick, you should apply your techniques to
Benjamin-Ono"; "For the moment, this is completely open". The two on-slide typos Gerard
flags ("y should be x", "I forgot the Fourier transform") are in the transcript and §10
correctly reports suppressing them.
Talk-vs-paper flags at :450 (H^inf vs H^1) and :409 ("if and only if") are both accurate
against the transcript.

### Verified clean against arXiv:2601.10488 (the "read in full" test)
- Theorem 1.1 (§4.3, :441-448): hypotheses `u_0 in H^1`, `xu_0 in H^1`,
  `x^2 u_0 = c_0 + v_0`, conclusion in H^1, AND the ordering `Im(p_1)<...<Im(p_N)` — all
  match verbatim.
- (2.3) `Im p_j = |I_+(phi_j)|^2/(4pi) = 1/(2|lam_j|) > 0` — matches exactly, every pi.
- (2.6) `u^pm_inf-hat(lam) = Pi u_0~^mp(lam)` — index flip correctly preserved.
- (3.2) soliton limit `i/(z - <X* phi_j, phi_j>)` — matches.
- (3.3) radiation limit `(2t)^{1/2} e^{it lam^2} Pi u(t, z-2t lam) -> e^{i pi/4}/sqrt(2pi)
  e^{i lam z} Pi u_0~(lam)`, weakly in L^2(0,inf) — matches, both constants.
- Corollary 2.2 (both iff's) — matches §5.4.
- The "non-trivial scattering map relates the soliton parameters" quote and the "p_j are
  the same as t->+inf and t->-inf" claim — verbatim in the paper's §1. §5.4 accurate.
- The §1 quote at :118-119 ("lacks a justified inverse-scattering transform formulated as
  any kind of Riemann-Hilbert problem, making the large-time asymptotics inaccessible to
  the Deift-Zhou method") — CONFIRMED verbatim in the paper's Introduction.
- Against arXiv:2212.03139: Theorem 4 (line, :470) and Theorem 3 (torus, :502) match
  character for character; Lemma 2 `[G,B_u] = -2L_u + i[L_u^2,G]` matches §4.5 (:544).
- Against arXiv:2412.13480 (§5.5): authors Yvonne Alama Bronsard, Xi Chen, Matthieu
  Dolbeault CONFIRMED (all three caption corrections correct); title correct; abstract
  confirms "error constant depending linearly on the final time instead of exponentially"
  and "computational cost of the method is independent of the final time".
- Amick-Toland, Acta Math. 167 (1991) 107-126 CONFIRMED in the paper's bibliography.

So the "read in full" claim holds for COVERAGE. It fails only on FORMULA FIDELITY, and at
exactly one place: eq. (2.7).

### §6 (exercises) — checked transitively, clean.
6.1 derives `I_+(phi_p) = -2i pi sqrt(Im p / pi)` and `|I_+|^2/4pi = Im p`, which closes
against the verified (2.3). 6.2 reproduces the verified (3.2). 6.3's Fresnel factor
`sqrt(pi/t) e^{i pi/4}` is consistent with the verified constants in (3.3). No defect.

## Self-report audit

The writing agent's §10 "Note on the tutorial process" is **honest in method and
substantially complete on scope, but it under-reports in exactly the zone that failed.**

**What it got right, and deserves credit for.**
- The two-paper sourcing, the DOI 403, and the unread EMS survey are all reported
  accurately and the unread survey is explicitly not used as a source.
- The four unresolvable names ("Sichan, Hanada, Sredin, Ola Melon") are named as
  unresolved and omitted from the body rather than guessed. That is the right call and it
  is visible in the transcript.
- "Jiao He" is marked *(reconstructed)* with its anchor stated.
- The H^inf-vs-H^1 and "if and only if" talk/paper divergences are flagged accurately.
- The two labelled reconstructions (the O(1/t) identity, the resolvent bound) are labelled
  in place, as claimed.
- The 1834/1864 and 1911/1915 corrections are real corrections of real transcript errors.
- The claim that the captions carry no mathematics is TRUE — I confirmed it; the
  transcript has zero formulas.

**Where it under-reports.**

1. **The headline defence is narrower than it reads.** §10 says "Formulas in this document
   are cross-checked, not transcribed once" and then that it "re-fetched the arXiv HTML of
   arXiv:2601.10488v2 ... and confirmed **the explicit formula, the soliton limit and the
   radiation limit** character by character." That is three displays. The distorted
   Plancherel identity (2.7) and the Lax-pair operator B_u are NOT in that set, and both
   are wrong (F1, F2). The report does not say which displays were left outside the check,
   so a reader reasonably reads the assurance as global. **This is the material
   under-report.** F1 in particular is exactly the failure mode §10 claims to have
   defended against — a lost 2*pi — and it survived.

2. **"Talk versus paper, where they differ. Three places" omits B_u.** At §4.1 the
   tutorial differs from the talk AND from the paper, both of which say (T_u)^2. That is a
   fourth divergence and it is not in the list, nor anywhere in §10.

3. **The refused constant was not actually unrecoverable.** §10 says "Where a constant
   could not be closed either way — specifically the commutator identity
   [X*,T_b]f ~ I_+(f) b — I describe the identity and refuse to display it." But Lemma 3
   of arXiv:2212.03139 gives it in plain HTML: `[G,T_b]f = (i/2pi) I_+(f) Pi b`. The
   writing agent demonstrably knew the HTML rescue route (it used it on the other paper)
   and did not apply it here. The refusal is honest about the outcome, and reporting a gap
   is better than inventing a constant — but the report frames the gap as forced when it
   was avoidable, and the prose paraphrase also drops the projector (b vs Pi b).

4. **Lax 1959 is dropped silently.** The transcript sources X* to Peter Lax, *Translation
   invariant spaces*, Acta Math. 1959, in the same breath as introducing it. §3 presents
   X* as "the one genuinely new operator" and §10's gap list does not mention the omission.

5. **The name table's Haldane-Shastry correction is a substantive external claim, not a
   spelling fix,** and §10's own rule ("substantive caption errors ... corrected in text
   and listed here") is applied to the 1834 and 1911 fixes but not to this one, which is
   left in the spelling table uncited.

**Verdict on the self-report: HONEST but INCOMPLETE.** No misrepresentation, no invented
verification. But the cross-check assurance in §10 is broader than the check it describes,
and the two formula defects (F1, F2) both fall in the untested margin — the reader is
given no way to see that margin exists.

## What I could not check
- The ICM proceedings chapter, DOI 10.1137/25M1805497 (SIAM, HTTP 403). I confirm the
  tutorial's account of the gap; I cannot confirm its contents, so the zero-dispersion-limit
  remark is unverifiable beyond the transcript (which does support it).
- The EMS survey *Lectures on integrable equations of Benjamin-Ono type* — paywalled, no
  arXiv version. Its existence and the 7 January 2026 date are unverified by me.
- Non-arXiv journal citations. My WebSearch budget for this session was exhausted, and the
  ar5iv/HTML bibliography extraction proved unreliable (one call returned a plainly
  fabricated Wu entry that a second call contradicted). So these remain UNVERIFIED, not
  disputed: Wu, SIAM J. Math. Anal. 48 (2016); Sun, Comm. Math. Phys. 383 (2021);
  Killip-Laurens-Vian, Invent. Math. 236 (2024); Gerard-Grellier, Trans. Amer. Math. Soc.
  367 (2015) 2979-2995; Gerard-Kappeler, Comm. Pure Appl. Math. 74 (2021) 1685-1747;
  Gerard-Lenzmann, Comm. Pure Appl. Math. 77 (2024) 4008-4062; Saut 1979; Toeplitz, Math.
  Ann. 70 (1911); Ablowitz-Fokas, Stud. Appl. Math. 68 (1983). What would settle them: one
  Crossref or MathSciNet lookup each.
  (Amick-Toland, Acta Math. 167 (1991) 107-126 IS verified, from the GGM bibliography.)
- Whether §5.1's reconstructed O(1/t) identity is the paper's own algebra. The tutorial
  labels it as a reconstruction and argues it is forced; I did not locate the paper's
  §3/§6 version to compare. It is at least self-consistent and matches (3.2).
- Whether the tutorial's Fourier convention in §2 is Gerard's. The captions carry no
  formulas, so the convention is unattributable either way; nothing downstream contradicts
  it.
