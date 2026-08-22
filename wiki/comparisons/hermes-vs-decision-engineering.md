---
title: Hermes and Decision Engineering
created: 2026-08-21
updated: 2026-08-21
type: comparison
tags: [comparison, agent-harness, context-engineering, decision, ledger, tooling]
sources: [raw/transcripts/discussing-decision-engineering-and-hermes-2026-08-21.md]
confidence: low
---

# Hermes and Decision Engineering

This page records the conversation's working architectural interpretation of Hermes Agent. It
has not yet been checked against Hermes documentation or usage evidence, so the architecture
and popularity claims remain hypotheses rather than established facts.

**Defined in glossary:** Agent skill, Decision Engineering, Decision ledger, Authoritative fact,
Projection, Traceability.

## Hermes as a prompt-assembly harness

The discussion describes Hermes as a loop around an LLM:

```text
user message
    ↓
load relevant memory + reusable skills
    ↓
assemble model context / prompt
    ↓
LLM ↔ tools
    ↓
respond, then possibly save memory or a new skill
```

Memory storage, skill loading, planning, and tools support the loop, but their selected outputs
eventually become text in the model context. In this framing, Hermes shares the usual
user → harness → LLM → tools skeleton; its emphasis is richer context assembly and write-back.

## Why it felt different

The conversation proposes three reasons Hermes became popular:

1. Persistent memory made the agent appear to know a project across sessions.
2. Reusable, self-improving skills made completed work feel cumulative: a successful procedure
   could become a how-to for next time.
3. Persistent-agent behavior—running jobs, using tools, and keeping sessions alive—felt more like
   an ongoing worker than a turn-by-turn chatbot.

These are product-behavior explanations, not claims of unique model capability. They need an
external source audit before being raised above `confidence: low`.

## Different organizing units

| Dimension | Hermes framing | Decision Engineering framing |
|---|---|---|
| Primary stored unit | Memory and skill | Decision and its typed relationships |
| Retrieval question | What memories and skills are relevant? | What decisions are required, and what do they depend on? |
| Compounding artifact | Reusable procedure or how-to | Durable record of reasoning and commitment |
| Context assembly | Selected memory and skills become prompt text | Decision dependencies select a minimal decision packet |
| When an input changes | Retrieve relevant context again | Traverse dependencies to identify what must be revisited |
| Main promise | Do a repeated task faster | Stay consistent and explain why behavior should follow |

The compact distinction is: **Hermes compounds procedures; [[decision-engineering]] compounds
decisions and reasoning.** A procedure records how to do something again. A durable decision
record preserves why an outcome was chosen, which facts were authoritative, what depends on it,
and what must be reconsidered when those facts change.

## Complement rather than replacement

The two approaches can coexist. A Hermes-like harness can provide the persistent execution loop,
tool use, memory, and skills, while [[decision-ledger]] supplies the authoritative decision graph
used to assemble task context. Skills would remain executable [[authority-and-projection|projections]]
of durable decisions rather than becoming competing authorities.

The product direction in [[productizing-decision-engineering]] therefore changes the organizing
unit beneath chat, not necessarily the entire agent loop: conversation produces decision deltas;
the ledger records commitments and dependencies; the graph determines which reasoning context a
later task requires.

## Open questions

- Does Hermes actually implement each described component this way, and which details vary by
  version or deployment?
- What evidence supports the proposed causes of its popularity?
- Can skill creation link back to the decisions that justify the skill's activation and behavior?
- What deterministic rules are needed for a decision graph to assemble better context than
  memory retrieval alone?

## Related

[[productizing-decision-engineering]] · [[decision-ledger]] · [[compiled-knowledge-base]] ·
[[schema-as-agent-constraint]]
