class BasePlugin:
    def __init__(self, **kwargs):
        super().__init__()
        self._set_attr_if_exists('logger', kwargs)

    def _set_attr_if_exists(self, attr_name, kwargs):
        if attr_name in kwargs:
            setattr(self, attr_name, kwargs[attr_name])

    # TODO:XXX this looks like too much of a hack,
    # probably needs refactoring
    def info(self, message):
        if not hasattr(self, 'logger'):
            print(f"[INFO] {message}")
        else:
            self.logger.info(message)

    def warn(self, message):
        if not hasattr(self, 'logger'):
            print(f"[WARNING {message}")
        else:
            self.logger.warn(message)

    def error(self, message):
        if not hasattr(self, 'logger'):
            print(f"[ERROR] {message}")
        else:
            self.logger.error(message)
