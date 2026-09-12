#!/usr/bin/env python3
"""Validate the self-contained Lighthouse Keeper candidate package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "README.md",
    "SKILL.md",
    "manifest.json",
    "agents/openai.yaml",
    "references/architecture-integration.md",
    "references/communication-templates.md",
    "references/evaluator.md",
    "references/exemplars.md",
    "references/operating-protocol.md",
    "references/role-specification.md",
    "references/signal-packet-schema.md",
    "schemas/package-manifest.schema.json",
    "schemas/signal-packet.schema.json",
    "scripts/validate_package.py",
    "tests/test_package.py",
    "examples/README.md",
    "examples/valid-signal-packet.json",
    "examples/held-no-material-signal.json",
    "requirements.txt",
}
FORBIDDEN_IDENTITY = re.compile("harbor" + "master", re.IGNORECASE)
FORBIDDEN_DEBRIS = re.compile(
    r"(^|/)(__pycache__|\.pytest_cache)(/|$)|\.(pyc|pyo|tmp|bak)$|(^|/)CHANGELOG\.md$",
    re.IGNORECASE,
)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_package_path(value: object, context: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value:
        fail(f"{context} must name a package file", errors)
        return
    relative = PurePosixPath(value)
    if (
        relative.is_absolute()
        or PureWindowsPath(value).drive
        or "\\" in value
        or ":" in value
        or ".." in relative.parts
    ):
        fail(f"{context} must use a portable relative path inside the package: {value}", errors)
        return
    try:
        target = (ROOT / value).resolve()
        if not target.is_relative_to(ROOT):
            fail(f"{context} resolves outside the package: {value}", errors)
        elif not target.is_file():
            fail(f"{context} points to missing file: {value}", errors)
    except (OSError, RuntimeError, ValueError) as exc:
        fail(f"{context} has an invalid path {value!r}: {exc}", errors)


def read_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}", errors)
        return None


def read_frontmatter(path: Path, errors: list[str]):
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}", errors)
        return None, ""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing or malformed", errors)
        return None, text
    try:
        return yaml.safe_load(match.group(1)), text
    except yaml.YAMLError as exc:
        fail(f"SKILL.md frontmatter is invalid YAML: {exc}", errors)
        return None, text


def main() -> int:
    errors: list[str] = []
    actual = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file()
    }
    for required in sorted(REQUIRED - actual):
        fail(f"missing required file: {required}", errors)
    for path in ROOT.rglob("*"):
        if FORBIDDEN_DEBRIS.search(path.relative_to(ROOT).as_posix()):
            fail(f"generated/cache/debris file present: {path.relative_to(ROOT)}", errors)
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml"}:
            try:
                if FORBIDDEN_IDENTITY.search(path.read_text(encoding="utf-8")):
                    fail(f"forbidden identity text present: {path.relative_to(ROOT)}", errors)
            except OSError as exc:
                fail(f"cannot scan {path.relative_to(ROOT)}: {exc}", errors)

    skill, skill_text = read_frontmatter(ROOT / "SKILL.md", errors)
    if isinstance(skill, dict):
        if set(skill) != {"name", "description"}:
            fail("SKILL.md frontmatter must contain only name and description", errors)
        if skill.get("name") != "lighthouse-keeper":
            fail("SKILL.md name must be lighthouse-keeper", errors)
        if not isinstance(skill.get("description"), str) or not skill["description"].strip():
            fail("SKILL.md description is missing", errors)
    for concept in ("Signal Packet", "warrant", "general communications", "route work"):
        if concept.lower() not in skill_text.lower():
            fail(f"SKILL.md is missing boundary/workflow concept: {concept}", errors)

    manifest = read_json(ROOT / "manifest.json", errors)
    package_schema = read_json(ROOT / "schemas/package-manifest.schema.json", errors)
    packet_schema = read_json(ROOT / "schemas/signal-packet.schema.json", errors)
    if isinstance(package_schema, dict):
        try:
            Draft202012Validator.check_schema(package_schema)
        except Exception as exc:  # pragma: no cover - defensive diagnostic
            fail(f"package manifest schema is invalid: {exc}", errors)
    if isinstance(packet_schema, dict):
        try:
            Draft202012Validator.check_schema(packet_schema)
        except Exception as exc:  # pragma: no cover - defensive diagnostic
            fail(f"Signal Packet schema is invalid: {exc}", errors)
    if isinstance(manifest, dict) and isinstance(package_schema, dict):
        errors.extend(
            f"manifest: {e.message}"
            for e in Draft202012Validator(package_schema, format_checker=FormatChecker()).iter_errors(manifest)
        )
        for field in ("$schema", "entrypoint", "role_specification", "references", "schemas", "examples"):
            values = manifest.get(field, [])
            if isinstance(values, str):
                values = [values]
            if isinstance(values, list):
                for rel in values:
                    validate_package_path(rel, f"manifest {field}", errors)

    if isinstance(packet_schema, dict):
        validator = Draft202012Validator(packet_schema, format_checker=FormatChecker())
        example_paths = sorted((ROOT / "examples").glob("*.json"))
        if len(example_paths) < 2:
            fail("expected at least two JSON examples", errors)
        for path in example_paths:
            example = read_json(path, errors)
            if isinstance(example, dict):
                errors.extend(
                    f"{path.relative_to(ROOT)}: {e.message}"
                    for e in validator.iter_errors(example)
                )

    metadata_path = ROOT / "agents/openai.yaml"
    try:
        metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        fail(f"invalid OpenAI metadata: {exc}", errors)
    else:
        interface = metadata.get("interface", {}) if isinstance(metadata, dict) else {}
        if interface.get("display_name") != "Lighthouse Keeper":
            fail("OpenAI metadata display_name must be Lighthouse Keeper", errors)
        prompt = interface.get("default_prompt", "")
        if "$lighthouse-keeper" not in prompt:
            fail("OpenAI metadata default_prompt must invoke $lighthouse-keeper", errors)
        if FORBIDDEN_IDENTITY.search(prompt):
            fail("OpenAI metadata contains forbidden identity text", errors)
        for field in ("icon_small", "icon_large"):
            if field in interface:
                validate_package_path(interface[field], f"OpenAI metadata {field}", errors)

    if errors:
        print("Lighthouse Keeper package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS lighthouse-keeper package identity, authority, schemas, examples, metadata, and debris checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
