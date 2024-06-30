import sys
import pytest
from event_plugin_system import EventPluginSystem as EventSystem
from copy import copy

EXAMPLE_PLUGINS_ROOT = "example_plugins"
#sys.path.append("../src")

@pytest.fixture
def basic_events():
    # XXX cleanup use Path 
    return EventSystem(plugin_dir=EXAMPLE_PLUGINS_ROOT + "/basic")

def test_init(basic_events):
    basic_events("start")

def test_arg_pass(basic_events):
    basic_events("arg", arg="test") 

# results need to be provided via a mutable, safe object eg queue
# or a destination URI for the handler to send results to
# most results should somehow use the plugin_name as the key
# unless each plugin does a queue.get() or similar 
def test_mutation(basic_events):
    x = "test"
    results = {}
    basic_events("test_mutation", arg="test", results=results) 

    # check if the double plugin duplicated the arg
    # its important to avoid conflicts, the plugin sets the key below
    # using its plugin name as key: results[self.plugin_name] 
    results['double'] == 'testtest'
