#coding: utf8

#######################################################
#######################################################
#													  #
#			Diseño de Algoritmos                      #     
#													  #
#			Práctica 2								  #
#													  #
#			Luis de la Ossa  						  #	
#													  #
#######################################################
#######################################################

from Tkinter import *

import tkFont # Para modificar el tipo de fuente
from time import clock # Funciones de reloj

from mapa import mapa
from caminos import algCaminos

# Esta clase implementa la interfaz gráfica. Permite interactuar con el algoritmo y enseñar el mapa.
class guiPr1:
	
	def __init__(self, master):		
		# Construye el objeto que contiene y trabaja con el mapa.
		self.mapa = mapa()
		# Construye el objeto que contiene los algoritmos de cálculo de caminos a partir del mapa
		self.algoritmos = algCaminos(self.mapa)
		
		
		####################################		
		# Componentes de la interfaz gráfica
		####################################	
			
		# Fuente para los rótulos grandes 
		self.fuenteGrande = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
		
		#####################################
		# Parte de introducción del trayecto
		#####################################		
		Label(text="Trayecto",font=self.fuenteGrande).grid(row=1, column=1, columnspan=2, sticky=W, padx=10)
		
		# Variables que contienen las entradas de los algoritmos que se muestran en la interface.
		# En realidad no son necesarias, pero así no hay que poner dos ciudades cada vez que se quiera hacer una prueba
		self.origenEntradaVar = StringVar()
		self.destinoEntradaVar = StringVar()
		
		self.origenEntradaVar.set('Albacete') # Fija por defecto estos valores
		self.destinoEntradaVar.set('Madrid')
		
		Label(text="Ciudad origen:").grid(row=2, column=1, sticky=W, padx=10)
		self.origenEntrada = Entry(master, width=20,textvariable=self.origenEntradaVar)
		self.origenEntrada.grid(row=2, column=2, padx=5, sticky=E)
		
		Label(text="Ciudad destino:").grid(row=3, column=1, sticky=W,padx=10)
		self.destinoEntrada = Entry(master, width=20,textvariable=self.destinoEntradaVar)
		self.destinoEntrada.grid(row=3, column=2, padx=5, sticky=E)
		
	
		
		#############################################	
		# Botones que llaman a los métodos de cálculo
		#############################################	
		Label(text="Métodos",font=self.fuenteGrande).grid(row=6, column=1, columnspan=1, sticky=W, padx=10)

		# Botones. Cada botón llama a una función de cálculo. 
		# Cuando aceptan argumentos, las funciones se tienen que definir como lambda
		self.dijkstraBoton = Button(master, width=15, text=" Dijkstra ",command=lambda:self.calculaCamino(self.algoritmos.dijkstra)) 
		self.dijkstraBoton.grid(row=7, column=1, columnspan=2)
		
		self.dijkstraeuBoton = Button(master, width=15, text="Dijkstra (Euclídeo)",command=lambda:self.calculaCamino(self.algoritmos.dijkstraConDistanciaEuclidea)) 
		self.dijkstraeuBoton.grid(row=8, column=1, columnspan=2)
		
		self.dijkstraeumeBoton = Button(master, width=15, text="Dijkstra Mejorado",command=lambda:self.calculaCamino(self.algoritmos.dijkstraConDistanciaEuclideaYMejoras)) 
		self.dijkstraeumeBoton.grid(row=9, column=1, columnspan=2)
		
		
		#############################################	
		# Parte de los resultados
		#############################################					
		Label(text="Resultados",font=self.fuenteGrande).grid(row=12, column=1, columnspan=1, sticky=W, padx=10)
		# Salidas
		
		# Variables que contienen las salidas de los algoritmos que se muestran en la interface.
		self.tiempoViajeEntradaVar = StringVar()
		self.nodosVisitadosEntradaVar = StringVar()
		self.aristasVisitadasEntradaVar = StringVar()
		self.tiempoCalculoEntradaVar = StringVar()
		
		Label(text="Tiempo de viaje:").grid(row=13, column=1, sticky=W,padx=10)
		self.tiempoViajeEntrada= Entry(master, width=20, textvariable=self.tiempoViajeEntradaVar)
		self.tiempoViajeEntrada.grid(row=13, column=2, padx=5, sticky=E)
		
		Label(text="Nodos visitados:").grid(row=14, column=1, sticky=W,padx=10)
		self.nodosVisitadosEntrada = Entry(master, width=20, textvariable=self.nodosVisitadosEntradaVar)
		self.nodosVisitadosEntrada.grid(row=14, column=2, padx=5, sticky=E)
		
		Label(text="Aristas visitadas:").grid(row=15, column=1, sticky=W,padx=10)
		self.aristasVisitadasEntrada = Entry(master, width=20, textvariable=self.aristasVisitadasEntradaVar)
		self.aristasVisitadasEntrada.grid(row=15, column=2, padx=5, sticky=E)
		
		Label(text="Tiempo de cálculo:").grid(row=16, column=1, sticky=W,padx=10)
		self.tiempoCalculoEntrada = Entry(master, width=20, textvariable=self.tiempoCalculoEntradaVar)
		self.tiempoCalculoEntrada.grid(row=16, column=2, padx=5, sticky=E)	
		
	
		self.resetBoton = Button(master, text="Reset",command=self.reset)
		self.resetBoton.grid(row=18, column=2)
		
		
		#############################################	
		# Dibujo. Lo obtiene del mapa, y se actualizará desde el propio mapa.	
		#############################################			
		self.canvas =  self.mapa.getCanvas(800, 800) 
		self.canvas.grid(row=0, column=0, rowspan=20, padx=5,pady=10)
		
		
	#############################################################################################
	# Funciones para la lectura de datos
	############################################################################################# 
	
	# Borra los caminos marcados del mapa y del dibujo y lee las entradas.	
	def reset(self):
		self.mapa.borraMarcas()  
		self.tiempoViajeEntradaVar.set('0.0')
		self.nodosVisitadosEntradaVar.set('0')	
		self.aristasVisitadasEntradaVar.set('0')
		self.tiempoCalculoEntradaVar.set('0.0')		

	# Calcula la menor distancia entre dos ciudades mediante el algoritmo pasado como parámetro.
	def calculaCamino(self,algoritmo):
		# Borra marcas del mapa
		self.reset()	
		
		# Almacena el tiempo de inicio
		t1 = clock()	
			
		# Calcula el camino
		origen = self.origenEntrada.get().encode("utf-8") # Trata el String como unicode. Si no, no se corresponde
		destino = self.destinoEntrada.get().encode("utf-8") # con la información que contiene el fichero
		(tViaje,nodos,aristas,camino)=algoritmo(origen,destino) # Algoritmo es una función que se pasa como parámetro
		
		# Almacena el tiempo de finalización.
		t2 = clock()
		tCalculo = t2-t1
		
		# Dibuja las marcas en el mapa		
		self.mapa.anadeMarcasVisitadas(aristas)
		self.mapa.anadeMarcasCamino(camino)
		
		# Almacena las salidas
		self.tiempoViajeEntradaVar.set('%0.3f horas'%(tViaje))
		self.nodosVisitadosEntradaVar.set(len(nodos))	
		self.aristasVisitadasEntradaVar.set(len(aristas))
		self.tiempoCalculoEntradaVar.set('%0.3f ms'%(tCalculo))
		
root = Tk()
root.title("Diseño de Algoritmos 2012/2013 -  Práctica 1: Grafos y algoritmos voraces")
main = guiPr1(root)

mainloop()
