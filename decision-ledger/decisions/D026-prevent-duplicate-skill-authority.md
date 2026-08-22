---
status: active
domain: assurance
id: D026
title: "Prevent duplicate skill authority"
updated_at: 2026-08-21
---

## Requirement

At most one installed Decision Engineering skill can govern ledger mutations in a project.

## Question

What happens when managed and editable installations coexist?

## Input facts

- `package.claude-code-distribution`
  - Kind: derived
  - Produced by: D022
- `package.codex-distribution`
  - Kind: derived
  - Produced by: D023
- `package.cursor-distribution`
  - Kind: derived
  - Produced by: D024
- `package.editable-installation`
  - Kind: derived
  - Produced by: D025
- `package.requested-duplicate-policy`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.duplicate-authority-policy`
- Meaning: Whether ledger mutation is permitted when more than one skill authority is observable.
- Shape: `{ duplicate_absent: allow, duplicate_present: block_with_removal_guidance }`
- Atomicity: Guidance explains the binary allow-or-block result and cannot vary independently.

## Invariant

The skill never mutates a ledger while it can observe another applicable Decision Engineering skill copy.

## Policy

Allow mutation only when scanning finds one applicable skill; otherwise stop and identify the copies to remove.

## Enforcement

`installation_guard.assert_single_authority` must approve the active project before `ledger_init.py`, `ledger_new.py`, or `ledger_render.py` changes ledger files; the skill instructions require the same guard before direct edits.

## Projection

`package.duplicate-authority-policy.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D028 initialization
- D038 acceptance
- All ledger-writing workflows

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
