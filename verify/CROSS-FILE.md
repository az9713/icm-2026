# Cross-file findings

Checks that no single-file verifier could make, because each verifier saw one tutorial only.
Run by the main session over all 20 files.

## 1. Timing metadata the transcripts cannot support

The transcripts are auto-captions. **They carry no timestamps.** A single `5:00` appears in
`transcripts/u-ssCmb8YBo_transcript.txt`, and that is spoken content, not a caption index.

So no clock claim about a recording can be checked against the transcript.

### 1a. Section-heading timestamp ranges — one file only

`summaries/arithmetic-patterns-ziegler.md` stamps 18 of its §4 headings — 17 ranges
(`00:00-08:00` ... `70:00-end`) plus one point stamp, `:678` `(48:00)`. **No other tutorial
does this.** The same file also
contradicts itself on the talk length: `:29` "fifty minutes", `:1481` "seventy-minute talk",
`:1500` "fifty-minute talk". 8,048 transcript words at 130-160 wpm gives 50-62 minutes.

### 1b. Prose claims about the recording — 11 files

Roughly 20 phrases across 11 files assert where something sits in the recording. Examples:
`ricci-flow-singularities-brendle.md:157` "the talk spends fifty minutes on";
`random-matrices-localization-yau.md:62` "devotes its last five minutes";
`maestro-serre-sarnak.md:64,:138,:1548` "the last twenty minutes";
`knots-four-manifolds-manolescu.md:70` "two minutes in";
`random-interface-growth-quastel.md:1481` "nine minutes in";
`ramsey-numbers-morris.md:723` "the last fifteen minutes" (Morris actually says "last few
minutes", then "the last 10 minutes").

**Two caveats before anyone edits these.**
1. A stated total duration (`prismatic-homotopy-lurie.md:1302` "49 minutes",
   `random-matrices-localization-yau.md:1367` "duration 53 minutes",
   `ramsey-numbers-morris.md:47` "56 minutes") may legitimately come from video metadata via
   yt-dlp. Check before deleting.
2. Every tutorial also carries reader-facing exercise estimates ("(25 minutes)"). Those are
   fine and are NOT this defect. A grep cannot separate the two classes reliably; a human
   must look.

Ordering claims ("the first third", "he opens with") are safe — the transcript is ordered.
Only clock quantities are unsupported.

## 2. Citation resolution

See `TIER0-citations.md`. 100 arXiv IDs, 4 DOIs, zero fabricated.

## 3. Gap-marker syntax drift

`TEMPLATE.md:212` specifies the literal form `[Gap: ...]`. Three files use
`[Gap, <impact>: ...]` instead, so a grep for `[Gap:` misses them and undercounts.

| File | `[Gap:` finds | `[Gap[,:]` finds |
|---|---|---|
| `quantitative-rectifiability-harmonic-measure-tolsa.md` | 0 | 3 |
| `prismatic-homotopy-lurie.md` | 2 | 3 |
| `randomness-rotations-resonances-dolgopyat.md` | 2 | 3 |

The Tolsa file looked like it marked no gaps at all. It marks three. The content complies
with the template; only the string differs. Grep `\[Gap[,:]` from now on.

Real total across all 20 files: **34 gap markers**, not the 29 a strict grep reports.
