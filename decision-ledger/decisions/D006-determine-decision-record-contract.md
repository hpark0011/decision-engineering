---
status: active
domain: ledger
id: D006
title: "Determine decision record contract"
updated_at: 2026-08-21
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
- `framework.record-recency-requirement`
  - Kind: root
  - Authority: repository maintainer

## Output fact

- Name: `framework.record-validity`
- Meaning: Whether one candidate Markdown decision record satisfies the complete schema contract.
- Shape: `{ state: valid | invalid, reason: string }`
- Atomicity: Validity applies to the record as one parser and maintenance contract; `reason` only explains that result.

## Invariant

Every accepted record has stable identity, lifecycle, routing, and ISO-date recency metadata plus exactly one non-placeholder Requirement, Question, Input facts, Output fact, Invariant, Policy, Enforcement, Projection, Consumers, and Verification section in schema order.

## Policy

Return `valid` only when the candidate conforms to `SCHEMA.md`, declares `updated_at` as `YYYY-MM-DD`, passes D004 and D005, names one projection and at least one consumer, and states concrete enforcement and verification obligations; otherwise return `invalid` with the failed contract condition. Refresh `updated_at` whenever decision semantics change.

## Enforcement

`ledger_lint.py` must reject structural violations, and ledger review must reject semantic placeholders or obligations that only satisfy syntax.

## Projection

`framework.record-validity.public`

Exposes record validity and the failing contract condition without duplicating the schema.

## Consumers

- D007 — Determine ledger storage model
- D017 — Determine ledger acceptance
- `ledger_new.py`
- Decision record authors and reviewers

## Verification

- Validate one complete record and representative missing, duplicate, reordered, and placeholder sections.
- Confirm structural lint and semantic review both contribute to the acceptance result.
- Reject missing and malformed `updated_at` values, and confirm new records use the current date.
- Confirm changing the contract requires a logged `SCHEMA.md` change and compatible record migration.
