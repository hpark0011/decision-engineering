---
name: decision-engineering
description: Run Decision Engineering by locating, creating, changing, validating, and tracing a Markdown decision ledger whose decisions remain explicit, authoritative, enforceable, traceable, and correctable. Use when a requirement, feature, architecture change, bug, policy, or implementation choice needs to be routed to an existing decision or expressed as a new one; when logic ownership or domain boundaries are unclear; when reviewing for duplicated policy, ambiguous fact authority, missing enforcement, or hidden decisions; and when reconciling intended decisions with code behavior.
---

# Decision Engineering

This file owns the workflow for locating, creating, changing, reviewing, and maintaining a ledger. The project's ledger `SCHEMA.md` owns its structure, fields, and invariants. Follow that schema when authoring or reviewing records. The [bundled schema](assets/decision-ledger/SCHEMA.md) supplies the default for new ledgers.

Treat the decision ledger as the source code of intent and the implementation as the source code of behavior. Treat disagreement as a divergence requiring human adjudication: either fix behavior to match recorded intent or change the ledger before changing behavior.

## Locate the ledger

1. Resolve the project root as the nearest Git root, falling back to the active host workspace root.
2. Run `python3 <skill-dir>/scripts/installation_guard.py <project-root>` before any ledger mutation. If it reports multiple applicable copies, stop and require the user to keep either the managed global plugin or one editable project copy.
3. Look inside the project root for an existing ledger named by project instructions or identifiable by its `SCHEMA.md` and decision records.
4. Use the existing location and schema when found. Maintain one ledger per system; never create a competing ledger.
5. If no ledger exists, use `decision-ledger/` at the project root unless the user or project instructions specify another location. Resolve the target, including symlinks, and keep it inside the project root.
6. Initialize that location by copying the bundled schema and creating the directories, empty index, semantic log, and Mermaid graph it defines. Perform this setup directly without requiring a separate user step. Preserve existing files; if the target directory contains unrelated content, resolve the location before writing.
7. Read the ledger's complete `SCHEMA.md`, then `index.md`, before changing anything.
8. Search `index.md` by output fact, question, requirement terms, input fact, and domain. Open the smallest candidate set. Search all decision files only when the index cannot route the request.

Maintain the ledger files directly and review them against the project's schema.

## Route before deriving

Classify the requested change:

- **Consume:** Reuse an existing output fact. No ledger change is needed when its meaning and dependencies stay the same.
- **Edit:** Change the existing decision that owns the affected output fact when the question, inputs, policy, invariants, enforcement, output meaning, or verification changes.
- **Create:** Add a decision only for an unresolved question with a new authoritative output fact.
- **Reconcile:** For a bug or mismatch, trace the wrong observation backward through output fact → decision → policy and invariants → input authorities → enforcement → verification. Let a human decide whether intent or behavior changes.

State the classification and the authoritative decision ID before editing code or ledger files.

## Derive or change a decision

1. Clarify the requested outcome and uncertainty, then inspect the governing decision and relevant implementation.
2. Trace the inputs to their authorities and work through the proposed result. Apply the schema's atomicity criteria before deciding whether to split the decision.
3. Draft or revise the record using the schema's required structure and field definitions. Check the policies against the invariants, and identify the enforcement and verification work needed to make the intent real. When an invariant, enforcement obligation, or verification obligation genuinely does not apply, record the schema-approved reason instead of omitting the section or inventing a binding.
4. Create a new Markdown file only after routing proves it is necessary. Select an unused ID by checking both existing records and semantic history, then write the complete record according to the project's schema.
5. Update metadata and filenames to reflect the accepted change, following the schema's identity and lifecycle rules. Retain adopted decisions through supersession or retirement; delete only accidental records that were never accepted.

Read [references/worked-example.md](references/worked-example.md) when the correct create/edit/consume boundary is unclear. Read [references/rationale.md](references/rationale.md) when explaining or contesting a structural rule.

## Change the schema

Change the project's schema when the record contract itself needs to change. Identify affected records, migrate them in the same change, and review the result against the updated contract. Record the migration and its reason in the semantic log. A bundled schema update does not automatically replace an existing project's schema.

## Record the semantic delta

Append a `log.md` entry for each accepted semantic, identity, lifecycle, or schema change, using the schema's entry format and change kinds. Walk downstream from every changed output fact and record the impact on decisions, code, and verification. Use version control for textual history; wording-only corrections do not need a semantic entry.

## Review and refresh the views

Review changed records and their dependencies against the project's complete schema. Assess policy correctness, actual enforcement and verification bindings, and every claimed not-applicable reason as well as structural conformance.

After a semantic change, edit the index and Mermaid graph directly from the records according to the schema's view definitions. Trace each affected reference to its source record and check both views for stale or missing entries. Repair confirmed defects and review the affected records and views again.

Report unresolved findings. Do not call a ledger implementation-ready while bindings, authorities, enforcement, verification, or open normative questions remain unresolved. A schema-approved not-applicable reason resolves the record obligation but remains an explicit limitation to report.

## Hand off the result

Report:

- the route taken: consume, edit, create, or reconcile;
- the decision IDs and output facts involved;
- the ledger files changed and semantic log entries added, or why no ledger mutation was required;
- downstream decisions and code affected;
- schema review and view refresh results;
- schema-approved not-applicable reasons and their limitations;
- unresolved questions, premises, or implementation bindings;
- whether code behavior now matches recorded intent.

Require behavior-changing implementation work to cite the decision IDs that justify it or include the ledger delta. Let specifications reference decision IDs rather than restating policies.
