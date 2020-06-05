from enum import Enum

class Fuero(str, Enum):
    Civil = 'Civil'
    Penal = 'Penal'
    Laboral = 'Laboral'
    Familia = 'Familia'
    Comercial = 'Comercial'