# Verification — knots-four-manifolds-manolescu
verdict: MINOR
uncited_external_claims: 21 (12 dated attributions in F1 + 1 named attribution in F2 + 3 items in F3 + 2 in F5 + 1 in F6 + 2 in F7. §4.14's ~15 unverifiable values (F4) are NOT counted here: they sit under an explicit section-level "Everything in this subsection is paper-only" label, which my counting policy treats as cited.)
unsupported_speaker_claims: 0 — all 12 block quotations and all 11 inline "Manolescu:" quotations checked individually against the transcript; every one maps to spoken text, with only caption-level repairs (e.g. "I define by"→"I divide by", "spaghetti with midballs"→"meatballs").
title_check: PASS — transcript: "The title of my lecture is from knots to four manifolds." The introducer announces the same. Front matter matches exactly. No repeat of the wrong-title failure.
gap_honesty: PASS — all five declared gaps sit on real transcript silences, each on an explicit spoken refusal ("I won't get into that", "you don't have to worry about it"). No gap was silently filled. The speaker's own hedge "I think we have a full computation" is preserved verbatim rather than hardened.
self_report_audit: HONEST, INCOMPLETE IN 4 PLACES — see "## Self-report audit" below.
citation_density_flag: FALSE POSITIVE — 4 arXiv instances because one companion paper is declared as the global source at :48-57, not because material is unsourced.
structural_language_flag: FALSE POSITIVE — the 3 hits are "structural differences", "structurally about", "structural match". No impact language.

## Method
Transcript is a single-line auto-caption file, 44,824 chars, read in full (200-col fold, 230 lines).
Tutorial is 1,772 lines / 102,830 bytes. Read section by section against the transcript.
Quotation sweep: grep'd every `> "` block quote (12) and every inline `Manolescu:` attribution (11)
across the whole file, including sections I had only sampled, and checked each against the
transcript. All matched.

## Findings
(in progress)

## Counting policy (stated up front, because it changes the numbers)

This file's citation model is **one companion paper sourced globally**, not inline arXiv ids.
`summaries/...:48-57` declares it: "Every displayed formula below comes from the paper. So does
every proper name." §10 repeats it. The paper is arXiv:2601.05425 and I cannot open it. So:

- A claim tied to the paper with a locator (a §, a figure, a bracketed reference number, or the
  phrase "the paper says/states/notes") counts as **cited**. Those go to "What I could not check",
  not to findings. This is why the "4 arXiv instances in 102 KB" density flag is a **false
  positive** — the density is low because one source covers the whole document by declaration.
- §2–§3 (~lines 150–582) is a deliberately-built background bridge, ~430 lines of standard
  textbook material that is not in the talk at all and is announced as such. I do **not** flag
  each definition. I count named theorems, named attributions, specific dates, and specific
  numeric values individually, and report generic bridge material as one class-level note.
- The 3 hits for "structural" (lines 60, 266, 1711) are "structural differences", "structurally
  about", "structural match". None is impact language. That flag is also a false positive.

## Findings

### F1 — MINOR, class-level. Precise dates attached to named theorems that the talk gave only by decade, with no locator.
`summaries/knots-four-manifolds-manolescu.md:92, 127, 128, 355, 367, 433, 483, 598, 936, 1095, 1192`
(12 dated attributions across 11 lines — `:127-128` carries two, Donaldson 1983 and Seiberg-Witten
1994; `:483` carries two, Lickorish 1962 and Wallace 1960.)

Each of these is a correct-sounding date the transcript does not contain and the file does not
source to the paper:

- `:92` "That is Taubes' theorem (1987)". The transcript states the fact ("in dimension four it
  has uncountably many") but **never names Taubes and never gives a year**. This is the single
  cleanest example of the class: a named theorem attribution invented from background knowledge.
- `:127-128` "Donaldson did it ... in 1983. Seiberg and Witten wrote down a better equation in
  1994." Transcript says only "in the 1980s" and "in the 90s".
- `:355` "The Alexander polynomial, from 1928"; `:367` "The Jones polynomial, from 1984". No date
  spoken for either.
- `:433` "Freedman's 1982 theorem". Transcript names Freedman, gives no year and does not state
  the classification theorem.
- `:483` "Theorem (Lickorish 1962, Wallace 1960)". Names spoken ("licorice wallace theorem") and
  §10 sources the names to "paper, Thm 4.1"; the two years are not sourced.
- `:598` "Khovanov 2000"; `:936` "Morrison, Walker and Wedrich, 2019 (published 2022)" — 2019 is
  spoken, "(published 2022)" is not.
- `:1095` "the slice-ribbon conjecture, open since 1966"; `:1192` "Akbulut proved it in 1991".
  Akbulut's name is spoken, the year is not.

**Why it matters.** These are the exact risk class the caller named: who proved what, and when.
Every one of them is plausible and I believe most are right, but the file gives a reader no way to
check any of them, and the reader is explicitly told the sourcing rule is "the paper". If these
came from the paper's bibliography the file should say so; if they came from the writing agent's
own knowledge they are unlabelled reconstruction.
**What would settle it:** the bibliography of arXiv:2601.05425. If each year appears there, this
collapses to a formatting complaint. If not, they are unsourced additions.

### F2 — MINOR (worst single item). A named external attribution with no anchor in either source.
`summaries/knots-four-manifolds-manolescu.md:866-868`

> "A fourth application the talk omits: knot Floer homology was used by **Juhász and Zemke**
> to compute Ozsváth–Szabó invariants of manifolds built by 'concordance surgery' — a
> computation nobody knows how to do on the Seiberg–Witten side."

"Juh" and "Zemke" appear **nowhere in the transcript** (checked). The sentence itself says the
talk omits it, so it is by construction external. It carries **no paper locator** — no §, no
figure, no bracketed reference number — unlike every neighbouring attribution in §4.10, which
do carry them ("the paper's reference [52]"). And it is **not listed anywhere in §10**, neither
in the name-correction table nor in the reconstruction list.
This is the only place in 1,772 lines where a named result is attributed to named people with
zero traceable source of any kind. It is almost certainly from the paper's §5.4 or similar, but
the file does not say so.
**What would settle it:** find Juhász–Zemke in the bibliography of arXiv:2601.05425.

### F3 — MINOR. Mechanism and specific manifolds in §4.10 that are neither spoken nor located.
`summaries/knots-four-manifolds-manolescu.md:843-861`

Three items in one paragraph, all absent from the transcript and none given a paper locator:

- "constructed a **new** exotic ℂP² # 9ℂP̄²". The talk never names the manifold; it says only
  "new exotic examples". The "9" is supplied.
- "proving it exotic with the Ozsváth–Szabó invariant". Not spoken at that point.
- "**Their manifold carries a free involution. Quotient by it**, and you get a manifold with
  fundamental group ℤ/2 and negative definite intersection form." This is a whole construction
  — free involution, quotient — that appears nowhere in the transcript. It is the mechanism
  that produces the section's headline theorem, and it is unsourced.

Note the contrast within the same paragraph: the π₁ = ℤ/2 caveat and the [52] authorship
correction **are** explicitly sourced to the paper. So the file knows how to cite here and did
not for these three. That pattern suggests the involution/quotient account may be reconstruction
rather than paper text.
**What would settle it:** §5 of arXiv:2601.05425, or Levine–Lidman–Piccirillo directly.

### F4 — MINOR. §4.14 is 65 lines of dense unverifiable numbers under a single section-level source label.
`summaries/knots-four-manifolds-manolescu.md:1080-1141`

The section opens honestly — "**Everything in this subsection is paper-only.**" — and the claim
is independently corroborated: I confirmed "slice", "ribbon", "Dunfield", "Gong", "Nakamura",
"Marengon", "Gukov" are all **absent from the transcript**, exactly as the file states at
`:64-66`. So the labelling is truthful.

But this is the file's highest-risk block and I want it named as such. Under one blanket label
it carries: 350 million prime knots, ≤19 crossings, 99.5% / 0.5% / 0.003%, ~11,400 undecided,
smallest at 13 crossings, "five candidate pairs", "the right-handed trefoil is H-slice in
#3ℂP² # 20ℂP̄² but not in K3 # ℂP̄²", the definitions of H-slice and k-slice, and the explicit
gluing W = (D⁴ ∖ nbhd(Δ)) ∪ X(K′,0). **Not one of these has a transcript check available**,
because the section was never delivered. The internal arithmetic is consistent (100 − 0.003 =
99.997%, matching `:1457`), which is a weak positive signal and nothing more.
**What would settle it:** §7 of arXiv:2601.05425. Until then, treat §4.14 as single-sourced.

### F5 — MINOR. §5's central numbers are quoted without an in-body source.
`summaries/knots-four-manifolds-manolescu.md:1147-1177`

The knot names (K₁ = −5₂, K₂ = P(3,−3,−8)) and the full bigraded answer
(𝒮_{0,q}(W₁;1)⊗ℚ = ℚ at q = 1,3; 𝒮_{0,q}(W₂;1)⊗ℚ = ℚ at q = −1,1) are **not in the transcript**.
The speaker names neither knot and states only the q = −1 comparison, which the file quotes
correctly. §10 concedes the derivation is impossible ("I can quote the answer but not derive
it"), which implies the answer is quoted from the paper — but §5 itself never says so.
Also `:1194` "the **first analysis-free proof** of the existence of an exotic pair of compact
orientable four-manifolds" is a stronger claim than the transcript's "now we have an
analysis-free proof that they are not diffeomorphic", and the word "first" is uncited.
**What would settle it:** §6.5 of arXiv:2601.05425, or Ren–Willis arXiv directly.

### F6 — MINOR. Two unflagged half-name expansions of the caption "Sabo".
`summaries/knots-four-manifolds-manolescu.md:838`

The transcript: "an early example of this was in one of the earlier papers by **Sabo** — they
computed the invariant of the K3 surface in this way by cutting it into handles."
The tutorial: "**Ozsváth and Szabó** did exactly this for the K3 surface."

This is the *same* correction §10 lists as substantive correction 3 (the surgery formula
"proved by Szabó" → Ozsváth–Szabó), applied a second time at a different place, without being
listed. Almost certainly right and almost certainly the same dropped-hyphenated-name caption
error. But §10 says "**Substantive corrections, not spellings. Three**" and this is a fourth.

### F7 — MINOR, class-level, low severity. Bridge elaborations beyond both sources.
`summaries/knots-four-manifolds-manolescu.md:135-137, 830-833, and §3 generally`

Per my counting policy I do not itemise §3's textbook definitions. Two elaborations are worth
one line because they add specificity the sources do not:
- `:135-137` gauge-theory solutions "correspond to holomorphic bundles or to divisors" — the
  transcript says only "there are some methods for studying these solutions".
- `:830-833` bordered Floer "computer programs for **the hat version**" and "a parallel theory
  for knots that decomposes a knot into **tangles**" — the transcript says "computer programs
  for **some version**" and mentions no tangles.
Both are plausible and neither changes any conclusion.

## Self-report audit

The extra instruction: is §10 ("Note on the tutorial process", `:1621-1772`) honest and complete
against what I actually found?

**Verdict: substantially honest, and unusually so. Under-reported in four small places.**

### What I verified as true

1. **The name-correction table is real, not decorative.** I grep'd 15 of the 30 caption strings
   against the transcript verbatim: `Rasm Muen`, `Kudluhani talps`, `Salivan Jang`, `Buer`,
   `licorice wallace`, `Nate Halot`, `Ben Ren Willis`, `boner sphere`, `curvy diagram`,
   `Abdulut`, `Frobinius`, `lipshit thirstston`, `kangi jini Honda`, `Sharkar`,
   `Morrison Walker and Vedric`. **All 15 present, exact.** A fabricated table would not survive
   this. This is the single strongest honesty signal in the file.
2. **All three "substantive corrections" check out against the transcript.**
   - "proved by Sabo" — transcript verbatim: "for knots the surgery formula was proved by Sabo".
   - The LLP/LP authorship split — transcript has both passages, exactly as quoted: "Lavin
     Lidman and Pikilo had a paper" and "Lidman and Pikerillo and Levvin they they found new
     examples".
   - The π₁ = ℤ/2 omission — the transcript's definite-intersection-form passage genuinely says
     nothing about the fundamental group. Confirmed absent.
3. **All five declared gaps match real transcript silences.** "There is a way of assigning
   signs. I won't get into the details of that" (grid signs); "It is bgraded... I won't get into
   that" (bigradings); "I wrote here the equations that you don't have to worry about it but
   they involve a dro operator a spinner and the curvature" (Seiberg–Witten); no 1-handle skein
   formula anywhere; and the S¹×S³ / S¹×D³ discrepancy is real — the transcript says "for S1
   times S3 **I think** we have a full computation", and `:1050` preserves that "I think" hedge
   verbatim rather than hardening it. Preserving a speaker's hedge is a deliberate honesty
   choice and I want it recorded.
4. **Every §10 pointer resolves.** "Flagged in §3.3" → the writhe ½ warning is at `:399-408`.
   "Flagged in §4.8" → present. "Corrected in §4.9" / "§4.10" → both present. "I quote both in
   §4.13 and decide nothing" → `:1050-1064`, and it genuinely decides nothing. No dangling
   pointer.
5. **The "0 reconstructed labels" concern in my brief is a false alarm.** The grep for the exact
   word "(reconstructed)" returns nothing, but point-of-use labels exist in other wording:
   `:185` "**The second use, which is mine and which I am labelling as mine**", the boxed
   "**Marked as my framing** ... **What would verify it**" at `:207-216`, `:495` "described in
   words since you cannot see Figure 7", `:949` same for Figures 13-14, and `:1376`
   "**Reconstructed:** ... **What would verify it:**". §10's claim that "where the prose is my
   reconstruction of a figure I have said so at the point of use" **holds**.
6. **The 88! arithmetic is right.** `:817` says "88! is about 1.85 × 10^134". Stirling gives
   log₁₀(88!) ≈ 134.3. Correct, and it is the writer's own arithmetic on the speaker's own
   spoken "88", which `:822-824` explicitly attributes to him and marks unverified.

### What §10 under-reported

- **U1 (matches F2). Juhász–Zemke.** §10 lists 30 name corrections, 3 substantive corrections,
  5 reconstructions, 5 gaps, 2 companion-document errors, 1 unverifiable item, and a dates note.
  It does **not** mention that §4.10 introduces two mathematicians and a result that exist in
  neither the transcript nor any cited locator. Given how granular the rest of §10 is, this
  omission is the one real hole in it.
- **U2 (matches F6). "Three substantive corrections" is four.** The second silent expansion of
  "Sabo" → "Ozsváth and Szabó", at `:838` for the K3 computation, is the same class of change
  §10 lists as correction 3 and is not listed.
- **U3 (matches F1). The dates are never mentioned.** §10 has a whole subsection "On dates" —
  but it is only about the arXiv stamp and the 2001/2003 preprint-vs-journal question. It says
  nothing about the twelve dated attributions the file supplies that the talk gave only by decade or
  not at all (Taubes 1987, Donaldson 1983, Seiberg–Witten 1994, Alexander 1928, Jones 1984,
  Freedman 1982, Lickorish 1962, Wallace 1960, Khovanov 2000, MWW "published 2022", slice-ribbon
  1966, Akbulut 1991). Under §10's own declared rule — "every displayed formula comes from the
  paper, so does every proper name" — dates fall in the gap between the two, and the reader is
  never told which of the two supplied them. `:92` "Taubes' theorem (1987)" is the clearest
  case: the speaker states the fact and names nobody.
- **U4 (matches F3). The free-involution/quotient construction.** §10's reconstruction list has
  five entries and this is not one, even though it is the argument that produces §4.10's
  headline theorem and appears in neither source I can read.

### Net

§10 is a far more rigorous self-report than the risk profile predicted, and it is honest in the
direction that matters — it volunteers two errors *in the companion paper*, refuses to name the
introducer on thin evidence, declines to invent three objects it could easily have faked
(`:1762-1767`), and preserves a spoken hedge it could have quietly hardened. The four
under-reports are all of the same shape: **material sourced from the paper's body or from
general knowledge, presented without a locator, and not listed among the reconstructions.** None
is a fabrication. None changes a conclusion. But a reader taking §10 as a complete inventory of
where the file goes beyond its sources would be missing F1, F2, F3 and F6.

## What I could not check

- **The companion paper, arXiv:2601.05425.** Fetching it is outside this brief's scope and it is
  not in the repo. One corroboration I do have: my tasking prompt independently named
  arXiv:2601.05425 as Manolescu, *From knots to four-manifolds* — the same id, author and title
  the file gives. That retires the worst residual risk here, a fabricated central citation. Every claim the file attributes to the paper — all displayed equations, the
  bibliography numbers [3], [12], [21], [41], [45], [47], [49], [52], [53], [54], [56], [59],
  [61], [62], [71], [82], [83], [84], [88], [90], [96], the §/Figure/Theorem/Question/Conjecture
  locators, the two claimed errors in the paper (writhe ½, "horizontal" β curves), and the whole
  of §4.14 — is unverifiable here. **This is the dominant limitation of this report.** Roughly
  half the file's substance rests on a document I cannot open.
- **Whether the full citations are real.** Manolescu–Ozsváth–Sarkar, *Annals* 169 (2009);
  Manolescu–Ozsváth–Thurston, *Annals* 201 (2025); Floer, *Comm. Math. Phys.* 118 (1988)
  215–240; Gompf–Stipsicz GSM 20 (1999); Ozsváth–Stipsicz–Szabó MSM 208 (2015). A fabricated
  journal/volume/year would be MAJOR. I could not check any of them. They are internally
  plausible and consistent with spoken hedges ("work with Obat and Sharkar from 20 years ago").
- **Whether the mathematics is true.** Out of scope by the brief's hard rule. I did not test any
  statement for correctness, only for provenance.
- **The slides.** Nineteen figures carried the entire formula content. Both the file and I are
  blind to them. Several open questions in this report (the "9" in ℂP² # 9ℂP̄², the S¹×S³ vs
  S¹×D³ discrepancy, the 88) would be settled by one slide each.
- **The other 15 rows of the name table.** I spot-checked 15 of 30; the remaining 15 are likely
  fine given the hit rate but were not individually confirmed.
