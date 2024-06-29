import sys
import pytest
from event_plugin_system import EventPluginSystem as EventSystem
from copy import copy

EXAMPLE_PLUGINS = "example_plugins"
#sys.path.append("../src")

@pytest.fixture
def emit():
    return EventSystem(plugin_dir=EXAMPLE_PLUGINS)

def test_init(emit):
    emit("start")

def test_arg_pass(emit):
    emit("arg", arg="test") 

# results need to be provided via a mutable, safe object eg queue
# or a destination URI for the handler to send results to
# most results should somehow use the plugin_name as the key
# unless each plugin does a queue.get() or similar 
def test_arg_pass2(emit):
    x = "test"
    results = {}
    emit("arg_pass2", arg="test", results=results) 

    # check if the double plugin duplicated the arg
    # its important to avoid conflicts, the plugin sets the key below
    # using its plugin name as key: results[self.plugin_name] 
    results['double'] == 'testtest'
