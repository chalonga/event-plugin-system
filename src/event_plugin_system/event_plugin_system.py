import os
import importlib


HANDLER_PREFIX = "handle"


def info(msg):
    print(f"[INFO] {msg}")


def error(msg):
    print(f"[ERROR] {msg}")


class EventPluginSystem:
    def __init__(self, plugin_dir=None, classname="Plugin", handler_prefix=HANDLER_PREFIX):
        self._prefix = handler_prefix
        self._plugins = []
        if plugin_dir:
            self.load_plugins(plugin_dir, classname=classname)

    def load_plugins(
        self, plugin_dir, classname="Plugin"
    ):  # , attr_name='plugin_name'):
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                plugin_path = os.path.join(plugin_dir, filename)
                plugin_name = filename[:-3]  # Remove .py extension

                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                plugin_class = getattr(module, classname, None)
                if plugin_class:
                    plugin_instance = plugin_class()
                    if not getattr(plugin_instance, "plugin_name", None):
                        plugin_instance.plugin_name = plugin_name
                    self.register(plugin_instance)
                    info(f"Loaded plugin: {plugin_instance.plugin_name}")

    def register(self, plugin):
        assert getattr(plugin, "plugin_name")
        if plugin not in self._plugins:
            self._plugins.append(plugin)

    # XXX is this going to be used?
    def detach(self, plugin):
        try:
            self._plugins.remove(plugin)
        except ValueError:
            pass

    def emit(self, event_type, **kwargs):
        handler_name = "_".join((self._prefix, event_type))

        for plugin in self._plugins:
            handler = getattr(plugin, handler_name, None)
            if not handler:
                continue
            # XXX thinking about adding in 'string handlers'
            # XXX strings/keywords that map to default/builtin handlers
            # XXX then this would change to isinstance(handler, str)
            # XXX not sure how the builtins would be useful for arbitrary plugins..
            # XXX probably a bad idea, but storing here...
            # if isinstance(handler, str):
            #    handler = builtin_handler_map[handler]
            if not callable(handler):
                continue
            handler(**kwargs)

    # allow function calling syntax
    __call__ = emit


class EventPluginSystemAsync(EventPluginSystem):
    async def emit(self, event_type, **kwargs):
        handler_name = "_".join((HANDLER_PREFIX, event_type))

        for plugin in self._plugins:
            handler = getattr(plugin, handler_name, None)
            if not handler:
                continue
            # XXX thinking about adding in 'string handlers'
            # XXX strings/keywords that map to default/builtin handlers
            # XXX then this would change to isinstance(handler, str)
            # XXX not sure how the builtins would be useful for arbitrary plugins..
            # XXX probably a bad idea, but storing here...
            # if isinstance(handler, str):
            #    handler = builtin_handler_map[handler]
            if not callable(handler):
                continue
            info(f"{handler_name} {handler} handler")
            try:
                # XXX change to launch task in background/taskpool?
                await handler(**kwargs)
            except TypeError as e:
                error(
                    f"{plugin.plugin_name} {handler_name} handler failed: is async? {e}"
                )

    __call__ = emit
