# Wiki Log

> Chronological record of all wiki actions. Append-only. Format: `## [YYYY-MM-DD] action | subject`Actions: ingest, update, query, lint, create, archive, delete When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## \[2026-08-20\] create | Wiki initialized

- Domain: decision engineering (decision ledgers, domain boundaries, invariants, agent context)
- Structure created with SCHEMA.md, index.md, log.md
- Directories: raw/{articles,papers,transcripts,assets}, entities, concepts, comparisons, queries

## \[2026-08-20\] ingest | LLM Wiki (Andrej Karpathy)

- Source: `raw/articles/karpathy-llm-wiki.md` (sha256 dc3efe98…7401)
- Created: `concepts/compiled-knowledge-base.md`
- Created: `concepts/three-layer-knowledge-architecture.md`
- Created: `concepts/schema-as-agent-constraint.md`
- Created: `concepts/wiki-operations.md`
- Created: `entities/andrej-karpathy.md`
- Created: `entities/obsidian.md`
- Updated: `index.md` (6 pages)
- Note: single-source ingest — all pages `confidence: medium` or lower pending corroboration

## \[2026-08-20\] ingest | README.md + GLOSSARY.md (decision engineering core docs)

- Sources: `raw/articles/de-readme.md` (sha256 4646f20d…b828), `raw/articles/de-glossary.md` (sha256 77c35e83…80c1)
- Both are snapshots of live workspace files; recompute digests on re-ingest to detect drift
- Updated SCHEMA.md: added `cost-of-change`, `traceability`, `presentation` tags; added the rule that GLOSSARY.md is the authoritative definition home and wiki pages must not redefine terms
- Created: `concepts/decision-engineering.md` (hub, `contested: true`)
- Created: `concepts/anatomy-of-a-decision.md`
- Created: `concepts/decision-ledger.md`
- Created: `concepts/domain-boundaries.md`
- Created: `concepts/decision-entropy.md`
- Created: `concepts/authority-and-projection.md`
- Created: `concepts/information-theoretic-foundation.md` (`confidence: low`)
- Updated: `concepts/compiled-knowledge-base.md`, `concepts/three-layer-knowledge-architecture.md`, `concepts/schema-as-agent-constraint.md`, `concepts/wiki-operations.md`, `entities/andrej-karpathy.md` — cross-linked into the domain
- Updated: `index.md` (13 pages, sectioned Concepts, added Sources)
- **Contradiction recorded:** README's inline Glossary stub defines Decision as "steps" while GLOSSARY.md defines it as "a question." Glossary is authoritative (newer, more refined). Filed on `concepts/decision-engineering.md` under Source tensions.
- **Gaps flagged at source:** "repair radius" used in README but undefined anywhere; "domain" undefined in GLOSSARY.md despite being central; README duplicates the glossary inline; "Why should you care" appears twice; "Entire process" section is an unfinished stub

## \[2026-08-20\] ingest | Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components

- Source: Stanford PDF of J. von Neumann's 1952 Caltech lectures, published 1956
- Created: `raw/papers/von-neumann-probabilistic-logics-1956.pdf` (original Stanford PDF; sha256 395d81d7…0914092a5f) and companion `.md` (66-page text extraction; body sha256 eb042e38…d91060c)
- Created: `entities/john-von-neumann.md`
- Updated: `concepts/information-theoretic-foundation.md` with the paper's single-line and multiplex error-control mechanisms, model-specific thresholds, restoration pattern, and limitations
- Updated: `concepts/decision-entropy.md`, `concepts/domain-boundaries.md`, `concepts/authority-and-projection.md` with source-qualified implications
- Updated: `index.md` (14 pages; source moved from cited-but-not-ingested to ingested)
- Source correction: the paper concerns probabilistic automata and neural-style logical networks, not specifically cellular automata; its thresholds do not transfer to decision engineering without an explicit error model

## \[2026-08-21\] ingest | Discussing Decision Engineering and Hermes

- Source: `raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md` (sha256 c830b846…191a7)
- Created: `concepts/productizing-decision-engineering.md`
- Created: `comparisons/hermes-vs-decision-engineering.md` (`confidence: low`; Hermes architecture and popularity claims await external verification)
- Updated: `concepts/decision-ledger.md` with asynchronous, event-triggered delta extraction as a proposed conversational write path
- Updated: `index.md` (16 pages; added comparison and transcript source)
- Key distinction captured: Hermes compounds reusable procedures and skills; Decision Engineering compounds durable decisions and reasoning—why, authoritative facts, dependencies, and what to revisit when facts change

## \[2026-08-21\] ingest | Agent skill distribution — mattpocock/skills + compound-engineering-plugin

- Sources: `raw/articles/mattpocock-skills-readme.md` (sha256 4079d981…d4f6), `raw/articles/mattpocock-skills-adr-0002-claude-code-plugin.md` (sha256 c8f8f946…d949d), `raw/articles/compound-engineering-plugin-readme.md` (sha256 002ff5d3…6ca30)
- All three are live GitHub files; recompute digests on re-ingest to detect drift
- Created: `comparisons/plugin-vs-installer-distribution.md` (`confidence: medium`)
- Updated: `concepts/productizing-decision-engineering.md` — added a Distribution pointer and related link
- Updated: `index.md` (17 pages; added comparison and three sources)
- No new tags needed; reused `comparison`, `tooling`, `agent-harness`, `methodology`, `projection`, `open-question`
- Key finding: both prior-art repos ship a native plugin *and* an `npx` installer rather than choosing. Pocock reuses third-party `skills.sh` for the installer channel, so it costs him nothing to maintain, and puts per-repo configuration in a setup *skill* rather than installer code.
- Constraint recorded: Claude's `plugin.json` takes `skills` as an array of explicit paths; Codex takes a single path string and recursively discovers `SKILL.md`, and drops symlinks on install. Manifest format therefore constrains repo layout.
- Hazard recorded: CE's retired Bun installer wrote a managed block into the user's global `~/.codex/AGENTS.md` containing a line that broke subagent dispatch; the README still carries a removal prompt. Argument against owning a bespoke installer.
- Framework connection: per-host `plugin.json` is a projection of the authoritative `skills/` dir, and Pocock's ADR encodes the completeness rule as an explicit invariant. The ADR is a decision entry with dependency edges written without the vocabulary.

## \[2026-08-24\] query | How Hermes memory works

- Answered from current official Nous Research documentation plus [[hermes-vs-decision-engineering]].
- Not filed: concise factual lookup, not a substantial synthesis.
- Correction to the existing low-confidence framing: built-in memory is bounded `MEMORY.md` + `USER.md` injected as a frozen session-start snapshot; full session history is separately searchable through SQLite FTS5, and one optional external memory provider can augment the built-in stores.

## \[2026-08-24\] query | What belongs in Hermes MEMORY.md

- Answered as a follow-up factual lookup; not filed.
- Clarified that `MEMORY.md` holds compact, durable, actionable environment and workflow facts, while user identity/preferences belong in `USER.md`, project authority belongs in context files, and transient or rediscoverable material stays out.

## [2026-09-02] update | Align summaries with the minimal ledger contract

- Source: the current workspace `decision-ledger/SCHEMA.md`, adopted through its logged schema change.
- Updated `concepts/decision-ledger.md` with the eight-section record format, one default schema, and dependencies derived from input/output facts.
- Updated `concepts/productizing-decision-engineering.md` to defer explicit usage lists from the earlier product discussion.
- Updated `concepts/authority-and-projection.md` to align its terminology with the current glossary.
- Updated `index.md` with the current contract source, summary, and date; kept the 17-page count.
- Preserved raw source snapshots as historical evidence.

## [2026-09-02] update | Multiple policies within a decision

- Source: the current workspace ledger schema and its schema-change entry for D006.
- Updated `concepts/decision-ledger.md` to describe multiple policies within the existing Policy section and their explicit combination.
- Updated `concepts/anatomy-of-a-decision.md` with the handoff example of several policies producing one output fact.
- Updated the `index.md` summary; the wiki remains at 17 pages.

## [2026-09-02] update | Direct ledger maintenance and source ownership

- Sources: `../skills/decision-engineering/SKILL.md` and its bundled `assets/decision-ledger/SCHEMA.md`.
- Removed the repository's internal ledger and its parser-dependent tooling; the skill now maintains project records and views directly.
- Updated `concepts/decision-ledger.md` to explain the current workflow and distinguish it from the earlier proposal for a skill's own design ledger.
- Retargeted current schema references in `concepts/decision-ledger.md`, `concepts/anatomy-of-a-decision.md`, `concepts/productizing-decision-engineering.md`, and `index.md` to the bundled contract.
- Updated `index.md` with the workflow source; retained the 17-page count and historical raw sources and log entries.
