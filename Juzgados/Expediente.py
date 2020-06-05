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
    return "Numero Expediente: " + str(self.numero) + '\n' + " Fuero: " + str(self.fuero.value)+ '\n' + " Prioridad: " + str(self.prioridad.value)+ '\n' + " Estado: " + str(self.estado.value)
   

  def getPrioridad(self):
    return self.prioridad

  def getEstado(self):
    return self.estado

  def setEstado(self,nuevoEstado):
      self.estado=nuevoEstado
      
  def setPrioridad(self,nuevaPrioridad):
      self.prioridad = nuevaPrioridad

  def getNumero(self):
    return self.numero


exp = Expediente(1, Fuero.Comercial, Prioridad.Normal, Estado.Investigacion)
print(exp)
    