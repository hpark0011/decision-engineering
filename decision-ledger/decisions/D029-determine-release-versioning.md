---
status: active
domain: lifecycle
id: D029
title: "Determine release versioning"
updated_at: 2026-08-21
---

## Requirement

Installed users receive predictable compatible updates from one authoritative version.

## Question

How is the package version assigned and advanced?

## Input facts

- `package.requested-versioning`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.release-version`
- Meaning: The authoritative versioning contract for every package projection.
- Shape: Semantic Versioning with initial version `0.1.0`
- Atomicity: One release has one version across every manifest and tag.

## Invariant

All generated metadata and release tags agree on one strict semantic version.

## Policy

Begin at `0.1.0`; use major, minor, and patch increments according to Semantic Versioning.

## Enforcement

Release validation must reject malformed or divergent version values.

## Projection

`package.release-version.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D030 metadata generation
- D038 acceptance
- D039 maturity gate
- Release tooling

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
