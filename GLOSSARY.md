# Decision Engineering Glossary

This glossary defines the terms used by Decision Engineering. It exists to stop one idea from picking up several names, and to stop one name from picking up several meanings.

Terms are listed in alphabetical order.

## How the terms fit together

An **intent** becomes a **business requirement**. To satisfy that requirement, the system must resolve one or more **decisions**. It resolves them from **authoritative facts**, using **policies**, without breaking its **invariants**. Every decision has an **owner** and a **home**.

The **decision outcome** is what the system then does. Other parts of the system may see that outcome through **projections** or **presentations**. **Enforcement** stops invalid behavior. **Verification** shows evidence that the system behaves as intended.

```text
intent → business requirement → decision → outcome → behavior
                                  ↑
                    facts + invariants + policy
```

## Activation policy

The rule that decides whether a capability is allowed to run in a given situation.

For an agent skill, the skill's description is a projection of its activation policy: it tells the agent when the skill applies.

## Activation verification

Evidence that a capability runs when its activation policy says it should, and stays quiet when it should not.

This is not the same as **behavior verification**, which checks what the capability does once it has started.

## Agent skill

A packaged capability that an AI agent can invoke, usually defined by a `SKILL.md` file plus any scripts, references, and configuration it needs.

A skill is a useful running example throughout this glossary because it has all the parts: an activation policy (when it runs), a behavior (what it does), and an authoritative design it is derived from.

## Authoritative fact

A fact that a decision is allowed to treat as true.

For example, if `task.assignedApplication` decides where a task is handed off, that field is an authoritative fact for the handoff decision. The decision should not work out the same answer separately from other places that happen to hold similar data.

## Authoritative state

An authoritative fact that can change over time. For example:

```text
task.status = "ready_for_review"
task.assignedApplication = "claude"
```

State is a kind of fact, not a separate part of the decision model.

## Authority

The right to say what is true, or what should happen. When two representations disagree, the authoritative one wins.

Being used in many places does not make something authoritative. A cached value, a UI label, or a copied rule can have many consumers and still have no authority.

The thing that holds authority over one particular meaning is commonly called its *source of truth*. Information can be copied for different consumers, but authority over a meaning should sit in one place.

## Behavior verification

Evidence that a capability produces the intended result once it runs.

Behavior verification checks what happened after activation. **Activation verification** checks whether the capability ran in the right situations.

## Business requirement

A precise statement of what the system must accomplish for an intent to be satisfied.

The intent "let users hand off tasks" might become this requirement: "When a user invokes Hand Off, the task is sent to its assigned AI application." The requirement says what must be true. It does not say how to build it.

## Cost of Next Change (CNC)

The effort needed to make the next change safely. It covers finding the relevant knowledge, deciding what to change, making the change, and checking the result.

CNC is a practical signal of decision entropy. When ownership is scattered or unclear, searching and checking both get more expensive.

## Decision

A question whose answer determines system behavior or state.

Examples: "Which application receives this task?" "Is handoff allowed?" "What happens if the assigned application is unavailable?"

A decision does not mean a person chooses something at runtime. Software usually resolves it automatically.

## Decision architecture

The structure of decisions, dependencies, ownership, policies, enforcement, and projections in a system.

**Decision Engineering** is the practice. Decision architecture is the structure that practice produces.

## Decision Engineering

The practice of making the decisions that govern a system explicit, owned, traceable, enforceable, and verifiable.

Its goal is to reduce surprise: the gap between what people expect the system to do and what it actually does.

## Decision entropy

The build-up of decision knowledge that is implicit, duplicated, stale, or scattered. As decision entropy rises, behavior gets harder to predict and changes get harder to make safely.

This is an engineering metaphor. It is not a claim about thermodynamic entropy.

## Decision home

The one authoritative place where a decision is defined or resolved. Other parts of the system may use the outcome, but they should not redefine it.

A home is a conceptual boundary, not necessarily a single file. It can be a module, a service, a policy, a document section, or a database field.

**Decision ownership** names who is responsible. Decision home names where that responsibility lives.

## Decision ledger

The authoritative description of the decisions that govern a system, and of the relationships around them.

A ledger records the business requirement, the invariants, and the decisions. For each decision, it records the facts and constraints involved, the policy that resolves it, its owner, its consumers, and how it is verified. The ledger describes what the implementation must mean. It is not the implementation.

For an agent skill, the ledger is the authoritative design and `SKILL.md` is an executable projection of it.

## Decision locality

How close the knowledge needed to understand or change a decision sits to its authoritative owner.

High locality does not mean cramming all related code into one file. It means keeping authority over one meaning in one conceptual place.

## Decision outcome

The resolved answer to a decision.

For the decision "Which application receives this task?", the outcome might be `"claude"`. A **presentation** of that outcome might read "Claude Desktop." The outcome is the answer itself, not the way it is displayed.

## Decision ownership

Responsibility for authoritatively resolving a decision. The owner is usually a module, service, policy, document section, or data field rather than a person.

Ownership only works when the owner actually has authority and the system backs it up. When other parts of the system can go around the owner, that is **weak ownership**.

## Duplicated decision

One decision that is independently resolved in more than one place.

For example: the UI allows approval when a task is complete, while the backend allows it only when the task is complete *and* the user has permission. The system now holds two definitions of the same decision. They can drift apart even if they agree today.

## Enforcement

A mechanism that blocks or rejects behavior that would break a policy or an invariant. Database constraints, type constraints, authorization checks, runtime guards, and API validation all count.

A policy says what valid behavior is. Enforcement makes invalid behavior impossible, or makes it fail loudly.

## Hidden coupling

A dependency that exists because one part of the system quietly relies on another part's decisions, assumptions, or state.

Hidden coupling is usually a symptom rather than a cause. Look underneath it for hidden decisions, duplicated decisions, scattered responsibility, or unclear authoritative facts.

## Hidden decision

A decision that affects behavior but has never been identified or given an owner.

For example, "send the task to its assigned application" quietly assumes an answer to "what determines which application is assigned?" If that question has no home, some implementation will eventually answer it by accident.

## Intent

The human goal or desired change that caused a system to exist or change. Intent explains why the work matters, but it is usually too vague to build from directly.

Decision Engineering turns intent into a business requirement precise enough to engineer.

## Invariant

A condition that must stay true for the system to be valid. For example: "A task has at most one assigned AI application." "A task may be handed off only to its assigned application."

A requirement says what the system must accomplish. An invariant says what the system must never violate along the way.

## Policy

A rule for resolving a decision from authoritative facts, while respecting the invariants that apply.

```text
facts + invariants → policy → decision outcome
```

The decision says what must be resolved. The policy says how to resolve it.

## Presentation

The human-facing version of resolved state or a decision outcome. The state `task.status = "ready_for_review"` might be presented as "Ready for review."

A presentation is a projection aimed at people. It stays derived from an authority. It does not become a second source of truth.

## Projection

A representation derived from authoritative information for the benefit of some consumer. API responses, search indexes, configuration files, and executable skills can all be projections.

Copying is fine in a projection. Independent authority is not. A projection must stay traceable to its source, and must never quietly become a second owner of the same meaning.

## Recursive decision mapping

A method for finding hidden decisions. Start from a requirement and keep asking what must be decided or known for it to hold:

```text
Users can hand off a task
→ Which application receives it?
→ What is the assigned application?
→ Who chooses that assignment?
→ When may it change?
→ What happens if the application is unavailable?
```

Stop when the decisions, facts, policies, and owners are explicit enough to implement and verify.

## Scattered responsibility

A situation where the knowledge needed for one conceptual responsibility is spread across several places with no clear owner.

Several files can legitimately take part in one decision. Responsibility is scattered when each file holds an independent piece of the rule and no single place determines the answer.

## Stale projection

A projection that no longer matches its authoritative source. For example, if a decision ledger changes but the `SKILL.md` derived from it does not, the skill is stale.

Traceability and verification are what keep projections from going stale unnoticed.

## Surprise

The gap between expected and observed system behavior. Bugs are one kind of surprise, but so are inconsistent UI, unexpected agent behavior, components that disagree with each other, and changes that break something apparently unrelated.

This is why "minimize surprise" is a broader goal than "minimize bugs."

## Traceability

The ability to follow observed behavior back through its implementation and its governing decisions to the requirement and intent that justify it.

```text
observed behavior
→ implementation
→ policy or invariant
→ decision and authoritative facts
→ business requirement
→ intent
```

Every rule that changes what the system does should have such a path. A rule that traces back to nothing is a **hidden decision** waiting to be found.

## Trigger

A condition that makes a capability eligible to run.

A user clicking Hand Off is a trigger. So is a task entering `ready_for_review`. A trigger is only an input: the **activation policy** takes the trigger and decides whether the capability actually runs.

## Verification

The process of gathering evidence that the implementation matches the intended decision architecture. Verification can check whether:

- a policy resolves to the intended outcome;
- enforcement rejects invalid behavior;
- a projection is still faithful to its source;
- a presentation communicates the correct state; or
- a business requirement holds end to end.

Verification detects whether the system behaves correctly. Unlike enforcement, it does not necessarily stop an invalid action in production.

## Weak ownership

A situation where a decision has a nominal home, but other parts of the system can bypass, redefine, or contradict it.

Ownership only counts when the owner has real authority and the system enforces it. A rule documented in one place and re-implemented in three others has weak ownership, whatever the documentation says.

## Distinctions at a glance

| Terms | Difference |
| --- | --- |
| Intent / Business requirement | Why the change matters / What the system must accomplish |
| Business requirement / Decision | Required outcome / Question that must be resolved |
| Decision / Decision outcome | Question / Resolved answer |
| Decision / Policy | What must be resolved / How it is resolved |
| Authoritative fact / Decision | What is accepted as true / What follows from those facts |
| Authoritative fact / Authoritative state | Any authoritative fact / One that changes over time |
| Policy / Enforcement | Defines valid behavior / Blocks or rejects invalid behavior |
| Enforcement / Verification | Prevents / Checks and provides evidence |
| Trigger / Activation policy | The condition that makes a capability eligible / The rule that decides whether it runs |
| Authority / Projection | Determines meaning / Derives a representation of that meaning |
| Projection / Presentation | Serves any consumer / Serves a human consumer |
| Decision ownership / Decision home | Who is responsible / Where that responsibility lives |
| Decision ownership / Weak ownership | Effective authority / Nominal authority others can bypass |
| Hidden decision / Hidden coupling | An unowned choice / A non-obvious dependency |
| Scattered responsibility / Duplicated decision | One rule spread out with no clear owner / One question answered independently more than once |
| Duplicated decision / Projection | Two independent authorities / One authority, many derived copies |
| Decision Engineering / Decision architecture | The practice / The structure the practice produces |
