# Decision Engineering

Decision Engineering is the discipline of building reliable decision systems out of unreliable decision-makers.

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

## Problem

Humans forget things, misunderstand context, make inconsistent judgments, and change their minds. Agents hallucinate, lose context, reason differently across runs, and confidently produce incorrect outputs.

So how do we build a reliable system that includes agents and humans?

First, let's think about what a "system" is.

A system is a collection of decisions put together to serve a larger goal.

Think of a restaurant. Its goal is to make profit by serving food people want to come back for. To do that, the owner, manager, chefs, and waiters all make decisions in their own part of the restaurant: what goes on the menu, who to hire, how much food to order, how to cook a dish, or how to deal with an unhappy customer.

If those decisions work well together, day after day, the restaurant is running on a reliable system and be able to consistently make profit by satisfying the customer.

But even a great chef who has worked there for ten years will eventually make a bad call. They might hire the wrong person, put a dish on the menu that nobody wants, or order too much food.

You can't demand every human or agent to be perfectly reliable.

The trick to building a reliable system out of unreliable parts isn't making sure nobody ever gets things wrong.

It's making sure the system can catch the mistake, contain the damage so the mistake doesn't propagate to other parts of the system, locate where the mistake was made, and recover from it.

## Solution

Decision Engineering makes decisions first-class architectural objects and gets used as a source of truth for intent of the system design.

It solves two problems that makes system unreliable.

1. Decisions made with implicit assumptions creates inconsistency or disagreement
2. Unable to pin point the single cause of error

It has two philosophies.

1. Break down every decision into a concrete structure and minimize judgements made with implicit assumptions.
2. Every decision should only output one fact. If decision creates more than one fact, the system is vulnerable for having scattered responsibilities or hidden couplings down the line.

The first step is to make important decisions explicit.

Instead of letting a decision live in someone's head, a chat thread, or buried inside a document, we write down what was decided, what facts it depended on, and what part of the system it controls.

Then we give that decision a clear boundary.

A pricing decision should decide the price. It shouldn't also quietly change the website, the sales forecast, and the marketing plan. Those parts of the system can use the price, but they should make their own decisions.

This matters because when something goes wrong, we want to know where the problem came from.

If sales drop because the price was wrong, we should be able to trace that back to the pricing decision, see what assumptions it was based on, fix it, and then update the parts of the system that depend on it.

We build a system where each decision has a clear job, its assumptions are visible, its effects are limited, and its output can be checked.

That way, when someone gets something wrong, the mistake doesn't have to bring the whole system down.

**Decision Engineering makes unreliable judgment safe to compose.**

## How does it work?

Read @decision-engineering/IDEA.md to learn how Decision Engineering works.

## Why this works

Most systems have a source of truth for facts and state. They can tell you that the price is $49, that we're targeting small businesses, that a feature is disabled, or that the launch date is October 10. But they usually don't have a source of truth for **why** those things are true.

That becomes a problem as soon as someone needs to make a change. Imagine an agent sees that the price is $49 and is asked to improve conversion. Why is the price $49? Maybe that's the minimum price we need to hit our margin target. Maybe we tested $39 and it performed worse. Maybe an important customer has a contract tied to that price. Or maybe $49 was just a guess we made six months ago.

The current state doesn't tell you, so the agent has to reconstruct the reason from whatever context it can find. Another agent may reconstruct it differently. Over time, this is how a system becomes inconsistent: each person or agent makes a reasonable decision, but they're making those decisions from different interpretations of why the system looks the way it does.

Decision Engineering gives the system a shared source of truth for that intent. Instead of a pile of disconnected facts:

`Facts → Facts → Facts`

you get a causal chain:

`Goal → Requirement → Facts → Decision → New Fact`

The system can now trace a fact back to the decision that created it, and trace that decision back to the facts, requirements, and goals behind it.

So instead of storing only:

**The price is $49.**

we also know:

**We chose $49 because CAC is $35 and we want to recover acquisition cost within two months.**

Now an agent doesn't have to reverse-engineer why the price is $49. It can look it up. More importantly, when something changes, the system can understand what that change affects. If CAC goes from $35 to $70, it can see that one of the reasons behind the $49 price is no longer true and point back to the pricing decision that needs to be revisited.

Without a source of truth for intent, every change starts with guessing why the system was built the way it was. With one, humans and agents can make changes from the same reasoning.

**State tells you what the system is. Intent tells you why it is that way.**

## Limitation

1\) Decision Engineering doesn't tell you what the right decision is.

A decision can be perfectly documented, clearly separated, and easy to verify, and still be wrong because the facts were wrong or the judgment was bad.

2\) Writing down every small decision would make the system slower and harder to use.

The challenge is deciding which decisions are important enough to make explicit and which ones can stay informal.

We could use the decision engineering framework to make this explicit so there isn't disagreeing judgement.

**A decision must be made explicit when its result becomes an input to another decision or another part of the system.**

```
Does another decision depend on this output?

No  → keep it local
Yes → make it explicit
```

3\) Decision Engineering can't completely remove uncertainty.

Sometimes there simply isn't enough information to know what the right answer is. In decision engineering, this is called irreducible uncertainties. In those cases, the system can make the uncertainty visible, keep the decision easy to change, and limit the damage if the decision turns out to be wrong.

So Decision Engineering does not make a system infallible.

**It makes failure easier to point, easier to understand, and easier to recover from.**

## First use

Ask the agent to route a requirement, feature, architecture change, policy, or bug through Decision Engineering. The skill reuses an existing conforming ledger or automatically creates `./decision-ledger` at the nearest Git root, falling back to the active workspace root. A user- or project-instruction override is accepted only when it stays inside that project root.

## Who is it for?

Decision engineering is intended to be applied to any kind of system that involves human intention — codebase, agent harness, company documents, investment strategy, and even when designing org structure.

However, this is my first version and I haven't had a chance to test this concept across different domains. The easiest place to test this concept is by applying it to the software development life cycle.

If you're familiar with domain driven design or if you've been doing spec driven development, and tried this decision engineering approach, I would love to hear your thoughts on how decision engineering approach compares — What's working well and where does this fail?

## How I got here

Decision engineering was born from the thought "can I measure agent's level of understanding of the codebase?".

My idea for this question was this. If agent can predict how much token it would cost to meet the user's requirement, it means the agent has full understanding of the codebase. In other words, I would have agent predict the token cost during the planning phase, and measure the delta of the prediction and real token usage after agent has implemented the plan. The delta would be the surprise that agent didn't expect to account when it was making the prediction and if I fix what caused the delta, it means that agent has a full understanding of the system and it's able to predict how much token it would cost to make a change in the system.

So I created a skill and tested this but in practice, there were too many variables that agent had to account to make the right prediction. Each model, thinking level, would impact the token cost and when I asked agent what caused the prediction delta and agent gave me the reason, many of the reasons were hard to verify.

However, digging into this idea brought me to the information theory and other ideas that is built on top of the information theory.

The core insight of Claude Shannon's information theory, John von Neumann's cellular automata, and threshold theorem is: You can build reliable system from unreliable parts if the system has enough error-correcting capacity to remove errors faster than they accumulate.

Decision engineering adopts this insight as well. Agents work probabilistically so they are unreliable. If the parts of the systems can self correct when agent makes an error, we can still create an reliable system.

## 