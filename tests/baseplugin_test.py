import sys
import pytest
from event_plugin_system import EventPluginSystem as EventSystem
from copy import copy

EXAMPLE_PLUGINS_ROOT = "example_plugins"

@pytest.fixture
def events():
    return EventSystem(plugin_dir=EXAMPLE_PLUGINS_ROOT + "/baseplugin")

def test_init(events):
    events("start")

