# Verification — random-matrices-localization-yau
verdict: MINOR
uncited_external_claims: 17 (counting rule and full enumeration below)
unsupported_speaker_claims: 0
title_check: PASS — Yau says from the podium "today I will talk about render matrices and wiggling universality and localization and beyond"; the front-matter title "Random Matrices, Wigner–Dyson Universality, Localization and Beyond" is a faithful de-mangling.
gap_honesty: PASS — all four declared gaps are real silences in the transcript; I found no gap silently filled. Self-report under-reports at the edges (see Self-report audit), not in the mathematics.

## Working notes (front matter through §3)

- Transcript is a single unlined blob, 6793 words, auto-captioned and heavily mangled
  (speaker's name -> "HT H"/"Yao"/"Dao"; delocalization -> "deoization"; matrix Brownian
  motion -> "magic brown emotions"; BBGKY -> "BPGki"/"musical"; martingale -> "mole term").
  The tutorial states all of this in its header and it matches what I read.
- Anchor quote (§2) checked verbatim against transcript: "This is something similar to this
  BPGki hierarchy in classical dynamics ... you get the the loop n you will be depend on
  loop n plus one and this morning [martingale] will depend on loop n plus2 and uh the whole
  thing is uh uh cannot be solved." SUPPORTED.

## Findings
(in progress)

## Working notes (§4 — the six definitions)

Every exponent in §4 checked against the transcript word-for-word:

- §4.1 variance profile `S_xy = W^{-d} f((x-y)/W)` — transcript "wus df of x - y / w". SUPPORTED.
- §4.1 `N = L^d` — transcript "because n is l3 to d". SUPPORTED.
- §4.2 dictionary `λ ↔ W^{-1}` — transcript "this lambda will be inter w minus one". SUPPORTED.
- §4.2 localization-length table (d=1: W²; d=2: exp(cW²); d≥3: ∞) — transcript "for d=1 is w²
  and for d=2 will be x1 w² [exp W²] and d=3 will be infinity". SUPPORTED.
- §4.2 d=2 transition at W ≈ √(log N) — transcript "you really want to do the log square root
  log n". SUPPORTED.
- §4.3 complete delocalization `‖u‖_∞² ≤ N^ε/N` — transcript "the error infinity norm squared
  is less than one / n up to n to the epsilon". SUPPORTED.
- §4.5 local law needs `η ≫ 1/N` — transcript "the imaginary part is bigger than one / n".
  SUPPORTED, and the podium quote about η ≈ 1/N is near-verbatim.
- §4.6 `H_t = H_0 + √t·GUE` — transcript "at time t is just h0 plus square root t times the
  gue". SUPPORTED. The data-science aside is a near-verbatim quote.

Provenance hygiene is unusually good in §4.2: Fyodorov–Mirlin PRL 67 (1991) 2405 is given a
full reference AND explicitly labelled "the attribution is mine" because Yau said only
"supersymmetric method and numerics"; likewise the 1979 scaling theory is expanded to
Abrahams–Anderson–Licciardello–Ramakrishnan with a note that Yau said only "Anderson 1979".

## Working notes (§5 — the rebuilt talk)

The exponent audit, which is the point of this file. Every threshold in §5.7:

| claim | tutorial | transcript | citation on its own line |
|---|---|---|---|
| d=1 delocalization | W ≥ N^{1/2+c} | "in dimension one ... the width is square n" | arXiv:2501.01718 YES |
| d=2 delocalization | W ≥ N^c | "in dimension two is n to the epsilon" | arXiv:2503.07606 YES |
| d≥3 delocalization | W ≥ N^c | "in dimension three that is big n to epsilon" | arXiv:2507.20274 YES |
| d=2 conjectured sharp | W ≈ √(log N) | "you really want to do the log square root log n" | — (spoken) |
| d=1 localization | W² ≪ N | "for W le square root of the n is [localized]" | arXiv:2508.05802 YES |
| non-Gaussian extension | W ≫ √N, 1d | "extended by non-gaussing case by Erdish and Riabov" | arXiv:2506.06441 YES |
| DBM local equilibrium | t ≳ N^{-1+ε} | "the time scale is n to minus one" | arXiv:1609.09011 YES |
| comparison window | t ≲ N^{-1/2} | "remain unchanged up to ... entering minus one half" | — (spoken) |
| old quantum diffusion | t ~ λ^{-2-κ}, d ≥ 3 | "t is lambda minus 2 epsilon", "intervention d uh 203" | Acta Math 200/AHP 8 YES |

No exponent in the file contradicts the transcript, and none is stated bare. This is the
single most important result of this verification.

Speaker quotes spot-checked and SUPPORTED: "hundreds of graph computations ... total
nightmare" / "didn't have the courage to continue"; "requires the matrix to be quite fat";
"a very strange way of using dynamics ... the initial data is already the same as at time
infinity"; "essentially everything we were hoping to prove for the band matrix was proved";
"you really want to do √(log N), but we only do N^ε".

Two caption inversions the tutorial catches and flags rather than propagating:
- §4.3: transcript says "complete **localization**" where it must be de-localization.
- §5.7: transcript says "for W ≤ √N is **delocalized**" where it must be localized.
Both corrections are correct and both are declared inline.

Honest gap verified: §5.5 marks the mechanism of step 3 as a gap. The transcript really
does say "I will explain this later on in a minute" and never returns to it. TRUE GAP.

## Findings

**F1 — `summaries/random-matrices-localization-yau.md:815` — a direct quotation of a named
living person, sourced only to a magazine name.** The file quotes Noga Alon: "Both of us were
somewhat wrong. Still, I was a little bit more correct, because the probability is bigger
than half," attributed to "*Quanta*" with no article title, author, date or URL. It is not in
the transcript. This is the only unsourced direct quotation of a third party in the file and
the highest-risk item in it, because a misattributed quote reads as fact.
*What would settle it:* the Quanta article URL and date, or deletion of the quote.

**F2 — lines 758–790, the random-regular-graph history block — a cluster of uncited external
claims.** Yau names only Lubotzky–Phillips–Sarnak, Marcus–Spielman–Srivastava, Alon and
Sarnak from the podium. The tutorial adds, with no citation: the Alon–Boppana bound
(λ₂ ≥ 2 − o(1)); Margulis's independent construction; the restriction to d−1 prime, later
prime power; Friedman's 2008 proof of Alon's conjecture; later proofs by Bordenave and by
Chen–Garza-Vargas–Tropp–van Handel; and "open since 1988". All are standard and none is
implausible, but every one is an external claim carrying no id.
*What would settle it:* a citation on each line, in the style already used in §4.2 and §5.7.

**F3 — line 355 — an author attribution the transcript does not carry and the file does not
label.** "Yau's version, proved for Wigner matrices **with Bourgade** and now for band
matrices." Bourgade is nowhere in the transcript. The file elsewhere labels exactly this kind
of addition ("the attribution is mine" for Fyodorov–Mirlin, §4.2) and does not here.
*What would settle it:* cite Bourgade–Yau on eigenvector QUE, or mark it as the writer's
attribution.

**F4 — line 371 and line 363 — uncited quantitative sharpenings of a spoken statement.** Yau
says only that projections of two eigenvectors onto a smaller set "are still also
orthonormal". The tutorial states the normalization ⟨u_i, E_A u_j⟩ ≈ (|A|/N)δ_{ij} and the
implication chain "QUE implies delocalization; the converse is false". Both are plausible and
neither is spoken or cited.

**F5 — line 1030 vs line 812 — internal date inconsistency.** §5.9 says the existence question
was "open since 1988"; §7.2 says the problem "waited thirty-seven years". 1988 to the December
2024 preprint is 36 years. Trivial, but both numbers are uncited.

**F6 — line 156 — an unverifiable timestamp.** "He does, at minute 42." The transcript carries
no timestamps at all; the quote itself is fully supported, only its position is asserted.
The same applies to "minute two", "the last five minutes" and "the last ninety seconds".

**F7 — §3 table, line 213 — a fourth meaning-inverting caption correction, not enumerated.**
The transcript says "dimension bigger than three and if the coupling constant lambda is
**large** then it's delocalized"; the table correctly writes "once λ is **small** enough".
The correction is right — Yau himself later says "in dimension three it's actually become
infinity as long as lambda is small" — but §11 enumerates only three such inversions.

**F8 — line 466 — the Wigner-matrix universality theorem is blockquoted with an author list
and a date range that carry no citation.** "Theorem (Erdős, Schlein, Yau, Yin, and
independently in part Tao–Vu; roughly 2007–2012)." The mathematical content (2+ε moments,
complete delocalization, probabilistic QUE) is fully spoken; the authors, apart from Tao–Vu,
and the years are not, and no id is given. Low risk — this is the speaker's own famous work —
but it is formatted as a theorem statement, which raises the standard.

**F9 — four scattered single uncited claims.** (a) line 431, Dyson Brownian motion described
with its 1/(λ_i − λ_j) repulsion — textbook, and covered by the companion book, but not
spoken and not cited at the line. (b) line 583, the gap note names "the Green function
comparison theorem (Erdős–Yau–Yin), a Lindeberg-type entry-by-entry swap" with no id.
(c) line 1013, "TW₁ puts about 83% of its mass below 0" — the number the whole 69% rests on,
uncited (it is at least internally consistent: 0.83² = 0.6889). (d) line 141, "Anderson's
answer, which won him the Nobel Prize" — common knowledge, uncited.

**F10 — §3, grouped: standard attributions given author + year but no title or id.** Minami
(1996), Klein (1998), Aizenman–Warzel, Jimbo–Miwa–Môri–Sato (1980), Tracy–Widom (1993–94),
and Yau's relative entropy method (1991). The names are all spoken (except the Jimbo
co-authors and Klein/Aizenman–Warzel); the years are not. The brief's standard is
"author+title+year", so these fall just short of it. Counted as **one** item, not six,
because this is the weakest class in the file and the dates are uncontroversial.

**Counting rule for the header.** An "instance" is one claim not present in the transcript
and not carrying an arXiv id, DOI, or author+title+year on its own line. F1=1, F2=6, F3=1,
F4=2, F5=1, F8=1, F9=4, F10=1 (grouped) → **17**. F6 (timestamp) and F7 (a fourth caption
inversion) are not uncited-claim instances and are excluded from the count.

**One further item, recorded for completeness.** Line 106: "Wigner's proposal was, in his own
later phrase and Yau's from the podium, 'extremely bold' and 'or you can call it crazy'."
Both phrases are Yau's, from the transcript ("he's going to made a extremely bold claim";
"the wager has a fantastic — or you can call it crazy — idea"); neither is Wigner's own later
phrase. This is a wording slip in attribution, not an uncited claim, so it is outside the
count, but it is the one place the file assigns a quotation to the wrong mouth.

**Not found:** no invented theorem, no invented exponent, no fabricated-looking citation, no
threshold stated bare, no wrong title, no silently-filled gap.

## Self-report audit

The §11 "Note on the tutorial process" is **honest, and substantially complete, but it
under-reports in three places.**

What it gets right, and this is the larger part. Every reconstruction I could detect is
declared: the §6 denominator split and heat-semigroup reading ("my algebra"), the §7.1 √N
heuristic, the schematic loop hierarchy that Yau explicitly declined to write, and the
Fyodorov–Mirlin (1991) and Abrahams–Anderson–Licciardello–Ramakrishnan (1979) attributions
that Yau did not voice. The "piggoa and lao" identification as Aggarwal–Lopatto–Yau is
labelled in bold as "a reconstruction, not a fact" both in §5.2 and in §11 — that is the
correct handling and it is rare. Two names ("emana and ego") are declared unresolved rather
than guessed, and the unidentified "yesterday" lecture is declared too. All four declared
gaps are real: I confirmed against the transcript that Yau says "I will explain this later on
in a minute" about the comparison step and never returns to it. The Gaudin–Mehta date
discrepancy (he says 1962; the tutorial writes "around 1960") is volunteered rather than
buried, which is the opposite of the failure mode this audit is looking for.

What it under-reports:

1. **The Quanta quotation (F1) is invisible in §11.** It appears in no list — not
   reconstructions, not gaps, not "names I could not verify", not the citation tiers. §11
   asserts "Everything else … comes from the primary papers, cited inline." That sentence is
   true of the band-matrix mathematics and false of this quote.
2. **The regular-graph history block (F2) is not covered by any §11 claim.** §11 accounts for
   "the loop hierarchy, the primitive hierarchy, the quantum diffusion formula, all six
   thresholds, the localization matching result" — the mathematics. Six uncited historical
   attributions in §5.9 fall outside that enumeration and are not mentioned.
3. **The count of meaning-inverting caption corrections is under-stated (F7).** §11 says
   "Three, and all three invert a meaning." The λ large/small inversion in the d ≥ 3 Anderson
   row is a fourth. Low severity, because the transcript itself supplies the correct version
   later, but the file's own claim of exhaustiveness is what makes it a miss.
   Similarly, the Bourgade attribution (F3) belongs in the "attributions are mine" list and
   is not there.

Nothing in §11 is a false statement. The pattern is omission at the edges of the mathematics
— the history, the anecdote, one co-author — while the technical core is declared with real
discipline. The writing agent did not overstate its recovery and did not hide a gap.

## What I could not check

- **Precise pointers into the cited papers.** Definition 2.9 / eq (2.41) (the G-loop),
  Lemma 2.11 / eq (2.45) (the loop hierarchy), Definition 2.12 / eq (2.48) (the primitive
  hierarchy), Theorem 2.4 / eqns (2.8)–(2.9) (quantum diffusion), all of arXiv:2501.01718;
  eq (1.2) and Corollary 1.3 and Remarks 3.10/3.12 of arXiv:2412.20263; Theorem 2.1 of
  CLN 28. The arXiv ids are confirmed real by the caller, but I do not have the PDFs, so I
  cannot confirm that the numbered items say what the tutorial says they say. **This is the
  file's largest residual risk**: the citations are real, and the risk named in my brief was
  a real citation attached to a claim the paper does not make. Fetching those four papers and
  checking the four numbered statements would settle it.
- **Whether the mathematics is true.** Out of scope by the brief.
- **The lecture's official printed title.** The tutorial's title is Yau's own spoken words
  and I confirmed that; no programme page was available to me.
- **The two unresolved caption names** ("piggoa and lao", "emana and ego"). Audio would
  settle both.
- **The Quanta quotation.** No URL was given and I did not fetch the web.
- **Timestamp claims** ("minute 42", "minute two"). The transcript has no timestamps.

---

# Round 2 — companion formula check, 2026-08-18

Round 1 read the transcript and the tutorial, not the papers. This round fetched
**Huang–Yau, *Lecture Notes on Edge Universality for Random Regular Graphs*,
`arXiv:2602.00975`** (via ar5iv) and the arXiv abstract page for
**Huang–McKenzie–Yau, `arXiv:2412.20263`**, and checked §5.9 — the section for which the
tutorial claims that companion.

**Result: every checkable formula in §5.9 is correct.** No change to the verdict.

## Checked against `arXiv:2602.00975`

| Tutorial | Companion | Verdict |
|---|---|---|
| `:788` `λ₁ = d/√(d−1)` | Theorem 1.1 preamble, and the `2412.20263` abstract | **correct** |
| `:795` Kesten–McKay density `1_{[−2,2]} (1 + 1/(d−1) − x²/d)^{−1} √(4−x²)/(2π)` | eq. (1.3) | **correct, character for character** |
| `:801` amplitude `A = d(d−1)/(d−2)²` | eq. (1.4), `𝒜 := d(d−1)/(d−2)²` | **correct** |
| `:826` `(AN)^{2/3}(λ₂ − 2) ⟹ TW₁` | Theorem 1.1, `ℙ_H((𝒜N)^{2/3}(λ₂−2) ⩾ s₁) = ℙ_GOE(N^{2/3}(μ₁−2) ⩾ s₁) + O(N^{−ε})` | **correct**, scaling constant included |
| `:829` "the analogous statement for −λ_N; and the two limits are **independent**" | "The analogous statement holds for the smallest eigenvalues"; "the largest and smallest nontrivial eigenvalues converge in distribution to **independent** Tracy-Widom 1 distributions" | **correct** |
| `:830` bulk `N^{−1+o(1)}`, edge `N^{−2/3+o(1)}` | `2412.20263` abstract, verbatim | **correct** |
| `:832` "approximately **69%** … are Ramanujan, meaning max{λ₂,\|λ_N\|} ≤ 2" | Corollary; `2412.20263` abstract, verbatim | **correct** |
| `:803`, `:1022`, `:1037` TW₁ puts about **83%** of its mass below 0, and 0.83² ≈ 0.69 | "The Tracy-Widom 1 distribution has about 83% of its mass on {x : x < 0}… Therefore Theorem 1.1 implies 83% of d-regular graphs have the second eigenvalue less than 2" | **correct**, and the tutorial's independence-squaring is the companion's own derivation |

I also re-derived the amplitude independently, because it is the one number a reader could
check with a pen and the tutorial invites them to. Near the edge,
`1 + 1/(d−1) − x²/d` at x = 2 equals `(d² − 4d + 4)/(d(d−1)) = (d−2)²/(d(d−1))`, so its
reciprocal is `d(d−1)/(d−2)²`. That is A. It also passes the sanity check the tutorial does
not make: A → 1 as d → ∞, recovering the semicircle amplitude.

Confirmed as a **false alarm** from the depth audit: `random-matrices-localization-yau` is a
Grade B file (transcript and citation list only), and the prediction in
`DEVELOPMENT-JOURNEY.html` §7.2 was that Grade B files were unchecked, not that they were
wrong. Here they are right.

## Two attributions I still could not check

- `:797` cites the Kesten–McKay density as **"equation (1.2) of arXiv:2412.20263"**. The
  companion carries the same density as its own eq. **(1.3)**. `arXiv:2412.20263` has no
  ar5iv or arXiv HTML rendering (`ar5iv` returns "No content available", `arxiv.org/html`
  returns 404), so only its abstract was readable and the equation number is unverified.
  Same for `:833` "**Corollary 1.3**", which the companion states as its own Corollary 1.2.
  Both are plausible; neither is confirmed.
- `:404` Theorem 2.1 of the Erdős–Yau book (CLN 28) for the local law, and Theorem 2.2 of
  `arXiv:2501.01718` for the band case. The book is not online; that paper was not fetched.

## The round-1 MAJOR-adjacent finding stands

`:815` still quotes **Noga Alon**, a living person, with a source that is the single word
*Quanta* — no title, no author, no date, no URL. Nothing in this round touched it. It remains
the sharpest provenance item in the file, and the companion papers cannot settle it.

## Round 2 — exercises re-derived

Both worked solutions were re-derived by hand. **Three defects**, all detailed in
`verify/ROUND2-EXERCISES.md` Errors 1-3:

1. `:964` the constant c is wrong — the stated `c = 2 Im m_sc(E)/√(4−E²)` is identically 1;
   the correct value is `c = 1/Im m_sc(E) = 2/√(4−E²)`. Both agree at E = 0, which is why a
   spot check misses it. No downstream effect: only `c > 0` is used.
2. `:963` a dropped minus sign — `m′ = −m/(2m+z) = m/(m − 1/m)`; the second expression should
   carry the minus.
3. `:1037-1041` the Tracy–Widom tail description is backwards. TW₁ has the **thin** tail on the
   left (`exp(−|s|³/24)`) and the thicker one on the right (`exp(−(2/3)s^{3/2})`), is
   right-skewed (+0.29), and has median ≈ −1.27, below 0. The numbers 0.83 and 0.69 are correct.

Everything else in both exercises is correct, including `|m_sc(E)| = 1`, the `1 − S ≈ −DΔ`
expansion, the `t ≈ 1/η` horizon, `W ≳ √N` in d = 1, `W ≳ 1` in d = 2, and the Fréchet bound
`max(0, 0.83 + 0.83 − 1) = 0.66`.
