# Internal consistency — round 2, 2026-08-18

The check `HANDOFF.md` listed as never run: does every cross-reference resolve, and does the
file render. No papers read, no transcripts read. Script:
`internal_check.py` pattern recorded at the bottom of this file.

Scope: all 20 files in `summaries/`.

## Result summary

| Check | Files scanned | Defects |
|---|---|---|
| Front matter keys + transcript file exists | 20 | **0** |
| `$$` display-block pairing | 20 | **0** (367 blocks, all balanced) |
| Inline `$...$` pairing, per file | 20 | **1** |
| Internal section cross-references | 20 | **14** in 4 files |
| Cross-tutorial section references | 7 refs | **0** — all resolve |
| Gap markers, grepped as `\[Gap[,:]` | 20 | 34, matches the recorded total |

## 1. Render defect — one unescaped currency `$`

`summaries/shape-of-math-kontorovich.md:637` writes `**$10,000**` with a bare dollar sign.
It is the file's only inline `$`. The next `$` in the file is the display block at `:709`.

Under MathJax with inline `$...$` enabled, the parser pairs those two and swallows lines
637-709 into a maths span. The file has no other inline maths, so nothing else masks it.

Fix: `\$10,000`. This is the only such case in the corpus — a grep for `$` followed by a
digit returns 51 hits and the other 50 are real maths (`$1/(x-z)$`, `$2t$`, `$32^3$`).

No file escapes a dollar anywhere (`grep '\\$'` returns nothing), so the escape is a new
convention, not a restored one.

## 2. Broken internal cross-references — 14, in 4 files

All 14 have one cause. Every tutorial ends with the same three back-matter sections, but
their **numbers differ per file** because the body section count differs. A reference was
written against another file's numbering.

| Where | Points at | Section actually holding the target |
|---|---|---|
| `hardy-spaces-explicit-formulae-gerard.md:57` | §11 | §8 "Where to read next" (`:1002`) |
| `hardy-spaces-explicit-formulae-gerard.md:82` | §13 | §10 "Note on the tutorial process" (`:1141`) |
| `hardy-spaces-explicit-formulae-gerard.md:85` | §13 | §10, correction table at `:1169` |
| `hardy-spaces-explicit-formulae-gerard.md:559` | §13 | §10 |
| `hardy-spaces-explicit-formulae-gerard.md:852` | §13 | §10 |
| `hardy-spaces-explicit-formulae-gerard.md:234` | §9.3 | §9 "Self-test" has no subsections; its items are numbered `<details>` blocks |
| `hardy-spaces-explicit-formulae-gerard.md:367` | §4.6 | §4 stops at 4.5 |
| `hardy-spaces-explicit-formulae-gerard.md:421` | §4.6 | §4 stops at 4.5 |
| `modern-ml-methods-bartlett.md:65` | §12 | §11 "Note on the tutorial process", table at `:1081` |
| `modern-ml-methods-bartlett.md:299` | §12 | §11 |
| `modern-ml-methods-bartlett.md:580` | §12 | §11 |
| `ramsey-numbers-morris.md:65` | §12 | §11, table at `:1391` |
| `quantitative-rectifiability-harmonic-measure-tolsa.md:643` | §5.15 | §5 stops at 5.14; the Jones-Wolff potential is at `:1252`, inside §5.14 |
| `quantitative-rectifiability-harmonic-measure-tolsa.md:894` | §9.2 | §9 "Where to read next" has no subsections |

`optimization-theory-practice-wright.md` runs to §13 and is the only file with that layout.
Three of the four broken files point at §12 or §13 — the Wright numbering.

**Reader impact: low but real.** A reader following "full correction table in §13" finds no
§13. Nothing states a wrong fact about the mathematics.

## 3. What returned clean, and what were false positives

**Cross-tutorial references all resolve.** Seven references reach into another summary file
by name. All seven targets exist: `otto:446`→wright §6.4; `gerard:996,:1281`→otto §8.5;
`sarnak:1355,:1730`→kontorovich §4.9 and §4.12; `bartlett:891`→wright §10.2;
`quastel:1308`→wright §10.4; `lurie:191,:1249`→gaitsgory §7.3; `dolgopyat:1648`→otto §8.5.

**Three false-positive classes**, recorded so nobody rebuilds the naive script:

1. **Bold inline subsection labels.** `modern-ml-methods-bartlett.md` writes §3.1-3.5 as
   `**3.1 Excess risk is not training loss.**`, not as headings. A heading-only scan calls
   6 valid references broken.
2. **Merged headings.** `knots-four-manifolds-manolescu.md:642` is `### 4.4-4.5 Kirby
   diagrams`. A scan keyed on one number per heading calls §4.5 missing.
3. **Line-wrapped inline maths.** The files hard-wrap at about 90 characters, so a `$...$`
   span often straddles a newline. A per-line dollar-parity test raises about 60 false
   positives in `gerard` and `sarnak` alone. Only whole-file parity is meaningful.

External `§` references — "paper §1.5.2", "Serre §1.6.5", "arXiv:2006.11748 §8.5" — are out
of scope here. They are provenance, and tier 3 covered them.

## 4. The script

Not kept as a repo file: it is 60 lines and re-derivable. Pattern, for a rebuild:

1. Parse the front matter between the first two `---` lines; require
   `title, speaker, source, date, transcript`; resolve `transcript` relative to `summaries/`.
2. Blank out fenced code blocks before any delimiter counting.
3. Count `$$` per file, require even. Remove `$$`, count `$`, require even. **Per file, never
   per line.**
4. Collect section labels from `^#{2,4} N(.M)* ` **and** from `^\*\*N.M `.
5. Flag `§N` or `§N.M` whose label is absent — then read each hit, because a reference to a
   companion paper looks identical to a reference to the file itself.

## 5. A count in `DEVELOPMENT-JOURNEY.html` that this check corrected

The journey document's §8.4 originally printed **1,048** inline `$...$` spans corpus-wide, and
per-file figures of `gerard` (51 display, 349 inline) and `buffa` (39 display, 212 inline).

Recounted here three ways:

| Method | corpus inline spans | gerard | buffa |
|---|---|---|---|
| Whole-file delimiter pairing (after removing `$$`) | **1,369** | 524 | 262 |
| Per-line regex, single-line spans only | 1,338 | 505 | 262 |
| Raw `$$` count / 2 | — | 51 display | **29** display |

Three corrections follow, and they are now in the journey document:

1. **1,369, not 1,048.** The gap between the two counting methods, 31 spans, is real — the files
   hard-wrap at about 90 characters, so some inline maths straddles a newline. Neither method
   yields 1,048; the original figure came from a method that was not recorded.
2. **`gerard` has 524 inline spans, not 349.** `buffa` has 262, not 212.
3. **`buffa` has 29 display blocks, not 39.** The corpus display total, 367, is confirmed by
   both methods and by the raw delimiter count, so the per-file 39 was simply wrong.

The `3,985 Unicode mathematical characters` figure was **not** re-derived — "Unicode mathematical
character" has no stable definition, and a naive character-class count returns numbers an order of
magnitude larger because it catches ordinary punctuation and Greek in prose.

**Why record this.** The undercount pointed the same way as the truth (heavy LaTeX in two files,
none in six), so nothing built on it was wrong. But it is a reminder that a corpus statistic
quoted in a report is itself an unverified claim.
