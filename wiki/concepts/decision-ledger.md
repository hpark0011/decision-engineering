---
title: Decision Ledger
created: 2026-08-20
updated: 2026-08-21
type: concept
tags: [ledger, decision, ownership, projection, verification]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md, raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md]
confidence: medium
---

# Decision Ledger

**Defined in glossary:** Decision ledger, Decision architecture, Projection, Stale projection,
Agent skill.

## What it is

The authoritative description of the decisions that govern a system. Per decision it records the
facts and constraints involved, the policy that resolves it, its owner, its consumers, and how
it is verified — plus the business requirement and invariants above them.

The critical framing: **the ledger describes what the implementation must mean. It is not the
implementation.**

## Ledger and projection

For an agent skill, the ledger is the authoritative design and `SKILL.md` is an *executable
projection* of it. This is the framework applied reflexively — the same relationship holds
between a ledger and any artifact derived from it (API docs, config, onboarding material).

The consequence is the failure mode the glossary names **stale projection**: if the ledger
changes and the derived `SKILL.md` doesn't, the skill is stale. Traceability and verification
are what catch that. See [[authority-and-projection]].

## What good looks like

From the README's own success criteria:^[raw/articles/de-readme.md]

- Compact and simple
- A table
- Dependencies written explicitly — what it depends on, where it's used, who owns it
- Those dependencies must be sufficient to construct a dependency graph

The dependency-graph requirement is the sharpest constraint. It means the ledger's columns
aren't descriptive prose — they're edges. A decision that names its facts, its owner, and its
consumers is a node with typed in- and out-edges, and the graph falls out mechanically.

That graph is what makes the ledger machine-checkable rather than merely documented: you can
ask which decisions change when a fact changes, which decisions have no owner, and which have
no verification, without reading the prose.

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

- No ledger exists yet in this workspace. The README describes what a good one looks like but
  the sources contain no worked example, so the format is unvalidated.
- Asynchronous chat extraction proposes how conversational decisions enter the ledger, but how
  the ledger stays in sync with code and other authoritative systems remains unspecified.
- At what system size does a single table stop being compact? The split rule is unstated.

## Related

[[decision-engineering]] · [[anatomy-of-a-decision]] · [[authority-and-projection]] · [[domain-boundaries]]
