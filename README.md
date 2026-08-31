# Decision Engineering

Decision Engineering is an installable agent skill for keeping behavior-shaping decisions explicit, authoritative, enforceable, traceable, and correctable.

## Installation

Choose one installation method. If you use multiple method, you would have multiple copies of skills.

### 1. Claude Code managed plugin

```bash
claude plugin marketplace add hpark0011/decision-engineering --scope user
claude plugin install decision-engineering@decision-engineering --scope user
```

### 2. Codex managed plugin

```bash
codex plugin marketplace add hpark0011/decision-engineering
codex plugin add decision-engineering@decision-engineering
```

### 3. Cursor Agent Plugin

The repository root follows Agent Plugins 1.0, which Cursor loads directly. Import `hpark0011/decision-engineering` into a Cursor team marketplace, then install Decision Engineering at user scope from Customize. For local validation before a marketplace listing, clone the repository into `~/.cursor/plugins/local/decision-engineering` and restart Cursor.

### 4. Editable skill with [skills.sh](http://skills.sh)

[skills.sh](https://skills.sh) is a tool for adding agent skills to your project. It copies the skill files into your project so you can review and customize them.

```bash
npx skills@latest add hpark0011/decision-engineering
```

## First use

Ask the agent to route a requirement, feature, architecture change, policy, or bug through Decision Engineering. The skill reuses an existing conforming ledger or automatically creates `./decision-ledger` at the nearest Git root, falling back to the active workspace root. A user- or project-instruction override is accepted only when it stays inside that project root.

## Update and uninstall

Update managed plugins through the host marketplace. For Codex, upgrade the marketplace and run `codex plugin add decision-engineering@decision-engineering` again. For an editable copy, run `npx skills update decision-engineering --project`. Uninstalling or updating the skill must never delete or rewrite the project's `decision-ledger`.

## Package development

`package/metadata.json` is the implementation source for generated distribution metadata. After changing it, run `python scripts/generate_manifests.py`, then `python scripts/validate_package.py`. The validation matrix runs on macOS, Linux, and Windows.

Version 0.1.0 becomes releasable when package acceptance passes. Version 1.0.0 additionally requires at least 20 matched tasks showing at least 25% fewer requirement-to-code divergences without worse initial correctness.

Report reproducible defects in GitHub Issues. Use GitHub Discussions for questions and field reports.

## What is it?

Decision Engineering makes behavior-shaping decisions first-class architectural objects. It gives every decision explicit inputs, constraints, policy, ownership, consumers, and verification so systems can evolve without accumulating hidden or competing sources of meaning.

The whole point of decision engineering is finding single home for each decision so there is no hidden couplings.

## Who is it for?

Decision engineering is intended to be applied to any kind of system that involves human intention — codebase, agent harness, company documents, investment strategy, and even when designing org structure.

However, this is my first version and I haven't had a chance to test this concept across different domains. The easiest place to test this concept is by applying it to the software development life cycle.

If you're familiar with domain driven design or if you've been doing spec driven development, and tried this decision engineering approach, I would love to hear your thoughts on how decision engineering approach compares — What's working well and where does this fail?

## Why should you care

As generating the code gets easier, maintaining the codebase is getting harder.

## Why should you care

We're all now prompting agents to do the work instead of us doing the work directly. To get the proper output from the agent, you have to give the right context prompt, and if you're messy with how you maintain whatever that is repeatedly used as a context prompt, such as your company docs, codes, or meeting notes, you end up wasting tokens and time.

This decision engineering skill tries to solve this from first principles. At the heart, it's about creating a concrete structure around abstract human intent, storing them so it can be used as a source of truth and context prompt, and update them as the requirement of the system changes so there is a single source of truth to check if the system has any bugs.

## When to use

Decision Engineering applies anywhere you are designing a system that must repeatedly turn inputs into reliable decisions. It can be applied for maintaining the codebase, creating agent skills, organizing the internal docs, or managing a team.

## Core philosophy

Decision engineering tries to make surprise local so the system detects the surprise and self corrects.

Let's say you asked an agent to write a launch email for the product that team has built. You expected the agent to write an email that targets marketers but agent creates content targeting founders. This is a surprise.

To find out why the agent was confused, you dig into the agents thought process. It turns out there were multiple documents that mentions who the target customer is. One in the strategy doc and one in the latest meeting note. In the meeting note, there was a discussion about whether the team should target the founders as a market wedge. Since this is the latest document, agent assumed the correct target customer is founder, but the team decided to stick with marketers as their market wedge.

This surprise was created because there isn't one place that tells an agent "if you want to know who our target customer is, this is where you should look". So the fix to this problem is to assign a single authoritative place for defining the current target customer.

This is the heart of the decision engineering skill. It tries to find a single home for all the parts that goes into making the right decision.

## Process

Decision Engineering makes behavior-shaping decisions first-class architectural objects. It gives every decision explicit facts, constraints, policy, ownership, consumers, and verification so systems can evolve without accumulating hidden or competing sources of meaning.

**Requirement**\
What outcome must become true?

↓

**Decision**\
What questions must the system answer to make that outcome true?

↓

**Facts**\
What truths does each decision depend on?

↓

**Owner**\
Who alone has authority to answer each decision and own each fact?

↓

**Domain**\
What is the smallest boundary in which those owned decisions can be made using owned facts plus explicit inputs from other domains?

↓

**Invariant**\
What must never become false for the decision to remain correct?

↓

**Policy**\
How is the decision derived from the authoritative facts while preserving the invariant?

↓

**Enforcement**\
Where is the invariant actually prevented from being violated?

↓

**Projection + Presentation**\
How does everyone else learn the resolved answer without deciding it again?

↓

**Verification**\
How do we detect when actual behavior diverges from the requirement, decision, or invariant?

## Deeper idea

Decision engineering was born from the thought "can I measure agent's level of understanding of the codebase?".

My idea for this question was this. If agent can predict how much token it would cost to meet the user's requirement, it means the agent has full understanding of the codebase. In other words, I would have agent predict the token cost during the planning phase, and measure the delta of the prediction and real token usage after agent has implemented the plan. The delta would be the surprise that agent didn't expect to account when it was making the prediction and if I fix what caused the delta, it means that agent has a full understanding of the system and it's able to predict how much token it would cost to make a change in the system.

So I created a skill and tested this but in practice, there were too many variables that agent had to account to make the right prediction. Each model, thinking level, would impact the token cost and when I asked agent what caused the prediction delta and agent gave me the reason, many of the reasons were hard to verify.

However, digging into this idea brought me to the information theory and other ideas that is built on top of the information theory.

The core insight of Claude Shannon's information theory, John von Neumann's cellular automata, and threshold theorem is: You can build reliable system from unreliable parts if the system has enough error-correcting capacity to remove errors faster than they accumulate.

Decision engineering adopts this insight as well. Agents work probabilistically so they are unreliable. If the parts of the systems can self correct when agent makes an error, we can still create an reliable system.

## Defining domain

Decision engineering is about making unreliable things work reliably. Naturally, agents like humans or quantum state is unreliable.

The key to making unreliable things work reliably is by localizing the error.

For example, main reason the vibe coding fails in the large codebase is because as you add more features or fix bugs, agent tends to solve problems by adding more rules. This naturally creates a lot of hidden couplings and scattered decisions and as the hidden couplings and scattered decisions increase, the system becomes unreliable.

The objective of domain is followings:

- Define a decision boundary so there is less randomness in surprises.
- If surprises has less randomness, it can be fixed, and we can prevent error being accumulated.

<https://www.researchgate.net/publication/291956995_Unreliable_Systems_Built_from_Reliable_Parts>

<https://web.stanford.edu/class/cs379c/class_messages_listing/curriculum/Biographical_Personal/figures/John_von_Neumann1956probabilistic_logics.pdf?utm_source=chatgpt.com>

So how would we define the threshold and what we be the above threshold and below threshold in decision engineering?

The whole point of decision engineering is finding single home for each decision so there is no hidden couplings.

- Requirement: Define domain in a way that minimizes surprise.
- Decision: Do these decisions belong in the same domain?
- Policy: Group decisions together if they consistently depend on the same authoritative facts, preserve the same invariants, and follow the same policies
- Depends on: The facts you collect are "what each decision needs, which policies apply, and which other decisions change when it changes".
- Invariant: Each decision belongs to one primary domain, and within that domain the decisions share the same core facts and must preserve the same invariants

&nbsp;

First, list the key decisions your system has to make. For each decision, write down the few facts you truly need to make it, and the rule you're applying. Then group together the decisions that use the same small set of facts and rules. Each group is a domain. Check your work by asking, when one decision changes, do most of the changes stay inside that group? If yes, your domain boundary is probably sound. That's a repeatable step-by-step process. List decisions, list needed facts and rules, group by overlap, then double check with the change test.

&nbsp;

Anatomy of decision is intent, decision, facts, policy, outcome, and invariants. Everything after the outcome, like presentation or enforcement, is system design around the decision, not the decision's reasoning.

Why we're deciding, what we're deciding, what we know, how we decide, what answer we got, and what must never become false. If decision engineering is about anything, it's about making each of those explicit.

&nbsp;

Information theory asks:

> Given a state at the source, can the receiver recover the intended state despite noise?

Decision engineering asks almost the same structural question:

> Given human intent at the source, can the system reliably recover the intended decision at the point where something must happen?

&nbsp;

domain boundaries emerge from decision dependencies, not from nouns or organizational categories.

Put decisions in the same domain when they must stay consistent with the same authoritative facts, meanings, and invariants. Separate them when they can change independently with only narrow, explicit dependencies.

A domain is a boundary within which the information needed to make its decisions is locally recoverable.

The way we track this is repair radius.

## What good looks like

- Documentation
  - Reader should be able to understand the benefit and how to apply the decision engineering within 5 minutes.
- Skill
  - It should be easy to read.
- Outcome of the skill
  - Decision ledger
    - It has to be compact and simple.
    - It should be a table.
    - The dependencies(what it depends on, where it's used, who owns it) should be explicitly written and with these dependencies, it should be able to create a dependency graph.

## Entire process of decision engineering

1. Understand user's intent.
2. 

## Glossary

- Intent: The goal user wants to achieve with the system.
- Decision: Steps system takes to remove the uncertainties.
- 

&nbsp;

The topology of the domain should be derived from the decisions.