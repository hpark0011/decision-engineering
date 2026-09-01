---
status: active
domain: compatibility
id: D031
title: "Determine macOS support"
---

## Requirement

The packaged skill operates correctly on supported macOS environments.

## Question

Is macOS an actively verified package platform?

## Input facts

- `package.requested-macos-support`
  - Kind: root
  - Authority: packaging-owner interview
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021

## Invariants

Every shipped Python workflow must pass on a current supported macOS runner.

## Policy

Declare macOS supported only while platform acceptance tests pass.

## Output fact

- Name: `package.macos-support`
- Meaning: Whether macOS belongs to the supported compatibility contract.
- Shape: `supported`
- Atomicity: Platform support is one independently testable proposition.

## Enforcement

The `macos-latest` job in `.github/workflows/validate.yml` must pass `scripts/validate_package.py` and ledger lint before release.

## Consumers

- D038 acceptance
- macOS users
- CI matrix

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
