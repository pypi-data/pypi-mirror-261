from . import config


class Proxy6Exception(Exception):
    def __init__(self, code: int | None = None, description: str | None = None):
        self.code = code
        self._description = description
        super().__init__(self.description)

    def __repr__(self):
        return '{}(code={}, description={})'.format(self.__class__, self.code, self.description)

    @property
    def description(self):
        return config.ERROR_CODES.get(int(self.code), config.ERROR_UNKNOWN)
