---
status: active
domain: topology
id: D014
title: "Validate dependency graph"
updated_at: 2026-08-21
---
## Requirement

Decision dependencies must form a traversable graph that supports deterministic ownership and downstream impact analysis.

## Question

Is the current ledger dependency graph structurally valid?

## Input facts

- `framework.fact-authority`
  - Kind: derived
  - Produced by: D005
- `framework.ledger-storage-model`
  - Kind: derived
  - Produced by: D007
- `framework.domain-membership`
  - Kind: derived
  - Produced by: D013
- `ledger.candidate-dependencies`
  - Kind: root
  - Authority: Candidate decision records under review

## Output fact

- Name: `framework.graph-validity`
- Meaning: Whether all current fact-to-decision dependencies satisfy the framework graph constraints.
- Shape: `{ state: valid | invalid, reason: string }`
- Atomicity: `reason` explains one graph-validity result and cannot vary without changing or misrepresenting it.

## Invariant

The graph is bipartite from authorities to facts to decisions to facts, has at most one producer per fact, resolves every reference, and contains no same-evaluation decision cycle.

## Policy

Return `valid` only when every input resolves, every derived producer agrees, root authorities are consistent, output and projection names are unique, supersession links resolve, and dependency traversal finds no synchronous cycle; model temporal feedback as an explicit persisted or previous-period root fact.

## Enforcement

`ledger_lint.py` must reject every invalid graph before projections are rendered or a ledger change is accepted.

## Projection

`framework.graph-validity.public`

Exposes graph validity and structural diagnostics; the Mermaid graph may change representation but never become authoritative.

## Consumers

- D017 — Determine ledger acceptance
- D018 — Determine ledger lookup scope
- `ledger_render.py`
- Impact analysis and architecture review

## Verification

- Exercise unresolved input, duplicate producer, inconsistent root authority, broken supersession, and cycle cases.
- Confirm persisted temporal feedback does not create a synchronous cycle.
- Compare generated graph nodes and edges with the authoritative decision records.