#coding: utf8

#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos 2019-2020           #
#                                                     #
#            Práctica 2                               #
#                                                     #
#            Raúl Alarcón López                       #    
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
        self.vector.append((elemento,valor))
        # Lo añade al diccionario
        self.tamano += 1
        self.diccionario[elemento] = self.tamano
        # Lo mueve hacia arriba
        self.up_heapify(self.tamano)
    
    # Extrae el elemento mínimo del diccionario de prioridad
    def extrae_min(self):
        # Si el tamaño es 0, no devuelve nada
        if self.tamano ==0:
            return None
        # Cambia el mínimo por la última posición...
        self.cambia_elementos(0, self.tamano)
        # Actualiza el diccionario, decrementa el tamaño y
        # reorganiza la pila
        del self.diccionario[self.vector[self.tamano][0]]
        self.tamano -=1
        self.down_heapify(0)
        # Retorna y borra el mínimo del vector, que estaba guardado en el último lugar,
        # en la posición self.tamano+1     
        return self.vector.pop()

    # Actualiza el valor de un elemento 
    def actualiza(self,(elemento,valor)):
        # Se actualiza el elemento
        position = self.diccionario[elemento]
        self.vector[position] = (elemento,valor)        
        # Se saca la posición del padre
        parentPosition = self.nodopadre(position)
        # Y se hace la reorganización correspondiente
        if self.vector[parentPosition][1] > self.vector[position][1]:
            self.up_heapify(position)
        else:
            self.down_heapify(position)
            
    # Borra un elemento
    def borra(self,elemento):
        # Si el elemento no está en el diccionario, vuelve
        if elemento not in self.diccionario:
            return
        # Se intercambia el elemento a borrar, y se 
        # reorganiza la estructura de datos.
        position = self.diccionario[elemento]
        self.cambia_elementos(position, self.tamano)
        # decrementamos el tamaño
        self.tamano -= 1
        # borramos de vector y diccionario
        del self.diccionario[elemento]
        del self.vector[self.tamano+1]
        # reorganizamos
        self.down_heapify(position)
        
    # Reordena el diccionario de prioridad hacia arriba a partir del elemento
    # almacenado en la posicion indice
    def up_heapify(self,indice):
        # Si es la raíz del árbol, no hace nada.
        if indice == 0:
            pass
        # Si el valor del índice es mayor que el del padre
        # se cumple la propiedad.    
        # Si no, hace el intercambio, y llama a la función 
        # recursiva con el padre.     
        else:
            parentPosition = self.nodopadre(indice)
            if(self.vector[indice][1] <= self.vector[parentPosition][1]):
                self.cambia_elementos(parentPosition, indice)
                self.up_heapify(parentPosition)
    
    # Reordena el diccionario de prioridad hacia abajo a partir del elemento
    # almacenado en la posicion indice
    def down_heapify(self,indice):
        # salimos del bucle cuando hemos llegado al final (hoja)
        if self.es_hoja(indice):
            return
        # Extrae los índices de los hijos.
        hijoIz = self.hijo_izquierdo(indice)
        hijoDe = self.hijo_derecho(indice)
        # Lo importante aquí es determinar si se cambia, y por qué hijo
        # se cambia. Esta función también es recursiva.
        # si solo tenemos un hijo, será el izquierdo
        if hijoDe > self.tamano:
            hijo = hijoIz
        # si tenemos dos, nos quedamos con el menor
        elif self.vector[hijoIz][1] > self.vector[hijoDe][1]:
            hijo = hijoDe
        else:
            hijo = hijoIz
        # si el hijo es menor que el elemento
        if self.vector[indice][1] > self.vector[hijo][1]:
            # cambiamos y ordenamos
            self.cambia_elementos(hijo,indice)
            self.down_heapify(hijo)
   
    
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
        return (self.hijo_izquierdo(indice) >= self.tamano) and (self.hijo_derecho(indice) >= self.tamano)
    
    # Devuelve True si el elemento almacenado en la posición indice tiene
    # solamente un hijo.
    
    def un_hijo(self,indice): 
        return (self.hijo_izquierdo(indice) < self.tamano) and (self.hijo_derecho(indice) >= self.tamano)
        
        
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