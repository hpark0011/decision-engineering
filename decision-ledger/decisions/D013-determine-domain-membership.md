---
status: active
domain: topology
id: D013
title: "Determine domain membership"
---
## Requirement

Domain boundaries must localize authority, consistency, and correction rather than mirror unstable implementation or organizational categories.

## Question

What is the smallest authoritative consistency boundary that should contain a candidate decision?

## Input facts

- `framework.decision-atomicity`
  - Kind: derived
  - Produced by: D004
- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005
- `framework.domain-evidence`
  - Kind: root
  - Authority: Maintainer review of decision dependencies, invariants, and change history

## Invariants

- Decisions grouped in a domain share invariants that must remain correct together.
- A decision produces only its declared output fact.
- Cross-domain dependencies read authoritative output facts and never write another domain's facts directly.

## Policy

Assign the candidate to the smallest boundary that has authority to maintain the decision and preserve its invariants with related outputs. Use authority, consistency, and correction locality as the tests; never derive the label merely from UI, API, database, team, or folder categories.

## Output fact

- Name: `framework.domain-membership`
- Meaning: The one primary authority and consistency boundary assigned to a candidate decision.
- Shape: `lowercase domain label`
- Atomicity: The answer assigns one decision to one primary routing boundary.

## Enforcement

Architecture review must reject a domain assignment that lacks dependency and change-locality evidence; domain changes update metadata and generated views without moving stable decision files.

## Consumers

- D014 — Validate dependency graph
- Generated decision index and graph
- Architecture routing and impact analysis

## Verification

- Compare each assignment with authority, shared invariants, and observed correction dependencies.
- Reject a grouping justified only by an implementation layer or organizational noun.
- Reject any design that permits a domain to write another domain's facts directly.
- Confirm a domain relabel leaves stable IDs, filenames, and fact ownership intact.
