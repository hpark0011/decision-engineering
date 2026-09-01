---
status: active
domain: assurance
id: D011
title: "Determine enforcement boundary"
---
## Requirement

Invalid actions and state transitions must be prevented across every consumer path.

## Question

Is a proposed boundary sufficient to enforce the governing invariant?

## Input facts

- `framework.invariant-preservation-requirement`
  - Kind: root
  - Authority: GLOSSARY.md — Invariant and Enforcement

## Invariants

Enforcement occurs at a commit or rejection boundary that no governed consumer can bypass.

## Policy

Return `sufficient` only when the proposed boundary can reject or prevent the invalid result or transition for all entry paths; return `insufficient` for disabled controls, hidden UI, warnings, documentation, or checks bypassable by another consumer.

## Output fact

- Name: `framework.enforcement-sufficiency`
- Meaning: Whether one proposed boundary can prevent or reject every governed invalid action or transition.
- Shape: `{ state: sufficient | insufficient, reason: string }`
- Atomicity: `reason` explains the sufficiency result for one boundary and cannot vary independently.

## Enforcement

Implementation review must block adoption until each active decision names a sufficient boundary or a concrete pre-implementation boundary obligation.

## Consumers

- D012 — Determine verification target
- Decision record authors
- Implementation and security reviewers

## Verification

- Exercise the proposed boundary through every known UI, API, worker, and agent entry path.
- Confirm a presentation-only control is classified as insufficient.
- Confirm the real boundary rejects every representative invalid result or transition.