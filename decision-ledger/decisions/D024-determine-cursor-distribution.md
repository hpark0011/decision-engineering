---
status: active
domain: distribution
id: D024
title: "Determine Cursor distribution"
updated_at: 2026-08-21
---
## Requirement

Cursor users can install one managed Decision Engineering plugin for their user account.

## Question

How is the canonical skill distributed to Cursor?

## Input facts

- `package.identity`
  - Kind: derived
  - Produced by: D019
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021
- `package.requested-cursor-support`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.cursor-distribution`
- Meaning: The complete host contract by which Cursor loads and scopes the package.
- Shape: `{ supported: true, format: agent-plugins-v1, manifest: plugin.json, scope: user }`
- Atomicity: Format, manifest, and scope jointly identify one deployable Cursor channel.

## Invariant

Cursor loads the canonical skill as a user-scoped Agent Plugin without a host-specific fork.

## Policy

Publish the Agent Plugins v1 root manifest and rely on fixed `skills/` discovery at user scope.

## Enforcement

Agent Plugins schema validation must reject an invalid root manifest or missing canonical skill.

## Projection

`package.cursor-distribution.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D026 duplicate prevention
- D030 metadata generation
- D038 acceptance
- Cursor users

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.