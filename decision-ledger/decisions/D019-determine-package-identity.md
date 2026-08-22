---
status: active
domain: distribution
id: D019
title: "Determine package identity"
updated_at: 2026-08-21
---
## Requirement

Every distribution projection identifies the package by one stable public name.

## Question

What package name identifies Decision Engineering across every supported host and install command?

## Input facts

- `package.requested-identity`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.identity`
- Meaning: The one public identifier used for the packaged skill.
- Shape: `decision-engineering`
- Atomicity: A package has one identifier; changing it replaces the whole fact.

## Invariant

Manifests, install commands, release artifacts, and documentation must name the same package.

## Policy

Use `decision-engineering` exactly, normalized as lowercase kebab-case, in every distribution projection.

## Enforcement

Distribution metadata validation must reject any manifest or install command whose package identifier differs.

## Projection

`package.identity.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D022-D025 distribution decisions
- D030 metadata generation
- README installation documentation

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.