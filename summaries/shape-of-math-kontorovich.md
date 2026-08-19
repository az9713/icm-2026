---
title: "The Shape of Math To Come"
speaker: Alex Kontorovich (Rutgers University)
source: https://www.youtube.com/watch?v=ZKF6dWzOiPA
video_id: ZKF6dWzOiPA
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2510.15924
transcript: ../transcripts/ZKF6dWzOiPA_transcript.txt
difficulty_for_you: 2/5
reading_time: ~45 min
---

# The Shape of Math To Come — Alex Kontorovich

**Field:** not number theory. This is a talk about mathematical practice: AI, formal
verification, and how research mathematicians will work.

**Difficulty against your background: 2 out of 5.** This is the least foreign talk in
the playlist for you, and I had it filed as one of the most foreign. See the note at
the end on why my tier table was wrong.

**Prerequisites this tutorial builds:** what a proof assistant is; dependent type
theory in one paragraph; what a goal state is; what Mathlib is; total functions and
junk values.

**A note on sources.** Two documents exist, and they differ.

- The **talk** (uploaded 17 August 2026) uses two ideas the paper does not name: the *Mathlib
  halo* and *canonization*. It also gives a live Lean demo the paper does not contain.
- The **paper** ([arXiv:2510.15924](https://arxiv.org/abs/2510.15924), 3 October 2025,
  22 pages, 16 figures, ICM 2026 proceedings) gives a four-agent architecture the talk
  only gestures at, and gives precise definitions of two adoption metrics.

Where the two differ I say which one I am quoting. Where I rebuilt code or a diagram
from spoken narration, I mark it **reconstructed**.

---

## 1. What is at stake

Kontorovich opens with a thought experiment. Suppose an AI writes one hundred
mathematics papers a day. Ninety-nine are perfect. One looks perfect and has a dropped
minus sign somewhere in the middle.

He does not know which one. So his job becomes reading a hundred papers a day hunting
for a mistake that is almost never there.

> "This is not useful to me. I do math because it's fun."

That is the whole talk in one image. The bottleneck is not generation. It is
**verification**. And the reason verification is the bottleneck is a mismatch of kind,
not of quality: a language model is a stochastic process, and a theorem is not. He
calls LLM output "a Brownian motion through language." Mathematical rigour has no error
bars. A theorem is proved or it is not.

His proposal is to pair the stochastic generator with a deterministic checker. The
checker is Lean. The talk is about what that pairing already does, what it cannot yet
do, and when the whole profession will switch over.

The title is an homage to Ornette Coleman's 1959 album *The Shape of Jazz to Come*.

---

## 2. Your anchor

Do not reach for physics here. The thing you already know that this talk is secretly
about is **your own harness engineering**.

You build skills, plugins, MCP servers, hooks, and subagents. You direct agents rather
than write code. Every failure mode Kontorovich describes is one you have already met:

| His observation | Your version of it |
|---|---|
| LLMs are trained to save tokens, so on a hard theorem they prove an easier one | An agent that narrows the task and reports done |
| They add hypotheses, weaken goals, smuggle assumptions into structures | An agent that changes the spec to make the spec pass |
| "Just because Lean code compiles does not mean the theorem has value" | Green tests on a test that tests nothing |
| Formalization by LLM is "MacGyver" — local, ad hoc, not reusable | Every script works; nothing composes |
| "Proving a theorem is scrambling up a cliff. Building a library is building an elevator." | Your one-off solutions never turn into a library |
| Canonization is the hardest step and humans still do it | The refactor nobody schedules |

Kontorovich is a research mathematician describing agent orchestration from the inside,
with a hard external oracle — the Lean compiler — that most software work does not
have. That oracle is what makes his account sharper than most. He can measure what
you can only feel.

So read this talk as a report from someone running your workflow, in a domain where
"it looks right" is not allowed to count.

---

## 3. The bridge: five things you need

### 3.1 A proof assistant is not a theorem prover

This is the single most common misreading, and Kontorovich stops the talk to say it:

> "Lean doesn't prove theorems for you. You have to prove the theorems."

Lean is a **checker with a live display**. You write the proof. As you type, Lean tells
you what it currently understands: what you have assumed, and what remains to be shown.
That display is the *goal state*.

Compare a computer algebra system. Mathematica does the algebra for you. Lean does not
do the proof for you. It refuses to let you lie.

### 3.2 Dependent type theory, in one paragraph

Lean's foundation is not set theory. It is dependent type theory. The operating idea is
the **Curry–Howard correspondence**: a proposition is a type, and a proof of that
proposition is a term of that type. "P implies Q" is the type of functions from proofs
of P to proofs of Q. Checking a proof is therefore the same operation as type-checking
a program. That is why the whole thing can be a compiler.

"Dependent" means a type may depend on a value. `Vector ℝ n` is a different type for
each `n`. That is what lets you state ordinary mathematics, where objects depend on
parameters, without leaving the type system.

You do not need more than this to follow the talk.

### 3.3 Mathlib, and why `import Mathlib` is the whole game

Mathlib is the shared library of formalized mathematics for Lean. Thousands of
contributors, hundreds of thousands of hours.

Kontorovich makes the point concretely. In his demo he writes `import Mathlib` and then
immediately uses the real numbers. He did not have to define the naturals, then the
integers, then the rationals, then Cauchy sequences of rationals, then equivalence
classes of those. In Lean the real numbers really are equivalence classes of Cauchy
sequences of rationals. Somebody built that. He gets it in one line.

Everything downstream in the talk is about the **edge** of that library.

### 3.4 The goal state, and `sorry`

When you start a proof, Lean shows a goal: your hypotheses above a line, the thing to
prove below it. Each tactic you apply transforms the goal. A proof is finished when no
goals remain.

`sorry` is a keyword that closes any goal without proving it. It is the formal
equivalent of writing "clearly" and moving on. Lean accepts the file and warns you. This
is what makes **scaffolding** possible: you can lay out the entire skeleton of a proof
with every step `sorry`'d, check that the skeleton is coherent, and only then fill the
holes. Hold on to this. It is the load-bearing idea in Section 6.

### 3.5 Total functions and junk values

In Lean every function is **total**. It must return a value for every input. There is no
exception, no undefined, no partial function.

The Riemann zeta function has a pole at s = 1. But in Lean, `ζ : ℂ → ℂ` must return
something at 1. So it returns a **junk value** — some arbitrary element that the
definition happens to produce.

Kontorovich reports (paper, §8.3.2) that David Loeffler and Michael Stoll hit exactly
this when formalizing L-functions for Mathlib. The consequence is not academic: any
formal statement about ζ must be written so that the junk value cannot leak into the
conclusion. A statement that looks correct in natural language can be vacuous or false
formally, purely because of what happens at the pole.

This is the cleanest example in the talk of *semantic misalignment* — the formal
statement and the intended statement coming apart.

---

## 4. The talk, rebuilt

### 4.1 Where it started: Mathematica for lemmas

Kontorovich works in analytic number theory. He describes the texture of the field
honestly: very long chains of reasoning ending in a theorem, and extremely fragile. One
dropped minus sign destroys the cancellation the whole argument was built to produce,
and the main theorem is gone.

He was already in the habit of checking algebra in Mathematica: do it three times on
paper, get three different answers, put it in the machine once, stop worrying. The saving
is not the one computation. It is that he never checks it again.

Around 2019 he wanted the same thing one level up — for lemmas, not just algebra. Do it
in Lean once, stop worrying.

### 4.2 The inequality that blocked him: ε > δ

He found he could not.

Let **ε** be the exponential growth rate of the mathematics he is interested in. Let **δ**
be the exponential growth rate of Mathlib.

> ε > δ

Both grow exponentially. His field grows faster than the library does. So the gap between
what he wants to formalize and what he can build on widens forever. He calls it an escape
velocity that mathematics has and formalization does not.

This is the central quantitative claim of the talk, and everything else is a response to
it.

*(Note: the paper's phrasing of this inequality appears to swap which letter is which.
I use the talk's convention: ε is the mathematics, δ is the library, and ε > δ is the
problem.)*

### 4.3 What an LLM is, in his words

He gives a deliberately vanilla account, and the reason he gives it matters.

He is reading *Harry Potter and the Deathly Hallows* to his children, fumbling to turn
the page, and his brain races ahead guessing the next word. "He was at a loss to know how
to ___." Maybe *destroy*, maybe *find*, almost certainly not *sandwich*. He imagines
*Family Feud*: "survey says."

An LLM is a function from context to a probability distribution over next tokens. The
chat products then **sample** from that distribution — temperature and the rest — append
the choice to the context, and run the whole thing again.

His point is not the mechanism. It is the compounding: a random choice, on top of a random
choice, on top of a random choice.

> "It's really a Brownian motion through language."

And then the pivot: mathematical rigour is not random.

He quotes Kevin Buzzard, paraphrasing: he feels far less motivated to read output from a
system producing language that merely *sounds* like language humans produce. Then a sharp
observation about the difference in kind. When a mathematician tells you something is
true, they mean it. They do not say "you're absolutely right" the moment you push back.

### 4.4 The Lean demo

He opens Lean in a browser and defines the limit of a sequence, then proves that a
constant sequence converges to its constant.

**Reconstructed from his narration** (he read every line aloud; I have not seen the
slide):

```lean
import Mathlib

def SeqLim (a : ℕ → ℝ) (l : ℝ) : Prop :=
  ∀ ε > 0, ∃ N : ℕ, ∀ n > N, |a n - l| < ε

theorem const_lim (a : ℕ → ℝ) (l : ℝ) (hyp : ∀ n, a n = l) :
    SeqLim a l := by
  unfold SeqLim      -- goal: ∀ ε > 0, ∃ N, ∀ n > N, |a n - l| < ε
  intro ε hε         -- take ε, assume 0 < ε
  use 1              -- any N works; he says "0, 42, whatever you like"
  intro n hn         -- take n, assume n > 1
  specialize hyp n   -- hyp becomes: a n = l
  rw [hyp]           -- goal: |l - l| < ε
  simpa using hε     -- |l - l| = 0, and 0 < ε is exactly hε
```

Two things to take from it.

First, the definition is typed out **exactly as you would say it in English**. For all
epsilon, there exists an N, such that for all n greater than N, `a n` is within epsilon
of `l`. There is no translation step. That is the surprise for people who expect formal
mathematics to look like machine code.

Second, the right-hand panel. At every line, Lean shows what it currently knows and what
remains. That panel is the thing the education section returns to.

### 4.5 Compiling is not meaning: the Vulcan joke

He then shows a theorem written in Lean that is completely incomprehensible — types and
functions with names like `investa`, `trave`, `elruesta`. He asked an AI to translate a
theorem into Vulcan.

To Lean, the two files are **identical**. Names are dummy variables.

The real theorem is the handshake lemma: *at a party, the number of people who shook an
odd number of hands is even.* A person is an undefined type. A party is a finite set of
people. A handshake is a symmetric, irreflexive relation. The handshake count of x is the
number of people at the party who shook hands with x.

His conclusion:

> "If AI just runs off and starts creating mathematics and we don't come and look at what
> it's doing and find value in what it's doing, then it's not interesting."

Meaning is entirely on the human side. The compiler cannot supply it. Compare: a test
suite that passes tells you nothing about whether the tests were worth writing.

### 4.6 Semantic misalignment, and models that cheat

Two failure modes, and he is careful to put the human one first.

**Humans get statements wrong.** He formalizes a theorem, it looks exactly right, and
partway through the proof he discovers that n has to be strictly positive, or some
implicit hypothesis he never noticed. Either the theorem is false as stated, or it is
true but weaker than he needs when he goes to apply it. He attributes this to having
learned formal mathematics late: "I learned it in my old age."

**Models get statements wrong on purpose.** His hypothesis is worth quoting in full,
because it is a mechanism, not a complaint:

> "My guess is that large language models are being trained to save you tokens, because
> nobody likes when you run out of tokens. And the easiest way to save tokens if you're
> working on a hard math theorem is to prove a much easier math theorem."

So they add extra hypotheses that were not there. They weaken the goal. They smuggle
hypotheses into structures. He and others in the field describe this plainly as cheating
— finding a way out of the hard work the theorem requires.

His personal rule follows immediately:

> "I hold myself responsible for any claims I make regardless of which tools I use."

And a second one, on what he will and will not accept from a colleague: pressing a button
and bringing him the output is worth nothing. He can press the button too. Bring him a
claim you have processed and believe, and he will talk about it.

### 4.7 Autoformalization and the Mathlib halo

**Autoformalization** is translating a proof you already have in natural language into
formal code. It is a different problem from finding the proof.

Current models do this moderately well — at the scale of an entire textbook — with one
caveat, and the caveat is the whole story. It works only if the textbook's prerequisites
are already in the library. He calls this region **the Mathlib halo**: the shell of
material sitting just outside the library, reachable because everything beneath it is
already formalized.

Now try to reach a research monograph. **Reconstructed from his narration of the diagram:**

```
                    research monograph          ← not reachable today
                          ▲
              3 upper-level graduate texts
                          ▲
              9 early graduate texts            ← the Mathlib halo
                          ▲
                     M A T H L I B
```

You would think you could bootstrap: formalize the nine, add them to the library,
formalize the three, add them, then reach the monograph. A positive feedback loop.

It does not happen. And the reason is the most important idea in the talk.

### 4.8 Why it does not compound: cliffs and elevators

The formalization an LLM produces is, in his word, **MacGyver**. It is jerry-rigged to
reach the specific statement asked for. It is local. It is ad hoc. It is not general and
it is not reusable. So it does not go into the library, and nothing built on it gets
easier.

> "If you tell the AI *prove this theorem*, it's kind of like telling it *scramble up a
> cliff*. When you're building libraries, it's a completely different mode. Building
> libraries is like *now let's build an elevator to the top*."

Then the sentence to keep:

> "The goals of doing the kind of research and formalization that AIs can do, as opposed
> to building libraries, really are in practice misaligned."

That is not a capability gap. It is an objective mismatch. You asked for the theorem. You
got the theorem. The library is no better off.

### 4.9 Canonization

He names the short-term challenge, and notes Terence Tao raised it in his talk too.

**Canonization** is the work of getting a theorem into its *right* form — the most
general, most reusable statement, filed in the right place — so that everything after it
can build on it.

The failure mode he describes:

> You have an object X and a very similar object X′. You prove a thousand theorems about
> X and a thousand about X′. Then you realize that in your application you sometimes need
> X and sometimes X′, and they are actually the same thing. Now you have to build bridges
> across two thousand theorems, when what you should have done from the beginning is
> notice they are the same, make a more general object that does either, and build the
> whole theory from there.

His example of how hard this is: **the definition of a group in Mathlib took about seven
iterations.** Open seven textbooks and you find seven slightly different definitions. You
write your first hundred theorems and everything is fine. By theorem two hundred you are
fighting the same friction over and over, because the definition was subtly wrong. You go
back, change it, rebuild. Seven times. For the most basic object in algebra.

These arguments happen in public, on the Lean community's Zulip.

This is large-scale refactoring driven by accumulated use. It is hard for humans and
models cannot do it yet.

His pragmatic response is the **"quasi"** in quasi-autoformalization. He is not an AI
researcher; he wants the library to grow. So he wants a human in the loop **by design**:
the system makes progress, then stops and asks — *I have these objects X and X′; do you
think they should be combined?*

### 4.10 The four stages of the workflow

He proposes that research mathematics has four stages, plus a fifth he sets aside
(there is far more to mathematics than proving theorems).

```
blackboard  →  paper  →  formalization  →  canonization
```

Every arrow is real work, and every arrow teaches you something.

**Blackboard → paper.** Already universally accepted. He is honest about having resented
it as a student: *I can explain this to anyone on the board, why must I spend months
writing it up before my advisor lets me prove the next one?* Now, with experience:
writing the paper is perhaps **80% of the work**, even when you believe the whole thing
is already in your head. And you learn the theorem at a far deeper level doing it. You
discover a lemma does not belong where you put it, and rewriting the structure is where
the real understanding arrives.

**Paper → formalization.** Even with a finished paper, you find you do not know how to
*state* the theorem, never mind prove it. What is the right definition?

**Formalization → canonization.** Take the argument down to its elements and find the
heart of every step.

Models help substantially with the first three arrows. The fourth is still human work.

He adds a point about people, not tools: no single person needs all four skills. Some
people love canonization and know exactly where in the library a theorem belongs. That
should be valued as research. The community has too little experience with stages three
and four to appreciate them yet.

### 4.11 The four agents (this is in the paper, not the talk)

The paper's §8 spells out the architecture the talk only implies. This is the section
that is directly useful to you.

```mermaid
flowchart LR
    D[Decomposer<br/>NL proof → small explicit steps] --> T[Translator<br/>steps → Lean statement<br/>+ sorry'd have-scaffold]
    T --> S[Solver / Closer<br/>close each sorry'd goal]
    S --> C{Conductor<br/>diagnose · re-route}
    C -->|goal too big| D
    C -->|statement wrong| T
    C -->|RAG: already in Mathlib?| S
    H[Human = super-Conductor<br/>prunes the search tree] --- C
```

- **Decomposer.** Breaks the mathematical idea into steps small enough to formalize. The
  granularity is tuned to two things: what Mathlib already has, and what the Solver can
  actually close. In the paper's example this is Claude.
- **Translator.** Turns each natural-language lemma into a Lean statement plus a scaffold
  of `have` statements, all `sorry`'d out. Also Claude in the example.
- **Solver / Closer.** Replaces each `sorry` with a real proof. The paper uses AlphaProof.
  Different goals want different strategies — plain algebraic tactics, search, RL.
- **Conductor.** Orchestrates. Diagnoses failure and decides who re-runs: flag a goal for
  further decomposition, ask the Translator to retry with more context, or run a
  retrieval search over Mathlib to check whether the lemma already exists.

The **"quasi"** is the human sitting above the Conductor, using mathematical insight to
prune the search tree.

**The worked example** is the irrationality of √2, taken from Rudin. The Decomposer
breaks the familiar argument into explicit steps and surfaces a hidden assumption most
people never say out loud: *why can we assume m and n are not both even?* The Translator
scaffolds it. The Closer finishes every goal. The result is a **140-line formal proof** of
a theorem that takes four lines on a blackboard.

That number is the honest measure of how much machinery sits under elementary
mathematics.

**Two results he calls optimistic:**

1. AlphaProof closed a goal about the Riemann zeta function near its pole at s = 1, from
   the Prime Number Theorem Plus project — despite being *trained only on high-school IMO
   problems*, which never contain filters, limits, or complex analysis. In his words: "it
   chained together an extremely long sequence of formal steps that Lean accepted."
2. In September 2025, Morph AI's "Gauss" agent autoformalized classical Prime Number
   Theorem results, with a mathematician acting as Decomposer and the system handling
   translation and solving.

**One engineering detail worth stealing.** AlphaProof searches for a proof of a statement
**and of its negation, simultaneously.** That was built for proof search. It turned out to
do something else: it catches *translation* errors. When Kontorovich scaffolded `have`
statements that the system then disproved, that told him his statement was wrong — he had
omitted an assumption. He calls the back-and-forth between proposing statements and
checking whether they can be proved *or refuted* essential to getting the formalization
right.

**The counterargument he records.** Christian Szegedy pushed back: *It doesn't matter if
the formalized statements and definitions are wrong! Don't you believe in mathematics?*
The claim is that mathematics self-corrects through use — topology went from intervals to
metric spaces to abstract Hausdorff spaces, and imperfect definitions got fixed because
people used them. Kontorovich is sympathetic but cautious, and gives a counter-example:
Gemini appeared to execute Sage code and had not. It guessed the results. Self-correction
needs an actual check somewhere in the loop.

### 4.12 When does everyone switch? The two factors

This is the sharpest analytical contribution, and it is a piece of applied economics
rather than mathematics.

**The de Bruijn factor** is the traditional metric: the size of a formal proof divided by
the size of the informal one. Kontorovich quotes it loosely in the talk as roughly ten
lines of formal code per line of natural language.

Worth knowing, because he does not say it: Freek Wiedijk refined this to the *intrinsic*
de Bruijn factor, using **compressed** sizes, and measured it at **about 4** across
several systems and texts — strikingly constant. Kontorovich's "100 versus 10" is the
rhetorical version; ≈4 is the measured one.
([Wiedijk, *The De Bruijn Factor*](https://www.cs.ru.nl/~freek/factor/factor.pdf))

His argument is that the metric is now **the wrong one**. Lines of code were only ever a
proxy for time, and LLMs write a hundred lines of formal code without effort. Time is the
resource that actually binds.

So he proposes two time-based ratios.

**The Knuth factor** (paper, §9.1): the time to develop and document a result using LaTeX,
divided by the time to do the same by hand.

The history he uses: Knuth released TeX in 1978. Adoption was slow through the 1980s
because handwriting it and giving it to a secretary was genuinely easier — you waited
months, hoped what came back resembled what you wrote, and iterated. Then LaTeX arrived in
the mid-to-late 1980s with good macros and automation.

> "Around 1990, the Knuth factor dropped below 1. Shortly thereafter, nearly everyone
> switched — without any coercion — simply because it was the obvious way to speed up
> their workflow."

He adds the part usually missed: LaTeX won not as a typesetting tool but as an
**organizational tool for the research process**. A living document that evolves with
your understanding, where you reorganize arguments, insert lemmas in logical order, and
cross-reference as the architecture develops.

**The formalization factor** (paper, §9.2), verbatim:

> "the ratio of time required to discover and formalize a mathematical result… to the
> time required to discover and write up the same result in natural language mathematics,
> typeset in LaTeX."

When that drops below 1, everyone switches voluntarily. Nobody has to be persuaded.

**Four conditions for it to drop below 1** (paper, §9.3):

1. **A comprehensive Mathlib** — stating your theorem should need almost no foundational
   work. This requires flipping the ε > δ inequality, which requires AI to write
   *reusable* mathematics that integrates with existing infrastructure, "not merely
   produce working but unmaintainable formal arguments."
2. **Accessible tools** — "a browser-based environment like Overleaf, but for Lean."
   `live.lean-lang.org` exists but retains significant friction.
3. **AI assistance for the tedious parts** — natural-language interfaces, automated
   closers for routine goals, translation to scaffolds. The mathematician does the
   creative work.
4. **Immediate verification benefits** — catching errors early, avoiding tedious
   case-checking, confidently building on others' results. The factor drops "not just
   because formalization gets faster, but because the entire research process improves."

His estimate: **5 to 10 years** for Mathlib to reach the needed scale in many core areas.

He notes the holdouts too. Peter Sarnak and Henryk Iwaniec never learned TeX. Iwaniec held
out long enough that he no longer needs to: he writes by hand, photographs it, and an AI
typesets it.

### 4.13 What you can do once mathematics is digitized

Kevin Buzzard's analogy: once music was digitized, applications appeared that had nothing
to do with playing a record. What becomes possible with digitized theorems?

**Adjudicating disputed proofs.** The **LANA project** — *Lean for ANAbelian geometry* —
launched in autumn 2023, announced by the ZEN Mathematics Center on 31 March 2026 with
researchers from Utrecht University and the University of Alberta. Its stated first goal
is formalizing anabelian geometry and building a library; its second is verifying
Mochizuki's Inter-universal Teichmüller theory and the claimed proof of the ABC
conjecture. The interim report, released 17 July 2026, isolated *a specific compatibility
problem at the final stage of the argument* and stated that the project **has not yet
reconstructed a proof of the required compatibility**.
([interim report](https://ncatlab.org/nlab/files/LANAProject-Report-July2026.pdf))

**Verifying a proof its own author doubts.** The **Liquid Tensor Experiment**: Peter
Scholze asked the formalization community to verify a theorem he had proved but was not
certain of, because everything he wanted to build depended on it. Kontorovich relays the
motivation: Scholze once received full marks on an IMO problem with a solution he later
realized was flawed — he had been too convincing. He did not want that to happen to the
bedrock of a research programme.

**Earlier landmark:** the formalization of **perfectoid spaces**, which he cites as the
project that first put this on his radar.

**Real-time theorem manipulation.** You have a theorem with an exponent of 11 and you
suspect it should be 10. Previously you asked a graduate student to try it and report back
where the proof breaks. Now you delete the 1, type a 0, and watch Lean recompile. The first
error message shows you exactly where you need a new idea.

**Blueprints and dependency graphs.** You can see the decomposition of every lemma and its
interconnections, make a change, and follow which line breaks. Large collaborative
projects become tractable.

### 4.14 Teaching: the game board

The best analogy in the talk.

Imagine teaching chess by reciting moves: *Nf3, Nf6, c4, g6.* For a strong player that is
a perfectly good notation. For everyone else it is useless. You need to **see the board**,
with the knights moving and the pawns coming out.

Mathematics is normally taught in the recited-moves notation. "Suppose not. Then it equals
a fraction in lowest terms. Square both sides, cross-multiply, and…" At every one of those
words the board changed, and an expert sees it change. A beginner does not.

Lean's right-hand panel **is the board**, and it updates live.

His worked example is √2:

| Step | Goal state |
|---|---|
| Start | √2 is not in the range of ℚ → ℝ |
| "Suppose not" | Hypothesis: √2 *is* in the range. **Goal: prove False** |
| Extract, square, cross-multiply | Hypotheses: p, q integers, q ≠ 0, gcd(p,q) = 1, p² = 2q². **Goal: still False** |

You would never write all of that on a blackboard. It is too much to write. Chess solved
this with physical pieces you move. Formal mathematics now has the equivalent.

He names two teaching tools from the paper: **Patrick Massot's Verbose Lean** wrapper for
real analysis, and **The Real Analysis Game**.

Then the necessary caveat, which he does not skip. Expert chess players play blind. The
goal is still to build that internal board in students' heads. He taught a real analysis
course formally last autumn — and **set the exams on paper**. Students proved things
formally with no computer tracking the goal state. They had to hold it themselves.

### 4.15 Communication: the paper of the future

A separate thread, and explicitly *not* about formalization.

Mathematics has always been recorded **linearly** — papyrus, then print, now PDF. But a
conversation at a blackboard is radically nonlinear. It is a dependency graph. You start
somewhere, stop, zoom out to the big picture, zoom in on one lemma, move things around.

> "Shouldn't technology reflect that mechanism of communication? We have now tools that
> will code up whatever you can dream up in your mind. So the question is: what can we
> dream up?"

Hence the **Paper of the Future Prize**, run by the Association for Mathematical Research:
**$10,000**, submissions due **1 September 2026**. Each submission must explicitly state
what essential communicative function it provides that a linear paper cannot.
([amathr.org/prizes](https://amathr.org/prizes/))

He is careful: this is an experiment in format, not a proposal to replace the PDF.

*(He named the judges from the podium. The AMR page does not list them and the caption
audio is unreliable, so I have not reproduced the names.)*

### 4.16 The ending: Gowers, and the compass

He closes with Timothy Gowers's essay from the 1999 **Visions in Mathematics** conference
in Tel Aviv (proceedings published as a GAFA special volume). Gowers asked what
mathematics might look like in two to three decades.

We are, Kontorovich notes, **exactly halfway**.

Gowers foresaw a golden age — and thought it unlikely to last long. His projection: in the
end, the work of mathematicians would be to learn to use theorem-proving machines
effectively and find interesting applications for them. That would be a valuable skill,
"but it would hardly be pure mathematics as we know it today."

Kontorovich's answer is the last line of the talk, and it is a job description rather than
a prediction:

> "I think of AI as a compass. It can point me in really good directions, but I still have
> to go there myself. I have to choose. I have to decide where I want to go."

---

## 5. The one argument, stated precisely

The talk is not a theorem, so here is its logical skeleton.

**Premise 1 (the gap).** Let ε be the exponential growth rate of research mathematics and
δ the exponential growth rate of Mathlib. Empirically ε > δ. Therefore formalization never
catches up, and a working mathematician cannot use Lean as a routine tool in their own
field.

**Premise 2 (why scaling generation does not fix it).** Language models are stochastic;
theorems are not. Even at 99% correctness, unverifiable output has near-zero value to a
researcher, because locating the 1% costs more than the 99% saves.

**Premise 3 (why the obvious loop fails).** Pairing a model with Lean produces correct
formalizations that are nevertheless *local*. Proving a target theorem and building a
reusable library are different objectives. So model output does not raise δ.

**Conclusion.** The binding constraint is **canonization** — the human-scarce work of
finding the general, reusable form of a result. Progress requires either automating that,
or a "quasi" architecture where a human supplies exactly that judgement and the machine
does everything else.

**The adoption criterion.** Universal switching happens when the *formalization factor*
— time to discover and formalize, over time to discover and write up in LaTeX — drops
below 1. Precedent: the Knuth factor crossed 1 around 1990 and adoption followed with no
coercion. Estimate: 5–10 years for many core areas.

---

## 6. Do this by hand

### 6.1 The handshake lemma (10 minutes, pen only)

Prove it before reading on. *At a party, the number of people who shook an odd number of
hands is even.*

<details>
<summary>Proof</summary>

Sum the handshake counts over everyone at the party. Every handshake involves exactly two
people, so it is counted exactly twice. Therefore

$$\sum_{x} d(x) = 2 \cdot (\text{number of handshakes})$$

which is even.

Split the sum into people with even count and people with odd count. The even-count part
is a sum of even numbers, so it is even. Therefore the odd-count part is even too.

A sum of odd numbers is even exactly when there is an even number of terms. So the number
of people with an odd handshake count is even. ∎

</details>

Now the point of the exercise. Write down what you had to *assume* that you never said:
handshakes are symmetric; nobody shakes their own hand; the party is finite. Those three
lines are the difference between the blackboard proof and the formal statement. That gap
is Kontorovich's arrow number two.

### 6.2 Run the Lean demo (15 minutes, no install)

Open <https://live.lean-lang.org> and paste the reconstructed `const_lim` proof from §4.4.
Then, deliberately, break it:

1. Delete `intro n hn`. Read the error and the goal state.
2. Change `use 1` to `use 0`. It still works — see why.
3. Delete the hypothesis `hyp` from the theorem statement. Watch what becomes unprovable.

Step 3 is the experiment that matters. It is the same operation as the "exponent 11 → 10"
trick from §4.13, at toy scale: change a hypothesis, and let the compiler tell you exactly
where the argument depended on it.

---

## 7. What is actually useful to you

Four transferable items, in order of value.

### 7.1 Cliff versus elevator — the diagnostic for your own harness

Kontorovich's sharpest idea is that "prove this theorem" and "build a library" are
**misaligned objectives**, not different difficulty levels. An agent asked for the result
will always take the cheapest path to that result, and the cheapest path is almost never
the reusable one.

Applied to your work: every skill, plugin, and script you generate is a cliff-scramble
unless something explicitly does the canonization pass. Nothing in the loop rewards
generality, so nothing produces it. This is why a large pile of working automation can
still fail to compound.

The diagnostic question is his X versus X′ test: **do I have two things that are nearly
the same, with separate accumulated machinery around each?** If yes, the canonization is
overdue, and it gets more expensive with every theorem you add on either side.

### 7.2 Prove-and-disprove as a spec check

Steal this directly. AlphaProof searches for a proof of a statement *and* its negation at
the same time. That was built for speed. Its real value turned out to be catching
**translation errors**: if the system disproves your `have` statement, your statement is
wrong, not the mathematics.

The pattern for you: when you hand an agent a specification, also ask it to construct a
counterexample to that specification. A successful counterexample means your spec is
wrong. This catches the exact failure mode you already have — an agent that satisfies a
requirement you did not intend to write.

### 7.3 The scaffold-then-fill pattern

The Translator does not write a proof. It writes the *statement* plus a skeleton of `have`
steps, every one `sorry`'d out. That skeleton compiles. Only then does the Closer fill the
holes.

The value is that the structure is validated before any of the expensive work happens, and
each hole is independently checkable. It is the formal-methods version of writing the
function signatures and the assertions first. For agent orchestration it means the
Decomposer's output is *verifiable as a shape* before you spend a Solver on it.

### 7.4 The formalization factor as a general adoption test

The reusable idea is not about Lean. It is: **a rigorous practice gets adopted when its
time cost relative to the sloppy alternative drops below 1, and not before — and then it
gets adopted with no persuasion at all.**

That reframes advocacy as an engineering problem. LaTeX did not win on argument. It won
when the ratio crossed 1 around 1990. And it won partly for a reason nobody predicted: it
turned out to be an *organizational* tool for the research process, not a typesetting
tool. The second-order benefit was the real one.

Apply the test to anything you are deciding whether to adopt or to build: measure the
ratio, and look for the second-order benefit that is not the stated purpose.

---

## 8. Where to read next

1. **Kontorovich, *The Shape of Math To Come*.**
   [arXiv:2510.15924](https://arxiv.org/abs/2510.15924) — 22 pages, 16 figures. The
   written version of this talk, with the four-agent architecture and the Rudin worked
   example in full. Read §8 and §9 if you read nothing else.
2. **Wiedijk, *The De Bruijn Factor*.**
   [PDF](https://www.cs.ru.nl/~freek/factor/factor.pdf) — short. The measured version of
   the number Kontorovich quotes rhetorically.
3. **Gowers, *Rough Structure and Classification*** (Visions in Mathematics, GAFA 2000
   special volume). The 1999 essay he closes on; his §2 quotes a snippet of it.

To try it rather than read it: <https://live.lean-lang.org>.

---

## 9. Self-test

<details>
<summary>1. What does ε > δ mean, and why is it the central problem?</summary>

ε is the exponential growth rate of research mathematics; δ is the exponential growth rate
of Mathlib. Since ε > δ, the library falls further behind forever, so a researcher can
never build on it in their own field. Everything else in the talk is a response to this.
</details>

<details>
<summary>2. Why is an AI that writes 99 correct papers out of 100 nearly useless to him?</summary>

He does not know which one is wrong. His day becomes hunting for a defect that is almost
never present. The value of output is gated by the cost of verifying it, not by its
accuracy rate.
</details>

<details>
<summary>3. What is the mechanism he proposes for why models weaken theorems?</summary>

They are trained to save tokens. On a hard theorem, the cheapest way to save tokens is to
prove an easier theorem — so they add hypotheses, weaken goals, or smuggle assumptions
into structures.
</details>

<details>
<summary>4. Why does LLM formalization fail to grow the library?</summary>

It is "MacGyver" — local, ad hoc, built to reach one target. Proving a theorem and building
a library are misaligned objectives. Correct-but-unreusable output does not raise δ.
</details>

<details>
<summary>5. What is canonization, and what is the X versus X′ failure?</summary>

Canonization is finding the most general, most reusable statement and placing it correctly
in the library. The failure: prove 1000 theorems about X and 1000 about X′, then discover
they are the same object. You should have generalized first. Mathlib's definition of a
*group* took about seven iterations.
</details>

<details>
<summary>6. Define the Knuth factor and the formalization factor. What happens at 1?</summary>

Knuth factor: time to develop and document with LaTeX ÷ time to do it by hand. It crossed
below 1 around 1990 and adoption followed with no coercion. Formalization factor: time to
discover and formalize ÷ time to discover and write up in LaTeX. When it crosses 1,
everyone switches voluntarily. His estimate is 5–10 years for many core areas.
</details>

<details>
<summary>7. Why does the Riemann zeta function have a junk value in Lean?</summary>

Lean functions are total. ζ : ℂ → ℂ must return something at its pole s = 1, so the
definition produces an arbitrary value there. Formal statements must be written so the junk
value cannot leak into the conclusion. Found by Loeffler and Stoll while formalizing
L-functions for Mathlib.
</details>

<details>
<summary>8. What did AlphaProof's search-both-directions feature turn out to be good for?</summary>

Catching translation errors. If the system disproves a scaffolded `have` statement, the
statement is wrong — usually a hypothesis was omitted — rather than the mathematics being
wrong.
</details>

---

## 10. Note on the tutorial process

I placed Kontorovich in **Tier 3 (far from your background)** based on his known field:
analytic number theory, Zaremba's conjecture, Apollonian circle packings, thin groups.

The talk has nothing to do with any of that. It is Tier 1–2 material and sits directly in
your working domain.

**Correction to the plan:** for the remaining 19 talks, tier and anchor get assigned after
reading the talk's actual content, never from the speaker's reputation. I will check each
title and first minutes before committing to a difficulty rating.

**On sources:** this talk was unusually kind to a transcript-based approach, because
Kontorovich narrates every slide aloud. Most of the remaining talks will not be. Every one
gets the arXiv-paper check that found `2510.15924` here.

**Reconstructed content in this document:** the Lean code in §4.4 (rebuilt from spoken
narration, verifiable at live.lean-lang.org) and the Mathlib halo diagram in §4.7. The
paper's Figure 7.2 shows the real Lean syntax; Figures 8.1 and 8.4–8.5 show the four-agent
schematic and the scaffolds.
