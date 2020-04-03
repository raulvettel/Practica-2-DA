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
        self.diccionario[elemento] = valor
        # Lo mueve hacia arriba
        self.tamano += 1
        # Ordenamos el vector por el valor
        self.vector.sort(key=self.sortSecond)

    # Metodo para devolver el segundo elemento del vector para ordenar
    def sortSecond(self,(elemento,valor)):
        return valor
    
    # Extrae el elemento mínimo del diccionario de prioridad
    def extrae_min(self):
        # Si el tamaño es 0, no devuelve nada
        if self.tamano ==0:
            return 
        # Cambia el mínimo por la última posición...
        self.cambia_elementos(0, self.tamano)
        # Actualiza el diccionario, decrementa el tamaño y
        # reorganiza la pila
        self.diccionario.pop(self.vector[self.tamano][0])
        self.tamano -=1
        menor = self.vector.pop()
        self.vector.sort(key=self.sortSecond)
        # Retorna y borra el mínimo del vector, que estaba guardado en el último lugar,
        # en la posición self.tamano+1     
        return menor

    # Actualiza el valor de un elemento 
    def actualiza(self,(elemento,valor)):
        # Se elimina del vector y se vuelve a insertar con el nuevo valor
        self.vector.remove((elemento,self.diccionario[elemento]))
        self.vector.append((elemento,valor))
        # Se actualiza el elemento
        self.diccionario[elemento] = valor
        # Y se hace la reorganización correspondiente
        self.vector.sort(key=self.sortSecond)
            
    # Borra un elemento
    def borra(self,elemento):
        # Si el elemento no está en el diccionario, vuelve
        if self.diccionario.__contains__(elemento):
            # Se intercambia el elemento a borrar, y se 
            # reorganiza la estructura de datos.
            valor = self.diccionario[elemento]
            self.diccionario.pop(elemento)
            self.vector.remove((elemento,valor))
            self.tamano -= 1
        else:
            return    
        
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
        return self.diccionario[elemento]
    
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