from bbl.bricks import Brick


class App(Brick):

    components = [
        (CliComponent, CliComponent.options(a=1, b=2))
    ]

    def __init__(self, options):
        super().__init__(options)
