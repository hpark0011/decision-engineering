---
title: Anatomy of a Decision
created: 2026-08-20
updated: 2026-09-02
type: concept
tags: [decision, requirement, fact, policy, invariant, enforcement, verification]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md, ../skills/decision-engineering/assets/decision-ledger/SCHEMA.md]
confidence: medium
---

# Anatomy of a Decision

**Defined in glossary:** Business requirement, Decision, Authoritative fact, Authoritative
state, Decision ownership, Decision home, Invariant, Policy, Enforcement, Projection,
Presentation, Verification, Decision outcome, Recursive decision mapping.

## The pipeline

Each step is a question. The README frames the whole method as answering them in order.

| Step | Question |
|---|---|
| Requirement | What outcome must become true? |
| Decision | What questions must the system answer to make that outcome true? |
| Facts | What truths does each decision depend on? |
| Owner | Who alone has authority to answer each decision and own each fact? |
| Domain | What is the smallest boundary in which those decisions can be made from owned facts plus explicit inputs? |
| Invariant | What must never become false for the decision to remain correct? |
| Policy | Which policies derive the answer from authoritative facts, and how do they combine while preserving the invariant? |
| Enforcement | Where is the invariant actually prevented from being violated? |
| Projection + Presentation | How does everyone else learn the resolved answer without deciding it again? |
| Verification | How do we detect when actual behavior diverges from requirement, decision, or invariant? |

The compact form from the glossary:

```text
intent → business requirement → decision → outcome → behavior
                                  ↑
                    facts + invariants + policies
```

## Where the decision ends

The README draws a line worth preserving: the decision proper is **intent, decision, facts,
policy, outcome, invariants** — why we're deciding, what we're deciding, what we know, how we
decide, what answer we got, what must never become false. Everything after the outcome —
enforcement, projection, presentation — is system design *around* the decision, not part of its
reasoning.^[raw/articles/de-readme.md]

This matters practically: a ledger entry can be complete as reasoning while its enforcement is
still unbuilt. The two are separately reviewable.

The [current schema](../../skills/decision-engineering/assets/decision-ledger/SCHEMA.md) permits multiple policies within one
decision. In the handoff example, task eligibility, work preservation, and assignee readiness
policies must all pass to produce one readiness fact. Several policies do not imply several
output facts.^[../skills/decision-engineering/assets/decision-ledger/SCHEMA.md]

## Finding the decisions: recursive decision mapping

Start from a requirement and keep asking what must be decided or known for it to hold:

```text
Users can hand off a task
→ Which application receives it?
→ What is the assigned application?
→ Who chooses that assignment?
→ When may it change?
→ What happens if the application is unavailable?
```

Stop when decisions, facts, policies, and owners are explicit enough to implement and verify.
This is the primary tool for surfacing hidden decisions — see [[decision-entropy]].

## Distinctions that keep collapsing

The glossary's own "distinctions at a glance" table exists because these pairs get conflated.
The four worth memorizing:

- **Decision vs. policy** — what must be resolved vs. how it is resolved
- **Policy vs. enforcement** — defines valid behavior vs. makes invalid behavior impossible
- **Enforcement vs. verification** — prevents vs. checks and provides evidence
- **Ownership vs. home** — who is responsible vs. where that responsibility lives

## Open questions

- The README's pipeline places Owner before Domain; [[domain-boundaries]] derives domains from
  decision dependencies, which implies ownership might follow from the boundary rather than
  precede it. The ordering is unresolved across the two sources.
- "Who alone has authority" reads as a person, but the glossary is explicit that owners are
  usually modules, services, policies, or fields. The README's phrasing invites the wrong reading.

## Related

[[decision-engineering]] · [[decision-ledger]] · [[domain-boundaries]] · [[authority-and-projection]]
