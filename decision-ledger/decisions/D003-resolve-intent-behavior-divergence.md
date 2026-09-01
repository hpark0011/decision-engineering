---
status: active
domain: authority
id: D003
title: "Resolve intent behavior divergence"
---
## Requirement

A mismatch between recorded intent and actual behavior must be corrected without silently declaring either side correct.

## Question

When ledger intent and implementation behavior disagree, which side must change?

## Input facts

- `framework.intent-authority`
  - Kind: derived
  - Produced by: D001
- `framework.behavior-authority`
  - Kind: derived
  - Produced by: D002
- `framework.divergence-observation`
  - Kind: root
  - Authority: Human or agent observing a mismatch between ledger intent and implementation behavior

## Invariants

No mismatch is resolved by silently editing code or intent before a human decides which authority is stale or wrong.

## Policy

Present the ledger fact and implementation evidence to a human; select `change-intent` when intended policy has changed, otherwise select `fix-behavior` when implementation diverges from adopted intent, and retain the adjudication rationale.

## Output fact

- Name: `framework.divergence-resolution`
- Meaning: The human-adjudicated correction direction for one observed intent-behavior mismatch.
- Shape: `{ action: change-intent | fix-behavior, rationale: string }`
- Atomicity: `rationale` explains the selected action and cannot vary without changing or misrepresenting that action.

## Enforcement

The reconciliation workflow must block behavior-changing work until a human records one resolution action and its rationale.

## Consumers

- D008 — Route framework changes
- Ledger maintenance workflow
- Implementation repair workflow

## Verification

- Exercise both outcomes with one stale-intent case and one incorrect-behavior case.
- Confirm the workflow cannot proceed while the action is unadjudicated.
- Trace each completed reconciliation to either a ledger delta or an implementation fix matching the recorded action.