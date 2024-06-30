class Plugin:
    def __init__(self, **kwargs):
        example = kwargs.get('example', None)
        if example:
            self.example = example
    def handle_test_kwarg(self, **kwargs):
        results = kwargs.get('results')
        results[self.plugin_name] = self.example
