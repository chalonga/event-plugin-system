class Plugin:
    def __init__(self, **kwargs):
        super().__init__()

    def handle_test_mutation(self, **kwargs):
        arg = kwargs.get('arg', None)
        results = kwargs.get('results', None)

        if arg is None or arg == '':
            results_ = ''
        else:
            results_ = arg + arg

        if results is None:
            print(f"RESULTS {str(results_)}\n")
        else:
            results[self.plugin_name] = results_
        
