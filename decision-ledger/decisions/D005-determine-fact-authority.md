---
status: active
domain: modeling
id: D005
title: "Determine fact authority"
---
## Requirement

Every fact used by a decision must trace to one correction site.

## Question

Is a candidate fact declaration authoritatively owned?

## Input facts

- `framework.correctability-requirement`
  - Kind: root
  - Authority: README.md — Core philosophy and IDEA.md — The correction threshold
- `framework.decision-atomicity`
  - Kind: derived
  - Produced by: D004

## Invariants

Every root fact has exactly one external authority or observation boundary, and every derived fact has exactly one producing decision.

## Policy

Return `valid` for a root fact only when it names one external authority, and for a derived fact only when it names the one decision that produces the identical stable fact; return `invalid` for absent, ambiguous, duplicated, paraphrased, or conflicting ownership.

## Output fact

- Name: `framework.fact-authority`
- Meaning: Whether one candidate fact has exactly one valid authority for its kind.
- Shape: `{ state: valid | invalid, reason: string }`
- Atomicity: `reason` explains the validity state of the same fact declaration and cannot vary independently.

## Enforcement

`ledger_lint.py` and ledger review must reject unresolved producers, missing root authorities, inconsistent authorities, duplicate outputs, and fact references that reconstruct another fact under a new name.

## Consumers

- D006 — Determine decision record contract
- D008 — Route framework changes
- D009 — Determine consumer representation treatment
- D010 — Determine consumer fact access
- D014 — Validate dependency graph

## Verification

- Exercise valid root and derived declarations plus missing, conflicting, and duplicate authority cases.
- Confirm every derived input resolves to the identical output fact and producer ID.
- Confirm the enforcement path rejects synonymous facts with competing owners.
