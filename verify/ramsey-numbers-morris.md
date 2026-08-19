# Verification — ramsey-numbers-morris
verdict: MINOR
uncited_external_claims: 0 — every external claim carries an arXiv id, an author+year, or an explicit "this is my reconstruction" label. I fetched and confirmed the three arXiv ids the companion could not corroborate.
unsupported_speaker_claims: 3 — two invented clock figures (F1, F2) and one misattribution to Kim (F3).
title_check: PASS — transcript opens "this talk is about combinatorics ... Ramsey numbers"; speaker introduced as Rob Morris of IMPA by Julian Sahasrabudhe. Title "Some Recent Results in Ramsey Theory" matches arXiv:2601.05221 exactly.
gap_honesty: PASS — all four declared gaps sit where the transcript really is silent; no gap silently filled.

## Ground truth used
- transcript: transcripts/McbrzDd7hCg_transcript.txt (10,021 words, NO timestamps anywhere)
- companion: arXiv:2601.05221 full text pulled from ar5iv and read locally.

## Numerical-bound audit (running)
Confirmed against the PAPER (Theorems 1.1-1.5 read verbatim):
- 2^{k/2} <= R(k) <= 4^k .............................. paper eq (1) OK; transcript OK
- R(l,k) <= C(k+l-2, l-1); R(k) <= C(2k-2,k-1) ~ 4^k/sqrt(k) . paper eq (2) OK
- R(k) <= (4-eps)^k, eps ~ 1/5 by Gupta-Ndiaye-Norin-Wei ... paper Thm 1.1 + remark OK
- (1/2+o(1))k^2/log k <= R(3,k) <= (1+o(1))k^2/log k ... paper Thm 1.2 OK
- ck^3/(log k)^4 <= R(4,k) <= Ck^3/(log k)^2 .......... paper Thm 1.3 OK
- R(l,k) >= k^{(l+1)/2+o(1)} (old lower) .............. paper Sec 1.1 OK
- AKS upper: R(l,k) <= Ck^{l-1}/(log k)^{l-2} ......... paper eq (3) OK
- R^ind(H) <= 2^{Ck} .................................. paper Thm 1.5 OK
- Shearer: alpha(G) >= (1+o(1)) n log d / d ........... paper Thm 2.2 OK
- Rodl nibble introduced by Rodl 1985 (Erdos-Hanani) ... paper Sec 2 OK
- R(3,k) lower bound by Hefty, Horn, King, Pfender ..... paper Thm 1.2 attribution OK

### Section 5.4 (R(3,k), the seven constructions) — every constant checked, ALL CORRECT
Checked one at a time against paper Sec 3 (verbatim):
- Erdos 1957 sphere/Kleitman construction -> R(3,k) >= k^{1+c} ......... paper 3.1 OK
- Erdos 1959, delete a VERTEX, p <= n^{-2/3} -> (k/log k)^{3/2} ....... paper 3.2 OK
- Erdos 1961, delete an EDGE, p ~ n^{-1/2} -> (k/log k)^2 ............. paper 3.3 OK
- Kim 1995 nibble -> k^2/log k order of magnitude ..................... paper 3.4 OK
- triangle-free process, FPGM + Bohman-Keevash -> (1/4+o(1)) k^2/log k  paper 3.5 OK
- alpha(G) = (2+o(1)) d(G) for the triangle-free process .............. paper 3.6 OK
- CJMS seed step: s=(log n)^2, p=sqrt(log n / 6n),
  d(G)=(sqrt2/sqrt3+o(1))sqrt(n log n), alpha<= (sqrt3/sqrt2+o(1))sqrt(n log n),
  -> (1/3+o(1)) k^2/log k ........................................... paper 3.6 OK (exact)
- HHKP: s=(log n)^2, p=sqrt(log n / 4n), d=(1+o(1))sqrt(n log n),
  alpha <= (1+o(1))sqrt(n log n) -> (1/2+o(1)) k^2/log k ............. paper 3.8 OK (exact)
- "roughly p^3 n^3 ~ p n^2 log n triangles in the union" .............. paper 3.8 OK
- "one deletion kills s = (log n)^2 triangles" ........................ paper 3.8 OK
- Alon-Rodl lemma: fewer than sqrt(C(n,k)) independent k-sets => R(3,3,k)>n  paper Lem 3.2 OK
- R(3,3,k) <= C k^3/(log k)^2 via AKS ................................. paper (13) OK
- R(3,3,k) >= c k^3/(log k)^4 via Alon 1994 graph ..................... paper (14) OK
- Shearer potential f(d)=(d log d - d + 1)/(d-1)^2, (d+1)f(d)=1+(d-d^2)f'(d), f''>0 . paper Thm 2.2 OK
I specifically hunted for the "constant moved across the equation" failure mode in these
nine formulas. I did not find one. sqrt2/sqrt3 and sqrt3/sqrt2 are the right way round;
6n and 4n are attached to the right constructions; the 1/4 -> 1/3 -> 1/2 chain matches.
Arithmetic self-check: alpha=(1+o(1))sqrt(n log n)=k gives n ~ k^2/(2 log k), i.e. 1/2. Consistent.

### Section 5.6 (R(4,k), Hermitian unital, containers) — ALL CORRECT
- H: n=Theta(q^4) vertices, Theta(q^3)-regular, Theta(q^3) edge-disjoint cliques of
  size Theta(q^2), every K_4 meets a clique in >= 3 vertices ......... paper Lem 4.2 OK
- unital defined by x^{q+1}+y^{q+1}+z^{q+1}=0 over (F_{q^2})^3, lines of PG(2,q^2)
  meeting U in exactly q+1 points ................................... paper Sec 4 OK
- O'Nan's theorem, 1972 ............................................. paper Sec 4 OK
- p = 1/q, k = q(log q)^3 ........................................... paper Sec 4 OK
- Container Lemma: R >= e^{-beta s} n and e(G[U]) >= beta|U|^2 for all |U|>=R
  => at most C(n,s) C(R,k-s) independent k-sets ..................... paper Lem 4.4 OK,
  restated with the exponent, the square and the binomials all in the right places.
- Kleitman-Winston 1982, Sapozhenko, Balogh-Morris-Samotij / Saxton-Thomason . paper OK
- greedy fingerprint/container proof sketch ........................ paper OK

### Sections 5.7-5.10, 6, 8 — every remaining bound checked, ALL CORRECT
- Thomason (1988, J. Graph Theory 12) -> Conlon (2009, Ann. Math. 170) -> Sah (2023, Duke 172),
  R(k) <= e^{-c(log k)^2} 4^k .. authors/years match paper bibliography [91],[28],[79];
  the e^{-(log k)^2} factor is SPOKEN in the transcript ("e to the lo k squ factor"). OK
- Spencer (1977, Discrete Math 20) improves the Erdos constant by exactly 2 ... paper [88] OK.
  The two constants 1/(sqrt2 e) and sqrt2/e are correctly LABELLED as a reconstruction
  (neither is in the transcript or the paper), and their ratio is 2, matching the spoken
  "a one became a two".
- Thm 9.1: for each r>=2 exists delta=delta(r)>0 with R_r(k) <= e^{-delta k} r^{rk};
  delta polynomial in r; absolute delta = Conjecture 9.4 ............. paper Sec 9 OK (exact)
- book (t,m)-book definition; t >= delta^4 k; m >= e^{-delta t^2/k} 2^{-t} n >= R(k-t,k);
  R(k-t,k) <= C(2k-t,k-t) <= e^{-t^2/6k} 2^{2k-t} ................... paper Sec 9 OK (exact)
  The tutorial's own three-line join (n = e^{(delta-1/6)t^2/k} 4^k, delta < 1/6) is its own
  arithmetic, is labelled as such, and is correct: 2^t * 2^{2k-t} = 4^k.
- Geometric Lemma 9.3, both alternatives: (31) P(inner products >= -1 for all i) >= delta,
  (32) P(inner product >= lambda) >= e^{-O(sqrt lambda)} ............ paper Lem 9.3 OK (exact)
- g(x_1..x_r) = sum_j x_j prod_{i!=j}(2 + cosh sqrt(x_i)); cosh sqrt x = sum x^n/(2n)!;
  and the case bound 3^r r exp(sum sqrt(x_i+3r)) / -1 ............... paper (33) OK (exact)
- Mubayi-Verstraete (2024): optimally pseudorandom K_l-free graph of density
  Theta(n^{-1/(2l-3)}) => R(l,k) >= c k^{l-1}/(log k)^{2l-4} ........ paper Thm 4.8 OK (exact)
- Bishnoi-Ihringer-Pepe 2020 give only density Theta(n^{-1/(l-1)}) ... paper (20) OK
- Question 4.7 "one of the most important open problems in graph theory" .. paper OK
- lower bounds c^{rk}; Abbott 1972; Conlon-Ferber, Wigderson, Sawin .. paper Sec 9 OK
- R_r(3) = O(r!) from Erdos-Szekeres; open to prove o(r!); Erdos 2^{Cr} .. paper 9.5/9.6 OK
- R_2^ind(H) <= k^{O(k)} (Conlon-Fox-Sudakov) -> R_r^ind(H) <= r^{Crk}
  (Aragao, Campos, Dahia, Filipe, Marciano, 2025+) .................. paper Thm 10.2 OK (exact)
- Campos-Samotij "efficient" container variant; global->local reduction .. paper Sec 1.3/10 OK
- f_q(X,Y) = e_B(X,Y) - q|X||Y|, with q = 1-p and gamma = 1-((sqrt5+1)/2),
  so p^2 = (1-gamma)(q-gamma) ...................................... paper Sec 7 OK, VERBATIM,
  including the counter-intuitive negative gamma; the writer did not "tidy" it.
- Fiz Pontiveros-Griffiths-Morris memoir is 125pp .................. paper ref [52]
  (Mem. Amer. Math. Soc. 263 (2020), 125pp) OK — "125 pages" is sourced, not guessed.
- E[X] = C(n,k) 2^{1-C(k,2)}, and the 3-uniform analogue C(n,k) 2^{1-C(k,3)} -> 2^{k^2/6}.
  The second is labelled as the writer's own reconstruction. Arithmetic checks out:
  k log_2 n ~ k^3/6 => n ~ 2^{k^2/6}.

### External citations fetched and verified (arXiv records, not merely plausible)
- arXiv:2605.28793 — Domagoj Bradac, "Off-diagonal Ramsey numbers", submitted 27 May 2026.
  Abstract states r(s,k) >= Omega(k^{s-1}/(log k)^{2s-4}). The tutorial's statement,
  exponent, id and date are ALL correct. I specifically suspected the writer might have
  copied the Mubayi-Verstraete conditional exponent 2l-4 into Bradac's theorem. It is
  genuinely Bradac's exponent.
- arXiv:2509.00716 — Ijay Narang and Muchen Ju, "Sharp Inner Product Correlations for
  Hypercube Bijections", 31 August 2025. Bound 1/4 - O(1/sqrt n); method = spectral
  decomposition of the Hamming association scheme, reformulated as a linear program over
  the Birkhoff polytope. The tutorial's bound, id, date, both first names and the proof
  method are ALL correct.
- arXiv:2512.20392 — Kuhn, Sauermann, Steiner, Wigderson, "Disproof of the Odd Hadwiger
  Conjecture". Chromatic number at least (3/2 - o(1))t; the conjecture is attributed to
  Gerards and Seymour, 1993, in the abstract. The tutorial's figure, attribution and year
  are correct. This id also appears in the companion's bibliography as [68].

I found NO instance of the sibling verifier's failure mode — a constant moved across an
equation. I checked roughly 45 separate numerical statements, one at a time.

## Findings

**F1 (MINOR — clock time; cannot come from the transcript).**
summaries/ramsey-numbers-morris.md:47 — "**The talk.** 56 minutes, uploaded 17 August 2026."
The transcript carries no timestamps and no duration. sources.txt lines 110-117 record no
duration either. The 56-minute figure can only be YouTube metadata; nothing in the two
verifiable sources supports it. Settled by: the video page's stated duration.

**F2 (MINOR — clock time; contradicted by the transcript's own wording).**
summaries/ramsey-numbers-morris.md:723 — "Now the last fifteen minutes, and the return to
R(k)." At the corresponding point Morris says "the last uh last few minutes of the of the
talk", and a paragraph later "the last 10 minutes of the talk". "Fifteen" appears nowhere in
the transcript. Low harm, but it is an invented clock figure. Settled by: deleting the number,
or using the speaker's own "last 10 minutes".

**F3 (MINOR — misreading of a speaker attribution).**
summaries/ramsey-numbers-morris.md:340 — "The nibble or semi-random method, introduced by
Rodl in 1985 and used by Kim in 1995 **for both directions** of the R(3,k) problem."
Kim [61] proved only the LOWER bound. The upper bound is Ajtai-Komlos-Szemeredi (1981) and
Shearer (1983) — the companion says so explicitly, and the tutorial itself says so correctly
in Sec 5.4. What Morris actually says is that the METHOD is used in both directions ("the
semi-random method is used to both the upper bound and the lower bound"), not that Kim did
both. The sentence gives both directions to Kim. Settled by: "...introduced by Rodl in 1985,
and used in both directions of the R(3,k) problem — by Ajtai-Komlos-Szemeredi above and by
Kim in 1995 below."

**F4 (MINOR — a year that neither source supports).**
summaries/ramsey-numbers-morris.md:164, :508, :509 — Campos-Jenssen-Michelen-Sahasrabudhe and
Hefty-Horn-King-Pfender are both dated **2026**. The companion (submitted 8 January 2026)
labels CJMS "2023+" in Theorem 2.3 and says the barrier "was finally overcome earlier this
year"; it dates HHKP only as "very recently". A January-2026 survey saying "earlier this year"
points to 2025, not 2026. The TRANSCRIPT settles it further: from an August-2026 podium Morris
dates the CJMS breakthrough to "just just last year", and says the HHKP construction "since
they put it on archive last year has had an amazing number of other applications". "Last year"
from August 2026 is 2025. So "2026" is not merely uncorroborated — the talk itself contradicts
it. Low harm — no bound depends on the year. Settled by: the arXiv submission dates.

**No MAJOR findings.** No invented theorem, no invented formula, no fabricated citation, no
wrong title.

## Self-report audit
The tutorial's Sec 11 "Note on the tutorial process" is **substantially honest, and unusually
so** — it over-reports rather than under-reports. Checked point by point:

- The 30-row name-correction table is accurate. Every corrected surname I could check appears
  either in the companion's bibliography (Fiz Pontiveros, Bohman, Keevash, Alon, Rodl,
  Mattheus, Verstraete, O'Nan, Campos, Jenssen, Michelen, Pfender, Krivelevich, Thomason,
  Conlon, Sah, E. Hurley, Tiba, Aragao/Dahia/Filipe/Marciano, Kuhn/Sauermann/Steiner/
  Wigderson) or in the arXiv records I fetched (Narang, Ju, Bradac). Its own caveat — that
  "Eoin" Hurley and the first names Ijay/Muchen are inferred, not heard — is correct and is
  disclosed.
- The four declared gaps are real gaps. The transcript IS silent exactly where claimed:
  Morris says "unfortunately I don't have time to explain his construction"; he says "I've
  ignored constants in the exponents. Apologies."; and the captions carry no formulas at the
  two diagonal-lower-bound slides. No gap was silently filled.
- The four declared reconstructions are the reconstructions actually present, and each is also
  labelled in place, not only in Sec 11.
- The three "substantive caption errors corrected" are genuine: the garbled book definition,
  the garbled R(3,k) <= R(3,3,k), and the 1947 Erdos conjecture date. Flagging that the
  companion does not corroborate the 1947 date is exactly right — it does not.

**Under-reported (three items, all minor):**
1. It does not disclose the two clock figures F1 and F2. Neither can come from a transcript
   that has no timestamps, and Sec 11 mentions neither.
2. It does not disclose that four substantive claims were sourced from OUTSIDE both the
   transcript and the companion, by fetching arXiv records: the Bradac id/date/exponent, the
   Narang-Ju id/date/bound/proof-method, and the odd-Hadwiger (3/2-o(1))t figure with the
   Gerards-Seymour 1993 attribution. Sec 8.7 half-acknowledges this ("six of the seven
   headline results are cited as arXiv preprints") and the Bradac gap row says "the paper is
   public", but Sec 11 never lists third-source lookups as a category of its own. I verified
   all four independently and every one is correct, so this cost nothing — but a reader
   auditing the tutorial from the two named sources alone could not confirm them.
3. It does not flag the Kim "both directions" slip (F3).

**Not under-reported:** the source-handling incident it records at the end (a CDN cache
returning the Hee Oh paper under the correct title) is a disclosure most writers would omit,
and it is consistent with the repo — verify/lens-of-circles-oh.md and the Hee Oh tutorial do
exist here, so the confusable document is real.

## What I could not check
- The video's true duration, its YouTube title, and its upload date. I have no access to the
  video metadata, and sources.txt records none of these.
- The publication years of the CJMS and HHKP papers (F4).
- Whether arXiv:2601.05221 is formally the ICM proceedings paper. The tutorial flags this
  itself at line 51 and states the evidence it used; the arXiv comment field does say only
  "37 pages, 2 figures" with no ICM mention, which matches its caveat.
- The mathematics itself. I checked that every bound is stated as its source states it. I did
  not check that any source is correct.
