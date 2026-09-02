from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "decision-engineering"


def run(*args: str, cwd: Path, expected: int = 0) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("DECISION_ENGINEERING_PROJECT_ROOT", None)
    env.pop("DECISION_ENGINEERING_SKILL_ROOTS", None)
    result = subprocess.run(args, cwd=cwd, env=env, text=True, capture_output=True)
    if result.returncode != expected:
        raise AssertionError(
            f"command returned {result.returncode}, expected {expected}: {args}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


class PackageTests(unittest.TestCase):
    def test_manifests_share_identity_and_version(self) -> None:
        metadata = json.loads((ROOT / "package" / "metadata.json").read_text(encoding="utf-8"))
        manifests = [
            json.loads((ROOT / "plugin.json").read_text(encoding="utf-8")),
            json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")),
            json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")),
        ]
        self.assertEqual({item["name"] for item in manifests}, {metadata["name"]})
        self.assertEqual({item["version"] for item in manifests}, {metadata["version"]})


class InstallationGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.temp = Path(temporary.name)
        self.project = self.temp / "project"
        self.project.mkdir()
        self.installed_skill = self.temp / "global" / "skills" / "decision-engineering"
        shutil.copytree(SKILL, self.installed_skill, ignore=shutil.ignore_patterns("__pycache__"))
        self.guard = self.installed_skill / "scripts" / "installation_guard.py"

    def test_git_root_and_project_containment(self) -> None:
        (self.project / ".git").mkdir()
        nested = self.project / "src"
        nested.mkdir()
        target = self.project / "decision-ledger"

        accepted = run(sys.executable, str(self.guard), str(target), cwd=nested)
        self.assertIn(str(self.project.resolve()), accepted.stdout)
        self.assertFalse(target.exists())

        outside = self.temp / "outside-ledger"
        rejected = run(sys.executable, str(self.guard), str(outside), cwd=nested, expected=1)
        self.assertIn("outside project root", rejected.stderr)
        self.assertFalse(outside.exists())

    def test_workspace_fallback_without_git(self) -> None:
        target = self.project / "decision-ledger"
        accepted = run(sys.executable, str(self.guard), str(target), cwd=self.project)
        self.assertIn(str(self.project.resolve()), accepted.stdout)
        self.assertFalse(target.exists())

    def test_duplicate_installations_and_resolution(self) -> None:
        (self.project / ".git").mkdir()
        run(sys.executable, str(self.guard), str(self.project), cwd=self.project)

        for location in ("skills", ".agents/skills", ".claude/skills", ".cursor/skills"):
            with self.subTest(location=location):
                editable = self.project / location / "decision-engineering"
                shutil.copytree(SKILL, editable, ignore=shutil.ignore_patterns("__pycache__"))
                blocked = run(
                    sys.executable, str(self.guard), str(self.project),
                    cwd=self.project, expected=1,
                )
                self.assertIn("duplicate Decision Engineering skill authorities", blocked.stderr)
                self.assertIn(str(editable.resolve()), blocked.stderr)
                self.assertIn(str(self.installed_skill.resolve()), blocked.stderr)
                shutil.rmtree(editable)
                run(sys.executable, str(self.guard), str(self.project), cwd=self.project)
