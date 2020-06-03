#TDA PILA
class Pila:
  def __init__(self):
    self.pila = []

  def empty(self):
    self.pila.clear()

  def apilar(self, elemento):
    self.pila.append(elemento)

  def __repr__(self):
    return str(self.pila)

  def desapilar(self):
    dato = None
    if not self.isEmpty():
      dato = self.pila.pop()
    return dato

  def top(self):
    dato = None
    if not self.isEmpty():
      dato = self.pila[len(self.pila)-1]
    return dato

  def isEmpty(self):
    return len(self.pila) == 0

  def clonar(self):
    nueva = Pila()
    for elemento in self.pila:
      nueva.pila.append(elemento)
    return nueva

  def len(self):
    return len(self.pila)