"""Basic tests that do not require Django."""

import os
import unittest

import toml

from nautobot_plugin_w_rrm import __version__ as project_version


class TestVersion(unittest.TestCase):
    """Test Version is the same."""

    @staticmethod
    def convert_version(version):
        """Convert between Python's versioning format to semantic versioning."""
        # Convert Python's pre-release format to semantic versioning
        if "alpha" in version:
            return version
        if "a" in version:
            return version.replace("a", "-alpha.")

    def test_version(self):
        """Verify that pyproject.toml version is the same as the version specified in the package."""
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        poetry_version_raw = toml.load(os.path.join(parent_path, "pyproject.toml"))["tool"]["poetry"]["version"]

        # Convert both versions to a consistent format before comparing
        poetry_version = self.convert_version(poetry_version_raw)
        project_version_converted = self.convert_version(project_version)

        self.assertEqual(project_version_converted, poetry_version)
