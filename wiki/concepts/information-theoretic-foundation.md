---
title: Information-Theoretic Foundation
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [information-theory, error-correction, domain, surprise, open-question]
sources: [raw/articles/de-readme.md, raw/papers/von-neumann-probabilistic-logics-1956.md]
confidence: medium
---

# Information-Theoretic Foundation

The rationale the author gives for why decision engineering should work. The von Neumann
source now supports the error-control mechanism, but its application to decision engineering
remains analogical and untested.

**Defined in glossary:** Surprise, Decision entropy. None of the information-theory vocabulary
on this page appears in `GLOSSARY.md`.

## The origin question

The framework started from: *can I measure an agent's level of understanding of a codebase?*

The proposed test was to have the agent predict the token cost of meeting a requirement during
planning, then measure the delta against actual usage after implementation. The delta would be
the surprise the agent failed to account for. Drive the delta to zero and the agent would
demonstrably understand the system well enough to predict the cost of changing it.

**This was built, tested, and abandoned.** Too many variables fed the prediction, including the
model and thinking level, and the agent's explanations for deltas were often unverifiable.
Worth preserving: the abandoned metric is the ancestor of both **Cost of Next Change** and the
undefined **repair radius** in [[domain-boundaries]].^[raw/articles/de-readme.md]

## What von Neumann actually establishes

[[john-von-neumann]] starts with physical logical components that each have a probability
`epsilon` of malfunction. Without control, errors accumulate along long stimulus-response
chains. In his memory example, the probability of retaining the original state tends toward
one-half: the result becomes not merely wrong but irrelevant.^[raw/papers/von-neumann-probabilistic-logics-1956.md]

He analyzes two control architectures:

| Architecture | Control mechanism | Bound and cost in the paper |
|---|---|---|
| Single-line replication | Triplicate a network and take majority outputs | The heuristic improvement requires `epsilon < 1/6`; the rigorous construction shown requires `epsilon < .0073` and grows roughly as `3^logical-depth`, which the paper calls impractical |
| Multiplexing | Replace each signal with a large bundle; follow each executive operation with a restoring operation that pushes the bundle back toward a stable extreme | In the paper's specific calculation, component error must be below `.0107`; with `epsilon = .005`, exacting examples require bundles on the order of 20,000 lines |

The exact numbers belong to the paper's particular organs, independence assumptions, and
construction. The durable architectural result is conditional: reliable behavior can be
synthesized from unreliable components when component error is bounded, redundancy is large
enough, and restorative operations are interleaved with the operations that degrade the
signal.^[raw/papers/von-neumann-probabilistic-logics-1956.md]

## The restoring-operation insight

The paper does not merely add redundancy. It separates two roles: an **executive organ** performs
the intended logical operation, while a **restoring organ** erases the degradation introduced by
executive work. Restoration also depends on errors being sufficiently independent; the paper
explicitly calls its constant, history-independent error model unrealistic.

The closest decision-engineering analogue is not a domain boundary by itself. A boundary can
localize damage, but something still has to restore agreement: verify an implementation against
its decision, regenerate a projection from its authority, or reject a state that violates an
invariant. See [[authority-and-projection]] and [[decision-ledger]]. This is an inference from the
paper, not a result the paper tests.

## Structural parallel

| Probabilistic automata | Decision engineering |
|---|---|
| A logical state must survive noisy physical components | Human intent must survive implementation and repeated agent work |
| Executive operations can degrade the represented signal | Changes can introduce hidden, duplicated, or stale decisions |
| Restoring organs repeatedly push the signal back toward a stable state | Verification and regeneration must repeatedly reconcile artifacts with their authority |
| Reliability holds only within an explicit error model and below model-specific bounds | The framework still lacks an error unit, rate, threshold, and measured restoration capacity |

## Corrections to the README's framing

- The cited paper is about probabilistic automata and neural-style logical networks, not
  specifically von Neumann's cellular automata.
- There is no single generic threshold in the paper. It derives several construction-specific
  bounds; the useful lesson is that a bound must be tied to an explicit component and error model.
- “Remove errors faster than they accumulate” is a fair synthesis of restoration, but not a
  sufficient design criterion until the framework identifies what performs restoration and how
  its capacity is measured.

## What remains missing in decision engineering

- No unit defines one decision error, so there is no error rate.
- No mechanism measures whether verification removes drift faster than agent work creates it.
- No threshold separates a recoverable domain from one whose decisions have become irrelevant.
- The framework says a domain is the unit of error correction, while the paper restores after
  individual executive operations. The right cadence and granularity remain open.

## Cited sources

- [[john-von-neumann]] — *Probabilistic Logics and the Synthesis of Reliable Organisms from
  Unreliable Components*; 1952 lectures, published 1956; ingested in
  `raw/papers/von-neumann-probabilistic-logics-1956.md`
- `raw/articles/de-readme.md` — the decision-engineering rationale that invokes the paper

## Related

[[decision-engineering]] · [[domain-boundaries]] · [[decision-entropy]] · [[decision-ledger]] ·
[[authority-and-projection]]
