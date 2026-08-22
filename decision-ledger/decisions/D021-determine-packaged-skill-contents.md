---
status: active
domain: distribution
id: D021
title: "Determine packaged skill contents"
updated_at: 2026-08-21
---
## Requirement

Every installation receives the complete runnable Decision Engineering capability.

## Question

Which files belong to the distributed skill payload?

## Input facts

- `package.canonical-skill-source`
  - Kind: derived
  - Produced by: D020
- `package.requested-content-scope`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.skill-content-contract`
- Meaning: The inclusion boundary for the installable skill payload.
- Shape: every file recursively contained by `skills/decision-engineering`
- Atomicity: The directory tree is one inclusion boundary; omitting any member makes the payload incomplete.

## Invariant

An installed skill retains its instructions, agents metadata, assets, references, and scripts with relative paths unchanged.

## Policy

Ship the complete canonical directory recursively and do not maintain host-specific forks.

## Enforcement

Package validation must reject any host-visible payload that omits a canonical file or introduces another maintained copy.

## Projection

`package.skill-content-contract.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D022-D025 distribution decisions
- Release validation

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.