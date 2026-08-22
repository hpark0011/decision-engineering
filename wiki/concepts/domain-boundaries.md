---
title: Domain Boundaries
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [domain, decision, invariant, fact, ddd, cost-of-change]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md, raw/papers/von-neumann-probabilistic-logics-1956.md]
confidence: medium
---

# Domain Boundaries

**Defined in glossary:** Decision home, Decision locality, Authoritative fact, Invariant, Policy.
Note: "domain" and "repair radius" are used in the README but **not defined in the glossary** —
see Open questions.

## The core claim

> Domain boundaries emerge from decision dependencies, not from nouns or organizational
> categories.

This is the load-bearing departure from how boundaries are usually drawn. Not "User", "Order",
"Billing" — but "which decisions must stay consistent with the same authoritative facts,
meanings, and invariants?"

The definition that follows: **a domain is a boundary within which the information needed to
make its decisions is locally recoverable.**^[raw/articles/de-readme.md]

## The procedure

1. List the key decisions the system has to make
2. For each, write the few facts you truly need and the rule you're applying
3. Group decisions that use the same small set of facts and rules — each group is a domain
4. **Change test:** when one decision changes, do most of the resulting changes stay inside
   that group? If yes, the boundary is probably sound

The change test is the whole method's falsifiability. Everything before it is a hypothesis
about grouping; step 4 is the measurement.

## Stated as a decision about decisions

The README applies the framework to itself, which is the clearest illustration of the
[[anatomy-of-a-decision]] pipeline in the sources:

| Part | Content |
|---|---|
| Requirement | Define domains so surprise is minimized |
| Decision | Do these decisions belong in the same domain? |
| Facts | What each decision needs, which policies apply, which other decisions change when it changes |
| Policy | Group decisions that consistently depend on the same authoritative facts, preserve the same invariants, and follow the same policies |
| Invariant | Each decision belongs to one primary domain; within it, decisions share core facts and must preserve the same invariants |

## Why boundaries matter: localization is not restoration

The stated purpose is to make surprise **local** rather than random. A bounded domain means a
surprise has a small set of possible causes, so it can be diagnosed and fixed before errors
accumulate. The README therefore treats a domain as the unit within which error correction can
outrun error accumulation.

The von Neumann source makes that analogy more demanding. Its multiplexed architecture follows
executive operations with restoring operations; a boundary alone does no correction. Applied
here, locality reduces where repair must look, while verification, reconciliation, or regeneration
from an authority must actually perform the repair.^[raw/papers/von-neumann-probabilistic-logics-1956.md]

This is the link to [[information-theoretic-foundation]] and [[authority-and-projection]]: domain
boundaries can contain the repair surface, but reliability depends on restorative mechanisms
inside those boundaries.

The named failure it prevents: agents solving problems by adding more rules, which produces
hidden couplings and scattered decisions until the system becomes unpredictable. This is the
stated reason vibe coding fails in large codebases. See [[decision-entropy]].

## Open questions

- **"Repair radius" is undefined.** The README says "the way we track this is repair radius" but
  never defines it, and the glossary defines **Cost of Next Change (CNC)** instead. Two names for
  what may be one metric, or two different metrics — unresolved. This is a real single-home
  violation in the sources themselves.
- **The threshold is unstated.** The README asks "how would we define the threshold and what
  would be above and below it?" and does not answer. The paper supplies model-specific thresholds,
  not one transferable threshold; decision engineering still lacks its own error model.
- **The restoring operation is unnamed.** Is it invariant enforcement, verification, regeneration
  of projections, or a combination? Until this is explicit, locality is being asked to do work
  that the source architecture assigns to a separate mechanism.
- **Relationship to DDD bounded contexts** is unexamined. The claim that boundaries come from
  decision dependencies rather than nouns is a direct contrast with how DDD is usually applied,
  and deserves a comparison page.

## Related

[[decision-engineering]] · [[decision-entropy]] · [[information-theoretic-foundation]] · [[anatomy-of-a-decision]]
