---
status: active
domain: distribution
id: D009
title: "Determine projection eligibility"
updated_at: 2026-08-21
---
## Requirement

Resolved facts must be adaptable for consumers without creating hidden decision owners.

## Question

May a proposed representation be published as a projection of an existing output fact?

## Input facts

- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005
- `framework.multi-consumer-requirement`
  - Kind: root
  - Authority: IDEA.md — Projection and Consumers

## Output fact

- Name: `framework.projection-eligibility`
- Meaning: Whether a proposed consumer representation is judgment-free and may remain a projection.
- Shape: `{ state: allowed | decision-required, reason: string }`
- Atomicity: `reason` explains the eligibility state for the same proposed representation and cannot vary independently.

## Invariant

A projection changes representation only and never becomes an independent authority or policy site.

## Policy

Return `allowed` when the proposal only renames, omits, formats, or explains the owning output without changing its meaning; return `decision-required` when producing it requires any new judgment, classification, default, or policy branch.

## Enforcement

Projection review must reject judgment-bearing representations until the new uncertainty is modeled as its own decision and authoritative fact.

## Projection

`framework.projection-eligibility.public`

Exposes the eligibility state and reason without transforming the proposed representation itself.

## Consumers

- D010 — Determine consumer fact access
- API, UI, agent-skill, report, index, and graph designers
- Decision record reviewers

## Verification

- Accept representative rename, omission, formatting, and explanation-only projections.
- Reject a projection that adds a default or classification not present in its source output.
- Confirm every accepted projection traces to exactly one authoritative output fact.