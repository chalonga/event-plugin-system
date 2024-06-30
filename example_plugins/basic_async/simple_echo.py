import asyncio

class Plugin:

    async def echo(self, msg):
        await asyncio.sleep(0.5)
        print(f"From Echo Plugin: {msg}\n")

    async def handle_start(self, **kwargs):
        await self.echo("Started")

    async def handle_arg(self, **kwargs):
        arg = kwargs.get('arg', None)
        if arg is None:
            self.echo("Got no arg")
            return
        await self.echo(f"Got arg {arg}")
        return
