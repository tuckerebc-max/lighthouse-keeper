"""Exercise package validation at its command-line boundary."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="lighthouse-validation-")
        self.addCleanup(temporary.cleanup)
        self.workspace = Path(temporary.name)
        self.package = self.workspace / "package with spaces"
        shutil.copytree(
            ROOT,
            self.package,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"),
        )

    def run_validator(self):
        return subprocess.run(
            [sys.executable, "-B", str(self.package / "scripts/validate_package.py")],
            cwd=self.workspace,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def set_reference(self, value):
        path = self.package / "manifest.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["references"][0] = value
        path.write_text(json.dumps(manifest), encoding="utf-8")

    def assert_rejected(self, result, context):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("package validation failed", result.stdout)
        self.assertIn(context, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_package_from_another_working_directory(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS lighthouse-keeper package", result.stdout)

    def test_rejects_manifest_reference_outside_package(self):
        (self.workspace / "external.md").write_text("External fixture.", encoding="utf-8")
        self.set_reference("../external.md")
        self.assert_rejected(self.run_validator(), "manifest references")

    def test_rejects_absolute_manifest_reference(self):
        external = self.workspace / "external.md"
        external.write_text("External fixture.", encoding="utf-8")
        self.set_reference(external.as_posix())
        self.assert_rejected(self.run_validator(), "manifest references")

    def test_rejects_windows_only_manifest_reference(self):
        self.set_reference("references\\operating-protocol.md")
        self.assert_rejected(self.run_validator(), "portable relative path")

    def test_reports_non_string_manifest_reference(self):
        self.set_reference(7)
        self.assert_rejected(self.run_validator(), "manifest references")

    def test_rejects_missing_metadata_icon(self):
        (self.package / "assets/icon.svg").unlink()
        self.assert_rejected(self.run_validator(), "OpenAI metadata icon_small")

    def test_rejects_metadata_icon_outside_package(self):
        (self.workspace / "external.svg").write_text("<svg/>", encoding="utf-8")
        path = self.package / "agents/openai.yaml"
        metadata = yaml.safe_load(path.read_text(encoding="utf-8"))
        metadata["interface"]["icon_small"] = "../external.svg"
        path.write_text(yaml.safe_dump(metadata), encoding="utf-8")
        self.assert_rejected(self.run_validator(), "OpenAI metadata icon_small")


if __name__ == "__main__":
    unittest.main()
