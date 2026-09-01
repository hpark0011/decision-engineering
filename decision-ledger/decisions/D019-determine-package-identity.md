---
status: active
domain: distribution
id: D019
title: "Determine package identity"
---
## Requirement

Every distribution artifact identifies the package by one stable public name.

## Question

What package name identifies Decision Engineering across every supported host and install command?

## Input facts

- `package.requested-identity`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

Manifests, install commands, release artifacts, and documentation must name the same package.

## Policy

Use `decision-engineering` exactly, normalized as lowercase kebab-case, in every distribution artifact.

## Output fact

- Name: `package.identity`
- Meaning: The one public identifier used for the packaged skill.
- Shape: `decision-engineering`
- Atomicity: A package has one identifier; changing it replaces the whole fact.

## Enforcement

Distribution metadata validation must reject any manifest or install command whose package identifier differs.

## Consumers

- D022-D025 distribution decisions
- D030 metadata generation
- README installation documentation

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
