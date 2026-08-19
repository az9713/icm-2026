# Verification — prismatic-homotopy-lurie
verdict: MINOR
uncited_external_claims: 7
unsupported_speaker_claims: 0
title_check: PASS — transcript opening announces "prismatics tabletop theory" by "Jacob Lurri from Institute for Advanced Study"; caption-mangled form of "Prismatic Stable Homotopy Theory", Jacob Lurie (IAS). Matches front matter.
gap_honesty: PASS — all 3 [Gap:] markers plus the 2 in-text "Reconstructed"/"flagged" notes sit exactly where the captions really are silent; no gap was silently filled.
self_report_audit: HONEST BUT INCOMPLETE — §11 under-reports 5 textbook-level imports it supplied itself (Lazard ring, HKR, Eilenberg–Steenrod axioms, "stable normal bundle", and its own quote-cleaning policy). No false claim in §11.
citations_verified_live: 3 of 3 real (arXiv:2507.13471, arXiv:2405.04329, youtube 1fSd7FxEA3w); a 4th (Bhatt MAT 549 PDF) resolves to a real file.

The 7 uncited external claims, all textbook-standard, none presented as the speaker's:
Eilenberg–Steenrod axioms + "1940s" (`:280`); formal-group-law axioms and the
Baker–Campbell–Hausdorff anchor (`:395`); "stable normal bundle" (`:443`); the Lazard ring
named (`:447`); the HKR theorem named (`:487`); "symmetric monoidal" for his "tensor category"
(`:984`); the height stratification of formal group laws (`:1187`).
This header list is final and supersedes the interim enumeration in the §§2–3 findings block
below: `:333` (Bott periodicity) was dropped because the transcript does state its content, and
`:283` was reclassified as a quote-presentation issue rather than an external claim.

Note: transcript is a single unbroken line (40,179 bytes, zero newlines). For reading I
folded it to 375 lines at width 110 in scratchpad. Line cites below use that folded copy
and are marked "tx:NNN" — they are NOT lines in the repo file.

Talk has NO proceedings paper and NO companion (verified by caller: nothing on
math.ias.edu/~lurie/). So every non-transcript claim needs an external citation or a
[Gap:] marker. Judged on that basis.

## Findings
Most-severe first. There is no MAJOR-class finding: no invented theorem, no wrong title, no
fabricated citation, no silently filled gap. What follows is the MINOR class.

### Sections 1–3 (framing + background scaffolding)

**No unsupported speaker claims found in §§1–3.** Every quote attributed to the podium is in
the transcript in caption-mangled form and the tutorial de-mangles it correctly. Spot checks:

- §1 "85-page paper… Adams and Atiyah reproved it in eight pages, main argument in a single
  paragraph… proof from the Book" — tx:26–32 has all four details verbatim, including Erdős.
- §1 "There are some invariants that I can compute without being able to define…" — tx:345, exact.
- §1 Hopf fibrations built "out of the real division algebras" — tx:24 "constructed using
  division algebras over the real numbers". The tutorial's expansion to "complex numbers,
  quaternions, octonions" is external but is textbook and harmless.
- §1 "So unfortunately, I didn't tell you what any of these things are… fit into a larger
  black box that I do not have a precise definition of" — tx:243–246, exact.
- §2.2 Clausen–Mathew–Morrow, "those three are the entire difference" — tx:79–84 supports this
  reading closely ("the entirety of the difference between K theory and topological
  cyclomology is explained by the three things").
- §3.2 Grothendieck priority, "they were imitating Grothendieck" — tx:43–45, exact.
- §3.7 "TC of R can be defined as just extensions from the unit object into THH of R" — tx:104.
- §3.7 Bökstedt THH(F_p) = polynomial on one degree-2 generator, "incarnation of Bott
  periodicity in an algebraic world" — tx:109–112, exact.
- §3.7 "one spectral sequence away from just understanding algebraic differential forms" — tx:120.
- §3.8 étale descent gloss — tx:74–76, exact.
- §3.6 "roughly as many cohomology theories in the world of topology as there are formal
  groups" — tx:352–354, exact (he says it late in the talk, not at §3.6's position; the
  tutorial has moved it forward, which it does not flag, but it does not misattribute it).

**Uncited external background in §§2–3 (the MINOR class).** These are not in the transcript and
carry no citation. All are standard textbook facts, none is presented as the speaker's:
1. `:280` Eilenberg–Steenrod axioms "in the 1940s", the dimension axiom, the named list.
2. `:333` "KU^n ≅ KU^{n+2}" as Bott's theorem — stated, explicitly not proved (tutorial says so).
3. `:395–412` formal group law axioms; Baker–Campbell–Hausdorff as the anchor.
4. `:443` MU built from "almost complex structure on the **stable normal bundle**" — the
   transcript says only "almost complex manifolds up to bordism compatible with their almost
   complex structures". The stable-normal-bundle refinement is the tutorial's own.
5. `:447` the Lazard ring named. Transcript says only "another ring… which classifies formal
   group laws" — the name Lazard is the tutorial's.
6. `:487` the **HKR theorem** named. Transcript states the content (HH of a smooth F_p-algebra
   = differential forms) but never the name or the attribution.
7. `:283` "long exact sequences, or excision, or Mayer–Vietoris" given inside quotation marks.
   The captions read "like long exact sequences for excision and meer via etc etc". The
   de-mangling is almost certainly right, but it is presented as a verbatim quote and is not.

**Two honest self-labels found, both correct and both to the tutorial's credit:**
- `:428` multiplicative formal group law F(x,y)=x+y+βxy explicitly marked "*Reconstructed from
  standard literature — the talk states the additive case only*". Confirmed: the transcript
  states only the additive rank-one rule (tx:325–328).
- `:381` and `:518` two facts attributed to the **March 2025 Simons recording, not the ICM**
  (Hℤ-modules = chain complexes; the Nikolaus–Scholze formulation of TC). Confirmed absent from
  the ICM transcript. The labelling is exactly what the brief asks for.

### Section 4 ("The talk, rebuilt") — the section that maps onto the transcript

**Zero unsupported speaker claims found.** I walked §4.1 to §4.10 against the transcript line by
line. Every attributed statement has a caption-level anchor:

| Tutorial claim | Transcript |
|---|---|
| Quillen 1970s, higher K-groups | tx:53–54 |
| three constituencies (Riemann–Roch / L-functions / surgery obstructions) | tx:55–60 |
| "K-theory of Z/4 still not completely known" | tx:61–62 |
| finite groups; odd part known since Quillen; the p-adic part is hard | tx:63–68 |
| three defects of TC; CMM makes them exhaustive | tx:70–84 |
| THH Künneth over THH(ground) | tx:130–134 |
| Atiyah–Hirzebruch spectral sequence "a good first approximation" | tx:150–156 |
| "around 2000", Levine and Friedlander–Suslin, smooth affine case, later generalized | tx:157–161 |
| Bhatt–Morrow–Scholze, syntomic → TC spectral sequence | tx:163–169 |
| Fontaine–Messing 1980s, rational coefficients; BMS integral, via topological methods | tx:169–174 |
| Bhatt–Scholze reinterpretation; "the part of prismatic cohomology where Frobenius acts by the identity" | tx:175–178 |
| F-gauges black-boxed with the same two survivals | tx:179–184 |
| "the point of having a formula like this is so that you can think about the Künneth formula" | tx:186–188 |
| the chart, all six rows | tx:196–205 |
| "extend this chart to the right as far as we wanted" | tx:205–208 |
| conjecture demands (a)–(g) including S_prism, S_prism^X, Künneth, KU_prism/Hz_prism, module categories | tx:222–248 |
| minimal vs maximal; "SH_prism : SH :: F-gauges : chain complexes" | tx:249–258 |
| dimension-axiom answer raised then discarded | tx:259–264 |
| MU_prism from Grassmannians; "let me not get into details" | tx:300–306 |
| the acceptance test, "the test that you have to pass to prove the conjecture" | tx:309–314 |
| Hopkins–Morel precedent, char ≠ p, and the "then it's a construction" conditional | tx:318–325 |
| Cartan–Serre Steenrod algebra; "basic building blocks" | tx:329–338 |
| Carmeli–Feng, Tate's Brauer-group conjecture, "trickiest cases", "proof of concept" | tx:338–348 |
| relative SH_prism(R); "provisional… conditional definition"; p^n-th roots of unity; Z/p; Carmeli–Feng | tx:358–375 |

**Citations checked live — all three are real and quoted accurately.**
1. `:572` **arXiv:2405.04329** — confirmed: Antieau, Krause, Nikolaus, "On the K-theory of
   Z/p^n", submitted 7 May 2024. The tutorial's paraphrase (prismatic description of K-groups of
   O_K/I plus a computation algorithm) matches the abstract. NOT a fabricated citation.
2. `:889` **arXiv:2507.13471** — confirmed: Shachar Carmeli, Tony Feng, "Prismatic Steenrod
   operations and arithmetic duality on Brauer groups", submitted 17 July 2025. I compared the
   tutorial's three quoted abstract fragments against the live abstract: **verbatim correct**,
   including "the last open cases of a 1966 Conjecture of Tate" and "generalizing the prismatic
   F-gauges of Drinfeld and Bhatt--Lurie". NOT fabricated.
3. `:79` **youtube.com/watch?v=1fSd7FxEA3w** — confirmed: "Jacob Lurie: Prismatic Stable
   Homotopy Theory (March 14, 2025)". Real, same speaker, same title, correct date. The
   tutorial's "seventeen months earlier" is arithmetically right (Mar 2025 → Aug 2026).

**The Z/4 attribution trap: handled correctly.** The transcript says only "we now know how big
they are" and names nobody (tx:64–66). The tutorial supplies Antieau–Krause–Nikolaus but wraps
it in an explicit bracket, "*Attribution restored, and the talk does not name the authors*"
(`:570`), with the arXiv id. This is exactly the required behaviour.

**Three gap markers, all placed where the transcript really is silent:**
- `:614` the Tor correction in the K-theory Künneth. tx:126 has literally "there's some slight
  correction" and nothing more. Correctly marked, impact honestly rated low.
- `:830` the MU_prism construction. tx:302 "let me not getting into details". Correctly marked.
- `:963` the relative construction. tx:371–373 gives only "there's a definition that you can
  write down that has all of the expected properties". Correctly marked.

**One additional silence the tutorial marks as a gap and rates "moderate", correctly**: `:701`,
the explicit syntomic Künneth formula. tx:190–193 confirms he says "There is a formula written
here" and the captions carry no formula. Not silently filled.

**Two quotes correctly labelled as coming from the March 2025 recording, not the ICM**: the
Hoyois extension of Hopkins–Morel (`:857`) and the "I took the important structural theorem"
sentence (`:880`). I grepped the ICM transcript: it contains "really control" but NOT "important
structural theorem" — so the label is accurate, not decorative.

### Sections 5–10

**§5 "The one conjecture, stated precisely".** This was the section most at risk — the speaker
calls his own conjecture "vague" (tx:205) and any tightening is the tutorial's work. It holds up.
Clauses 1–5 each trace to a spoken demand (tx:222–248 and tx:249–258), and clause 5's
factorization S_prism -> MU_prism -> Hz_prism is exactly tx:316–320 ("in the classical world you
can factor that map in two steps... we're demanding that you get the prismatic Eilenberg–MacLane
spectrum by a completely analogous procedure"). §4.5 also carries the honest header "Conjecture
(**vague form**)". The Status table's five rows are each transcript-backed or citation-backed.
**One unflagged strengthening:** `:984` says "symmetric monoidal, triangulated". The transcript
says only "tensor category" and "triangulated category". Symmetric monoidal is almost certainly
what is meant, but it is the tutorial's word, not his, and it is not marked. Low impact.

**§6** is interpretation of the §4.3 chart; no new external claims.

**§7 exercises.** Both are explicitly the tutorial's own — `:1122` "The swindle is standard and is
not in either recording; the exercise is mine"; `:1191` "this exercise is mine end to end... the
talk states that MU carries the universal formal group law and gives the additive law for
ordinary cohomology; it never writes down the multiplicative law, the logarithm, or the
denominators." I confirm: the transcript has zero hits for "Lazard", "height", "HKR". The
mathematics in the solutions that I can check by hand is correct — 1+bF_m(x,y)=(1+bx)(1+by)
holds, and log_{F_m}(x) = (1/b)ln(1+bx) = sum (-1)^{n-1} b^{n-1} x^n / n is the correct
term-by-term integration of 1/(1+bt). **One uncited external claim inside the solution** at
`:1187`: the height stratification of formal group laws (additive at height infinity,
multiplicative at height 1). Standard, uncited, and only loosely covered by that section's
blanket "entirely mine".

**§9 reading list — three entries, all checked:**
- Entry 1, the March 2025 recording: URL resolves, correct title/speaker/date. But entry 1 also
  makes detailed content claims (the Drinfeld/Bhatt syntomic stack Z_p^syn, the specific loci
  giving de Rham / crystalline / Hodge–Tate / prismatic / q-de Rham, and TP / TC-minus / THH /
  periodic HH for KU_prism). **I cannot check any of these** — §11 states that the 2025
  transcript was cleaned "into my scratchpad, not into `transcripts/`", so the cross-check source
  is not in the repo. See "What I could not check".
- Entry 2, Bhatt, *Prismatic F-gauges*, MAT 549 Fall 2022:
  `math.ias.edu/~bhatt/teaching/mat549f22/lectures.pdf` — the URL resolves to a real 1.2 MB PDF.
  I could not extract its title text (compressed streams) and my web-search budget was exhausted,
  so the title is unconfirmed; the path `mat549f22` is consistent with the claim. Not fabricated.
- Entry 3 and the trailing AKN pointer: both verified above.

**§10 self-test** restates §§3–5 content; no new external claims beyond the Eilenberg–Steenrod
package already logged.

## Self-report audit

**Verdict on §11: substantially HONEST, and unusually detailed — but not COMPLETE. It
under-reports in five specific places, all in the same direction: standard-textbook names and
facts supplied by the writing agent are filed in the name-correction table, or nowhere, rather
than in the "Reconstructed" list where they belong.**

What §11 gets right, and which I confirmed independently rather than taking on trust:
- Every one of its five listed gaps is in a place the transcript really is silent (checked above).
- Its claim that the ICM talk never says "infinity-category" / "higher category" / "homotopy" in
  that sense — I grepped the transcript; correct.
- Its two "substantive corrections beyond spelling" (the unattributed Z/4 computation; the
  Carmeli–Feng "trickiest cases" vs "last open cases" discrepancy) are both real, and both are
  also flagged inline in the body, not only here.
- Its six "Reconstructed" items are each genuinely reconstructed and each carries a verification
  route.
- Its "Could not verify" list is honest: the pre-2000 field case really is unnamed at tx:159–160,
  and the writer really did decline to guess a name.
- Its three cited sources all check out live (see the Section 4 block above). No fabrication.

**Under-reported — five items.**

1. **The name-correction table is doing double duty and hides one import.** `lzard ring -> Lazard
   ring` is filed under "From the **March 2025 recording only**, listed separately because none of
   it is in the ICM talk **and I have used almost none of it in the body**". But §3.6 `:447` uses
   "the Lazard ring" in the body, unlabelled, as though it were the ICM talk's word. The ICM
   transcript has zero hits for Lazard; it says only "another ring... which classifies formal
   group laws". The fact is correct and standard; the disclosure placement is wrong, and it is the
   one case where §11's own "almost none of it in the body" is not true.
2. **The HKR theorem is named at `:487` and appears nowhere in §11.** Zero transcript hits for
   "HKR". The talk states the content, never the name or the attribution
   (Hochschild–Kostant–Rosenberg). It belonged in the "Reconstructed" list.
3. **Eilenberg–Steenrod and the dimension axiom (§3.1, reused in §10) appear nowhere in §11.**
   The transcript's five "Steenrod" hits are all the Steenrod *algebra*, late in the talk. The
   named axiom list and the date "in the 1940s" are the writer's, correctly, but undisclosed.
4. **`:443` "almost complex structure on the stable normal bundle".** The transcript says only
   "almost complex manifolds up to bordism compatible with their almost complex structures". The
   stable-normal-bundle refinement is the writer's and is not disclosed.
5. **The quote-cleaning policy is never stated.** §11's table covers word-level caption repairs,
   but the body silently repairs text *inside quotation marks*. Clearest case, `:283`: the
   tutorial prints as a quotation "like long exact sequences, or excision, or Mayer–Vietoris";
   the captions read "like long exact sequences for excision and meer via etc etc". Filler removal
   and de-mangling are almost certainly faithful to what was said, but a reader who trusts
   quotation marks is never told this is happening.

**One further transparency issue that §11 names but does not treat as a cost:** it discloses that
the March 2025 transcript "was cleaned into my scratchpad, not into `transcripts/`". Since the
tutorial leans on that recording at seven labelled points plus the §9 entry-1 content claims,
that decision makes roughly a tenth of the tutorial permanently unverifiable from the repo. The
labelling is exemplary; the source is gone.

**Nothing in §11 is a false claim.** I found no case where §11 asserts something the transcript
contradicts, no gap it claims to have marked that it did not mark, and no citation it claims to
have verified that failed my check. The under-reporting is omission of textbook-level imports,
not concealment of invention.

## Why this is not thin, despite having no companion

The caller flagged this as the file most likely to be thin. It is not. The reason is in the
transcript itself and the tutorial identifies it correctly at `:84`: **this is a talk of spoken
formulas.** Lurie states TC(R) = Ext(unit, THH(R)), THH(F_p) = polynomial on one degree-2
generator, the THH Kunneth formula, the motive Kunneth formula, MU^*(pt) = polynomial on one
generator in each even degree, and "mod out MU by those generators and you get Hz" — all out
loud, all caught by the captions. What died on the slides is only the indexing (degrees, weights,
Tate twists, spectral-sequence pages) plus one displayed formula, and the tutorial marks that
loss precisely rather than papering over it. The section that carries the conjecture (§4, §5) is
the *best*-sourced part of the file, not the worst. The uncited material is concentrated in §3
and §7 — the background scaffolding and the exercises — which is the right place for it.

## What I could not check

- Whether the mathematics is true. Out of scope per the brief.
- **Everything drawn from the March 2025 recording** — seven labelled points plus the §9 entry-1
  content list. The video is real and correctly titled, but its transcript is not in the repo and
  I did not fetch its captions. To settle: save that transcript into `transcripts/` and re-run.
- The title of the Bhatt MAT 549 PDF. The file exists at the stated URL; text extraction failed
  on the compressed streams and my web-search budget was exhausted.
- Whether the ICM programme lists this talk under exactly this title. The reconstruction from the
  announcer's mangled words plus the March 2025 title is sound but is not the programme itself.
- Whether "he returns to Kunneth five separate times" (`:151`) is exactly five. The captions carry
  11 mangled Kunneth tokens across roughly six to eight distinct discussion points; "five" is a
  defensible count of occasions and if anything undercounts. Not a problem.
- Whether "Lurie has posted nothing to arXiv since January 2022" (`:57`) is current. The caller
  verified math.ias.edu/~lurie independently; I did not re-check the arXiv listing.
