---
name: decision-engineering
description: Run Decision Engineering by locating, creating, changing, validating, and tracing a Markdown decision ledger whose decisions remain explicit, authoritative, enforceable, traceable, and correctable. Use when a requirement, feature, architecture change, bug, policy, or implementation choice needs to be routed to an existing decision or expressed as a new one; when logic ownership or domain boundaries are unclear; when reviewing for duplicated policy, ambiguous fact authority, missing enforcement, hidden decisions, or consumer re-derivation; and when reconciling intended decisions with code behavior.
---

# Decision Engineering

Treat the decision ledger as the source code of intent and the implementation as the source code of behavior. Treat disagreement as a divergence requiring human adjudication: either fix behavior to match recorded intent or change the ledger before changing behavior.

Maintain one ledger directory per system:

```text
decision-ledger/
├── SCHEMA.md
├── index.md
├── log.md
├── decisions/
│   └── D001-determine-example.md
└── generated/
    └── graph.mmd
```

Keep `decisions/*.md` and `SCHEMA.md` authoritative. Treat `index.md` and `generated/graph.mmd` as generated projections. Treat `log.md` as append-only semantic history.

## Hold the structural invariants

- Resolve one question in each decision file.
- Produce one independently decidable output fact from each decision.
- Give every derived fact exactly one producing decision.
- Give every root fact exactly one named external authority or observation boundary.
- Consume authoritative facts; never paraphrase or reconstruct another decision's result.
- Publish a projection that changes representation only. Create another decision if a projection would introduce judgment.
- Enforce at a boundary that can reject or commit an action. Never treat UI presentation as enforcement.
- Verify the authoritative policy, invariant, and enforcement path. Never copy policy into a test as a second authority.
- Keep stable decision IDs. Never renumber or reuse IDs.
- Store `status`, `domain`, `id`, `title`, and ISO-date `updated_at` only in YAML frontmatter. Refresh `updated_at` on every semantic decision edit. Start the body with `## Requirement`; do not repeat identity or lifecycle metadata in an H1 or prose line.

Use the atomicity tests before accepting a structured output. Split it if one part could change independently, be right while another is wrong, serve a consumer independently, or require a different policy, invariant, or verification.

## Locate the ledger

1. Resolve the project root as the nearest Git root, falling back to the active host workspace root.
2. Run `python3 <skill-dir>/scripts/installation_guard.py <project-root>` before any ledger mutation. If it reports multiple applicable copies, stop and require the user to keep either the managed global plugin or one editable project copy.
3. Look inside the project root for an existing ledger named by project instructions or containing `SCHEMA.md`, `index.md`, `log.md`, and `decisions/`.
4. Use the existing location and schema when found. Never create a competing ledger.
5. Otherwise automatically initialize `decision-ledger/` at the project root without requiring a separate setup step:

   ```bash
   python3 <skill-dir>/scripts/ledger_init.py <project-root>/decision-ledger
   ```

6. Accept a user- or project-instruction override only when it resolves inside the project root.
7. Read the ledger's complete `SCHEMA.md`, then `index.md`, before changing anything.
8. Search `index.md` by output fact, question, requirement terms, input fact, consumer, and domain. Open the smallest candidate set. Search all decision files only when the index cannot route the request.

## Route before deriving

Classify the requested change:

- **Consume:** Reuse an existing output fact or projection. Add the consumer to its owning decision when the schema records consumers. Do not create a decision.
- **Edit:** Change the existing decision that owns the affected output fact when the question, inputs, policy, invariant, enforcement, projection, output meaning, or verification changes.
- **Create:** Add a decision only for a genuinely unresolved question with a new authoritative output fact.
- **Reconcile:** For a bug or mismatch, trace the wrong observation backward through projection → output fact → decision → policy and invariant → input authorities → enforcement → verification. Let a human decide whether intent or behavior changes.

State the classification and the authoritative decision ID before editing code or ledger files.

## Derive or change a decision

1. Restate the requirement as an outcome: what must become true? Remove implementation details.
2. State what must remain true for that outcome to hold.
3. Ask the exact uncertainty the system must resolve.
4. Record `status`, `domain`, `id`, `title`, and `updated_at` in YAML frontmatter. Keep those five fields out of the body and set `updated_at` to the current ISO calendar date whenever decision semantics change.
5. Identify each input by stable fact name:
   - Declare a root fact with `Kind: root` and one named `Authority`.
   - Declare a derived fact with `Kind: derived` and `Produced by: Dxxx`.
6. Define one output fact with a stable name, meaning, shape, and atomicity justification.
7. Write the invariant and the policy mapping input facts to the output fact.
8. Name the enforcement boundary that can reject the invalid action or transition. Use an obligation description when code does not exist; never invent a symbol.
9. Name one projection and describe only representational changes.
10. List known consumers. Require each to use the projection or authoritative output contract without re-deriving policy.
11. Write verification obligations for the policy, invariant, and enforcement boundary.
12. Allocate a new file only after routing proves it is necessary:

    ```bash
    python3 <skill-dir>/scripts/ledger_new.py <ledger-dir> "Determine example"
    ```

13. Preserve a decision's ID when renaming, editing, superseding, or retiring it. Prefer superseding or retiring adopted decisions over deleting them.

Read [references/ledger-schema.md](references/ledger-schema.md) before authoring or changing decision files. Read [references/worked-example.md](references/worked-example.md) when the correct create/edit/consume boundary is unclear. Read [references/rationale.md](references/rationale.md) when explaining or contesting a structural rule.

## Record the semantic delta

Append one `log.md` entry for each accepted create, edit, rename, supersede, retire, restore, delete, or schema change. Use:

```markdown
## [YYYY-MM-DD] edit | D003 | Determine handoff readiness

Reason:
Why the decision model changed.

Changed:
- The semantic changes.

Affected:
- Output facts, downstream decisions, consumers, code, and verification.
```

Log semantic changes, not wording-only corrections. Walk downstream from every changed output fact and list the impact.

## Validate and render

Run lint before and after rendering:

```bash
python3 <skill-dir>/scripts/ledger_lint.py <ledger-dir>
python3 <skill-dir>/scripts/ledger_render.py <ledger-dir>
python3 <skill-dir>/scripts/ledger_lint.py <ledger-dir>
```

Treat lint errors as design flaws. Repair ownership, atomicity, references, lifecycle, dependency order, or missing obligations; do not suppress or reword around them. Make each correction pass strictly reduce the error count. Stop and report remaining errors if a pass does not reduce them.

Review warnings explicitly. Do not call a ledger implementation-ready while bindings, authorities, enforcement, verification, or open normative questions remain unresolved.

## Hand off the result

Report:

- the route taken: consume, edit, create, or reconcile;
- the decision IDs and output facts involved;
- the ledger files changed and semantic log entry added;
- downstream decisions, consumers, and code affected;
- lint and render results;
- unresolved questions, premises, or implementation bindings;
- whether code behavior now matches recorded intent.

Require behavior-changing implementation work to cite the decision IDs that justify it or include the ledger delta. Let specifications reference decision IDs rather than restating policies.
