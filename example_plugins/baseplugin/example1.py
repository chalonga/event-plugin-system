from event_plugin_system import BasePlugin

class Plugin(BasePlugin):
    def handle_start(self):
        self.info(f"{self.plugin_name} started")
