import sys
import pytest
from event_plugin_system import EventPluginSystem as EventSystem
from copy import copy

EXAMPLE_PLUGINS_ROOT = "example_plugins"

@pytest.fixture
def init_events():
    # XXX cleanup use Path 
    return EventSystem(plugin_dir=EXAMPLE_PLUGINS_ROOT + "/basic",
                       init_kwargs=dict(example="example"))

def test_kwarg(init_events):
    results = {}

    init_events("test_kwarg", results=results) 

    results['test_kwarg'] == "example"
