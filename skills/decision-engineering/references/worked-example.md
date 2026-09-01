# Worked example: handoff readiness

## Requirement

> Another owner must be able to continue a task without losing work or receiving a task that cannot be acted on.

## Locate and route

Search the index for `handoff`, the expected readiness answer, and known input facts.

- If `handoff.readiness` already exists, add the new UI, API, worker, or agent as a consumer of that output fact. Create no decision.
- If readiness semantics change, edit the decision that produces `handoff.readiness` and trace downstream impact.
- If no decision resolves readiness, create one.

## New decision

```markdown
---
status: active
domain: handoff
id: D003
title: "Determine handoff readiness"
---

## Requirement

Another owner must be able to continue a task without losing work or receiving a task that cannot be acted on.

## Question

Is this task ready to enter handoff now?

## Input facts

- `task.status`
  - Kind: root
  - Authority: task-lifecycle-store
- `workspace.cleanliness`
  - Kind: root
  - Authority: workspace-state-observer
- `assignee.readiness`
  - Kind: derived
  - Produced by: D002

## Invariants

- A task reported as ready has no unrecoverable work.
- A task reported as ready has a receiving assignee who can act on it.

## Policy

Return `ready` when the task is active, the workspace is clean or recoverably snapshotted, and `assignee.readiness` is ready. Otherwise return `blocked` with the first authoritative blocking reason.

## Output fact

- Name: `handoff.readiness`
- Meaning: Whether the task currently satisfies every precondition for handoff.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot change independently.

## Enforcement

The start-handoff boundary must reject the transition whenever `handoff.readiness.state` is `blocked`.

## Consumers

- D004 — Authorize task handoff; reads `handoff.readiness` directly.
- Task detail UI; formats `state` and `reason` without recomputing readiness.
- Handoff API; exposes `state` and `reason` without recomputing readiness.
- Automation agent; reads `handoff.readiness` directly.

## Verification

- Block when the task is not active.
- Block when work is neither clean nor recoverably snapshotted.
- Block when the receiving assignee is not ready.
- Return ready only when every required input permits handoff.
- Reject every blocked result at the start-handoff boundary.
```

The output is atomic because `reason` explains the same readiness proposition. Authorization, assignment state, audit severity, and UI presentation state would be independently decidable and therefore require separate decisions.

## Semantic log entry

```markdown
## [2026-08-20] create | D003 | Determine handoff readiness

Reason:
Handoff readiness had no authoritative owner.

Changed:
- Added D003 producing `handoff.readiness`.
- Declared two root facts and one derived input.

Affected:
- D004 — Authorize task handoff
- Task detail UI
- Handoff API
- Automation agent
```

Render the index and graph, lint, then cite D003 from implementation work.

## Small-change counterexample

For “add a keyboard shortcut to archive the selected task,” first locate the owner of `task.archivability`.

- If it exists, add `Keyboard shortcut` to that decision's consumers. The delta contains zero new decisions.
- If it does not exist, create the one question “May the selected task be archived now?” and one output fact `task.archivability`.

Proportionality changes the size of the delta, not whether intent is recorded.
