---
status: active
domain: authority
id: D001
title: "Determine intent authority"
updated_at: 2026-08-21
---

## Requirement

The system's intended behavior must have one durable, reviewable source of truth.

## Question

Which artifact is authoritative for what the system is intended to decide?

## Input facts

- `framework.persisted-intent-requirement`
  - Kind: root
  - Authority: IDEA.md — The core idea

## Output fact

- Name: `framework.intent-authority`
- Meaning: The artifact class that authoritatively defines current intended decisions.
- Shape: `decision-ledger`
- Atomicity: The answer names one authority for one meaning and has no independently variable part.

## Invariant

No implementation, projection, ticket, comment, or conversation independently overrides adopted ledger intent.

## Policy

Treat `decision-ledger/SCHEMA.md` and active `decision-ledger/decisions/*.md` as the source code of intent; treat other descriptions as requirement evidence or projections unless a human adopts them through a ledger change.

## Enforcement

The behavior-changing review workflow must reject changes that neither cite the governing decision IDs nor include the required ledger delta.

## Projection

`framework.intent-authority.public`

Names the ledger as the intent authority and may link to its index without adding or restating policy.

## Consumers

- D003 — Resolve intent behavior divergence
- D008 — Route framework changes
- Decision Engineering maintainers and implementation reviewers

## Verification

- Trace each behavior-shaping framework instruction to `SCHEMA.md` or one active decision record.
- Flag any implementation or projection that introduces policy with no governing decision ID.
- Confirm the review boundary rejects an untraced behavior change.