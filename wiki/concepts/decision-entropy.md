---
title: Decision Entropy
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drift, hidden-coupling, scattered-decision, ownership, cost-of-change, surprise]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md, raw/papers/von-neumann-probabilistic-logics-1956.md]
confidence: medium
---

# Decision Entropy

**Defined in glossary:** Decision entropy, Hidden decision, Duplicated decision, Scattered
responsibility, Hidden coupling, Weak ownership, Stale projection, Cost of Next Change (CNC).

The glossary is explicit that this is an engineering metaphor, not a thermodynamic claim.

## The failure taxonomy

Six named ways decision knowledge decays. They are distinct, and the glossary's distinctions
table exists because they get conflated:

| Failure | Shape | Tell |
|---|---|---|
| Hidden decision | A choice that affects behavior but was never identified or owned | A rule that traces back to nothing |
| Duplicated decision | One question independently answered in 2+ places | UI and backend disagree on when approval is allowed |
| Scattered responsibility | One rule spread across places, no single place determines the answer | Each file holds a piece; none holds the rule |
| Hidden coupling | One part quietly relies on another's decisions or state | Unrelated things break together |
| Weak ownership | Nominal home others can bypass, redefine, or contradict | Documented once, reimplemented three times |
| Stale projection | A derived artifact no longer matches its source | Ledger changed, `SKILL.md` didn't |

## Symptom versus cause

Hidden coupling is called out as usually a **symptom**, not a cause. Underneath it, look for
hidden decisions, duplicated decisions, scattered responsibility, or unclear authoritative
facts. This ordering matters for diagnosis: removing the coupling without finding the unowned
decision underneath just relocates it.

The general relationship: decision entropy is the cause, **surprise** is the observed effect,
and CNC is what you actually feel.

## Error can decay into irrelevance

[[john-von-neumann]] distinguishes an unreliable result from an irrelevant one. In his memory
example, repeated component errors drive the probability of retaining the original state toward
one-half; the system eventually carries no discriminating information about what it was meant to
remember.^[raw/papers/von-neumann-probabilistic-logics-1956.md]

This refines the engineering metaphor. Decision entropy need not produce a consistently wrong
answer. It can produce artifacts whose relationship to the original intent is no better than an
unguarded guess. [[information-theoretic-foundation]] explains why repeated restoration, not only
one-time cleanup, is the relevant control pattern.

## Cost of Next Change as the signal

CNC is the effort to make the next change safely — finding the knowledge, deciding what to
change, making it, checking the result. The glossary positions it as the practical, observable
signal of decision entropy: when ownership is scattered or unclear, searching and checking both
get more expensive.

This is the closest thing the framework has to a metric. It is also unmeasured — see
[[information-theoretic-foundation]] for the abandoned attempt to quantify it via token cost,
and [[domain-boundaries]] for the competing, undefined "repair radius."

## Why it accelerates with agents

The README's mechanism: as features and fixes accumulate, agents tend to solve problems by
**adding more rules**. Each added rule is a candidate hidden or duplicated decision. Hidden
couplings and scattered decisions therefore grow with agent throughput rather than with human
effort — which is why the problem is worse now than it was.^[raw/articles/de-readme.md]

## Open questions

- No detection method is specified. Recursive decision mapping finds hidden decisions when you
  go looking; nothing tells you where to look, or continuously flags new entropy.
- CNC has no unit and no proposed measurement procedure.
- The relationship between duplicated decision and legitimate [[authority-and-projection]] is
  the trickiest one to judge in practice: one authority with many derived copies is fine, two
  independent authorities is the failure. Telling them apart requires knowing which is derived.

## Related

[[decision-engineering]] · [[domain-boundaries]] · [[authority-and-projection]] · [[anatomy-of-a-decision]]
