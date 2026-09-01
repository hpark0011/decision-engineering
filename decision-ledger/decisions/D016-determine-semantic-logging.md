---
status: active
domain: lifecycle
id: D016
title: "Determine semantic logging"
---
## Requirement

Maintainers must be able to understand why the decision model changed and what the change affected without reconstructing meaning from line history.

## Question

Does a proposed ledger change require a semantic log entry?

## Input facts

- `framework.decision-identity`
  - Kind: derived
  - Produced by: D015
- `ledger.change-kind`
  - Kind: root
  - Authority: Maintainer proposing the ledger change

## Invariants

Every accepted semantic create, edit, rename, supersede, retire, restore, delete, or schema change remains attributable by stable ID with reason, changed meaning, and downstream impact.

## Policy

Return `required` when the delta changes ownership, meaning, dependencies, policy, invariants, output, enforcement, consumers, verification, lifecycle, or schema; return `not-required` only for wording or formatting that leaves the decision model unchanged.

## Output fact

- Name: `framework.semantic-log-obligation`
- Meaning: Whether one proposed ledger delta must append semantic history.
- Shape: `{ state: required | not-required, reason: string }`
- Atomicity: `reason` explains the obligation for the same delta and cannot vary independently.

## Enforcement

Ledger review must reject a semantic change without an appended `log.md` entry; `ledger_lint.py` must reject a decision with no create, restore, or migration history.

## Consumers

- D017 — Determine ledger acceptance
- `decision-ledger/log.md`
- Change, impact, and lifecycle review workflows

## Verification

- Exercise every semantic operation category and one wording-only correction.
- Confirm required entries include reason, changed semantics, and downstream affected items.
- Confirm prior log history is preserved byte-for-byte when a new entry is appended.
