from pydentic import BaseModel
from bbl.bricks import Brick 
from bbl.bricks import Options 


class Requirements(BaseModel):

    __after__ = []


class Options(bbl.bricks.Options):
    components: list[Component, ComponentOptions]


class Component(Brick):

    req: Requirements
    components: list[tuple[Component, ComponentOptions]]

    def __init__(self, options: Options, req: Requirements):
        super().__init__(options)
        self.components = self.components + options.components
        
        self.req = req
