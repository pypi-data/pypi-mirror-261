from .rulez import Rulez


class Configuration:
    rulez = None

    def __init__(self):
        # print(environ)
        Configuration.rulez = Rulez('nest.yaml')
