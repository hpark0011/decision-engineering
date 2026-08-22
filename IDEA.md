# Decision Engineering

A pattern for building systems whose decisions remain explicit, authoritative, enforceable, traceable, and correctable as the system changes.

This is an idea file. It is designed to be copied into an LLM agent such as Codex, Claude Code, Cursor, or another coding agent. Its purpose is to communicate the high-level architecture and operating rules. The human and agent can instantiate the exact conventions, scripts, and code bindings for a particular system.

## The core idea

Most software work starts with a requirement and jumps directly into implementation:

```text
requirement → code → behavior
```

The reasoning in between is rarely preserved as a first-class artifact. It becomes scattered across UI conditions, API handlers, database constraints, workers, tests, tickets, comments, and people's memory.

Every meaningful change then forces the system to reconstruct its own reasoning:

- What question was this behavior answering?
- Which facts were supposed to determine the answer?
- Which policy turned those facts into the answer?
- Which boundary was supposed to prevent an invalid result?
- Which other decisions and consumers depend on it?
- Was the behavior wrong, or did the intended decision change?

Nothing compounds. The same decisions are repeatedly rediscovered and often reimplemented in slightly different ways.

Decision Engineering introduces a persistent reasoning layer between requirements and behavior:

```text
requirements → decision ledger → code → behavior
                        ↓
                 projections
                        ↓
              UI, APIs, agents, reports
```

The decision ledger is not one monolithic YAML file. It is a maintained directory of schema-constrained Markdown files. Each file contains one authoritative decision. Facts connect those decisions into a graph.

```text
input facts → decision policy → one output fact
```

When a new requirement arrives, the agent does not immediately add logic. It first routes through the existing ledger:

- If an existing decision already produces the required fact, the new feature consumes that decision's projection.
- If the answer should change, the owning decision is edited.
- Only a genuinely new question creates a new decision file.

The reasoning is derived once, written into the ledger, and maintained as the system changes. Consumers reuse resolved facts instead of recreating the policy.

The ledger is the source code of intent.

## The central unit

A decision is a named answer to a question the system must answer to make progress.

It is a step that removes uncertainty.

A task is work to be performed. A decision is the conclusion that the work is meant to establish.

```text
Task:     Review whether this task can be handed off.
Decision: May this task enter handoff now?
```

A decision reads authoritative input facts, applies one policy, and produces exactly one authoritative output fact.

```text
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

```text
handoff.readiness = {
  state: "blocked",
  reason: "The workspace contains uncommitted changes"
}
```

`state` is the resolved answer. `reason` explains that same answer. The reason cannot be changed independently without changing or misrepresenting the answer.

This is not one fact:

```text
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

```text
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

```text
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

```text
SCHEMA.md       = constitution of the ledger
                  conventions, policies, invariants, and workflows

decisions/*.md = authoritative current decision records

index.md        = routing projection over all decision records

log.md          = append-only semantic history of ledger changes

graph.mmd       = generated dependency projection of facts and decisions
```

`SCHEMA.md` and `decisions/*.md` define the current decision system. `log.md` records how that system changed. `index.md` and the graph make the authoritative records fast to navigate, but they must not contain unique decision logic.

### Code and runtime behavior

The implementation makes the decisions executable. It observes root facts, evaluates policies, produces derived facts, enforces invariants, changes state, and publishes projections.

The decision files are authoritative for intent. The code is authoritative for actual behavior.

```text
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

```text
| ID   | Decision                    | Produces                | Reads                              | Status |
|------|-----------------------------|-------------------------|------------------------------------|--------|
| D003 | Determine handoff readiness | `handoff.readiness`     | `task.status`, `workspace.clean`   | active |
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

```text
## [2026-08-20] edit | D003 | Determine handoff readiness
```

A useful entry records:

```markdown
## [2026-08-20] edit | D003 | Determine handoff readiness

Reason:
The system may now hand off work when unsaved changes have been captured
in a recoverable snapshot.

Changed:
- Added input fact `workspace.snapshot-status`.
- Revised the policy and invariant.
- Added two verification cases.

Affected:
- `handoff.readiness`
- D004 — Authorize task handoff
- Task detail UI
- Handoff API
```

At minimum, the log records create, edit, and delete operations. A mature ledger will usually also use rename, supersede, retire, restore, schema-change, and lint entries.

Prefer superseding or retiring an adopted decision over deleting it. Stable IDs may already be referenced by requirements, commits, tests, logs, or downstream decisions. Hard deletion should be reserved for accidental records that never became part of the accepted ledger.

The log records semantic changes, not every wording correction. A change belongs in `log.md` when it changes ownership, meaning, dependencies, policy, invariant, enforcement, projection, consumers, verification, or lifecycle state.

### `SCHEMA.md`: the constitution

`SCHEMA.md` tells humans and agents how the ledger is structured and maintained.

It defines:

- what counts as a decision;
- what counts as a fact;
- the one-decision-to-one-output-fact invariant;
- the atomicity tests for structured outputs;
- how root and derived facts are identified;
- decision ID and filename conventions;
- required headings and their order;
- how fact references are written;
- allowed graph nodes and edges;
- how projections and consumers are represented;
- how enforcement and verification are recorded;
- how decisions are created, edited, renamed, superseded, retired, and deleted;
- when `index.md`, `log.md`, and generated artifacts must change;
- which deterministic lint checks must pass before a ledger change is accepted.

`SCHEMA.md` should be precise enough that two agents following it produce structurally compatible decision files.

The schema will evolve as the system teaches you what is missing. A schema change is itself a logged change and may require migrating existing decision files.

## Decision files

Each file in `decisions/` contains one decision ledger.

```text
one Markdown file
    = one decision
    = one question
    = one policy
    = one output fact
```

Use a stable ID followed by a descriptive filename:

```text
D003-determine-handoff-readiness.md
```

The description makes the file discoverable. The stable ID keeps references intact when wording improves or the file is renamed. IDs are never renumbered or reused.

A decision file should contain these sections:

```markdown
# D003 — Determine handoff readiness

Status: active

## Requirement

## Question

## Input facts

## Output fact

## Invariant

## Policy

## Enforcement

## Projection

## Consumers

## Verification
```

Optional sections may include source references, open questions, implementation bindings, supersession metadata, or notes, but they must not weaken the required structure.

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

### Output fact

The one authoritative fact produced by the decision.

The record should define its stable name, meaning, possible values or shape, and what makes it atomic.

### Invariant

What must never become false while the output fact or resulting state is accepted as valid.

### Policy

The rule that maps the input facts to the output fact.

Facts describe. The policy decides.

### Enforcement

The boundary that can reject an invalid action or state transition.

A disabled button, warning message, or hidden control is presentation, not enforcement. Enforcement must exist at a boundary that cannot be bypassed by another consumer.

### Projection

The named consumer-facing representation of the output fact.

A projection may rename fields, hide internal evidence, or attach a reason to the resolved answer. It may not make another policy choice. If creating a projection requires a new judgment, that judgment is another decision and must produce its own fact.

```text
decision → output fact → projection → consumers
```

### Consumers

The UI, API, worker, agent, report, or downstream decision that uses the projection or output contract.

A consumer must not re-derive the decision from raw inputs.

### Verification

The tests, assertions, simulations, or other checks that prove the authoritative policy and invariant.

Verification should target the owning decision and its enforcement boundary. It must not recreate a second copy of the policy inside the test and then merely prove that the two copies agree.

## The decision graph

The ledger forms a directed bipartite graph with two primary node types:

```text
facts ↔ decisions
```

The core edge types are:

```text
fact     --input-to--> decision
decision --produces--> fact
```

A decision may have many incoming fact edges but exactly one outgoing `produces` edge.

A fact may have many outgoing consumer edges but at most one incoming `produces` edge.

```text
(task.status) ──────────────────┐
(workspace.cleanliness) ────────┼──▶ [D003: Determine handoff readiness]
(assignee.readiness) ───────────┘                    │
                                                      ▼
                                           (handoff.readiness)
```

A downstream decision may consume that result:

```text
(handoff.readiness) ────────────┐
(actor.handoff-permission) ─────┴──▶ [D004: Authorize task handoff]
                                                     │
                                                     ▼
                                          (handoff.authorization)
```

The resulting structure is:

```text
fact → decision → fact → decision → fact
```

### Root facts and derived facts

Not every fact is produced by another decision.

A root fact is observed or written by an authoritative source outside the decision graph:

```text
task.status
current-time
payment-processor.response
user.submitted-email
workspace.cleanliness
```

Each root fact must declare exactly one authoritative writer or observation boundary.

A derived fact is produced by exactly one decision:

```text
handoff.readiness
payment.eligibility
account.access-level
```

Graphically:

```text
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
 6. Every projection originates from one decision output.
 7. A projection may transform representation but may not introduce a new judgment.
 8. Every consumer points to a projection or an authoritative output contract rather than recreating the policy.
 9. Every decision has an invariant, enforcement obligation, and verification obligation, or an explicit schema-approved reason one is not applicable.
10. Every active decision is indexed, and every active index entry resolves to one decision file.

A same-evaluation dependency cycle is invalid because no decision can resolve first:

```text
D001 needs fact B
D002 produces fact B but needs fact A
D001 produces fact A
```

Temporal feedback is allowed only when the time boundary is explicit. For example, a decision may read `previous-period.risk-score` as a root or persisted state fact rather than directly depending on its own current output.

The graph is a generated projection. The decision files remain authoritative.

## Domains

A domain is a boundary within which a group of decisions and facts must remain correct together.

Domains should be derived from the decision graph and its invariants rather than chosen from implementation layers such as UI, API, database, worker, or queue.

Two decisions belong in the same domain when their owned state must change together to preserve an invariant; changing one independently would create an invalid observable state.

Domains are useful for routing, impact analysis, and visualization, but they should not control the physical folder structure. Keep decision files stable and flat; let `index.md` and the graph group them by the current domain model.

Cross-domain consumers should receive named projections rather than reading another domain's private root facts and reconstructing its decisions.

## Operations

### Locate before creating

Every operation begins by reading `SCHEMA.md` and scanning `index.md`.

Before creating a decision, ask:

- Does an existing decision already answer this question?
- Does an existing output fact already represent the answer?
- Is this only a new consumer of an existing projection?
- Is the requirement changing an existing policy, invariant, input, or output meaning?
- What genuinely new uncertainty remains unresolved?

Do not create a second decision that produces a synonymous version of an existing fact.

### Create a decision

To create a new decision:

 1. Restate the requirement as an outcome, without implementation details.
 2. Write the exact question the system must answer.
 3. Locate or define every authoritative input fact.
 4. Define one output fact.
 5. Run the output atomicity tests. Split the decision when the output contains independently changing facts.
 6. Write the invariant and policy.
 7. Identify the enforcement boundary.
 8. Define the projection and known consumers.
 9. Write verification obligations.
10. Assign a stable decision ID and descriptive filename.
11. Add the decision file.
12. Update or regenerate `index.md` and the graph.
13. Append a create entry to `log.md`.
14. Run deterministic lint.

A decision is not accepted while its output ownership or input authorities are ambiguous.

### Edit a decision

To change behavior:

1. Locate the decision that owns the affected output fact.
2. Identify whether the change affects the requirement, question, inputs, output meaning, invariant, policy, enforcement, projection, consumers, or verification.
3. Edit the authoritative decision file.
4. Walk the graph downstream from the changed output fact.
5. Update affected consumers, decisions, code, and verification.
6. Regenerate the index and graph.
7. Append an edit entry to `log.md` explaining the semantic change and impact.
8. Run lint and tests.

If an edit causes the decision to produce more than one fact, split it into multiple decisions rather than expanding the original file.

### Consume a decision

A new UI, API, worker, or agent usually does not require a new decision.

If the required answer already exists:

1. add the new consumer to the owning decision;
2. expose or reuse an appropriate projection;
3. ensure the consumer does not re-derive the policy;
4. update the index and log when required by the schema.

Prefer one strong decision with many consumers over many copies of the same policy.

### Supersede, retire, or delete

When a question has been replaced by a different question or output fact, mark the old decision as superseded and point to its successor.

When a decision is no longer used but remains historically meaningful, retire it.

Delete only when the file was created accidentally or never became an accepted part of the ledger. Log every deletion with the reason and affected references.

Never reuse a deleted, retired, or superseded decision ID.

### Diagnose an error

When the system produces a wrong result, start from the wrong fact and walk backward:

```text
wrong observed output
    → projection
    → authoritative output fact
    → producing decision
    → policy and invariant
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
- the invariant omitted a forbidden state;
- enforcement was absent or bypassed;
- the projection misrepresented the fact;
- a consumer recreated the policy;
- verification missed the failing case;
- the recorded intent itself was wrong.

Do not patch the nearest visible surface before locating the fact and decision that own the answer.

### Lint

A deterministic linter should parse the schema-constrained Markdown and validate the ledger graph.

Useful checks include:

- every decision file has one stable unique ID;
- every required heading exists exactly once;
- every decision produces exactly one fact;
- every derived fact has exactly one producer;
- every root fact has exactly one declared writer or observation boundary;
- every fact reference resolves;
- fact names are unique and follow the schema convention;
- no synchronous dependency cycle exists;
- projections point to their owning output fact;
- projections do not declare independent policy;
- consumers reference projections or authoritative outputs;
- active decision files and index entries match;
- every semantic ledger change has a corresponding log entry;
- supersession and retirement links resolve;
- enforcement and verification bindings point to real code when marked bound;
- generated graph and index files match the decision records.

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
8. Do consumers use the projection without re-deriving the answer?

If any answer is no, the system is not yet reliably correctable.

## Example decision file

`decisions/D003-determine-handoff-readiness.md`:

```markdown
# D003 — Determine handoff readiness

Status: active
Domain: handoff

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

## Output fact

- Name: `handoff.readiness`
- Meaning: Whether the task currently satisfies every precondition for handoff.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot change independently of it.

## Invariant

A task reported as ready for handoff has no unrecoverable work and has a
receiving assignee who can act on it.

## Policy

Return `ready` when the task is active, the workspace is clean or recoverably
snapshotted, and `assignee.readiness` is ready. Otherwise return `blocked`
with the first authoritative blocking reason.

## Enforcement

The `start-handoff` command must reject the transition whenever
`handoff.readiness.state` is `blocked`.

## Projection

`handoff.readiness.public`

Exposes:
- `state`
- `reason`

The projection may hide internal evidence but may not recompute readiness.

## Consumers

- D004 — Authorize task handoff
- Task detail UI
- Handoff API
- Automation agent

## Verification

- Blocks when the task is not active.
- Blocks when work is neither clean nor recoverably snapshotted.
- Blocks when the receiving assignee is not ready.
- Returns ready only when every required input permits handoff.
- The command rejects every blocked result.
```

The corresponding graph fragment is:

```text
(task.status) ──────────────────┐
(workspace.cleanliness) ────────┼──▶ [D003] ──▶ (handoff.readiness)
(assignee.readiness) ───────────┘
```

D003 produces one fact. It does not also produce authorization, assignment state, audit severity, or UI presentation state. Those are separate uncertainties and, when needed, belong to separate decisions.

## Optional tools

The smallest implementation may need only:

```text
SCHEMA.md
decisions/*.md
index.md
log.md
```

Useful deterministic tools can be added as the ledger grows:

```text
scripts/ledger_lint.py    validate structure and graph invariants
scripts/ledger_index.py   generate index.md from decision files
scripts/ledger_graph.py   generate Mermaid, DOT, or JSON graph output
scripts/ledger_new.py     allocate an ID and create a valid decision template
```

At small scale, `index.md`, filename search, and ordinary text search are enough. At larger scale, add full-text or graph search without changing the authoritative Markdown model.

Runtime decision traces may later record:

```text
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

Instead of searching the entire codebase for scattered conditions, a developer or agent starts from the output fact and opens its one producing decision. Instead of allowing every surface to reinterpret raw facts, the decision publishes a projection. Instead of discovering dependencies after a regression, the fact graph reveals downstream decisions and consumers before the change. Instead of hiding multiple responsibilities inside one policy, the one-output-fact invariant forces the uncertainty to be split into atomic decisions.

This lowers the Cost of the Next Change:

```text
search → decision → modification → verification
```

The ledger compounds because every accepted decision becomes a reusable node in the system's reasoning graph.

The architecture also applies Decision Engineering to itself:

```text
SCHEMA.md       = policy and invariants of the ledger system
linter          = enforcement and verification

decisions/*.md = authoritative decision facts and policies
index.md        = routing projection

graph.mmd       = dependency projection
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
- projections expose resolved facts without introducing new judgment;
- consumers do not re-derive authoritative decisions;
- verification targets the authoritative policy and enforcement boundary;
- the ledger and code remain explicitly reconcilable.

Share this file with an LLM agent and instantiate the smallest version that makes those constraints real for your system.