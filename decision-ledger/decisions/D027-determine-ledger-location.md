---
status: active
domain: ledger
id: D027
title: "Determine ledger location"
---
## Requirement

Every project has one predictable, project-contained location for its authoritative decision ledger.

## Question

Where must the skill locate or create a project's decision ledger?

## Input facts

- `project.detected-root`
  - Kind: root
  - Authority: runtime project-root resolver
- `project.explicit-ledger-path`
  - Kind: root
  - Authority: project instructions or user statement

## Invariants

The resolved ledger stays inside the detected project root and no competing ledger is created.

## Policy

Use an explicit project-contained path when supplied; otherwise use the nearest Git root, falling back to the workspace root, plus `decision-ledger`.

## Output fact

- Name: `package.ledger-location`
- Meaning: The authoritative repository-relative path of the project's decision ledger.
- Shape: explicit project-contained path when supplied; otherwise `./decision-ledger`
- Atomicity: A project resolves to exactly one ledger directory.

## Enforcement

`installation_guard.project_root_for` must resolve the active Git or workspace root and reject a target outside it; the skill lookup workflow must reuse a conforming ledger before creation.

## Consumers

- D028 initialization
- D037 execution boundary
- All ledger workflows

## Verification

- Exercise every meaningful policy branch using the authoritative inputs.
- Prove the invariant and rejection behavior at the named enforcement boundary.
