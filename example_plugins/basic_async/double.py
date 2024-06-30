class Plugin:
    async def handle_arg_pass2(self, **kwargs):
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
        
