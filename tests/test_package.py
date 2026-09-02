import json
import re
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


class PackageTest(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.packet_schema = json.loads(
            (ROOT / "schemas" / "signal-packet.schema.json").read_text(encoding="utf-8")
        )

    def test_identity_and_authority(self):
        self.assertEqual(self.manifest["package_id"], "lighthouse-keeper")
        self.assertEqual(self.manifest["skill_id"], "lighthouse-keeper")
        self.assertEqual(self.manifest["role_id"], "navy-yard.lighthouse-keeper")
        self.assertEqual(self.manifest["display_name"], "Lighthouse Keeper")
        for key in (
            "may_publish",
            "may_promote",
            "may_route",
            "may_assign",
            "may_allocate_capacity",
            "may_mutate_source_records",
        ):
            self.assertFalse(self.manifest["authority"][key])

    def test_skill_frontmatter_and_metadata_agree(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match)
        frontmatter = yaml.safe_load(match.group(1))
        self.assertEqual(set(frontmatter), {"name", "description"})
        self.assertEqual(frontmatter["name"], "lighthouse-keeper")
        metadata = yaml.safe_load((ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8"))
        self.assertEqual(metadata["interface"]["display_name"], "Lighthouse Keeper")
        self.assertIn("$lighthouse-keeper", metadata["interface"]["default_prompt"])

    def test_manifest_references_exist(self):
        for field in ("role_specification", "references", "schemas", "examples"):
            values = self.manifest[field]
            if isinstance(values, str):
                values = [values]
            for value in values:
                self.assertTrue((ROOT / value).is_file(), value)

    def test_examples_validate(self):
        validator = Draft202012Validator(self.packet_schema, format_checker=FormatChecker())
        examples = sorted((ROOT / "examples").glob("*.json"))
        self.assertGreaterEqual(len(examples), 2)
        for path in examples:
            with self.subTest(path=path.name):
                value = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(list(validator.iter_errors(value)), [])

    def test_no_conflicting_identity_or_tracked_debris(self):
        forbidden = re.compile("harbor" + "master", re.IGNORECASE)
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix.lower() in {".pyc", ".pyo"}:
                continue
            relative = path.relative_to(ROOT).as_posix()
            self.assertNotRegex(relative, r"\.(tmp|bak)$")
            if path.suffix.lower() in {".md", ".json", ".yaml", ".yml"}:
                self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), relative)


if __name__ == "__main__":
    unittest.main()
