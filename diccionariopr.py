#coding: utf8

#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos 2012-2013           #
#                                                     #
#            Práctica 1                               #
#                                                     #
#            Luis de la Ossa                          #    
#                                                     #
#######################################################
#######################################################


# Esta clase debe implementar un diccionario de prioridad
class dicPrioridad:
    
    # Constructor. Opcionalmente toma una lista de pares
    # (elemento,valor)
    def __init__(self,objetos=[]):
        self.diccionario = {}
        self.vector = [ ]
        self.tamano = -1 # Realmente es el índice del último elemento.
        # Se insertan de uno en uno los objetos.
        for (elemento,valor) in objetos:
            self.inserta((elemento,valor))
 
    # Inserta un elemento
    def inserta(self,(elemento,valor)):
        # Lo añade al final
        # Lo añade al diccionario
        # Lo mueve hacia arriba
        pass
    
    # Extrae el elemento mínimo del diccionario de prioridad
    def extrae_min(self):
        # Si el tamaño es 0, no devuelve nada
        # Cambia el mínimo por la última posición...
        self.cambia_elementos(0, self.tamano)
        # Actualiza el diccionario, decrementa el tamaño y
        # reorganiza la pila

        # Implementación 
         
        # Retorna y borra el mínimo del vector, que estaba guardado en el último lugar,
        # en la posición self.tamano+1     
        return self.vector.pop()

    # Actualiza el valor de un elemento 
    def actualiza(self,(elemento,valor)):
        # Se actualiza el elemento        
        # Se saca la posición del padre
        # Y se hace la reorganización correspondiente
        pass
            
    # Borra un elemento
    def borra(self,elemento):
        # Si el elemento no está en el diccionario, vuelve
        # Se intercambia el elemento a borrar, y se 
        # reorganiza la estructura de datos.
        pass    
        
    # Reordena el diccionario de prioridad hacia arriba a partir del elemento
    # almacenado en la posicion indice
    def up_heapify(self,indice):
        # Si es la raíz del árbol, no hace nada.
        # Si el valor del índice es mayor que el del padre
        # se cumple la propiedad.    
        # Si no, hace el intercambio, y llama a la función 
        # recursiva con el padre.     
        pass
  
    
    # Reordena el diccionario de prioridad hacia abajo a partir del elemento
    # almacenado en la posicion indice
    def down_heapify(self,indice):
        # Extrae los índices de los hijos.
        hijoIz = self.hijo_izquierdo(indice)
        hijoDe = self.hijo_derecho(indice)
        
        # Lo importante aquí es determinar si se cambia, y por qué hijo
        # se cambia. Esta función también es recursiva.
   
    
    # Intercambia dos elementos (han de ser padre e hijo)
    def cambia_elementos(self, nodo1, nodo2):
        # Cambia los valores en el diccionario. 
        self.diccionario[self.vector[nodo1][0]] = nodo2
        self.diccionario[self.vector[nodo2][0]] = nodo1
        # Cambia los valores en el vector
        self.vector[nodo2],self.vector[nodo1] = self.vector[nodo1],self.vector[nodo2]        
       
         
    # Devuelve la posición del padre del elemento almacenado en la posición
    # indice del vector    
    def nodopadre(self,indice):    
        if (indice%2==0):  
            return (indice-2) / 2 # Hijo derecho
        else:  
            return (indice-1) / 2 # Hijo izquierdo
    
    # Devuelve la posición del hijo izquierdo del elemento almacenado en la 
    # posición indice del vector        
    def hijo_izquierdo(self,indice): 
        return 2*indice+1
    
    # Devuelve la posición del hijo izquierdo del elemento almacenado en la 
    # posición indice del vector        
    def hijo_derecho(self,indice): 
        return 2*indice+2  
      
    # Devuelve True si el elemento almacenado en la posición indice es una 
    # hoja del árbol.  
    def es_hoja(self,indice): 
        return (self.__hijo_izquierdo(indice) >= self.tamano) and (self.__hijo_derecho(indice) >= self.tamano)
    
    # Devuelve True si el elemento almacenado en la posición indice tiene
    # solamente un hijo.
    
    def un_hijo(self,indice): 
        return (self.__hijo_izquierdo(indice) < self.tamano) and (self.__hijo_derecho(indice) >= self.tamano)
        
        
    # Con estas funciones se premite llamar al diccionario de prioridad como a cualquier
    # otra secuencia    
        
    # Devuelve el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede utilizar 'dp[elemento]'
    def __getitem__(self,elemento):
        indice = self.diccionario[elemento]
        return self.vector[indice][1]   
    
    # Devuelve True si el diccionario contiene el elemento.
    # Si dp es un diccionario de prioridad, se puede usar 'elemento in dp'
    def __contains__(self,elemento):  
        return elemento in self.diccionario   
    
    # Esta función permite actualizar directamente el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede hacer 'dp[elemento]=valor'
    def __setitem__(self, elemento, valor):
        if elemento in self.diccionario:
            self.actualiza((elemento, valor))  
        else:
            self.inserta((elemento, valor))
        
    # Esta función permite actualizar directamente el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede hacer 'del dp[elemento]'        
    def __delitem__(self,elemento):      
        self.borra(elemento)  
                
# Esta función permite comprobar el funcionamiento del diccionario de prioridad.        
def test():
        L = [('A',6), ('B',4), ('C',3), ('D',5), ('E',9), ('F',7), ('G',7)]        
        dp = dicPrioridad(L)
        print dp.extrae_min()
        dp.inserta(('H', 1))
        print dp['F']
        dp.actualiza(('F',3))
        print dp['F']
        print 'F' in dp
        del dp['F']
        print 'F' in dp
        print dp.extrae_min()


 #test()   