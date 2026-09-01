#!/usr/bin/env python3
"""Allocate a stable decision ID and create a schema-valid editing template."""

from pathlib import Path
import json
import re
import sys

from ledger_lib import slugify
from installation_guard import assert_single_authority

TEMPLATE = """---
status: active
domain: <domain>
id: {decision_id}
title: {title_json}
---

## Requirement

<Outcome that must become true.>

## Question

<Exact uncertainty resolved?>

## Input facts

- `<fact.name>`
  - Kind: root
  - Authority: <external-authority>

## Invariants

- <What must never become false.>

## Policy

<Rule mapping the input facts to the output fact.>

## Output fact

- Name: `<output.fact>`
- Meaning: <One independently decidable proposition.>
- Shape: <Value or structured shape.>
- Atomicity: <Why no part can vary independently.>

## Enforcement

<Boundary obligation that can reject or commit the action.>

## Consumers

- <Known UI, API, worker, agent, report, or downstream decision that reads the output fact.>

## Verification

- <Exercise each meaningful policy branch.>
- <Prove the invariant at the enforcement boundary.>
"""


def main() -> int:
    if len(sys.argv) != 3:
        print('usage: ledger_new.py <ledger-dir> "Determine example"', file=sys.stderr)
        return 2
    ledger_dir = Path(sys.argv[1]).resolve()
    try:
        assert_single_authority(ledger_dir)
    except (RuntimeError, ValueError) as error:
        print(f"ledger_new: {error}", file=sys.stderr)
        return 1
    decision_dir = ledger_dir / "decisions"
    if not decision_dir.is_dir() or not (ledger_dir / "SCHEMA.md").is_file():
        print(f"ledger_new: {ledger_dir} is not an initialized decision ledger", file=sys.stderr)
        return 1
    title = " ".join(sys.argv[2].split())
    existing_ids = []
    for path in decision_dir.glob("D*.md"):
        match = re.match(r"D(\d{3,})-", path.name)
        if match:
            existing_ids.append(int(match.group(1)))
    next_number = max(existing_ids, default=0) + 1
    decision_id = f"D{next_number:03d}"
    path = decision_dir / f"{decision_id}-{slugify(title)}.md"
    path.write_text(
        TEMPLATE.format(
            decision_id=decision_id,
            title_json=json.dumps(title, ensure_ascii=False),
        ),
        encoding="utf-8",
    )
    print(path)
    print(f"ledger_new: fill every placeholder, append a create entry for {decision_id}, render, and lint")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
