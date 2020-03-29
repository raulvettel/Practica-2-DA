#coding: utf8

#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos                     #
#                                                     #
#            Práctica 2                               #
#                                                     #
#            Elaborador por: Raúl Alarcón López       #    
#                                                     #
#######################################################
#######################################################

import math
from diccionariopr import dicPrioridad

# Esta clase debe implementar los algoritmos para el cálculo de caminos.
class algCaminos:
    
    # Constructor
    def __init__(self,mapa):
        
        # El primer paso consiste en extraer las estructuras de datos del mapa y adaptarlas y/o convertirlas
        # del modo conveniente.
        
        # Cada pueblo o ciudad es un nodo
        self.N = tuple(mapa.pueblos+mapa.ciudades) 
        
        # Lee las coordenadas
        self.C = mapa.coordenadas
        
        # Todas las carreteras y autovías son aristas        
        self.E = mapa.carreteras + mapa.autovias
        
        # Actualiza las carreteras para que contemplen los dos sentidos
        self.E  = tuple(self.E + [(o,d) for (d,o) in self.E])
        
        # Actualiza los pesos de los arcos según la distancia y el tipo de carretera
        self.D ={}
        # Sacamos el peso dependiendo del tipo de carretera
        for item in self.E:
            if item in mapa.carreteras:
                self.D[item[0],item[1]] = (mapa.distancias[item])
                self.D[item[1],item[0]] = (mapa.distancias[item])
            elif item in mapa.autovias:
                self.D[item[1],item[0]] = (mapa.distancias[item])
                self.D[item[0],item[1]] = (mapa.distancias[item])
        #self.T = mapa.distancias

    # Esta función debe implementar el algoritmo de Dijkstra
    def dijkstra(self,origen,destino):
        # Se pueden cambiar los nombres de las funciones para 
        # que el código sea más claro
        edges = self.E
        distances = self.D
        
        # Estructuras necesarias
        S = set([]) # Nodos incluidos
        Q = set([]) # Nodos candidatos
        D = {} # Distancia al origen
        P = {} # Camino
        
        # Estas estructuras almacenan los resultados
        aristasVisitadas = set([])
        camino = []
        tiempoViaje=0
        i = 0
        # Inicialización
        S.add(origen)
        D[origen] = 0
        ultimo = origen
        # Bucle principal
        while ultimo!= destino:
            # Buscamos nodos candidatos
            for item in edges:
                tupleAux = edges[edges.index(item)]
                # Si no está en Q lo añadimos
                if tupleAux[0] == ultimo and tupleAux[1] not in Q and tupleAux[1] not in S:
                    Q.add(tupleAux[1])
                    D[tupleAux[1]] = D[ultimo]  + distances[tupleAux]
                    aristasVisitadas.add(tupleAux)
                # Si está cogemos el mínimo
                elif tupleAux[0] == ultimo and tupleAux[1] not in Q and tupleAux[1] not in S:
                    D[tupleAux[1]] = min(D[ultimo]+distances[tupleAux],D[tupleAux[1]])
                    aristasVisitadas.add(tupleAux)
            # Nos quedamos con el nodo más cercano
            menor = 10000
            nodo = ''
            for item2 in Q:
                if D[item2] < menor:
                    menor = D[item2]
                    nodo = item2
            #tiempoViaje += T[(ultimo,nodo)]
            S.add(nodo)
            Q.remove(nodo)
            camino.append((ultimo,nodo))
            ultimo = nodo
            print camino
        ##############################################
        # Salida ejemplo ¡¡BORRAR!!!
        self.tiempoViaje = 1.0
        #S = set(['Albacete','La Roda','Cuenca'])
        #Q = set(['Ruidera'])
        #aristasVisitadas = [('Albacete','La Roda'),('La Roda','Cuenca'),('Albacete','Ruidera')] 
        #camino = [('Albacete','La Roda'),('La Roda','Cuenca')] # El camino debe ser un conjunto de tuplas
        ##############################################
        
        # Devuelve la salida.
        return (tiempoViaje/60, Q | S,  aristasVisitadas, camino)   
    
    
    # Esta función debe implementar el algoritmo de Dijkstra que introduzca información euclídea
    def dijkstraConDistanciaEuclidea(self,origen,destino):
        # Se pueden cambiar los nombres de las funciones para 
        # que el código sea más claro             
        edges = self.E
        distances = self.D
        coordenadas = self.C
        
        # Estructuras necesarias
        S = set([]) # Nodos incluidos
        Q = set([]) # Nodos candidatos
        D = {} # Distancia al origen
        P = {} # Camino
        EU = {} # Distancia euclídea de cada nodo al destino
        
        
        # Estas estructuras almacenan los resultados
        aristasVisitadas = set([])
        camino = []
        tiempoViaje=0
        
        
        # Implementación
        

        ##############################################
        # Salida ejemplo ¡¡BORRAR!!!
        self.tiempoViaje = 1.0
        S = set(['Albacete','La Roda','Cuenca'])
        Q = set(['Ruidera'])
        aristasVisitadas = [('Albacete','La Roda'),('La Roda','Cuenca'),('Albacete','Ruidera')] 
        camino = [('Albacete','La Roda'),('La Roda','Cuenca')] # El camino debe ser un conjunto de tuplas
        ##############################################
        
        # Devuelve la salida.
        return (tiempoViaje, Q | S,  aristasVisitadas, camino)           
    
    # Esta función debe implementar el algoritmo de Dijkstra que introduzca información euclídea
    def dijkstraConDistanciaEuclideaYMejoras(self,origen,destino):
        # Se pueden cambiar los nombres de las funciones para 
        # que el código sea más claro        
        edges = self.E
        distances = self.D
        coordenadas = self.C
        
        # Estructuras necesarias        
        S = set([]) # Nodos incluidos
        Q = set([]) # Nodos candidatos
        DP = dicPrioridad() # Distancia al origen
        P = {} # Camino
        EU = {} # Distancia euclídea de cada nodo al destino
        
        
        # Estas estructuras almacenan los resultados
        aristasVisitadas = set([])
        camino = []
        tiempoViaje=0
        
        # Implementación
        

        ##############################################
        # Salida ejemplo ¡¡BORRAR!!!
        self.tiempoViaje = 1.0
        S = set(['Albacete','La Roda','Cuenca'])
        Q = set(['Ruidera'])
        aristasVisitadas = [('Albacete','La Roda'),('La Roda','Cuenca'),('Albacete','Ruidera')] 
        camino = [('Albacete','La Roda'),('La Roda','Cuenca')] # El camino debe ser un conjunto de tuplas
        ##############################################
        
        # Devuelve la salida.
        return (tiempoViaje, Q | S,  aristasVisitadas, camino)   