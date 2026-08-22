---
title: Plugin vs Installer — Distributing Agent Skills
created: 2026-08-21
updated: 2026-08-21
type: comparison
tags: [comparison, tooling, agent-harness, methodology, projection, open-question]
sources:
  - raw/articles/mattpocock-skills-readme.md
  - raw/articles/mattpocock-skills-adr-0002-claude-code-plugin.md
  - raw/articles/compound-engineering-plugin-readme.md
confidence: medium
---

# Plugin vs Installer — Distributing Agent Skills

**Defined in glossary:** Agent skill, Decision home, Duplicated decision, Projection, Authority.

How to ship the decision engineering skills so other people can install them. Two channels
exist, and the two most-cited prior-art repos both ship **both** rather than choosing.

## The two channels

| | Native plugin | `npx` installer |
|---|---|---|
| What arrives | A managed, read-only bundle | Ordinary files in the user's repo |
| Relationship | Subscribe | Fork |
| Updates | Push — arrive when the author ships | Pull — user runs `npx skills update` |
| Editing | Discouraged/blocked; edits are lost on update | Expected; the point of the channel |
| Reach | Only harnesses with a plugin system | Any Agent-Skills-standard harness |
| Curation | Manifest names what ships | Installer prompts the user to pick |
| Maintenance cost | Manifest + version sync | Zero, if you reuse `skills.sh` |

Matt Pocock's framing: *"Two ways in, two philosophies… Pick one: installing both leaves you
with every skill twice."*^[raw/articles/mattpocock-skills-readme.md] That warning is the
[[decision-ledger]] failure mode in miniature — two installed copies of the same skill are two
homes for the same instruction, and the agent has no way to know which one governs.

## What the prior art actually does

### mattpocock/skills

Plugin is the headline route (`claude plugins install mattpocock-skills`, accepted into Claude
Code's official marketplace so no `marketplace add` step is needed). `npx skills@latest add
mattpocock/skills` — **skills.sh, a third-party generic installer he did not write** — covers
Codex and everything else. The installer channel therefore costs him nothing to
maintain.^[raw/articles/mattpocock-skills-readme.md]

Per-repo configuration is **not** installer logic. It is a skill: `/setup-matt-pocock-skills`,
run once per repo, which interviews the user about issue tracker, triage labels, and doc
location.^[raw/articles/mattpocock-skills-readme.md] The installer moves files; the skill
resolves the decisions.

### EveryInc/compound-engineering-plugin

Plugin everywhere. One root `skills/` directory, with thin per-host manifest directories
(`.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.grok-plugin/`, `.kimi-plugin/`,
`.omp-plugin/`, `.opencode/`, `.pi/extensions/`, `.agy/`) projecting the same skills into each
ecosystem. They had a bespoke Bun `convert` / `install --to` CLI and have demoted it: it is now
"only needed for repo development tasks and converter maintenance," not
installation.^[raw/articles/compound-engineering-plugin-readme.md]

Notably, Qwen Code "installs Claude Code-compatible plugins directly from GitHub and converts
the plugin format during install."^[raw/articles/compound-engineering-plugin-readme.md] The
Claude plugin manifest is becoming the de-facto interchange format, which raises the value of
producing one even for non-Claude reach.

## Three hazards the sources document

**1. A bespoke installer that writes global config outlives its usefulness.** CE's old Bun CLI
injected a managed block into the user's *global* `~/.codex/AGENTS.md`, and one line in it
"incorrectly told Codex to collapse subagent dispatch onto the main thread." The README now
carries a removal prompt users must run.^[raw/articles/compound-engineering-plugin-readme.md]
An installer that only copies files into the project has no such tail.

**2. Manifest format constrains repo layout.** Claude's `plugin.json` takes `skills` as an array
of explicit paths, so a bucketed repo can ship a curated subset. Codex takes a **single path
string** and discovers `SKILL.md` recursively beneath it — no way to name two buckets or exclude
one. Symlinked flat directories fail too: "Codex copies the plugin tree into its cache and
**drops symlinks**, so the skills arrive empty." Pocock deferred the Codex plugin rather than
restructure `skills/` or commit duplicate copies.^[raw/articles/mattpocock-skills-adr-0002-claude-code-plugin.md]

**3. Moving your layout strands existing installs.** CE moved from `plugins/compound-engineering`
to a root-native layout; installed users hold a *cached* marketplace snapshot pointing at the old
path, so `/plugin update` alone silently keeps them on the previous version. The marketplace must
be refreshed first — "order matters."^[raw/articles/compound-engineering-plugin-readme.md]
Layout is part of the published contract, not an internal detail.

Related: Claude's official marketplace listing pins a **sha**, so a release reaches installed
users when that pin moves, not when the author tags. Pocock's ADR records the listing sitting two
commits behind `main`, showing 22 skills instead of the manifest's
24.^[raw/articles/mattpocock-skills-adr-0002-claude-code-plugin.md]

## Where this touches the framework

This is not a neutral tooling question. Three connections:

- **The manifest is a [[authority-and-projection|projection]].** `skills/` is the authoritative
  home for skill content; each per-host `plugin.json` is a derived view of it. Pocock encodes
  exactly this as an invariant: *"Every promoted skill has an entry in `plugin.json`'s `skills`
  array."*^[raw/articles/mattpocock-skills-adr-0002-claude-code-plugin.md] Without that
  enforcement the manifest becomes a stale projection that silently drops skills.
- **Version sync is a second invariant.** `.claude-plugin/plugin.json`'s `version` must track
  `package.json`'s, because the host reads the plugin version to decide whether installed users
  see an update. Two fields, one fact — a duplicated-fact hazard resolved by a release-time rule
  rather than a single source.
- **The ADR itself is decision engineering in the wild.** Pocock's `0002` states the forcing
  constraint, records rejected options with the reason each failed, and closes with an
  "Invariants this creates" section. It is a decision entry with dependency edges, written
  without the vocabulary. Worth reading as evidence the [[decision-ledger]] shape is
  discovered independently under pressure.

## Working recommendation for this repo

Do both, in this order:

1. Keep one root `skills/` directory as the single home for skill content.
2. Add `.claude-plugin/plugin.json` listing each shipped skill explicitly, plus
   `marketplace.json` as the fallback install path. Sync `version` on every release.
3. Point at `skills.sh` for the `npx` route rather than writing an installer. Reach for free,
   no global-config tail.
4. Ship a `setup-decision-engineering` skill for per-repo configuration — where the ledger
   lives, which domains exist — instead of putting that interview in installer code.

This mirrors what [[productizing-decision-engineering]] argues at the product level: the
distribution channel should not ask the user to learn the method. The setup skill is the
first place the method touches them, and it should behave like a conversation.

## Open questions

- Do the decision engineering skills need bucketing (promoted vs. in-progress) at all? If not,
  the Codex single-path constraint that blocked Pocock never binds here — a flat promoted-only
  `skills/` ships to both ecosystems from one manifest each.
- Does the ledger itself travel with the skills, or is it always repo-local content the setup
  skill scaffolds? A shipped ledger template is a projection; a shipped ledger is a competing
  authority. See [[authority-and-projection]].
- Under the plugin channel the skills are read-only. Does that conflict with a method whose
  premise is that decisions get amended and superseded, or is the amendable artifact strictly
  the user's ledger and never the skill?
- Is the `.claude-plugin` manifest worth generating from `skills/` rather than hand-maintaining,
  given the invariant above is exactly the kind a script can check?

## Related

[[productizing-decision-engineering]] · [[decision-engineering]] · [[decision-ledger]] ·
[[authority-and-projection]] · [[schema-as-agent-constraint]]
