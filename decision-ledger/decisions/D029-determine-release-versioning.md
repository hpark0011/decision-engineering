---
status: active
domain: lifecycle
id: D029
title: "Determine release versioning"
---

## Requirement

Installed users receive predictable compatible updates from one authoritative version.

## Question

How is the package version assigned and advanced?

## Input facts

- `package.requested-versioning`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

All generated metadata and release tags agree on one strict semantic version.

## Policy

Begin at `0.1.0`; use major, minor, and patch increments according to Semantic Versioning.

## Output fact

- Name: `package.release-version`
- Meaning: The authoritative versioning contract for every package artifact.
- Shape: Semantic Versioning with initial version `0.1.0`
- Atomicity: One release has one version across every manifest and tag.

## Enforcement

Release validation must reject malformed or divergent version values.

## Consumers

- D030 metadata generation
- D038 acceptance
- D039 maturity gate
- Release tooling

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
