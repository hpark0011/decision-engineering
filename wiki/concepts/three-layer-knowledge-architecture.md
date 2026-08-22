---
title: Three-Layer Knowledge Architecture
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [knowledge-base, ownership, context-engineering, agent-harness]
sources: [raw/articles/karpathy-llm-wiki.md]
confidence: medium
---

# Three-Layer Knowledge Architecture

## Definition

The structural split that makes a [[compiled-knowledge-base]] maintainable: three layers with
**disjoint write ownership**.

| Layer | Contents | Who writes | Mutability |
|---|---|---|---|
| Raw sources | Articles, papers, transcripts, assets | The human (curation only) | Immutable |
| The wiki | Entity, concept, comparison, query pages | The agent, entirely | Continuously rewritten |
| The schema | Conventions, taxonomy, workflows | Human and agent, co-evolved | Deliberate, versioned |

## Why the split matters

Each layer has exactly one writer, so no layer can be corrupted by the layer above or below it.
Raw sources stay trustworthy because nothing may edit them — corrections live in the wiki, not
in the source. The wiki can be regenerated or aggressively revised because it is derived, not
original. The schema changes slowly because it governs the other two.

The division of labor follows: the human curates sources, directs analysis, and asks the
questions; the agent does the summarizing, cross-referencing, filing, and bookkeeping.

## Relevance to decision engineering

This is an ownership boundary in the [[decision-engineering]] sense — the answer to "who alone has
authority here?" differs per layer, and that is what makes the whole thing hold. A wiki where
the agent edits raw sources has no source of truth left; a wiki where the human hand-edits
pages accumulates unowned drift the agent won't reconcile.

The layers map onto [[anatomy-of-a-decision]]: raw sources are the **facts**, the wiki is the
**projection** everyone reads instead of re-deciding, and the schema is the **policy** that
determines how facts become the projection. The mapping is suggestive rather than exact — the
wiki holds no invariant that the schema actually prevents from being violated, which is the
layer this architecture is thinnest on. See [[wiki-operations]], where lint is the only
verification-shaped step, and [[authority-and-projection]] for why a projection that drifts
becomes a competing authority.

## Open questions

- Enforcement is advisory here: nothing mechanically stops an agent from editing `raw/`. Is a
  convention plus a lint check sufficient, or does this need a real write barrier?
- The schema is described as co-evolved, which means its ownership is shared. Shared ownership
  is exactly what decision engineering warns against. Does the schema need a single owner?

## Related

[[compiled-knowledge-base]] · [[schema-as-agent-constraint]] · [[wiki-operations]]
