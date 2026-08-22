---
title: Schema as Agent Constraint
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [policy, enforcement, agent-harness, context-engineering, methodology]
sources: [raw/articles/karpathy-llm-wiki.md]
confidence: medium
---

# Schema as Agent Constraint

## Definition

The schema file (`CLAUDE.md`, `AGENTS.md`, or `SCHEMA.md`) is what turns an agent from a
generic chatbot into a **disciplined maintainer**. It declares the structure, the conventions,
the tag taxonomy, and the workflow to follow on ingest, query, and lint. Karpathy calls it the
key configuration file of the whole system.

## What it actually does

Without a schema, every ingest is a fresh judgment call: what to name the file, whether a
concept warrants its own page, which tags to use, whether to overwrite or annotate a
contradiction. An agent making those calls independently each session produces a wiki that is
internally inconsistent in ways that compound. The schema converts recurring judgment calls
into pre-resolved policy.

Concretely it fixes: naming, required frontmatter, minimum outbound links, page-creation
thresholds, tag vocabulary, split/archive triggers, and what to do when sources conflict.

## Relevance to decision engineering

This is the closest thing in the source to [[decision-engineering]]'s own thesis. The schema is a
**policy document with a single home** — the agent doesn't infer conventions from surrounding
pages (which would make every page a competing authority), it reads one file that answers
"how do we decide this?" for the whole system.

Two properties are worth naming explicitly:

- **It removes randomness from surprise.** When the agent does something unexpected, the schema
  is the first place to look, and the fix goes in one place. Surprise stays local.
- **Its enforcement is weak.** The schema states policy but nothing prevents violation at write
  time; lint detects violations after the fact. In the framework's terms this is verification
  without enforcement — acceptable for a personal wiki, insufficient where a violation is
  costly. It is arguably **weak ownership**: a nominal home other writes can bypass. See
  [[decision-entropy]].

The schema also has the co-evolution problem noted in [[three-layer-knowledge-architecture]]:
human and agent both write it, so authority over the conventions is shared.

## Open questions

- Should tag taxonomy violations be a hard write-time failure rather than a lint finding?
- The schema is described as domain-specific and hand-tuned. Is there a portable core, or is
  every schema necessarily bespoke?

## Related

[[three-layer-knowledge-architecture]] · [[wiki-operations]] · [[compiled-knowledge-base]]
