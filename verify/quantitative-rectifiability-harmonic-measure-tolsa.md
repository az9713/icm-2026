# Verification — quantitative-rectifiability-harmonic-measure-tolsa
verdict: MINOR
uncited_external_claims: 5 (author-only attributions, all sourced to the verified survey; no fabricated citation found)
unsupported_speaker_claims: 0
title_check: PASS — transcript intro says verbatim "the title of today's talk is quantitative rectifiability and harmonic measure"; speaker "Shabiel/Shavier Tulsa" = Xavier Tolsa, "research professor at the Catalan Institution for Research and Advanced Studies" (= ICREA), "universaton de Barcelona and CRM". Front matter matches on every field.
gap_honesty: PASS (one caveat) — 4 gaps + 1 correction are marked and accurately rated, but written as [Gap, <impact>: ...] instead of the TEMPLATE form [Gap: ...]; one small unmarked fill at 6 Step 3.

## Working notes (in progress)

### Source situation — this is the key structural fact
Front matter claims arXiv:2607.16457 as a proceedings paper. VERIFIED by fetching
https://arxiv.org/abs/2607.16457 : title "Interactions between quantitative rectifiability,
singular integrals, and boundary value problems for harmonic functions", author Xavier Tolsa,
[v1] 17 July 2026, [v2] 21 July 2026, comment field verbatim "Survey paper for the ICM 2026
plenary lecture of the author". The tutorial's §preamble claim about the paper is exact,
including both dates and the verbatim comment string.

This explains the anomaly flagged in my brief (110 KB, only 2 arXiv citation instances,
ZERO `[Gap: ...]` markers). The tutorial does not need per-claim arXiv ids because it
declares ONE governing source and uses it throughout. Whether that is honest is the
question §11 audit below answers.

### Timestamp check (cross-file)
`grep -n "[0-9][0-9]:[0-9][0-9]"` over the whole 1951-line tutorial returns ZERO hits.
No timestamp ranges in any section heading. CLEAN on this check.

### Transcript ground truth (single-line file, 38797 chars, no timestamps)
Named results the speaker actually states, in order:
Kakutani 1944 (Brownian exit) / F.&M. Riesz brothers 1916 / Dahlberg 1977 (Lipschitz) /
David–Semmes β₂ + UR characterization, 1990s, "inspired in part by previous results of
Peter Jones" / Azzam–Tolsa 2015 ("Jonasa Sam and myself in 2015") / earlier work of
Schul ("Shul"), Naber ("neighbor") / Nazarov–Tolsa–Volberg 2014
("near of myself and Borick") / Coifman–McIntosh–Meyer ("Cadron Kman Mintosh and meer") /
David–Semmes problem "early '90s" / planar n=1 case by "matila and vertera" using
curvature of measures / Dąbrowski–Tolsa ("a former student Danielski") general measures /
Painlevé problem "from the 1900 more or less" / Vitushkin conjecture proved by David /
"Navidan Matila in 2000" (plane) / AHM3TV-type one-phase theorem "Hman Martu myself and
Bber", solving a question of Chris Bishop 1990 / two-phase theorem "Jonas Moru and Borber",
Bishop planar 1991, Bishop conjecture 1992, blowup inspired by "kenik presenter",
Alt–Caffarelli–Friedman monotonicity formula, rectifiability criterion "due to a student of
myself and me" / frozen-snowflake example / Dahlberg, Verchota, Dahlberg–Kenig 1980s, L² on
Lipschitz / Kenig's question "early '9s".

### RESOLUTION of the "zero [Gap:] markers" anomaly — it is a FALSE ALARM
The tutorial DOES mark gaps. It uses the syntax `[Gap, <severity> impact: ...]`, not the
literal `[Gap: ...]` the survey grep looked for. FOUR markers exist:
- line 747 `[Gap, moderate impact:` — the |∇_x G(x,y₀)| ≲ ω(B(x,r))/r^{d−1} estimate,
  correctly identified as "the single most load-bearing unproved step in the talk";
  transcript confirms the speaker waves at it ("by a standard estimates from harmonic
  measure it turns out that this gradient of the green function can be estimated by this
  density ratio of harmonic measure").
- line 754 `[Gap, low impact:` — the informal ε truncation. Transcript confirms verbatim:
  "I am of course I am cheating a little because I am I have introduced for free this
  epsilon".
- line 1017 [Gap, low impact: — the frozen-snowflake construction (speaker: "if you dont remember the precise construction, dont worry").
- line 1107 [Gap in the talk, structural — but low net impact...] — the talk poses Kenigs question and stops. NOTE: this fourth marker has no colon in its opening clause, so a grep for the literal "[Gap:" or "[Gap...:" misses it too.
Plus explicit non-gap honesty devices: "*Reconstructed reasoning, not stated by either
source:*" (line 634, with "I have not done that; I flag the reasoning as mine"), and
"paper-only" / "paper-not-podium" labels for every survey-sourced block.
So the combination the brief flagged (long file + structural language + no gaps) is NOT
gap-filling-without-marking. It is a marker-syntax mismatch against the TEMPLATE spec.

### Cross-reference drift — real, small, several
Internal section pointers do not resolve. Confirmed:
- line ~370 (§3.3) "We will use it again for removability in §5.10" — removability is §5.9
  (line 896); §5.10 is the one-phase problem.
- line ~229 (§2.4) "we differentiate it in §5.7" — the Green-function differentiation is
  §5.6 (line 699); §5.7 is NToV.
- line ~424 (§3.5) "We come to that in §5.8" — plausible target is §5.3 or §5.8; ambiguous.
- line ~648 (§5.4) "the Dąbrowski–Tolsa theorem of §5.9" — Dąbrowski–Tolsa is §5.8 (line 845).
- line ~648 (§5.4) and §4 map both cite "§5.15" and "Coda (§5.14–5.15)". There is no §5.15.
  Highest numbered subsection is §5.14 (line 1212).
These are MINOR (navigation, not mathematics), but they are systematic: the numbering
appears to have shifted by one after drafting and the back-references were not updated.

### Ground truth obtained from the survey (ar5iv HTML of 2607.16457)
Theorem numbering and attributions from the paper match the tutorial where checked:
Thm 3.2 David–Semmes (n-AD-regular, 1≤p<2n/(n−2), Carleson β²); Thm 3.3 non-AD-regular
pointwise β₂ characterization (direct implication [105] = Tolsa, converse Azzam–Tolsa [14]);
Thm 4.2 David–Semmes problem solved for n=1 (Mattila–Melnikov–Verdera 1996) and n=d−1
(Nazarov–Tolsa–Volberg); Question 4.4 the 1<n<d−1 case OPEN; Thm 4.7 Dąbrowski–Tolsa;
Thm 5.2 Painlevé for Lipschitz harmonic functions (Tolsa–Volberg; d=2 David–Mattila;
holomorphic David); Thm 6.1 Dahlberg; Thm 6.3 one-phase AHM3TV [7]; Thm 6.4 two-phase
Azzam–Mourgoglou–Tolsa–Volberg [12], d=2 Bishop [18]; Thm 3.8 Alt–Caffarelli–Friedman.
The paper also confirms the tutorial's sharp p-claim: "on the theorem above one cannot
replace the coefficients β₂,E^n by β_{p,E}^n for any p≠2".
The tutorial's §3.6 attribution of that to "Tolsa, *Publ. Mat.* 63 (2019)" is consistent
with the paper's citation [106]; I could not open reference [106] to confirm the exact
volume/year. Marked as UNVERIFIED-BUT-PLAUSIBLE, not fabricated.

## Findings

**F1 — MINOR. One silently filled step in the centrepiece argument.**
`summaries/quantitative-rectifiability-harmonic-measure-tolsa.md:1308` (§6 Step 3).
Claims the passage from "R_*w finite a.e." to "L2(mu) bounded on a subset" is done "by
Chebyshev" plus "a T1/good-lambda argument". The transcript says only "using this fact and
some uh tools from harmonic analysis", and the survey does not spell it out either.
Chebyshev is obvious; naming **T1 / good-lambda** is a specific mechanism supplied from
outside both sources and NOT marked as a reconstruction — unlike the §5.4 density-theorem
reasoning, which IS marked. This is the single genuine gap-fill I found in 1951 lines.
*What would settle it:* the survey's proof sketch of Theorem 6.3, or the GAFA 2016 paper.

**F2 — MINOR. Gap markers use non-spec syntax, which is why the audit grep read zero.**
Lines 747, 754, 1017, 1107 carry [Gap, moderate impact: ...] / [Gap, low impact: ...] / [Gap in the talk, structural ...] (this last with no colon at all), and
line 1063 carries `[Correction, moderate impact: ...]`. `TEMPLATE.md:212` specifies the
literal form `[Gap: ...]`; `TEMPLATE.md:231` separately asks for an impact rating in the
process note. The writer merged the two into the marker. The content is compliant and the
ratings are accurate; the string is not. This fully explains the "110 KB, zero gaps"
signal in the audit.

**F3 — MINOR. Systematic off-by-one cross-reference drift; two targets do not exist.**
- §3.3 -> "removability in §5.10" — removability is §5.9 (line 896).
- §2.4 -> "we differentiate it in §5.7" — the differentiation is §5.6 (line 699).
- §5.4 -> "the Dabrowski-Tolsa theorem of §5.9" — it is §5.8 (line 845).
- §5.4 and the §4 map -> "§5.15" and "Coda (§5.14-5.15)". **No §5.15 exists**; the last
  subsection is §5.14 (line 1212).
- §5.8 -> "I return to it in §9.2". **§9 has no subsections**; the real target is §8.1/§8.2.
Navigational only. No mathematics affected.

**F4 — MINOR. Five survey-sourced claims carry author names but no year or title.**
Not fabrications, and each is explicitly attributed to the survey, but below the brief's
author+title+year bar: "Eiderman-Nazarov-Volberg" on vanishing lower density (§5.7); the
"David-Semmes BAUP criterion" (§5.7); Naber-Valtorta on harmonic-map singular sets (§5.4);
Hofmann-Mitrea-Taylor on (N_p) in SKT domains (§5.13); Jones and Murai on zero Favard
length with positive analytic capacity (§5.14). Count: 5.

**F5 — INFORMATIONAL, not a defect. Timestamps: NONE.**
The specific cross-file check requested. `grep -n "[0-9][0-9]:[0-9][0-9]"` over all 1951
lines returns zero hits. No section heading in this file carries a timestamp range. The
file is clean on the contamination pattern seen elsewhere in this repo.

## Self-report audit

§11 "Note on the tutorial process" (lines 1793-1951) is the most detailed self-report in
this repo: a talk/paper divergence table (8 rows), a 30-row caption->name correction table,
two explicit "not corroborated by the companion" notes (Calderon-Coifman-McIntosh-Meyer;
Kakutani), a "Names I could not verify, and did not guess" section naming two ("Pot",
"hung"), three substantive caption sign-flips, five rated gaps, two marked reconstructions.

**Load-bearing self-reported items I verified against the transcript — all true:**
- The three sign-flips are real caption errors, each present verbatim: "E is uniformly
  unrectifiable if and only if uh the risk transform ... is bounded in L2"; "this implies
  that f is unrectifiable"; "the set is invertifiable if and only if this integral is
  finite". Correcting all three was necessary; leaving them would have inverted theorems.
- "Pot" genuinely has no resolvable match. Refusing to write "Pajot" is the right call.
- The Bishop 1990/1992 and Kenig 1991/1994 reconciliations match the transcript
  ("bishop Chris Bishop in 1990", "a conjecture by bishop by 1992", "Carlos Kenik in the
  early '9s").
- The beta_{mu,1} vs beta_{mu,2} correction is CORRECT. I pulled the survey's Theorem 4.6
  verbatim: hypothesis (b) reads "beta_{mu,1}^{(d-1,L)}(B) <= delta * Theta_mu^{(d-1)}(B)".
  The speaker did say beta_2. The tutorial quoted the survey and flagged the divergence.
- Every block quote I spot-checked ("main black box", "cheating a little", "more visible",
  "I think that you should know this", "don't worry", "exhausting argument", "should not be
  so surprising", "topology in higher dimensions", "these domains are not interesting for
  us") is in the transcript, cleaned of disfluency only.

**What the self-report UNDER-reports — three items, all small:**

1. **A fourth silent caption correction, not among the "three sign-flips."** Line 215 quotes
   the speaker as "What is interesting and **remarkable**, I think...". The transcript reads
   "What is interesting and and **unremarkable** I think from this uh result". The fix is
   obviously right in context, but it is a fourth substantive (not spelling) caption change,
   and §11 asserts there are exactly three.
2. **The §6 Step 3 fill (F1) is absent from "Reconstructed and marked as such."** §11 lists
   two reconstructions (§5.4 density theorem, §7.2 constants). "Chebyshev + T1/good-lambda"
   is a third and is unlisted.
3. **The cross-reference drift (F3) is not mentioned at all**, including the two pointers to
   sections that do not exist (§5.15, §9.2).

**Verdict on the self-report: HONEST, and substantially complete.** Nothing it reports is
false; nothing material is concealed. The three omissions are one minor quote repair, one
unlabelled small reconstruction, and internal-numbering hygiene. That is under-reporting at
the margins, not misrepresentation.

## Direct answer to the audit hypothesis

The brief's worry: 110 KB + "structural" impact language x6 + zero `[Gap: ]` markers =
either the speaker stated everything, or gaps were filled instead of marked. **Neither.**
The correct third answer: **the tutorial DID mark its gaps, in a different string format,
and it had a full published companion paper — arXiv:2607.16457, which I verified is real,
with the exact title, both submission dates (17 and 21 July 2026), and the verbatim comment
field "Survey paper for the ICM 2026 plenary lecture of the author" that the front matter
claims** — to restore what the auto-captions destroyed. That is why the citation density is
low: it declares one governing source once, then labels every block drawn from it
"paper-only" or "paper-not-podium". One real fill exists (F1) and it is small.

## What I could not check
- Survey reference [106] (the p != 2 sharpness result). The tutorial gives it as Tolsa,
  *Publ. Mat.* 63 (2019); the survey's numbered citation exists but I could not open the
  bibliography entry. Plausible, not confirmed.
- Whether the survey truly contains NO probability/Kakutani anywhere (the tutorial's claim).
  My two ar5iv fetches surfaced none, consistent with the claim, but I did not read all
  ~25 pages.
- Exact page ranges on ~15 journal citations (Acta 213 (2014) 237-321; GAFA 26 (2016)
  703-728; Duke 173 (2024) 1731-1837; Invent. Math. 222 (2020) 881-993; Ann. of Math. 194
  (2021) 97-161; etc.). Journals, volumes and years are all consistent with real papers;
  I did not open each one.
- Whether the mathematics is TRUE. Out of scope by the brief.
- The identity of "Pot" and of "hung" — as the tutorial itself says, undeterminable from
  the captions.
