from Juzgados.Colas import Cola

#TDA JUZGADO

'''TDA JUZGADO'''
class Juzgado:
    
  '''EL JUZGADO SE INICIALIZA CON EL NOMBRE DEL JUEZ Y POR LA CANTIDAD CRITICA DE 
   EXPEDIENTES QUE PUEDE TENER'''
  def __init__(self, nombre, cantCritica = 50):
    self.nombre = nombre
    self.cantCritica = cantCritica
    self.expUrgentes = Cola()
    self.expNormales = Cola()
    
  def repr(self):
        cadena = 'nombre del juzgado: '+ self.nombre + '\n' + 'expedientes prioridad normal: '+str(self.expNormales) + '\n'+ 'expedientes prioridad urgente: '+str(self.expUrgentes) + 'expedientes estado en Investigacion: '+str(self.enInvestigacion) + '\n'+ 'expedientes estado en Juicio: '+str(self.enJuicio)
        return cadena
  '''DEVUELVE EL NOMBRE DEL JUEZ'''  
  def getNombreJuez(self):
      return self.nombre  
  
  '''FUNCION QUE SE UTILIZA PARA IMPRIMIR SI LOS EXPEDIENTES ENTRARON EN ZONA CRITICA '''  
  def controlarCrticidad(self, tipo):
      if(tipo == "Normal") and (self.expNormales.len() > 50):
          print("Expedientes Normales en cantidad critica")
      elif(tipo == "Urgente") and (self.expUrgentes.len() > 50):
          print("Expedientes Urgentes en cantidad critica")
          

  '''FUNCION QUE RECIBE EL EXPEDIENTE Y LO AGREGA A LA COLA QUE PERTENECE'''
  def recibirExpediente(self, expediente):
    if(expediente.getPrioridad() == "Normal"):
       self.expNormales.encolar(expediente)
       '''LLAMO A LA FUNCION PARA DAR EL AVISO DE ESTADO CRITICO'''
       self.controlarCriticidad("Normal")
    else:
      self.expUrgentes.encolar(expediente)
      self.controlarCriticidad("Urgente")
    
    

  

  '''FUNCION QUE DEVUELVE SI EL JUZGADO TIENE EXPEDIENTES URGENTES'''
  def tieneUrgentes(self):
    return not self.expUrgentes.estaVacia()

  '''FUNCION QUE DEVUELVE SI EL JUZGADO TIENE EXPEDIENTES NORMALES'''
  def tieneNormales(self):
    return not self.expNormales.estaVacia()

  '''FUNCION QUE DEVUELVE CUAL ES EL PRIMER EXPEDIENTE QUE SE DEBERIA TRATAR'''
  def primerExpedienteATratar(self):
    exped = None
    '''PRIMERO CONSULTA SI TIENE URGENTES PARA TRATAR'''
    if(self.tieneUrgentes()):
      exped = self.expUrgentes.top()
      '''SINO HAY URGENTES CONSULTO POR LOS EXPEDIENTES NORMALES'''
    elif(self.tieneNormales()):
      exped = self.expNormales.top()
    return exped

  '''FUNCION QUE DEVUELVE EL EXPEDIENTE A TRATARN Y LO SACA DEL JUZGADO'''
  def tratarExpediente(self):
    exped = None
    '''PRIMERO CONSULTA SI TIENE URGENTES PARA TRATAR'''
    if(self.tieneUrgentes()):
      '''DESENCOLA EL EXPEDIENTE'''
      exped = self.expUrgentes.desencolar()
    elif(self.tieneNormales()):
      exped = self.expNormales.desencolar()
    else:
      print("En el juzgado no hay espedientes para tratar")
    return exped

  '''DEVUELVE LA CANTIDAD DE EXPEDIENTES NORMALES PARA TRATAR'''
  def cantidadDeExpedientesNormales(self):
    return self.expNormales.len()

  '''FUNCION QUE DEVUELVE LA CANTIDAD DE EXPEDIENTES URGENTES'''
  def cantidadDeExpedientesUrgentes(self):
    return self.expUrgentes.len()

  '''FUNCION QUE DEVUELVE LA CANTIDAD DE EXPEDIENTES EN EL JUZGADO
  LLAMA A LA FUNCION DE CADA TIPO Y LOS SUMA'''
  def cantidadTotalDeExpedientes(self):
    return self.cantidadDeExpedientesNormales() + self.cantidadDeExpedientesUrgentes()


  '''FUNCION QUE DEVUELVE SI ALGUNA COLA DE EXPEDIENTES SOBREPASA LA CANTIDAD CRITICA'''
  def esCritico(self):
    return self.cantidadDeExpedientesNormales() > self.cantCritica or self.cantidadDeExpedientesUrgentes() > self.cantCritica
  
  '''FUNCION QUE DEVUELVE LOS EXPEDIENTES URGENTES EN JUICIO'''
  def enJuicioUrgentes(self):
    cantidad = 0
    '''CLONO LOS EXPEDIENTES URGENTES'''
    colaAuxUrgentes = self.expUrgentes.clonar()
    '''MIENTRAS LA COLA DE URGENTES NO ESTE VACIA'''
    while not colaAuxUrgentes.isEmpty():
      '''SACO EL EXPEDIENTE DE LA COLA AUXILIAR'''
      exp = colaAuxUrgentes.desencolar()
      '''CONSULTO SI EL ESTADO DEL EXPEDIENTE ES EN JUICIO'''
      if(exp.getEstado() == "Juicio"):
        '''SI EL ESTADO ES JUICIO SUMAMOS 1'''
        cantidad = cantidad + 1
    return cantidad

  '''FUNCION QUE DEVUELVE LOS EXPEDIENTES NORMALES EN JUICIO'''
  def enJuicioNormales(self):
    cantidad = 0
    exp = None
    colaAuxNormales = self.expNormales.clonar()
    while not colaAuxNormales.isEmpty():
      exp = colaAuxNormales.desencolar()
      if(exp.getEstado() == "Juicio"):
        cantidad = cantidad + 1
    return cantidad

  '''FUNCION QUE DEVUELVE LOS EXPEDIENTES EN JUICIO SUMANDO LOS RESULTADOS DE LAS 
  DOS FUNCIONES'''
  def enJuicio(self):
    return self.enJuicioUrgentes() + self.enJuicioNormales()

          
        
  '''FUNCION QUE BUSCA UN EXPEDIENTE POR NUMERO'''
  def buscarExpediente(self, numero):
    '''HAGO UNA COPIA DE LAS DOS COLAS'''
    colaAuxNormales = self.expNormales.clonar()
    colaAuxUrgentes = self.expUrgentes.clonar()
    '''DECLARO DOS VARIABLES, UNA ES PARA NO RECORRER TODA LA COLA DE EXPEDIENTES
    SI SE ENCUENTRA '''
    encontrado = False
    expediente = None
    '''MIENTRAS LA COLA DE EXPEDIENTES NORMALES NO ESTE VACIO O SI TODAVIA NO SE 
    ENCONTRO EL EXPEDIENTE'''
    while not colaAuxNormales.isEmpty() and encontrado == False:
      exp = colaAuxNormales.desencolar()
      '''EL NUMERO DEL EXPEDIENTE DESENCOLADO SE COMPARA CON EL NUMERO QUE SE DESEA BUSCAR'''
      if(exp.getNumero() == numero):
        encontrado = True
        expediente = exp
    while not colaAuxUrgentes.isEmpty() and encontrado == False:
      exp = colaAuxUrgentes.desencolar()
      if(exp.getNumero() == numero):
        encontrado = True
        expediente = exp
    return expediente

  '''FUNCION QUE ELIMINA LOS EXPEDIENTES NORMALES'''
  def eliminarExpNormal(self, numero):
      '''CLONO LA COLA DE EXPEDIENTES NORMALES'''
      colaNormAux = self.expNormales.clonar()
      '''VACIO LA COLA ORIGINAL'''
      self.expNormales.vaciar()
      '''VARIABLE PARA INFORMAR SI SE ENCONTRO EL EXPEDIENTE EN LA COLA DE NORMALES'''
      encontrado = False
      '''MIENTRAS LA COLA AUXILIAR NO ESTE VACIA '''
      while not colaNormAux.estaVacia():
        '''CONSULTO SI EL EXPEDIETE DE LA PRIMERA POSICION NO ES EL EXPEDIENTE BUSCADO'''  
        if colaNormAux.top().getNumero() != numero:
            '''COMO NO ES EL EXPEDIENTE A ELIMINAR LO VUELVO A GUARDAR EN LA COLA ORIGINAL'''
            self.expNormales.encolar()(colaNormAux.desencolar())
        else:
            '''SI EL EXPEDIENTE ES IGUAL AL NUMERO BUSCADO LO ELIMINO DE LA COLA AUXILIAR
            PERO NO LO GUARDO EN LA COLA ORIGINAL'''
            colaNormAux.desencolar()
            '''COLOCO LA VARIABLE EN TRUE PORQUE SE ENCONTRO EL EXPEDIENTE'''
            encontrado = True
      return encontrado
  
  def eliminarExpUrgente(self, numero):
      colaUrgAux = self.expUrgentes.clone()
      self.expUrgentes.vaciar()
      encontrado = False
      while not colaUrgAux.estaVacia():
        if colaUrgAux.top().getNumero() != numero:
            self.expUrgentes.encolar()(colaUrgAux.desencolar())
        else:
            colaUrgAux.desencolar()
            encontrado = True
      return encontrado
      

  

       
  '''FUNCION PARA ELIMINAR EL EXPEDIENTE QUE LLAMA A LAS FUNCIONES PARTICULARES 
  PARA CADA TIPO'''          
  def eliminarExpediente(self,nroExp):
      '''SI NO SE ENCONTRO EL EXPEDIENTE EN LA COLA DE NORMALES'''
      if not self.eliminarExpNormal():
          '''SE BUSCA EN LA COLA DE URGENTES'''
          if not self.eliminarExpUrgente():
              '''SI NO SE ENCUENTRA EL ARCHIVO EN NINGUNA DE LAS COLAS SE DA EL MENSAJE DE ERROR'''
              return "El archivo se elimino correctamente"

  def cambiarDeEstado(self,numero):
      '''CLONO LAS DOS COLAS''' 
      colaUrgAux = self.expUrgentes.clone()
      colaNormAux = self.expNormales.clonar()
      encontrado = False
        
      '''VACIO LA COLA DE URGENTES'''
      self.expUrgentes.vaciar()
        
      '''RECORRO LAS COLAS AUXILIARES Y SI NO SON IGUALES AL NUMERO LAS ENCOLO EN LAS COLAS ORIGINALES'''
      while not colaUrgAux.estaVacia():
        if colaUrgAux.top().getNumero() != numero:
            self.expUrgentes.encolar()(colaUrgAux.desencolar())  
        else:
            self.expNormales.encolar(colaUrgAux.desencolar())
      '''CONSULTO SI SE ENCONTRO EL EXPEDIENTE PORQUE SINO LO VOLVERIA A PASAR A LA OTRA COLA'''      
      if(not encontrado):
          self.expNormales.vaciar()
          while not colaNormAux.estaVacia():
              if colaNormAux.top().getNumero() != numero:
                  self.expNormales.encolar()(colaNormAux.desencolar())
              else:
                  self.expUrgentes.encolar(colaNormAux.desencolar())

    

    
    
    

    


  
  


