import sys
import pytest
from event_plugin_system import EventPluginSystemAsync as EventSystem
from copy import copy
import pytest


EXAMPLE_PLUGINS_ROOT = "example_plugins"

@pytest.fixture
def async_events():
    # XXX cleanup use Path 
    return EventSystem(plugin_dir=EXAMPLE_PLUGINS_ROOT + "/basic_async")

@pytest.mark.asyncio
async def test_init(async_events):
    return await async_events("start")

@pytest.mark.asyncio
async def test_arg_pass(async_events):
    return await async_events("arg", arg="test") 

# results need to be provided via a mutable, safe object eg queue
# or a destination URI for the handler to send results to
# most results should somehow use the plugin_name as the key
# unless each plugin does a queue.get() or similar 
@pytest.mark.asyncio
async def test_arg_pass2(async_events):
    x = "test"
    results = {}
    await async_events("arg_pass2", arg="test", results=results) 

    # check if the double plugin duplicated the arg
    # its important to avoid conflicts, the plugin sets the key below
    # using its plugin name as key: results[self.plugin_name] 
    results['double'] == 'testtest'
