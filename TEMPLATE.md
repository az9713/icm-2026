# Tutorial spec — ICM 2026 plenary lectures

You are writing one long-form tutorial for one ICM 2026 plenary lecture, for one specific
reader. Read this whole file before you write anything.

Two finished examples live in `summaries/`. Read **both** before starting — they are the
ground truth for tone, depth, and length:

- `summaries/shape-of-math-kontorovich.md` — a talk outside the speaker's famous field
- `summaries/optimization-theory-practice-wright.md` — a talk inside the reader's own field

---

## 1. The reader

Everything you write is aimed at one person. Get this wrong and the tutorial is worthless.

**The reader.** Doctoral training in **classical physics and applied mathematics**.

They have, deeply: real and complex analysis, ODEs and PDEs, linear algebra, probability,
Fourier analysis, numerical methods, calculus of variations, classical mechanics,
statistical mechanics, optimization, some functional analysis.

They do **not** have: algebraic geometry, algebraic topology, number theory (analytic or
algebraic), representation theory, category theory, geometric group theory,
low-dimensional topology, derived algebraic geometry.

Professionally they **build and direct AI agent systems**, rather than hand-writing code.

They read everything. They want to **learn something useful** from each talk, not to be
given trivia. Plain language, full technical substance. They would rather delete a file
than add one.

---

## 2. The two rules that produced the first two tutorials

### Rule 1 — Read the talk before you judge it

**A plenary talk is often much narrower than the speaker's famous field, and sometimes has
nothing to do with it at all.**

The worked failure: Alex Kontorovich is famous for analytic number theory, Apollonian
circle packings, and Zaremba's conjecture. He was filed as one of the hardest talks in the
set. His actual talk was about **AI, Lean, and formal verification** — squarely in the
reader's own professional domain, and one of the easiest in the set.

Confirmed instances in this playlist: Simon Brendle's talk is **"Hamilton's Ricci Flow"**,
not his recent scalar-curvature work. Patrick Gérard's is **Hardy-space explicit
formulae**, not his field broadly. Robert Morris's is **graph Ramsey numbers**
specifically.

So: download the transcript, read all of it, and only then decide what the talk is about,
how hard it is, and what to anchor it to. Never assign any of those from the speaker's
reputation or from the lecture title alone.

### Rule 2 — Anchor to something the reader already owns

For each talk find the **anchor**: a thing the reader already knows deeply that this talk is
structurally about. Not a decorative analogy — a real correspondence.

Real examples, to calibrate what counts:

- Optimal transport: the Fokker–Planck equation **is** the gradient flow of entropy in the
  Wasserstein metric. That is their statistical mechanics.
- Arithmetic quantum chaos: the Selberg trace formula plays the role of the Gutzwiller
  trace formula.
- Floer homology: Morse theory on an infinite-dimensional space of gauge fields; the
  origin is Yang–Mills.
- Random matrices: Wigner invented them to model nuclear energy levels.
- KPZ: surface growth and a stochastic Burgers equation.
- Random graph thresholds: percolation and phase transitions.
- The Kontorovich talk: **the reader's own agent-orchestration work** — the anchor was not
  physics at all.

The anchor is chosen from the talk's actual content. If the honest anchor is weak, say so
plainly rather than inflating it.

**Best case: the speaker hands you the anchor.** Gaitsgory says from the podium that the
Langlands correspondence "should be seen as some sort of non-abelian Fourier transform".
That is better than any anchor a search would produce. Look for it before inventing one.

**Reject a suggested anchor that the talk does not support — including one your own brief
suggested.** The brief for the Gaitsgory tutorial proposed Kapustin–Witten
electric–magnetic duality, which is a real and famous bridge into geometric Langlands. The
talk never mentions it. The correct response, and the one taken, was to use the speaker's
own framing and add one short paragraph naming the physics route *as absent*, so the reader
knows it exists and knows it is not what the talk does. Decorating a talk with someone
else's picture is a subtler form of the fabrication rule below.

---

## 3. Difficulty rating

Rate 1–5 against **the reader's** background, from the talk's content:

- **1** — their own field. Optimization, numerical PDE, statistical mechanics, agent systems.
- **2** — one step out. Needs a few new definitions they could absorb in an afternoon.
- **3** — a real but crossable gap. Needs a genuine background section.
- **4** — far. Multiple unfamiliar layers stacked.
- **5** — frontier of abstraction. ∞-categories, geometric Langlands, derived AG.

### Split the rating when the talk genuinely splits

A single number sometimes misdescribes a talk. Two cases seen already, both real:

- **Two half-talks.** Otto's lecture is two disjoint vignettes joined by one method. Part
  one is Otto calculus, difficulty 1. Part two is singular SPDE and renormalization,
  difficulty 3. Rated `1/5 (part one) — 3/5 (part two)`, with the Tier-0 inversion applied
  to part one only and a full bridge built for part two.
- **Maths easy, frame hard.** Bartlett's lecture uses only objects the reader owns —
  gradient flow, Hessian eigenvalues, KKT, the pseudoinverse — inside a statistical
  vocabulary they do not: excess risk, effective rank, margin bounds. Rated
  `2/5 (the mathematics) — 3/5 (the statistical frame)`, compressing the optimization
  background and building a real bridge for the statistics.

Split it when splitting is honest. Say in the header which half is which, and apply the
inversion to whichever part earns it.

### The Tier-0/1 inversion — important

**When the talk is at difficulty 1 or 2, invert the template.** Do not spend the document
teaching them things they already know.

Compress the background into a **one-page calibration section** they can skip — just enough
to fix vocabulary — and spend the length instead on **what has changed recently** in that
field. The delta, not the bridge. See the Wright tutorial, which does exactly this.

At difficulty 3–5, the bridge is the main event and gets the space.

---

## 4. Sources

### The transcript

Download and clean it with exactly this, substituting the video ID. All transcripts in this
repo must be byte-identical in format.

```bash
cd /path/to/icm_2026
yt-dlp --no-update --skip-download --write-auto-subs --sub-langs "en" --sub-format vtt \
  -o "transcripts/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=VIDEO_ID"
```

Then clean and delete the intermediate `.vtt`:

```python
import re, pathlib
vid = "VIDEO_ID"
src = pathlib.Path(f"transcripts/{vid}.en.vtt").read_text(encoding="utf-8")
out, seen = [], None
for line in src.splitlines():
    if "-->" in line or line.startswith(("WEBVTT","Kind:","Language:")) or not line.strip():
        continue
    t = re.sub(r"<[^>]+>", "", line).strip()
    if not t or t == seen:      # auto-captions repeat the previous line
        continue
    out.append(t); seen = t
text = re.sub(r"\s+", " ", " ".join(out))
p = pathlib.Path(f"transcripts/{vid}_transcript.txt")
p.write_text(text, encoding="utf-8")
pathlib.Path(f"transcripts/{vid}.en.vtt").unlink()
print(p, len(text.split()), "words")
```

**Read the whole transcript.** Not the first half.

### The companion document

In order of preference:

1. **The ICM 2026 proceedings paper**, if you are given an arXiv ID. Use it. Fetch
   `https://arxiv.org/abs/ID` and, if you need detail,
   `https://arxiv.org/html/IDv1` (the PDF endpoint often exceeds the fetch size limit).
2. **If there is no proceedings paper** — and for most talks in this playlist there is
   not — find the speaker's most recent **survey or lecture notes on this specific talk
   topic**. Label it clearly in the front matter and in the source note as a *companion,
   not the proceedings paper*. Do not silently present it as the ICM paper.
3. **If neither exists**, say so explicitly in the source note and work from the transcript
   alone.

**Listen for the speaker naming their own survey.** The single most reliable way to find a
companion is that speakers cite themselves from the podium. Bartlett names his Acta
Numerica review aloud; that turned out to be the correct companion and no search would have
ranked it first. Scan the transcript for "my survey", "our review", "the paper with", a
journal name, or a book title before searching the web.

**Restore from the primary literature, not only from the companion.** When a talk presents
published results, each rate, threshold and definition can be recovered from *its own*
paper. That is how the Bartlett tutorial recovered almost all of its mathematics despite
having no proceedings paper at all. Cite those inline by name, and keep them visibly
distinct from the companion — they are primary literature for one theorem, not a substitute
for the proceedings paper.

Note the talk and the paper can genuinely differ — the Kontorovich talk named two concepts
his paper does not, and the paper spelled out an architecture the talk only gestured at.
Where they differ, say which one you are quoting.

---

## 5. Hard rules

These are not style preferences. Breaking any of them makes the document worse than nothing.

**Never invent mathematics.** Auto-captions carry no formulas — the mathematics lived on
the board and the slides, invisible to the caption track. If the transcript and the
companion document together do not support a statement, **do not write it**. Mark the gap
in place:

> *[Gap: the speaker states the main estimate here; the captions carry no formula and no
> companion paper exists. The result is described qualitatively below.]*

A tutorial with honest holes is useful. A tutorial with plausible fabrications is
poison — the reader cannot tell which parts to trust, so they must distrust all of it.

**Some things cannot be taught in a tutorial. Say so and stop.** The Gaitsgory tutorial
declines to teach two objects (AGCat, 2-IndCoh), presenting each as a fact with its
motivation and its consequence and no more, and states in the process note that this was
deliberate. That is correct. Faking depth produces exactly the smooth fabrication that is
worse than an acknowledged hole.

**Check the companion document too — it is not infallible.** The Gaitsgory paper's
bibliography carries an invalid arXiv identifier (`2020.02998`; there is no month 20, the
real one is `2008.02998`). Also: an arXiv HTML title block often shows a date produced by
LaTeX's `\today` at regeneration time, **not** the submission date — take the date from the
arXiv stamp instead. And where the paper states a result more strongly than the speaker did
from the podium, quote the paper and note the difference.

**Rate each gap's impact** in the process note — low, moderate, or structural — so the
reader knows which holes cost them something. "The constants were on the slide; the shape
carries the argument and is stated" is low impact. "This is the most consequential caveat
in the talk and he gives one sentence" is moderate. Say which.

**Cross-reference sibling tutorials rather than rewriting them.** Several of these talks
overlap — Wright, Bartlett and Otto all touch implicit bias and benign overfitting; several
touch AI and verification. Where another tutorial in `summaries/` already covers shared
material at length, cite it by filename and move on. Keep your own tutorial readable alone,
but do not reproduce a neighbour's bridge section wholesale.

**Mark reconstruction.** Where you rebuild code, a diagram, or an equation from spoken
narration, label it **reconstructed** and say what would verify it.

**Verify every proper noun.** Auto-captions destroy names — real examples already found:
"Danig" → Dantzig, "Kacion" → Khachiyan, "Spielman and Tang" → Spielman and **Teng**,
"Nearoski and Uden" → Nemirovski and Yudin, "Wayne and her" → Weinan E, "Sophie Hibbitz" →
Sophie **Huiberts**. Check each against a primary source. Put the corrections in a table in
the process note. If you cannot verify a name, write *(reconstructed)* or omit it — never
guess silently.

**Correct substantive caption errors too, not just spellings.** One transcript said an
iterate had its "last n−k components nonzero" when they are **zero** — the opposite, and
the whole argument depends on it. Fix it in the text and flag it in the process note.

**Full prose, not bullet digests.** Long-form narrative paragraphs that walk through the
argument. Light headings for navigation. Tables where a table genuinely helps. No
LLM-slop openers.

---

## 6. Structure

Front matter:

```yaml
---
title: "<the lecture's actual title>"
speaker: Name (Institution)
source: https://www.youtube.com/watch?v=VIDEO_ID
video_id: VIDEO_ID
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: <arXiv URL, or "none — companion: <URL>", or "none">
transcript: ../transcripts/VIDEO_ID_transcript.txt
difficulty_for_you: N/5
reading_time: ~N min
---
```

Then, adapting freely where the talk demands it:

1. **Header block** — field, difficulty with one line of justification, what this tutorial
   builds, and a short **note on sources** saying what exists and what does not.
2. **What is at stake** — the question and why it matters, in plain language, no jargon.
3. **Your anchor** — the thing they already know. At difficulty 1–2 this becomes
   *Calibration: what you can skip*.
4. **The bridge** — the minimum new vocabulary, each concept defined by deforming
   something they know, each with a small concrete example. The main event at difficulty
   3–5; compressed to one page at 1–2.
5. **The talk, rebuilt** — a walkthrough in the speaker's own order, with the mathematics
   restored from the companion document. Every symbol defined before use. Gaps marked.
6. **The one argument** — the central result or claim, stated precisely, with a proof
   sketch at an honest depth. Rename it if "theorem" does not fit the talk.
7. **Do this by hand** — one or two small, concrete, checkable exercises with `<details>`
   solutions. This is where the learning actually happens; do not skip it.
8. **What is actually useful to you** — the highest-value section. A transferable tool,
   method, or reframe. Where the talk touches agent systems, verification, or how research
   is done, make the connection to their work explicit and concrete.
9. **Where to read next** — three items maximum, ordered.
10. **Self-test** — 8 to 10 questions, each answer inside `<details>`.
11. **Note on the tutorial process** — the name-correction table, what you reconstructed,
    what you could not verify, where the gaps are, and whether the difficulty matched what
    the speaker's reputation would have predicted.

Length: comparable to the two examples. Substantial. Do not pad, and do not truncate the
walkthrough to save effort.

---

## 7. Filename

`summaries/{short-slug}-{speaker-surname}.md` — lowercase, dashes only, no underscores.
Keep the slug short; drop filler words.

Examples: `shape-of-math-kontorovich.md`, `optimization-theory-practice-wright.md`.

---

## 8. What you must NOT do

- **Do not touch `sources.txt`.** The main session regenerates it from front matter.
  Concurrent appends corrupt it.
- **Do not run any `git` command.** Not `add`, not `commit`, not `status`. The main session
  commits. Concurrent git collides on `index.lock`.
- **Do not write any file** other than your own `summaries/{slug}.md` and
  `transcripts/{video_id}_transcript.txt`.
- **Do not paste the tutorial back** in your final report. Write the file; report briefly.

## 9. Your final report

Short. Six lines, not six paragraphs:

1. The talk's **actual** subject, in one sentence, from the transcript.
2. Difficulty assigned, and whether it matched the speaker's reputation.
3. The anchor you chose.
4. Companion document used, or none.
5. **Gaps flagged** — where the mathematics was unrecoverable, and how bad it is.
6. Names you could not verify.
