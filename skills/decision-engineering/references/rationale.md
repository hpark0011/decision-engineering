# Structural rationale

Use this file to explain or contest rules. [SKILL.md](../SKILL.md) owns the workflow; the project's ledger `SCHEMA.md` owns the record contract. The [bundled schema](../assets/decision-ledger/SCHEMA.md) supplies the default for new ledgers.

## Why decisions are the unit

A task describes work; a decision removes one uncertainty. Naming the question, inputs, policies, output, and owner creates a bounded correction site. If a record produces no fact, it is probably analysis, presentation, or work rather than a decision. If it produces independently variable facts, it hides multiple uncertainties and must be split.

Several policies can jointly answer one question. Task eligibility, work preservation, and assignee readiness can all govern the same handoff result. Keeping their combination explicit in one decision preserves a single place to correct that result. Policy count alone does not determine how many decisions are needed.

## Why every fact has one authority

When several places can author the same proposition, a wrong value does not identify where correction belongs. One external authority per root fact and one producing decision per derived fact make the repair path deterministic.

## Why enforcement is not presentation

A disabled button or warning can be bypassed by another UI, API, worker, or agent. Only a commit or rejection boundary can preserve the invariant across every entry point. Presentation may explain the result; enforcement must prevent an invalid result or transition.

## Why intent and behavior remain separate authorities

The ledger states what the system is meant to decide. Code states what it actually does. Declaring either one automatically correct would erase the distinction between a bug and an unrecorded intent change. A human adjudicates divergence, then changes the losing side.

## Why the ledger is a directory of Markdown

One file per decision keeps correction local and makes review proportional to the changed uncertainty. Stable IDs survive renames and domain regrouping. An index routes quickly, a graph exposes dependencies, and an append-only semantic log explains model changes without duplicating Git's line history. The index and graph derive their content from the records even when maintained directly.

## Why domains are routing metadata

Domain labels help routing and impact analysis, but domain boundaries can evolve. Keeping decision records flat prevents taxonomy changes from breaking stable references. Derive meaningful boundaries from facts, decisions, and invariants rather than from UI/API/database layers.

## Why review uses the project's schema

Maintainers can inspect and change ordinary Markdown without keeping a parser's rules synchronized with the schema. Reviewing against the project's own contract also accommodates deliberate schema changes. Automation can be added when repeated maintenance problems justify its cost.

## Known limits

Direct review can miss structural mistakes and stale views. A review must also assess whether the requirement is complete, the output is atomic, the policies are correct, and enforcement descriptions bind to real code. Those conclusions need evidence beyond a well-formed record.
