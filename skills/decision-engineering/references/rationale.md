# Structural rationale

Use this file to explain or contest rules. Treat `SKILL.md`, the ledger's `SCHEMA.md`, and deterministic lint results as operational authority.

## Why decisions are the unit

A task describes work; a decision removes one uncertainty. Naming the question, inputs, policy, output, and owner creates a bounded correction site. If a record produces no fact, it is probably analysis, presentation, or work rather than a decision. If it produces independently variable facts, it hides multiple uncertainties and must be split.

## Why every fact has one authority

When several places can author the same proposition, a wrong value does not identify where correction belongs. One external authority per root fact and one producing decision per derived fact make the repair path deterministic. Consumers use the resolved fact rather than rebuilding policy from raw inputs.

## Why projections cannot decide

Projections adapt representation for consumers. Allowing them to add judgment creates a second, less visible decision owner. If representation requires a new normative choice, model that uncertainty as another decision and fact.

## Why enforcement is not presentation

A disabled button or warning can be bypassed by another UI, API, worker, or agent. Only a commit or rejection boundary can preserve the invariant across every consumer. Presentation may explain the result; enforcement must prevent an invalid result or transition.

## Why intent and behavior remain separate authorities

The ledger states what the system is meant to decide. Code states what it actually does. Declaring either one automatically correct would erase the distinction between a bug and an unrecorded intent change. A human adjudicates divergence, then changes the losing side.

## Why the ledger is a directory of Markdown

One file per decision keeps correction local and makes review proportional to the changed uncertainty. Stable IDs survive renames and domain regrouping. A generated index routes quickly, a generated graph exposes dependencies, and an append-only semantic log explains model changes without duplicating Git's line history.

## Why domains are projections

Domain labels help routing and impact analysis, but domain boundaries can evolve. Keeping decision records flat prevents taxonomy changes from breaking stable references. Derive meaningful boundaries from facts, decisions, and invariants rather than from UI/API/database layers.

## Why deterministic lint matters

Agents exercise judgment while deriving policies and fact boundaries. Mechanical constraints should produce the same verdict every run. Lint catches structural ambiguity—duplicate producers, missing authorities, dangling links, cycles, incomplete records, and stale projections—while humans retain authority over normative correctness.

## Known limits

Lint validates ledger structure, not truth. It cannot prove that the requirement is complete, a structured output is genuinely atomic, prose policy is correct, a projection contains no hidden decision, consumers do not reimplement policy, or an enforcement description binds to real code. Keep those as explicit review and verification obligations.
