---
status: active
domain: lifecycle
id: D039
title: "Determine release maturity gate"
updated_at: 2026-08-21
---
## Requirement

Package version maturity reflects demonstrated effectiveness rather than packaging completion alone.

## Question

When is the package eligible for 0.1.0 and 1.0.0 release maturity?

## Input facts

- `package.acceptance`
  - Kind: derived
  - Produced by: D038
- `package.benchmark-results`
  - Kind: root
  - Authority: controlled matched-task evaluation

## Output fact

- Name: `package.release-maturity`
- Meaning: The highest release maturity justified by current evidence.
- Shape: `0.1.0-eligible | 1.0.0-eligible`
- Atomicity: A candidate has one highest justified maturity state.

## Invariant

Version 1.0.0 is never released solely on packaging success.

## Policy

Grant 0.1.0 eligibility after package acceptance; grant 1.0.0 eligibility only after at least 20 matched tasks show at least 25 percent fewer requirement-to-code divergences without worse initial correctness.

## Enforcement

The release gate must reject a version whose required acceptance or benchmark evidence is absent.

## Projection

`package.release-maturity.public`

Expose the output fact with host-appropriate naming and formatting only; introduce no new judgment.

## Consumers

- Release workflow
- Benchmark report
- Users evaluating maturity

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.