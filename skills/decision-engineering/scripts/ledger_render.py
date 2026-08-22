#!/usr/bin/env python3
"""Render index.md and generated/graph.mmd from decision records."""

from pathlib import Path
import sys

from ledger_lib import load_decisions, render_graph, render_index
from installation_guard import assert_single_authority


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: ledger_render.py <ledger-dir>", file=sys.stderr)
        return 2
    ledger_dir = Path(sys.argv[1]).resolve()
    try:
        assert_single_authority(ledger_dir)
    except (RuntimeError, ValueError) as error:
        print(f"ledger_render: {error}", file=sys.stderr)
        return 1
    decisions, issues = load_decisions(ledger_dir)
    errors = [issue for issue in issues if not issue.warning]
    if errors:
        for issue in errors:
            print(issue.format(), file=sys.stderr)
        print("ledger_render: decision records are invalid; render aborted", file=sys.stderr)
        return 1
    (ledger_dir / "generated").mkdir(parents=True, exist_ok=True)
    (ledger_dir / "index.md").write_text(render_index(decisions), encoding="utf-8")
    (ledger_dir / "generated" / "graph.mmd").write_text(render_graph(decisions), encoding="utf-8")
    print(f"ledger_render: rendered {len(decisions)} decision(s)")
    print(ledger_dir / "index.md")
    print(ledger_dir / "generated" / "graph.mmd")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
