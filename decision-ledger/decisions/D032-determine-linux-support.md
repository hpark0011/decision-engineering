---
status: active
domain: compatibility
id: D032
title: "Determine Linux support"
---

## Requirement

The packaged skill operates correctly on supported Linux environments.

## Question

Is Linux an actively verified package platform?

## Input facts

- `package.requested-linux-support`
  - Kind: root
  - Authority: packaging-owner interview
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021

## Invariants

Every shipped Python workflow must pass on a current supported Linux runner.

## Policy

Declare Linux supported only while platform acceptance tests pass.

## Output fact

- Name: `package.linux-support`
- Meaning: Whether Linux belongs to the supported compatibility contract.
- Shape: `supported`
- Atomicity: Platform support is one independently testable proposition.

## Enforcement

The `ubuntu-latest` job in `.github/workflows/validate.yml` must pass `scripts/validate_package.py` and ledger lint before release.

## Consumers

- D038 acceptance
- Linux users
- CI matrix

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
