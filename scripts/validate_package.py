#!/usr/bin/env python3
"""Validate generated metadata, source ownership, execution boundaries, and installation checks."""

from __future__ import annotations

import ast
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "skills" / "decision-engineering"
FORBIDDEN_IMPORTS = {"httpx", "requests", "socket", "urllib"}
REPOSITORY = "https://github.com/hpark0011/decision-engineering"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
REQUIRED_RUNNERS = ("ubuntu-latest", "macos-latest", "windows-latest")
REQUIRED_PAYLOAD = (
    "SKILL.md",
    "assets/decision-ledger/SCHEMA.md",
    "scripts/installation_guard.py",
)


def fail(message: str) -> None:
    raise SystemExit(f"validate_package: {message}")


def load_json(relative: str) -> dict:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing required manifest {relative}")
    return json.loads(path.read_text(encoding="utf-8"))


def skill_target(manifest: dict, relative: str) -> None:
    """Confirm a host manifest's skills entry locates the canonical skill tree."""
    declared = manifest.get("skills")
    entries = [declared] if isinstance(declared, str) else list(declared or [])
    if not entries:
        fail(f"{relative} declares no skills location")
    for entry in entries:
        if not isinstance(entry, str):
            fail(f"{relative} declares a non-path skills entry")
        located = (ROOT / entry.lstrip("./")).resolve()
        if located == CANONICAL.resolve():
            continue
        if (located / "decision-engineering" / "SKILL.md").is_file():
            continue
        fail(f"{relative} skills entry {entry} does not locate the canonical skill")


def check_identity_and_metadata() -> None:
    metadata = load_json("package/metadata.json")
    if metadata.get("name") != "decision-engineering":
        fail("package identity must be decision-engineering")
    version = metadata.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        fail("package version is not strict semver")

    versioned = {
        "plugin.json": load_json("plugin.json"),
        ".claude-plugin/plugin.json": load_json(".claude-plugin/plugin.json"),
        ".codex-plugin/plugin.json": load_json(".codex-plugin/plugin.json"),
    }
    for relative, manifest in versioned.items():
        if manifest.get("name") != "decision-engineering":
            fail(f"{relative} does not use the decision-engineering identity")
        if manifest.get("version") != version:
            fail(f"{relative} version disagrees with package/metadata.json")
        if manifest.get("license") != "MIT":
            fail(f"{relative} does not declare MIT")
        for field in ("homepage", "repository"):
            if not str(manifest.get(field, "")).startswith(REPOSITORY):
                fail(f"{relative} {field} does not point at {REPOSITORY}")

    version_file = ROOT / "VERSION"
    if not version_file.is_file() or version_file.read_text(encoding="utf-8").strip() != version:
        fail("VERSION disagrees with package/metadata.json")

    claude_marketplace = load_json(".claude-plugin/marketplace.json")
    if claude_marketplace.get("metadata", {}).get("version") != version:
        fail("Claude marketplace catalog version disagrees with package/metadata.json")
    catalogs = {
        ".claude-plugin/marketplace.json": claude_marketplace,
        ".agents/plugins/marketplace.json": load_json(".agents/plugins/marketplace.json"),
    }
    for relative, catalog in catalogs.items():
        plugins = catalog.get("plugins") or []
        if catalog.get("name") != "decision-engineering" or len(plugins) != 1:
            fail(f"{relative} does not list exactly one decision-engineering plugin")
        if plugins[0].get("name") != "decision-engineering":
            fail(f"{relative} plugin entry does not use the decision-engineering identity")

    skill_target(versioned[".claude-plugin/plugin.json"], ".claude-plugin/plugin.json")
    skill_target(versioned[".codex-plugin/plugin.json"], ".codex-plugin/plugin.json")

    portable = versioned["plugin.json"]
    allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
    if set(portable) - allowed:
        fail("portable manifest contains unsupported fields")
    if portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("portable manifest schema is incorrect")
    # Cursor loads the root manifest and discovers skills from the standard skills/ tree.
    if not (ROOT / "skills" / "decision-engineering" / "SKILL.md").is_file():
        fail("standard skills discovery cannot locate the canonical skill")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").is_file() else ""
    if "MIT License" not in license_text:
        fail("LICENSE is missing or is not the MIT license")


def check_documentation() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if not re.search(r"(?i)defects?.*github issues", readme):
        fail("README does not route reproducible defects to GitHub Issues")
    if not re.search(r"(?i)github discussions", readme):
        fail("README does not route questions and field reports to GitHub Discussions")
    if "--scope user" not in readme:
        fail("README does not document user-scoped managed installation")
    installers = [line for line in readme.splitlines() if "skills@latest add" in line]
    if not installers:
        fail("README does not document the skills.sh editable install")
    for line in installers:
        if "--copy" in line:
            fail("README documents skills.sh with the --copy flag")
        if "--global" in line:
            fail("README documents the editable install as global rather than project-scoped")
        if "hpark0011/decision-engineering" not in line:
            fail("README skills.sh command does not target hpark0011/decision-engineering")
    if not (ROOT / "CHANGELOG.md").is_file():
        fail("CHANGELOG.md is missing")

    bespoke = [
        path.relative_to(ROOT)
        for path in ROOT.glob("*install*")
        if path.is_file() and path.suffix in {".sh", ".ps1", ".py", ".bat"}
    ]
    if bespoke:
        fail("bespoke installer present: " + ", ".join(map(str, bespoke)))


def check_runtime_boundary() -> None:
    missing = [relative for relative in REQUIRED_PAYLOAD if not (CANONICAL / relative).is_file()]
    if missing:
        fail("canonical skill payload is incomplete: " + ", ".join(missing))
    duplicates: list[Path] = []
    for path in ROOT.rglob("SKILL.md"):
        text = path.read_text(encoding="utf-8")
        if "name: decision-engineering" in text and path.resolve() != (CANONICAL / "SKILL.md").resolve():
            duplicates.append(path.relative_to(ROOT))
    if duplicates:
        fail("duplicate skill authorities: " + ", ".join(map(str, duplicates)))

    for path in (CANONICAL / "scripts").glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        imports = {
            node.names[0].name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import) and node.names
        }
        imports.update(
            node.module.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        )
        forbidden = imports & FORBIDDEN_IMPORTS
        if forbidden:
            fail(f"runtime network import in {path.relative_to(ROOT)}: {sorted(forbidden)}")


def check_platform_matrix() -> None:
    workflow = ROOT / ".github" / "workflows" / "validate.yml"
    if not workflow.is_file():
        fail("platform validation workflow is missing")
    text = workflow.read_text(encoding="utf-8")
    missing = [runner for runner in REQUIRED_RUNNERS if runner not in text]
    if missing:
        fail("validation workflow omits runners: " + ", ".join(missing))
    if "scripts/validate_package.py" not in text:
        fail("validation workflow does not run the package validator")


def main() -> int:
    generated = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_manifests.py"), "--check"],
        cwd=ROOT,
        text=True,
    )
    if generated.returncode:
        return generated.returncode

    check_identity_and_metadata()
    check_documentation()
    check_runtime_boundary()
    check_platform_matrix()

    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        text=True,
    )
    if tests.returncode:
        return tests.returncode
    print("validate_package: package acceptance checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
