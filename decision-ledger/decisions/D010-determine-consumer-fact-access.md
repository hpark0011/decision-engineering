---
status: active
domain: distribution
id: D010
title: "Determine consumer fact access"
updated_at: 2026-08-21
---
## Requirement

Consumers must reuse authoritative answers instead of recreating policies from upstream facts.

## Question

May a proposed consumer access the selected decision information directly?

## Input facts

- `framework.projection-eligibility`
  - Kind: derived
  - Produced by: D009
- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005

## Output fact

- Name: `framework.consumer-access`
- Meaning: Whether one proposed consumer path preserves the owning decision's authority.
- Shape: `{ state: allowed | blocked, reason: string }`
- Atomicity: `reason` explains the access result for the same consumer path and cannot vary independently.

## Invariant

No consumer reconstructs an authoritative decision from raw inputs or a paraphrased equivalent fact.

## Policy

Return `allowed` when the consumer reads the owning output contract or an allowed D009 projection; return `blocked` when it reads private upstream facts to recreate policy, copies the rule, or treats a presentation as authority.

## Enforcement

Consumer integration review must reject any path that bypasses the output contract or independently re-derives the owning policy.

## Projection

`framework.consumer-access.public`

Exposes the access result and governing output or projection link without restating the policy being consumed.

## Consumers

- Cross-domain integrations
- UI, API, worker, agent, and report implementations
- Architecture and code review workflows

## Verification

- Accept one direct authoritative-output consumer and one faithful projection consumer.
- Reject a consumer that reproduces the same result from raw upstream facts.
- Trace each allowed path back to one producer and confirm no copied policy exists in the consumer.