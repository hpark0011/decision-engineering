---
title: Compiled Knowledge Base
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [knowledge-base, context-engineering, rag, drift, projection]
sources: [raw/articles/karpathy-llm-wiki.md]
confidence: medium
---

# Compiled Knowledge Base

## Definition

A knowledge base whose synthesis is **computed once at write time and then kept current**,
rather than re-derived from raw documents at each query. The compiled artifact — a set of
interlinked markdown pages — sits between the reader and the raw sources.

## The contrast with RAG

Retrieval-augmented generation retrieves chunks at query time and generates an answer from
them. Nothing accumulates. A question requiring synthesis across five documents forces the
model to find and reassemble the same fragments every time it is asked.

| | RAG | Compiled wiki |
|---|---|---|
| When synthesis happens | Query time, every time | Ingest time, once |
| Cross-references | Re-derived per query | Already written |
| Contradictions | Invisible unless retrieved together | Flagged when the conflicting source arrived |
| Cost of a hard question | Full re-derivation | Read the page |
| Artifact left behind | None | The wiki |

## Why it compounds

Every ingest and every good query answer can be filed back, so exploration accrues to the
artifact instead of dissolving into chat history. The wiki gets richer with use rather than
staying flat.

## Relevance to decision engineering

This is the same move [[decision-engineering]] makes on intent. A scattered set of documents
that each imply an answer is the knowledge-base analogue of scattered responsibility — the
reader (human or agent) must re-adjudicate the answer on every read, and different readers land
differently. Compiling to one authoritative page is the knowledge-base form of a decision home.
See [[schema-as-agent-constraint]] for the layer that enforces it.

The failure mode compiling prevents is exactly the launch-email example in
[[decision-engineering]]: two live sources for the same fact, the reader silently picking the
more recent one. Note the limit of the analogy — a compiled page is a **projection**, not an
authority. If the wiki starts deciding things the sources don't say, it has become a second
owner of the meaning, which [[authority-and-projection]] forbids. That risk is the price of
compiling early.

## Open questions

- Compiling early risks freezing a synthesis before the evidence justifies it. Where is the
  line between a compiled claim and a premature one? `confidence` frontmatter is a partial
  answer, not a complete one.
- At what corpus size does the index-first navigation in [[wiki-operations]] stop working and
  real search become necessary? The source claims ~100 sources / a few hundred pages.

## Related

[[three-layer-knowledge-architecture]] · [[wiki-operations]] · [[schema-as-agent-constraint]]
