# Decision index

Generated from `decisions/*.md`. Do not edit by hand.

| ID | Decision | Produces | Reads | Domain | Status |
|---|---|---|---|---|---|
| [D001](decisions/D001-determine-intent-authority.md) | Determine intent authority | `framework.intent-authority` | `framework.persisted-intent-requirement` | authority | active |
| [D002](decisions/D002-determine-behavior-authority.md) | Determine behavior authority | `framework.behavior-authority` | `framework.behavior-observation-requirement` | authority | active |
| [D003](decisions/D003-resolve-intent-behavior-divergence.md) | Resolve intent behavior divergence | `framework.divergence-resolution` | `framework.intent-authority`, `framework.behavior-authority`, `framework.divergence-observation` | authority | active |
| [D004](decisions/D004-determine-decision-atomicity.md) | Determine decision atomicity | `framework.decision-atomicity` | `framework.correctability-requirement`, `framework.atomicity-evidence` | modeling | active |
| [D005](decisions/D005-determine-fact-authority.md) | Determine fact authority | `framework.fact-authority` | `framework.correctability-requirement`, `framework.decision-atomicity` | modeling | active |
| [D006](decisions/D006-determine-decision-record-contract.md) | Determine decision record contract | `framework.record-validity` | `framework.decision-atomicity`, `framework.fact-authority`, `framework.machine-checkability-requirement` | ledger | active |
| [D007](decisions/D007-determine-ledger-storage-model.md) | Determine ledger storage model | `framework.ledger-storage-model` | `framework.record-validity`, `framework.change-locality-requirement` | ledger | active |
| [D008](decisions/D008-route-framework-changes.md) | Route framework changes | `framework.change-route` | `maintenance.request`, `framework.intent-authority`, `framework.fact-authority` | operations | active |
| [D009](decisions/D009-determine-consumer-representation-treatment.md) | Determine consumer representation treatment | `framework.consumer-representation-treatment` | `framework.fact-authority`, `framework.consumer-representation-requirement` | distribution | active |
| [D010](decisions/D010-determine-consumer-fact-access.md) | Determine consumer fact access | `framework.consumer-access` | `framework.consumer-representation-treatment`, `framework.fact-authority` | distribution | active |
| [D011](decisions/D011-determine-enforcement-boundary.md) | Determine enforcement boundary | `framework.enforcement-sufficiency` | `framework.invariant-preservation-requirement` | assurance | active |
| [D012](decisions/D012-determine-verification-target.md) | Determine verification target | `framework.verification-sufficiency` | `framework.enforcement-sufficiency`, `framework.decision-atomicity`, `framework.verification-evidence-requirement` | assurance | active |
| [D013](decisions/D013-determine-domain-membership.md) | Determine domain membership | `framework.domain-membership` | `framework.decision-atomicity`, `framework.fact-authority`, `framework.domain-evidence` | topology | active |
| [D014](decisions/D014-validate-dependency-graph.md) | Validate dependency graph | `framework.graph-validity` | `framework.fact-authority`, `framework.ledger-storage-model`, `framework.domain-membership`, `ledger.candidate-dependencies` | topology | active |
| [D015](decisions/D015-determine-decision-identity.md) | Determine decision identity | `framework.decision-identity` | `framework.ledger-storage-model`, `ledger.existing-identifiers`, `ledger.record-lifecycle` | lifecycle | active |
| [D016](decisions/D016-determine-semantic-logging.md) | Determine semantic logging | `framework.semantic-log-obligation` | `framework.decision-identity`, `ledger.change-kind` | lifecycle | active |
| [D017](decisions/D017-determine-ledger-acceptance.md) | Determine ledger acceptance | `framework.ledger-acceptance` | `framework.record-validity`, `framework.verification-sufficiency`, `framework.graph-validity`, `framework.semantic-log-obligation`, `ledger.pre-render-lint-result`, `ledger.render-result`, `ledger.post-render-lint-result`, `ledger.normative-review` | assurance | active |
| [D018](decisions/D018-determine-ledger-lookup-scope.md) | Determine ledger lookup scope | `framework.lookup-scope` | `maintenance.lookup-query`, `framework.ledger-storage-model`, `framework.change-route`, `framework.graph-validity` | operations | active |
| [D019](decisions/D019-determine-package-identity.md) | Determine package identity | `package.identity` | `package.requested-identity` | distribution | active |
| [D020](decisions/D020-determine-canonical-skill-source.md) | Determine canonical skill source | `package.canonical-skill-source` | `package.requested-source-layout` | distribution | active |
| [D021](decisions/D021-determine-packaged-skill-contents.md) | Determine packaged skill contents | `package.skill-content-contract` | `package.canonical-skill-source`, `package.requested-content-scope` | distribution | active |
| [D022](decisions/D022-determine-claude-code-distribution.md) | Determine Claude Code distribution | `package.claude-code-distribution` | `package.identity`, `package.skill-content-contract`, `package.requested-claude-support` | distribution | active |
| [D023](decisions/D023-determine-codex-distribution.md) | Determine Codex distribution | `package.codex-distribution` | `package.identity`, `package.skill-content-contract`, `package.requested-codex-support` | distribution | active |
| [D024](decisions/D024-determine-cursor-distribution.md) | Determine Cursor distribution | `package.cursor-distribution` | `package.identity`, `package.skill-content-contract`, `package.requested-cursor-support` | distribution | active |
| [D025](decisions/D025-determine-editable-project-installation.md) | Determine editable project installation | `package.editable-installation` | `package.identity`, `package.skill-content-contract`, `package.requested-editable-channel` | distribution | active |
| [D026](decisions/D026-prevent-duplicate-skill-authority.md) | Prevent duplicate skill authority | `package.duplicate-authority-policy` | `package.claude-code-distribution`, `package.codex-distribution`, `package.cursor-distribution`, `package.editable-installation`, `package.requested-duplicate-policy` | assurance | active |
| [D027](decisions/D027-determine-ledger-location.md) | Determine ledger location | `package.ledger-location` | `project.detected-root`, `project.explicit-ledger-path` | ledger | active |
| [D028](decisions/D028-initialize-a-missing-ledger.md) | Initialize a missing ledger | `package.ledger-initialization` | `package.ledger-location`, `package.duplicate-authority-policy`, `project.ledger-existence` | operations | active |
| [D029](decisions/D029-determine-release-versioning.md) | Determine release versioning | `package.release-version` | `package.requested-versioning` | lifecycle | active |
| [D030](decisions/D030-generate-distribution-metadata.md) | Generate distribution metadata | `package.distribution-metadata` | `package.identity`, `package.canonical-skill-source`, `package.claude-code-distribution`, `package.codex-distribution`, `package.cursor-distribution`, `package.release-version` | distribution | active |
| [D031](decisions/D031-determine-macos-support.md) | Determine macOS support | `package.macos-support` | `package.requested-macos-support`, `package.skill-content-contract` | compatibility | active |
| [D032](decisions/D032-determine-linux-support.md) | Determine Linux support | `package.linux-support` | `package.requested-linux-support`, `package.skill-content-contract` | compatibility | active |
| [D033](decisions/D033-determine-windows-support.md) | Determine Windows support | `package.windows-support` | `package.requested-windows-support`, `package.skill-content-contract` | compatibility | active |
| [D034](decisions/D034-determine-public-release-source.md) | Determine public release source | `package.public-release-source` | `package.identity`, `package.requested-release-source` | distribution | active |
| [D035](decisions/D035-determine-package-licensing.md) | Determine package licensing | `package.license` | `package.public-release-source`, `package.delegated-license-choice` | governance | active |
| [D036](decisions/D036-determine-support-channels.md) | Determine support channels | `package.support-routing` | `package.public-release-source`, `package.delegated-support-choice` | governance | active |
| [D037](decisions/D037-constrain-packaged-execution.md) | Constrain packaged execution | `package.execution-boundary` | `package.ledger-location`, `package.requested-execution-boundary` | assurance | active |
| [D038](decisions/D038-determine-package-acceptance.md) | Determine package acceptance | `package.acceptance` | `package.claude-code-distribution`, `package.codex-distribution`, `package.cursor-distribution`, `package.editable-installation`, `package.duplicate-authority-policy`, `package.ledger-initialization`, `package.distribution-metadata`, `package.macos-support`, `package.linux-support`, `package.windows-support`, `package.license`, `package.support-routing`, `package.execution-boundary`, `package.acceptance-evidence` | assurance | active |
| [D039](decisions/D039-determine-release-maturity-gate.md) | Determine release maturity gate | `package.release-maturity` | `package.acceptance`, `package.benchmark-results` | lifecycle | active |

## Routing

Search this file by output fact, question, input fact, consumer, domain, status, or requirement terms in the linked decision record.
