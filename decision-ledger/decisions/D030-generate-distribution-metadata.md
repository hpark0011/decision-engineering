---
status: active
domain: distribution
id: D030
title: "Generate distribution metadata"
---
## Requirement

Host manifests remain correct generated artifacts of package identity, contents, and version.

## Question

How are host manifests and their versions maintained?

## Input facts

- `package.identity`
  - Kind: derived
  - Produced by: D019
- `package.canonical-skill-source`
  - Kind: derived
  - Produced by: D020
- `package.claude-code-distribution`
  - Kind: derived
  - Produced by: D022
- `package.codex-distribution`
  - Kind: derived
  - Produced by: D023
- `package.cursor-distribution`
  - Kind: derived
  - Produced by: D024
- `package.release-version`
  - Kind: derived
  - Produced by: D029

## Invariants

Generated manifests contain no independent policy and always match canonical identity, source layout, and version.

## Policy

Generate every host manifest and GitHub marketplace catalog from one metadata definition and verify checked-in artifacts are current.

## Output fact

- Name: `package.distribution-metadata`
- Meaning: The generated set of host manifests and shared version metadata.
- Shape: `{ plugin.json, .claude-plugin/plugin.json, .claude-plugin/marketplace.json, .codex-plugin/plugin.json, .agents/plugins/marketplace.json, VERSION }`
- Atomicity: The files form one generated artifact set; a stale member invalidates the set.

## Enforcement

`scripts/generate_manifests.py --check`, called by `scripts/validate_package.py`, must reject hand drift or a stale generated file.

## Consumers

- D038 acceptance
- Claude Code, Codex, and Cursor
- Release tooling

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
