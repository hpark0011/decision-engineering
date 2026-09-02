---
title: Decision Ledger
created: 2026-08-20
updated: 2026-09-02
type: concept
tags: [ledger, decision, ownership, projection, verification]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md, raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md, ../skills/decision-engineering/assets/decision-ledger/SCHEMA.md, ../skills/decision-engineering/SKILL.md, ../README.md]
confidence: medium
---

# Decision Ledger

**Defined in glossary:** Decision ledger, Decision architecture, Projection, Stale projection,
Agent skill.

## Current record format

The [bundled schema](../../skills/decision-engineering/assets/decision-ledger/SCHEMA.md) defines the default format. As of
2026-09-02, each record has eight sections: Requirement, Question, Input facts, Invariants,
Policy, Output fact, Enforcement, and Verification. Decision dependencies come from declared
input and output facts. The initialized ledger owns its schema; the skill bundles one default
schema for new ledgers.^[../skills/decision-engineering/assets/decision-ledger/SCHEMA.md]

The ledger may contain multiple policies, and a decision's single `Policy` section may hold
several policies that jointly produce its one output fact. The record states how those policies
combine and resolves any overlap through explicit precedence or conflict rules.^[../skills/decision-engineering/assets/decision-ledger/SCHEMA.md]

## Ledger and projection

The 2026-08-20 glossary snapshot proposed making a skill's `SKILL.md` a projection of its own
design ledger.^[raw/articles/de-glossary.md]

As of 2026-09-02, this repository maintains the skill directly: `SKILL.md` owns
the workflow and the bundled schema owns the default record contract. The repository's own
design ledger has been removed.^[../README.md]

Within a project's ledger, the index and graph remain projections of decision records. The
skill maintains them directly and reviews them against those records. This makes stale views
a review concern without requiring a parser. See [[authority-and-projection]].^[../skills/decision-engineering/SKILL.md]

## What good looks like

The 2026-08-20 README snapshot proposed these success criteria:^[raw/articles/de-readme.md]

- Compact and simple
- A table
- Dependencies written explicitly — what it depends on, where it's used, who owns it
- Those dependencies must be sufficient to construct a dependency graph

The current schema implements the dependency-graph requirement through input and output facts.
Each input identifies an external authority or a producing decision, so the graph can be
derived without maintaining a separate usage list.^[../skills/decision-engineering/assets/decision-ledger/SCHEMA.md]

Those links support impact analysis: reviewers can trace which decisions depend on a changed
fact, then inspect their policies and verification. The current skill performs that review
directly against the project's schema.^[../skills/decision-engineering/SKILL.md]

## A proposed conversational write path

[[productizing-decision-engineering]] proposes maintaining the ledger from ordinary chat without
putting extraction on the synchronous response path. Idle, thread-end, or explicit topic-change
events trigger a background pass over only the unprocessed conversation delta. Candidate
commitments are compared with existing entries before the ledger is updated and the change is
appended to a chronological log.^[raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md]

This is a candidate answer to how the ledger stays current, not yet a validated mechanism. Its
quality depends on reliably separating decisions from brainstorming, preserving why and
authoritative inputs, making repeated events idempotent, and giving people a lightweight way to
correct what was recorded.^[raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md]

## Relationship to this wiki

This wiki is itself a projection problem. `GLOSSARY.md` holds definitional authority, the
README holds intent and rationale, and these pages hold synthesis — see the SCHEMA rule that
forbids restating definitions here. The same discipline the ledger demands.

## Open questions

- How well do the bundled schema and worked example support correction in projects that adopt them?
- Asynchronous chat extraction proposes how conversational decisions enter the ledger, but how
  the ledger stays in sync with code and other authoritative systems remains unspecified.
- At what system size does the index need more routing structure or maintenance tooling?

## Related

[[decision-engineering]] · [[anatomy-of-a-decision]] · [[authority-and-projection]] · [[domain-boundaries]]
