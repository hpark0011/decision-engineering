# Decision Engineering

This is an idea file inspired by Andrej Karpathy's [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). It is designed to be copied into an LLM agent such as Codex, Claude Code, Cursor, or another coding agent. Its purpose is to communicate the high-level architecture and operating rules for builders who want to create their own skill instead of using the pre-built skill.

## The core idea

Decision Engineering is the discipline of building reliable decision systems out of unreliable decision-makers.

Humans forget context, make implicit assumptions, disagree, and sometimes make the wrong call. Agents hallucinate, lose context, reason differently across runs, and confidently produce incorrect outputs. A system that depends on their judgment cannot become reliable by demanding that every person or agent be right every time.

A reliable decision system assumes that individual judgments will fail. It must be able to catch a mistake, contain its effects, locate its source, and recover from it.

Consider a product whose subscription price is `$49`. Most systems can store that price as a source of truth for current state, but they cannot answer why `$49` is the right price. Perhaps customer acquisition cost is `$35` and the business wants to recover it within two months. Perhaps a test showed that `$39` performed worse. Perhaps a customer contract constrains the price. Or perhaps `$49` was only a guess.

Now imagine an agent is asked to improve conversion. It can see the price, but it cannot tell which assumptions the price depends on, which decision owns it, or what else relies on it. The agent may make a locally reasonable change that silently breaks the margin target, billing, forecasts, and marketing.

The core problem is not simply that the agent must rediscover old reasoning. The system has no authoritative structure for distinguishing state from intent, checking whether the assumptions behind a decision still hold, or containing a wrong judgment before it propagates.

Decision Engineering makes each important decision a first-class architectural object:

```
goal → requirement → input facts → decision policy → one output fact → consumers
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

The pricing decision has one clear job and produces one authoritative fact. Its inputs, policy, and invariants are visible. Every downstream consumer reads the same output instead of reinterpreting the raw facts or making its own pricing decision.

If the price is wrong, the system provides a bounded path back to the pricing decision and the facts behind it. If CAC changes from `$35` to `$70`, the system can identify the decision that must be revisited and the consumers affected by its output. The error has an owner, and its blast radius is visible.

This gives the system a source of truth for intent, not only state:

```
state  = what the system is
intent = why it is that way
```

The decision ledger makes that structure authoritative. It is not one monolithic YAML file. It is a maintained directory of schema-constrained Markdown files. Each file contains one decision, and facts connect those decisions into a graph.

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

A decision reads authoritative input facts, applies one policy, and produces exactly one authoritative output fact.

```
(fact A) ──┐
(fact B) ──┼──▶ [decision] ──▶ (one output fact)
(fact C) ──┘
```

This creates the core structural rule:

> One decision file resolves one question and produces one fact.

A decision may read many facts. A fact may be read by many decisions. But every decision produces exactly one fact, and every derived fact has exactly one producing decision.

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

Those fields answer different questions. They can change independently, have different consumers, and require different policies. They belong to separate decisions.

Use these tests whenever output atomicity is unclear:

1. Could one part change while the other parts remain valid?

2. Could one part be correct while another part is wrong?

3. Could a consumer need one part without accepting the others?

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

The implementation makes the decisions executable. It observes root facts, evaluates policies, produces derived facts, enforces invariants, changes state, and makes authoritative output facts available to consumers.

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

Its job is not to explain every decision in full. Its job is to route quickly from a requirement, fact, consumer, or domain to the correct source file.

A useful index entry contains:

```
| ID   | Decision                    | Produces                | Reads                            | Status |
|------|-----------------------------|-------------------------|----------------------------------|--------|
| D003 | Determine handoff readiness | `handoff.readiness`     | `task.status`, `workspace.clean` | active |
```

The most important routing key is usually the output fact. When an agent needs to know who owns `handoff.readiness`, the index should point directly to the one decision that produces it.

The index may also organize decisions:

- by output fact;

- by domain;

- by requirement or capability;

- by consumer;

- by status, including active, superseded, and retired decisions.

The lookup workflow is:

1. Read `index.md`.

2. Search by the uncertainty being resolved, the expected output fact, known input facts, consumer, or requirement terms.

3. Open the smallest set of candidate decision files.

4. Follow their fact links upstream or downstream when more context is needed.

5. Search the entire `decisions/` folder only when the index cannot route the request.

`index.md` should be generated from the decision files or deterministically verified against them. It must never become a second source of decision logic.

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

At minimum, the log records create, edit, and delete operations. A mature ledger will usually also use rename, supersede, retire, restore, schema-change, and lint entries.

Prefer superseding or retiring an adopted decision over deleting it. Stable IDs may already be referenced by requirements, commits, tests, logs, or downstream decisions. Hard deletion should be reserved for accidental records that never became part of the accepted ledger.

The log records semantic changes, not every wording correction. A change belongs in `log.md` when it changes ownership, meaning, dependencies, policy, invariants, enforcement, consumers, verification, or lifecycle state.

### `SCHEMA.md`: the constitution

`SCHEMA.md` tells humans and agents how the ledger is structured and maintained.

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

- how consumers and implementation bindings are represented;

- how enforcement and verification are recorded;

- how decisions are created, edited, renamed, superseded, retired, and deleted;

- when `index.md`, `log.md`, and generated artifacts must change;

- which deterministic lint checks must pass before a ledger change is accepted.

`SCHEMA.md` should be precise enough that two agents following it produce structurally compatible decision files.

The schema will evolve as the system teaches you what is missing. A schema change is itself a logged change and may require migrating existing decision files.

## Decision files

Each file in `decisions/` contains one decision record.

```
one Markdown file
    = one decision
    = one question
    = one policy
    = one output fact
```

Use a stable ID followed by a descriptive filename:

```
D003-determine-handoff-readiness.md
```

The description makes the file discoverable. The stable ID keeps references intact when wording improves or the file is renamed. IDs are never renumbered or reused.

A decision file should begin with YAML frontmatter and contain these sections in this order:

```
---
status: active
domain: handoff
id: D003
title: "Determine handoff readiness"
---

## Requirement

## Question

## Input facts

## Invariants

## Policy

## Output fact

## Enforcement

## Consumers

## Verification
```

Optional metadata or sections may include source references, implementation bindings, supersession metadata, or notes, but they must not weaken the required structure.

### Requirement

The outcome or intent that makes the decision necessary.

A requirement says what must become true, not how the implementation should work.

### Question

The exact uncertainty the decision resolves.

It should be answerable with one authoritative output fact.

### Input facts

The authoritative facts read by the policy.

Input facts are referenced by stable fact identity, not recreated as loosely equivalent prose. Each one must resolve to either:

- a root fact with one declared external writer or observer; or

- a derived fact produced by exactly one other decision.

### Invariants

What must never become false while the output fact or resulting state is accepted as valid.

A decision may have multiple invariants, but they must all constrain the same policy and output fact. If an invariant requires a separately decidable answer, split it into another decision.

### Policy

The rule that maps the input facts to the output fact while preserving the invariants.

Facts describe. The policy decides.

### Output fact

The one authoritative fact produced by the decision.

The record should define its stable name, meaning, possible values or shape, and what makes it atomic.

### Enforcement

The boundary that can reject an invalid action or state transition.

A disabled button, warning message, or hidden control is presentation, not enforcement. Enforcement must exist at a boundary that cannot be bypassed by another consumer.

### Consumers

The UI, API, worker, agent, report, or downstream decision that reads the authoritative output fact.

A consumer must not re-derive the decision from raw inputs.

A consumer may format, rename, omit, or transport an output fact as an implementation detail. That representation does not belong in the decision schema and does not become another authoritative fact.

If producing a consumer-facing value requires new judgment, classification, defaulting, or a policy branch, it is not merely representation. It requires another decision with its own authoritative output fact.

```
mechanical adaptation:
output fact → format, rename, omit, or transport → consumer

new judgment:
output fact → new decision → new output fact → consumer
```

### Verification

The tests, assertions, simulations, or other checks that prove the authoritative policy, invariants, and enforcement boundary.

Verification should target the owning decision and its enforcement boundary. It must not recreate a second copy of the policy inside the test and then merely prove that the two copies agree.

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

A fact may have many outgoing consumer edges but at most one incoming `produces` edge.

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

A fact with neither a producer nor an external writer is unauthoritative. A fact with multiple producers or writers is ambiguous. Both are lint errors.

### Graph invariants

The graph must satisfy these mechanical constraints:

 1. Every decision has exactly one output fact.

 2. Every derived fact has exactly one producing decision.

 3. Every root fact has exactly one authoritative external writer or observer.

 4. Every input fact reference resolves to an existing fact identity.

 5. A decision may not list the same fact as both an unresolved input and its output.

 6. Every consumer reads an authoritative output fact rather than recreating its policy.

 7. Formatting, renaming, omission, or transport does not create another authoritative fact.

 8. A consumer-facing value that introduces new judgment is produced by a separate decision.

 9. Every decision has invariants, an enforcement obligation, and verification obligations, or an explicit schema-approved reason one is not applicable.

10. Every active decision is indexed, and every active index entry resolves to one decision file.

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

Cross-domain consumers should therefore read authoritative output facts rather than reading another domain's private root facts and reconstructing its decisions.

## Operations

### Locate before creating

Every operation begins by reading `SCHEMA.md` and scanning `index.md`.

Before creating a decision, ask:

- Does an existing decision already answer this question?

- Does an existing output fact already represent the answer?

- Is this only a new consumer of an existing output fact?

- Is the requirement changing an existing policy, invariant, input, or output meaning?

- Does the proposed consumer-facing value introduce new judgment?

- What genuinely new uncertainty remains unresolved?

Do not create a second decision that produces a synonymous version of an existing fact.

### Create a decision

To create a new decision:

 1. Restate the requirement as an outcome, without implementation details.

 2. Write the exact question the system must answer.

 3. Locate or define every authoritative input fact.

 4. Write the invariants.

 5. Write the policy that maps the inputs to one answer.

 6. Define one output fact.

 7. Run the output atomicity tests and split the decision when the output contains independently changing facts.

 8. Identify the enforcement boundary.

 9. List known consumers.

10. Treat mechanical consumer adaptations as implementation details.

11. Create another decision if a consumer-facing value requires new judgment.

12. Write verification obligations.

13. Assign a stable decision ID and descriptive filename.

14. Add the decision file.

15. Update or regenerate `index.md` and the graph.

16. Append a create entry to `log.md`.

17. Run deterministic lint.

A decision is not accepted while its output ownership or input authorities are ambiguous.

### Edit a decision

To change behavior:

1. Locate the decision that owns the affected output fact.

2. Identify whether the change affects the requirement, question, inputs, invariants, policy, output meaning, enforcement, consumers, or verification.

3. Edit the authoritative decision file.

4. Walk the graph downstream from the changed output fact.

5. Update affected consumers, decisions, code, and verification.

6. Regenerate the index and graph.

7. Append an edit entry to `log.md` explaining the semantic change and impact.

8. Run lint and tests.

If an edit causes the decision to produce more than one fact, split it into multiple decisions rather than expanding the original file.

### Consume a decision

A new UI, API, worker, report, or agent usually does not require a new decision.

If the required answer already exists:

1. Add the new consumer to the owning decision.

2. Make the consumer read the authoritative output fact.

3. Adapt the fact mechanically when formatting, renaming, omission, or transport is required.

4. Create another decision if the consumer-facing value requires new judgment.

5. Ensure the consumer does not re-derive the policy.

6. Update the index and log when required by the schema.

Prefer one strong decision with many consumers over many copies of the same policy.

### Supersede, retire, or delete

When a question has been replaced by a different question or output fact, mark the old decision as superseded and point to its successor.

When a decision is no longer used but remains historically meaningful, retire it.

Delete only when the file was created accidentally or never became an accepted part of the ledger. Log every deletion with the reason and affected references.

Never reuse a deleted, retired, or superseded decision ID.

### Diagnose an error

When the system produces a wrong result, start from the observed behavior and walk backward:

```
wrong observed output
    → consumer and implementation binding
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

- a consumer misrepresented the authoritative output fact;

- a consumer recreated the policy;

- a judgment-bearing representation was hidden in implementation instead of modeled as a decision;

- verification missed the failing case;

- the recorded intent itself was wrong.

Do not patch the nearest visible surface before locating the fact and decision that own the answer.

### Lint

A deterministic linter should parse the schema-constrained Markdown and validate the ledger graph.

Useful checks include:

- every decision file has one stable unique ID;

- every required frontmatter field exists exactly once;

- every required heading exists exactly once and appears in the required order;

- every decision produces exactly one fact;

- every derived fact has exactly one producer;

- every root fact has exactly one declared writer or observation boundary;

- every fact reference resolves;

- fact names are unique and follow the schema convention;

- no synchronous dependency cycle exists;

- known downstream decisions reference authoritative output facts;

- active decision files and index entries match;

- every semantic ledger change has a corresponding log entry;

- supersession and retirement links resolve;

- enforcement and verification bindings point to real code when marked bound;

- generated graph and index files match the decision records.

Some consumer behavior can only be verified through implementation review or tests. Those checks should confirm that consumers read authoritative output facts, do not recreate policy, and do not introduce hidden judgment.

Lint errors are design flaws. Repair the ownership, atomicity, dependency, or boundary problem rather than suppressing the signal.

## The correction threshold

Decision Engineering is not mainly documentation. Its purpose is to keep wrong answers localizable and correctable.

A decision is below the correction threshold when:

- the observed output traces to exactly one authoritative fact;

- that fact traces to exactly one producing decision or root writer;

- the decision's inputs each trace to one authority;

- the policy is written in one place;

- an enforceable boundary can reject the invalid result or transition;

- verification targets that authoritative path;

- consumers receive the resolved answer rather than re-deriving it.

When the answer is wrong, the graph leads to a bounded location where the correction belongs.

The threshold is crossed when this structure breaks:

- one decision hides multiple output facts;

- multiple decisions produce equivalent or competing facts;

- one fact has multiple writers;

- a decision reads an unauthoritative or unresolved input;

- consumers rebuild the policy from raw facts;

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

5. Is there one written policy for producing the output?

6. Is there a boundary that can reject the invalid result or transition?

7. Does verification exercise that authoritative path?

8. Do consumers read the authoritative output fact without re-deriving the answer?

If any answer is no, the system is not yet reliably correctable.

## Example decision file

`decisions/D003-determine-handoff-readiness.md`:

```
---
status: active
domain: handoff
id: D003
title: "Determine handoff readiness"
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

Return `ready` when the task is active, the workspace is clean or recoverably
snapshotted, and `assignee.readiness` is ready. Otherwise return `blocked`
with the first authoritative blocking reason.

## Output fact

- Name: `handoff.readiness`
- Meaning: Whether the task currently satisfies every precondition for handoff.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot change independently of it.

## Enforcement

The `start-handoff` command must reject the transition whenever
`handoff.readiness.state` is `blocked`.

## Consumers

- D004 — Authorize task handoff
- Task detail UI
- Handoff API
- Automation agent

The UI and API may format or omit fields for their audiences, but they must
read `handoff.readiness` and must not recompute readiness.

## Verification

- Blocks when the task is not active.
- Blocks when work is neither clean nor recoverably snapshotted.
- Blocks when the receiving assignee is not ready.
- Returns ready only when every required input permits handoff.
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

Useful deterministic tools can be added as the ledger grows:

```
scripts/ledger_lint.py    validate structure and graph invariants
scripts/ledger_index.py   generate index.md from decision files
scripts/ledger_graph.py   generate Mermaid, DOT, or JSON graph output
scripts/ledger_new.py     allocate an ID and create a valid decision template
```

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

## Tips and tricks

- Start from the question the system must answer, not the component you plan to build.

- Keep one decision per file and one output fact per decision.

- Use stable fact identities everywhere; do not paraphrase the same fact into multiple names.

- Treat reason strings as explanations of one answer, not as a place to hide additional outputs.

- Prefer root facts that are directly observable over inferred inputs with unclear ownership.

- Let derived facts flow through named decision outputs rather than cross-domain raw reads.

- Prefer one authoritative decision with many consumers over repeated policy.

- Treat mechanical consumer adaptations as implementation details.

- Model consumer-facing judgment as a separate decision and output fact.

- Keep `decisions/` physically flat; organize by domain in generated views.

- Generate or verify `index.md`; do not manually let it drift from the source files.

- Use `log.md` for semantic history and Git for textual history.

- Supersede or retire adopted decisions instead of deleting their history.

- Do not invent implementation bindings before the code exists.

- Treat every multi-output decision as a request to inspect whether multiple uncertainties have been collapsed into one owner.

- Let lint failures force structural repair rather than hiding ambiguity with exceptions.

## Human and agent roles

The human supplies intent, resolves normative ambiguity, approves policy choices, and adjudicates disagreements between the ledger and the implementation.

The agent reads `SCHEMA.md`, routes through `index.md`, locates existing fact ownership, derives candidate decisions, maintains the Markdown files, updates cross-references, appends semantic log entries, generates the graph, traces impact, and performs the bookkeeping required to keep intent coherent.

Deterministic tools verify what can be verified mechanically:

- one file per decision;

- one output fact per decision;

- one producer or writer per fact;

- valid references;

- no forbidden cycles;

- complete indexing;

- required enforcement and verification structure.

The agent proposes and maintains. The system constrains. The human decides where judgment is irreducible.

## Why this works

The expensive part of changing a system is often not editing code. It is reconstructing the reasoning required to know which code should change and how to prove the change is safe.

Decision Engineering makes that reasoning persistent and graph-shaped.

Instead of searching the entire codebase for scattered conditions, a developer or agent starts from the output fact and opens its one producing decision. Instead of allowing every surface to reinterpret raw facts, consumers read the authoritative output fact directly. Instead of discovering dependencies after a regression, the fact graph reveals downstream decisions and consumers before the change. Instead of hiding multiple responsibilities inside one policy, the one-output-fact invariant forces the uncertainty to be split into atomic decisions.

This lowers the Cost of the Next Change:

```
search → decision → modification → verification
```

The ledger compounds because every accepted decision becomes a reusable node in the system's reasoning graph.

The architecture also applies Decision Engineering to itself:

```
SCHEMA.md       = policy and invariants of the ledger system
linter          = enforcement and verification

decisions/*.md = authoritative decision facts and policies
index.md        = generated routing view

graph.mmd       = generated dependency view
log.md          = transition history

humans/agents   = consumers and maintainers
```

The system becomes easier to change because its uncertainties have stable owners, its facts have explicit authorities, and its errors have bounded places to live.

## Note

This document describes the pattern, not one universal implementation.

The exact Markdown syntax, naming convention, generated graph format, search tooling, and implementation-binding strategy may vary. The core constraints should not:

- the ledger is a maintained directory of schema-constrained Markdown files;

- `index.md` routes agents to the authoritative decision quickly;

- `log.md` records semantic creates, edits, deletions, and lifecycle changes;

- `SCHEMA.md` defines the structure and maintenance protocol;

- each decision file resolves one question;

- each decision produces exactly one authoritative fact;

- every derived fact has exactly one producing decision;

- every root fact has exactly one authoritative writer or observation boundary;

- facts connect decisions into a traversable graph;

- policies decide, invariants constrain, and enforcement prevents;

- consumers read authoritative output facts without re-deriving decisions;

- mechanical consumer representations remain implementation details;

- judgment-bearing representations become separate decisions with their own output facts;

- verification targets the authoritative policy and enforcement boundary;

- the ledger and code remain explicitly reconcilable.

Share this file with an LLM agent and instantiate the smallest version that makes those constraints real for your system.
