# Wiki Schema

## Domain

Decision engineering: making behavior-shaping decisions first-class architectural objects.
Covers decision ledgers, domain boundaries, invariants, ownership, policy, enforcement,
projection, and verification — plus the adjacent knowledge-systems and agent-context
literature that informs how intent is stored and recovered without drift.

Out of scope: general software engineering, general ML research, tooling reviews that
don't bear on how intent or decisions are represented.

## Conventions

- File names: lowercase, hyphens, no spaces (e.g. `decision-ledger.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** on pages synthesizing 3+ sources, append `^[raw/articles/source.md]`
  at the end of paragraphs whose claims come from a specific source. Optional on
  single-source pages where the `sources:` frontmatter is enough.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

Set `confidence: medium` or `low` for single-source or opinion-heavy claims. This wiki
covers a young, largely untested framework — most pages should start below `high`.

### raw/ Frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the body below the frontmatter>
---
```

On re-ingest of the same URL: recompute the digest, skip if identical, flag drift if not.

## Tag Taxonomy

Add new tags here BEFORE using them.

**Core framework:** `decision`, `requirement`, `fact`, `policy`, `invariant`, `domain`,
`ownership`, `enforcement`, `projection`, `verification`, `ledger`

**Failure modes:** `hidden-coupling`, `scattered-decision`, `drift`, `surprise`, `cost-of-change`

**Traceability:** `traceability`, `presentation`

**Foundations:** `information-theory`, `error-correction`, `ddd`

**Knowledge systems:** `knowledge-base`, `context-engineering`, `agent-harness`, `rag`, `tooling`

**Meta:** `person`, `comparison`, `open-question`, `methodology`

## Page Thresholds

- **Create a page** when a concept/entity appears in 2+ sources OR is central to one source
- **Add to an existing page** when a source touches something already covered
- **DON'T create a page** for passing mentions or anything outside the domain
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when fully superseded — move to `_archive/`, remove from index

## Page Types

**Entity pages** — people, orgs, tools, frameworks. Overview, key facts, relationships, sources.

**Concept pages** — one idea per page. Definition, current state of knowledge, relevance to
decision engineering, open questions, related concepts.

**Comparison pages** — what is compared and why, dimensions (table preferred), verdict, sources.

**Query pages** — filed answers worth keeping. Only file answers painful to re-derive.

## Update Policy

1. Check dates — newer sources generally supersede older ones
2. If genuinely contradictory, record both positions with dates and sources
3. Mark it: `contradictions: [page-name]` and `contested: true`
4. Flag for user review in the next lint report

## Domain-Specific Rule

Decision engineering is about locating a single home for each decision. This wiki is held
to its own standard: if two pages both claim authority over the same fact, that is a lint
error, not a stylistic preference. Prefer one authoritative page plus links over
restating a definition in several places.

### GLOSSARY.md is the definition home

`GLOSSARY.md` at the workspace root is the authoritative home for term definitions. Wiki
pages **must not restate definitions** — doing so would create a second authority over the
same meaning, which is the exact failure the framework exists to prevent.

Wiki pages instead hold what the glossary does not: synthesis across sources, worked
examples, tensions between documents, provenance, and open questions. Each page names the
glossary terms it uses under a `Defined in` line and links to them rather than redefining.

When a wiki page needs a term the glossary lacks, that is a finding — report it as a gap in
the glossary, don't fill it in the wiki.
