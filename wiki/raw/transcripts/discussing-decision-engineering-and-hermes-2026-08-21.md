---
source_url: chatgpt-conversation://6a877fca-d888-83ee-b0d3-3e3b48bd591d
ingested: 2026-08-21
sha256: c830b8469a562c605c4ace9248973143246f390d712412a29df516ba047191a7
---

# Discussing Decision Engineering and Hermes

Selected relevant turns from the ChatGPT conversation titled “Discussing Earnings.” False starts and unrelated earnings-season turns are omitted; wording below is preserved from the conversation.

## Productizing Decision Engineering

**User:** Okay Um We had created this into a skill now now I want to figure out how we can productize this so anyone can use it without friction

**Assistant:** Hmm. I'd start by confronting the biggest risk. People won't learn decision engineering just to use a tool. So the product has to capture decisions as a byproduct, not a form that people fill in. So, layer one is passive capture, watching conversations, code or docs, and quietly extracting decision artifacts. Layer two is verification. What facts are authoritative? What changed? What does that break? And then layer three is guidance, showing Hey, you've made this decision before. Here are the inputs you need. The aha moment isn't “I have a decision graph”, it's “I changed one requirement and instantly saw the seven decisions I need to revisit.” That, I think, feels like magic. And the chat is just the interface, not the product.

**User:** Okay, I think I'm getting an idea. So, the MVP should be a chat and. As user chats with the agent it. I- on background. it's Agent captures any kind of decision that was Uh. made during the conversation It would update The decision ledger

**Assistant:** Exactly.

**User:** Uh, if user hasn't Uh responded for a while then Um, let's say for about 10 minutes. Agent would uh or There will be a back in-in the It will trigger Um. It would trigger something that would uh- uh scan the chat session. So, th- the Chat log And it would pick out all the decisions that were made. And record it in the ledger

**Assistant:** Yeah, that's a solid MVP, I think, because it's zero behavior change. The user just chats. I'd tweak it slightly. Don't think of it as scanning the whole conversation after ten minutes. Make it event-based. 10 minutes of idle, end of a thread, manual “new topic”. Then the background agent extracts only the delta, compares it against existing decisions, and updates the ledger and the log. That way the chat stays fast while the structure builds quietly and automatically. And crucially, you don't have to extract everything. Just capture moments where the user actually committed to something. Then occasionally summarize back, “Here's what I recorded. Anything to edit?”. That keeps the loop lightweight, but still builds that reliable decision base you want.

## Hermes architecture

**User:** Okay, I like this Um and before- O-okay, now I wanna kinda switch the gear and I want to understand the architecture of two products Um And I guess we could start with Uh Hermes, since we've been talking about it uh explain the architecture of Hermes

**Assistant:** Checking. Here's the basic shape. Think of a conversation loop at the center. User message comes in, it pulls in memories and skills, builds a prompt, calls the LLM, runs any tools, then maybe writes back new memories or skills. Underneath that you have a memory store, a skill loader, and a planner, and everything eventually becomes text in the model context. Your architecture breaks that pattern. Instead of memories feeding prompts, you're proposing a decision ledger and graph that sits between chat and model. Chat drives extraction, which updates the decision graph, which then deterministically assembles the minimal context for the model. That gives you a clear separation: chat UX on top, decision infrastructure beneath. So, Hermes is memory/skill centric, and yours is decision centric. That's the core architectural divergence.

**User:** Okay Um, a- a- ca- can you slow down? Uh, you went too fast and Uh yeah, is hard to hard to understand

**Assistant:** Right. Let me take it slower. Hermes is built around a loop. Message comes in, it pulls some memories and skills, calls the model, maybe uses a tool, and sometimes saves new memories or skills. The center of gravity is prompt assembly. Your structure is different. Chat still happens, but underneath, you extract decisions into a ledger, connect them into a graph, and then build the model's context from that. So, the model gets exactly what it needs.

**User:** Okay Okay, so Sounds like the way you describe it Hermes, Uh- See if I understood this correctly. So it runs on a loop So u- user prompts it, and then Hermes Uh looks at the skill- available skills and context from the memory and then It assembles a prompt. So it's a system prompt and submits that system prompt to a model. Is that correct

**Assistant:** Yep, that's right. The key point is

**User:** But go- go ahead

**Assistant:** Right. The key point is it treats memories and skills as text. It's all about what gets stuffed into the context window.

**User:** Okay, how is that different from other harnesses

**Assistant:** Checking. Honestly, not that different. Most harnesses have that same basic skeleton, user to harness to LLM to tools. The difference is just how much context work the harness does. Some do almost none, Hermes does a lot with memories and skills. Yours changes the organizing unit. Instead of “what memories are relevant”, it's “what decisions are required”. That's subtle, but it is a different retrieval philosophy.

## Why Hermes became popular and what compounds

**User:** R-right, but Um What I'm asking is uh, why did Hermes become popular? What made it There must be something unique about Hermes that people are are Uh you know, finding useful compared to others

**Assistant:** I think it's a few things, and none of them are actually model magic. First, persistent memory. It felt like the agent actually knew your project over time, not just in a single session. Second, that self-improving loop. After a task, it tries to create a skill so next time it's easier. That gave people the sense that effort compounds. And third, it leaned into the idea of a persistent agent instead of a chatbot. It runs jobs, uses tools, keeps sessions alive. But underneath, it's still compounding skills, not compounding decisions. One-liner difference is Hermes compounds procedures; Decision engineering compounds reasoning.

**User:** When you say it compounds decisions, you mean like a- compounds or it- or procedure, it compounds the skill. That's what you mean by it

**Assistant:** Yeah. In Hermes, when it completes a task, it tries to save a reusable how-to. That's a skill. Next time, it loads that and goes faster. That's compounding procedures.

What you're talking about, compounding decisions, is keeping a durable record of why something was chosen, what facts supported it, and what other decisions depend on it. So when a fact changes, you know exactly what to revisit. Skills help you do; decision ledger helps you stay consistent and explain why you're doing it.
