---
status: active
domain: topology
id: D013
title: "Determine domain membership"
updated_at: 2026-08-21
---

## Requirement

Domain boundaries must localize correction and change rather than mirror unstable implementation or organizational categories.

## Question

Which primary domain should own a candidate decision?

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

## Output fact

- Name: `framework.domain-membership`
- Meaning: The one primary domain label assigned to a candidate decision from its correction dependencies.
- Shape: `lowercase domain label`
- Atomicity: The answer assigns one decision to one primary routing boundary.

## Invariant

Decisions grouped in a domain share the facts and invariants that must remain correct together, while cross-domain dependencies stay narrow and explicit.

## Policy

Assign the candidate to the domain whose decisions consistently depend on the same authoritative facts, preserve the same invariants, and change together; use change locality as the check, and never derive the label merely from UI, API, database, team, or folder categories.

## Enforcement

Architecture review must reject a domain assignment that lacks dependency and change-locality evidence; domain changes update metadata and generated views without moving stable decision files.

## Projection

`framework.domain-membership.public`

Exposes the assigned label and links to dependency evidence without adding another grouping judgment.

## Consumers

- D014 — Validate dependency graph
- Generated decision index and graph
- Architecture routing and impact analysis

## Verification

- Compare each assignment with shared fact, invariant, and observed change dependencies.
- Reject a grouping justified only by an implementation layer or organizational noun.
- Confirm a domain relabel leaves stable IDs, filenames, and fact ownership intact.