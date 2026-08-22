---
title: Wiki Operations — Ingest, Query, Lint
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [methodology, knowledge-base, verification, drift]
sources: [raw/articles/karpathy-llm-wiki.md]
confidence: medium
---

# Wiki Operations — Ingest, Query, Lint

The three operations that maintain a [[compiled-knowledge-base]].

## Ingest

A source lands in `raw/`. The agent reads it, discusses takeaways with the human, writes or
updates the pages it touches, refreshes the index, and appends to the log. One source may touch
10–15 pages — that fan-out is the compounding effect working, not a sign of sprawl.

Karpathy's stated preference is one source at a time with the human in the loop, reading the
summaries and steering emphasis. Batch ingest with less supervision is possible and cheaper.

## Query

The agent reads `index.md` to locate relevant pages, drills into them, and synthesizes with
citations. The important move: **good answers get filed back** as new pages. A comparison, an
analysis, a connection discovered mid-conversation — these are as valuable as ingested sources
and shouldn't evaporate into chat history.

## Lint

A periodic health check. Look for contradictions between pages, stale claims newer sources have
superseded, orphan pages with no inbound links, concepts mentioned everywhere but lacking a
page, missing cross-references, and data gaps a web search could fill.

Lint is the only verification-shaped operation in the system — the mechanism by which the wiki
detects that it has diverged from its own schema. Its weakness is that it runs on request
rather than on write. See [[schema-as-agent-constraint]].

## The two navigation files

**`index.md` is content-oriented.** A catalog of every page with a link and a one-line summary,
grouped by category. Updated on every ingest. Read first on every query. At moderate scale
(~100 sources) this replaces embedding-based retrieval entirely.

**`log.md` is chronological.** Append-only, one entry per action. A consistent prefix like
`## [2026-04-02] ingest | Article Title` makes it greppable — `grep "^## \[" log.md | tail -5`
returns recent activity. The log is how a fresh session learns what has already been done.

The two answer different questions: index answers "what do we know?", log answers "what have we
done?". Keeping them separate is deliberate — merging them would give both jobs to one file and
neither would be read reliably.

## Relevance to decision engineering

Ingest is where new facts arrive and existing conclusions must be re-checked against them —
structurally the same as re-evaluating a decision when its authoritative facts change. Lint is
the detection step, and maps cleanly onto verification in [[anatomy-of-a-decision]]: divergence
between what the wiki claims and what the sources support. Orphan pages and stale claims are the
wiki's form of the failures in [[decision-entropy]]. The system has no enforcement step, which
is its main structural gap.

## Related

[[compiled-knowledge-base]] · [[schema-as-agent-constraint]] · [[three-layer-knowledge-architecture]] · [[obsidian]]
