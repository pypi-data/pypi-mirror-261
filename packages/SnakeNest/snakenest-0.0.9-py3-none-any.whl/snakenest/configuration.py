from .rulez import Rulez
from os import environ

class Configuration:
    rulez = None

    def __init__(self):
        print(environ)
        Configuration.rulez = Rulez('nest.yaml')
