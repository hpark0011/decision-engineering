---
title: John von Neumann
created: 2026-08-20
updated: 2026-08-20
type: entity
tags: [person, information-theory, error-correction]
sources: [raw/papers/von-neumann-probabilistic-logics-1956.md]
confidence: medium
---

# John von Neumann

This page records von Neumann's relevance to decision engineering, not a general biography.

## Source in this wiki

*Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components* is
based on five Caltech lectures delivered in January 1952, recorded by R. S. Pierce, and
published in *Automata Studies* in 1956. The ingested Stanford edition was reconstructed in
2010 from the original Caltech version and notes known errors in later published figures.

## Contribution relevant here

Von Neumann treats component error as part of automata design rather than an external accident.
His central architectural move is to combine redundancy with explicit restoring operations, so
that degradation introduced by useful work is repeatedly pushed back toward a stable logical
state. See [[information-theoretic-foundation]] for the mechanisms and bounds.

The result sharpens the decision-engineering question: identifying a home for a decision may
localize error, but reliability also requires a mechanism that detects and repairs drift. That
connects the paper to [[authority-and-projection]] and [[decision-entropy]].

## Precision and limits

- The paper studies probabilistic automata and neural-style logical networks, not specifically
  cellular automata.
- Its numerical thresholds are specific to its component models and statistical assumptions.
- It explicitly acknowledges that independent, constant component-error probabilities are
  unrealistic and leaves correlated, history-dependent, and time-varying errors untreated.
- Its multiplex construction achieves strong reliability at enormous redundancy cost; it is an
  existence and architecture result, not a practical recipe for this project.

## Related

[[information-theoretic-foundation]] · [[domain-boundaries]] · [[authority-and-projection]] ·
[[decision-entropy]]
