# Verification — learning-in-games-tardos
verdict: MINOR
uncited_external_claims: 10 (findings 2, 3, 4 = 3; finding 5 = 4; finding 6 = 3. Of these, 4 matter: :311, :262, :524, :741.)
unsupported_speaker_claims: 1
title_check: PASS — the tutorial's own title is disclosed as the writing agent's invention; "carryover effect" is spoken verbatim in the transcript and the subject matches.
gap_honesty: PASS — no inline `[Gap:]` markers, but §10 carries an explicit "Gaps, with impact ratings" list (4 items) plus a "Reconstructed" list (3 items). Different convention, not a missing one.

## Method

Transcript `transcripts/u-ssCmb8YBo_transcript.txt` is a single unwrapped line, 42,870
bytes (~440 lines wrapped at 100 cols). I read all of it, and all 1,444 lines of the
tutorial. I re-derived every piece of arithmetic in the tutorial that the transcript does
not carry, and I fetched all three arXiv abstracts.

**The specific hunt — filled-in mathematics with no citation — came up largely empty.**
Every formula in the tutorial falls into one of four buckets: (a) spoken in the transcript;
(b) arithmetic I re-derived and confirmed self-consistent; (c) attributed to a named paper
and theorem/lemma number; (d) standard textbook material. I found no theorem statement or
constant that is both absent from the transcript and unattributed *and* load-bearing.

**Citation-fabrication gate: PASSED.** All three arXiv ids resolve with exactly the titles
and author lists the tutorial gives:
- 2003.07009 — Gaitonde & Tardos, *Stability and Learning in Strategic Queuing Systems*. ✔
- 2011.10205 — Gaitonde & Tardos, *Virtues of Patience in Strategic Queuing Systems*. ✔
  Abstract contains `\frac{e}{e-1}\approx 1.58` verbatim, as §10 claims.
- 2502.08898 — Abel, Kolumbus, Martin Duque, Palma Foster & Tardos, *Learning in Strategic
  Queuing Systems with Small Buffers*. ✔ Author list matches exactly.

The 2502.08898 abstract also independently corroborates two things: the JACM 2023 journal
version exists ("EC 2020 and JACM 2023"), and the qualitative content of §4.11 ("ensuring
that the system is stable requires the use of timestamps and priority for older packets").

## Findings

### 1. §4.11 / §5 / §7.5 — a theorem that is not in the lecture is presented as lecture content
`summaries/learning-in-games-tardos.md:694`, `:952`, `:1145`, `:1273`

Claims: "Gaitonde–Tardos Theorem 2.2: in the alternative model without timestamps, for large
enough n there is a centrally feasible system of n queues and n servers that stays feasible
even when λ is scaled up by Ω(n^{1/3}) ... and the system is still unstable."

The transcript contains nothing of the kind. Tardos says only that timestamps make the
internet "infinitely more efficient" (one sentence, model point 6). She never states, hints
at, or numbers a theorem about removing age priority. Yet §4.11 sits inside "§4. The talk,
rebuilt", and §7.5 opens "§4.11 is the most underrated fact **in the lecture**".

It *is* attributed to a paper and theorem number, and the small-buffers abstract corroborates
the direction qualitatively. So this is a framing problem, not a fabrication. Severity:
moderate — it is the sole support for §7.5, one of six "what is useful to you" items.

What would settle it: read Theorem 2.2 of arXiv:2003.07009 and confirm the Ω(n^{1/3}) exponent.

### 2. §3.4 — a hard constant with no citation on the line
`summaries/learning-in-games-tardos.md:311`

"atomic selfish routing with affine cost functions is (5/3, 1/3)-smooth, giving
PoA ≤ (5/3)/(1 − 1/3) = 5/2."

Not spoken (she declines to give any constant from that literature). The algebra checks:
(5/3)/(2/3) = 5/2. The result is real and standard (Christodoulou–Koutsoupias 2005;
Awerbuch–Azar–Epstein 2005; the smoothness parameters are Roughgarden's). No citation at the
line; §10:1418 discloses that the constant was supplied, but names no source for it.

### 3. §3.5 vs §4.10 — "strongly stable" is stated more strongly than the theorem it rests on
`summaries/learning-in-games-tardos.md:320`, `:595`, `:926` vs `:619`

§3.5 and §5 both assert stability means "for every fixed r ≥ 0 there is C_r ... E[Q^r] ≤ C_r",
and §3.5 says "That is the conclusion Pemantle–Rosenthal delivers". But the tutorial's own
statement of Pemantle–Rosenthal at :619 gives moments only "for every 0 < r < p − 1". The
transcript says merely "guaranteed to stay bounded in expectation", and the arXiv:2003.07009
abstract likewise says only "the expected number of packets ... will remain bounded".

Internal inconsistency plus a strengthening over both the podium and the abstract. Cannot
determine whether the paper body proves all-moments; that would settle it.

### 4. §4.10 — the moment condition silently contradicts the speaker
`summaries/learning-in-games-tardos.md:616`

Tutorial: "There is p > 2 and θ > 0 with E[|X_{t+1} − X_t|^p | ℱ_t] ≤ θ."
Transcript: "one property is that it's sufficiently regular — concretely I think the second
moment is bounded is good enough."

p > 2 is strictly stronger than "second moment". The published Pemantle–Rosenthal condition
does require p > 2, so the tutorial is almost certainly right and Tardos was loose from the
podium. But this is a correction *of the speaker*, and §10's name-correction table and gap
list do not mention it. Also note the citation here is "Pemantle and Rosenthal (1999)" —
author + year, no title or journal.

### 5. Four bare or missing citations
- `:262` — "the bandit-feedback version EXP3.P is what the queuing papers actually invoke."
  Not spoken; no id. The named algorithms Hedge/multiplicative-weights/EXP3.P are all absent
  from the transcript (she says only "watch the past, randomise, weight what did well").
- `:524` — "Balseiro & Gur; Fikioris & Tardos" for the budgeted-auctions literature. Surnames
  only; no title, year, or id. Not spoken.
- `:741` — "the elegant linear-programming-duality characterisation of the no-buffer case
  (Fu et al. 2022)". Author + year only. Not spoken.
- `:739` — "The paper's Lemma 1 gives the counterexample: one queue and two servers each with
  μ = 1/2 needs λ < 23/24 < 1 even with full coordination." 23/24 is a precise constant the
  transcript does not carry (she says "I have an example I'm going to skip here"). Cited by
  lemma number only; unverifiable without the PDF.

### 6. Lower-severity uncited-but-textbook
`:210` Nash's existence theorem; `:445` Brown (1951) / Julia Robinson (1951) dates;
`:426–428` PPAD-completeness, ICM 2018 Rio, and the Rolf Nevanlinna Prize → IMU Abacus Medal
renaming. All standard public record; none spoken with those specifics. Listed for
completeness, not as a concern.

### 7. Arithmetic I re-derived and confirmed correct (no finding)
- §4.1 / §6.1 Braess: 50/100+1 = 1.5, deviator 1.02, all-tunnel 2, PoA 4/3. Every input
  number is spoken; the 4/3 itself is not spoken but is cited inline (Roughgarden & Tardos,
  JACM 2002) at both :377 and :986. Correct handling.
- §4.12(a): 1 − (3/4)³ = 37/64 ≈ 0.578 > 1/2. ✔ Labelled "Reconstructed arithmetic, my own".
- §4.13 / §6.2: Σ_{i≥1} (1/k)(1−1/k)^{i−1}(1 − (1−1/n)^i) = 1 − (n−1)/(n+k−1) = k/(n+k−1).
  I evaluated the geometric series independently and it is exactly right. The threshold
  k > n−1 and the resulting capacity k/n ≈ 1 = 2λ follow. ✔
- §6.2(e): round robin 1 − (1−1/n)^n → 1 − 1/e ≈ 0.632 vs n/(2n−1) → 1/2. ✔

Note on §4.13: the transcript's own arithmetic is muddled — "n servers with service rate one
in n ... the total service rate is a factor of two and the arrival rate is a half" (n × 1/n = 1,
which is 2 × 0.5). The tutorial silently generalises to a two-parameter (k, n) family and
cleans the arithmetic up. That is a real reconstruction and §10 does not list it.

## Self-report audit

**Overall: honest, unusually thorough, and it under-reports four things.**

What §10 gets right, and these are not small:
- It discloses at line 40, in bold, that the title is the writing agent's own, and explains
  the ICM-1990-Kyoto confusion at length. This is the opposite of the failure the brief's
  check exists for.
- **It discloses the one genuine substantive correction to the mathematics.** §10:1379–1384
  states that the captions render the constant as "E minus one over E" = (e−1)/e ≈ 0.63,
  observes that a capacity *increase* cannot be below 1, and gives the published value
  e/(e−1) ≈ 1.58. I verified this against the arXiv:2011.10205 abstract, which contains
  `\frac{e}{e-1}\approx 1.58` verbatim. The correction is right and the disclosure is exact.
  This was the single most likely place for a silent fill-in and the agent flagged it itself.
- The "Reconstructed" list (Braess figure, §4.12(a) arithmetic, §6.2(e) k=n case) matches
  what I independently identified as reconstruction.
- The "Not verified, and omitted rather than guessed" paragraph (:1386–1391) is a genuine
  restraint note: it leaves the chair "Yuri" unidentified and attributes the ICM 2006
  Roughgarden claim to her rather than asserting it.
- It records a *negative* result honestly (:1428–1434): the predicted Wright overlap
  evaporated and it says so rather than manufacturing links.

What it under-reports:
1. **The §4.11 / Theorem 2.2 material is not flagged as absent from the talk.** §10 has no
   entry saying "this section is entirely from the paper, she never said it". Given §7.5
   calls it "the most underrated fact in the lecture", this is the meaningful omission.
2. **The p > 2 vs "second moment" correction is not listed.** §10:1422–1425 asserts the
   Pemantle–Rosenthal statement was "recovered verbatim from the primary papers", which
   quietly covers it, but it is a correction of the speaker and belongs in the corrections
   table alongside the e/(e−1) entry.
3. **The strong-stability strengthening is not listed**, and it is inconsistent with the
   tutorial's own theorem statement (finding 3).
4. **The (k, n) generalisation and cleaned-up arithmetic of the §4.13 lower bound is not in
   the "Reconstructed" list**, even though §10 does list the two smaller reconstructions
   around it. §10:1424 puts "the lower bound" in the "recovered verbatim" bucket instead.

Minor: the EXP3.P/Hedge naming (:262) and the bare "Balseiro & Gur; Fikioris & Tardos" and
"Fu et al. 2022" citations are not mentioned anywhere in §10.

**Answer to the question that sent me:** the talk was genuinely clean. It is narrative-heavy
and formula-light — Tardos states almost every number she uses out loud (100 cars, x/100,
1.5, 2, factor 2, factor 3, 0.47, 50/50, 1/2 arrival, 1/n servers, three servers at 1/4), and
the one constant the captions garbled is the one §10 explicitly corrects. The writing agent
did not silently fill gaps with invented mathematics. What it did instead is import a
substantial amount of *published* material (theorem numbers, the dual-process potential
Φ = Σ λ_i T^i(T^i − 1), the √Φ sampling, Lemma numbers, 23/24, Ω(n^{1/3})) and weave it into
the "talk, rebuilt" narrative without always marking the seam. That is a provenance-labelling
weakness, not fabrication.

## What I could not check
- Whether the mathematics is **true**. Out of scope per the brief; I have no papers.
- **Every theorem/lemma number** cited to the papers: Gaitonde–Tardos Theorems 2.1, 2.2, 3.1,
  3.3, Assumption 3.1, Lemma 3.1; Abel et al. Theorem 1, Theorem 3, Lemmas 1, 2, 3. I
  verified the papers exist with the stated titles and authors; I did not open the PDFs. Any
  of these numbers could be wrong. Fetching the three PDFs would settle all of it at once.
- The **Ω(n^{1/3})** exponent (§4.11), the **23/24** constant (§4.12b), the potential
  **Φ = Σ_i λ_i T^i(T^i − 1)** and the **√Φ** sampling (§4.10, §5), and the buffered
  potential **Φ = Σ_i (N_i − (½λ_i + 2δ)T)^+** (§4.12c). All are internal to the papers.
- **JACM 2023, doi:10.1145/3587250.** The tutorial says the ACM page returned 403; I did not
  retry. The arXiv:2502.08898 abstract does reference "Gaitonde and Tardos (EC 2020 and JACM
  2023)", which is independent corroboration that the journal version exists.
- **Name-correction ground truth** (Gödel Prize 2012, IEEE von Neumann Medal 2019, Nevanlinna
  → Abacus). Out of scope per the brief; I checked that each is *disclosed* in §10:1365–1379,
  not that each is *accurate*. Cannot determine on accuracy.
- Whether **anything on the slides** contradicts the reconstruction. The video was not viewed.
- Two cross-links asserted at :79–84 (`optimization-theory-practice-wright.md`,
  `shape-of-math-kontorovich.md`) — I did not open those files.

---

# Round 2 — companion formula check, 2026-08-18

Round 1 was a transcript-and-citation-list check. This round fetched the companion —
Gaitonde and Tardos, *Stability and Learning in Strategic Queuing Systems*, `arXiv:2003.07009`
(EC 2020), via ar5iv — and compared every statement the tutorial attributes to it, by theorem
number.

**Result: every companion-attributed statement is correct, theorem numbers included.** No
change to the verdict.

## Checked against `arXiv:2003.07009`

| Tutorial | Companion | Verdict |
|---|---|---|
| `:566-570` **Theorem 2.1**: centrally schedulable iff `Σ_{i≤k} μ_i > Σ_{i≤k} λ_i` for every k | Theorem 2.1, same inequality, strict | **correct** |
| `:571-573` the preprocessing caveat — "delete a maximal equal prefix of 1's from both vectors first" | Theorem 2.1's own opening clause, "preprocessed so that a maximal, equal prefix of 1's is deleted from both" | **correct**, and the tutorial is the only place this caveat is recorded at all |
| `:588-594` **Assumption 3.1**: `½(1−η) Σ_{i≤k} μ_i ≥ Σ_{i≤k} λ_i` for all k | Assumption 3.1 (Feasibility), identical | **correct**, including the direction of the inequality and the non-strictness |
| `:588` **Theorem 3.1**: no-regret on long windows with high probability implies strong stability | Theorem 3.1 | **correct** |
| `:694-698` **Theorem 2.2**: without timestamps, for large enough n a centrally feasible system stays feasible with λ scaled up by **Ω(n^{1/3})**, all queues can be at Nash equilibrium every step, and the system is still unstable | Theorem 2.2, verbatim including the exponent | **correct** |
| `:698` "no sub-polynomial capacity factor suffices at all" | "this shows that in this model, **no sub-polynomial factor is possible in general**" | **correct**, near-verbatim |
| `:1264` **Theorem 3.3** shows the result fails at **½ + o(1)** | Theorem 3.3, "satisfying Assumption 3.1 with ½ + o_n(1) in place of ½ … the system is not strongly stable" | **correct** |
| `:916-926` strong stability as `E[(Σ_i Q^i_t)^r] ≤ C_r` for every r ≥ 0, C_r independent of t | Definition 2.1, with `Q_t := Σ_{i=1}^n Q^i_t` | **correct** |
| `:920-923` the model: one packet per queue per step, one packet per server per step, **oldest timestamp** served, unserved packets returned, bandit feedback | §2 model, points 1-4 | **correct** in every clause |

## One simplification the tutorial makes silently, and it is legitimate

The companion's Theorem 3.1 begins "Suppose that Assumption 3.1 holds for the **dual** queuing
system". The tutorial's §4.9 and §5 drop the word *dual* and state the hypothesis directly
about the system.

That is safe, and the companion says why: the dual system tracks the **age of each queue's
oldest packet** rather than its length, the two are explicitly coupled, and "strong stability
in the standard system is **equivalent** to strong stability in the dual system." The tutorial
even explains the age-tracking device on its own at `:632` ("Gaitonde–Tardos track only the age
T^i_t of the oldest packet in each queue"). So the object is present; only the word is dropped.
Recording it because a reader comparing the tutorial's Theorem 3.1 with the paper's will find
the statements textually different.

## What this round confirms about the round-1 finding

Round 1 flagged that the Gaitonde–Tardos result called "the most underrated fact in the
lecture" (`:694`, `:952`, `:1145`) **is not in the lecture**, though it is correctly attributed
to the paper. This round confirms the second half exactly: it is Theorem 2.2 of
`arXiv:2003.07009`, and the tutorial states it correctly, exponent and all. The defect is
placement, not content — the fix is one word, not a rewrite.

## What this round did not check

- `arXiv:2011.10205` (Gaitonde–Tardos, *Virtues of Patience*, EC 2021), the source of the
  **e/(e−1)** result at `:864` and `:1316`. Not fetched.
- `arXiv:2502.08898`, cited inline.
- The Pemantle–Rosenthal moment bound. It is named in the companion at the point the tutorial
  says it is (immediately after Theorem 3.1, "The technical tool we use to establish the
  stability of our system in Theorem 3.1 is the following result of Pemantle and Rosenthal"),
  so the *placement* is verified; the statement itself is not.
- The drift argument's Case A / Case B split, which is the tutorial's own exposition of the
  proof rather than a quotation.
