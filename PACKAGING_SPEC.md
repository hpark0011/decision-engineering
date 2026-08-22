---
status: delegation-ready
authority: "Active decision records D019–D039"
target_release: "0.1.0"
public_repository: "https://github.com/hpark0011/decision-engineering"
---
# Decision Engineering Public Packaging Specification

## 1. Assignment

Package Decision Engineering as a public, installable agent skill for Claude Code, Codex, Cursor, and editable project use through skills.sh.

Work from the existing repository state. Inspect before changing anything, preserve conforming implementation, and close only the gaps between the repository and this specification. Do not redesign the Decision Engineering method or revise the product decisions listed here.

The work is complete only when the repository satisfies the acceptance contract in section 8 and all locally executable checks pass.

## 2. Sources of authority

When sources conflict, use this order:

1. Active records in decision-ledger/decisions/D019–D039 define intended packaging behavior.
2. decision-ledger/SCHEMA.md defines how those decisions are interpreted.
3. Executable code and tests show current behavior.
4. README and generated manifests are projections and must be corrected when they conflict with the active decisions.

Do not change an active decision merely to make an implementation easier. If compliance requires a new product choice or contradicts an active decision, stop and report the conflict to the owner.

## 3. Required product contract

| Area | Required result | Decision |
| --- | --- | --- |
| Public identity | Use decision-engineering exactly in every manifest, install command, release artifact, and document. | D019 |
| Canonical source | The only maintained skill tree is skills/decision-engineering. | D020 |
| Payload | Ship every file under the canonical skill tree recursively, preserving relative paths. | D021 |
| Claude Code | Provide a user-scoped managed Claude plugin through .claude-plugin/plugin.json. | D022 |
| Codex | Provide a user-scoped managed Codex plugin through .codex-plugin/plugin.json. | D023 |
| Cursor | Provide a user-scoped Agent Plugins v1 package through root plugin.json and standard skills discovery. | D024 |
| Editable install | Support project-scoped installation from hpark0011/decision-engineering with skills.sh, without --copy and without a bespoke installer. | D025 |
| Duplicate authority | Block ledger mutations when more than one applicable Decision Engineering skill is present and identify copies to remove. | D026 |
| Ledger location | Use an explicit project-contained path when supplied; otherwise use decision-ledger under the nearest Git root, falling back to the workspace root. | D027 |
| First use | Reuse a conforming ledger or initialize a missing ledger automatically after containment and duplicate checks. Never overwrite an existing ledger. | D028 |
| Versioning | Use strict Semantic Versioning, beginning at 0.1.0, with one version across manifests and tags. | D029 |
| Metadata | Generate all host manifests, marketplace catalogs, and VERSION from one metadata definition. Checked-in projections must not drift. | D030 |
| macOS | Support macOS only while acceptance checks pass on its current CI runner. | D031 |
| Linux | Support Linux only while acceptance checks pass on its current CI runner. | D032 |
| Windows | Support Windows only while acceptance checks pass on its current CI runner. | D033 |
| Release source | Publish source and releases from https://github.com/hpark0011/decision-engineering. | D034 |
| License | Use MIT consistently in LICENSE and every applicable manifest. | D035 |
| Support | Route reproducible defects to GitHub Issues; route questions and field reports to GitHub Discussions. | D036 |
| Runtime boundary | Runtime uses local standard-library operations only, performs no telemetry or network access, and writes only to the resolved project ledger. | D037 |
| Package acceptance | Reject release when any required lifecycle, host, platform, metadata, license, support, or execution check is missing or failing. | D038 |
| Maturity | Acceptance permits 0.1.0. Version 1.0.0 additionally requires the benchmark evidence in section 9. | D039 |

## 4. Required repository shape

The completed package must contain and consistently use these paths:

```text
skills/decision-engineering/       canonical skill payload
  SKILL.md
  assets/
  references/
  scripts/

package/metadata.json              implementation source for generated metadata
plugin.json                        Cursor / Agent Plugins v1 manifest
.claude-plugin/plugin.json         Claude Code plugin manifest
.claude-plugin/marketplace.json    Claude marketplace catalog
.codex-plugin/plugin.json          Codex plugin manifest
.agents/plugins/marketplace.json   Codex marketplace catalog
VERSION                            shared package version
LICENSE                            MIT license
README.md                          install, lifecycle, privacy, and support instructions
CHANGELOG.md                       release history
scripts/generate_manifests.py      metadata generator and drift checker
scripts/validate_package.py        local package acceptance entry point
tests/                             package and lifecycle tests
.github/workflows/validate.yml     macOS, Linux, and Windows validation matrix
```

Do not create maintained copies of the Decision Engineering SKILL.md outside skills/decision-engineering. Host metadata must point to or discover the canonical skill tree.

## 5. Installation and lifecycle requirements

### Managed installs

Document user-scoped managed installation for Claude Code and Codex using their native marketplace/plugin flows. Document Cursor installation as an Agent Plugins v1 user-scoped flow.

Managed installations are host-owned and read-only from the project's perspective. They must not create an editable project copy.

### Editable project install

Document a skills.sh command targeting hpark0011/decision-engineering, the decision-engineering skill, and the supported agents. Do not use --copy. Do not add a custom installer.

Disable the third-party skills.sh installation event in the documented command when supported. Clarify that this installation-time network behavior is distinct from Decision Engineering runtime, which must remain local and telemetry-free.

### Updates and uninstall

Document host-managed updates for managed plugins and project-scoped skills.sh updates for editable installations.

Updating or uninstalling the skill must never delete, overwrite, or migrate a project's decision-ledger without a separate authorized ledger operation.

### First invocation

Before any ledger mutation:

1. Resolve the active project root.
2. Resolve an explicit project-contained ledger path, or default to project-root/decision-ledger.
3. Reject paths outside the active project.
4. Scan for competing applicable Decision Engineering skill authorities.
5. Block with actionable removal guidance if duplicates exist.
6. Reuse an existing conforming ledger.
7. Otherwise initialize from the bundled template without overwriting existing files.

The same guard applies to scripted mutations and direct agent edits instructed by SKILL.md.

## 6. Runtime safety requirements

Packaged runtime code must:

- perform no network requests;
- emit no telemetry;
- process project data locally;
- use Python standard-library dependencies only;
- reject ledger targets outside the active project;
- restrict writes to the resolved decision ledger; and
- avoid hidden global configuration changes.

Package validation must inspect runtime imports and fail on network-client dependencies. Installation documentation must not imply that third-party installer behavior is package runtime behavior.

## 7. Implementation sequence

Use this order unless the current repository already satisfies a step:

 1. Inventory existing package files and map each to D019–D039.
 2. Confirm skills/decision-engineering is the only canonical maintained skill source.
 3. Confirm the full skill payload is self-contained and uses valid relative references.
 4. Confirm package/metadata.json is the sole implementation input for generated host metadata.
 5. Generate or repair Claude, Codex, Cursor, marketplace, VERSION, repository, and license projections.
 6. Implement or repair project containment, duplicate-authority, initialization, and mutation guards.
 7. Implement or repair host lifecycle and package acceptance tests.
 8. Align README, CHANGELOG, license, privacy, support, update, and uninstall guidance with the active decisions.
 9. Run targeted tests while editing.
10. Run the full local acceptance command once near completion.
11. Confirm the three-OS CI matrix is configured.
12. Report local results separately from checks that require host credentials, marketplace access, CI, or publication authority.

Do not publish a release, push changes, create marketplace listings, or modify remote repository settings unless separately authorized.

## 8. Acceptance contract for 0.1.0

A candidate is accepted only when every applicable item below passes.

### Source and metadata

- The public identity is decision-engineering everywhere.
- skills/decision-engineering exists and contains the complete runnable payload.
- No second maintained Decision Engineering skill authority exists.
- Generated manifests and VERSION match package/metadata.json.
- All repository URLs point to hpark0011/decision-engineering.
- Every version is strict SemVer and agrees on 0.1.0.
- LICENSE exists and applicable manifests declare MIT.
- README routes defects to Issues and questions/field reports to Discussions.

### Host packaging

- Claude Code manifest and marketplace metadata validate and locate the canonical skill.
- Codex manifest and marketplace metadata validate and locate the canonical skill.
- Cursor root manifest validates against Agent Plugins v1 and standard skills discovery locates the canonical skill.
- Documentation makes managed installations user-scoped.
- The editable skills.sh flow is project-scoped, uses no --copy flag, and introduces no bespoke installer.

### Project lifecycle

For each supported host or a faithful isolated harness, verify:

- installation and skill discovery;
- skill invocation;
- automatic initialization of a missing ledger;
- reuse of an existing conforming ledger;
- creation of a valid decision;
- lint and render behavior;
- preservation of the ledger across skill update;
- preservation of the ledger across uninstall;
- rejection of a ledger path outside the project;
- duplicate-authority detection before mutation; and
- actionable removal guidance when mutation is blocked.

### Runtime and platforms

- Runtime scripts contain no prohibited network-client imports.
- Runtime performs no telemetry or network calls.
- Writes remain inside the resolved project ledger.
- Package validation and ledger lint pass on ubuntu-latest, macos-latest, and windows-latest.
- Any missing required result rejects acceptance; no check may be treated as optional merely because it is inconvenient to run.

## 9. Release maturity

0.1.0 eligibility requires complete package acceptance.

Do not declare 1.0.0 eligible until at least 20 matched tasks demonstrate:

- at least 25 percent fewer requirement-to-code divergences; and
- no degradation in initial correctness.

Packaging completion alone is not evidence for 1.0.0.

## 10. Validation commands

Run from the repository root:

```bash
python scripts/generate_manifests.py --check
python -m unittest discover -s tests -v
python skills/decision-engineering/scripts/ledger_lint.py decision-ledger
python scripts/validate_package.py
```

If metadata intentionally changes, regenerate before checking:

```bash
python scripts/generate_manifests.py
python scripts/validate_package.py
```

Also verify the GitHub Actions workflow runs the package validator and ledger lint on ubuntu-latest, macos-latest, and windows-latest.

Do not claim native host or marketplace verification unless it was actually executed. Record unavailable checks as external evidence still required.

## 11. Agent constraints and stop conditions

The delegated agent may modify repository files necessary to satisfy this specification and may run local validation. It must preserve unrelated user changes.

Stop and request owner direction when:

- an active decision conflicts with another active decision;
- a host's current official packaging contract cannot satisfy the recorded decision;
- compliance requires changing package identity, repository, license, support routing, platform scope, installation ownership, runtime privacy, or release maturity;
- a required external action needs credentials, publication authority, or remote configuration access; or
- destructive migration of a user's ledger appears necessary.

When official host packaging rules may have changed, verify them against current primary documentation and cite the source in the handoff.

## 12. Required handoff report

Return a concise report containing:

1. Outcome: accepted, rejected, or blocked.
2. Files changed, with the decision IDs each change implements.
3. Validation commands run and their exact pass/fail results.
4. Acceptance checklist failures or missing evidence.
5. External host, CI, marketplace, or publication work still required.
6. Any observed conflict between intended behavior and repository behavior.
7. Confirmation that no release or remote mutation was performed without authorization.

## 13. Copyable delegation prompt

Use this prompt when assigning the work:

> Package the Decision Engineering skill according to PACKAGING_SPEC.md. Treat decision-ledger/decisions/D019–D039 as authoritative intent. Inspect the current repository first, preserve conforming work, and implement only the gaps. Do not invent or revise product policy. Run the local acceptance checks, keep all runtime processing local and project-confined, and return the required handoff report. Do not publish, push, or modify remote marketplace/repository state without separate authorization.