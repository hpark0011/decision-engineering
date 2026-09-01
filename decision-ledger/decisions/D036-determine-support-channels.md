---
status: active
domain: governance
id: D036
title: "Determine support channels"
---
## Requirement

Users have authoritative places to report defects and discuss adoption evidence.

## Question

Where are package support requests routed?

## Input facts

- `package.public-release-source`
  - Kind: derived
  - Produced by: D034
- `package.delegated-support-choice`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

Documentation never presents another authoritative support destination.

## Policy

Route reproducible defects to Issues and usage questions or field evidence to Discussions.

## Output fact

- Name: `package.support-routing`
- Meaning: The mapping from support request kind to its public channel.
- Shape: `{ defects: GitHub Issues, questions_and_field_reports: GitHub Discussions }`
- Atomicity: The mapping is one routing policy; each request resolves to exactly one channel.

## Enforcement

Documentation review must reject absent or conflicting support routes.

## Consumers

- D038 acceptance
- README
- Contributors and users

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.