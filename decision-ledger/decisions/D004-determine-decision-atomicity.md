---
status: active
domain: modeling
id: D004
title: "Determine decision atomicity"
---
## Requirement

Each recorded decision must localize one independently correctable uncertainty.

## Question

Does a candidate decision resolve exactly one independently decidable proposition?

## Input facts

- `framework.correctability-requirement`
  - Kind: root
  - Authority: README.md — Core philosophy and IDEA.md — The correction threshold
- `framework.atomicity-evidence`
  - Kind: root
  - Authority: IDEA.md — The central unit

## Invariants

One decision resolves one question, applies one policy, and produces one authoritative output fact.

## Policy

Return `split-required` if any output part can change independently, be correct while another is wrong, serve a consumer independently, or require a different policy, invariant, or verification; otherwise return `atomic` only when the record produces one proposition from one question.

## Output fact

- Name: `framework.decision-atomicity`
- Meaning: Whether one candidate decision is atomic or must be split.
- Shape: `{ state: atomic | split-required, reason: string }`
- Atomicity: `reason` explains the atomicity state and cannot change independently without misrepresenting it.

## Enforcement

Ledger authoring review must reject a candidate record until the atomicity tests pass; `ledger_lint.py` must reject records that syntactically declare anything other than one output fact.

## Consumers

- D005 — Determine fact authority
- D006 — Determine decision record contract
- D012 — Determine verification target
- D013 — Determine domain membership

## Verification

- Apply all four atomicity tests to every structured output before acceptance.
- Confirm a deliberately multi-fact record is rejected and split into separate decisions.
- Confirm `ledger_lint.py` rejects a record with multiple output declarations.