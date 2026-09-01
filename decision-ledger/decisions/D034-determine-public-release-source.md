---
status: active
domain: distribution
id: D034
title: "Determine public release source"
---
## Requirement

Users install and inspect releases from one public source repository.

## Question

Which source publishes the package?

## Input facts

- `package.identity`
  - Kind: derived
  - Produced by: D019
- `package.requested-release-source`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

All host metadata and installation documentation point to the same GitHub repository.

## Policy

Publish releases and source from the existing GitHub origin.

## Output fact

- Name: `package.public-release-source`
- Meaning: The authoritative public repository for package source and releases.
- Shape: `https://github.com/hpark0011/decision-engineering`
- Atomicity: A published release resolves to one source repository.

## Enforcement

Release validation must reject repository URLs that differ from the authoritative source.

## Consumers

- D035 licensing
- D036 support channels
- D038 acceptance
- Users and host installers

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.