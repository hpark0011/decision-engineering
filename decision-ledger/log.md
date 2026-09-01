# Decision log

Append semantic creates, edits, renames, supersessions, retirements, restorations, deletions, and schema changes. Use Git for textual history.

## \[2026-08-20\] create | D001 | Determine intent authority

Reason: The framework needs one durable authority for intended behavior.

Changed:

- Established the decision ledger as the source code of intent.

Affected:

- `framework.intent-authority`
- D003, D008, framework maintainers, and implementation reviewers

## \[2026-08-20\] create | D002 | Determine behavior authority

Reason: The framework must distinguish intended behavior from evidence of actual behavior.

Changed:

- Established implementation and runtime observations as authoritative behavior evidence.

Affected:

- `framework.behavior-authority`
- D003, D012, diagnostics, and implementation review

## \[2026-08-20\] create | D003 | Resolve intent behavior divergence

Reason: Intent-behavior mismatches require explicit normative adjudication.

Changed:

- Required a human to choose whether intent or behavior changes before repair proceeds.

Affected:

- `framework.divergence-resolution`
- D008, ledger maintenance, and implementation repair

## \[2026-08-20\] create | D004 | Determine decision atomicity

Reason: Each uncertainty needs one independently correctable owner.

Changed:

- Adopted the one-question, one-policy, one-output-fact rule and four split tests.

Affected:

- `framework.decision-atomicity`
- D005, D006, D012, D013, record authors, and lint review

## \[2026-08-20\] create | D005 | Determine fact authority

Reason: Every consumed fact needs one deterministic correction site.

Changed:

- Required one external authority for root facts and one producing decision for derived facts.

Affected:

- `framework.fact-authority`
- D006, D008, D009, D010, D014, and graph validation

## \[2026-08-20\] create | D006 | Determine decision record contract

Reason: Humans, agents, and tools need one compatible record shape.

Changed:

- Established the schema-complete validity test for decision Markdown.

Affected:

- `framework.record-validity`
- D007, D017, decision authors, `ledger_new.py`, and `ledger_lint.py`

## \[2026-08-20\] create | D007 | Determine ledger storage model

Reason: The framework needs one navigable and taxonomy-stable ledger layout per system.

Changed:

- Adopted a schema-constrained Markdown directory with flat authoritative decisions and generated views.

Affected:

- `framework.ledger-storage-model`
- D014, D015, D018, initialization, and maintenance tooling

## \[2026-08-20\] create | D008 | Route framework changes

Reason: Maintenance must reuse existing ownership and create authority only for new uncertainty.

Changed:

- Established consume, edit, create, and reconcile as the exclusive change routes.

Affected:

- `framework.change-route`
- D018, the Decision Engineering workflow, and change review

## \[2026-08-20\] create | D009 | Determine projection eligibility

Reason: Consumer representations must not become hidden policy owners.

Changed:

- Limited projections to judgment-free representational changes.

Affected:

- `framework.projection-eligibility`
- D010, projection designers, and decision reviewers

## \[2026-08-20\] create | D010 | Determine consumer fact access

Reason: Consumers must reuse authoritative answers instead of reconstructing them.

Changed:

- Required consumer access through an owning output contract or faithful projection.

Affected:

- `framework.consumer-access`
- Cross-domain integrations and implementation review

## \[2026-08-20\] create | D011 | Determine enforcement boundary

Reason: Framework invariants need boundaries that cannot be bypassed by another consumer.

Changed:

- Distinguished commit or rejection enforcement from UI presentation and warnings.

Affected:

- `framework.enforcement-sufficiency`
- D012, decision authors, and implementation reviewers

## \[2026-08-20\] create | D012 | Determine verification target

Reason: Verification must test the authoritative path without duplicating policy.

Changed:

- Required branch, invariant, and enforcement evidence against the owning decision path.

Affected:

- `framework.verification-sufficiency`
- D017, test authors, and release review

## \[2026-08-20\] create | D013 | Determine domain membership

Reason: Domain boundaries should localize change and correction rather than mirror implementation layers.

Changed:

- Based primary domain assignment on shared facts, invariants, and change locality.

Affected:

- `framework.domain-membership`
- D014, generated views, routing, and impact analysis

## \[2026-08-20\] create | D014 | Validate dependency graph

Reason: Ownership and downstream impact require a resolvable acyclic fact-decision graph.

Changed:

- Established graph validity, resolution, uniqueness, and cycle rules.

Affected:

- `framework.graph-validity`
- D017, D018, rendering, lint, and impact analysis

## \[2026-08-20\] create | D015 | Determine decision identity

Reason: Decision references must survive rename, regrouping, and lifecycle changes.

Changed:

- Made stable D-prefixed IDs permanent and non-reusable.

Affected:

- `framework.decision-identity`
- D016, filenames, references, logs, specifications, tests, and commits

## \[2026-08-20\] create | D016 | Determine semantic logging

Reason: Git line history does not explain why the decision model changed or its impact.

Changed:

- Required append-only semantic entries for meaningful decision and schema changes.

Affected:

- `framework.semantic-log-obligation`
- D017, `log.md`, lifecycle review, and impact review

## \[2026-08-20\] create | D017 | Determine ledger acceptance

Reason: Maintainers need one explicit gate for structural, generated, and normative completeness.

Changed:

- Required lint, render, lint, semantic history, warning review, and resolved normative obligations.

Affected:

- `framework.ledger-acceptance`
- Completion reporting, implementation planning, and adoption review

## \[2026-08-20\] create | D018 | Determine ledger lookup scope

Reason: Maintainers need a bounded path from a request to authoritative decision records.

Changed:

- Established index-first routing and the smallest-candidate-set lookup rule.

Affected:

- `framework.lookup-scope`
- Decision Engineering maintainers, D008 route evidence, review, and reconciliation

## \[2026-08-20\] schema-change | decision records | Move identity metadata to YAML frontmatter

Reason: Decision identity and routing metadata were duplicated between the filename, H1, and body, producing redundant rendered documents and weakening machine-readable metadata.

Changed:

- Made `status`, `domain`, `id`, and `title` required YAML frontmatter fields.
- Removed the repeated H1, status, and domain lines from D001–D018.
- Required decision bodies to begin with `## Requirement`.
- Added optional frontmatter `superseded_by` for superseded records.

Affected:

- D001–D018
- `SCHEMA.md`
- `index.md`
- `generated/graph.mmd`
- Decision authoring, linting, rendering, and Obsidian presentation

## \[2026-08-21\] create | D019 | Determine package identity

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.identity` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D020 | Determine canonical skill source

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.canonical-skill-source` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D021 | Determine packaged skill contents

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.skill-content-contract` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D022 | Determine Claude Code distribution

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.claude-code-distribution` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D023 | Determine Codex distribution

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.codex-distribution` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D024 | Determine Cursor distribution

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.cursor-distribution` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D025 | Determine editable project installation

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.editable-installation` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D026 | Prevent duplicate skill authority

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.duplicate-authority-policy` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D027 | Determine ledger location

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.ledger-location` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D028 | Initialize a missing ledger

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.ledger-initialization` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D029 | Determine release versioning

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.release-version` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D030 | Generate distribution metadata

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.distribution-metadata` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D031 | Determine macOS support

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.macos-support` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D032 | Determine Linux support

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.linux-support` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D033 | Determine Windows support

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.windows-support` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D034 | Determine public release source

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.public-release-source` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D035 | Determine package licensing

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.license` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D036 | Determine support channels

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.support-routing` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D037 | Constrain packaged execution

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.execution-boundary` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D038 | Determine package acceptance

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.acceptance` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] create | D039 | Determine release maturity gate

Reason: The package requirement introduced a new authoritative question that the existing framework decisions do not resolve.

Changed:

- Established `package.release-maturity` from the packaging-owner interview and its declared dependencies.

Affected:

- Package manifests, installation documentation, release validation, and downstream packaging decisions that consume this fact.

## \[2026-08-21\] edit | D030 | Generate distribution metadata

Reason: Official Claude Code and Codex GitHub installation flows require repository marketplace catalogs in addition to plugin manifests.

Changed:

- Added generated Claude and Codex marketplace catalogs to `package.distribution-metadata`.

Affected:

- `.claude-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`
- GitHub installation commands, metadata generation, and package acceptance

## \[2026-08-21\] edit | D026-D028, D030-D033, D037-D038 | Bind package enforcement

Reason: The package implementation now provides concrete mutation, metadata, platform, execution, and acceptance boundaries for previously recorded obligations.

Changed:

- Bound duplicate prevention and project containment to `installation_guard.py`.
- Bound safe initialization to `ledger_init.py`.
- Bound metadata drift detection and package acceptance to repository validation scripts.
- Bound platform support to the GitHub Actions operating-system matrix.

Affected:

- `package.duplicate-authority-policy`, `package.ledger-location`, and `package.ledger-initialization`
- `package.distribution-metadata`, platform support facts, `package.execution-boundary`, and `package.acceptance`
- Packaged scripts, tests, CI, and release readiness

## \[2026-08-21\] edit | D025 | Determine editable project installation

Reason: An exact skills.sh installation showed that `--copy` creates independently editable host trees, violating the single-authority invariant.

Changed:

- Required the default skills.sh linked installation instead of `--copy` so one project payload remains canonical.

Affected:

- `package.editable-installation`
- README installation commands, duplicate detection, and lifecycle acceptance

## \[2026-08-21\] schema-change | D006 | Require decision recency metadata

Reason: Every decision record needs visible recency metadata so maintainers and agents can tell when its semantics were last updated.

Changed:

- Required `updated_at` in decision frontmatter as an ISO calendar date (`YYYY-MM-DD`).
- Required semantic decision edits to refresh `updated_at`.
- Migrated D001-D039 and updated templates, examples, parsing, and lint enforcement.

Affected:

- `framework.record-validity`
- D001-D039
- `SCHEMA.md`, the bundled ledger schema, skill instructions, record templates, examples, tests, and linting

## \[2026-09-01\] schema-change | D006 | Simplify the decision record contract

Reason: The record duplicated recency already owned by semantic history and version control, and the required Projection field duplicated the authoritative output fact with an implementation representation.

Changed:

- Removed `updated_at` from authoritative frontmatter.
- Replaced the singular `Invariant` heading with one `Invariants` section that may list multiple constraints.
- Ordered the decision body as inputs, invariants, policy, output, enforcement, consumers, and verification.
- Removed the required `Projection` section and required consumers to read the authoritative output fact directly.
- Defined mechanical consumer representations as implementation bindings and judgment-bearing representations as separate decisions.
- Migrated D001-D039 and updated templates, examples, parsing, rendering, lint enforcement, and tests.

Affected:

- `framework.record-validity`
- D001-D039
- `SCHEMA.md`, the bundled ledger schema, skill instructions, record templates, examples, tests, rendering, and linting

## \[2026-09-01\] rename | D009 | Determine consumer representation treatment

Reason: Projection eligibility was removed from the record schema, but the boundary between mechanical representation and new judgment remains an authoritative framework decision.

Changed:

- Renamed D009 from “Determine projection eligibility.”
- Replaced `framework.projection-eligibility` with `framework.consumer-representation-treatment`.
- Classified formatting, renaming, omission, and transport as implementation details while requiring a separate decision for judgment-bearing representations.

Affected:

- D005 — Determine fact authority
- D010 — Determine consumer fact access
- Consumer integration and decision review

## \[2026-09-01\] edit | D010, D013 | Align consumer access and domain ownership

Reason: Removing projections and adopting an authority-and-consistency definition of domain changed the rules for consumer access and domain assignment.

Changed:

- Required consumers to read authoritative output facts directly, with mechanical representation limited to implementation bindings.
- Defined a domain as the smallest authority and consistency boundary that preserves related invariants.
- Prohibited domains from writing another domain's facts directly.

Affected:

- `framework.consumer-access`
- `framework.domain-membership`
- Consumer integrations, architecture routing, and impact analysis