---
status: active
domain: distribution
id: D023
title: "Determine Codex distribution"
---

## Requirement

Codex users can install one managed Decision Engineering plugin for their user account.

## Question

How is the canonical skill distributed to Codex?

## Input facts

- `package.identity`
  - Kind: derived
  - Produced by: D019
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021
- `package.requested-codex-support`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

Codex loads the canonical skill as a user-scoped managed plugin without a second project copy.

## Policy

Publish a Codex native manifest pointing at `./skills/` and document user scope as the managed installation.

## Output fact

- Name: `package.codex-distribution`
- Meaning: The complete host contract by which Codex loads and scopes the package.
- Shape: `{ supported: true, format: codex-plugin, manifest: .codex-plugin/plugin.json, scope: user }`
- Atomicity: Format, manifest, and scope jointly identify one deployable Codex channel.

## Enforcement

Codex plugin validation must reject an invalid manifest or missing canonical skill.

## Consumers

- D026 duplicate prevention
- D030 metadata generation
- D038 acceptance
- Codex users

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
