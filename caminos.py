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
                self.D[item[0],item[1]] = (mapa.distancias[item] / 90)
                self.D[item[1],item[0]] = (mapa.distancias[item] / 90)
            elif item in mapa.autovias:
                self.D[item[1],item[0]] = (mapa.distancias[item] / 120)
                self.D[item[0],item[1]] = (mapa.distancias[item] / 120)
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

        # Inicialización
        for item in self.N:
            D[item] = (float('inf'))
        S.add(origen)
        D[origen] = 0
        ultimo = origen
        # Bucle principal
        while destino not in S:
            # Recorremos cada (u,v)
            for (u,v) in edges:
                if u == ultimo:
                    # Si v no está entre los candidatos lo añadimos
                    if v not in Q:
                        Q.add(v)
                    # Nos quedamos con la menor de las distancias
                    if (D[u] + distances[(u,v)]) < D[v]:
                        aristasVisitadas.add((u,v))
                        D[v] = D[u] + distances[(u,v)]
                        P[v] = u
            # Extraemos el menor
            elegido = ''
            menor = (float('inf'))
            for item in Q:
                if D[item] < menor and item not in S:
                    menor = D[item]
                    elegido = item
            ultimo = elegido
            S.add(elegido)

        destiny = destino
        origin = P[destino]
        # añadimos la ruta inicial
        camino.append((origin,destiny))
        #sumamos el tiempo de esa ruta
        tiempoViaje += distances[(origin,destiny)]
        # Recuperamos el camino
        while True:
            # Cuando estamos en origen rompemos ejecución.
            if origin==origen:
                break
            else:
                destiny = origin
                origin = P[destiny]
                # Se inserta al principio para cumplir con el formato pedido de salida
                camino.insert(0,(origin,destiny))
                tiempoViaje += distances[(origin,destiny)]
        # Devuelve la salida.
        return (tiempoViaje, Q | S,  aristasVisitadas, camino)   
    
    
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
        
        print coordenadas
        # Estas estructuras almacenan los resultados
        aristasVisitadas = set([])
        camino = []
        tiempoViaje=0
        # Inicialización
        for item in self.N:
            D[item] = (float('inf'))
        S.add(origen)
        D[origen] = 0
        EU[destino] = 0
        ultimo = origen
        
        # Bucle principal
        while destino not in S:
            # Recorremos cada (u,v)
            for (u,v) in edges:
                if u == ultimo:
                    # Si v no está entre los candidatos lo añadimos
                    if v not in Q:
                        Q.add(v)
                    # Nos quedamos con la menor de las distancias a origen
                    if (D[u] + distances[(u,v)]) < D[v]:
                        aristasVisitadas.add((u,v))
                        D[v] = D[u] + distances[(u,v)]
                        P[v] = u
                    # Calculamos la distancia euclidea del nodo a destino mediante la formula matematica
                    if v not in EU:
                        EU[v] = math.sqrt(((coordenadas[destino][0] - coordenadas[v][0])**2) + ((coordenadas[destino][1] - coordenadas[v][1])**2)) / 120
            # Extraemos el menor
            elegido = ''
            menor = (float('inf'))
            for item in Q:
                if D[item] + EU[item] < menor and item not in S:
                    menor = D[item]
                    elegido = item
            ultimo = elegido
            S.add(elegido)

        destiny = destino
        origin = P[destino]
        # añadimos la ruta inicial
        camino.append((origin,destiny))
        #sumamos el tiempo de esa ruta
        tiempoViaje += distances[(origin,destiny)]
        # Recuperamos el camino
        while True:
            # Cuando estamos en origen rompemos ejecución.
            if origin==origen:
                break
            else:
                destiny = origin
                origin = P[destiny]
                # Se inserta al principio para cumplir con el formato pedido de salida
                camino.insert(0,(origin,destiny))
                tiempoViaje += distances[(origin,destiny)]

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