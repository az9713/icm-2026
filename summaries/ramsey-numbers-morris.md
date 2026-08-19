---
title: "Some Recent Results in Ramsey Theory"
speaker: Robert Morris (IMPA)
source: https://www.youtube.com/watch?v=McbrzDd7hCg
video_id: McbrzDd7hCg
channel: Simons Foundation
event: ICM 2026 Plenary Lecture
date: 2026-08-17
paper: https://arxiv.org/abs/2601.05221
transcript: ../transcripts/McbrzDd7hCg_transcript.txt
difficulty_for_you: 2/5 (the tools) — 3/5 (the culture, and one genuinely new method)
reading_time: ~65 min
---

# Some Recent Results in Ramsey Theory — Robert Morris

**Field:** graph Ramsey numbers. Not extremal combinatorics broadly, not hypergraph
containers, not bootstrap percolation — all of which Morris is known for. One family of
numbers, R(ℓ, k), and what has happened to the bounds on them in the last four years.

**Difficulty against your background: split.**

- **The mathematics: 2 out of 5.** Almost every tool in this talk is one you already own.
  First-moment arguments. The union bound. Chernoff. Concentration of measure on the
  sphere. Martingales. Greedy algorithms and their failure modes. The Lovász Local Lemma
  is one definition away. The single genuinely new method — the *container method* — has
  a proof that is a greedy algorithm you could write on a napkin.
- **The culture: 3 out of 5.** This is the real gap, and it is not technical. Extremal
  combinatorics reasons in a way analysis does not. There is no space to take limits in,
  no operator to spectrally decompose, no PDE to well-pose. Instead there is a
  century-long conversation in which the *same* two numbers get pushed toward each other
  by a sequence of increasingly clever tricks, and where the object of study — a
  "random-like" colouring — has no definition anyone is happy with. §4 is about that.

**One object I will not teach:** the *Hermitian unital*. It is finite projective geometry
over 𝔽_{q²} and teaching it properly would take a chapter you do not want. I state what it
provides, why that is exactly what was needed, and stop. Morris does the same from the
podium ("I'm sorry I don't have a picture of this").

**What this tutorial builds:** the colouring↔graph dictionary that makes the whole subject
readable; the deletion method; the semi-random (nibble) method; blow-ups; pseudorandomness
and jumbledness; the container method; and the *book algorithm* that produced the 2023
diagonal breakthrough. Every symbol is defined before use.

**Note on sources.** Both documents exist and they cover the same ground.

- **The talk.** 56 minutes, uploaded 17 August 2026. The YouTube title is the generic
  "ICM 2026 Plenary Lecture - Robert Morris" — the lecture's own title is not in the video
  metadata, so I use the survey's title.
- **The companion.** [arXiv:2601.05221](https://arxiv.org/abs/2601.05221), Robert Morris,
  *Some recent results in Ramsey theory*, submitted 8 January 2026, 37 pages, 2 figures.
  **Caveat on how this was confirmed as the proceedings paper:** the arXiv comment field
  says only "37 pages, 2 figures" and never mentions ICM. The identification rests on an
  exact title match against the SIAM proceedings chapter list, plus the fact that the
  abstract enumerates precisely the five results the talk covers. Treat it as the
  proceedings paper with that caveat noted.
- **Where they differ, I say which one I am quoting.** They differ in one important place:
  the talk contains a result from **May 2026** that the January paper cannot contain
  (§5.6). It also *omits* three long technical sections the paper has (§§5–7 of the paper),
  which I compress rather than import.

**Names.** The auto-captions destroy essentially every proper noun in this talk — it is a
talk about Hungarians, Brazilians and Britons, delivered by an Englishman in Rio. Every
name below is verified against the paper's bibliography or against the primary paper. The
correction table is in §12.

---

## 1. What is at stake

Colour every edge of a complete graph on n vertices red or blue, any way you like. Ramsey
proved in 1929 that if n is big enough, you cannot avoid a monochromatic clique on k
vertices — k points with *all* the edges between them the same colour.

**R(k)** is the smallest n that forces this. Two bounds, both from the 1930s–40s:

$$2^{k/2} \;\leqslant\; R(k) \;\leqslant\; 4^{k}$$

The upper bound is Erdős and Szekeres (1935). The lower bound is Erdős (1947). Both proofs
are about half a page. You will see both in §5.

And then **nothing happened for eighty years.** Not "slow progress" — the base of the
exponential did not move at either end. Improvements existed, but they were sub-exponential
factors sitting on top of 4^k and √2^k.

That is the first thing to absorb, because it is unlike anything in your training. In
numerical analysis, a factor-of-2 gap in a constant is a nuisance. Here a factor of 2 *in
the base of an exponential* is a chasm that consumed the careers of the best combinatorial
minds of the twentieth century, and it is still not closed.

**Why anyone should care beyond the number itself.** Morris states it once, plainly, and
the survey repeats it in the introduction:

> the problem "exposes a serious gap in our understanding of 'random-like' (or
> pseudorandom) graphs and colourings."

The lower bound 2^{k/2} comes from flipping a coin for every edge. Eighty years of effort
have not beaten a coin flip by more than a constant. Nobody can construct anything more
random-looking than randomness, and nobody can prove that randomness is optimal. The
Ramsey number is a thermometer for that ignorance.

**What changed.** Since 2023:

| Quantity | Old | New | Who |
|---|---|---|---|
| R(k), upper | 4^k | (4−ε)^k, ε ≈ 1/5 | Campos–Griffiths–Morris–Sahasrabudhe; optimised by Gupta–Ndiaye–Norin–Wei |
| R_r(k), upper (r colours) | r^{rk} | e^{−δk} r^{rk} | Balister–Bollobás–Campos–Griffiths–Hurley–Morris–Sahasrabudhe–Tiba |
| R(3,k), lower | (1/4+o(1)) k²/log k | (1/2+o(1)) k²/log k | Campos–Jenssen–Michelen–Sahasrabudhe, then Hefty–Horn–King–Pfender |
| R(4,k), lower | k^{5/2+o(1)} | ck³/(log k)⁴ | Mattheus–Verstraëte |
| R(ℓ,k), lower, all ℓ | k^{(ℓ+1)/2+o(1)} | Ω(k^{ℓ−1}/(log k)^{2ℓ−4}) | Bradač (May 2026 — talk only) |
| R^{ind}(H), upper | k^{O(k)} | 2^{Ck} | Aragão–Campos–Dahia–Filipe–Marciano |

Six long-standing barriers, all in about thirty months. Morris's framing of *why* this is
one story and not six is the actual content of the lecture: each breakthrough re-used the
idea from the previous one, often in a setting nobody predicted.

---

## 2. Your anchor

Morris hands you three, and I am going to use all three rather than invent a fourth. The
last one is the strongest and it is also the talk's biggest open problem.

### 2.1 The probabilistic method *is* the first moment method

You know this from probability, and you will recognise it immediately, but it is worth
saying exactly what the correspondence is because the whole subject is built on it.

Erdős's 1947 lower bound, in full:

> Let X be the number of monochromatic k-cliques in a uniformly random red/blue colouring
> of K_n. If **E**[X] < 1, then since X is a non-negative integer, **P**(X = 0) > 0. So some
> colouring has none. So R(k) > n.

That is a first-moment / union-bound argument and nothing more. Morris says it from the
podium in exactly those terms: *the expected number is a non-negative integer, and if the
average is strictly less than one it must be zero sometimes.*

This matters because it tells you where the field's difficulty lives. First moments are
easy. The entire subsequent history is a search for ways to keep the first-moment argument
alive while making the underlying random object *less* random — because pure randomness
has already been squeezed dry.

The Lovász Local Lemma, which gives the factor-of-2 improvement in §5.9, is the standard
refinement: instead of a union bound over all bad events, you exploit the fact that each
bad event (a monochromatic clique on a specific k-set) is independent of all but a
controlled number of the others. If you have not met it, that one sentence is the whole
idea.

### 2.2 High-dimensional geometry, three times

Morris flags this explicitly and calls it surprising: *"this is the first time, very much
not the last time, that high-dimensional geometry will make an appearance in this talk and
in Ramsey theory in general."* It appears three times, and each is something you own.

1. **Erdős 1957** builds a colouring by throwing n points at random onto a
   high-dimensional sphere and colouring a pair red when the angle between them exceeds
   2π/3. Why no red triangle: three unit vectors pairwise at angle strictly greater than
   2π/3 would have all three pairwise inner products below −1/2, and then
   ‖u+v+w‖² = 3 + 2(⟨u,v⟩+⟨u,w⟩+⟨v,w⟩) < 3 − 3 = 0, which is impossible. Why no large blue
   clique: **concentration of measure** on the sphere. A blue clique is a set of points
   pairwise within angle 2π/3, which lives in a cap, and caps carry exponentially little
   measure. That is a statement you could have made in a statistical mechanics course.
2. **Campos–Jenssen–Michelen–Sahasrabudhe (2026)** improve the R(3,k) lower bound using
   tools they had built for a completely different purpose: their improvement to the best
   known **sphere-packing density** in high dimensions. Morris flags this as "perhaps quite
   surprising".
3. **The book algorithm's key lemma** (§6) is a statement about r arbitrary maps from a
   finite set into ℝⁿ and the correlations between inner products of their images. It is a
   pure high-dimensional probability statement, proved by a moment-generating-function
   positivity argument. Morris calls it "the only really technical slide in the talk" and
   also says its proof is "relatively short, just sort of two three pages".

### 2.3 The best anchor: the solution space fragments

This is the one to keep. It is the talk's *final* slide, it is the field's central open
problem, and it is verbatim your statistical mechanics.

The upper bound R(3,k) ≤ (1+o(1))k²/log k comes from a greedy algorithm: build a large
independent set by repeatedly grabbing a random available vertex and deleting its
neighbours. Shearer's 1983 analysis takes that method to its exact limit. Everyone believes
the truth is a factor of 2 better. Here is Morris, from the podium, on why nobody can get
it:

> "greedy should get stuck about halfway through the process just because at that point a
> typical independent set is maximal, but we don't know how to do that — and really,
> there's work in statistical physics showing that the solution space fragments at this
> point in some complicated way, and so greedy is not going to work, and you really need to
> find some way to explore this very complicated fractal space in a clever way."

You have seen this exact picture. It is the clustering / replica-symmetry-breaking
transition. Below the transition, the set of solutions is one connected blob and local
search finds it. Above it, the solution space shatters into exponentially many far-apart
clusters, each locally maximal, and every local algorithm gets trapped in one. This is the
same phenomenon that makes random k-SAT hard above its clustering threshold, and the same
phenomenon behind the "overlap gap property" barrier for local algorithms on spin glasses.

So the sharpest one-sentence statement of the field's frustration is:

> **The Ramsey problem is stuck exactly where a physicist would predict a glass transition,
> and the tools to get past a glass transition do not exist.**

That is not decoration. Morris names the mechanism, names the field it comes from, and
declares improving either bound "a major breakthrough".

**A fourth, weaker anchor, which I flag as weak.** The random processes in §5.4 (the
triangle-free process, the nibble) are analysed by the *differential equation method*: write
the expected one-step change of each tracked statistic, treat the family as a system of
ODEs, solve, and prove martingale concentration around the solution. That is Wormald's
method and it is genuinely your ODE-plus-probability background. **But Morris never says
this from the podium and the survey does not spell it out** — the survey only says the
proofs involve "the careful control of several large families of random variables that
interact with one another in complex ways". I include it because it will help you read the
literature; do not attribute it to the talk.

---

## 3. The bridge, part one: the dictionary

Nine definitions. Take twenty minutes on this section and the rest of the document reads
like ordinary mathematics.

**Graph.** A finite vertex set V and a set of unordered pairs (edges). K_n is the
*complete* graph: all pairs present.

**Clique.** A set of vertices with all pairs joined. K_k means a clique on k vertices.

**Independent set.** A set of vertices with *no* pair joined. Write **α(G)** for the size
of the largest independent set in G. Write **Δ(G)** for the maximum degree, **d(G)** for the
average degree.

**The dictionary — this is the whole trick.** A red/blue colouring of E(K_n) *is* a graph.
Let G be the graph of red edges. Then:

| Colouring language | Graph language |
|---|---|
| red K_ℓ | clique of size ℓ in G |
| blue K_k | independent set of size k in G |
| "no red triangle" | G is triangle-free |
| "no blue K_k" | α(G) < k |

So **R(ℓ,k) > n** if and only if there exists a K_ℓ-free graph on n vertices with
α(G) < k. That single equivalence converts every question about colourings into a question
about one graph, and it is why the entire literature talks about triangle-free graphs with
small independence number rather than about colourings. Internalise it now; every
construction below is stated in graph language.

**Ramsey numbers.**
- **R(ℓ,k)**: smallest n such that every red/blue colouring of E(K_n) has a red K_ℓ or a
  blue K_k. *Off-diagonal* means ℓ fixed, k → ∞.
- **R(k) = R(k,k)**: the *diagonal* case.
- **R_r(k)**: r colours, monochromatic K_k in some colour.
- **R(3,3,k)**: three colours, avoid a red triangle, a blue triangle, or a green K_k.
- **R^{ind}(H)**: smallest v(G) over graphs G such that every red/blue colouring of E(G)
  contains a monochromatic copy of H that is *induced* in G. Note the base graph is no
  longer required to be complete — you get to design it.

Trivia to fix the definitions, and Morris makes the audience shout these out:
R(1,k) = 1, R(2,k) = k, and R(3,3) = 6. (Exercise 7.1 does the last one.)

**G(n,p).** The Erdős–Rényi random graph: n vertices, each pair present independently with
probability p. Facts you need, both standard: α(G(n,p)) ≈ (2 log(pn))/p, and the number of
triangles is about p³n³.

**Blow-up.** Take a graph H. Replace each vertex by an independent set of size s, and each
edge by a complete bipartite graph between the corresponding two sets. The result has s·v(H)
vertices. Blow-ups have a signature property that turns out to be the pivotal idea of the
last two years: **they have large independent sets, but very few of them.** Any large
independent set must repeatedly reuse whole parts, so the number of such sets is far smaller
than in a random graph of the same density. Hold that thought.

**Pseudorandom / jumbled.** Thomason's 1987 definition. G is **(p,β)-jumbled** if for every
vertex subset U,

$$\Big| e(G[U]) - p\binom{|U|}{2} \Big| \;\leqslant\; \beta|U|.$$

In words: every induced subgraph has about the edge count a random graph of density p would
have, with error at most β per vertex. Chernoff gives β = O(√(pn)) for G(n,p), and
Erdős–Goldberg–Pach–Spencer proved no graph can do better than that. So a graph is called
**optimally pseudorandom** when β = O(√(pn)) — it is as random-looking as anything can be.

The dependence of the whole field on this notion is direct, and §5.6 states the exact
conditional theorem.

---

## 4. The bridge, part two: how this field thinks

This is the part that has no analogue in your training, and it is where most of the
difficulty actually is. Four moves recur. Learn them and the whole talk becomes a sequence
you can anticipate.

### 4.1 Do the stupid thing, then repair it

Morris says this in almost these words about Erdős 1947: *"instead of doing something very
clever and coming up with a complicated construction, he did something that was very stupid.
Very stupid but very clever. He just coloured randomly."*

The pattern generalises into the **deletion method**, and the generalisation is where the
real gains are:

1. Generate a random object with roughly the properties you want.
2. It has some defects (a few red triangles, say).
3. **Destroy the defects by hand**, and bound the collateral damage.

The interesting engineering is entirely in step 3. Morris runs the whole progression on one
slide:

- **Delete a vertex** from each triangle. Costs you nothing in the other direction —
  removing vertices cannot create a larger independent set. But it is wasteful, so you can
  only afford density p ≈ n^{−2/3}. Result: R(3,k) ≳ (k/log k)^{3/2}. (Erdős, 1959.)
- **Delete an edge** from each triangle instead. Far more efficient — now you only need
  fewer triangles than *edges*, which permits p ≈ n^{−1/2}. But removing edges *can* create
  larger independent sets, and controlling that increase is genuinely hard. Erdős did it in
  1961, in a paper Morris calls "way ahead of its time"; it gives R(3,k) ≳ (k/log k)².

Two sentences, one method, one exponent's worth of progress. The gap between those two
bullets is a decade.

### 4.2 Relax "none" to "few"

This is the single most portable idea in the talk, and it is due to Alon and Rödl (2005).

The naive requirement on a construction is: *G must have no independent set of size k*.
That is a hard, brittle constraint. Alon and Rödl replaced it with: *G must have **few**
independent sets of size k* — and then killed the survivors probabilistically. Their lemma
(§5.5) shows that "few" is enough, because you can overlay two independent random copies of
G and a first-moment argument does the rest.

Morris: *"It allows us, instead of having to look for a colouring with zero monochromatic
cliques, to just need to find one with few. And that's a much easier, more flexible task."*

Once you see it, you see it three more times in the talk: in Mattheus–Verstraëte's
R(4,k) bound, in Campos–Jenssen–Michelen–Sahasrabudhe's R(3,k) bound, and in Bradač's 2026
result. It is the reason blow-ups became useful, because a blow-up's defect (large
independent sets) is tolerable exactly when you only need *few*.

### 4.3 Semi-random: choose randomly, but only from what is still legal

The **nibble** or **semi-random method**, introduced by Rödl in 1985 and used by Kim in 1995
for both directions of the R(3,k) problem.

Building an independent set greedily and adversarially is hopeless. Building it *randomly*
is analysable. So: pick vertices at random, one at a time or in small batches ("nibbles"),
but restrict each pick to the vertices that are still available given everything chosen so
far. The process is self-correcting — as you delete neighbourhoods, the remaining graph gets
sparser, so later steps cost less.

The same idea run in reverse builds *colourings*: add red edges one at a time, chosen
uniformly at random among edges that do not complete a red triangle. That is the
**triangle-free process**, suggested by Bollobás and Erdős. Morris ran it to its asymptotic
end with Fiz Pontiveros and Griffiths; the paper is 125 pages. His aside is worth keeping:

> "just lest you think that all of these things are very simple — this actually took well
> over 100 pages."

### 4.4 A gap of a *constant factor* can be a decade of work

You need to recalibrate what counts as progress. In §5.4, the sequence of lower bounds on
R(3,k)/(k²/log k) is:

$$\tfrac14 \;\to\; \tfrac13 \;\to\; \tfrac12$$

Each arrow is a separate paper, and Morris says of the first one: *"It may not seem like
it's a very big deal, but it really felt like — I even conjectured that the quarter was
correct. It really felt like this was the limit."*

The reason those constants matter is that each one encodes a structural claim about how
random-like an object can be. The 1/4 corresponds to "the triangle-free process is the
densest random-like triangle-free graph". Beating it required proving that belief false.

---

## 5. The talk, rebuilt

Morris's order, with the mathematics restored from the survey. He is a good storyteller and
the order is the argument, so I keep it.

### 5.1 The happy ending problem

Frank Ramsey, Cambridge — mathematician, philosopher, economist, logician — proved the
lemma in 1929 inside a paper on logic, and died at 26. The general statement: for any r
colours, any set size s, and any k, if n is large enough then every r-colouring of the
s-element subsets of [n] contains k elements all of whose s-subsets get the same colour.

**The talk restricts to s = 2 and mostly r = 2** for the rest of the hour. Morris returns to
s ≥ 3 only on the final slide (§5.10).

The subject only became a subject because of Esther Klein. In Budapest, a few years later,
she observed that any five points in the plane, no three collinear, contain four in convex
position. Proof: if the convex hull already has four points, done; otherwise the hull is a
triangle with two points inside, and the line through those two points splits the triangle so
that two of its vertices lie on one side — those two plus the two interior points are convex.

Then she asked the right question: for every k, do enough points contain k in convex
position? Paul Erdős and George Szekeres proved yes, by rediscovering Ramsey's theorem and
applying it as follows.

**Colour every 4-subset red if its points are in convex position, blue otherwise.** Ramsey
gives a monochromatic k-set.

- If red: suppose the k points are not in convex position. Then one is inside the hull of
  the others; triangulate the hull; that point sits in some triangle; those four points are
  a *blue* 4-subset. Contradiction.
- If blue: impossible for k ≥ 5, because Klein's observation says every 5 points contain a
  red 4-subset.

Klein and Szekeres married and stayed married for nearly seventy years, dying within an hour
of each other. Hence the name: **the happy ending problem**.

The structural lesson, and Morris draws it deliberately: the colouring was *invented* to
encode a property that had nothing to do with colours. That is what Ramsey theory is for.

### 5.2 The upper bound 4^k, and the factor you are paying

Erdős–Szekeres, 1935:

$$R(\ell,k) \;\leqslant\; \binom{k+\ell-2}{\ell-1}, \qquad\text{so}\qquad R(k) \leqslant \binom{2k-2}{k-1} \approx \frac{4^k}{\sqrt{k}}.$$

Two proofs, and you want both because the second is the one that gets improved in §6.

**Proof 1 (induction).** R(ℓ,k) ≤ R(ℓ−1,k) + R(ℓ,k−1). Take a colouring on
n = R(ℓ,k) − 1 vertices with no red K_ℓ and no blue K_k. Fix any vertex v. It has at most
R(ℓ−1,k) − 1 red neighbours (else find a red K_{ℓ−1} among them, plus v, giving a red K_ℓ)
and at most R(ℓ,k−1) − 1 blue neighbours. Count vertices. Done.

**Proof 2 (the greedy algorithm — this is the one to remember).** Maintain three sets:

- **A**, a red clique;
- **B**, a blue clique;
- **X**, the "reservoir": every edge from A to X is red, every edge from B to X is blue.

Start with A = B = ∅, X = V. Pick any x ∈ X. It has some red neighbours in X and some blue
neighbours in X; take the larger set. If it is red, put x into A and replace X by
N_red(x) ∩ X. If blue, put x into B and replace X by N_blue(x) ∩ X.

Every step adds one vertex to A or to B, and **shrinks X by a factor of at most 2**. After
2k steps, one of A, B has size k. So n > 2^{2k} = 4^k suffices.

Now look at the accounting, because the whole of §6 is an attack on it:

> You pay a factor of 2 on **every** step, whether the step was red or blue. Over 2k steps
> that is 4^k. But a red step only ever helps the red clique. **You are paying in both
> currencies for a purchase in one.**

That observation, made precise, is worth (4−ε)^k.

### 5.3 The lower bound √2^k

Erdős, 1947. Colour each edge red or blue by an independent fair coin flip. Let X be the
number of monochromatic k-cliques.

$$\mathbb{E}[X] \;=\; \binom{n}{k}\,2^{1-\binom{k}{2}}$$

— choose the k-set, then the probability all C(k,2) edges match is 2·2^{−C(k,2)}. If this is
below 1 then some colouring has X = 0. Using C(n,k) ≤ (en/k)^k, the threshold is at
n ≈ √2^k. Hence R(k) ≥ 2^{k/2}.

Morris's emphasis is on what this proof *cost the world*, not what it proved: it is the
origin of the probabilistic method, which he describes as having "infused huge amounts of
computer science and mathematics".

And the contrast that makes it remarkable: constructing an explicit colouring is
brutally hard. Morris sets it as a challenge and warns you off: super-polynomial explicit
bounds are now known, but *"it's really, really not easy even to get k cubed."* Randomness
beats every construction anyone can write down, by an exponential factor. Eighty years on.

### 5.4 R(3,k): seven constructions, ninety years

This is the longest arc in the talk, and it is where the recent excitement is. Under the
dictionary, the question is: **how dense can a triangle-free graph on n vertices be while
keeping α(G) small?**

The answer, as of 2026:

$$\Big(\tfrac12+o(1)\Big)\frac{k^2}{\log k} \;\leqslant\; R(3,k) \;\leqslant\; \big(1+o(1)\big)\frac{k^2}{\log k}$$

**The upper bound.** Ajtai, Komlós and Szemerédi (1981) proved the order of magnitude;
Shearer (1983) found a short, sharp argument and took the method to its limit:

> **Theorem (Shearer, 1983).** If G is triangle-free with n vertices and average degree d,
> then α(G) ≥ (1+o(1)) n log d / d.

Feed a triangle-free graph with no independent k-set into this: triangle-freeness means every
neighbourhood is itself independent, so Δ(G) < k, and the theorem gives
k > (1+o(1)) n log k / k, i.e. n ≤ (1+o(1)) k²/log k.

Why the *log d* is the whole point: a trivial greedy argument gives only α ≥ n/(Δ+1), which
would give n ≤ k². The logarithm is the gain, and it comes from choosing vertices *randomly*
rather than adversarially — the average degree of what remains drops as you go, so later
steps cost less. Morris: *"the basic idea is that if we choose the vertices v randomly, then
the average degree of the graph on the remaining vertices should go down."*

Shearer's proof is an induction on n with an explicitly chosen potential function
f(d) = (d log d − d + 1)/(d−1)², which works because of two calculus identities:
(d+1)f(d) = 1 + (d − d²)f′(d) and f″(d) > 0. That is a clean instance of a move you already
make constantly: guess the right potential and let convexity close the argument.

**The lower bounds — the seven constructions.**

| # | Construction | Bound on R(3,k) | Who |
|---|---|---|---|
| 1 | random points on a sphere, angle > 2π/3 → red | k^{1+c} | Erdős 1957 |
| 2 | G(n,p), delete a vertex per triangle | (k/log k)^{3/2} | Erdős 1959 |
| 3 | G(n,p), delete an **edge** per triangle | (k/log k)² | Erdős 1961 |
| 4 | Kim's nibble | k²/log k, order of magnitude | Kim 1995 |
| 5 | the triangle-free process, tracked to the end | (1/4+o(1)) k²/log k | Fiz Pontiveros–Griffiths–Morris; Bohman–Keevash |
| 6 | **blow-up of G(n,p) as a seed, then nibble** | (1/3+o(1)) k²/log k | Campos–Jenssen–Michelen–Sahasrabudhe, 2026 |
| 7 | **two random blow-ups, overlaid** | (1/2+o(1)) k²/log k | Hefty–Horn–King–Pfender, 2026 |

Rows 1–3 are §4.1. Row 4 is §4.3. Rows 6 and 7 are the new material and are worth spelling
out, because they are the ideas that then propagated everywhere else in the talk.

**Where the factor of 4 was hiding.** The gap between row 5 and Shearer is a factor of 4,
and Morris decomposes it into two independent factors of 2:

- One factor of 2 is the greedy barrier of §2.3 — the gap in Shearer's theorem itself, the
  glass transition, still open.
- The other factor of 2 is a property of the triangle-free process: the graph G it produces
  satisfies α(G) = (2+o(1))·d(G). Its largest independent sets are twice the size of a
  vertex neighbourhood. So there was room, in principle, for a **denser** triangle-free graph
  with the same independence number.

For more than a decade nobody could build one, and Morris and his coauthors conjectured none
existed. He says so on the slide: *"I even conjectured that the quarter was correct."*

**Row 6 — the seed step (Campos–Jenssen–Michelen–Sahasrabudhe).** Do not start the
triangle-free process from an empty graph. Start it from a **blow-up of a sparse random
graph**:

1. Take G(n/s, p) with s = (log n)² and p = √(log n / 6n).
2. That graph has *fewer triangles than edges*, so you can delete them cheaply without
   damaging its pseudorandomness (§4.1 again).
3. Blow it up by a factor of s. Now you have a triangle-free graph on n vertices which has
   large independent sets — but, crucially, **very few of them** (§4.2).
4. Run a nibble on top of the blow-up to add random edges, destroying those few large
   independent sets.

Result: d(G) = (√2/√3 + o(1))√(n log n), α(G) ≤ (√3/√2 + o(1))√(n log n), so
R(3,k) ≥ (1/3 + o(1))k²/log k.

Two side notes Morris makes and I keep. First, they added a **regularisation step** between
nibble steps, which dramatically simplifies the analysis — you may read it as re-projecting
the state back onto the intended trajectory before the next increment, which is a move you
know from numerical integration. Second, the tools came from their own work on **sphere
packing in high dimensions** (§2.2).

**Row 7 — two random blow-ups (Hefty–Horn–King–Pfender).** And now the anecdote, which is
the best two minutes of the lecture. Michelen gave a talk on row 6. Florian Pfender was in
the audience, liked the blow-up idea, was confused by the triangle-free process part, went
back to his hotel, and *in the shower* wondered: what if you skip the process entirely and
just take **two** random blow-ups laid on top of each other? He took it to Hefty, Horn and
King. Not only was the proof simpler — the constant improved from 1/3 to 1/2.

The construction, from the survey:

1. Let H₁, H₂ be independent copies of G(n/s, p), with s = (log n)² and p = √(log n / 4n).
2. Delete an edge from each triangle in each, giving triangle-free H₁′, H₂′.
3. Blow both up to n vertices, giving G₁ and G₂; choose a **random bijection** between their
   vertex sets and take the union G₁ ∪ G₂.
4. Delete an edge from each triangle in G₁ ∪ G₂.

Morris flags exactly why you should not believe this works. G₁ and G₂ are each
triangle-free, but their union is full of triangles — roughly p³n³ ≈ pn² log n of them, far
too many for naive deletion.

**The observation that rescues it.** Every triangle in the union has two edges from one copy
and one from the other. Delete the *minority* edge. Because that edge came from a blow-up, it
is not in one triangle — it is in about s = (log n)² of them. **The triangles come in batches,
and one deletion kills a whole batch.** So the deletion is efficient enough not to inflate the
independence number.

Final result: d(G) = (1+o(1))√(n log n) and α(G) ≤ (1+o(1))√(n log n), giving
R(3,k) ≥ (1/2+o(1)) k²/log k.

Morris's coda on this construction is the most striking claim about research dynamics in the
talk: since it went on arXiv, the same construction has been applied all over the place. In
particular the **odd Hadwiger conjecture** of Gerards and Seymour (1993) was disproved with
essentially the same idea, by Kühn, Sauermann, Steiner and Wigderson
([arXiv:2512.20392](https://arxiv.org/abs/2512.20392)) — they build graphs with no K_t odd
minor and chromatic number at least (3/2 − o(1))t. Morris: *"There are several other problems
in Ramsey theory which are falling one by one to variants of this idea."*

### 5.5 The detour: three colours, and the Alon–Rödl lemma

Morris now does something that is characteristic of the field and worth flagging as a move
in its own right: *to make progress on R(4,k), go and study a different problem.*

The different problem is **R(3,3,k)**: three colours, avoid a red triangle, a blue triangle,
or a green K_k. Erdős–Szekeres gives ≤ k³, and the AKS method improves this to
Ck³/(log k)². The lower bound was stuck at essentially R(3,k) ≈ k²/log k — you can always
just not use one of the three colours. Nobody could prove the obvious: that three colours
is genuinely harder than two.

Alon and Rödl broke it in 2005 with a lemma that is four lines long and, as Morris says,
"simple, beautiful, and surprisingly powerful".

> **Lemma (Alon–Rödl, 2005).** If there exists a triangle-free graph G on n vertices with
> fewer than √(C(n,k)) independent sets of size k, then R(3,3,k) > n.

**Proof.** Let G_R and G_B be two independent random copies of G — apply two independent
random permutations to the vertex set. Colour red the edges of G_R, blue the edges of G_B,
green everything else. No red triangle and no blue triangle, since G is triangle-free.

Now count green K_k's. A set is green-complete exactly when it is independent in G_R *and*
independent in G_B, and those two events are independent. So for each k-set,

$$\mathbb{P}(\text{green } K_k) \;=\; \left(\frac{\#\{\text{independent }k\text{-sets of } G\}}{\binom{n}{k}}\right)^{\!2}$$

and the expected number of green K_k's is C(n,k) times that, which is below 1 exactly under
the hypothesis. First moment. Done. ∎

Notice what the square bought you. Requiring *zero* independent k-sets is impossible for a
dense triangle-free graph. Requiring *fewer than the square root of the total number* is
achievable. Two independent copies convert "few" into "none". That is §4.2 in its purest
form, and Morris identifies it as the idea that eventually unlocked R(4,k).

Applying the lemma to a blow-up of **Alon's 1994 explicit optimally pseudorandom
triangle-free graph** (density n^{−1/3}), plus a counting argument for independent sets,
gives R(3,3,k) ≥ ck³/(log k)⁴ — a full power of k above R(3,k), as expected.

### 5.6 R(4,k), and then all ℓ at once

**Mattheus and Verstraëte (2024)** settled R(4,k) up to polylogarithmic factors:

$$\frac{ck^3}{(\log k)^4} \;\leqslant\; R(4,k) \;\leqslant\; \frac{Ck^3}{(\log k)^2}$$

The upper bound is Ajtai–Komlós–Szemerédi's general R(ℓ,k) ≤ Ck^{ℓ−1}/(log k)^{ℓ−2}. The
lower bound is the breakthrough, and its shape is exactly Alon–Rödl's philosophy plus one
algebraic object.

**The object I will not teach.** The *Hermitian unital*: take the 1-dimensional subspaces of
(𝔽_{q²})³ spanned by points with x^{q+1} + y^{q+1} + z^{q+1} = 0; the vertices of the graph H
are the lines of the projective plane PG(2,q²) meeting that set in exactly q+1 points, and two
lines are adjacent when they meet in one of those points.

What matters is only the output, which is Lemma 4.2 of the survey:

> There is a graph H on n = Θ(q⁴) vertices, Θ(q³)-regular, whose edge set is the disjoint
> union of Θ(q³) **edge-disjoint cliques** of size Θ(q²), such that **every K₄ in H meets one
> of those cliques in at least a triangle**.

That last property is O'Nan's theorem (1972), and it is exactly the miracle. It says all the
K₄'s are *localised* inside the cliques.

**The construction, in three moves:**

1. **Kill the K₄'s.** Since every K₄ has three vertices inside one clique, it is enough to
   replace each clique by a **triangle-free** graph — they use a random complete bipartite
   graph. Call the result H′. Now H′ is K₄-free.
2. **Accept the damage.** H′ has huge independent sets — each side of each complete bipartite
   graph, of size Θ(n^{1/2}). But (§4.2) that is fine if there are few of them.
3. **Count them, then destroy them.** Take a random subset S of the vertices, each included
   with probability p = 1/q, and show the expected number of independent k-sets inside S is
   below 1, with k = q(log q)³.

Step 3 needs a good bound on the number of independent k-sets of H′, and this is where the
one genuinely new method in the talk enters.

**The container method** (Kleitman–Winston 1982; Sapozhenko; and in the general hypergraph
form, Balogh–Morris–Samotij and Saxton–Thomason). The slogan:

> The independent sets of a graph are not spread out. They cluster, and a small number of
> *sparse* sets covers all of them.

Formally (survey Lemma 4.4): if for every U ⊂ V(G) with |U| ≥ R we have e(G[U]) ≥ β|U|², and
R ≥ e^{−βs}n, then G has at most C(n,s)·C(R,k−s) independent sets of size k.

**And the proof is a greedy algorithm you could write in ten lines.** For each independent
set I: repeatedly pick the vertex of maximum degree in the current container; if it is not in
I, drop it from the container; if it is in I, add it to a "fingerprint" set and delete its
neighbours from the container. After s fingerprint additions the container has shrunk below
R. So every independent k-set is determined by a fingerprint of size s (at most C(n,s)
choices) plus k−s elements chosen from a container of size R.

That is a **compression argument**. You are showing that a huge family of objects has small
description length, so a union bound over it becomes affordable. If you have met ε-nets,
covering numbers, or metric entropy in statistical learning theory, this is the same species
of statement: bound the complexity of a class by exhibiting a small cover.

To apply it you need a *supersaturation* input — that every large subset of H′ contains many
edges — which they prove with a martingale argument on the randomness in step 1.

**Then May 2026, and this is in the talk only.** Morris says with evident delight that his
talk had "extremely good timing". For ℓ ≥ 5, the picture had been embarrassing:

$$k^{(\ell+1)/2 + o(1)} \;\leqslant\; R(\ell,k) \;\leqslant\; k^{\ell-1+o(1)}$$

— a *polynomial* gap, because the K_ℓ-free process gives only the exponent (ℓ+1)/2. Everyone
was trying to find algebraic objects analogous to the Hermitian unital for ℓ = 5. Morris:
*"It turned out that the right idea was not to think about ℓ = 5. It was to go back to
ℓ = 3."*

**Domagoj Bradač**, *Off-diagonal Ramsey numbers*,
[arXiv:2605.28793](https://arxiv.org/abs/2605.28793), 27 May 2026:

$$R(\ell,k) \;=\; \Omega\!\left(\frac{k^{\ell-1}}{(\log k)^{2\ell-4}}\right)$$

for every fixed ℓ ≥ 3. That matches the Ajtai–Komlós–Szemerédi upper bound to within
polylogarithmic factors, for **every** ℓ. A ninety-year-old problem, closed to polylog.

> *[Gap — low impact. Morris says explicitly: "unfortunately I don't have time to explain
> his construction to you properly." What he does give: Bradač uses **random blow-ups**,
> inspired directly by the R(3,k) constructions of rows 6 and 7; a simpler geometric
> ingredient than the Hermitian unital, namely the **Alon–Krivelevich** construction placing
> edges between orthogonal vectors in 𝔽_q^d, with linear algebra ensuring no red K_ℓ; and
> then the familiar combinatorial machinery — Alon–Rödl counting of independent k-sets, and
> randomness to destroy them. The mechanism is described at that level and no further. This
> gap is low impact because the *shape* of the argument is exactly the one built up over
> §§5.4–5.6, and the paper is four weeks' reading away. The January proceedings paper
> predates this result entirely and does not mention it.]*

**The conditional theorem that frames all of this.** Mubayi and Verstraëte (2024) proved
that if an optimally pseudorandom K_ℓ-free graph of density Θ(n^{−1/(2ℓ−3)}) exists, then
R(ℓ,k) ≥ ck^{ℓ−1}/(log k)^{2ℓ−4}. The best known such graphs (Bishnoi–Ihringer–Pepe, 2020)
have density only Θ(n^{−1/(ℓ−1)}). So Question 4.7 of the survey — *how dense can an
optimally pseudorandom K_ℓ-free graph be?* — is, in the survey's words, "one of the most
important open problems in graph theory". Bradač reached the conclusion without the
hypothesis; the hypothesis remains open.

### 5.7 Back to the diagonal: what was known

Now the last fifteen minutes, and the return to R(k).

**Upper bound, the pre-2023 chain.** Thomason (1988) → Conlon (2009) → Sah (2023) improved
Erdős–Szekeres to

$$R(k) \;\leqslant\; e^{-c(\log k)^2}\,4^{k},$$

a super-polynomial but sub-exponential saving. Morris makes a point of the by-product rather
than the result: Thomason introduced **quasirandomness** to combinatorics in order to attack
this problem, and quasirandomness went on to become a large field with heavy consequences in
theoretical computer science. The idea being that if the Erdős–Szekeres greedy algorithm is
anywhere close to tight, the colouring must look random-like in specific measurable ways.

Then it stopped. Morris: *"this is basically the limit of what this method can give you."*

**Lower bound.** Erdős's calculation done carefully gives R(k) ≥ (1/(√2 e) + o(1))·k·2^{k/2}.
Thirty years later Spencer (1977) improved it via the Lovász Local Lemma. Morris invites the
audience to spot the difference between the two slides and then spoils it himself:

> "a one became a two."

That is, a factor of exactly 2. **And in the fifty years since, nothing.** Morris is blunt
about what that means: *"even with all of these improvements with the off-diagonal Ramsey
numbers, all these techniques that we developed, we're still completely stuck with the lower
bound. This is really saying there's something that we don't understand about these
objects."*

> *[Gap — low impact. The two constants were on a slide and the captions carry no formulas.
> I have restored them from the standard literature: Erdős's first-moment bound is
> (1/(√2 e))(1+o(1))·k·2^{k/2} and Spencer's Local Lemma bound is
> (√2/e)(1+o(1))·k·2^{k/2}. The survey states neither. The *shape* — a factor of 2, and
> nothing else in fifty years — is what carries the argument, and Morris states that
> explicitly.]*

### 5.8 The 2023 breakthrough, and the better proof

**Theorem (Campos, Griffiths, Morris, Sahasrabudhe, 2023).** There exists ε > 0 with
R(k) ≤ (4−ε)^k for all large k.

The ε was tiny. Gupta, Ndiaye, Norin and Wei then streamlined and optimised the method to
**ε ≈ 1/5**.

Morris then declines to explain that proof, and the reason he gives is the most interesting
methodological remark in the lecture:

> "I'm not going to tell you about our original proof. I'm going to tell you about a second,
> much nicer proof… we weren't really happy with our original proof for various reasons, so
> we continued thinking about it, and we came up with a geometric conjecture."

The survey is blunter about what was wrong with the first proof (§9): it needed a long
opaque calculation to verify it beat Erdős–Szekeres at all, it gave no clean story for
*why*, and it produced a **worse** bound than Erdős–Szekeres in the multicolour case.

The second proof, with Balister, Bollobás, Hurley and Tiba, is shorter, carries a clear
story, extends to r colours, and rests on a geometric lemma with a three-page proof. That is
§6.

### 5.9 Where the multicolour problem stands

**Theorem (Balister, Bollobás, Campos, Griffiths, Hurley, Morris, Sahasrabudhe, Tiba,
2024+).** For each r ≥ 2 there is δ = δ(r) > 0 with

$$R_r(k) \;\leqslant\; e^{-\delta k}\, r^{rk}$$

for all large k. The δ they obtain is polynomial in r — it degrades as colours are added.
Making δ an absolute constant is Conjecture 9.4 of the survey.

The lower bound side is worse. For r ≥ 3, random colourings are no longer the best thing —
you want something more structured — and the best known bounds are c^{rk} for constants
c > 1 (Abbott 1972; improved by Conlon–Ferber, Wigderson, Sawin). Morris: *"the constant is
between something between one and two… the problem is really, really wide open."*

Two smaller multicolour problems he does not mention but the survey highlights, worth
knowing because they are embarrassingly open: R_r(3) = O(r!) via Erdős–Szekeres and nobody
can prove R_r(3) = o(r!); and Erdős's problem of whether R_r(3) ≤ 2^{Cr}.

### 5.10 The closing slide: four open problems

1. **The factor of 2 in Shearer's theorem.** §2.3. The glass transition. Morris's verdict:
   *"an improvement of either of these bounds would really be a major breakthrough."*
2. **Hypergraph Ramsey, s ≥ 3.** Colour *triples* rather than pairs. The bounds are
   single-exponential from below (a random colouring) and **double**-exponential from above
   (a clever old argument of Erdős and Hajnal). Erdős conjectured the double exponential is
   the truth. Morris: *"I don't know if I believe it, but we can't do anything better in
   either direction."*
   > *[Gap — moderate impact. The exponents were on a slide and the captions carry none.
   > Morris himself says "I've ignored constants in the exponents. Apologies." The survey
   > covers only s = 2 and states nothing here. What I can restore honestly is the shape and
   > the lower-bound mechanism: the same first-moment computation as §5.3, with C(k,2)
   > replaced by C(k,3), gives a lower bound of the form 2^{ck²} — this is exercise 7.3. The
   > upper bound is doubly exponential. The gap between 2^{k²} and 2^{2^{k}} is the largest
   > unclosed gap named in the lecture, which is why I rate this moderate rather than low.]*
3. **Induced Ramsey numbers.** Instead of colouring K_n, you get to *choose* the host graph
   G, and you want a monochromatic copy of H that is induced in G. R^{ind}(H) is the smallest
   number of vertices of such a G. Ramsey gives an exponential lower bound; Erdős conjectured
   in the 1970s that exponential is also the truth, for **every** graph H.

   This was proved in 2025 by **Aragão, Campos, Dahia, Filipe and Marciano** — Morris's
   "Marcelo and four very clever young Brazilians in our group at IMPA":

   $$R_r^{\mathrm{ind}}(H) \;\leqslant\; r^{Crk}$$

   for every graph H on k vertices and every r ≥ 2. The mechanism, in one line: show that
   G(n,1/2) itself works for *every* H on k vertices simultaneously, once n ≥ r^{Crk}. The
   difficulty is a brutal union bound — the adversary colours the edges inside a set U after
   seeing the whole graph, so you must beat r^{|U|²} colourings, which forces you to find not
   one copy of H−v but a large, well-distributed *family* of them, maintained through the
   induction. The tool is a new "efficient" hypergraph container lemma of Campos and Samotij,
   and a generalisation that converts global properties (well-distributedness) into local ones
   that containers can handle. Morris calls the proof "extremely intricate"; the survey calls
   it "extremely complicated". Same container idea as §5.6, one level up.
4. **General H, general host.** Ask any of this for graphs other than cliques, and inside
   arbitrary or random host graphs. Wide open.

---

## 6. The one argument: the book algorithm

This is the mechanism behind (4−ε)^k. I follow the survey's §9, which is the second and
better proof, and which Morris presents from the podium.

### 6.1 The idea in one paragraph

Go back to the Erdős–Szekeres greedy algorithm of §5.2 and its accounting problem: the
reservoir X is simultaneously the common **red** neighbourhood of A and the common **blue**
neighbourhood of B, so every step costs a factor of 2 no matter which clique grew. Over 2k
steps, 4^k.

The fix is to maintain, alongside X, a second set for each colour that is only constrained in
*that* colour.

**Definition (book).** A pair (A, Y) is a **red (t,m)-book** if |A| = t, |Y| = m, and every
edge with one endpoint in A and the other in A ∪ Y is red. A is the **spine**; Y is the
**pages**. So A is a red clique, and every page-vertex sees the whole spine in red — but the
pages are completely unconstrained among themselves.

The algorithm maintains, for r colours:

- **X**, the reservoir, as before;
- for each colour i, a clique **A_i** in colour i, and a set **Y_i** such that (A_i, Y_i) is a
  colour-i book.

**The accounting.** Y_i shrinks only on steps that use colour i, so after the algorithm has
put t_i vertices into A_i, the set Y_i has shrunk by roughly p^{t_i} where p ≈ 1/r. Whereas
X, which is constrained in every colour at once, shrinks by ≈ 1/r *every* step. Morris, from
the podium, for r = 2:

> "these Y_i should be much bigger than X. They should be of size 2^{−|A_i|} rather than
> 4^{−|A_i|}."

**The endgame.** Suppose you can produce a monochromatic (t,m)-book with

$$t \;\geqslant\; \delta^4 k \qquad\text{and}\qquad m \;\geqslant\; e^{-\delta t^2/k}\,2^{-t}n \;\geqslant\; R(k-t,\,k).$$

Say the book is red. Its page set Y has m ≥ R(k−t, k) vertices, so inside Y there is either a
red K_{k−t} — which together with the spine A gives a red K_k, since every page vertex sees
all of A in red — or a blue K_k, and you are done either way.

**Why this beats 4^k, in three lines.** Erdős–Szekeres bounds the endgame:

$$R(k-t,k) \;\leqslant\; \binom{2k-t}{k-t} \;\leqslant\; e^{-t^2/6k}\,2^{2k-t}.$$

That exponential factor is just the cost of being off-centre in a binomial coefficient by
t/2. So it suffices to take

$$n \;=\; e^{\delta t^2/k}\cdot 2^{t}\cdot e^{-t^2/6k}\,2^{2k-t} \;=\; e^{(\delta - 1/6)\,t^2/k}\cdot 4^{k}.$$

Choose δ < 1/6. Then with t ≥ δ⁴k the exponent is −ck, and

$$R(k) \;\leqslant\; e^{-ck}\,4^{k} \;=\; (4-\varepsilon)^{k}.$$

**That is the whole story, and it is a good one.** The saving is not a clever cancellation. It
is the observation that the Erdős–Szekeres endgame is *cheaper when it is off-diagonal*, plus
a mechanism (books) for getting far enough off-diagonal to collect the discount. The
"significantly shorter" proof Morris advertises is exactly this: the discount is visible in one
line rather than buried in a calculation.

### 6.2 How the book gets built, and where the geometry enters

At each step you take a vertex x ∈ X and want one of two things:

- **(a) A clique step.** Add x to some A_i without the density of colour-i edges between X and
  Y_i dropping much.
- **(b) A density boost.** Fail to grow the clique, but find large subsets X′ ⊂ X and
  Y′ ⊂ Y_i on which the colour-i density is *substantially higher* than before.

If you can always get one or the other, the algorithm terminates with a good book: the clique
steps build the spine, and the density boosts cannot happen too often because density is
bounded by 1.

Encode the state geometrically. For each colour i, define f_i : X → ℝ^{|Y_i|} by letting
f_i(x) record the colour-i neighbourhood of x inside Y_i, recentred so that the ambient
density is subtracted. Then

$$\langle f_i(x), f_i(y)\rangle$$

measures the **excess overlap** of the colour-i neighbourhoods of x and y inside Y_i. If it is
non-negative, then restricting X to y's with non-negative overlap and shrinking Y_i to
N_i(x) ∩ Y_i does not hurt the density. That is case (a). If the inner products are strongly
negatively correlated across colours, you cannot do (a), and you need (b).

The lemma says you always get one:

> **Lemma (the geometric lemma).** Let U, U′ be i.i.d. uniform on a finite set X, and let
> f₁, …, f_r : X → ℝⁿ be **arbitrary** functions. Then either
>
> $$\mathbb{P}\Big(\langle f_i(U), f_i(U')\rangle \geqslant -1 \ \text{ for all } i \in [r]\Big) \;\geqslant\; \delta \tag{31}$$
>
> or there exist a colour i and a sufficiently large λ > 0 with
>
> $$\mathbb{P}\Big(\langle f_i(U), f_i(U')\rangle \geqslant \lambda\Big) \;\geqslant\; e^{-O(\sqrt{\lambda})}. \tag{32}$$

In words: **either the r inner products are simultaneously non-negative with constant
probability, or one of them has a fat upper tail — a "clustering" of that colour's
neighbourhoods.** The first alternative gives you a clique step on a constant fraction of X;
the second gives you a density boost, at the cost of shrinking X by a factor e^{−O(√λ)}. And
because √λ is *sub-linear* in λ, that shrinkage is affordable relative to the density gain λ.
Morris on the slide: *"the fight is to get this function on the right, e^{−√λ}, smaller than
exponential in λ."*

### 6.3 The proof of the geometric lemma

Two ingredients, and both are things you already own.

**Ingredient 1 — the moments of an i.i.d. inner product are non-negative.** The survey states
this in passing; here is why, because it is the load-bearing fact and it is a two-line
computation.

> **Reconstructed derivation.** For any f : X → ℝⁿ and U, U′ i.i.d.,
>
> $$\mathbb{E}\big[\langle f(U), f(U')\rangle^{\,n}\big] \;=\; \sum_{a_1,\dots,a_n} \mathbb{E}\Big[\prod_j f_{a_j}(U)\Big]\,\mathbb{E}\Big[\prod_j f_{a_j}(U')\Big] \;=\; \sum_{a_1,\dots,a_n} \Big(\mathbb{E}\Big[\prod_j f_{a_j}(U)\Big]\Big)^{2} \;\geqslant\; 0,$$
>
> since U and U′ are independent and identically distributed, so the two expectations are
> equal and the summand is a square. *(Verification: expand the n-th power of the inner
> product as a sum over multi-indices, then use independence to factor each term.)*

This is a positive-definiteness statement, exactly the kind that makes covariance kernels and
Bochner's theorem work. Every moment is a sum of squares.

**Ingredient 2 — a test function with non-negative Taylor coefficients.** Define

$$g(x_1,\dots,x_r) \;=\; \sum_{j=1}^{r} x_j \prod_{i \neq j}\Big(2 + \cosh\sqrt{x_i}\Big), \qquad \cosh\sqrt{x} \;=\; \sum_{n=0}^{\infty}\frac{x^n}{(2n)!}.$$

Read cosh√x by its Taylor series, so it is an entire function of x with all coefficients
positive, and note it grows like e^{√x}. Every Taylor coefficient of g is therefore
non-negative, so by Ingredient 1,

$$\mathbb{E}\Big[\,g\big(\langle f_1(U),f_1(U')\rangle, \dots, \langle f_r(U),f_r(U')\rangle\big)\Big] \;\geqslant\; 0.$$

Now the calculus. The function satisfies

$$g(x_1,\dots,x_r) \;\leqslant\; \begin{cases} 3^r r \exp\Big(\sum_{i} \sqrt{x_i + 3r}\Big) & \text{if } x_i \geqslant -3r \text{ for all } i, \\[4pt] -1 & \text{otherwise.} \end{cases}$$

So g is *negative* off the good region and grows at most like exp(Σ√x_i) on it. Since the
expectation must be ≥ 0, the good region must carry enough mass — either at constant
probability (alternative 31), or one coordinate must have a tail heavy enough to overcome the
deficit, and the e^{√x} growth rate of cosh√x is precisely what makes that tail e^{−O(√λ)}
(alternative 32).

**Read it as a moment-generating-function argument.** You choose a test function whose
positivity is forced by the structure of the random variable, whose *growth rate* encodes the
tail you can tolerate, and you read the dichotomy off the sign of one expectation. That is the
Chernoff/Cramér move with cosh√x in place of e^{tx}, chosen because e^{√x} is exactly the
boundary between "affordable" and "fatal" for this application.

### 6.4 The toy question, and a footnote about the audience

Morris gives a stripped-down version of the same geometry, and it is worth stating because it
is beautiful and because of what happened to it.

> Take a bijection between two copies of the hypercube {−1,1}^n. Pick two uniformly random
> vectors x, y in the first copy. What is the probability that ⟨x, y⟩ ≥ 0 **and** the inner
> product of their images is also ≥ 0?

If the bijection were random, the two events are roughly independent, each of probability 1/2,
giving 1/4. The question is whether an adversarial bijection can **anti-correlate** them —
arrange that whenever one inner product is positive, the other is almost always negative.

Morris and coauthors proved the probability is at least some small constant c. He conjectured
the truth is 1/4. He mentioned it at a PCMI event; **Ijay Narang and Muchen Ju** then proved
the sharp bound 1/4 − O(1/√n)
([arXiv:2509.00716](https://arxiv.org/abs/2509.00716), 31 August 2025), by spectrally
decomposing the Hamming association scheme and turning the problem into a linear program over
the Birkhoff polytope. Morris: *"a very clever, very non-trivial proof."*

You cannot anti-correlate at all. The trivial bound is the truth.

---

## 7. Do this by hand

Three exercises. The first two are Morris's own — he sets them from the podium.

### 7.1 R(3,3) = 6 (fifteen minutes, pen)

Show that every red/blue colouring of the edges of K₆ contains a monochromatic triangle, and
that K₅ has a colouring with none.

<details>
<summary>Solution</summary>

**Upper.** Take a vertex v. It has 5 edges, so by pigeonhole at least 3 have the same colour —
say red, to neighbours a, b, c. If any of ab, ac, bc is red, that edge plus v gives a red
triangle. If none is, then abc is a blue triangle. ∎

**Lower.** On 5 vertices, colour the edges of a 5-cycle red and the edges of the complementary
5-cycle (the pentagram) blue. Each colour class is a 5-cycle, which has no triangle. ∎

Now notice what you just did in the upper bound: you fixed a vertex and looked at the larger
of its two neighbourhoods. **That is exactly the Erdős–Szekeres greedy algorithm of §5.2,
run for one step.** The whole 4^k proof is this argument iterated 2k times, and the "factor of
2" you paid is the pigeonhole step.

Also notice the dictionary at work in the lower bound: the red graph is C₅, which is
triangle-free with α(C₅) = 2 < 3. So R(3,3) > 5, exactly as §3 says it should read.
</details>

### 7.2 The Erdős first-moment bound (twenty minutes, pen)

Derive R(k) ≥ 2^{k/2} from scratch. Colour each edge of K_n red or blue independently and
uniformly. Let X count monochromatic k-cliques. Compute **E**[X], find the n at which it
crosses 1, and state the conclusion.

<details>
<summary>Solution, and the thing to notice afterwards</summary>

For a fixed k-set, all C(k,2) edges match with probability 2·2^{−C(k,2)} = 2^{1−k(k−1)/2}.
By linearity,

$$\mathbb{E}[X] \;=\; \binom{n}{k}\,2^{1 - \binom{k}{2}}.$$

Use C(n,k) ≤ (en/k)^k:

$$\mathbb{E}[X] \;\leqslant\; 2\left(\frac{en}{k}\right)^{k} 2^{-k(k-1)/2} \;=\; 2\left(\frac{en}{k\,2^{(k-1)/2}}\right)^{k}.$$

This is below 1 once n < (k/e)·2^{(k−1)/2}, i.e. n ≈ 2^{k/2} up to a factor linear in k. Since
X is a non-negative integer with mean below 1, **P**(X = 0) > 0, so some colouring has no
monochromatic K_k, so R(k) > n. ∎

**Now the thing to notice.** Track where the two exponentials came from. The C(n,k) is an
entropy term — the number of *places* a bad event can happen. The 2^{−C(k,2)} is an energy
term — the *cost* of each. The threshold is where entropy balances energy, and it sits at
n = 2^{k/2} because C(k,2) ≈ k²/2 while log C(n,k) ≈ k log n.

That is a partition-function calculation and you have done hundreds of them. It is also why
the field's language ("first moment", "second moment", "threshold") reads as statistical
mechanics: it is statistical mechanics, with the Boltzmann factor replaced by a probability
of a colouring coincidence.
</details>

### 7.3 Why hypergraph Ramsey is single-exponential from below (ten minutes)

Repeat exercise 7.2 for **triples**. Colour every 3-element subset of [n] red or blue at
random; let X count k-sets all of whose triples are the same colour. Find the threshold.

<details>
<summary>Solution, and what it tells you about §5.10</summary>

$$\mathbb{E}[X] \;=\; \binom{n}{k}\,2^{1-\binom{k}{3}}.$$

Now C(k,3) ≈ k³/6, and log₂ C(n,k) ≈ k log₂ n. Setting them equal:

$$k \log_2 n \;\approx\; \frac{k^3}{6} \qquad\Longrightarrow\qquad n \;\approx\; 2^{k^2/6}.$$

So the random colouring gives a lower bound of the form 2^{ck²} for the 3-uniform Ramsey
number.

**The point.** The upper bound from the Erdős–Hajnal argument is **doubly** exponential,
2^{2^{ck}}. Compare 2^{k²} against 2^{2^{k}} and you see why Morris calls this "a huge area of
unsolved problems" and why he will not say whether he believes Erdős's conjecture. In the
s = 2 case the corresponding gap was a factor of 2 in the base, and it took ninety years and
this entire lecture to move it. Here the gap is between a polynomial and an exponential *in
the exponent*.

*(This computation is my reconstruction, standard and checkable, not something the survey
states — the survey covers only s = 2. Morris showed a slide with the bounds and said he had
suppressed the constants in the exponents. Verify it against Conlon–Fox–Sudakov's survey,
which the paper recommends.)*
</details>

---

## 8. What is actually useful to you

Seven items, ordered by how far they travel. The first four are, I think, genuinely portable
into how you design and run agent systems; the last three are ways of thinking that will pay
off anywhere.

### 8.1 Relax "none" to "few", then use independence to get back to "none"

The Alon–Rödl lemma (§5.5) is the sharpest transferable idea in the talk.

The pattern: you need an object with **zero** defects, and that is unattainable. So instead
build an object with **few** defects — a much weaker, much more flexible requirement — and
then take two independent copies and overlay them. A defect must survive in *both*, and if
the copies are independent, the failure probability squares. Fewer than √N defects out of N
possible sites becomes zero defects.

Where this shows up in your work: any time you need a generated artefact to be defect-free
and cannot get there directly. Generate an artefact with a bounded defect *count*, generate a
second independently, and require agreement. The squaring is doing the work, and it is doing
it because the two samples are independent — which is exactly the condition you must engineer
and the one that quietly fails when both runs share a prompt, a seed, or a retrieved context.

The same idea appears three more times in the talk (§5.4 row 7, §5.6 steps 2–3, §5.6 Bradač),
which is the strongest evidence that it is a genuine method and not a trick.

### 8.2 Containers: bound the description length, not the count

The container method (§5.6) says: the independent sets of a graph are not spread out; a small
family of sparse "containers" covers all of them, and each independent set is pinned down by a
short "fingerprint" plus a choice inside its container.

The generalisable statement is about **union bounds you cannot afford**. When the number of
bad configurations is astronomically large, do not try to bound the count directly. Show that
every bad configuration has a *short description* — a fingerprint of size s, plus a choice
from a small container — and the union bound collapses to C(n,s)·C(R,k−s).

And the construction of the fingerprint is a greedy algorithm: repeatedly take the highest
degree remaining element; if it is in the object, record it and prune its neighbours; if not,
discard it. That is a **deterministic compression scheme** you could implement in an
afternoon.

For agent work: the shape of the argument is "a huge search space is really a small number of
clusters, and the cluster is determined by a few decisions". When you are tempted to enumerate
a combinatorial space of configurations, the productive question is which small set of
decisions determines the rest.

### 8.3 Track the excess above a baseline, not the raw quantity

Both the near-diagonal proof (Gupta–Ndiaye–Norin–Wei) and the book algorithm are built on a
potential function of the form

$$f_q(X,Y) \;=\; e_B(X,Y) \;-\; q\,|X||Y|$$

— the number of blue edges between X and Y **minus** what a density-q graph would have. The
survey calls the innovation "beautiful": it is sufficient to track only this *excess*, not the
sizes and densities separately.

This is a Lyapunov function, and the design principle is one you know from numerics: subtract
the known leading behaviour and track only the residual, because the residual is what actually
carries the argument and it has far better conditioning. What is new here is the *choice* of
baseline q as a free parameter that you then tune (they set q = 1−p and γ = 1−(√5+1)/2, so
that p² = (1−γ)(q−γ) — the golden ratio appears because that is where the two-move recursion
balances).

The transferable question: **what is the reference against which my quantity should be
measured, and is it a free parameter I could be optimising?**

### 8.4 Know which barrier you are at: greedy, or glassy

§2.3 is the most valuable diagnostic in the lecture.

Morris's own algorithm gets stuck at the point where "a typical independent set is maximal",
and the reason it cannot be pushed further is that the solution space *fragments* there. That
is not a proof-technique deficiency. It is a structural fact about the landscape, and it means
no local algorithm — no amount of cleverness in the greedy rule — will get past it.

The distinction worth carrying:

- **Barrier type A: the analysis is loose.** Better bookkeeping helps. (This is what the book
  algorithm fixed: Erdős–Szekeres was paying twice for one purchase.)
- **Barrier type B: the landscape has shattered.** Better bookkeeping cannot help. You need
  a fundamentally non-local method, and nobody has one.

Morris is explicit that the R(3,k) upper bound is type B and that this is why it has not
moved. Before you spend effort tuning a search procedure, it is worth asking which one you are
looking at — because in the type-B case, the tuning is guaranteed to be wasted.

### 8.5 The best move may be to go back, not forward

The single most striking narrative fact in the lecture. For two or three years, everyone
working on R(ℓ,k) was trying to build algebraic objects for ℓ = 5, because ℓ = 3 and ℓ = 4
were done. Morris:

> "Obviously you've done three and four. Obviously you should think about ℓ = 5. That's the
> way you should think. And it turned out that the right idea was not to think about ℓ = 5.
> It was to go back to ℓ = 3."

The improvement from 1/4 to 1/3 to 1/2 on a case everyone considered finished produced the
construction that then solved every ℓ at once. The obvious next case was the wrong place to
stand.

There is a related instance in the same talk: Morris and coauthors had a proof of the
headline theorem and kept working on it anyway because they were "not really happy with it",
which produced a shorter proof that also extended to r colours — something the original could
not do at all (§5.8).

### 8.6 The failure mode is the resource

The blow-up construction has a *defect*: it has large independent sets. That defect is the
whole reason it works, because it has *few* of them, and few is what you need after §8.1. For
a decade the defect was read as a disqualification.

Similarly, the Hefty–Horn–King–Pfender union of two blow-ups creates far too many triangles —
apparently fatal — and the rescue is that the triangles come in *batches* of (log n)², so one
deletion kills a whole batch. The excess was the mechanism.

The recurring shape: an object is rejected because of a property that looks like damage, and
becomes decisive once someone asks what that property *buys*.

### 8.7 Two documents, one story, and a note about how the field publishes

Small, but worth registering as a reader of technical work. The talk contains a result
(Bradač, May 2026) that the January proceedings paper cannot contain, and the paper contains
three technical sections (the full Ajtai–Komlós–Szemerédi proof, Rödl's path-counting method,
and the Gupta–Ndiaye–Norin–Wei induction) that the talk drops entirely. Neither document is a
superset. Six of the seven headline results in this lecture are cited as arXiv preprints or
"to appear". The frontier of this field is currently on arXiv and nowhere else.

---

## 9. Where to read next

1. **Morris, *Some recent results in Ramsey theory*.**
   [arXiv:2601.05221](https://arxiv.org/abs/2601.05221) — 37 pages. The written version of
   this lecture. Read §§2–4 for the R(3,k) and R(4,k) constructions with full details, and
   §9 for the book algorithm. §§5–7 are the technical material the talk omits and can be
   skipped on a first pass.
2. **Conlon, Fox and Sudakov, *Recent developments in graph Ramsey theory*.** Morris
   recommends this by name as the broad survey his own is deliberately not — decades of
   development, many more results, many more open problems.
3. **Bradač, *Off-diagonal Ramsey numbers*.**
   [arXiv:2605.28793](https://arxiv.org/abs/2605.28793) — the May 2026 result that closes
   R(ℓ,k) to polylog for every fixed ℓ, and the one thing in this lecture that no written
   source yet covers. If you read one primary paper from the talk, this is the one whose
   story is not told anywhere else.

---

## 10. Self-test

<details>
<summary>1. State the dictionary between colourings and graphs, and use it to say what R(ℓ,k) > n means.</summary>

Let G be the graph of red edges of a red/blue colouring of K_n. A red K_ℓ is a clique of
size ℓ in G; a blue K_k is an independent set of size k in G. So R(ℓ,k) > n if and only if
there exists a K_ℓ-free graph on n vertices with α(G) < k. Every construction in the subject
is stated this way.
</details>

<details>
<summary>2. Why does the Erdős–Szekeres greedy algorithm give 4^k rather than 2^k, and what exactly does the book algorithm change?</summary>

The reservoir X is simultaneously the common red neighbourhood of the red clique A and the
common blue neighbourhood of the blue clique B, so it shrinks by a factor of ~2 on **every**
step regardless of which clique grew. Over 2k steps that is 4^k — you pay in both colours for
a gain in one. The book algorithm maintains, for each colour i, a set Y_i constrained only in
colour i, so Y_i shrinks only on colour-i steps: 2^{−|A_i|} rather than 4^{−|A_i|}. That
buys enough to reach an off-diagonal endgame R(k−t,k), which is cheaper than R(k,k) by a
factor e^{−t²/6k} from the binomial coefficient.
</details>

<details>
<summary>3. State the Alon–Rödl lemma and explain in one sentence why the square root appears.</summary>

If there is a triangle-free graph G on n vertices with fewer than √(C(n,k)) independent
k-sets, then R(3,3,k) > n. Proof: take two independent random copies G_R, G_B, colour their
edges red and blue and everything else green; a green K_k must be independent in both, and by
independence the probability squares, so the expected number is C(n,k)·(count/C(n,k))² < 1.
The square root appears because two independent copies square the failure probability.
</details>

<details>
<summary>4. What property of blow-ups makes them the pivotal construction of the last two years?</summary>

A blow-up (each vertex → an independent set of size s, each edge → a complete bipartite graph)
has **large** independent sets but **very few** of them, because any large independent set
must reuse whole parts. Under the Alon–Rödl philosophy, "few" is all you need — so the
property that had disqualified blow-ups for a decade turns out to be exactly what makes them
usable.
</details>

<details>
<summary>5. Why does the union of two random blow-ups not drown in triangles?</summary>

It does have far too many — about p³n³ ≈ pn² log n — but every triangle in the union has two
edges from one copy and one from the other. Delete the minority edge. Because it came from a
blow-up, it lies in about s = (log n)² triangles, not one. The triangles come in batches and
one deletion kills a whole batch, so the deletion is cheap enough not to inflate the
independence number. (Hefty–Horn–King–Pfender, giving R(3,k) ≥ (1/2+o(1))k²/log k.)
</details>

<details>
<summary>6. What does the container method assert, and what is its proof?</summary>

That the independent sets of a graph cluster, and can be covered by a small family of sparse
"containers": every independent k-set is determined by a fingerprint of size s plus k−s
elements chosen from a container of size R, giving at most C(n,s)·C(R,k−s) of them. The proof
is a greedy compression algorithm: repeatedly take the maximum-degree vertex of the current
container; if it is in the set, add it to the fingerprint and delete its neighbours; if not,
drop it. The hypothesis needed is supersaturation — every large vertex set spans many edges.
</details>

<details>
<summary>7. State the geometric lemma behind the book algorithm and say what each alternative buys.</summary>

For i.i.d. U, U′ uniform on a finite X and arbitrary f₁,…,f_r : X → ℝⁿ: either
**P**(⟨f_i(U),f_i(U′)⟩ ≥ −1 for all i) ≥ δ, or for some colour i and large λ,
**P**(⟨f_i(U),f_i(U′)⟩ ≥ λ) ≥ e^{−O(√λ)}. The first alternative gives a clique step on a
constant fraction of X without losing density. The second gives a density boost, shrinking X
by e^{−O(√λ)} — affordable because √λ is sub-linear in the density gain λ.
</details>

<details>
<summary>8. Why are all moments of ⟨f(U),f(U′)⟩ non-negative, and why does that matter?</summary>

Expanding the n-th power over multi-indices and using independence,
**E**[⟨f(U),f(U′)⟩ⁿ] = Σ (**E**[Π_j f_{a_j}(U)])² ≥ 0 — a sum of squares, because U and U′
are i.i.d. It matters because the lemma's proof applies a test function
g(x₁,…,x_r) = Σ_j x_j Π_{i≠j}(2 + cosh√x_i) all of whose Taylor coefficients are
non-negative, so **E**[g] ≥ 0 is automatic; the dichotomy is then read off from the fact that
g is negative outside the good region and grows only like exp(Σ√x_i) inside it. The e^{√x}
growth rate of cosh√x is exactly what makes the tolerated tail e^{−O(√λ)}.
</details>

<details>
<summary>9. Where is the R(3,k) upper bound stuck, and why is the obstruction structural rather than technical?</summary>

At Shearer's bound α(G) ≥ (1+o(1))n log d / d for triangle-free G, which gives
R(3,k) ≤ (1+o(1))k²/log k. Everyone believes a factor of 2 is available. Every known proof
finds a *typical* independent set, and in a random d-regular graph typical sets have exactly
this size while the largest are twice as big. Greedy stalls at the point where a typical
independent set becomes maximal, and work in statistical physics shows the solution space
**fragments** there — the same clustering/glass transition that traps local algorithms on
random constraint-satisfaction problems. So it is a property of the landscape, not of the
proof.
</details>

<details>
<summary>10. Summarise the last three years of R(k) bounds and what remains.</summary>

Upper: 4^k (Erdős–Szekeres 1935) → e^{−c(log k)²}4^k (Thomason, Conlon, Sah) → (4−ε)^k
(Campos–Griffiths–Morris–Sahasrabudhe 2023), with ε ≈ 1/5 after Gupta–Ndiaye–Norin–Wei, and a
second, shorter proof (with Balister, Bollobás, Hurley, Tiba) that also gives
R_r(k) ≤ e^{−δk}r^{rk} for r colours. Lower: 2^{k/2} (Erdős 1947), improved by a factor of
exactly 2 by Spencer in 1977 via the Local Lemma, and **not at all since**. The gap between
2^{k/2} and (4−ε)^k remains a full exponential, and the lower bound has not beaten a coin
flip in eighty years.
</details>

---

## 11. Note on the tutorial process

**Difficulty against the speaker's reputation.** Morris's reputation would predict a hard
talk: hypergraph containers, bootstrap percolation, the triangle-free process, all
technically heavy. The talk is the opposite — he says at the start *"I'm not going to assume
that you know anything about this, I'm going to try to explain everything from the
beginning"*, and he does. He also states his method openly: *"Terry said in his talk that he
emphasised that storytelling is very important. I very much believe this."*

So the reputation over-predicts. But the *content* is narrower than the reputation in a second
way that matters: this is graph Ramsey numbers specifically, not extremal combinatorics
broadly, and not the container method (which appears as a tool, twice, in support of other
people's theorems). The brief's warning was correct and the transcript confirms it.

**Why I split the rating.** The tools are 2/5 — first moments, greedy algorithms,
concentration, martingales, potential functions. The culture is 3/5, and it is the culture
that will cost you time: a subject where a constant factor is a decade of work, where the
central object ("random-like") has no satisfactory definition, and where the only way to
attack a problem is to go and solve a different one. The Bartlett tutorial
(`modern-ml-methods-bartlett.md`) made the same split for the same structural reason —
familiar mathematics inside an unfamiliar frame.

**Name corrections.** The auto-captions destroy nearly every proper noun. All corrections are
verified against the survey's bibliography or against the cited primary paper.

| Caption | Correct |
|---|---|
| Julian Sahaser / Julian Jun | Julian Sahasrabudhe |
| Ba Bolabos / Balabash | Béla Bollobás |
| Esther Klene | Esther Klein |
| George Saresh | George Szekeres |
| Edish / Edush / Ed / air | Erdős |
| Ed securus / Edison Sees | Erdős–Szekeres |
| Edish Highland | Erdős–Hajnal |
| Shira / Sheera | Shearer (J. B. Shearer) |
| Tom and Peter Kash | Bohman and Keevash |
| Gonzalez Bont | Gonzalo Fiz Pontiveros |
| Alan Riddle / Allan and Riddle / Alan and Myrtle | Alon and Rödl |
| Sam Mateos and Jacqu Ratarta | Sam Mattheus and Jacques Verstraëte |
| Onan | O'Nan |
| hermission unit | Hermitian unital |
| Marcelo Campus | Marcelo Campos |
| Yensson, Marcus Michelin | Jenssen, and Michelen |
| Floren Fender | Florian Pfender |
| Hefty Horn and King | Hefty, Horn and King |
| Domaguch | Domagoj Bradač |
| Alan Kurovich | Alon and Krivelevich |
| Thomas / Thomasson | Andrew Thomason |
| David Conlan | David Conlon |
| Ashwin Sar | Ashwin Sah |
| Owen Hurley | **E**oin Hurley (bibliography gives "E. Hurley") |
| Marius Ta | Marius Tiba |
| EJ Narang and Muchin | Ijay Narang and Muchen Ju |
| odd hadwig | odd Hadwiger |
| Marcelo and four young Brazilians | Aragão, Campos, Dahia, Filipe and Marciano |

**Names I could not fully verify:** none remain. Every surname above appears in the survey's
bibliography or in the arXiv record of the cited paper. Two first names are inferred rather
than heard: "Eoin" Hurley (the bibliography gives only "E. Hurley"; I use the surname in the
body text) and "Ijay" Narang / "Muchen" Ju (from the arXiv author list of 2509.00716, not
from the captions).

**Substantive caption errors corrected, not just spellings.**

1. **The book sets.** The captions render the Y_i as "the common red neighbourhood of the red
   clique and the common red neighbourhood of the blue clique". That is garbled and, read
   literally, wrong. The correct statement, from survey §9: (A_i, Y_i) is a **colour-i book**
   — every edge from A_i to A_i ∪ Y_i has colour i, and Y_i is unconstrained in the other
   colours. That asymmetry is the entire mechanism, so getting it wrong would destroy the
   argument. Corrected in §6.
2. **The "silly inequality".** The captions say "3k is just at most R33". The intended
   statement is R(3,k) ≤ R(3,3,k) — obvious, since you can simply not use one of the three
   colours — and the point is that nobody could prove the inequality is far from tight until
   Alon and Rödl in 2005. Corrected in §5.5.
3. **Erdős's 1947 conjecture.** Morris says from the podium that Erdős conjectured already in
   1947 that the Erdős–Szekeres upper bound k^{ℓ−1} is the truth for fixed ℓ. The survey does
   not repeat this attribution, describing the question only as "one of the most important
   open problems in Ramsey theory". I report it as the talk's claim and flag that the paper
   does not corroborate the date.

**Where the mathematics could not be recovered, and how much it costs.**

| Gap | Impact | Note |
|---|---|---|
| Bradač's construction (§5.6) | **Low** | Morris says outright he has no time for it. The ingredients he names — random blow-ups, Alon–Krivelevich orthogonal-vector graphs, Alon–Rödl counting — are exactly the ones built up over §§5.4–5.6, so the shape is recoverable even though the proof is not. The paper is public. |
| The two diagonal lower-bound constants (§5.7) | **Low** | Slide only; captions carry no formulas; the survey states neither. Restored from the standard literature and labelled. The *shape* — a factor of exactly 2 in fifty years — is what carries the argument and Morris states it aloud. |
| Hypergraph Ramsey exponents, s ≥ 3 (§5.10) | **Moderate** | Morris himself says "I've ignored constants in the exponents. Apologies." The survey covers only s = 2. I restored the lower-bound *mechanism* (exercise 7.3) because it is the same first-moment computation as §5.3, and stated the upper bound only as "doubly exponential". This is the largest unclosed gap named in the lecture and it gets one slide, which is why I rate it moderate. |
| Gupta–Ndiaye–Norin–Wei induction (§5.8) | **Low** | Present in the paper (§7) but absent from the talk. I state the result and the one transferable idea (tracking the excess f_q, §8.3) and do not reproduce the calculation, which the survey itself declines to give in full. |

**Reconstructed, and labelled as such in place:**

- The two-line proof that all moments of ⟨f(U),f(U′)⟩ are non-negative (§6.3). The survey
  asserts this without proof; the derivation is mine and is verified by expanding the n-th
  power over multi-indices and using independence.
- The reason 2π/3 is the right angle in Erdős's 1957 sphere construction (§2.2) — the
  ‖u+v+w‖² ≥ 0 argument. The talk asserts triangle-freeness; the survey uses Kleitman's
  hypercube theorem instead of the sphere. Both are legitimate; I give the talk's version with
  the reason supplied.
- The three-line endgame accounting for (4−ε)^k in §6.1 is assembled from the survey's stated
  ingredients (the book condition, the Erdős–Szekeres binomial bound, and δ < 1/6). Each
  ingredient is quoted; the arithmetic joining them is mine.
- Exercise 7.3, the 3-uniform first-moment threshold.

**One source-handling incident worth recording.** The first fetch of
`arxiv.org/html/2601.05221v1` returned a page whose `<title>` was correct but whose body was a
*different* ICM paper entirely (Hee Oh's, on Kleinian groups) — a CDN cache mismatch, with an
`X-Cache: HIT` header. Caught by grepping the downloaded file for "Ramsey" and getting zero
hits. Re-fetching with a no-cache header returned the correct document. Nothing in this
tutorial derives from the bad fetch, but the failure mode is worth knowing: a correct title
tag is not evidence of correct content, and a one-line content grep is a cheap check.
