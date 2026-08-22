---
status: active
domain: operations
id: D028
title: "Initialize a missing ledger"
updated_at: 2026-08-21
---
## Requirement

A project can use Decision Engineering on first invocation without a separate setup step.

## Question

What action occurs when the resolved project ledger does not exist?

## Input facts

- `package.ledger-location`
  - Kind: derived
  - Produced by: D027
- `package.duplicate-authority-policy`
  - Kind: derived
  - Produced by: D026
- `project.ledger-existence`
  - Kind: root
  - Authority: filesystem observation at the resolved path

## Output fact

- Name: `package.ledger-initialization`
- Meaning: The action required before the first ledger-backed operation proceeds.
- Shape: `{ existing: reuse, missing_and_unique_skill: create, duplicate_skill: block }`
- Atomicity: The selected action is one mutually exclusive initialization state.

## Invariant

Initialization never overwrites an existing ledger or proceeds with duplicate authority.

## Policy

Reuse a conforming ledger; otherwise automatically initialize the resolved path only after duplicate validation permits mutation.

## Enforcement

`ledger_init.main` must perform project-containment, duplicate-authority, and existence checks before writing the bundled template.

## Projection

`package.ledger-initialization.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D038 acceptance
- First-use workflow
- Ledger initialization script

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.