---
status: active
domain: distribution
id: D025
title: "Determine editable project installation"
---

## Requirement

Users who want to adapt the skill can install an explicitly editable project-local copy.

## Question

Which installation channel provides an editable project-scoped skill?

## Input facts

- `package.identity`
  - Kind: derived
  - Produced by: D019
- `package.skill-content-contract`
  - Kind: derived
  - Produced by: D021
- `package.requested-editable-channel`
  - Kind: root
  - Authority: packaging-owner interview

## Invariants

The editable channel installs one canonical project payload with host links and never modifies global agent configuration.

## Policy

Use skills.sh without `--copy` for one editable canonical project payload with host links, and do not create a bespoke installer.

## Output fact

- Name: `package.editable-installation`
- Meaning: The supported channel for installing a user-owned skill copy.
- Shape: `{ installer: skills.sh, source: hpark0011/decision-engineering, scope: project, ownership: editable }`
- Atomicity: Installer, source, scope, and ownership together define one installation relationship.

## Enforcement

Acceptance validation must reject an editable path that writes global configuration or uses a maintained custom installer.

## Consumers

- D026 duplicate prevention
- D038 acceptance
- README installation documentation

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
