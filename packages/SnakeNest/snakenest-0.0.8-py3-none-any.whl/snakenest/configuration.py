from .rulez import Rulez


class Configuration:
    rulez = None

    def __init__(self):
        Configuration.rulez = Rulez('nest.yaml')
