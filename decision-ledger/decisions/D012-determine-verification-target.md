---
status: active
domain: assurance
id: D012
title: "Determine verification target"
---
## Requirement

Verification must provide evidence about the authoritative policy, invariant, and enforcement path without creating a competing policy.

## Question

Is a proposed verification plan aimed at the authoritative decision path?

## Input facts

- `framework.enforcement-sufficiency`
  - Kind: derived
  - Produced by: D011
- `framework.decision-atomicity`
  - Kind: derived
  - Produced by: D004
- `framework.verification-evidence-requirement`
  - Kind: root
  - Authority: IDEA.md — Verification

## Invariants

Tests exercise the owning policy, invariant, and enforcement boundary rather than comparing behavior with a second copy of the same policy.

## Policy

Return `sufficient` when the plan covers every meaningful policy branch, proves the invariant at the D011 boundary, and exercises rejection paths through the authoritative implementation; otherwise return `insufficient`, including when expected results are independently computed from copied policy.

## Output fact

- Name: `framework.verification-sufficiency`
- Meaning: Whether one verification plan adequately tests an authoritative decision and its enforcement.
- Shape: `{ state: sufficient | insufficient, reason: string }`
- Atomicity: `reason` explains the verification state for one plan and cannot vary independently.

## Enforcement

The ledger and implementation acceptance workflow must reject material behavior whose verification plan is insufficient or targets only a presentation layer.

## Consumers

- D017 — Determine ledger acceptance
- Test authors
- Ledger, implementation, and release reviewers

## Verification

- Review representative branch, invariant, and rejection-path evidence for each active policy.
- Reject a test that duplicates the policy and only proves both copies agree.
- Confirm verification fails when the real enforcement boundary is bypassed or missing.