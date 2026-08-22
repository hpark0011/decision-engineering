---
status: active
domain: assurance
id: D038
title: "Determine package acceptance"
updated_at: 2026-08-21
---

## Requirement

Only a complete, installable, lifecycle-safe package can be released.

## Question

Which verification result makes a package release acceptable?

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
- `package.duplicate-authority-policy`
  - Kind: derived
  - Produced by: D026
- `package.ledger-initialization`
  - Kind: derived
  - Produced by: D028
- `package.distribution-metadata`
  - Kind: derived
  - Produced by: D030
- `package.macos-support`
  - Kind: derived
  - Produced by: D031
- `package.linux-support`
  - Kind: derived
  - Produced by: D032
- `package.windows-support`
  - Kind: derived
  - Produced by: D033
- `package.license`
  - Kind: derived
  - Produced by: D035
- `package.support-routing`
  - Kind: derived
  - Produced by: D036
- `package.execution-boundary`
  - Kind: derived
  - Produced by: D037
- `package.acceptance-evidence`
  - Kind: root
  - Authority: release verification results

## Output fact

- Name: `package.acceptance`
- Meaning: Whether a candidate package satisfies every required release check.
- Shape: `{ state: accepted | rejected, failures: string[] }`
- Atomicity: Failures explain the aggregate state and cannot vary independently.

## Invariant

Acceptance requires host installation, skill invocation, initialization, decision creation, lint/render, upgrade preservation, uninstall preservation, duplicate detection, platform, metadata, license, support, and execution-boundary checks.

## Policy

Accept only when every required check passes; any missing or failing result rejects the candidate.

## Enforcement

`scripts/validate_package.py`, the three-host lifecycle tests, native manifest validators, skills.sh discovery, and the three-OS CI matrix form the acceptance boundary; publication must not proceed while any required result is absent or failing.

## Projection

`package.acceptance.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- D039 maturity gate
- Release workflow
- Package maintainers

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
