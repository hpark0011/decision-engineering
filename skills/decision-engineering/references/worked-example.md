# Worked example: handoff readiness

## Requirement

> Another owner must be able to continue a task without losing work or receiving a task that cannot be acted on.

## Locate and route

Search the index for `handoff`, the expected readiness answer, and known input facts.

- If `handoff.readiness` already exists, reuse that output fact. No ledger change is needed when its meaning and dependencies stay the same.
- If readiness semantics change, edit the decision that produces `handoff.readiness` and trace downstream impact.
- If no decision resolves readiness, create one.

## New decision

```markdown
---
status: active
domain: handoff
id: D003
title: "Determine handoff readiness"
updated_at: 2026-08-20
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

- Task eligibility policy: the task must be active.
- Work preservation policy: the workspace must be clean or recoverably snapshotted.
- Assignee readiness policy: `assignee.readiness` must be ready.

All three policies must pass for the output to be `ready`. Otherwise return `blocked`, using the first failing policy in the order above as the reason.

## Output fact

- Name: `handoff.readiness`
- Meaning: Whether the task currently satisfies every precondition for handoff.
- Shape: `{ state: ready | blocked, reason: string }`
- Atomicity: `reason` explains `state` and cannot change independently.

## Enforcement

The start-handoff boundary must reject the transition whenever `handoff.readiness.state` is `blocked`.

## Verification

- Block when the task is not active.
- Block when work is neither clean nor recoverably snapshotted.
- Block when the receiving assignee is not ready.
- Return ready only when every required input permits handoff.
- When multiple policies fail, report the first failure in the declared order.
- Reject every blocked result at the start-handoff boundary.
```

The three policies jointly resolve one readiness proposition. The output is atomic because `reason` explains that same proposition. Authorization, assignment state, audit severity, and UI presentation state would be independently decidable and therefore require separate decisions.

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

Follow the [review and view-maintenance workflow](../SKILL.md#review-and-refresh-the-views), then cite D003 from implementation work.

## Small-change counterexample

For “add a keyboard shortcut to archive the selected task,” first locate the owner of `task.archivability`.

- If it exists, make the shortcut use `task.archivability`. The ledger stays unchanged when the existing policy and dependencies already cover the action.
- If it does not exist, create the one question “May the selected task be archived now?” and one output fact `task.archivability`.

Proportionality changes the size of the delta, not whether intent is recorded.
