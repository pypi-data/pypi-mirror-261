"""Verifies the plugin utilities work as expected"""

from typing import LiteralString

import pytest
from synodic_utilities.plugin import Plugin

from pytest_synodic.plugin import UnitTests


class MockPlugin(Plugin):
    """A mock plugin for testing"""


class TestPluginOverride(UnitTests[MockPlugin]):
    """Verifies the plugin utilities work as expected"""

    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[MockPlugin]:
        """A required testing hook that allows type generation

        Returns:
            The overridden provider type
        """
        return MockPlugin

    @pytest.fixture(name="plugin_group_name", scope="session")
    def fixture_plugin_group_name(self) -> LiteralString:
        """A required testing hook that allows plugin group name generation

        Returns:
            The plugin group name
        """

        return "plugin"
