# Verifier brief — ICM 2026 tutorial provenance check

You verify ONE tutorial. You do not rewrite it. You do not edit it. You never run git.

## Your two files
- Tutorial: `summaries/{SLUG}.md`
- Transcript: path is in the tutorial's own front-matter `transcript:` key (relative to `summaries/`).

## What you check — PROVENANCE, not peer review
You cannot check whether the mathematics is TRUE; you do not have the papers.
You check whether each claim has a source. Four questions only:

1. **Speaker-attributed claims.** When the tutorial says the speaker said/showed/proved
   something, does the transcript support it? Auto-captions destroy proper nouns and all
   formulas — absence of a mangled name is NOT evidence. Absence of the whole IDEA is.
2. **External claims.** Every theorem, rate, constant, or definition NOT in the transcript
   must carry a citation (arXiv id, DOI, or author+title+year). An uncited external claim
   is the dangerous class. Flag every one.
3. **Front-matter title vs transcript opening.** Read the first ~80 lines of the transcript.
   Does the announced subject match the title? (A previous tutorial had a wrong title from
   the video listing; this check exists because of that.)
4. **Honest gaps.** The tutorial marks unrecoverable spots with `[Gap: ...]`. Are the gaps
   where the transcript really is silent? Did it silently fill a gap instead of marking it?

## Hard rule
Never invent mathematics to test mathematics. If you cannot tell, write "cannot determine"
and say what would settle it.

## How to write your report — WRITE AS YOU GO
Create `verify/{SLUG}.md` after you finish reading the FIRST major section, then APPEND to it
as you read on. Do not hold the report in memory until the end. If your session dies, a
partial file on disk is the whole point.

Report format:

    # Verification — {SLUG}
    verdict: CLEAN | MINOR | MAJOR
    uncited_external_claims: N
    unsupported_speaker_claims: N
    title_check: PASS | FAIL — <one line>
    gap_honesty: PASS | CONCERN — <one line>

    ## Findings
    (one block per finding: `summaries/{SLUG}.md:LINE`, what it claims, why it is a problem,
     what would settle it. Most-severe first. Write "none" if none.)

    ## What I could not check
    (list)

Verdicts: MAJOR = an invented theorem/formula, a wrong title, or a fabricated citation.
MINOR = uncited-but-plausible claims, thin sections, small inconsistencies.
CLEAN = every external claim cited, every speaker claim supported, title correct.

When the report is complete, write the single word `done` into `verify/{SLUG}.DONE`.

## What you return to the caller
At most 400 words: the verdict line, the counts, and the 3 worst findings. Nothing else.
The full detail lives in your file, not in your reply.
