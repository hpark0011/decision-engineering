---
status: active
domain: ledger
id: D006
title: "Determine decision record contract"
---

## Requirement

Humans, agents, and deterministic tools must interpret every decision record compatibly.

## Question

Does a candidate decision file satisfy the ledger's record contract?

## Input facts

- `framework.decision-atomicity`
  - Kind: derived
  - Produced by: D004
- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005
- `framework.machine-checkability-requirement`
  - Kind: root
  - Authority: IDEA.md — SCHEMA.md and Lint
## Invariants

- Every accepted record has stable identity, lifecycle, and routing metadata.
- Every accepted record has exactly one non-placeholder Requirement, Question, Input facts, Invariants, Policy, Output fact, Enforcement, Consumers, and Verification section in schema order.

## Policy

Return `valid` only when the candidate conforms to `SCHEMA.md`, passes D004 and D005, names at least one consumer of the output fact, and states concrete enforcement and verification obligations; otherwise return `invalid` with the failed contract condition.

## Output fact

- Name: `framework.record-validity`
- Meaning: Whether one candidate Markdown decision record satisfies the complete schema contract.
- Shape: `{ state: valid | invalid, reason: string }`
- Atomicity: Validity applies to the record as one parser and maintenance contract; `reason` only explains that result.

## Enforcement

`ledger_lint.py` must reject structural violations, and ledger review must reject semantic placeholders or obligations that only satisfy syntax.

## Consumers

- D007 — Determine ledger storage model
- D017 — Determine ledger acceptance
- `ledger_new.py`
- Decision record authors and reviewers

## Verification

- Validate one complete record and representative missing, duplicate, reordered, and placeholder sections.
- Confirm structural lint and semantic review both contribute to the acceptance result.
- Reject unsupported metadata and unsupported decision sections.
- Confirm changing the contract requires a logged `SCHEMA.md` change and compatible record migration.
