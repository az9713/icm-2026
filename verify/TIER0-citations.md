# Tier 0 — citation resolution check

Run 2026-08-18. Machine check only: every arXiv ID and DOI in `summaries/*.md`
resolved against the arXiv API and the Crossref API. No mathematics was read.

## Result

- **261 citation instances**, **100 unique arXiv IDs**, 4 unique DOIs.
- **99 of 100 arXiv IDs resolve** to a real paper.
- **4 of 4 DOIs resolve** on Crossref.
- **Zero fabricated citations.**

The single unresolved ID is `arXiv:2020.02998` (month 20 is impossible), at
`summaries/langlands-function-fields-gaitsgory.md:1548`. The tutorial is *quoting an
error in Gaitsgory's own bibliography* and flags it as such. Not a defect.

## The four DOIs

| DOI | Resolves to |
|---|---|
| `10.1137/25M1799052` | Brendle, *Hamilton's Ricci Flow*, ICM 2026 Proceedings |
| `10.1137/25M1805497` | Gérard, *Hardy Spaces of Holomorphic Functions and Explicit Formulae...*, ICM 2026 Proceedings |
| `10.1137/25m1806971` | Dolgopyat, *Randomness, Rotations, Renormalization, and Resonances*, ICM 2026 Proceedings |
| `10.1145/3587250` | Gaitonde, Tardos, *The Price of Anarchy of Strategic Queuing Systems*, J. ACM |

## False positives — recorded so nobody re-runs them

The first pass raised 23 author/title mismatches and 12 date mismatches. **All 35 were
defects in the checking script, not in the tutorials.**

- The 23 were bare ID references in prose, with the full citation elsewhere in the file.
- The 12 were tutorials correctly giving BOTH a v1 and a v2 date; the script compared v1 only.
  One was a Bourbaki seminar delivery date, correctly distinguished from the arXiv date.

Positive evidence: the v1/v2 dates are accurate throughout. The writing agents opened the
real arXiv pages; they did not recite from memory.

## What this check CANNOT see

An invented formula. A theorem stated with no citation next to it. An author-year
reference carrying no ID. **Tier 0 moves no file from 'structural' to 'content-verified'.**
Only a read does that. See `verify/{slug}.md` for the tier 3 reads.

## Citation density per file

| File | Citation instances |
|---|---|
| `random-interface-growth-quastel.md` | 40 |
| `random-matrices-localization-yau.md` | 33 |
| `arithmetic-patterns-ziegler.md` | 24 |
| `hardy-spaces-explicit-formulae-gerard.md` | 24 |
| `randomness-rotations-resonances-dolgopyat.md` | 21 |
| `modern-ml-methods-bartlett.md` | 19 |
| `maestro-serre-sarnak.md` | 18 |
| `langlands-function-fields-gaitsgory.md` | 12 |
| `mesh-generation-pdes-buffa.md` | 10 |
| `learning-in-games-tardos.md` | 9 |
| `prismatic-homotopy-lurie.md` | 9 |
| `ricci-flow-singularities-brendle.md` | 9 |
| `geometric-concepts-pde-otto.md` | 7 |
| `optimization-theory-practice-wright.md` | 6 |
| `ramsey-numbers-morris.md` | 6 |
| `knots-four-manifolds-manolescu.md` | 4 |
| `lens-of-circles-oh.md` | 4 |
| `quantitative-rectifiability-harmonic-measure-tolsa.md` | 2 |
| `shape-of-math-kontorovich.md` | 2 |
| `uniformization-complex-geometry-mok.md` | 2 |
