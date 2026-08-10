# Create decision engineering skill

## Problem

We're all now prompting agents to do the work instead of us doing the work directly. To get the proper output from the agent, you have to give the right context prompt, and if you're messy with how you maintain whatever that is repeatedly used as a context prompt, such as your company docs, codes, or meeting notes, you end up wasting tokens and time.

This decision engineering framework tries to solve this from first principles. At the heart, it's about creating a concrete structure around abstract human intent, storing them so it can be used as a source of truth and context prompt, and update them as the requirement of the system changes so there is a single source of truth to check if the system has any bugs.

## Core philosophy

Decision engineering skills try to minimize the surprise in the system by finding a single home .

Let's say you asked an agent, “Write a launch email for our product.” You expected the agent to write an email that targets marketers but agent creates content targeting founders. This is a surprise.

To find out why the agent was confused, you dig into the agents thought process. It turns out there were multiple documents that mentions the target customer and in the latest meeting note, there was a discussion about whether the team should target the founders as a market wedge. Since this is the latest document, agent assumed the correct target customer is founder, but the team decided to stick with marketers as their target.

This surprise was created because there isn't one place that tells an agent "if you want to know who our target customer is, this is where you should look". So the fix to this problem is to assign a single authoritative place for defining the current target customer.

This is the heart of the decision engineering skill. It tries to find a single home for all the parts that goes into making the right decision.

## Process

User provides intent (requirement) → Intent is turned into decision ledger → Decision ledger is used to create a plan → Implement →
