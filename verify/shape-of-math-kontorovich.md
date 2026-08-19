# Verification — shape-of-math-kontorovich
verdict: MINOR
uncited_external_claims: 3
unsupported_speaker_claims: 1
title_check: PASS — the introducer says "who will tell us about the shape of math to come"; Kontorovich then calls the title "an homage to one of my favorite jazz albums by Ornette Coleman".
gap_honesty: PASS — no `[Gap:` markers; the file instead marks two blocks **reconstructed** and refuses to name the prize judges. That refusal is the strongest honesty signal in the file.

Round 2, 2026-08-18. This was tutorial 1, written and self-verified by the session that
produced it, and **not** covered by the 15-file tier 3 run. This is its first independent
check. Method: full read of `summaries/shape-of-math-kontorovich.md` against
`transcripts/ZKF6dWzOiPA_transcript.txt`. Companion `arXiv:2510.15924` not fetched.

## Findings

### 1. `summaries/shape-of-math-kontorovich.md:637` — a render defect, not a content defect

`**$10,000**` carries a bare dollar sign. It is the only inline `$` in the file, and the
next `$` is the display block at `:709`, so a MathJax render pairs them and swallows 70
lines. Write `\$10,000`. Full detail in `verify/INTERNAL-CONSISTENCY.md` §1.

### 2. `summaries/shape-of-math-kontorovich.md:585` — "5 to 10 years", no source

> "His estimate: **5 to 10 years** for Mathlib to reach the needed scale in many core areas."

Repeated at `:917` (self-test question 6).

The transcript has no such number. Searches for "5 to 10", "10 years", "ten years" return
nothing, and the nearest sentence he actually speaks is hedged with no horizon at all: "if
that ratio gets below one, and I think it might, that's when everyone will just voluntarily
switch". The estimate is plausibly from the paper's §9, but the file gives no locator here,
while it does give one three paragraphs earlier ("paper, §9.1", "paper, §9.2", "paper, §9.3").

**Why it matters:** it is the file's one falsifiable prediction, and it is stated as the
speaker's. **What would settle it:** a paper section number, or deletion.

### 3. `summaries/shape-of-math-kontorovich.md:559-566` — the LANA paragraph adds institutions the talk does not give, and dates the report differently from the speaker

The talk says, entirely: LANA "had been ongoing for many years … was just announced
recently … I think **last week** released a report on the project. This is the LANA project,
Lean for anabelian geometry, **coming out of Japan**."

The tutorial says it was "launched in autumn 2023, announced by the ZEN Mathematics Center on
31 March 2026 with researchers from **Utrecht University and the University of Alberta**",
with an interim report "released **17 July 2026**".

Two gaps. The two named universities are not in the talk, and neither is Japan-based, so they
sit oddly against the one provenance detail the speaker did give. And the talk was uploaded
17 August 2026 with "last week" for the report, which does not match 17 July.

The paragraph does carry a citation — an `ncatlab.org` PDF — so this is not a fabricated
source. It is an unflagged substitution of the file's research for the speaker's words, in
a paragraph whose subject is a live and contested claim about Mochizuki's work. That subject
is why this is worth naming rather than waving through.

**What would settle it:** fetch the nLab PDF and either confirm the institutions and the
date, or attribute them to it explicitly and note the "last week" mismatch.

### 4. Two small external facts with no source

`:52` "Ornette Coleman's **1959** album" — the year is not spoken. `:227` "**Around 1990**,
the Knuth factor dropped below 1" is inside a quotation attributed to the paper, so it is
sourced; the surrounding TeX-adoption history is supported by the transcript ("AMS tech was
around in the 80s … it was just easier to handwrite and give it to a secretary").

## What I checked and found supported

The auto-captions destroy nearly every proper noun in this talk, so each of these was found
by searching for the idea, not the name. All are present:

- The 100-papers-a-day thought experiment, "This is not useful to me. I do math because it's
  fun", and "Brownian motion through language".
- **Kevin Buzzard** ("Kevin Buzzer" in captions), both times: the motivation quote, and the
  digitized-music analogy.
- **Scholze** ("Schultz") and the Liquid Tensor Experiment, including the IMO-perfect-score
  story, and the perfectoid project as what "first hit my radar".
- The token-saving hypothesis for why models weaken theorems — near-verbatim.
- The **Mathlib halo**, and the textbook-scale autoformalization caveat — verbatim term.
- Canonization, the X-versus-X′ failure, Zulip, and **"the definition of a group took maybe
  seven iterations"** — verbatim, seven included.
- The **de Bruijn factor** ("de Brun constant"), stated in the talk as 10 lines of natural
  language to 100 lines of formal code, and called "the wrong metric … because LLMs can write
  a 100 lines of formal code no problem". The file's "roughly ten lines per line" matches.
- **Sarnak and Iwaniec** as TeX holdouts ("Peter Sarn and my great colleague at Ruckers,
  Henrikets"), including the photograph-and-let-the-AI-typeset detail.
- **Gowers** and the 1999 essay: "what might mathematics look like in two to three decades?
  And here we are exactly halfway", and the "hardly pure mathematics as we know it today" line.
- The closing compass image — verbatim.

**The Wiedijk correction is the file at its best.** At `:517` it states plainly that
Kontorovich's "100 versus 10" is rhetorical and that the measured intrinsic de Bruijn factor
is about 4, cites the source, and does not pretend the speaker said it.

**The §4.11 four-agent section is correctly walled off.** Its heading reads "(this is in the
paper, not the talk)", and nothing in it is attributed to the podium.

## Exercises re-derived

- **§6.1 handshake lemma.** Re-derived. **Correct.** Σ_x d(x) = 2·(handshakes) is even; the
  even-degree part of the sum is even; so the odd-degree part is even; a sum of odd numbers is
  even exactly when the number of terms is even. The follow-up — name the three unstated
  assumptions (symmetry, irreflexivity, finiteness) — is the right pedagogical point and
  matches the talk's own framing of the Vulcan joke.
- **§6.2 Lean demo.** Not run, but each instruction was traced by hand against the
  reconstructed proof. Step 2 ("change `use 1` to `use 0`. It still works — see why") is
  correct: `hyp` holds for every n, so the witness is irrelevant. Step 1 (delete `intro n hn`)
  does break at `specialize hyp n`, as claimed. The code itself is marked **reconstructed**
  and is type-plausible; I did not compile it.

## What I could not check

- The companion `arXiv:2510.15924` was not fetched. Everything the file attributes to "the
  paper" — the four-agent architecture, the Rudin √2 example and its 140-line count, the two
  factor definitions in §9.1-9.3, the figure numbers in §10 — rests on the writing agent.
- The `ncatlab.org` LANA report and the `amathr.org/prizes` page. Neither is an arXiv id or a
  DOI, so `check_citations.py` never covered them either. They are the two most load-bearing
  non-arXiv URLs in the corpus.
- Whether the Lean code compiles. It is marked reconstructed; verifying it needs
  `live.lean-lang.org`.
- The Morph AI "Gauss" September 2025 claim, which the file attributes to the paper.
