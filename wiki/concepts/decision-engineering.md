---
title: Decision Engineering
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [decision, methodology, surprise, ownership]
sources: [raw/articles/de-glossary.md, raw/articles/de-readme.md]
confidence: medium
contested: true
---

# Decision Engineering

Hub page. Definitions live in `GLOSSARY.md`; this page holds the shape of the framework and
where its parts connect.

**Defined in glossary:** Decision Engineering, Decision architecture, Surprise, Intent,
Business requirement, Decision.

## The thesis in one line

Make behavior-shaping decisions first-class architectural objects, so that every decision has
exactly one home and the system accumulates no hidden or competing sources of meaning.

The goal is stated as reducing **surprise** — the gap between expected and observed behavior.
This is deliberately broader than reducing bugs: inconsistent UI, unexpected agent behavior,
components that disagree, and changes that break something unrelated all count.

## The worked example that motivates it

An agent is asked to write a launch email for marketers and writes one for founders. Digging
into its reasoning: the strategy doc names marketers, a later meeting note discusses founders
as a possible wedge. The agent took the newer document as authoritative. The team had actually
stuck with marketers.

Nothing was a bug. The failure was that no single place answers "who is the target customer?",
so the agent had to adjudicate between two live sources and picked wrong. The fix is not better
prompting — it is assigning one authoritative home for that fact.^[raw/articles/de-readme.md]

This example is load-bearing because it shows the framework is not code-specific. The same
failure shape appears in company docs, meeting notes, investment strategy, and org design.

## Why now

The stated motivation: generating code has gotten easy, maintaining it has gotten hard. Because
we now prompt agents rather than working directly, whatever is repeatedly used as context — docs,
code, notes — becomes the real bottleneck. Messy context wastes tokens and produces wrong output.
See [[compiled-knowledge-base]] for the same argument made about knowledge bases.

## The parts

- [[anatomy-of-a-decision]] — the requirement-to-verification pipeline every decision passes through
- [[decision-ledger]] — the artifact that records it all
- [[domain-boundaries]] — how decisions group into domains
- [[decision-entropy]] — the failure modes when they don't
- [[authority-and-projection]] — how everyone else learns the answer without re-deciding it
- [[information-theoretic-foundation]] — why the author thinks this works at all

## Scope and maturity

Intended for any system involving human intention: codebases, agent harnesses, company
documents, investment strategy, org structure. The author is explicit that this is a first
version, untested across domains, with the software development lifecycle as the easiest place
to try it. Comparisons to domain-driven design and spec-driven development are invited but not
yet made.^[raw/articles/de-readme.md]

Treat claims here as a working hypothesis, not established practice. This is why most pages in
this wiki carry `confidence: medium`.

## Source tensions

`README.md` and `GLOSSARY.md` disagree, and the README is the older, rougher document. Per the
update policy the glossary wins; recorded here so the conflict isn't silently resolved.

| Term | README stub | GLOSSARY.md (authoritative) |
|---|---|---|
| Decision | "Steps system takes to remove the uncertainties" | "A question whose answer determines system behavior or state" |
| Intent | "The goal user wants to achieve with the system" | "The human goal or desired change that caused a system to exist or change" |

The Decision conflict is substantive, not cosmetic: steps are procedure, a question is an
object with an owner and a home. The whole framework depends on the second reading.

Additional README defects worth fixing at the source: the inline Glossary section duplicates
`GLOSSARY.md` (a duplicated decision about definitions — the exact failure the framework names),
"Why should you care" appears twice, "Entire process of decision engineering" is an unfinished
two-item stub, and "repair radius" is used but never defined — see [[domain-boundaries]].

## Open questions

- How does this compare to DDD's bounded contexts and to spec-driven development? The README
  asks the question and does not answer it — this is the most obvious gap to fill next.
- Where does the approach fail? No failure cases are documented anywhere in the sources.
- The README's stated "what good looks like" includes "reader understands the benefit in
  5 minutes." Nothing in the sources tests that.

## Related

[[anatomy-of-a-decision]] · [[decision-ledger]] · [[decision-entropy]] · [[domain-boundaries]]
