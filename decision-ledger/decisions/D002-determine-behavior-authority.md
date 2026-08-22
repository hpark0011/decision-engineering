---
status: active
domain: authority
id: D002
title: "Determine behavior authority"
updated_at: 2026-08-21
---
## Requirement

Observed system behavior must be diagnosed from evidence of what the implementation actually does.

## Question

Which artifact is authoritative for actual system behavior?

## Input facts

- `framework.behavior-observation-requirement`
  - Kind: root
  - Authority: IDEA.md — Code and runtime behavior

## Output fact

- Name: `framework.behavior-authority`
- Meaning: The evidence class that authoritatively establishes actual behavior.
- Shape: `implementation-and-runtime`
- Atomicity: The answer identifies one behavior authority and contains no separate policy choice.

## Invariant

Recorded intent is never presented as proof that the system currently behaves that way.

## Policy

Treat executable implementation and runtime observations as authoritative for actual behavior; use tests and traces as evidence about that behavior, not as substitutes for observing the authoritative path.

## Enforcement

The diagnostic and reconciliation workflow must inspect the relevant implementation or runtime boundary before claiming what the system does.

## Projection

`framework.behavior-authority.public`

Names implementation and runtime evidence as the behavior authority without interpreting whether the behavior is correct.

## Consumers

- D003 — Resolve intent behavior divergence
- D012 — Determine verification target
- Bug diagnosis and implementation review workflows

## Verification

- For a sampled framework behavior, compare the claim with the executable path or a runtime observation.
- Reject a behavior report supported only by ledger prose.
- Confirm tests exercise the same implementation boundary whose behavior they claim to verify.