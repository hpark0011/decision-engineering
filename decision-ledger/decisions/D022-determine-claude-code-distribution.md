---
status: active
domain: distribution
id: D022
title: "Determine Claude Code distribution"
updated_at: 2026-08-21
---
## Requirement

Claude Code users can install one managed Decision Engineering plugin for their user account.

## Question

How is the canonical skill distributed to Claude Code?

## Input facts

- `package.identity`
  - Kind: derived
  - Produced by: D019
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021
- `package.requested-claude-support`
  - Kind: root
  - Authority: packaging-owner interview

## Output fact

- Name: `package.claude-code-distribution`
- Meaning: The complete host contract by which Claude Code loads and scopes the package.
- Shape: `{ supported: true, format: claude-plugin, manifest: .claude-plugin/plugin.json, scope: user }`
- Atomicity: Format, manifest, and scope jointly identify one deployable Claude Code channel.

## Invariant

Claude Code loads the canonical skill as a user-scoped managed plugin without an editable project copy.

## Policy

Publish a Claude native manifest pointing at `./skills/` and document user scope as the default managed installation.

## Enforcement

Claude package validation must reject an invalid manifest, missing skill, or non-user default instruction.

## Projection

`package.claude-code-distribution.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D026 duplicate prevention
- D030 metadata generation
- D038 acceptance
- Claude Code users

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.