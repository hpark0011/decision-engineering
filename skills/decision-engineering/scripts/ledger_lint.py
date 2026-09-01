#!/usr/bin/env python3
"""Deterministically lint a Markdown Decision Engineering ledger."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
import sys
from typing import Dict, List, Set

from ledger_lib import Decision, Issue, load_decisions, render_index, slugify


def find_cycles(edges: Dict[str, Set[str]]) -> List[List[str]]:
    cycles: List[List[str]] = []
    state: Dict[str, int] = {}
    stack: List[str] = []

    def visit(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for neighbor in sorted(edges.get(node, set())):
            if state.get(neighbor, 0) == 0:
                visit(neighbor)
            elif state.get(neighbor) == 1 and neighbor in stack:
                start = stack.index(neighbor)
                cycle = stack[start:] + [neighbor]
                if cycle not in cycles:
                    cycles.append(cycle)
        stack.pop()
        state[node] = 2

    for node in sorted(edges):
        if state.get(node, 0) == 0:
            visit(node)
    return cycles


def lint(ledger_dir: Path) -> List[Issue]:
    issues: List[Issue] = []
    for required in ("SCHEMA.md", "index.md", "log.md"):
        path = ledger_dir / required
        if not path.is_file():
            issues.append(Issue("E001", f"missing required file {required}", path))
    graph_path = ledger_dir / "generated" / "graph.mmd"
    if not graph_path.is_file():
        issues.append(Issue("E001", "missing generated/graph.mmd; run ledger_render.py", graph_path))

    decisions, parse_issues = load_decisions(ledger_dir)
    issues.extend(parse_issues)
    by_id: Dict[str, Decision] = {}
    by_output: Dict[str, Decision] = {}
    root_authorities: Dict[str, str] = {}

    for decision in decisions:
        if decision.id in by_id:
            issues.append(Issue("E201", f"duplicate decision ID {decision.id}", decision.path))
        else:
            by_id[decision.id] = decision
        expected_filename = f"{decision.id}-{slugify(decision.title)}.md"
        if decision.path.name != expected_filename:
            issues.append(Issue("E202", f"filename must be `{expected_filename}` from frontmatter id and title", decision.path))
        if decision.output_name:
            if decision.output_name in by_output:
                issues.append(Issue("E203", f"output fact `{decision.output_name}` also produced by {by_output[decision.output_name].id}", decision.path))
            else:
                by_output[decision.output_name] = decision
        for fact in decision.inputs:
            if fact.kind == "root" and fact.authority:
                previous = root_authorities.get(fact.name)
                if previous and previous != fact.authority:
                    issues.append(Issue("E205", f"root fact `{fact.name}` has conflicting authorities `{previous}` and `{fact.authority}`", decision.path))
                root_authorities[fact.name] = fact.authority

    edges: Dict[str, Set[str]] = defaultdict(set)
    for decision in decisions:
        if decision.superseded_by and decision.superseded_by not in by_id:
            issues.append(Issue("E206", f"frontmatter superseded_by target {decision.superseded_by} does not exist", decision.path))
        if decision.output_name in root_authorities:
            issues.append(Issue("E207", f"fact `{decision.output_name}` is both derived and externally authoritative", decision.path))
        for fact in decision.inputs:
            if fact.name == decision.output_name:
                issues.append(Issue("E208", f"decision consumes its own current output `{fact.name}`", decision.path))
            if fact.kind == "derived":
                producer = by_output.get(fact.name)
                if not producer:
                    issues.append(Issue("E209", f"derived input `{fact.name}` has no producing decision", decision.path))
                elif producer.id != fact.producer:
                    issues.append(Issue("E210", f"derived input `{fact.name}` says {fact.producer}, but is produced by {producer.id}", decision.path))
                if fact.producer and fact.producer not in by_id:
                    issues.append(Issue("E211", f"Produced by target {fact.producer} does not exist", decision.path))
                if fact.producer:
                    edges[fact.producer].add(decision.id)
        for consumer in decision.consumers:
            for referenced in re.findall(r"\bD\d{3,}\b", consumer):
                if referenced not in by_id:
                    issues.append(Issue("E212", f"consumer references missing decision {referenced}", decision.path))

    for cycle in find_cycles(edges):
        issues.append(Issue("E213", f"same-evaluation dependency cycle: {' -> '.join(cycle)}"))

    log_path = ledger_dir / "log.md"
    if log_path.is_file():
        log_text = log_path.read_text(encoding="utf-8")
        for decision in decisions:
            history = re.search(
                rf"(?m)^## \\?\[\d{{4}}-\d{{2}}-\d{{2}}\\?\] (?:create|restore|schema-change|schema-migration) \| {re.escape(decision.id)} \|",
                log_text,
            )
            if not history:
                issues.append(Issue("E214", f"log.md lacks create/restore/schema-change history for {decision.id}", log_path))

    index_path = ledger_dir / "index.md"
    if index_path.is_file():
        expected = render_index(decisions)
        actual = index_path.read_text(encoding="utf-8")
        if actual != expected:
            issues.append(Issue("E215", "index.md is stale; run ledger_render.py", index_path))

    if decisions and all(decision.status != "active" for decision in decisions):
        issues.append(Issue("W201", "ledger contains no active decisions", warning=True))
    if not decisions:
        issues.append(Issue("W202", "ledger contains no decision records", warning=True))
    return issues


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: ledger_lint.py <ledger-dir>", file=sys.stderr)
        return 2
    ledger_dir = Path(sys.argv[1]).resolve()
    issues = lint(ledger_dir)
    errors = [issue for issue in issues if not issue.warning]
    warnings = [issue for issue in issues if issue.warning]
    for issue in sorted(issues, key=lambda item: (item.warning, item.code, str(item.path or ""), item.message)):
        print(issue.format())
    decisions, _ = load_decisions(ledger_dir)
    outputs = len({decision.output_name for decision in decisions if decision.output_name})
    print(f"ledger_lint: {len(errors)} error(s), {len(warnings)} warning(s)")
    print(f"decisions: {len(decisions)} · output facts: {outputs}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
