---
status: active
domain: lifecycle
id: D015
title: "Determine decision identity"
updated_at: 2026-08-21
---
## Requirement

References to adopted decisions must survive clearer titles, domain regrouping, and lifecycle changes.

## Question

Which stable identifier must a candidate decision record use?

## Input facts

- `framework.ledger-storage-model`
  - Kind: derived
  - Produced by: D007
- `ledger.existing-identifiers`
  - Kind: root
  - Authority: decision-ledger/decisions directory observer
- `ledger.record-lifecycle`
  - Kind: root
  - Authority: Maintainer proposing the ledger change

## Output fact

- Name: `framework.decision-identity`
- Meaning: The permanent D-prefixed identifier assigned to one decision record.
- Shape: `D followed by at least three decimal digits`
- Atomicity: The output is one indivisible identifier for one decision.

## Invariant

An adopted ID is never renumbered, reused, or changed by rename, edit, domain reassignment, supersession, retirement, or restoration.

## Policy

Preserve the existing ID for every lifecycle transition of an adopted record; for a genuinely new decision, allocate the next unused numeric ID above the greatest identifier ever present and never recycle deleted, retired, or superseded IDs.

## Enforcement

`ledger_new.py` must allocate the next ID, `ledger_lint.py` must reject filename and heading mismatches or duplicate IDs, and lifecycle review must reject reuse of historical IDs.

## Projection

`framework.decision-identity.public`

Exposes the stable ID and current title without deriving identity from title, domain, or path.

## Consumers

- D016 — Determine semantic logging
- Decision filenames, references, log entries, specifications, tests, and commits
- `ledger_new.py` and `ledger_lint.py`

## Verification

- Rename and re-domain a fixture decision and confirm its ID remains unchanged.
- Supersede, retire, and restore a fixture without reusing its ID.
- Confirm new allocation remains above all historical identifiers.