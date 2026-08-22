# Decision ledger schema

This file is the constitution of this ledger. Change it only through a logged `schema-change` and migrate affected decision records in the same change.

## Authority

- Treat `SCHEMA.md` and `decisions/*.md` as authoritative current intent.
- Treat `index.md` and `generated/graph.mmd` as generated projections.
- Treat `log.md` as append-only semantic history.
- Treat code as authoritative behavior. Require human adjudication when behavior and intent diverge.

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

Keep decision files flat. Use stable IDs with at least three digits. Never renumber or reuse an ID.

## Decision invariant

Require each decision file to resolve one question by applying one policy to authoritative input facts and producing exactly one independently decidable output fact.

Give every derived fact exactly one producing decision. Give every root fact exactly one external authority or observation boundary. Let many decisions consume one fact. Do not consume another decision's raw reasoning or reconstruct its policy.

Split a structured output when any part can change independently, be right while another part is wrong, serve a consumer independently, or require different policy, invariant, or verification.

## Required decision record

Use the headings exactly once and in this order:

1. `## Requirement`
2. `## Question`
3. `## Input facts`
4. `## Output fact`
5. `## Invariant`
6. `## Policy`
7. `## Enforcement`
8. `## Projection`
9. `## Consumers`
10. `## Verification`

Begin each file with YAML frontmatter:

```markdown
---
status: active
domain: example
id: D001
title: "Determine example"
updated_at: 2026-08-21
---
```

Require `status`, `domain`, `id`, `title`, and `updated_at` exactly once in frontmatter. Treat frontmatter as the only authoritative location for those values. Store `updated_at` as an ISO calendar date (`YYYY-MM-DD`) and refresh it on every semantic decision edit. Start the body with `## Requirement`; do not repeat decision identity in an H1 or repeat any of the five fields as body metadata.

Allow `active`, `superseded`, or `retired` status. Add `superseded_by: Dxxx` to the frontmatter of a superseded record. Keep domain as routing metadata; do not move files when domain groupings change. Derive each filename as `{id}-{slug(title)}.md` and keep it synchronized with frontmatter.

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

Use lowercase dot- or hyphen-separated stable fact names. Keep a root authority consistent in every record. Model temporal feedback through an explicit persisted or previous-period root fact; do not create same-evaluation cycles.

### Output fact

Declare exactly these bullet fields:

```markdown
- Name: `handoff.readiness`
- Meaning: Whether all handoff preconditions are currently satisfied.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot vary independently.
```

### Invariant, policy, and enforcement

State what must never become false, how inputs map to the one output, and which boundary can reject or commit an invalid action or transition. Before code exists, state a binding obligation rather than inventing an implementation symbol. UI presentation is never enforcement.

### Projection and consumers

Begin `Projection` with exactly one standalone backticked projection name. Permit representation changes only; require a separate decision for new judgment. List known UI, API, worker, agent, report, and downstream-decision consumers. Require consumers to use the projection or authoritative output contract.

### Verification

List concrete obligations that exercise the authoritative policy, invariant, and enforcement boundary. Do not encode a second copy of policy in tests.

## Operations

Read this file and `index.md` before every operation. Route a requirement to an existing output fact before creating a decision.

- Consume an existing projection for a new consumer.
- Edit the owning decision when its semantics change.
- Create only for a genuinely unresolved question and new output fact.
- Reconcile wrong behavior by tracing projection → output fact → decision → inputs → authorities → enforcement → verification.

Append a semantic `log.md` entry for every create, edit, rename, supersede, retire, restore, delete, or schema change. Record reason, changed semantics, and affected facts, decisions, consumers, code, and verification.

Regenerate projections and lint after every semantic change. Repair structural errors rather than suppressing them.
