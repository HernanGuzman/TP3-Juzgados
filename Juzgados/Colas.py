class Cola:
  def __init__(self):
    self.cola = []

  def vaciar(self):
    self.cola.clear()

  def encolar(self, elemento):
    self.cola.insert(0,elemento)

  def __repr__(self):
    return str(self.cola)

  def desencolar(self):
    dato = None
    if not self.estaVacia():
      dato = self.cola.pop()
    return dato

  def top(self):
    dato = None
    if not self.estaVacia():
      dato = self.cola[len(self.cola)-1]
    return dato

  def estaVacia(self):
    return len(self.cola) == 0

  def clonar(self):
    nueva = Cola()
    for elemento in self.cola:
      nueva.encolar(elemento)
    return nueva

  def len(self):
    return len(self.cola)