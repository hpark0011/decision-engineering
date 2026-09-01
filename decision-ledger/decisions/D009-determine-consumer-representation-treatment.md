---
status: active
domain: distribution
id: D009
title: "Determine consumer representation treatment"
---
## Requirement

Consumers must adapt authoritative output facts without creating hidden decision owners.

## Question

Does a proposed consumer-facing representation require its own decision?

## Input facts

- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005
- `framework.consumer-representation-requirement`
  - Kind: root
  - Authority: decision-ledger/SCHEMA.md — Consumers

## Invariants

- A mechanical representation remains an implementation detail rather than an authoritative fact.
- Any representation that introduces judgment has its own decision and output fact.

## Policy

Return `implementation-detail` when the proposal only formats, renames, omits, or transports the owning output without changing its meaning; return `decision-required` when producing it requires any new judgment, classification, default, or policy branch.

## Output fact

- Name: `framework.consumer-representation-treatment`
- Meaning: Whether a proposed consumer-facing representation is an implementation detail or requires a separate decision.
- Shape: `{ state: implementation-detail | decision-required, reason: string }`
- Atomicity: `reason` explains the treatment of the same proposed representation and cannot vary independently.

## Enforcement

Consumer integration review must reject judgment-bearing representations until the new uncertainty is modeled as its own decision and authoritative fact.

## Consumers

- D010 — Determine consumer fact access
- API, UI, agent-skill, and report designers
- Decision record reviewers

## Verification

- Classify representative renaming, omission, formatting, and transport as implementation details.
- Require a new decision for a representation that adds a default or classification not present in its source output.
- Confirm every accepted implementation detail reads exactly one authoritative output fact.
