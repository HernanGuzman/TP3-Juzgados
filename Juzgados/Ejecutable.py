
from Juzgados.tipoFuero import Fuero
from Juzgados.tipoPrioridad import Prioridad
from Juzgados.tipoEstado import Estado
from Juzgados.Expediente import Expediente


expe = Expediente(1, Fuero.Familia, Prioridad.Urgente, Estado.Juicio)
print(expe)




'''SI EL ARRAY NO ES DE TAMAÑO 1 CONSULTO SI ES JUZGADO DE LA POSICION 0 ES CRITICO'''