# Event System

A simple plugin event system designed to handle events with plugins dynamically loaded from a specified directory.

## Features

- Load plugins from a directory.
- Emit events that plugins can handle.
- Support for both synchronous and asynchronous event handling.

## Installation

To install the package, use:

```bash
pip install event-plugin-system
```

## Usage

```python

from event_plugin_system import EventPluginSystem

# Specify the directory containing your plugins
plugin_dir = "path/to/your/plugins"

# Initialize the event system
event_system = EventPluginSystem(plugin_dir=plugin_dir)

# Emit an event
event_system.emit("start")

# Emit an event with arguments
results = {}
event_system.emit("arg_pass2", arg="test", results=results)

# Check results
# storage/location for results from event handlers need to provided to the handler
# Appropriate safe objects should be used for results
# Consider async queue for async, threadsafe queue when using threads
# Destination URI's are good choices as well like redis, etc..
# if threadsafe/simple flow dictionary can be used with plugin_name as the key
print(results)
```

### Function Syntax
`__call__` is aliased to `emit()`. The instance can be used like a function.
```python
event_system = EventPluginSystem(plugin_dir=plugin_dir)
event_system("event", arg1=arg)
```

## Plugin Structure

Each plugin should be a Python file in the specified plugin directory and contain a class named Plugin. The class should define methods with names following the pattern handle_<event_name>.

### Example Plugin (simple_echo.py):
```python
class Plugin:
    def handle_start(self, **kwargs):
        print("Start event received.")

    def handle_arg(self, arg, **kwargs):
        print(f"Arg received: {arg}")
```

## Asynchronous Support

### For asynchronous event handling, use EventPluginSystemAsync:

```python
import asyncio
from event_plugin_system import EventPluginSystemAsync

es = EventPluginSystemAsync(plugin_dir=plugin_dir)

async def example():
    await es.emit("start")

if __name__ == '__main__':
    asyncio.run(example())

```

## Testing

```
pytest
```
