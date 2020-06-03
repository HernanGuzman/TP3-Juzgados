import numpy as np
from Juzgados.juzgados import Juzgado
from Juzgados.Pila import Pila
from Juzgados.tipoPrioridad import Prioridad


'''TDA TRIBUNALES'''
class Tribunales:
    '''INICIO EL EDIFICIO DE TRIBUNALES CON UNA MATRIZ DE JUZGADOS'''
    def __init__(self, pisos =5, oficinas =2):
        self.edificio = np.empty((pisos, oficinas), Juzgado)
    def __repr__(self):
        return str(self.tribunales)
    
    '''AGREGO UN JUZGADO A UNA OFICINA DEL EDIFICIO'''
    def establecerJuzgado(self, piso, oficina, Juzgado):
        self.edificio[piso, oficina] = Juzgado
    
    
    '''RECIBO EL PISO DONDE SE DEBE BUSCAR EL JUZGADO CRITICO'''
    def buscarCriticos(self, piso):
        '''CONSULTO SI EL TAMAÑO DEL ARRAY ES IGUAL A 1'''
        if(len(piso)==1):
            '''SI ES ASI CONSULTO SI ES CRITICO PARA DEVOLVER 1'''
            if self.edificio[piso, 0].esCritico():
                return 1
            else:
                return 0
        else:
            '''SI EL ARRAY NO ES DE TAMAÑO 1 CONSULTO SI ES JUZGADO DE LA POSICION 0 ES CRITICO'''
            if self.edificio[piso, 0].esCritico():
                '''SI ES CRITICO SUMO 1 Y VUELVO A LLAMAR A LA FUNCION PERO CON EL ARRAY SIN
                LA POSICION 0'''
                return 1 + self.buscarCriticos(self.edificio[piso, 1:])
            else:
                '''SI NO ES CRITICO SUMO VUELVO A LLAMAR A LA FUNCION PERO CON EL ARRAY SIN
                LA POSICION 0'''
                return self.buscarCriticos(self.edificio[piso, 1:])
            
            
    '''RECIBO EL NUMERO DE PISO PARA CONSULTAR LOS JUZGADOS CRITICOS'''
    def cantidadDeJuzgadosCriticos(self,piso):
        '''RECIBO DE LA FUNCION BUSCAR CRITICOS LA CANTIDAD DE JUZGADOS EN ESTADO CRITICOS
        A LA FUNCION LE PASO EL ARRAY DEL PISO'''
        cantidad = self.buscarCriticos(self.edificio[piso])
        return cantidad
        
    '''RECORRO TODO EL EDIFICIO PARA ENCONTRAR EL JUZGADO CON MENOS EXPEDIENTES'''        
    def juzgadoMenosRecargado(self):
        pisoMenosExp = 0
        oficinaMenosExp = 0
        expedientes = 100
        '''RECORRO TODO EL EDIFICIO'''
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[piso])):
                '''CONSULTO SI EL JUZGADO TIENE MENOS EXPEDIENTES URGENTES QUE EL GUARDADO'''
                if(self.edificio[piso,oficina].cantidadDeExpedientesUrgentes()<expedientes):
                    pisoMenosExp = piso
                    oficinaMenosExp = oficina
        return pisoMenosExp, oficinaMenosExp
             
    '''BUSCO EL JUZGADO DEL JUEZ'''
    def buscaJuez(self, juez):
        '''RECORRO EL EDIFICIO (MATRIZ) HASTA ENCONTRAR EL JUZGADO DEL JUEZ'''
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[piso])):
                if(self.edificio[piso,oficina].getNombreJuez == juez):
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
        exp = self.edificio[pisoOrgien, oficinaDest].buscarExpediente(numero)
        '''ELIMINO EL EXPEDIENTE EN EL JUZGADO DE ORIGEN'''
        self.edificio[pisoOrgien, oficinaDest].eliminarExpediente(numero)
        '''ENVIO EL EXPEDIENTE A EL JUZGADO DEL JUEZ DE DESTINO'''
        self.edificio[pisoDest, oficinaDest].recibirExpediente(exp)
        
        

tribunales = Tribunales(2,3) 

print(tribunales)
