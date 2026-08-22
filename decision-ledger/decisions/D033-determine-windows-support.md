---
status: active
domain: compatibility
id: D033
title: "Determine Windows support"
updated_at: 2026-08-21
---
## Requirement

The packaged skill operates correctly on supported Windows environments.

## Question

Is Windows an actively verified package platform?

## Input facts

- `package.requested-windows-support`
  - Kind: root
  - Authority: packaging-owner interview
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021

## Output fact

- Name: `package.windows-support`
- Meaning: Whether Windows belongs to the supported compatibility contract.
- Shape: `supported`
- Atomicity: Platform support is one independently testable proposition.

## Invariant

Every shipped workflow uses cross-platform Python and passes on a current Windows runner.

## Policy

Declare Windows supported only while platform acceptance tests pass.

## Enforcement

The `windows-latest` job in `.github/workflows/validate.yml` must pass `scripts/validate_package.py` and ledger lint before release.

## Projection

`package.windows-support.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D038 acceptance
- Windows users
- CI matrix

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.