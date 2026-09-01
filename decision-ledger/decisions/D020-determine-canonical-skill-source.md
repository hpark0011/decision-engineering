---
status: active
domain: distribution
id: D020
title: "Determine canonical skill source"
---

## Requirement

All hosts and installers package one authoritative skill tree rather than host-specific copies.

## Question

Which repository path is the authoritative source for the Decision Engineering skill?

## Input facts

- `package.requested-source-layout`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

No host directory may contain a second maintained copy of the skill.

## Policy

Move the current skill tree to `skills/decision-engineering` and make every host consume that directory.

## Output fact

- Name: `package.canonical-skill-source`
- Meaning: The sole repository location from which every packaged skill copy is derived.
- Shape: `skills/decision-engineering`
- Atomicity: Authority resolves to one directory path and cannot be partially assigned.

## Enforcement

Repository validation must reject a missing canonical tree or a duplicate Decision Engineering `SKILL.md` outside it.

## Consumers

- D021 packaged contents
- D022-D025 distribution decisions
- D030 metadata generation

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
