# Decision Engineering

This is an idea file inspired by Andrej Karpathy's [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). It is designed to be copied into an LLM agent such as Codex, Claude Code, Cursor, or another coding agent. Its purpose is to communicate the high-level architecture and operating rules for builders who want to create their own skill instead of using the pre-built skill.

For the maintained skill, use [SKILL.md](skills/decision-engineering/SKILL.md) for the workflow and the [bundled schema](skills/decision-engineering/assets/decision-ledger/SCHEMA.md) for the default record contract.

## The core idea

Decision Engineering is the discipline of building reliable decision systems out of unreliable decision-makers.

Humans forget context, make implicit assumptions, disagree, and sometimes make the wrong call. Agents hallucinate, lose context, reason differently across runs, and confidently produce incorrect outputs. A system that depends on their judgment cannot become reliable by demanding that every person or agent be right every time.

A reliable decision system assumes that individual judgments will fail. It must be able to catch a mistake, contain its effects, locate its source, and recover from it.

Consider a product whose subscription price is `$49`. Most systems can store that price as a source of truth for current state, but they cannot answer why `$49` is the right price. Perhaps customer acquisition cost is `$35` and the business wants to recover it within two months. Perhaps a test showed that `$39` performed worse. Perhaps a customer contract constrains the price. Or perhaps `$49` was only a guess.

Now imagine an agent is asked to improve conversion. It can see the price, but it cannot tell which assumptions the price depends on, which decision owns it, or what else relies on it. The agent may make a locally reasonable change that silently breaks the margin target, billing, forecasts, and marketing.

The core problem is not simply that the agent must rediscover old reasoning. The system has no authoritative structure for distinguishing state from intent, checking whether the assumptions behind a decision still hold, or containing a wrong judgment before it propagates.

Decision Engineering makes each important decision a first-class architectural object:

```
goal → requirement → input facts → decision policies → one output fact
```

For the pricing example:

```
CAC = $35 ───────────────────┐
target payback < 2 months ───┼──▶ [decide subscription price]
gross margin = 85% ──────────┘                 │
                                               ▼
                            product.monthly_price = $49
                                               │
                        ┌──────────┬────────────┼──────────┐
                        ▼          ▼            ▼          ▼
                     website    billing     forecast   marketing
```

The pricing decision has one clear job and produces one authoritative fact. Its inputs, policy, and invariants are visible. The implementation uses that output wherever the subscription price is needed.

If the price is wrong, the system provides a bounded path back to the pricing decision and the facts behind it. If CAC changes from `$35` to `$70`, the system can identify the decision that must be revisited and the downstream decisions affected by its output. The error has an owner, and its blast radius is visible.

This gives the system a source of truth for intent, not only state:

```
state  = what the system is
intent = why it is that way
```

The decision ledger makes that structure authoritative. It is a maintained directory of schema-constrained Markdown files. Each file contains one decision, and facts connect those decisions into a graph.

When a new requirement arrives, the agent routes it through the existing ledger before adding logic:

- If an existing decision already produces the required fact, the new feature consumes that output fact.

- If the answer should change, the owning decision is edited.

- Only a genuinely new question creates a new decision file.

The ledger is the source code of intent. It gives unreliable humans and agents a shared structure in which mistakes are detectable, traceable, contained, and correctable.

## The central unit

A decision is a named answer to a question the system must answer to make progress.

It is a step that removes uncertainty.

A task is work to be performed. A decision is the conclusion that the work is meant to establish.

```
Task:     Review whether this task can be handed off.
Decision: May this task enter handoff now?
```

A decision reads authoritative input facts, applies one or more policies, and produces exactly one authoritative output fact.

```
(fact A) ──┐
(fact B) ──┼──▶ [decision] ──▶ (one output fact)
(fact C) ──┘
```

This creates the core structural rule:

> One decision file resolves one question and produces one fact.

A decision may read many facts. A fact may be read by many decisions. But every decision produces exactly one fact, and every derived fact has exactly one producing decision.

A ledger can contain multiple policies, including several policies within one decision. Record them in the decision's `Policy` section and state how they combine. For example, task eligibility, work preservation, and assignee readiness policies may all need to pass for one handoff-readiness result. State precedence or conflict rules when policies overlap. Policy count alone does not require splitting a decision.

A decision that produces no fact has not resolved an uncertainty. It is probably a task, note, analysis, presentation, or enforcement mechanism rather than a decision.

A decision that produces multiple independently meaningful facts is answering multiple questions and must be split.

### What counts as one fact?

A fact is the smallest authoritative proposition that can change independently.

A structured value may still be one fact when all of its fields describe the same inseparable answer:

```
handoff.readiness = {
  state: "blocked",
  reason: "The workspace contains uncommitted changes"
}
```

`state` is the resolved answer. `reason` explains that same answer. The reason cannot be changed independently without changing or misrepresenting the answer.

This is not one fact:

```
{
  handoff_allowed: false,
  assignee_available: true,
  audit_severity: "medium"
}
```

Those fields answer different questions. They can change independently and require different policies. They belong to separate decisions.

Use these tests whenever output atomicity is unclear:

1. Could one part change while the other parts remain valid?

2. Could one part be correct while another part is wrong?

3. Could one part be useful without accepting the others?

4. Do different parts require different policies, invariants, or verification?

If any answer is yes, the output contains multiple facts and the decision must be split.

The real invariant is:

```
one decision
    → one independently decidable proposition
    → one authoritative output fact
```

## Architecture

A Decision Engineering ledger has three conceptual layers.

### Requirement sources

Requirements may come from conversations, tickets, product specifications, regulations, customer commitments, research, operating rules, or human instructions.

They may be incomplete, noisy, contradictory, or written in implementation language. They are evidence of intent, not yet an executable decision model.

### The decision ledger

The ledger is a directory of Markdown files maintained by humans and agents under the rules in `SCHEMA.md`.

A minimal folder looks like this:

```
decision-ledger/
├── index.md
├── SCHEMA.md
├── log.md
├── decisions/
│   ├── D001-determine-account-access.md
│   ├── D002-determine-payment-eligibility.md
│   └── D003-determine-handoff-readiness.md
└── generated/
    └── graph.mmd
```

The active decision files should remain flat inside `decisions/` at first. Domain groupings belong in the index and graph rather than in nested directories. Domain boundaries may change; stable decision identities should not depend on the current folder taxonomy.

The files have different responsibilities:

```
SCHEMA.md       = constitution of the ledger
                  conventions, policies, invariants, and workflows

decisions/*.md = authoritative current decision records

index.md        = generated routing view over all decision records

log.md          = append-only semantic history of ledger changes

graph.mmd       = generated dependency view of facts and decisions
```

`SCHEMA.md` and `decisions/*.md` define the current decision system. `log.md` records how that system changed. `index.md` and the graph make the authoritative records fast to navigate, but they must not contain unique decision logic.

### Code and runtime behavior

The implementation makes the decisions executable. It observes root facts, evaluates policies, produces derived facts, enforces invariants, changes state, and exposes authoritative output facts.

The decision files are authoritative for intent. The code is authoritative for actual behavior.

```
decision ledger = what the system is intended to decide
code             = what the system actually does
```

A bug is a divergence between the two. When they disagree, neither side automatically wins. The implementation may be wrong, or intent may have changed without being recorded. A human adjudicates which one should change.

A behavior-changing code change with no corresponding ledger delta is therefore a review flag.

## The root files

### `index.md`: the router

`index.md` is the first file an agent reads when it needs to find the authoritative decision.

Its job is not to explain every decision in full. Its job is to route quickly from a requirement, fact, or domain to the correct source file.

A useful index entry contains:

```
| ID   | Decision                    | Produces            | Reads                                                               | Domain  | Status |
|------|-----------------------------|---------------------|---------------------------------------------------------------------|---------|--------|
| D003 | Determine handoff readiness | `handoff.readiness` | `task.status`, `workspace.cleanliness`, `assignee.readiness`         | handoff | active |
```

The most important routing key is usually the output fact. When an agent needs to know who owns `handoff.readiness`, the index should point directly to the one decision that produces it.

The index may also organize decisions:

- by output fact;

- by domain;

- by requirement or capability;

- by status, including active, superseded, and retired decisions.

The lookup workflow is:

1. Read `index.md`.

2. Search by the uncertainty being resolved, the expected output fact, known input facts or requirement terms.

3. Open the smallest set of candidate decision files.

4. Follow their fact links upstream or downstream when more context is needed.

5. Search the entire `decisions/` folder only when the index cannot route the request.

`index.md` derives its content from the decision files and is reviewed against them. It must never become a second source of decision logic.

### `log.md`: the semantic history

`log.md` is an append-only chronological record of changes to the decision ledger.

Git already answers:

> Which lines changed?

The decision log should answer:

> What changed in the decision model, why did it change, and what was affected?

Each entry should start with a consistent, parseable heading:

```
## [2026-08-20] edit | D003 | Determine handoff readiness
```

A useful entry records:

```
## [2026-08-20] edit | D003 | Determine handoff readiness

Reason:
The system may now hand off work when unsaved changes have been captured
in a recoverable snapshot.

Changed:
- Added input fact `workspace.snapshot-status`.
- Revised the policy and invariants.
- Added two verification cases.

Affected:
- `handoff.readiness`
- D004 — Authorize task handoff
- Task detail UI
- Handoff API
```

The log records semantic changes using the change kinds defined in the ledger's schema.

Prefer superseding or retiring an adopted decision over deleting it. Stable IDs may already be referenced by requirements, commits, tests, logs, or downstream decisions. Hard deletion should be reserved for accidental records that never became part of the accepted ledger.

The log records semantic changes, not every wording correction. A change belongs in `log.md` when it changes ownership, meaning, dependencies, policy, invariants, enforcement, verification, or lifecycle state.

### `SCHEMA.md`: the constitution

`SCHEMA.md` tells humans and agents how the ledger is structured. `SKILL.md` owns the maintenance workflow.

It defines:

- what counts as a decision;

- what counts as a fact;

- the one-decision-to-one-output-fact invariant;

- the atomicity tests for structured outputs;

- how root and derived facts are identified;

- decision ID and filename conventions;

- required frontmatter and headings;

- required heading order;

- how fact references are written;

- allowed graph nodes and edges;

- how enforcement and verification are recorded;

- lifecycle metadata and semantic log entry structure;

- the content of the index and graph views.

`SCHEMA.md` should be precise enough that two agents following it produce structurally compatible decision files.

The schema will evolve as the system teaches you what is missing. A schema change is itself a logged change and may require migrating existing decision files.

## Decision files

Each file in `decisions/` contains one decision record.

```
one Markdown file
    = one decision
    = one question
    = one or more policies
    = one output fact
```

Each decision needs a stable identity so links and history survive wording changes. Never reuse that identity for another decision.

The ledger's `SCHEMA.md` defines the exact metadata, headings, order, and formatting. At the idea level, every decision record must capture:

- **Requirement:** What must become true, without prescribing the implementation.

- **Question:** The one uncertainty being resolved.

- **Input facts:** The authoritative root or derived facts the decision reads.

- **Invariants:** What must remain true regardless the answer.

- **Policy:** One or more policies that turn the input facts into an answer, including how they combine.

- **Output fact:** The one result this decision owns.

- **Enforcement:** The boundary that can reject an invalid action or state.

- **Verification:** The checks that exercise the policies, their interactions, and invariants.

## The decision graph

The ledger forms a directed bipartite graph with two primary node types:

```
facts ↔ decisions
```

The core edge types are:

```
fact     --input-to--> decision
decision --produces--> fact
```

A decision may have many incoming fact edges but exactly one outgoing `produces` edge.

A fact may have many outgoing `input-to` edges but at most one incoming `produces` edge.

```
(task.status) ──────────────────┐
(workspace.cleanliness) ────────┼──▶ [D003: Determine handoff readiness]
(assignee.readiness) ───────────┘                    │
                                                      ▼
                                           (handoff.readiness)
```

A downstream decision may consume that result:

```
(handoff.readiness) ────────────┐
(actor.handoff-permission) ─────┴──▶ [D004: Authorize task handoff]
                                                     │
                                                     ▼
                                          (handoff.authorization)
```

The resulting structure is:

```
fact → decision → fact → decision → fact
```

### Root facts and derived facts

Not every fact is produced by another decision.

A root fact is observed or written by an authoritative source outside the decision graph:

```
task.status
current-time
payment-processor.response
user.submitted-email
workspace.cleanliness
```

Each root fact must declare exactly one authoritative writer or observation boundary.

A derived fact is produced by exactly one decision:

```
handoff.readiness
payment.eligibility
account.access-level
```

Graphically:

```
[external writer] → (root fact) → [decision] → (derived fact)
```

A fact with neither a producer nor an external writer is unauthoritative. A fact with multiple producers or writers is ambiguous. Both are structural defects to resolve during review.

### Graph invariants

The graph must satisfy these mechanical constraints:

1. Every decision has exactly one output fact.

2. Every derived fact has exactly one producing decision.

3. Every root fact has exactly one authoritative external writer or observer.

4. Every input fact reference resolves to an existing fact identity.

5. A decision may not list the same fact as both an unresolved input and its output.

6. Every decision has invariants, an enforcement obligation, and verification obligations, or an explicit schema-approved reason one is not applicable.

7. Every active decision is indexed, and every active index entry resolves to one decision file.

A same-evaluation dependency cycle is invalid because no decision can resolve first:

```
D001 needs fact B
D002 produces fact B but needs fact A
D001 produces fact A
```

Temporal feedback is allowed only when the time boundary is explicit. For example, a decision may read `previous-period.risk-score` as a root or persisted state fact rather than directly depending on its own current output.

The graph is a generated view. The decision files remain authoritative.

## Domains

A domain is the smallest authoritative consistency boundary responsible for a group of decisions and their output facts.

Domains should be derived from the decision graph and its invariants rather than chosen from implementation layers such as UI, API, database, worker, or queue.

Two decisions belong in the same domain when their owned state must change together to preserve an invariant; changing one independently would create an invalid observable state.

Domains are useful for routing, impact analysis, and visualization, but they should not control the physical folder structure. Keep decision files stable and flat; let `index.md` and the graph group them by the current domain model.

A decision may read authoritative output facts from another domain, but it produces only its own declared output fact. No domain may directly write facts owned by another domain.

## Operations

### Locate before creating

Every operation begins by reading `SCHEMA.md` and scanning `index.md`.

Before creating a decision, ask:

- Does an existing decision already answer this question?

- Does an existing output fact already represent the answer?

- Can this request reuse an existing output fact?

- Is the requirement changing an existing policy, invariant, input, or output meaning?

- What genuinely new uncertainty remains unresolved?

Do not create a second decision that produces a synonymous version of an existing fact.

### Create a decision

To create a new decision:

1. Confirm that no existing decision or output fact already answers the question.

2. Restate the requirement as an outcome and name the exact uncertainty to resolve.

3. Identify the authoritative inputs, invariants, and policy.

4. Define one atomic output fact. Split the decision if the result contains independently changing facts.

5. Identify enforcement and verification.

6. Write the record according to `SCHEMA.md`.

7. Update the log, index, and graph directly, then review the record against the project's schema and verify affected behavior.

A decision is not accepted while its output ownership or input authorities are ambiguous.

### Edit a decision

To change behavior:

1. Locate the decision that owns the affected output fact.

2. Identify whether the change affects the requirement, question, inputs, invariants, policy, output meaning, enforcement or verification.

3. Edit the authoritative decision file.

4. Walk the graph downstream from the changed output fact.

5. Update affected decisions, code, and verification.

6. Update the index and graph directly from the records.

7. Append an edit entry to `log.md` explaining the semantic change and impact.

8. Review the changed records and views against the project's schema and verify affected behavior.

If an edit causes the decision to produce more than one fact, split it into multiple decisions rather than expanding the original file.

### Consume a decision

If the required answer already exists, reuse the authoritative output fact. No ledger change is needed when its meaning and dependencies stay the same.

If the answer must change, edit its owning decision. If a new question remains unresolved, create a decision for that question.

### Supersede, retire, or delete

When a question has been replaced by a different question or output fact, mark the old decision as superseded and point to its successor.

When a decision is no longer used but remains historically meaningful, retire it.

Delete only when the file was created accidentally or never became an accepted part of the ledger. Log every deletion with the reason and affected references.

Never reuse a deleted, retired, or superseded decision ID.

### Diagnose an error

When the system produces a wrong result, start from the observed behavior and walk backward:

```
wrong observed output
    → authoritative output fact
    → producing decision
    → policy and invariants
    → input facts
    → producers or external writers of those facts
    → enforcement
    → verification
```

This localizes the error to a bounded set of possible causes:

- a root fact was wrong or stale;

- the wrong authoritative source wrote the fact;

- a derived input fact was produced incorrectly;

- the policy was incomplete or wrong;

- an invariant omitted a forbidden state;

- enforcement was absent or bypassed;

- the implementation introduced unrecorded policy;

- verification missed the failing case;

- the recorded intent itself was wrong.

Do not patch the nearest visible surface before locating the fact and decision that own the answer.

### Review

The skill uses direct review against the project's schema. Follow the [review workflow](skills/decision-engineering/SKILL.md#review-and-refresh-the-views) to assess the records and keep the index and graph current.

## The correction threshold

Decision Engineering is not mainly documentation. Its purpose is to keep wrong answers localizable and correctable.

A decision is below the correction threshold when:

- the observed output traces to exactly one authoritative fact;

- that fact traces to exactly one producing decision or root writer;

- the decision's inputs each trace to one authority;

- the applicable policies and how they combine are written in one authoritative place;

- an enforceable boundary can reject the invalid result or transition;

- verification targets that authoritative path.

When the answer is wrong, the graph leads to a bounded location where the correction belongs.

The threshold is crossed when this structure breaks:

- one decision hides multiple output facts;

- multiple decisions produce equivalent or competing facts;

- one fact has multiple writers;

- a decision reads an unauthoritative or unresolved input;

- implementation introduces hidden judgment;

- presentation substitutes for enforcement;

- a dependency cycle prevents a stable evaluation order;

- tests verify copied logic rather than the authoritative decision.

Above the threshold, an error no longer tells you where to fix it. Local patches accumulate, policies drift, and every future change requires rediscovery.

A mechanical threshold check is:

1. Can the wrong output be named as one fact?

2. Does exactly one decision or external writer own that fact?

3. Does that decision produce only that fact?

4. Does every input fact have exactly one authority?

5. Are all applicable policies and how they combine recorded for the output?

6. Is there a boundary that can reject the invalid result or transition?

7. Does verification exercise that authoritative path?

If any answer is no, the system is not yet reliably correctable.

## Example decision file

`decisions/D003-determine-handoff-readiness.md`:

```
---
status: active
domain: handoff
id: D003
title: "Determine handoff readiness"
updated_at: 2026-08-20
---

## Requirement

Another owner must be able to continue a task without losing work or
receiving a task that cannot be acted on.

## Question

Is this task ready to enter handoff now?

## Input facts

- `task.status`
  - Kind: root
  - Authority: task lifecycle store
- `workspace.cleanliness`
  - Kind: root
  - Authority: workspace state observer
- `assignee.readiness`
  - Kind: derived
  - Produced by: D002 — Determine assignee readiness

## Invariants

- A task reported as ready for handoff has no unrecoverable work.
- A task reported as ready has a receiving assignee who can act on it.

## Policy

- Task eligibility policy: the task must be active.
- Work preservation policy: the workspace must be clean or recoverably snapshotted.
- Assignee readiness policy: `assignee.readiness` must be ready.

All three policies must pass for the output to be `ready`. Otherwise return
`blocked`, using the first failing policy in the order above as the reason.

## Output fact

- Name: `handoff.readiness`
- Meaning: Whether the task currently satisfies every precondition for handoff.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot change independently of it.

## Enforcement

The `start-handoff` command must reject the transition whenever
`handoff.readiness.state` is `blocked`.

## Verification

- Blocks when the task is not active.
- Blocks when work is neither clean nor recoverably snapshotted.
- Blocks when the receiving assignee is not ready.
- Returns ready only when every required input permits handoff.
- When multiple policies fail, reports the first failure in the declared order.
- The command rejects every blocked result.
```

The corresponding graph fragment is:

```
(task.status) ──────────────────┐
(workspace.cleanliness) ────────┼──▶ [D003] ──▶ (handoff.readiness)
(assignee.readiness) ───────────┘
```

D003 produces one fact. It does not also produce authorization, assignment state, audit severity, or UI presentation state. Those are separate uncertainties and, when needed, belong to separate decisions.

## Optional tools

The smallest implementation may need only:

```
SCHEMA.md
decisions/*.md
index.md
log.md
```

The current skill maintains records and views directly. Add automation when repeated maintenance problems justify its cost.

At small scale, `index.md`, filename search, and ordinary text search are enough. At larger scale, add full-text or graph search without changing the authoritative Markdown model.

Runtime decision traces may later record:

```
output fact
producing decision
input fact values and versions
policy version
resolved value and reason
enforcement result
```

This allows a wrong runtime answer to be traced directly back into the ledger graph.

## Human and agent roles

The human supplies intent, resolves normative ambiguity, approves policy choices, and adjudicates disagreements between the ledger and the implementation.

The agent reads `SCHEMA.md`, routes through `index.md`, locates existing fact ownership, derives candidate decisions, maintains the Markdown files, updates cross-references, appends semantic log entries, updates the graph, and traces impact. It reviews those artifacts against the project's schema, including their references and dependency relationships.

The agent proposes and maintains. The system constrains. The human decides where judgment is irreducible.

## Why this works

The expensive part of changing a system is often not editing code. It is reconstructing the reasoning required to know which code should change and how to prove the change is safe.

Decision Engineering makes that reasoning persistent and graph-shaped.

Instead of searching the entire codebase for scattered conditions, a developer or agent starts from the output fact and opens its one producing decision. Instead of discovering dependencies after a regression, the fact graph reveals downstream decisions before the change. Instead of hiding multiple responsibilities inside one policy, the one-output-fact invariant forces the uncertainty to be split into atomic decisions.

This lowers the Cost of the Next Change:

```
search → decision → modification → verification
```

The ledger compounds because every accepted decision becomes a reusable node in the system's reasoning graph.

The ledger's parts have distinct roles:

```
SKILL.md        = ledger maintenance workflow
SCHEMA.md       = record contract and invariants

decisions/*.md = authoritative decision facts and policies
index.md        = derived routing view

graph.mmd       = derived dependency view
log.md          = transition history

humans/agents   = maintainers
```

The system becomes easier to change because its uncertainties have stable owners, its facts have explicit authorities, and its errors have bounded places to live.
