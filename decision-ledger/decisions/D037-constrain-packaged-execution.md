---
status: active
domain: assurance
id: D037
title: "Constrain packaged execution"
---
## Requirement

Running the installed skill remains local, private, and confined to its active project.

## Question

What side-effect boundary governs packaged skill execution?

## Input facts

- `package.ledger-location`
  - Kind: derived
  - Produced by: D027
- `package.requested-execution-boundary`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

Skill execution never transmits data or writes outside the project-contained ledger.

## Policy

Use local standard-library operations only; distinguish third-party installation-time network activity from skill runtime.

## Output fact

- Name: `package.execution-boundary`
- Meaning: The permitted runtime side effects of the installed skill.
- Shape: `{ network: denied, telemetry: none, processing: local, writes: resolved project ledger only }`
- Atomicity: The fields jointly define one execution sandbox; relaxing any field changes the boundary.

## Enforcement

`scripts/validate_package.py` must reject network-client imports, and `installation_guard.project_root_for` must reject ledger writes outside the active project.

## Consumers

- D038 acceptance
- All packaged scripts
- Security review

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.