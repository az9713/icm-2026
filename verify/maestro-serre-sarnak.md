# Verification — maestro-serre-sarnak
verdict: MINOR
uncited_external_claims: 5
unsupported_speaker_claims: 0
title_check: PASS — Katz's introduction announces "maestro Jean Pierre sir" (Serre) and Sarnak says "my talk from now on will be about Jean Pier"; front-matter title and speaker both match.
gap_honesty: PASS — the auto-captions carry no formula anywhere, and the tutorial marks the formula-heavy sections (§5.6 inline `[Gap: ...]`, plus a gap table in §11.6) exactly where the transcript really goes silent. I found no silently filled gap.

## Citation existence check (the MAJOR-risk class)
All six external citations were fetched and verified. **None is fabricated.**

| Cited as | Verified |
|---|---|
| arXiv:1807.11700, Serre, *Distribution asymptotique des valeurs propres des endomorphismes de Frobenius [d'après Abel, Chebyshev, Robinson, ...]*, Bourbaki, 42pp, French | exact title, author, page count and language match |
| arXiv:2603.05849, Gamburd–Ghosh–Sarnak–Whang, *On indefinite integral ternary quadratic forms*, v1 6 Mar 2026, v2 2 Jun 2026 | exact title, all four authors, both dates match |
| arXiv:2111.12660, A. Smith, *Algebraic integers with conjugates in a prescribed distribution*, bound 1.89831 | title, author and the constant 1.89831 all present in the abstract |
| arXiv:2401.03252, Orloski–Sardari–Smith, *New Lower Bounds for the Schur–Siegel–Smyth Trace Problem*, bound 1.80203 | exact; the abstract also confirms the tutorial's description of the method (new constraints reduce the number of variables; recovers Schur's and Siegel's bounds) |
| arXiv:2302.02872, Orloski–Sardari, general-K classification | *Limiting distributions of conjugate algebraic integers*, correct authors |
| arXiv:1704.02106, Parzanchevski–Sarnak, *Super-Golden-Gates for PU(2)* | exact |

## Verdict on the tribute-lecture adaptation (§5 and §6, checked hard)
**The adaptation is honest.** The failure mode named in my instructions — expanding a
passing mention into a full worked treatment Sarnak never gave — does occur in §6, but it
is declared, not concealed.

- §6 is a complete four-step proof (resultant integrality → weak limit → two variables →
  capacity) of a result Sarnak states in **one sentence** of the transcript: "any weak
  limit must satisfy that the integral of log of absolute of Q against that weak limit
  measure must be greater than equal to zero". Sarnak never mentions the resultant, never
  defines it, and gives no proof of anything in the last third.
- The tutorial says so, repeatedly and unprompted. The section opens "Here it is in full,
  **from Serre's §1.3–1.4**"; every step carries a lemma number from the companion (1.3.1,
  1.3.4, 1.3.7, 1.2.8, 1.2.11); and §11.6's gap table records "§5.11, §6 — the mathematics
  | **None. Fully restored from Serre's own exposé, with theorem numbers.**"
- §5.11 behaves the same way: every theorem number (1.2.10, 1.6.2, 1.7.8, 1.8.1, 1.8.2,
  (1.7.3), §1.5, §1.6.5) is attributed to arXiv:1807.11700, and the tutorial's own
  explanatory additions (the Joukowski derivation of the exponent 1/4; the electrostatics
  gloss) are visibly in the tutorial's voice rather than put into Sarnak's mouth.
- Everything the tutorial **does** attribute to Sarnak in §5.11 is in the transcript,
  including the q^(1/4) threshold, cap(circle of radius sqrt q) = sqrt q, Honda–Tate, the
  "much much smaller quite a thin set" remark, and "it's hard to compute capacities, by
  the way".

The one wobble is a framing sentence, not a claim: §6 opening (line ~1023), "The lecture
has no single theorem. But **it has** one argument that is short, complete, and entirely
within your reach." The lecture does not have that argument; Serre's exposé does. The very
next sentence names the source, so a reader is not misled for more than one line.

§5.1–5.9 track the transcript closely. Spot-checked and supported: the rank condition
i = 4m−1, n = 2m ("if I n is 4 m minus one 2 m"); S^61; Weyl's laudation wording; the 37 in
Serre uniformity; the knee-surgery story; the "cocycle races" acknowledgement; CSP kernel
finite iff the unit group is infinite; the Hamilton-quaternion two-primes challenge;
Conjectures I and II with the Steinberg 1965 / Merkurjev–Suslin 1985 /
Bayer-Fluckiger–Parimala 1995 chain; the Clifford+T and IBM quantum computer aside; the
closing 15 September 2026 paragraph. §5.5 correctly reproduces **and repairs** Sarnak's
live self-correction on the open image theorem, and flags in place that it is doing so.

## Findings

**F1 — §5.10, line ~797. Uncited external history, and not disclosed in §11.**
Claim: "Serre proved an upper bound with the large sieve; Hooley proved a matching lower
bound of the same order. The exact asymptotic resisted for 35 years."
Problem: none of this is in the transcript. Sarnak says only that Serre asked the question
in 1990 and that "this was resolved recently by Gamburd Gosh and myself and Wang".
"Hooley" appears nowhere in the transcript, nowhere in the §11.2 caption-correction table,
and nowhere in §11.5's "reconstructed" or "could not verify" lists. The nearby
arXiv:2603.05849 citation is attached to the *theorem statement*, not to this history.
This is the tutorial's clearest under-report.
Settles it: the introduction of arXiv:2603.05849, which would name Serre's and Hooley's
prior bounds if they exist.

**F2 — §1, lines ~113–115. Uncited biographical detail, asserted as checked.**
Claim: "**Paul Serre** (1895–1972), a France international wing and centre" and "**Denis
Serre**, who works on nonlinear PDE at **ENS Lyon**", closed with "Both facts check out."
Problem: the transcript supports only "a Paul sir who was a very famous rugby player
playing for France internationally", "uncle", and "Dennis S is a very accomplished
mathematician working in nonlinear PD". The birth and death years, the playing positions,
and the ENS Lyon affiliation are external, carry no citation, and "Both facts check out"
asserts a verification the reader cannot audit. Low stakes, but it is exactly the
uncited-external pattern.
Settles it: a source for Paul Serre's dates and positions.

**F3 — §5.4, line ~500. "Bass–Milnor–Serre (1967)".**
The transcript gives the names ("basil ner") but **no year**. 1967 is external and uncited.
§11.2 even reprints "1967" in the *Check* column of the correction table without a source,
which makes an added fact look like a recovered one.
Settles it: the Bass–Milnor–Serre paper reference.

**F4 — §5.7, line ~677. Book subtitle and publisher.**
Claim: "*Chasing a Conjecture: Inside the Mind of a Mathematician*, Juggernaut. **It
exists**." The transcript gives only "a book ... called chasing a conjecture". The subtitle
and the publisher are external and uncited, and "It exists" again asserts an unauditable
check.
Settles it: the book's catalogue entry.

**F5 — §5.8, line ~717. Tunnell.**
Claim: "The octahedral case is Tunnell's, building on Langlands. Sarnak did not say this;
I add it." The disclosure is exemplary — the tutorial flags its own addition inline — but
the addition still carries no citation.
Settles it: Tunnell, *Artin's conjecture for representations of octahedral type*, 1981.

**Borderline, not counted.** "Chris Smyth, who introduced this technique in 1984" (§5.11).
The 1984 date is external, but §11.3 states that Serre cites him as "[Sm 84]" in the
exposé, so it is effectively sourced to the companion.

**Not a finding, recorded for completeness — the two Orloski arXiv ids are both correct.**
§5.11 uses 2302.02872 for the general-K classification (Orloski–Sardari) and 2401.03252
for the 1.80203 lower bound (Orloski–Sardari–Smith). I verified these are two genuinely
distinct papers and that each is attached to the right claim. The front-matter "note on
sources" mentions only 2401.03252; that is incompleteness, not error.

**Not a finding, recorded — one internal muddle.** §5.8 says Maass forms "with eigenvalue
exactly 1/4" and then, two lines later, "Those eigenvalues are 'outside a quarter'". Both
halves derive from the caption "an igen value with value of quarter ... those are outside
a quarter". The two sentences read as contradicting each other. **Cannot determine** which
reading Sarnak intended; the captions are the only evidence and they are ambiguous. The
audio would settle it.

**Unsupported speaker claims: none found.** The nearest candidate is §5.11's "If you
restrict to **Jacobians of curves** with genus growing" — the transcript says only "a
sequence of curves whose genus is getting large". "Jacobians" is the tutorial's
interpolation and is the standard reading of the statement; I do not count it.

## Self-report audit

**The §11 self-report is honest and, on everything structural, unusually complete.** It
correctly discloses:

- that §6 and §5.11 are restored from Serre's exposé rather than from the lecture (§11.5,
  §11.6). This is the single most important disclosure in the document and it is made
  plainly, in two separate places, rather than buried;
- the Smyth / Alexander Smith conflation (§11.3), which the captions genuinely make
  invisible — a real trap, correctly identified as two different people, with the
  consequence spelled out (Smyth's condition is necessary, Smith proved it sufficient);
- Sarnak's live self-correction on the open image theorem (§11.3);
- the Fekete–Szegő "every neighbourhood" versus Robinson "in E itself" distinction that
  Sarnak blurred, and why the difference matters for Serre's application (§11.3);
- five reconstructions with their evidence: Kneser, Eskin–Oh, Mestre, Milnor-as-reviewer,
  Fricke;
- five "could not verify" items, including the unrecoverable "GMA" lecture of 1953, which
  it **omits rather than guesses** — the right call;
- the **Tsfasman–Vlăduţ versus Drinfeld–Vlăduţ** ambiguity (§11.5). This is the item most
  worth praising. The captions read "a theorem of Vlad and Drenfell", i.e.
  Drinfeld–Vlăduţ; the tutorial prints Tsfasman–Vlăduţ instead, and then says exactly
  that, gives its reason (the companion cites [TV 97]), and names the alternative reading.
  A dishonest agent would have printed one name and said nothing;
- an ~80-row caption/correction table which matched the transcript, row for row, on every
  entry I sampled.

**Where it under-reports.** Four items, all of one kind: small external facts laid on top
of what Sarnak said, none disclosed anywhere in §11.

1. **Hooley and the large sieve (F1)** — the most substantive omission. A named
   mathematician and a named method, attributed to a research history the lecture never
   gives, absent from both the name table and the "could not verify" list.
2. **Paul Serre's dates and playing positions, and Denis Serre's ENS Lyon affiliation
   (F2)** — and the sentence "Both facts check out" claims a verification that §11 never
   accounts for.
3. **Bass–Milnor–Serre 1967 (F3)** — the year is added silently, and §11.2 reprints it in
   a column reserved for recovered facts.
4. **The Khare book's subtitle and publisher (F4)**, again with an "It exists" assertion
   that §11 does not back.

Also unlisted in §11, though flagged inline where each occurs: **Tunnell** (F5), and the
§5.8 eigenvalue muddle.

**Net judgement.** The self-report is honest about everything structural — what was
reconstructed, what came from the companion instead of the lecture, what could not be
recovered, and which name it deliberately changed against the captions. It under-reports
only small uncited biographical and bibliographic garnish. None of the omissions touches
the mathematics, and none is a case of the agent concealing a reconstruction. The pattern
is a writer who policed the mathematics rigorously and then relaxed on the anecdotes.

## What I could not check
- Whether the mathematics is **true**. Out of scope by the brief.
- **Every theorem number quoted from arXiv:1807.11700** — 1.2.8, 1.2.10, 1.2.11, 1.3.1,
  1.3.4, 1.3.7, §1.5, 1.6.2, §1.6.5, 1.6.8, (1.7.3), 1.7.8, 1.8.1, 1.8.2, and Appendix
  A.1/A.2/A.3. The paper exists with the exact claimed title, author, length and language,
  but I did not read the PDF. Settles it: reading arXiv:1807.11700.
- **The two claimed errata in the companion** (§3.3 and §11.4: the doubled 1/n exponent in
  (A.2.1); §7.3 and §11.4: e^(3/2) printed as "4,816"). Note that the arXiv comment field
  for 1807.11700 records "two corrections suggested by J. Rivera-Letelier and M. Sombra",
  so the posted version has already been corrected once — the tutorial's errata may or may
  not survive in the current version. Settles it: the PDF.
- **Theorem 1.3 and Theorem 1.1 of arXiv:2603.05849** as quoted in §5.10, including the
  X^6 / sqrt(log X) asymptotic and the Markoff-spectrum statement. Paper, authors and both
  submission dates verify; the theorem statements were not read.
- **Serre's *Œuvres* volume V**, and the Oberwolfach Report citation for the quaquaversal
  group (vol. 6 (2009) no. 2, 1421–1426), including the claim that the generators have
  orders 6 and 4 — the transcript says only "two rotations".
- **Whether Sarnak said "Drinfeld–Vlăduţ" or "Tsfasman–Vlăduţ"**. Only the audio settles it.
- **Milnor as the reviewer of Serre's collected works I–III.** Captions say "Milton"; the
  tutorial's reading is plausible and is flagged as unconfirmed in two places.
- **The exact wording of Weyl's 1954 laudation** against the printed Amsterdam proceedings.
- The tutorial's process claim that Sarnak's arXiv author listing has "39 entries, most
  recent March 2026" and contains no ICM proceedings contribution.
