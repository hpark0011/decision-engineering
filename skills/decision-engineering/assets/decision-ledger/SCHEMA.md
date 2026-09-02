# Decision ledger schema

This file defines the ledger's record contract: structure, fields, and invariants. The Decision Engineering skill's `SKILL.md` defines the workflow for locating, creating, changing, reviewing, and maintaining the ledger.

## Authority

- `SCHEMA.md` is the authoritative contract for this ledger.
- Active `decisions/*.md` records are authoritative current intent; superseded and retired records preserve historical intent.
- `index.md` and `generated/graph.mmd` are derived views of the records.
- `log.md` is append-only semantic history.

## Directory

```text
decision-ledger/
├── SCHEMA.md
├── index.md
├── log.md
├── decisions/
│   └── D001-determine-example.md
└── generated/
    └── graph.mmd
```

Decision files are flat. Each has a unique, stable ID consisting of `D` followed by at least three digits. IDs remain unchanged across renames and lifecycle changes and are never reused, including IDs present only in history.

## Decision invariant

A ledger can contain multiple policies. Each decision file resolves one question by applying one or more policies to authoritative input facts and produces exactly one independently decidable output fact.

A fact is the smallest authoritative proposition that can change independently. Every derived fact has exactly one producing decision and a globally unique name. Every root fact has exactly one external authority or observation boundary. Many decisions may read one fact; dependencies reference the authoritative fact rather than another decision's raw reasoning or a reconstruction of its policy.

Split a structured output when any part can change independently, be right while another part is wrong, be useful independently, or require different policy, invariant, or verification.

Multiple policies that jointly resolve the same output fact do not by themselves require separate decisions.

## Required decision record

Use only these headings, exactly once and in this order:

1. `## Requirement`
2. `## Question`
3. `## Input facts`
4. `## Invariants`
5. `## Policy`
6. `## Output fact`
7. `## Enforcement`
8. `## Verification`

State the outcome that must become true in `Requirement` and the exact uncertainty to resolve in `Question`. Fill every section with concrete content.

Begin each file with YAML frontmatter:

```markdown
---
status: active
domain: example
id: D001
title: "Determine example"
updated_at: 2026-09-02
---
```

Require `status`, `domain`, `id`, `title`, and `updated_at` exactly once in frontmatter. `updated_at` is a valid `YYYY-MM-DD` date recording the last change to the decision's semantics, dependencies, lifecycle, or authoritative metadata. Frontmatter is the only authoritative location for those values. The body starts with `## Requirement`, with no H1 or repeated frontmatter metadata.

Allowed statuses are `active`, `superseded`, and `retired`. A superseded record requires `superseded_by: Dxxx` in frontmatter, referring to an existing successor; other statuses omit that field. Each filename is `{id}-{slug(title)}.md`, matching the record's frontmatter.

### Domain

A domain is the smallest authoritative consistency boundary responsible for a group of decisions and their output facts. A decision may read facts from other domains, but it produces only its own declared output fact. No domain may directly write facts owned by another domain; cross-domain use occurs through authoritative output facts. Domain is routing metadata and does not determine the file path.

### Input facts

Declare root inputs as:

```markdown
- `task.status`
  - Kind: root
  - Authority: task-lifecycle-store
```

Declare derived inputs as:

```markdown
- `handoff.readiness`
  - Kind: derived
  - Produced by: D003
```

Use lowercase dot- or hyphen-separated stable fact names and reuse the identical name in every reference. A root authority names the owner or observation boundary rather than its transport and is consistent in every record. A derived input's name and producer ID resolve to that producer's declared output fact.

### Output fact

Declare exactly these bullet fields:

```markdown
- Name: `handoff.readiness`
- Meaning: Whether all handoff preconditions are currently satisfied.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot vary independently.
```

### Invariants, policies, and enforcement

`Invariants` states what must never become false. The single `Policy` section contains one or more policies, expressed as paragraphs or bullets, and explains how they combine to map inputs to the one output. Overlapping policies include their precedence or conflict rule.

`Enforcement` names the boundary that can reject an invalid action or commit a valid transition. Before code exists, it states a binding obligation rather than an invented implementation symbol. UI presentation is never enforcement.

### Verification

`Verification` contains concrete bullet obligations that exercise every meaningful policy branch and interaction between policies, prove the invariant at the enforcement boundary, and verify rejection of invalid results or transitions. Verification exercises the authoritative policies without encoding a second copy in tests.

## Semantic log

Each `log.md` entry has this structure:

```markdown
## [YYYY-MM-DD] <kind> | <ID> | <Title>

Reason:
Why the decision model changed.

Changed:
- The semantic changes.

Affected:
- Output facts, downstream decisions, code, and verification.
```

Allowed kinds are `create`, `edit`, `rename`, `supersede`, `retire`, `restore`, `delete`, and `schema-change`. Every decision has a `create`, `restore`, or `schema-change` entry for its ID.

## Derived views and dependency invariants

`index.md` reflects the decision records, routing primarily by output fact and including ID, title, inputs, domain, and status. Questions and requirements are available through linked records. The index contains no unique policy text.

`generated/graph.mmd` reflects declared input facts and output facts:

```text
external authority → root fact → decision → derived fact → decision
```

Both views agree with the records. Self-input and same-evaluation dependency cycles are invalid. Temporal feedback uses an explicit persisted or previous-period root fact.
