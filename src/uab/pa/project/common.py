from enum import Enum


class TipusDades(Enum):
    Pelicules = "pelicules"
    Llibres = "llibres"


class TipusRecomanador(Enum):
    Simple = "simple"
    Colaboratiu = "col.laboratiu"
    Contingut = "contingut"
