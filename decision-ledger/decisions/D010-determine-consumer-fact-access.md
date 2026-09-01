---
status: active
domain: distribution
id: D010
title: "Determine consumer fact access"
---
## Requirement

Consumers must reuse authoritative answers instead of recreating policies from upstream facts.

## Question

May a proposed consumer access the selected decision information directly?

## Input facts

- `framework.consumer-representation-treatment`
  - Kind: derived
  - Produced by: D009
- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005

## Invariants

No consumer reconstructs an authoritative decision from raw inputs or a paraphrased equivalent fact.

## Policy

Return `allowed` when the consumer reads the owning output fact directly or applies a D009 implementation-detail representation; return `blocked` when it reads private upstream facts to recreate policy, copies the rule, treats a representation as authority, or uses a D009 `decision-required` representation without its own decision.

## Output fact

- Name: `framework.consumer-access`
- Meaning: Whether one proposed consumer path preserves the owning decision's authority.
- Shape: `{ state: allowed | blocked, reason: string }`
- Atomicity: `reason` explains the access result for the same consumer path and cannot vary independently.

## Enforcement

Consumer integration review must reject any path that bypasses the output contract or independently re-derives the owning policy.

## Consumers

- Cross-domain integrations
- UI, API, worker, agent, and report implementations
- Architecture and code review workflows

## Verification

- Accept one direct authoritative-output consumer and one consumer with a mechanical representation binding.
- Reject a consumer that reproduces the same result from raw upstream facts.
- Trace each allowed path back to one producer and confirm no copied policy exists in the consumer.
