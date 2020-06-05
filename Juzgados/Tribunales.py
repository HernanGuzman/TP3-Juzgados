import numpy as np
from Juzgados.juzgados import Juzgado
from Juzgados.Pila import Pila
from Juzgados.tipoPrioridad import Prioridad
from Juzgados.Expediente import Expediente
from Juzgados.tipoFuero import Fuero
from Juzgados.tipoEstado import Estado


'''TDA TRIBUNALES'''
class Tribunales:
    '''INICIO EL EDIFICIO DE TRIBUNALES CON UNA MATRIZ DE JUZGADOS'''
    def __init__(self, pisos =5, oficinas =2):
        self.edificio = np.empty((pisos, oficinas), Juzgado)
    def __repr__(self):
        return str(self.edificio)
    
    '''AGREGO UN JUZGADO A UNA OFICINA DEL EDIFICIO'''
    def establecerJuzgado(self, piso, oficina, Juzgado):
        self.edificio[piso, oficina] = Juzgado
    
    def cantOficinasOcupadas(self, piso):
        contador = 0
        for i in range(0, len(piso)):
            if (piso[i]) != None:
                contador +=1
                
        return contador
    def oficinasOcupadas(self, piso, ocupadas):
        oficOcupadas = np.empty((ocupadas), Juzgado)
        contador = 0
        for i in range(0, len(piso)):
            if (piso[i]) != None:
                oficOcupadas[contador] = piso[i]
                contador += 1
        return oficOcupadas
        
        
    '''RECIBO EL PISO DONDE SE DEBE BUSCAR EL JUZGADO CRITICO'''
    
    def buscarCriticos(self, piso):
        
        
        
        juzgado = piso[0]
        if(len(piso)==1):
            '''SI ES ASI CONSULTO SI ES CRITICO PARA DEVOLVER 1'''
            
            if juzgado.esCritico():
                return 1
            else:
                return 0
        else:
            
            if juzgado.esCritico():
                '''SI ES CRITICO SUMO 1 Y VUELVO A LLAMAR A LA FUNCION PERO CON EL ARRAY SIN
                LA POSICION 0'''
                return 1 + self.buscarCriticos(piso[1:])
            else:
                '''SI NO ES CRITICO SUMO VUELVO A LLAMAR A LA FUNCION PERO CON EL ARRAY SIN
                LA POSICION 0'''
                return self.buscarCriticos(piso[1:])
            
            
    '''RECIBO EL NUMERO DE PISO PARA CONSULTAR LOS JUZGADOS CRITICOS'''
    def cantidadDeJuzgadosCriticos(self,piso):
        '''RECIBO DE LA FUNCION BUSCAR CRITICOS LA CANTIDAD DE JUZGADOS EN ESTADO CRITICOS
        A LA FUNCION LE PASO EL ARRAY DEL PISO'''
        ocupadas = self.cantOficinasOcupadas(self.edificio[piso])
        oficOcupadas = self.oficinasOcupadas(self.edificio[piso], ocupadas)
        
        cantidad = self.buscarCriticos(oficOcupadas)
        return cantidad
        
    '''RECORRO TODO EL EDIFICIO PARA ENCONTRAR EL JUZGADO CON MENOS EXPEDIENTES'''        
    def juzgadoMenosRecargado(self):
        pisoMenosExp = 0
        oficinaMenosExp = 0
        expedientes = 100
              
        '''RECORRO TODO EL EDIFICIO'''
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[piso])):
                if(self.edificio[piso, oficina] != None):
                    '''CONSULTO SI EL JUZGADO TIENE MENOS EXPEDIENTES URGENTES QUE EL GUARDADO'''
                    if(self.edificio[piso,oficina].cantidadDeExpedientesUrgentes()<expedientes):
                        pisoMenosExp = piso
                        oficinaMenosExp = oficina
                        expedientes = self.edificio[piso,oficina].cantidadDeExpedientesUrgentes()
        return pisoMenosExp, oficinaMenosExp
             
    '''BUSCO EL JUZGADO DEL JUEZ'''
    def buscaJuez(self, juez):
        '''RECORRO EL EDIFICIO (MATRIZ) HASTA ENCONTRAR EL JUZGADO DEL JUEZ'''
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[piso])):
                 if(self.edificio[piso, oficina] != None):
                     if(self.edificio[piso,oficina].getNombreJuez() == juez):
                         return piso, oficina
                    
    '''ENVIO A LA MESA DE ENTRADA UNA PILA DE EXPEDIENTES Y EL JUEZ DE GUARDIA'''
    def mesaDeEntradas(self, pilaDeExpedientes, juez):
        '''CONSULTO EL PISO Y OFICINA DEL JUEZ'''    
        piso, oficina = self.buscaJuez(juez)
        '''CONSULTO EL JUZGADO MENOS OCUPADO POR SI FUERA NECESARIO'''
        pisoMenosOcupado , oficinaMenosOcupada = self.juzgadoMenosRecargado()
        '''RECORRO LA PILA DE EXPEDIENTES HASTA QUE ESTE VACIA'''
        while not pilaDeExpedientes.isEmpty():
            '''CONSULTO SI EL JUZGADO DEL JUEZ DE GUARDIA NO ESTA EN ESTADO CRITICO'''
            if(not self.edificio[piso, oficina].esCritico()):
                '''SINO ESTA EN ESTADO CRITICO AGREGO EL EXPEDIENTE AL JUZGADO'''
                self.edificio[piso, oficina].recibirExpediente(pilaDeExpedientes.desapilar())
                
            else:
                '''SI ESTA EN ESTADO CRITICO LO AGREGO AL JUZGADO CON MENOS EXPEDIENTES'''
                self.edificio[pisoMenosOcupado, oficinaMenosOcupada].recibirExpediente(pilaDeExpedientes.desapilar())
                    
                
                    
    def moverExpediente(self, numero, juezOrigen, juezDestino):
        '''CONSULTO EL PISO Y OFICINA DEL JUEZ DE ORIGEN'''
        pisoOrgien, oficinaOrigen = self.buscaJuez(juezOrigen)
        '''CONSULTO EL PISO Y OFICINA DEL JUEZ DE DESTINO'''
        pisoDest, oficinaDest = self.buscaJuez(juezDestino)
        '''BUSCO EL EXPEDIENTE DEL JUZGADO'''
        exp = self.edificio[pisoOrgien, oficinaOrigen].buscarExpediente(numero)
        if(exp != None):
            '''ELIMINO EL EXPEDIENTE EN EL JUZGADO DE ORIGEN'''
            self.edificio[pisoOrgien, oficinaDest].eliminarExpediente(numero)
            '''ENVIO EL EXPEDIENTE A EL JUZGADO DEL JUEZ DE DESTINO'''
            self.edificio[pisoDest, oficinaDest].recibirExpediente(exp)
            print("El Expediente se movio correctamente al juzgado del doctor : " + juezDestino)
        else:
            print("El Expediente no se encuentra en el juzgado indicado")
        

tribunales = Tribunales(2,3) 

print(tribunales)

juzgado1 = Juzgado("Oyarbide", 3)
juzgado2 = Juzgado("Gonzalez", 4)   


exp1 = Expediente(1, Fuero.Comercial, Prioridad.Normal, Estado.Investigacion)
exp2 = Expediente(2, Fuero.Civil, Prioridad.Urgente, Estado.Juicio)
exp3 = Expediente(3, Fuero.Familia, Prioridad.Normal, Estado.Investigacion)
exp4 = Expediente(4, Fuero.Penal, Prioridad.Normal, Estado.Juicio)
exp5 = Expediente(5, Fuero.Penal, Prioridad.Urgente, Estado.Juicio)
exp6 = Expediente(6, Fuero.Penal, Prioridad.Normal, Estado.Investigacion)
exp7 = Expediente(7, Fuero.Comercial, Prioridad.Normal, Estado.Investigacion)
exp8 = Expediente(8, Fuero.Civil, Prioridad.Urgente, Estado.Juicio)
exp9 = Expediente(9, Fuero.Familia, Prioridad.Normal, Estado.Investigacion)
exp10 = Expediente(10, Fuero.Penal, Prioridad.Normal, Estado.Juicio)
exp11 = Expediente(11, Fuero.Penal, Prioridad.Urgente, Estado.Juicio)
exp12 = Expediente(12, Fuero.Penal, Prioridad.Normal, Estado.Investigacion)

juzgado1.recibirExpediente(exp1)
juzgado1.recibirExpediente(exp2)
juzgado1.recibirExpediente(exp3)
juzgado1.recibirExpediente(exp4)
juzgado1.recibirExpediente(exp5)
juzgado1.recibirExpediente(exp6)

juzgado2.recibirExpediente(exp1)
juzgado2.recibirExpediente(exp2)
juzgado2.recibirExpediente(exp3)
juzgado2.recibirExpediente(exp4)
juzgado2.recibirExpediente(exp5)
juzgado2.recibirExpediente(exp6)

tribunales = Tribunales(2,3) 



tribunales.establecerJuzgado(1, 2, juzgado1)
tribunales.establecerJuzgado(1, 1, juzgado2)

print(tribunales)

tribunales.cantidadDeJuzgadosCriticos(1)

print("La cantidad de juzgados en estado critico es: " + str(tribunales.cantidadDeJuzgadosCriticos(1)))
piso, oficina = tribunales.juzgadoMenosRecargado()
print("El juzgado menos cargado se encuentra en el piso: " + str(piso) + " oficina: " + str(oficina))
piso, oficina = tribunales.buscaJuez("Oyarbide")
print("El juzgado el juez se encuentra en el piso: " + str(piso) + " oficina: " + str(oficina))


pilaExp = Pila()
pilaExp.apilar(exp7)
pilaExp.apilar(exp8)
pilaExp.apilar(exp9)
pilaExp.apilar(exp10)
pilaExp.apilar(exp11)
pilaExp.apilar(exp12)

tribunales.mesaDeEntradas(pilaExp, "Oyarbide")

print(tribunales)

tribunales.moverExpediente(12, "Gonzalez", "Oyarbide")








