---
status: active
domain: assurance
id: D017
title: "Determine ledger acceptance"
updated_at: 2026-08-21
---
## Requirement

A ledger change must be structurally valid, navigationally current, and normatively reviewable before maintainers rely on it.

## Question

May the current decision-ledger state be accepted?

## Input facts

- `framework.record-validity`
  - Kind: derived
  - Produced by: D006
- `framework.verification-sufficiency`
  - Kind: derived
  - Produced by: D012
- `framework.graph-validity`
  - Kind: derived
  - Produced by: D014
- `framework.semantic-log-obligation`
  - Kind: derived
  - Produced by: D016
- `ledger.pre-render-lint-result`
  - Kind: root
  - Authority: ledger_lint.py execution
- `ledger.render-result`
  - Kind: root
  - Authority: ledger_render.py execution
- `ledger.post-render-lint-result`
  - Kind: root
  - Authority: ledger_lint.py execution
- `ledger.normative-review`
  - Kind: root
  - Authority: Human or agent reviewing authorities, bindings, enforcement, verification, and open questions

## Output fact

- Name: `framework.ledger-acceptance`
- Meaning: Whether the current ledger revision is safe to treat as the maintained intent model.
- Shape: `{ state: accepted | rejected, reason: string }`
- Atomicity: `reason` explains the acceptance state for the same ledger revision and cannot vary independently.

## Invariant

An accepted revision has zero lint errors before and after deterministic rendering, current generated projections, required semantic history, and no unreviewed normative gaps hidden by structural success.

## Policy

Return `accepted` only when record and graph facts are valid, required log entries exist, lint passes before render, render succeeds, lint passes again, warnings are explicitly reviewed, and authorities, enforcement, verification, bindings, and open normative questions are resolved or accurately reported; otherwise return `rejected`.

## Enforcement

The ledger completion workflow must run lint, render, and lint in that order and must not report implementation-readiness while this output is `rejected`.

## Projection

`framework.ledger-acceptance.public`

Exposes acceptance state, concise reason, validation counts, and unresolved review findings without recomputing acceptance.

## Consumers

- Decision Engineering completion report
- Implementation planning and behavior-changing reviews
- Humans deciding whether to adopt the ledger revision

## Verification

- Exercise lint failure, render failure, stale projection, missing log, unresolved warning, and fully accepted cases.
- Confirm rendering is bracketed by successful lint runs.
- Confirm structural success cannot hide an unresolved authority, enforcement, verification, binding, or normative question.