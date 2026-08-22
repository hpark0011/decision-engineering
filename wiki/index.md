# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary. Read this first to find relevant pages for any query. Last updated: 2026-08-21 | Total pages: 17

## Start here

[[decision-engineering]] is the hub. Definitions are **not** in this wiki — `GLOSSARY.md` at the workspace root is the authoritative definition home, and pages here deliberately defer to it.

## Entities

- [[andrej-karpathy]] — Author of the LLM Wiki gist; positions the pattern in the Memex lineage and argues maintenance cost is what kills human wikis.
- [[john-von-neumann]] — Frames error as an architectural input and separates executive work from the restoring operations needed to synthesize reliability.
- [[obsidian]] — Local markdown editor used as the human read surface over the agent-written wiki; graph view, Dataview, Web Clipper.

## Concepts

### Decision engineering

- [[decision-engineering]] — Hub: the thesis, the launch-email example, scope, and where README and GLOSSARY disagree. `contested`
- [[anatomy-of-a-decision]] — The requirement → decision → facts → owner → domain → invariant → policy → enforcement → projection → verification pipeline, and where the decision proper ends.
- [[authority-and-projection]] — Information may be copied; authority may not. Projections, presentations, traceability, and how a projection becomes a competing authority.
- [[decision-entropy]] — The six failure modes (hidden, duplicated, scattered, coupled, weakly owned, stale) and Cost of Next Change as their signal.
- [[decision-ledger]] — The authoritative record of decisions; why the dependency-graph requirement is what makes it machine-checkable.
- [[domain-boundaries]] — Domains emerge from decision dependencies, not nouns; the grouping procedure and the change test.
- [[information-theoretic-foundation]] — What von Neumann's error-control constructions actually establish, how restoration maps to verification, and what the analogy still lacks.
- [[productizing-decision-engineering]] — Zero-friction chat MVP: event-triggered delta extraction quietly turns conversational commitments into ledger and log updates.

### Knowledge systems

- [[compiled-knowledge-base]] — Synthesis computed once at ingest and kept current, versus RAG re-deriving it per query.
- [[schema-as-agent-constraint]] — The schema file as pre-resolved policy that turns an agent into a disciplined maintainer; strong policy, weak enforcement.
- [[three-layer-knowledge-architecture]] — Raw sources / wiki / schema, split by disjoint write ownership so no layer can corrupt another.
- [[wiki-operations]] — Ingest, query, and lint; why index.md and log.md answer different questions.

## Comparisons

- [[hermes-vs-decision-engineering]] — Hermes assembles prompts from memory, skills, tools, and an LLM loop; Decision Engineering changes the compounding unit from procedures to durable reasoning.
- [[plugin-vs-installer-distribution]] — Shipping skills as a managed plugin (subscribe) versus an `npx` installer (fork); why the prior art ships both, and the manifest constraints that shape repo layout.

Top remaining candidate: decision engineering vs. DDD bounded contexts vs. spec-driven development — asked in the README, unanswered in every source.

## Queries

_None yet._

## Sources

- `raw/articles/de-glossary.md` — GLOSSARY.md snapshot, 2026-08-20. Authoritative for definitions.
- `raw/articles/de-readme.md` — README.md snapshot, 2026-08-20. Intent and rationale; rougher and older than the glossary.
- `raw/articles/karpathy-llm-wiki.md` — Andrej Karpathy, "LLM Wiki" (gist), ingested 2026-08-20.
- `raw/papers/von-neumann-probabilistic-logics-1956.md` and companion `.pdf` — J. von Neumann, *Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components*; 1952 lectures, published 1956, ingested 2026-08-20.
- `raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md` — ChatGPT discussion of a zero-friction Decision Engineering product and its architectural contrast with Hermes, ingested 2026-08-21.
- `raw/articles/mattpocock-skills-readme.md` — README of `mattpocock/skills`, ingested 2026-08-21. The "two ways in, two philosophies" install framing.
- `raw/articles/mattpocock-skills-adr-0002-claude-code-plugin.md` — ADR 0002 from the same repo, ingested 2026-08-21. Primary source on plugin manifest constraints and the resulting invariants.
- `raw/articles/compound-engineering-plugin-readme.md` — README of `EveryInc/compound-engineering-plugin`, ingested 2026-08-21. Multi-host root-native plugin layout and the legacy-installer cleanup.

### Cited but not yet ingested

- *Unreliable Systems Built from Reliable Parts* (ResearchGate)
