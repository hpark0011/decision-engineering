---
status: active
domain: operations
id: D008
title: "Route framework changes"
---
## Requirement

Each maintenance request must reuse existing decision ownership when possible and create new authority only for a genuinely new uncertainty.

## Question

Which ledger operation class applies to the current framework request?

## Input facts

- `maintenance.request`
  - Kind: root
  - Authority: Current human or project requirement
- `framework.intent-authority`
  - Kind: derived
  - Produced by: D001
- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005

## Invariants

No request creates a second decision for an output fact or question that already has an authoritative owner.

## Policy

Choose `consume` when an existing output fact already answers the request, `edit` when the owning decision's semantics must change, `create` only for a new question and output fact, and `reconcile` for an observed intent-behavior mismatch governed by D003.

## Output fact

- Name: `framework.change-route`
- Meaning: The one operation class that governs a current requested framework change.
- Shape: `consume | edit | create | reconcile`
- Atomicity: One request receives one mutually exclusive route before ledger or implementation editing begins.

## Enforcement

The Decision Engineering maintenance workflow must state the route and governing decision ID or newly allocated ID before changing ledger or behavior.

## Consumers

- D018 — Determine ledger lookup scope
- Decision Engineering skill workflow
- Ledger and implementation change reviews

## Verification

- Exercise one clear request for each of the four route branches.
- Confirm an existing synonymous output is routed to `consume` or `edit`, never `create`.
- Confirm a mismatch is routed through D003 before either authority is changed.
