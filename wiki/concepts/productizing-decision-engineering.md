---
title: Productizing Decision Engineering
created: 2026-08-21
updated: 2026-09-02
type: concept
tags: [decision, ledger, context-engineering, agent-harness, verification, methodology]
sources: [raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md, ../skills/decision-engineering/assets/decision-ledger/SCHEMA.md]
confidence: medium
---

# Productizing Decision Engineering

**Defined in glossary:** Decision Engineering, Decision ledger, Decision, Authoritative fact,
Traceability, Verification.

## Product thesis

The lowest-friction product does not ask people to learn the method or fill in a decision form.
They use an ordinary chat; the system captures decision artifacts as a byproduct. Chat is the
interface. The product underneath is the durable, inspectable decision infrastructure that chat
quietly builds.

The intended “magic” is not seeing a graph. It is changing one requirement or authoritative
fact and immediately seeing the decisions that may need to be revisited. That is where the
dependency structure in [[decision-ledger]] becomes user value rather than documentation.

## Zero-friction chat MVP

```text
ordinary chat
    ↓ event boundary
unprocessed conversation delta
    ↓ extract actual commitments
compare with the current ledger
    ↓
update ledger + append change log
    ↓ occasionally
show “Here is what I recorded” for correction
```

The write path is asynchronous so extraction does not slow the conversation. Useful trigger
events include:

- an idle interval, with ten minutes as an initial heuristic;
- the end of a thread; and
- an explicit “new topic” boundary.

The trigger should process only the delta since the last successful checkpoint. Rescanning the
entire thread on every idle event wastes work and makes duplicate or contradictory entries more
likely. Before writing, the extractor compares candidates with existing decisions and chooses
whether to add, amend, supersede, or ignore them.

## What gets captured

The extractor should record moments of commitment, not every idea mentioned in conversation.
A useful candidate preserves enough reasoning to remain actionable later:

- what was decided;
- why it was chosen;
- which facts were treated as authoritative;
- which other decisions depend on it; and
- what should be revisited if an input changes.

The [2026-09-02 ledger contract](../../skills/decision-engineering/assets/decision-ledger/SCHEMA.md) narrows dependency capture to
declared input and output facts. Separate usage lists from the earlier product discussion are
deferred in the minimal skill.

This is the product-level distinction explored in [[hermes-vs-decision-engineering]]: reusable
procedures make repeated execution easier, while a durable decision record keeps later reasoning
consistent and exposes the impact of change.

## Three product layers

| Layer | User value |
|---|---|
| Passive capture | Decisions accumulate without a separate documentation ritual. |
| Verification | The system asks which facts are authoritative, notices changes, and identifies affected decisions. |
| Guidance | Prior decisions and the required inputs are surfaced when a related choice arises. |

The MVP is primarily passive capture plus a lightweight correction loop. Verification and
guidance are the compounding layers, but both depend on capture producing reliable ledger edges.

## Guardrails for the first version

- Keep extraction off the synchronous chat path.
- Persist a checkpoint so each event handles a bounded delta.
- Make ledger writes idempotent and preserve a chronological log of changes.
- Distinguish commitments from brainstorming, questions, and rejected options.
- Periodically present the captured decisions for human correction rather than interrupting on
  every candidate.
- Treat dependency impact as the payoff: a changed fact should identify what to revisit.

## Distribution

The chat MVP above is one delivery shape. The nearer-term one is shipping the method as
installable agent skills, where the same zero-friction principle applies: the install path
should not ask the user to learn the method first. See
[[plugin-vs-installer-distribution]] for the channel comparison and the prior art.

## Open questions

- What evidence is sufficient to classify an utterance as a commitment?
- How should edits, reversals, and superseding decisions appear in the ledger and log?
- When is silent capture appropriate, and when must the system ask before recording?
- Which review cadence catches extraction errors without recreating the documentation burden?
- How should context be assembled from the decision graph without turning the ledger into a
  generic memory store? See [[compiled-knowledge-base]].

## Related

[[decision-engineering]] · [[decision-ledger]] · [[hermes-vs-decision-engineering]] ·
[[authority-and-projection]] · [[plugin-vs-installer-distribution]]
