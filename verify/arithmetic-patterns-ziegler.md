# Verification — arithmetic-patterns-ziegler
verdict: MINOR
uncited_external_claims: 4
unsupported_speaker_claims: 0
title_check: PASS — chair announces "the structure of sets with an unexpected number of arithmetic patterns"; Ziegler repeats it verbatim in her own second sentence. Front-matter title matches exactly.
gap_honesty: PASS — the single `[Gap: …]` marker (PTE, line 859) and the single `[My reading]` marker (line 872) both sit where the transcript really is silent; no gap is silently filled with mathematics.
self_report_audit: HONEST BUT INCOMPLETE — §11 makes the critical disclosure (no ICM 2026 paper; 2014 companion; last third from primary papers) and does not restore 2026 content from the 2014 survey. It omits three additions: the invented §4 timeline, a stale 2014 open-problem status stated as current, and one uncited researcher name.

**Why MINOR and not MAJOR:** no invented theorem, no wrong title, no fabricated citation. All
24 arXiv instances resolve (checked independently by the caller). The four uncited claims are
navigational or standard-textbook, not load-bearing mathematics.

**Caller question (b) — answered, cleared.** I fetched the abstract of arXiv:1605.04628. Every
clause the tutorial attributes to Tao's 2016 paper is in that abstract, including the two I
had provisionally flagged. See finding F4.

### Progress log — sections 1–4 read against the full transcript

The transcript is a single 40.7 KB line (387 wrapped lines). I read all of it. No Q&A follows
the applause. Transcript quoted below by wrapped-line number.

**Attribution ledger (caller question (a): Ziegler vs. others).** Checked every named result:

| Tutorial line | Attributed to | Transcript support |
|---|---|---|
| 548 | Roth–Meshulam | "the Roth Mishulan dichotomy" (tr. 44) ✓ |
| 555 | Szemerédi 1975 | "sami ... his celebrated sarity theorem" (tr. 76) ✓ |
| 568 | Furstenberg (Kronecker factor, k=2) | "what Fenberg shows ... obstruction comes from a non-trivial morphism to an aelion dynamical system" (tr. 113–114) ✓ |
| 575 | Furstenberg–Weiss, 1980s, 2-step nilpotent | "fenber advice in the 80s showed that there are new obstructions coming from ... two-step nil potent" (tr. 140–141) ✓ |
| 587 | Conze–Lesigne; Furstenberg–Weiss (4-term universal char. factor) | "kwansine and fenburg and vice showed ... the universal characteristic factor for four term progressions has a structure of a two step ... pro nil systems" (tr. 158–160) ✓ |
| 597 | Host–Kra 2005; Ziegler 2007 (general k) | "shown by this by host Cryan myself" (tr. 165–166) ✓ — the tutorial correctly reads "myself" as Ziegler's own JAMS 2007 paper and does NOT claim she proved the k=2 or k=3 cases |
| 632 | Green and Tao *conjectured* the inverse theorem | "green and conjectured that the underlying reason should be algebraic" (tr. 193) ✓ |
| 516/644 | Green–Tao–Ziegler *proved* it (arXiv:1009.3998) | not spoken; carries full citation ✓ |
| 637 | Green–Tao (progressions in primes) | "green and tiles theorem" (tr. 220) ✓ |
| 761 | Tao 2016 (log-Chowla ⟺ log-Sarnak) | "Tao showed in 2016 that ... a logarithmic ... version of these conjectures ... they actually are equivalent" (tr. 307–308) ✓ |
| 773 | Frantzikinakis–Host 2018 | "franchikinakis and host in 2018" (tr. 315) ✓ |
| 782 | Matomäki–Radziwiłł | "Matumaki Razil about short interval estimates" (tr. 320–321) ✓ |
| 784 | Tao's entropy decrement argument | "an additional ... entropy decrement argument of toao" (tr. 322) ✓ |
| 799 | Matomäki, Radziwiłł, Tao, Teräväinen, **Ziegler** | "relatively recent work with Mataki, Radi Tao and Terodina" (tr. 329) ✓ — "with" makes her a coauthor, not sole author; tutorial lists her last, correctly |
| 826 | Walsh | "Walsh was able to show" (tr. 349) ✓ |
| 734 | "Sarnak proved Chowla ⟹ Sarnak" | "sarn shows that his conjecture follows from chala's conjecture" (tr. 288) ✓ |

**Verdict on (a): the tutorial separates Ziegler's own results from others' cleanly.**
Nowhere does it hand her a theorem the transcript gives to someone else. It is in fact more
conservative than it needed to be: §4.7 splits Host–Kra (2005) from Ziegler (2007) where the
captions say only "host Cryan myself".

**Leng / Sah / Sawhney: absent.** The tutorial makes **no** quantitative-bound claim about
the inverse theorems — so it cannot get one wrong. The one consequence is the reverse
problem: it inherits the 2014 companion's "these bounds are open" and states it as current.
See finding F2.

---

## Findings

### F1 — MINOR/systemic. Eighteen fabricated timestamp ranges; the transcript has none.
`summaries/arithmetic-patterns-ziegler.md:539, 546, 553, 560, 565, 573, 595, 626, 635, 678, 683, 704, 736, 756, 771, 808, 844, 863`

Every §4 subsection heading carries a clock range — "(00:00–08:00)", "(30:00–36:00)",
"(70:00–end)". The transcript file contains **zero** timestamps (grep for a `[0-9]:` pattern
returns 0 hits; it is one unbroken 8,048-word paragraph). The ranges are therefore inferred,
and nothing in the document says so.

Why it matters: a reader will treat them as citations and try to scrub to 56:00 for the
Sarnak/entropy argument. They are also internally inconsistent — line 29 says "**In fifty
minutes** she uses Kronecker factors, …", §11 line 1481 says "five minutes of a
**seventy-minute** talk", and line 1500 says "None of the three fit in a **fifty-minute**
talk". The §4 grid runs to 70:00. Both numbers cannot be right. 8,048 words at a normal
lecture pace of 130–160 wpm is about 50–62 minutes, which favours the fifty.

What would settle it: the video runtime from the YouTube metadata for `czHiX0pYTDg`.

**Not disclosed in §11.** The self-report lists reconstructions, name corrections, caption
corrections and gaps in detail — and never mentions that the timeline is invented. This is
the clearest under-report.

### F2 — MINOR. "no effective bounds" for the inverse theorem, sourced from a 2014 document, stated as current.
`summaries/arithmetic-patterns-ziegler.md:331-332, 921-922, 953-955`

Three statements:
- 331: "both inverse theorems are **qualitative**: making them quantitative is, in the
  companion's words, 'a major open question'." — attributed, fine
- 921: "This step is the hard one … and it is qualitative — **no effective bounds**." — flat
  present tense, no attribution
- 953: "**Honesty check.** … What is *not* known: quantitative forms of step 2" — flat
  present tense, no attribution

The companion is arXiv:1404.0775, **April 2014**. Ziegler never says this from the podium —
no such claim appears anywhere in the transcript. Presenting a 2014 open-problem status as
the 2026 state of the art is exactly the 2014-companion hazard, and lines 921 and 953 drop
the "in the companion's words" hedge that line 331 keeps. Whether the status has since
changed I cannot determine from the two files I have; the fix is one hedge, not a rewrite.

What would settle it: a literature check on quantitative bounds for the U^(s+1)[N] inverse
theorem published between 2014 and 2026.

**Not disclosed in §11.**

### F3 — MINOR. Uncited name: "the Walsh/**Pilatte** frontier".
`summaries/arithmetic-patterns-ziegler.md:954`

"Pilatte" appears exactly once in the document, in §5's honesty check. No citation, no arXiv
id, no first name, no explanation — and §4.16, which the sentence cross-references, discusses
only Walsh. Not in the transcript. Every other researcher named in the tutorial carries
either transcript support or a full citation; this one carries neither.

What would settle it: an arXiv id, as given for Walsh (2310.07873), Koymans–Pagano
(2412.01768) and Zywina (2502.01957).

**Not disclosed in §11.**

### F4 — RESOLVED, NOT A DEFECT. Caller question (b): the Tao arXiv:1605.04628 attribution is fully correct.
`summaries/arithmetic-patterns-ziegler.md:761-765`

> "**Theorem (Tao 2016).** The logarithmically averaged Chowla and Sarnak conjectures are
> **equivalent** to each other, **and to the 'local Gowers uniformity' of λ**."

The first half is exactly what she says (tr. 307–312: "Tao showed in 2016 that if you take a
logarithmic average version of these conjectures then they actually are equivalent") and
exactly what the cited paper's title asserts. **Correct.** The tutorial also gets the
neighbouring attributions right: **Sarnak**, not Tao, proved Chowla ⟹ Sarnak (line 734 vs
tr. 288), and the entropy decrement argument is **Tao's** (line 784 vs tr. 322).

I initially flagged the third conjunct — equivalence "to the local Gowers uniformity of λ" —
and the parenthetical "The proof uses the entropy decrement argument together with the
Green–Tao–Ziegler inverse theorem", because neither is spoken in the transcript and neither
is implied by the paper's title. **I then fetched the arXiv abstract, and all three check
out.** Tao's own abstract for 1605.04628:

- names the equivalence "to the **'local Gowers uniformity'** of the Liouville function" as
  part of the main result — the tutorial even keeps Tao's scare quotes;
- names "the **entropy decrement argument** of the author used recently" as a main tool;
- names "the **inverse conjecture for the Gowers norms, obtained by Green, Ziegler, and the
  author**" as the other key tool.

So the tutorial did not stretch the citation. It supplied three details from the paper it
cites, at the point of citation, exactly as the front matter promises. **Claim attribution
on arXiv:1605.04628 is correct in every clause.** Nothing to fix.

Source: [arXiv:1605.04628](https://arxiv.org/abs/1605.04628).

The name-correction table at lines 1412–1413 lists "Tao arXiv:1605.04628" as the *source* for
the spellings **Chowla** and **Sarnak**. That is a source for an orthography, not a claim
attribution, and is fine.

### F5 — MINOR. Riemann-hypothesis equivalence: an exponent not spoken and not cited.
`summaries/arithmetic-patterns-ziegler.md:695-697`

"Σ_{n≤N} λ(n) = **O(N^(1/2+ε))** is equivalent to the Riemann hypothesis." She says only
"square root cancellation" and "like random walk on the integers" (tr. 252–254). The
neighbouring PNT equivalence at line 693 *is* spoken (tr. 248–252). The 1/2+ε is standard
textbook material, but per the brief every quantitative statement not in the transcript needs
a citation on its own line, and this one has none.

By contrast the tutorial handles the other numbers correctly: δ³|V|² and δ²|V|² (tr. 31, 42),
N^(1/3) (tr. 57), σ_k·N²/(log N)^k (tr. 222–223, 230), N^θ (tr. 336–337), log 2 and zero
entropy (tr. 276–279), λ(12) = −1 (tr. 245) are all spoken; Sanders' 1/(log N)^(1−o(1))
(line 228) and Walsh's (log X)^(ψ(X)) (line 829) both carry sources.

### F6 — informational, not a defect. Zywina's mechanism.
`summaries/arithmetic-patterns-ziegler.md:853-857`

The tutorial says Zywina gets infinitude "by applying the **Tao–Ziegler** polynomial
Szemerédi theorem for primes — that is, her own theorem, Acta Math. 201 (2008), 213–305."
She does **not** say this; she names the elliptic-curve result in one clause (tr. 359–361)
with no author. The claim carries the arXiv id 2502.01957 so it passes the brief's citation
test, but the rhetorical payoff ("her own theorem") is the tutorial's construction, not hers.
I cannot check the paper. Low risk; recorded for completeness.

---

## Self-report audit (§11, lines 1368–1506)

**Verdict on the self-report: honest in substance, thorough well beyond the norm, and
under-reported in three specific places.**

What §11 gets right, and it is a lot:

- It states plainly that there is **no ICM 2026 proceedings paper** and that the companion is
  a **2014 sectional survey** that "**stops in 2014**" (lines 42–61, 1379–1384). It says the
  last third is restored from primary papers. This is the single most important disclosure
  the caller asked about, and it is made three times: front matter line 9, the "A note on
  sources" block at lines 57–61, and §11 lines 1382–1384. **It does not restore 2026 content
  from the 2014 document.**
- It separates **four substantive caption corrections** (indexing drift; the weaker
  plain-existence vs. the averaged Furstenberg statement; the non-classical-polynomial
  caveat; Walsh's GRH-vs-RH) from mere spellings, and all four check out against the
  transcript.
- It lists **six reconstructions** with a verification recipe for each. I confirmed all six
  are genuinely absent from the transcript — that is, it did not claim as spoken anything it
  invented.
- It names the two acknowledgement spellings it **could not** verify and refuses to guess
  (lines 1430–1434). That is the right call.
- Its four declared gaps (PTE, the multidimensional outlook, the slides, Conze–Lesigne) are
  real gaps: the transcript genuinely says nothing more on any of them. The one in-text
  `[Gap: …]` marker (line 859) and the one `[My reading, marked as such]` marker (line 872)
  are both placed where the transcript is actually silent.
- Its 29-row name table is accurate. I checked every caption string against the transcript;
  all 29 mangled forms occur there, and every correction is either transcript-derivable or
  labelled "search".

**Where §11 under-reports.** Three items, all things the writing agent added and did not
list:

1. **The §4 timestamps (F1).** Eighteen invented clock ranges, presented with the authority
   of a citation, plus a 50-vs-70-minute self-contradiction. §11 has a "Reconstructed, with
   what would verify each" list; the timeline belongs on it and is absent. This is the
   material omission.
2. **The stale 2014 open-problem status (F2).** §11 has a whole subsection titled "Where the
   companion beats the talk", naming three places the 2014 document is *better* than the
   talk. It has no corresponding note on where the 2014 document is **older** than 2026 — and
   "quantitative inverse theorems are open" is precisely such a place. §3.10 hedges it; §5
   twice does not.
3. **"Pilatte" (F3).** A researcher named once, uncited, in a document whose §11 makes a
   point of listing everything it could not verify. Either a citation was dropped or a name
   was recalled from memory; §11 mentions neither.

**Not under-reported — checked and cleared:**

- No claim of an ICM 2026 paper anywhere.
- No 2026 content presented as coming from the 2014 companion. Every post-2014 result
  (Tao 2016, Frantzikinakis–Host 2018, MRTTZ 2023, Walsh 2023, Koymans–Pagano 2024, Zywina
  2025) carries its own arXiv id at the point of use, never a companion reference.
- No theorem transferred to Ziegler that the transcript gives to someone else — see the
  attribution ledger above.
- All 20-plus direct quotations are faithful to the caption text; several are verbatim.
- The `[Gap: …]` marker is used where the transcript is silent, not to paper over anything.

---

## What I could not check

- Whether the mathematics is **true**. I have neither the companion (arXiv:1404.0775) nor any
  of the 20-plus cited primary papers. Every "(Companion, Theorem X.Y)" pointer is unverified
  as to *content*; I verified only that such pointers exist and are used consistently.
- Whether "quantitative inverse theorem" is still open in 2026 (F2).
- Who "Pilatte" is and which result is meant (F3).
- Zywina's actual proof mechanism (F6).
- The video runtime, which would settle the 50-vs-70-minute contradiction (F1).
- The two unverified acknowledgement names ("Cecile Gashon", "Danny Castle"). The tutorial
  also does not know them and says so; I have no better source.
- Every displayed formula. The captions carry none, so for §§2, 3, 5, 6 and 7 I could check
  only that a citation or a "reconstructed" label is attached — never the algebra itself. Per
  the hard rule I did not invent mathematics to test mathematics; §7's worked solutions look
  internally consistent on inspection, but I make no claim about them.

---

# Round 2 — companion formula check, 2026-08-18

Round 1 was a transcript-and-citation-list check. This round fetched the companion —
Ziegler, *Linear equations in primes and dynamics of nilmanifolds*, `arXiv:1404.0775`
(her ICM 2014 sectional survey), via ar5iv — and compared every statement the tutorial
attributes to it.

**Result: every companion-attributed statement is correct.** No change to the verdict.

## Checked against `arXiv:1404.0775`

| Tutorial | Companion | Verdict |
|---|---|---|
| `:452` `Δ_h f(x) = f(x+h)·conj(f(x))` | Definition 5.1 | **correct** |
| `:456` `‖f‖^{2^k}_{U^k} = 𝔼_{x,h₁,…,h_k} Δ_{h₁}⋯Δ_{h_k} f(x)` | Definition 5.1 | **correct** |
| `:461` 1-bounded `‖f‖_{U^k} = 1` iff `f = e^{2πi q(x)}`, `deg q < k` | first bullet after Remark 5.2 | **correct**, including the strict `< k` |
| `:464` correlation implies large norm, by repeated Cauchy–Schwarz | second bullet | **correct** |
| `:465` a random ±1 function has `‖f‖_{U^k} = o(1)` | third bullet | **correct** |
| `:469` `AP_k(f) = 𝔼_{x,d} f(x)f(x+d)⋯f(x+kd)` and `\|AP_k(f) − AP_k(g)\| ≪_k ‖f−g‖_{U^k[N]}` | eq. (3) and the sentence defining `AP_k` as the count of **(k+1)**-term progressions | **correct**, and the tutorial's `(k+1)-term ↔ U^k` pairing at `:342` is the companion's own indexing |
| `:474-478` generalized von Neumann, m forms in d variables, no two affinely dependent | Proposition 5.3 | **correct**, hypothesis included |
| `:510-516` the over-ℤ inverse theorem: finite list of s-step nilmanifolds depending on (s, δ), some g ∈ G, Lipschitz F, `\|𝔼_{n∈[N]} f(n) conj(F(gⁿxΓ))\| ≥ c(s,δ)` | Conjecture 8.1, GI(s) | **correct**, clause for clause |
| `:518` Green–Tao–Ziegler, **Ann. of Math. 176 (2012), 1231–1372** | reference [24]: "Ann. Math. (2) 176 (2012), no. 2, 1231-1372" | **correct**, page range included |
| `:519` "(Companion, Conjecture 8.1 and Theorem 8.4.)" | Theorem 8.4 is stated as "Conjecture 8.1 was proved" | **correct pointer** |

## The caveat at `:501-509` is the file's strongest passage, and it is right

The tutorial says the naive finite-field inverse conjecture is **false**, that the
counterexample for `U⁴(𝔽₂ⁿ)` was found **independently by Green–Tao and by
Lovett–Meshulam–Samorodnitsky (STOC 2008)**, that the repair replaces "polynomial" with
**non-classical polynomial** (noting the companion's word is "non-standard"), that this is
**Theorem 8.3, Bergelson–Tao–Ziegler and Tao–Ziegler**, and that Ziegler says "polynomial
phase function" from the podium without the caveat.

Every clause checks out:

- Companion: "Surprisingly, **Conjecture 8.2 turned out to be false**; a counter example for
  the `U⁴[𝔽₂ⁿ]` was constructed **independently** in [18, 35]."
- Reference **[18]** is B. Green, T. Tao, *The distribution of polynomials over finite fields,
  with applications to the Gowers norms*, Contrib. Discrete Math. 4(2), 2009.
- Reference **[35]** is S. Lovett, R. Meshulam, A. Samorodnitsky, *Inverse conjecture for the
  Gowers norm is false*, **STOC 2008**.
- Companion Theorem 8.3 is credited "(Bergelson-Tao-Z (10), Tao-Z (10,12))" and its
  conclusion is a **non-standard polynomial of degree ≤ s**.

One precision the tutorial could add: the companion numbers the *false* statement
**Conjecture 8.2** (the finite-field form), while **Conjecture 8.1** is the ℤ form that is
true. The tutorial cites 8.1 and 8.3 and 8.4 correctly and never cites 8.2, so nothing is
wrong — but a reader tracing "the naive form of this conjecture is false" back to the
companion will be looking for a number the tutorial never gives.

## Re-derived independently, not just matched

Two things in §3.8 are the tutorial's own and neither is in the companion. Both are correct.

- **`:150` the U² identity.** `‖f‖⁴_{U²} = Σ_r |f̂(r)|⁴` and `‖f̂‖⁴_4 ≤ ‖f̂‖²_∞·‖f̂‖²_2` are
  standard; with Parseval `Σ_r|f̂(r)|² = 𝔼_x|f(x)|² ≤ 1` for 1-bounded f, they give
  `‖f‖⁴_{U²} ≤ ‖f̂‖²_∞`, hence `‖f‖_{U²} ≥ η ⟹ ‖f̂‖_∞ ≥ η²`. The tutorial's conclusion is
  right, including the square.
- **`:157` the 3AP Fourier identity**, which the tutorial labels *reconstructed* because "the
  companion asserts the consequence without displaying the identity" — an accurate description
  of the companion. I re-derived it. Expanding all three functions in characters gives the two
  constraints `a+b+c ≡ 0` and `b+2c ≡ 0`, so `b = −2c` and `a = c`, leaving
  `Σ_c f̂(c) ĝ(−2c) ĥ(c)`. **That is exactly what the tutorial prints.**

## What this round did not check

Everything in the talk's last third, which postdates the 2014 survey: Chowla, Sarnak,
logarithmic averaging, the Liouville subshift, sign patterns, the multidimensional frontier.
The tutorial cites those to primary papers (`arXiv:1708.00677`, `arXiv:2007.15644` and
others named inline); none was fetched. Also unchecked: the round-1 finding at `:921`/`:953`
that a 2014 open-problem status is stated as present fact — the companion is precisely the
2014 source, so it cannot settle whether the status changed since.

---

## Round 2 — exercises re-derived, 2026-08-18

Both worked solutions re-derived by hand, all ten parts. **The mathematics is correct
throughout.** Two wording slips, detailed in `verify/ROUND2-EXERCISES.md` Error 4:

- `:1039` "Summing the **at most 7** nonzero mixed terms" — the solution has just shown that
  three of the seven mixed terms vanish, so at most **4** are nonzero. The bound still holds
  and the exercise statement's constant 7 is correct as a generous bound; the sentence just
  contradicts the one before it.
- `:1037` the Cauchy–Schwarz step writes `≤ ‖f̂‖_∞ Σ_r |f̂(r)||ĥ(r)|`; the middle factor
  should be `|ĝ(−2r)|`.

Verified correct: the four-fold expansion collapsing to `Σ_a |f̂(a)|⁴`; the η-to-η² deduction;
the 3AP identity `Σ_c f̂(c)ĝ(−2c)ĥ(c)`; the two-parameter obstruction for 4APs; the skew-shift
induction `Tⁿ(z,w) = (z+nα, w+2nz+n²α)`; the third-difference identity with weights
(1,−3,3,−1); the eigenvalue `e(2α)`; the zero Kronecker projection; and the four-function
construction whose correlation is identically 1.
