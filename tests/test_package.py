from __future__ import annotations

import json
from datetime import date
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "decision-engineering"


def run(*args: str, cwd: Path, expected: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode != expected:
        raise AssertionError(
            f"command returned {result.returncode}, expected {expected}: {args}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


class PackageTests(unittest.TestCase):
    def test_manifests_share_identity_and_version(self) -> None:
        manifests = [
            json.loads((ROOT / "plugin.json").read_text(encoding="utf-8")),
            json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")),
            json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")),
        ]
        self.assertEqual({item["name"] for item in manifests}, {"decision-engineering"})
        self.assertEqual({item["version"] for item in manifests}, {"0.1.0"})

    def test_ledger_reuse_and_project_containment(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            temp = Path(raw)
            project = temp / "project"
            project.mkdir()
            (project / ".git").mkdir()
            installed_skill = temp / "global" / "decision-engineering" / "skills" / "decision-engineering"
            installed_skill.parent.mkdir(parents=True)
            shutil.copytree(SKILL, installed_skill)
            scripts = installed_skill / "scripts"
            ledger = project / "decision-ledger"

            run(sys.executable, str(scripts / "ledger_init.py"), str(ledger), cwd=project)
            run(sys.executable, str(scripts / "ledger_new.py"), str(ledger), "Determine reuse", cwd=project)
            before = sorted(path.name for path in (ledger / "decisions").iterdir())

            reused = run(sys.executable, str(scripts / "ledger_init.py"), str(ledger), cwd=project)
            self.assertIn("existing ledger preserved", reused.stdout)
            self.assertEqual(sorted(path.name for path in (ledger / "decisions").iterdir()), before)

            outside = temp / "outside-ledger"
            rejected = run(
                sys.executable,
                str(scripts / "ledger_init.py"),
                str(outside),
                cwd=project,
                expected=1,
            )
            self.assertIn("outside project root", rejected.stderr)
            self.assertFalse(outside.exists())

    def test_host_lifecycle_and_duplicate_blocking(self) -> None:
        for host in ("claude", "codex", "cursor"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as raw:
                temp = Path(raw)
                project = temp / "project"
                project.mkdir()
                (project / ".git").mkdir()
                installed_skill = temp / "global" / host / "decision-engineering" / "skills" / "decision-engineering"
                installed_skill.parent.mkdir(parents=True)
                shutil.copytree(SKILL, installed_skill)
                scripts = installed_skill / "scripts"
                ledger = project / "decision-ledger"

                run(sys.executable, str(scripts / "ledger_init.py"), str(ledger), cwd=project)
                marker = ledger / "consumer-data.txt"
                marker.write_text("preserve me", encoding="utf-8")
                created = run(sys.executable, str(scripts / "ledger_new.py"), str(ledger), "Determine sample", cwd=project)
                decision_path = Path(created.stdout.splitlines()[0])
                self.assertIn(
                    f"updated_at: {date.today().isoformat()}",
                    decision_path.read_text(encoding="utf-8"),
                )
                decision_path.write_text(
                    """---
status: active
domain: sample
id: D001
title: "Determine sample"
updated_at: 2026-08-21
---

## Requirement

The sample outcome becomes true.

## Question

Is the sample accepted?

## Input facts

- `sample.request`
  - Kind: root
  - Authority: test fixture

## Output fact

- Name: `sample.acceptance`
- Meaning: Whether the sample is accepted.
- Shape: `accepted | rejected`
- Atomicity: One binary state changes as a whole.

## Invariant

Only an observed request can be accepted.

## Policy

Accept the observed test request.

## Enforcement

The test boundary rejects an unobserved request.

## Projection

`sample.acceptance.public`

Render the state without new judgment.

## Consumers

- Test report

## Verification

- Exercise the accepted branch.
- Prove rejection at the test boundary.
""",
                    encoding="utf-8",
                )
                with (ledger / "log.md").open("a", encoding="utf-8") as handle:
                    handle.write("\n## [2026-08-21] create | D001 | Determine sample\n")
                run(sys.executable, str(scripts / "ledger_render.py"), str(ledger), cwd=project)
                run(sys.executable, str(scripts / "ledger_lint.py"), str(ledger), cwd=project)

                valid_decision = decision_path.read_text(encoding="utf-8")
                decision_path.write_text(
                    valid_decision.replace("updated_at: 2026-08-21", "updated_at: not-a-date"),
                    encoding="utf-8",
                )
                malformed = run(
                    sys.executable,
                    str(scripts / "ledger_lint.py"),
                    str(ledger),
                    cwd=project,
                    expected=1,
                )
                self.assertIn("updated_at must be an ISO calendar date", malformed.stdout)
                decision_path.write_text(valid_decision, encoding="utf-8")

                shutil.rmtree(installed_skill)
                shutil.copytree(SKILL, installed_skill)
                self.assertEqual(marker.read_text(encoding="utf-8"), "preserve me")

                editable = project / ".agents" / "skills" / "decision-engineering"
                editable.mkdir(parents=True)
                (editable / "SKILL.md").write_text("---\nname: decision-engineering\n---\n", encoding="utf-8")
                for mutation in ("ledger_render.py", "ledger_init.py"):
                    blocked = run(
                        sys.executable,
                        str(installed_skill / "scripts" / mutation),
                        str(ledger),
                        cwd=project,
                        expected=1,
                    )
                    self.assertIn("duplicate Decision Engineering skill authorities", blocked.stderr)
                    self.assertIn(str(editable.resolve()), blocked.stderr)
                    self.assertIn(str(installed_skill.resolve()), blocked.stderr)
                    self.assertIn("then retry", blocked.stderr)
                blocked_create = run(
                    sys.executable,
                    str(installed_skill / "scripts" / "ledger_new.py"),
                    str(ledger),
                    "Determine blocked",
                    cwd=project,
                    expected=1,
                )
                self.assertIn("duplicate Decision Engineering skill authorities", blocked_create.stderr)
                shutil.rmtree(editable.parent)

                shutil.rmtree(installed_skill.parents[1])
                self.assertTrue(ledger.is_dir())
                self.assertEqual(marker.read_text(encoding="utf-8"), "preserve me")
