#coding: utf8

#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos                     #
#                                                     #
#            Práctica 2                               #
#                                                     #
#            Luis de la Ossa                          #    
#                                                     #
#######################################################
#######################################################

from Tkinter import Canvas
import sys
  
# Esta clase implementa las funcionalidades relacionadas con el mapa.
# Básicamente lee y almacena la información a partir de los ficheros, 
# y proporciona las funciones para el dibujo.

class mapa:
        
    # Constructor
    def __init__(self):
     
        # Estructuras de datos que guardan las ciudades, pueblos y sus respectivas coordenadas.
        self.ciudades = []
        self.pueblos = []
        self.coordenadas = {}

        # Estructuras de datos que guardan las carreteras y autovías
        self.carreteras = []
        self.distancias = {}
        self.autovias = []
        
        # Carga todos los datos
        self.cargaCiudades() 
        self.cargaPueblos()
        self.cargaCarreteras()
        self.cargaAutovias()
        
        # Estructura de datos que contiene los caminos 
        self.marcadasCamino = []
        # Estructura de datos que contiene los caminos marcados
        self.marcadasVisitadas = []
        # Guarda los identificadores de las líneas marcadas para poderlas borrar
        self.lineasMarcadas = {}        
        

    #############################################################################################
    # Funciones para la lectura de datos
    #############################################################################################  
    
    # Carga la lista de ciudades y sus coordenadas relativas a Madrid desde el fichero ciudades    
    def cargaCiudades(self):                    
        for linea in file('ciudades'): 
            ciudad, x, y = linea.strip().split(':')
            self.ciudades.append(ciudad)
            self.coordenadas[ciudad]=(float(x),float(y))
            
    #Carga la lista de pueblos y sus coordenadas relativas a Madrid desde el fichero pueblos      
    def cargaPueblos(self):                    
        for linea in file('pueblos'): 
            pueblo, x, y = linea.strip().split(':')
            self.pueblos.append(pueblo)
            self.coordenadas[pueblo]=(float(x),float(y))       
            
    #Carga la lista de carreteras
    def cargaCarreteras(self):
        for linea in file('carreteras'):
            origen,destino,distancia =  linea.strip().split(':')
            self.carreteras.append((origen,destino))  
            self.distancias[(origen,destino)]=float(distancia)
            
    #Carga la lista de autovías
    def cargaAutovias(self):
        for linea in file('autovias'):
            origen,destino,distancia =  linea.strip().split(':')           
            self.autovias.append((origen,destino))  
            self.distancias[(origen,destino)]=float(distancia)          
            
    #############################################################################################
    # Funciones para añadir y quitar marcas
    #############################################################################################   
    
    # Añade un conjunto de marcas del camino al mapa y los dibuja
    def anadeMarcasCamino(self,marcas):
        for marca in marcas:
            self.anadeMarcaCamino(marca)
    
    # Añade una marca del camino al mapa y la dibuja (sobre una carretera)
    def anadeMarcaCamino(self,marca): 
        (origen,destino) = marca
        if (origen,destino) in self.carreteras or (destino,origen) in self.carreteras \
        or (origen,destino) in self.autovias or (destino,origen) in self.autovias:
            self.marcadasCamino.append(marca) 
            if self.canvas!=None:
                self.dibujaMarcaCamino(marca) 
        else:
            print 'No existe la carretera '+marca     
            
    # Añade un conjunto de marcas de aristas visitadas al mapa y los dibuja
    def anadeMarcasVisitadas(self,marcas):
        for marca in marcas:
            self.anadeMarcaVisitadas(marca)
    
    # Añade una marca al mapa y la dibuja (sobre una carretera)
    def anadeMarcaVisitadas(self,marca): 
        (origen,destino) = marca
        if (origen,destino) in self.carreteras or (destino,origen) in self.carreteras \
        or (origen,destino) in self.autovias or (destino,origen) in self.autovias:
            self.marcadasVisitadas.append(marca) 
            if self.canvas!=None:
                self.dibujaMarcaVisitada(marca) 
        else:
            print 'No existe la carretera '+marca               
              
    # Borra todas las marcas del mapa  
    def borraMarcas(self):
        self.marcadasCamino = []
        self.marcadasVisitadas = []
        # Las borra del dibujo
        for linea in self.lineasMarcadas.values():
            self.canvas.delete(linea)
       
      
       
    #############################################################################################
    # Funciones para el dibujo del mapa
    #############################################################################################
    
    # Crea el dibujo a partir de los datos del mapa y las marcas presentes y devuelve la referencia
    def getCanvas(self, altura=800, anchura=800):   
        # Recalcula dimension,centro y escala en función de el tamaño del mapa.
        self.altura = altura
        self.anchura = anchura
        self.centroX = anchura/2-(anchura*0.025) # La pequeña corrección es para centrar el mapa, ya que Madrid no está en el centro en realidad
        self.centroY = altura/2-(altura*0.05) 
        self.escalaX = anchura/1000.0
        self.escalaY = altura/1000.0  
                      
        # Crea el mapa, que se queda almacenado en el objeto
        self.canvas = Canvas(height=altura, width=anchura, background="white") 
         
        # Añade todos los componentes 
        for ciudad in self.ciudades:
            self.dibujaCiudad(ciudad)     
            
        for pueblo in self.pueblos:
            self.dibujaPueblo(pueblo)     
             
        for carretera in self.carreteras:
            self.dibujaCarretera(carretera);
            
        for autovia in self.autovias:
            self.dibujaAutovia(autovia);            
            
        for marcaCamino in self.marcadasCamino:
            self.dibujaMarcaCamino(marcaCamino);   
            
        for marcaVisitada in self.marcadasVisitadas:
            self.dibujaMarcaVisitada(marcaVisitada);   
          
        #Devuelve el objeto canvas    
        return self.canvas    
        
         
    # Recalcula la posición de una ciudad de acuerdo al tamaño del dibujo     
    def calculaPos(self,(x,y)):
        return (x*self.escalaX+self.centroX , y*self.escalaY+self.centroY)

    # Dibuja cada ciudad como un círculo rojo de radio 4 píxeles
    def dibujaCiudad(self,ciudad):
        (posX,posY) = self.calculaPos(self.coordenadas[ciudad])
        self.canvas.create_oval(posX-4,posY-4,posX+4,posY+4,fill='red')
        
    # Dibuja cada ciudad como un círculo rojo de radio 2 píxeles        
    def dibujaPueblo(self,pueblo):
        (posX,posY) = self.calculaPos(self.coordenadas[pueblo])    
        self.canvas.create_oval(posX-2,posY-2,posX+2,posY+2,fill='red')
        
    # Dibuja una carretera como una línea negra de un punto de ancho
    def dibujaCarretera(self,(origen,destino)):
        (posXOrigen,posYOrigen) = self.calculaPos(self.coordenadas[origen])
        (posXDestino,posYDestino) = self.calculaPos(self.coordenadas[destino])
        self.canvas.create_line(posXOrigen,posYOrigen,posXDestino,posYDestino,fill='black', width=1)
        
    # Dibuja una autovía como una línea azul con dos puntos de ancho
    def dibujaAutovia(self,(origen,destino)):
        (posXOrigen,posYOrigen) = self.calculaPos(self.coordenadas[origen])
        (posXDestino,posYDestino) = self.calculaPos(self.coordenadas[destino])
        self.canvas.create_line(posXOrigen,posYOrigen,posXDestino,posYDestino,fill='blue', width=2)        
        
    # Dibuja las marcas del camino  como líneas rojas con 4 puntos de ancho 
    def dibujaMarcaCamino(self,(origen,destino)):
        (posXOrigen,posYOrigen) = self.calculaPos(self.coordenadas[origen])
        (posXDestino,posYDestino) = self.calculaPos(self.coordenadas[destino])
        self.lineasMarcadas[(origen,destino)] = self.canvas.create_line(posXOrigen,posYOrigen,posXDestino,posYDestino,fill='red', width=4)

    # Dibuja las marcas del camino  como líneas verdes con 4 puntos de ancho 
    def dibujaMarcaVisitada(self,(origen,destino)):
        (posXOrigen,posYOrigen) = self.calculaPos(self.coordenadas[origen])
        (posXDestino,posYDestino) = self.calculaPos(self.coordenadas[destino])
        self.lineasMarcadas[(origen,destino)] = self.canvas.create_line(posXOrigen,posYOrigen,posXDestino,posYDestino,fill='green', width=2)
        
        
        
        