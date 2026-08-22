---
title: Authority and Projection
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [projection, presentation, ownership, traceability, drift, verification]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md, raw/papers/von-neumann-probabilistic-logics-1956.md]
confidence: medium
---

# Authority and Projection

**Defined in glossary:** Authority, Authoritative fact, Authoritative state, Projection,
Presentation, Stale projection, Traceability, Weak ownership, Decision outcome.

## The rule

Information may be copied freely. **Authority over a meaning may not.**

This single sentence carries most of the framework's practical weight. A projection is a
representation derived from authoritative information for some consumer — API responses, search
indexes, config files, executable skills. Copying is fine in a projection. Independent authority
is not. A projection must stay traceable to its source and must never quietly become a second
owner of the same meaning.

## Authority is not popularity

> Being used in many places does not make something authoritative.

A cached value, a UI label, or a copied rule can have many consumers and still have no
authority. This inverts the usual intuition that the most-referenced thing is the real one —
and it is exactly the mistake the agent made in the launch-email example on
[[decision-engineering]], where recency stood in for authority.

## The projection chain

```text
authoritative fact → decision → outcome → projection → presentation
```

**Projection** serves any consumer; **presentation** serves a human. The state
`task.status = "ready_for_review"` is authoritative, `"Ready for review"` is a presentation of
it. A presentation stays derived. It does not become a second source of truth.

## Traceability closes the loop

Every rule that changes behavior should have a path back:

```text
observed behavior → implementation → policy or invariant
→ decision and authoritative facts → business requirement → intent
```

A rule that traces back to nothing is a hidden decision waiting to be found. Traceability is
therefore not documentation hygiene — it is the detection mechanism for the failures catalogued
in [[decision-entropy]].

## Where it breaks: stale projection

Traceability and verification are what keep projections from going stale unnoticed. Without
them, a projection drifts from its source and silently becomes a competing authority — which is
how a duplicated decision is born from something that started out legitimate. The
[[decision-ledger]] and its derived `SKILL.md` are the worked case.

## Verification as a restoring operation

In [[john-von-neumann]]'s multiplexed automata, executive organs perform the useful operation and
restoring organs repeatedly push degraded signals back toward a stable state. The closest analogue
here is to derive a projection, then verify or regenerate it against its authority before drift can
compound.^[raw/papers/von-neumann-probabilistic-logics-1956.md]

This is an architectural inference, not a claim the paper makes about documents. It does clarify
why traceability alone is insufficient: a path back to authority enables repair, but some active
mechanism must walk that path and restore agreement.

## Activation as a projection

A subtle instance worth noting: for an agent skill, the skill's **description is a projection of
its activation policy** — it tells the agent when the skill applies. That makes description
drift a correctness problem, not a copywriting one. The glossary splits verification to match:
**activation verification** checks whether a capability runs in the right situations,
**behavior verification** checks what it does once running.

## Open questions

- Nothing enforces the copy-but-don't-own rule mechanically. How would a system detect that a
  projection has started deciding for itself?
- The glossary distinguishes trigger from activation policy cleanly, but no source shows how
  activation verification is actually performed.

## Related

[[decision-engineering]] · [[decision-entropy]] · [[decision-ledger]] · [[schema-as-agent-constraint]]
