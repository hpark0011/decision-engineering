#!/usr/bin/env python3
"""Shared parser and deterministic renderers for Markdown decision ledgers."""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import re
from typing import Dict, List, Optional, Sequence, Tuple
import unicodedata


REQUIRED_HEADINGS = [
    "Requirement",
    "Question",
    "Input facts",
    "Invariants",
    "Policy",
    "Output fact",
    "Enforcement",
    "Consumers",
    "Verification",
]

SECTION_RE = re.compile(r"^## ([^\n]+?)\s*$", re.MULTILINE)
FACT_RE = re.compile(r"(?m)^- `([a-z][a-z0-9]*(?:[.-][a-z0-9]+)*)`\s*$")
FIELD_RE_TEMPLATE = r"(?m)^- {field}:\s*(.+?)\s*$"
FACT_NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*$")
DECISION_ID_RE = re.compile(r"^D\d{3,}$")
PLACEHOLDER_RE = re.compile(r"<[^>]+>|\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)
REQUIRED_FRONTMATTER = ("status", "domain", "id", "title")
ALLOWED_FRONTMATTER = set(REQUIRED_FRONTMATTER) | {"superseded_by"}


@dataclass(frozen=True)
class Issue:
    code: str
    message: str
    path: Optional[Path] = None
    warning: bool = False

    def format(self) -> str:
        level = "WARNING" if self.warning else "ERROR"
        location = f" {self.path}:" if self.path else ""
        return f"{level} {self.code}:{location} {self.message}"


@dataclass(frozen=True)
class InputFact:
    name: str
    kind: str
    authority: Optional[str] = None
    producer: Optional[str] = None


@dataclass
class Decision:
    path: Path
    id: str
    title: str
    status: str
    domain: str
    superseded_by: Optional[str]
    sections: Dict[str, str]
    inputs: List[InputFact] = field(default_factory=list)
    output_name: str = ""
    output_meaning: str = ""
    output_shape: str = ""
    output_atomicity: str = ""
    consumers: List[str] = field(default_factory=list)
    verification: List[str] = field(default_factory=list)

    @property
    def question(self) -> str:
        return collapse(self.sections.get("Question", ""))


def collapse(text: str) -> str:
    return " ".join(text.split())


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKC", title).casefold()
    slug = re.sub(r"[^\w]+", "-", normalized, flags=re.UNICODE).strip("-")
    return slug.replace("_", "-") or "untitled-decision"


def parse_scalar(raw: str) -> Optional[str]:
    value = raw.strip()
    if not value:
        return None
    if value.startswith('"') and value.endswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, str) and parsed else None
    if value.startswith("'") and value.endswith("'"):
        parsed = value[1:-1].replace("''", "'")
        return parsed or None
    if value[0] in "\"'" or value[-1] in "\"'":
        return None
    if value[0] in "[{&*!|>@`" or value in {"null", "~"}:
        return None
    return value


def parse_frontmatter(text: str, path: Path) -> Tuple[Dict[str, str], str, List[Issue]]:
    issues: List[Issue] = []
    if not text.startswith("---\n"):
        return {}, text, [Issue("E101", "decision must begin with YAML frontmatter", path)]
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, [Issue("E101", "decision frontmatter is not closed with `---`", path)]
    raw_frontmatter = text[4:end]
    body = text[end + 5:]
    values: Dict[str, str] = {}
    for line_number, line in enumerate(raw_frontmatter.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_]*)\s*:\s*(.*?)\s*", line)
        if not match:
            issues.append(Issue("E101", f"invalid frontmatter line {line_number}: `{line}`", path))
            continue
        key, raw_value = match.groups()
        if key in values:
            issues.append(Issue("E101", f"frontmatter key `{key}` occurs more than once", path))
            continue
        value = parse_scalar(raw_value)
        if value is None:
            issues.append(Issue("E101", f"frontmatter key `{key}` must have one scalar value", path))
            continue
        values[key] = value
        if key not in ALLOWED_FRONTMATTER:
            issues.append(Issue("E101", f"unsupported frontmatter key `{key}`", path))
    for key in REQUIRED_FRONTMATTER:
        if key not in values:
            issues.append(Issue("E101", f"frontmatter must declare `{key}`", path))
    return values, body, issues


def extract_fields(text: str, field_name: str) -> List[str]:
    return [
        match.strip()
        for match in re.findall(FIELD_RE_TEMPLATE.format(field=re.escape(field_name)), text)
    ]


def strip_ticks(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def parse_bullets(text: str) -> List[str]:
    return [collapse(item) for item in re.findall(r"(?m)^- (.+?)\s*$", text)]


def parse_input_facts(text: str, path: Path) -> Tuple[List[InputFact], List[Issue]]:
    matches = list(FACT_RE.finditer(text))
    facts: List[InputFact] = []
    issues: List[Issue] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end():end]
        name = match.group(1)
        kind_match = re.search(r"(?m)^\s{2,}- Kind:\s*(root|derived)\s*$", block)
        authority_match = re.search(r"(?m)^\s{2,}- Authority:\s*(.+?)\s*$", block)
        producer_match = re.search(r"(?m)^\s{2,}- Produced by:\s*(D\d{3,})(?:\s+—.*)?\s*$", block)
        if not kind_match:
            issues.append(Issue("E107", f"input fact `{name}` must declare Kind: root or derived", path))
            continue
        kind = kind_match.group(1)
        authority = authority_match.group(1).strip() if authority_match else None
        producer = producer_match.group(1) if producer_match else None
        if kind == "root" and not authority:
            issues.append(Issue("E108", f"root fact `{name}` must declare one Authority", path))
        if kind == "root" and producer:
            issues.append(Issue("E109", f"root fact `{name}` must not declare Produced by", path))
        if kind == "derived" and not producer:
            issues.append(Issue("E110", f"derived fact `{name}` must declare Produced by: Dxxx", path))
        if kind == "derived" and authority:
            issues.append(Issue("E111", f"derived fact `{name}` must not declare Authority", path))
        facts.append(InputFact(name=name, kind=kind, authority=authority, producer=producer))
    if text.strip() and not matches:
        issues.append(Issue("E106", "Input facts must use schema bullet records", path))
    return facts, issues


def parse_decision(path: Path) -> Tuple[Optional[Decision], List[Issue]]:
    text = path.read_text(encoding="utf-8")
    metadata, body, issues = parse_frontmatter(text, path)
    if any(key not in metadata for key in REQUIRED_FRONTMATTER):
        return None, issues
    decision_id = metadata.get("id", "")
    title = metadata.get("title", "")
    status = metadata.get("status", "")
    domain = metadata.get("domain", "")
    superseded_by = metadata.get("superseded_by")

    if decision_id and not DECISION_ID_RE.fullmatch(decision_id):
        issues.append(Issue("E112", f"frontmatter id `{decision_id}` must match Dxxx", path))
        return None, issues
    if title and PLACEHOLDER_RE.search(title):
        issues.append(Issue("E112", "frontmatter title contains a placeholder", path))
    if domain and PLACEHOLDER_RE.search(domain):
        issues.append(Issue("E112", "frontmatter domain contains a placeholder", path))
    if status not in {"active", "superseded", "retired"}:
        issues.append(Issue("E112", "frontmatter status must be active, superseded, or retired", path))
    if superseded_by and not DECISION_ID_RE.fullmatch(superseded_by):
        issues.append(Issue("E113", "frontmatter superseded_by must match Dxxx", path))
    if status == "superseded" and not superseded_by:
        issues.append(Issue("E113", "superseded decision must declare frontmatter superseded_by", path))
    if status != "superseded" and superseded_by:
        issues.append(Issue("E114", "only a superseded decision may declare frontmatter superseded_by", path))

    if re.search(r"(?m)^#\s+", body):
        issues.append(Issue("E120", "body must not repeat decision identity as an H1 heading", path))
    repeated_metadata = re.findall(r"(?im)^(?:status|domain|id|title):\s*.+$", body)
    if repeated_metadata:
        issues.append(Issue("E121", "body must not repeat status, domain, id, or title metadata", path))

    section_matches = list(SECTION_RE.finditer(body))
    headings = [match.group(1).strip() for match in section_matches]
    for heading in headings:
        if heading not in REQUIRED_HEADINGS:
            issues.append(Issue("E122", f"unsupported decision section `## {heading}`", path))
    for heading in REQUIRED_HEADINGS:
        count = headings.count(heading)
        if count != 1:
            issues.append(Issue("E102", f"heading `## {heading}` must occur exactly once; found {count}", path))
    required_positions = [headings.index(h) for h in REQUIRED_HEADINGS if h in headings]
    if required_positions != sorted(required_positions):
        issues.append(Issue("E103", "required headings are out of schema order", path))

    sections: Dict[str, str] = {}
    for index, match in enumerate(section_matches):
        end = section_matches[index + 1].start() if index + 1 < len(section_matches) else len(body)
        sections[match.group(1).strip()] = body[match.end():end].strip()
    for heading in REQUIRED_HEADINGS:
        body = sections.get(heading, "")
        if not body:
            issues.append(Issue("E104", f"section `{heading}` must not be empty", path))
        elif PLACEHOLDER_RE.search(body):
            issues.append(Issue("E105", f"section `{heading}` contains a placeholder", path))

    inputs, input_issues = parse_input_facts(sections.get("Input facts", ""), path)
    issues.extend(input_issues)

    output = sections.get("Output fact", "")
    output_fields = {
        field_name: extract_fields(output, field_name)
        for field_name in ("Name", "Meaning", "Shape", "Atomicity")
    }
    output_name = strip_ticks(output_fields["Name"][0]) if output_fields["Name"] else ""
    output_meaning = output_fields["Meaning"][0] if output_fields["Meaning"] else ""
    output_shape = output_fields["Shape"][0] if output_fields["Shape"] else ""
    output_atomicity = output_fields["Atomicity"][0] if output_fields["Atomicity"] else ""
    for field_name, value in (
        ("Name", output_name),
        ("Meaning", output_meaning),
        ("Shape", output_shape),
        ("Atomicity", output_atomicity),
    ):
        if len(output_fields[field_name]) != 1:
            issues.append(Issue("E115", f"Output fact must declare `{field_name}` exactly once; found {len(output_fields[field_name])}", path))
        elif PLACEHOLDER_RE.search(value):
            issues.append(Issue("E116", f"Output fact `{field_name}` contains a placeholder", path))
    if output_name and not FACT_NAME_RE.fullmatch(output_name):
        issues.append(Issue("E117", f"output fact name `{output_name}` is not lowercase dot/hyphen notation", path))

    consumers = parse_bullets(sections.get("Consumers", ""))
    verification = parse_bullets(sections.get("Verification", ""))
    if not consumers:
        issues.append(Issue("W101", "decision declares no bullet-list consumers", path, warning=True))
    if not verification:
        issues.append(Issue("E119", "Verification must contain at least one bullet obligation", path))

    decision = Decision(
        path=path,
        id=decision_id,
        title=title,
        status=status,
        domain=domain,
        superseded_by=superseded_by,
        sections=sections,
        inputs=inputs,
        output_name=output_name,
        output_meaning=output_meaning,
        output_shape=output_shape,
        output_atomicity=output_atomicity,
        consumers=consumers,
        verification=verification,
    )
    return decision, issues


def load_decisions(ledger_dir: Path) -> Tuple[List[Decision], List[Issue]]:
    decision_dir = ledger_dir / "decisions"
    if not decision_dir.is_dir():
        return [], [Issue("E001", "missing decisions/ directory", decision_dir)]
    decisions: List[Decision] = []
    issues: List[Issue] = []
    for path in sorted(decision_dir.glob("*.md")):
        decision, parsed_issues = parse_decision(path)
        issues.extend(parsed_issues)
        if decision:
            decisions.append(decision)
    return decisions, issues


def escape_cell(value: str) -> str:
    return collapse(value).replace("|", "\\|")


def render_index(decisions: Sequence[Decision]) -> str:
    lines = [
        "# Decision index",
        "",
        "Generated from `decisions/*.md`. Do not edit by hand.",
        "",
        "| ID | Decision | Produces | Reads | Domain | Status |",
        "|---|---|---|---|---|---|",
    ]
    for decision in sorted(decisions, key=lambda item: int(item.id[1:])):
        inputs = ", ".join(f"`{fact.name}`" for fact in decision.inputs) or "—"
        lines.append(
            "| [{id}](decisions/{filename}) | {title} | `{output}` | {inputs} | {domain} | {status} |".format(
                id=decision.id,
                filename=decision.path.name,
                title=escape_cell(decision.title),
                output=decision.output_name,
                inputs=inputs,
                domain=escape_cell(decision.domain),
                status=decision.status,
            )
        )
    lines.extend(["", "## Routing", "", "Search this file by output fact, question, input fact, consumer, domain, status, or requirement terms in the linked decision record.", ""])
    return "\n".join(lines)


def node_id(prefix: str, value: str) -> str:
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]
    return f"{prefix}_{digest}"


def mermaid_label(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', "\\\"")


def render_graph(decisions: Sequence[Decision]) -> str:
    lines = ["flowchart LR"]
    roots: Dict[str, str] = {}
    for decision in decisions:
        for fact in decision.inputs:
            if fact.kind == "root" and fact.authority:
                roots.setdefault(fact.name, fact.authority)

    for fact_name, authority in sorted(roots.items()):
        authority_id = node_id("a", authority)
        fact_id = node_id("f", fact_name)
        lines.append(f'  {authority_id}[["{mermaid_label(authority)}"]]')
        lines.append(f'  {fact_id}(("{mermaid_label(fact_name)}"))')
        lines.append(f"  {authority_id} --> {fact_id}")

    for decision in sorted(decisions, key=lambda item: int(item.id[1:])):
        decision_node = f"d_{decision.id.lower()}"
        output_node = node_id("f", decision.output_name)
        lines.append(f'  {decision_node}["{decision.id}: {mermaid_label(decision.title)}"]')
        lines.append(f'  {output_node}(("{mermaid_label(decision.output_name)}"))')
        for fact in decision.inputs:
            lines.append(f"  {node_id('f', fact.name)} --> {decision_node}")
        lines.append(f"  {decision_node} --> {output_node}")

    lines.extend([
        "  classDef decision fill:#fff4cc,stroke:#8a6d1d,stroke-width:1px;",
        "  classDef fact fill:#e8f3ff,stroke:#326891,stroke-width:1px;",
        "  classDef authority fill:#f4e8ff,stroke:#704a8a,stroke-width:1px;",
    ])
    decision_nodes = [f"d_{decision.id.lower()}" for decision in decisions]
    fact_nodes = sorted({node_id("f", decision.output_name) for decision in decisions} | {node_id("f", fact.name) for decision in decisions for fact in decision.inputs})
    authority_nodes = sorted({node_id("a", authority) for authority in roots.values()})
    if decision_nodes:
        lines.append(f"  class {','.join(decision_nodes)} decision;")
    if fact_nodes:
        lines.append(f"  class {','.join(fact_nodes)} fact;")
    if authority_nodes:
        lines.append(f"  class {','.join(authority_nodes)} authority;")
    return "\n".join(lines) + "\n"
