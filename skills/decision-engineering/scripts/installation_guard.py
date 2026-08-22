#!/usr/bin/env python3
"""Resolve a project root and prevent competing Decision Engineering authorities."""

from __future__ import annotations

import os
from pathlib import Path
import sys


PROJECT_SKILL_PATHS = (
    Path("skills/decision-engineering"),
    Path(".agents/skills/decision-engineering"),
    Path(".claude/skills/decision-engineering"),
    Path(".cursor/skills/decision-engineering"),
)


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def project_root_for(path: Path) -> Path:
    resolved = path.resolve()
    workspace = Path(os.environ.get("DECISION_ENGINEERING_PROJECT_ROOT", Path.cwd())).resolve()
    project_root = workspace
    for candidate in (workspace, *workspace.parents):
        if (candidate / ".git").exists():
            project_root = candidate
            break
    if not is_within(resolved, project_root):
        raise ValueError(f"resolved path {resolved} is outside project root {project_root}")
    return project_root


def applicable_skill_roots(project_root: Path, current_skill_root: Path | None = None) -> list[Path]:
    roots: set[Path] = set()
    current = (current_skill_root or Path(__file__).resolve().parents[1]).resolve()
    if (current / "SKILL.md").is_file():
        roots.add(current)
    for relative in PROJECT_SKILL_PATHS:
        candidate = (project_root / relative).resolve()
        if (candidate / "SKILL.md").is_file():
            roots.add(candidate)
    extra = os.environ.get("DECISION_ENGINEERING_SKILL_ROOTS", "")
    for raw in filter(None, extra.split(os.pathsep)):
        candidate = Path(raw).resolve()
        if (candidate / "SKILL.md").is_file():
            roots.add(candidate)
    return sorted(roots)


def assert_single_authority(target: Path, current_skill_root: Path | None = None) -> Path:
    project_root = project_root_for(target)
    roots = applicable_skill_roots(project_root, current_skill_root)
    if len(roots) > 1:
        paths = "\n".join(f"  - {path}" for path in roots)
        raise RuntimeError(
            "duplicate Decision Engineering skill authorities detected:\n"
            f"{paths}\n"
            "Keep either the managed global plugin or one editable project copy, then retry."
        )
    return project_root


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) == 2 else Path.cwd()
    try:
        project_root = assert_single_authority(target)
    except (RuntimeError, ValueError) as error:
        print(f"installation_guard: {error}", file=sys.stderr)
        return 1
    print(f"installation_guard: one authority for {project_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
