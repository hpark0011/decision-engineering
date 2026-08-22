# Decision ledger schema

Use this schema for ledgers initialized by this skill. If a repository already has a stricter `SCHEMA.md`, follow that file instead.

## Contents

1. [Ledger directory](#ledger-directory)
2. [Decision record](#decision-record)
3. [Fact references](#fact-references)
4. [Lifecycle](#lifecycle)
5. [Generated projections](#generated-projections)
6. [Lint rules](#lint-rules)

## Ledger directory

```text
decision-ledger/
├── SCHEMA.md                 authoritative maintenance constitution
├── index.md                  generated routing projection
├── log.md                    append-only semantic history
├── decisions/                authoritative flat decision records
│   └── D001-determine-x.md
└── generated/
    └── graph.mmd              generated dependency projection
```

Keep active decision files physically flat. Put changing domain groupings in metadata, the index, and the graph so stable identities do not depend on taxonomy.

## Decision record

Use the headings exactly once and in this order:

```markdown
---
status: active
domain: example
id: D001
title: "Determine example"
updated_at: 2026-08-21
---

## Requirement

State the outcome that must become true.

## Question

What exact uncertainty does the system resolve?

## Input facts

- `source.example`
  - Kind: root
  - Authority: example-system
- `upstream.answer`
  - Kind: derived
  - Produced by: D000

## Output fact

- Name: `example.answer`
- Meaning: The independently decidable proposition resolved here.
- Shape: `{ state: allowed | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot vary independently.

## Invariant

State what must never become false while the output is accepted as valid.

## Policy

State the rule mapping input facts to the output fact.

## Enforcement

Name the boundary that can reject or commit the action. Before code exists, state an obligation rather than inventing a symbol.

## Projection

`example.answer.public`

Describe allowed renaming, omission, or explanation. Introduce no judgment.

## Consumers

- Example UI
- D002 — Determine downstream result

## Verification

- Exercise the authoritative policy over each meaningful branch.
- Prove the invariant at the enforcement boundary.
- Prove the boundary rejects every invalid result or transition.
```

Require the five frontmatter fields `status`, `domain`, `id`, `title`, and `updated_at`. Treat them as the single authoritative location for decision identity, lifecycle, routing, and recency metadata. Store `updated_at` as `YYYY-MM-DD` and refresh it on every semantic decision edit. Do not repeat them in an H1 or body line; begin the body with `## Requirement`.

Use a stable `D` ID with at least three digits. Keep the ID unchanged when the title or filename changes. Derive the filename as `{id}-{slug(title)}.md` and lint it against frontmatter. Use lowercase dot-separated fact and projection names. Use `active`, `superseded`, or `retired` status.

## Fact references

Treat a fact as the smallest authoritative proposition that can change independently.

- Declare each root input with `Kind: root` and one `Authority` naming the owner or observation boundary, not the transport.
- Declare each derived input with `Kind: derived` and the one `Produced by` decision ID.
- Produce exactly one output fact per decision.
- Give each derived output fact one globally unique name and producer.
- Reuse the identical fact name wherever it is consumed.
- Keep an authority consistent wherever the same root fact appears.

Split a structured output if a field can change independently, can be correct while another is wrong, can serve a consumer independently, or needs a different policy, invariant, or verification.

## Lifecycle

For `superseded` records, add optional lifecycle metadata to frontmatter:

```yaml
superseded_by: D009
```

Require the successor to exist. Keep superseded and retired records for historical references. Delete only accidental records that were never accepted. Never reuse an ID.

Append semantic changes to `log.md`. Write each entry heading as `## [YYYY-MM-DD] <kind> | <ID> | <Title>`. Require every decision to have at least one `create`, `restore`, or `schema-change` entry that mentions its ID. Use Git for line history and the ledger log for meaning and impact.

## Generated projections

Generate `index.md` from decision records. Route primarily by output fact; include ID, question, inputs, projection, domain, and status. Store no unique policy text there.

Generate `generated/graph.mmd` as a bipartite graph:

```text
external authority → root fact → decision → derived fact → decision
```

Allow a fact many consumers but at most one producer. Reject same-evaluation dependency cycles. Model temporal feedback through an explicit previous-period or persisted-state root fact.

## Lint rules

The bundled linter checks mechanically:

- required frontmatter, ISO-date `updated_at`, required files, headings, heading order, IDs, filenames, statuses, and non-placeholder content;
- absence of repeated status, domain, ID, title, or H1 metadata in the body;
- exactly one output fact, projection, invariant, policy, enforcement obligation, and verification list per decision;
- output and projection uniqueness;
- root authority consistency;
- derived fact and producer resolution;
- no self-input and no synchronous decision dependency cycle;
- supersession target resolution;
- create-history presence in `log.md`;
- exact agreement between generated `index.md` and decision records.

The linter cannot prove that prose expresses the correct policy, output atomicity is well judged, a projection contains no hidden judgment, consumers do not recreate logic in code, or bindings resolve to real code. Review those as explicit human/agent obligations.
