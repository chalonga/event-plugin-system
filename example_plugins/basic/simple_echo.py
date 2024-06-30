class Plugin:

    def __init__(self, **kwargs):
        super().__init__()

    def echo(self, msg):
        print(f"From Echo Plugin: {msg}\n")

    def handle_start(self, **kwargs):
        self.echo("Started")

    def handle_arg(self, **kwargs):
        arg = kwargs.get('arg', None)
        if arg is None:
            self.echo("Got no arg")
            return
        self.echo(f"Got arg {arg}")
        return
