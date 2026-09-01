---
status: active
domain: ledger
id: D007
title: "Determine ledger storage model"
---
## Requirement

Framework intent must remain local to decisions, navigable at repository scale, and stable as domain groupings evolve.

## Question

Which storage model governs one system's decision ledger?

## Input facts

- `framework.record-validity`
  - Kind: derived
  - Produced by: D006
- `framework.change-locality-requirement`
  - Kind: root
  - Authority: IDEA.md — Why this works

## Invariants

One system has one ledger; authoritative decision files remain flat and stable while navigation, graphs, and domain groupings remain derived.

## Policy

Store one root `decision-ledger/` directory containing authoritative `SCHEMA.md` and flat `decisions/*.md`, append-only `log.md`, and generated `index.md` and `generated/graph.mmd`; never create a competing ledger for the same system.

## Output fact

- Name: `framework.ledger-storage-model`
- Meaning: The canonical physical and authority model for one system ledger.
- Shape: `schema-constrained-markdown-directory`
- Atomicity: The value names one storage contract consumed as a whole by maintainers and ledger tools.

## Enforcement

`ledger_init.py` must preserve an existing valid ledger and refuse to overwrite a conflicting non-empty directory; maintenance review must reject competing ledger roots or decision subdirectories.

## Consumers

- D014 — Validate dependency graph
- D015 — Determine decision identity
- D018 — Determine ledger lookup scope
- Ledger initialization and maintenance tools

## Verification

- Initialize an empty target and confirm the complete canonical tree is produced.
- Confirm initialization preserves an existing valid ledger and rejects a conflicting non-empty target.
- Confirm changing a domain label does not move or rename a decision solely because of taxonomy.