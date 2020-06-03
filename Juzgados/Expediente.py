from Juzgados.tipoEstado import Estado
from Juzgados.tipoPrioridad import Prioridad
from Juzgados.tipoFuero import Fuero


class Expediente:
  def __init__(self, numero, fuero = Fuero.Civil, prioridad = Prioridad.Urgente, estado = Estado.Investigacion):
    self.numero = numero
    self.fuero = fuero
    self.prioridad = prioridad
    self.estado = estado
    
  def __repr__(self):
    return "Numero Expediente: " + str(self.numero)  + " Fuero: " + str(self.fuero) + " Prioridad: " + str(self.prioridad) + " Estado: " + str(self.estado)
   

  def getPrioridad(self):
    return self.prioridad

  def getEstado(self):
    return self.estado

  def getNumero(self):
    return self.numero

  
    