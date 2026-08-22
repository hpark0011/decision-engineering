---
status: active
domain: assurance
id: D011
title: "Determine enforcement boundary"
updated_at: 2026-08-21
---
## Requirement

Invalid actions and state transitions must be prevented across every consumer path.

## Question

Is a proposed boundary sufficient to enforce the governing invariant?

## Input facts

- `framework.invariant-preservation-requirement`
  - Kind: root
  - Authority: GLOSSARY.md — Invariant and Enforcement

## Output fact

- Name: `framework.enforcement-sufficiency`
- Meaning: Whether one proposed boundary can prevent or reject every governed invalid action or transition.
- Shape: `{ state: sufficient | insufficient, reason: string }`
- Atomicity: `reason` explains the sufficiency result for one boundary and cannot vary independently.

## Invariant

Enforcement occurs at a commit or rejection boundary that no governed consumer can bypass.

## Policy

Return `sufficient` only when the proposed boundary can reject or prevent the invalid result or transition for all entry paths; return `insufficient` for disabled controls, hidden UI, warnings, documentation, or checks bypassable by another consumer.

## Enforcement

Implementation review must block adoption until each active decision names a sufficient boundary or a concrete pre-implementation boundary obligation.

## Projection

`framework.enforcement-sufficiency.public`

Exposes the sufficiency result and boundary description without claiming that enforcement has been implemented when it is only an obligation.

## Consumers

- D012 — Determine verification target
- Decision record authors
- Implementation and security reviewers

## Verification

- Exercise the proposed boundary through every known UI, API, worker, and agent entry path.
- Confirm a presentation-only control is classified as insufficient.
- Confirm the real boundary rejects every representative invalid result or transition.