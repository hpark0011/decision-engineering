---
status: active
domain: governance
id: D035
title: "Determine package licensing"
updated_at: 2026-08-21
---
## Requirement

Recipients have clear permission to use, modify, and redistribute the package.

## Question

Which license governs the distributed package?

## Input facts

- `package.public-release-source`
  - Kind: derived
  - Produced by: D034
- `package.delegated-license-choice`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.license`
- Meaning: The legal license applied to package source and distributions.
- Shape: `MIT`
- Atomicity: One SPDX license identifier governs the package.

## Invariant

The repository license file and every manifest declare MIT.

## Policy

Use the MIT License for broad adoption and editable redistribution.

## Enforcement

Package validation must reject a missing license file or mismatched manifest identifier.

## Projection

`package.license.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D038 acceptance
- Users
- Host marketplaces

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.