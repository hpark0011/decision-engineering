---
status: active
domain: operations
id: D018
title: "Determine ledger lookup scope"
updated_at: 2026-08-21
---
## Requirement

Maintainers must find the authoritative owner of a request quickly without loading or reinterpreting the entire decision system.

## Question

Which existing decision records should be opened for the current maintenance request?

## Input facts

- `maintenance.lookup-query`
  - Kind: root
  - Authority: Current human or project requirement
- `framework.ledger-storage-model`
  - Kind: derived
  - Produced by: D007
- `framework.change-route`
  - Kind: derived
  - Produced by: D008
- `framework.graph-validity`
  - Kind: derived
  - Produced by: D014

## Output fact

- Name: `framework.lookup-scope`
- Meaning: The smallest ordered set of authoritative decision IDs that can route and trace the current request.
- Shape: `ordered list of D-prefixed decision IDs`
- Atomicity: The list is one lookup answer for one query and is consumed as a complete candidate scope.

## Invariant

Lookup starts from generated routing information but resolves every selected result to authoritative decision files before policy is used.

## Policy

Search `index.md` by output fact, question, requirement terms, input fact, consumer, and domain; open the smallest candidate set, follow fact dependencies only as needed, and search all decision files only when the generated index cannot route the query.

## Enforcement

The Decision Engineering maintenance workflow must read `SCHEMA.md` and `index.md` first, then restrict initial decision reads to this result unless the index demonstrably fails to route the request.

## Projection

`framework.lookup-scope.public`

Exposes selected IDs, titles, and links in lookup order without copying their policy text.

## Consumers

- Decision Engineering maintainers and agents
- D008 route evidence and downstream impact analysis
- Review and reconciliation workflows

## Verification

- Route representative queries by output, question, input, consumer, domain, and requirement term.
- Confirm every selected index row resolves to the matching authoritative record.
- Confirm full-directory search occurs only for an unrouteable query and that the failure is reported.