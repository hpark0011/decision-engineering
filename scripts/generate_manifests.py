#!/usr/bin/env python3
"""Generate host plugin manifests from one package metadata source."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "package" / "metadata.json"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


def encoded(value: object) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def projections(metadata: dict[str, object]) -> dict[Path, str]:
    common = {
        "name": metadata["name"],
        "version": metadata["version"],
        "description": metadata["description"],
        "author": metadata["author"],
        "homepage": metadata["homepage"],
        "repository": metadata["repository"],
        "license": metadata["license"],
        "keywords": metadata["keywords"],
    }
    portable = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        **common,
    }
    claude = {
        "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
        **common,
        "displayName": "Decision Engineering",
        "skills": "./skills/",
    }
    codex = {
        **common,
        "skills": "./skills/",
        "interface": {
            "displayName": "Decision Engineering",
            "shortDescription": "Maintain authoritative decision ledgers.",
            "longDescription": "Route requirements to explicit decisions, trace authoritative facts, and validate intent against behavior.",
            "developerName": "hpark0011",
            "category": "Productivity",
            "capabilities": ["Local", "Write"],
            "defaultPrompt": "Use Decision Engineering to route this requirement through the decision ledger.",
        },
    }
    claude_marketplace = {
        "name": metadata["name"],
        "owner": metadata["author"],
        "metadata": {
            "description": metadata["description"],
            "version": metadata["version"],
        },
        "plugins": [{
            "name": metadata["name"],
            "description": metadata["description"],
            "author": metadata["author"],
            "homepage": metadata["homepage"],
            "tags": metadata["keywords"],
            "source": "./",
        }],
    }
    codex_marketplace = {
        "name": metadata["name"],
        "interface": {"displayName": "Decision Engineering"},
        "plugins": [{
            "name": metadata["name"],
            "source": {"source": "local", "path": "./"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Coding",
        }],
    }
    return {
        ROOT / "VERSION": f"{metadata['version']}\n",
        ROOT / "plugin.json": encoded(portable),
        ROOT / ".claude-plugin" / "plugin.json": encoded(claude),
        ROOT / ".claude-plugin" / "marketplace.json": encoded(claude_marketplace),
        ROOT / ".codex-plugin" / "plugin.json": encoded(codex),
        ROOT / ".agents" / "plugins" / "marketplace.json": encoded(codex_marketplace),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    version = metadata.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        print("generate_manifests: metadata version is not strict semver", file=sys.stderr)
        return 1
    if metadata.get("name") != "decision-engineering":
        print("generate_manifests: package name must be decision-engineering", file=sys.stderr)
        return 1
    if not (ROOT / "skills" / "decision-engineering" / "SKILL.md").is_file():
        print("generate_manifests: canonical skill is missing", file=sys.stderr)
        return 1
    stale: list[str] = []
    for path, content in projections(metadata).items():
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            if path.is_file() and path.read_text(encoding="utf-8") == content:
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        print("generate_manifests: stale generated files: " + ", ".join(stale), file=sys.stderr)
        return 1
    print("generate_manifests: projections are current" if args.check else "generate_manifests: generated host manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
