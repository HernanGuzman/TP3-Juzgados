from enum import Enum

class Fuero(int, Enum):
    Civil = 0
    Penal = 1
    Laboral = 2
    Familia = 3
    Comercial = 4