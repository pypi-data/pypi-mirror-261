from abc import ABC
from pydantic import BaseModel


class Options(BaseModel):
    pass


class Brick(ABC):

    options: Options

    def __init__(self, options: Options):
        self.options = options

    async def __ainit__(self):
        """Async constructior."""
