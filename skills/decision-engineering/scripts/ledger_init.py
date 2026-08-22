#!/usr/bin/env python3
"""Initialize the smallest valid Markdown decision-ledger directory."""

from pathlib import Path
import shutil
import sys

from ledger_lib import render_graph, render_index
from installation_guard import assert_single_authority, is_within


LOG_HEADER = """# Decision log

Append semantic creates, edits, renames, supersessions, retirements, restorations, deletions, and schema changes. Use Git for textual history.
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: ledger_init.py <ledger-dir>", file=sys.stderr)
        return 2
    ledger_dir = Path(sys.argv[1]).resolve()
    try:
        project_root = assert_single_authority(ledger_dir)
    except (RuntimeError, ValueError) as error:
        print(f"ledger_init: {error}", file=sys.stderr)
        return 1
    if not is_within(ledger_dir, project_root):
        print(f"ledger_init: ledger must stay inside project root {project_root}", file=sys.stderr)
        return 1
    schema_source = Path(__file__).resolve().parent.parent / "assets" / "decision-ledger" / "SCHEMA.md"
    if ledger_dir.exists() and any(ledger_dir.iterdir()):
        required = [ledger_dir / name for name in ("SCHEMA.md", "index.md", "log.md", "decisions")]
        if all(path.exists() for path in required):
            print(f"ledger_init: existing ledger preserved at {ledger_dir}")
            return 0
        print(f"ledger_init: refusing to overwrite non-empty directory {ledger_dir}", file=sys.stderr)
        return 1
    ledger_dir.mkdir(parents=True, exist_ok=True)
    (ledger_dir / "decisions").mkdir(exist_ok=True)
    (ledger_dir / "generated").mkdir(exist_ok=True)
    shutil.copyfile(schema_source, ledger_dir / "SCHEMA.md")
    (ledger_dir / "log.md").write_text(LOG_HEADER, encoding="utf-8")
    (ledger_dir / "index.md").write_text(render_index([]), encoding="utf-8")
    (ledger_dir / "generated" / "graph.mmd").write_text(render_graph([]), encoding="utf-8")
    print(f"ledger_init: initialized {ledger_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
