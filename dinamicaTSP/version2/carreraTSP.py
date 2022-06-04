"""Simulaciones Problema del Agente Viajero en Turtle y resuelto con OR-TOOLS
Luis Miguel Escobar
Juan Manuel Cárdenas
Programa de Ingeniería de Sistemas
Universidad Libre Seccional Pereira"""

#Librerías del solver OR-Tools - GoogleAI
from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

#Librería para mostrar gráficamente soluciones
import matplotlib.pyplot as plt

#Librería para operaciones matemáticas
import math

#Librería animación tortuga y tomas de tiempo
import turtle 
from time import perf_counter

#Librería para aleatoriedad
import random

#Función para dibujar los puntos de la tortuga
#def dibujarPuntosTortuga(coordenadasClientes,tour):	
def dibujarPuntosTortuga(coordenadasClientes,tour,corrimientoX,corrimientoY,nombreEquipo="Equipo"):	
    
	#Obtener las componentes mayores
	componenteXMayor = max(coordenadasClientes,key=lambda x : x[1])[1]
	componenteYMayor = max(coordenadasClientes,key=lambda x : x[2])[2]
		
	factorEscala = 20
	#factorEscala = 8
	#factorEscala = 35
	#corrimientoX = 300
	#corrimientoY = 300
	corrimientoTextoX = 10
	corrimientoTextoY = 10
	tortuga = turtle
	tortuga.penup()
	tortuga.speed(100000)
	tortuga.hideturtle()
	
	#Dibujar los puntos y sus etiquetas	
	for i,tupla in enumerate(coordenadasClientes):		
		
		#Dibujar los puntos
		tortuga.setposition(tupla[1] * factorEscala + corrimientoX ,tupla[2] * factorEscala + corrimientoY)
		tortuga.dot()

		#Dibujar las etiquetas
		tortuga.setposition(tupla[1] * factorEscala + corrimientoX + corrimientoTextoX ,tupla[2] * factorEscala + corrimientoY + corrimientoTextoY)
		tortuga.color('deep pink')
		tortuga.write(i, font=("Verdana", 15, "bold"))
		tortuga.color('black')
	
	#turtle.done()
	tortuga.showturtle()
	
	#Ubicar la tortuga en la ciudad 0
	tortuga.setposition(coordenadasClientes[0][1] * factorEscala + corrimientoX ,coordenadasClientes[0][2] * factorEscala + corrimientoY)
 
	#Pausar antes de proceder a dibujar
	#input()
	
	#Realizar el recorrido recibido	
	tortuga.speed(1)#Disminuir velocidad para simulación
	tortuga.pendown()
	t1_start = perf_counter()#Inicio del recorrido
	
	#Diagnóstico tour orden listado original
	print("Revisando el tour recibido en el dibujado de tortuga:")
	print(tour)	
 
	#Cargar un recorrido basado en el orden de etiquetado
	#tour = range(len(coordenadasClientes))	
	
	#Dibujar las conexiones bajadas en el tour (recibido por parámetro o forzado)
	for ciudad in tour:
		tortuga.goto(coordenadasClientes[ ciudad ][1] * factorEscala + corrimientoX ,coordenadasClientes[ciudad][2] * factorEscala + corrimientoY)
		tortuga.dot("green")
  
	#Dibujar el retorno al punto inicial y pintarlo de azul
	tortuga.goto(coordenadasClientes[ tour[0] ][1] * factorEscala + corrimientoX ,coordenadasClientes[ tour[0] ][2] * factorEscala + corrimientoY)
	tortuga.dot("blue")
	
	#Detener el cronómetro
	t1_stop = perf_counter()
	print("----------------------------------------------------")
	print("Tiempo transcurrido en segundos:", t1_stop-t1_start)
	print("----------------------------------------------------")
	# input()#Pausa antes de mostrar la solución	
 
	#Dibujar el tiempo transcurrido en la GUI de Turtle 
	tiempoTranscurridoTexto = str(round(t1_stop-t1_start,2))
	tortuga.penup()
	tortuga.setposition(componenteXMayor * factorEscala + corrimientoX + corrimientoTextoX + 10, componenteYMayor * factorEscala + corrimientoY + corrimientoTextoY + 10)
	tortuga.pendown()
	tortuga.color('blue')
	tortuga.write("Tiempo transcurrido: "+tiempoTranscurridoTexto, font=("Verdana", 15, "bold"))
	tortuga.color('black')
 
	#Dibujar el nombre del equipo
	tortuga.penup()
	tortuga.setposition(componenteXMayor * factorEscala + corrimientoX + corrimientoTextoX + 10, componenteYMayor * factorEscala + corrimientoY + corrimientoTextoY + 10 - 15)
	tortuga.pendown()
	tortuga.color('green')
	tortuga.write(nombreEquipo, font=("Verdana", 15, "bold"))
	tortuga.color('black')

#Generar coordenadas graficables del camino (arcos solución)
def generarCoordenadasSolucion(coordenadasClientes,tour):
	tourX = []
	tourY = []
	for i in range(0,len(coordenadasClientes)-1):
		tourX.append(coordenadasClientes[ tour[i] ][1])
		tourX.append(coordenadasClientes[ tour[i+1] ][1])
		tourY.append(coordenadasClientes[  tour[i] ][2])
		tourY.append(coordenadasClientes[ tour[i+1] ][2])
		i = i + 1
	#Agregar el retorno
	tourX.append(coordenadasClientes[ tour[-1] ][1])
	tourY.append(coordenadasClientes[ tour[-1] ][2])	
	return tourX,tourY

#Generar coordenadas graficables de todos los arcos (n x n nodos)
def generarCoordenadasGrafoCompleto(coordenadasClientes):
	arcoX = []
	arcoY = []
	#Obtener el número de nodos
	numeroNodos = len(coordenadasClientes)
	for i in range(numeroNodos):
		for j in range(numeroNodos):
			if i != j:
				arcoX.append(coordenadasClientes[ i ][1])
				arcoX.append(coordenadasClientes[ j ][1])
				arcoY.append(coordenadasClientes[ i ][2])
				arcoY.append(coordenadasClientes[ j ][2])		
	return arcoX,arcoY
	
# Función para graficar solución
def dibujarSolucion(coordenadasClientes,tour,optimo=None):

	#Componente x de las coordenadas de los clientes
	componentesX = [i[1] for i in coordenadasClientes]

	#Componente y de las coordenadas de los clientes
	componentesY = [i[2] for i in coordenadasClientes]

	#Draw point based on above x, y axis values	
	plt.scatter(componentesX, componentesY, s=10)	
	
	
	#Generar coordenadas solucion
	coordenadasSolucionX,coordenadasSolucionY = generarCoordenadasSolucion(coordenadasClientes,tour)
	
	#Colocar etiquetas
	etiquetas = range(len(coordenadasClientes))
	#plt.text(componentesX, componentesX, etiquetas, fontsize=9)
	for et in etiquetas:
		plt.annotate(et, (coordenadasClientes[et][1] + 0.05, coordenadasClientes[et][2]))  # add labels			
		
	"""plt.annotate(
        label,
        xy=(x, y), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))"""
	
	#Salida de diagnóstico
	print("Coordenadas solución")
	print(coordenadasSolucionX,coordenadasSolucionY)	
	print(list(zip(coordenadasSolucionX,coordenadasSolucionY)))
	print("Coordenadas problema")
	print(coordenadasClientes)		
	
	#Dibujar camino si llega como parámetro
	if len(tour)>0 and optimo==None:
		plt.plot(coordenadasSolucionX,coordenadasSolucionY,linewidth=0.5)
	

	# Set chart title.
	plt.title("Caso TSP " + str(len(coordenadasClientes)) + " Clientes (Nodos)")	

	# Set x, y label text.
	plt.xlabel("Eje X")
	plt.ylabel("Eje Y")
	plt.show()
 
 # Función para graficar el grafo completo
def dibujarGrafoCompleto(coordenadasClientes):

	#Componente x de las coordenadas de los clientes
	componentesX = [i[1] for i in coordenadasClientes]

	#Componente y de las coordenadas de los clientes
	componentesY = [i[2] for i in coordenadasClientes]

	#Draw point based on above x, y axis values	
	plt.scatter(componentesX, componentesY, s=10, c="black")
	
	#Generar coordenadas de todos los arcos
	coordenadasSolucionX,coordenadasSolucionY = generarCoordenadasGrafoCompleto(coordenadasClientes)
	
	#Colocar etiquetas
	etiquetas = range(len(coordenadasClientes))
	#plt.text(componentesX, componentesX, etiquetas, fontsize=9)
	for et in etiquetas:
		plt.annotate(et, (coordenadasClientes[et][1] + 0.05, coordenadasClientes[et][2]))  # add labels				
	
	#Dibujar arcos	 
	# plt.plot(coordenadasSolucionX,coordenadasSolucionY,linewidth=0.5)
	plt.plot(coordenadasSolucionX,coordenadasSolucionY,'g--',linewidth=0.5)
	# plt.plot(coordenadasSolucionX,coordenadasSolucionY,linewidth=0.5,markeredgecolor='black',markeredgewidth=2)	
 
	# Set chart title.
	plt.title("Grafo Completo Caso TSP " + str(len(coordenadasClientes)) + " Clientes (Nodos)")	

	# Set x, y label text.
	plt.xlabel("Eje X")
	plt.ylabel("Eje Y")
	plt.show()
	

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    """data['distance_matrix'] = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]  # yapf: disable"""
    data['distance_matrix'] = [        
    ]  # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    print('Objective: {} miles'.format(assignment.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]


def distanciaEuclidiana(coordenadaA, coordenadaB):
	#print(coordenadaA)
	#print(coordenadaB)
	#print(coordenadaA[1],coordenadaB[1] )
	#print(coordenadaA[2],coordenadaB[2] )	
	xd = coordenadaA[1]-coordenadaB[1]
	yd = coordenadaA[2]-coordenadaB[2]	
	#input()
	#return pow(  ( pow((coordenadaA[1]-coordenadaB[1]),2)+pow((coordenadaA[2]-coordenadaB[2]),2) ), 0.5   )
	#return math.sqrt( pow((coordenadaA[1]-coordenadaB[1]),2)+pow((coordenadaA[2]-coordenadaB[2]),2) )
	return math.ceil(math.sqrt( xd*xd + yd*yd))


def indicesSolucionesOptimasTSPLIB():
	tourOptimo = [1, 36, 29, 13, 70, 35, 31, 69, 38, 59, 22, 66, 63, 57, 15, 24, 19, 7, 2, 4, 18, 42, 32, 3, 8, 26, 55, 49, 28, 14, 20, 30, 44, 68, 27, 46, 25, 45, 39, 61, 40, 9, 17, 43, 41, 6, 53, 5, 10, 52, 60, 12, 34, 21, 33, 62, 54, 48, 67, 11, 64, 65, 56, 51, 50, 58, 37, 47, 16, 23]
	#Ajustar valores
	decrementar = lambda valor : valor-1	
	return list(map(decrementar,tourOptimo))
	#Salida de diagnóstico
	#print("Tour Optimo: ",tourOptimo)	
	#tourOptimoSubIndicesDecrementados = list(map(decrementar, tourOptimo ))
	#print("Tour Optimo Index: ",tourOptimoSubIndicesDecrementados)
	
	
#Sección principal
#-----------------
#Lectura del archivo
# f = open('eil51.tsp', 'r')	
# f = open('st70.tsp', 'r')
# f = open('pereira.tsp', 'r')
# f = open('pereiraVersion1.tsp', 'r')
f = open('dosquebradasJunio10.tsp', 'r')

#Contenedores
coordenadasClientes = []
matrizDistancias = []

#Recorrer línea a línea el archivo y almacenar las coordenadas
for line in f:		 					
	coordenadasClientes.append(  list(map(int, line.split() ))    )	
#print(coordenadasClientes)
numeroClientes = len(coordenadasClientes)

#Generar la matriz de distancias
for i in range(numeroClientes):
	fila = []
	for j in range(numeroClientes):
		if i==j:
			fila.append(99999)
		else:
			#fila.append( int( distanciaEuclidiana( coordenadasClientes[i], coordenadasClientes[j] ) ) )
			fila.append(  distanciaEuclidiana( coordenadasClientes[i], coordenadasClientes[j] )  )
	matrizDistancias.append(fila)
		
print("Distancias calculadas (Matriz de Distancias):")
[print(fila) for fila in matrizDistancias]

#Agregar matriz de distancias manual

#Caso gr17
"""matrizDistancias = [[0, 633, 0, 257, 390, 0, 91, 661, 228, 0, 412, 227],
[ 169, 383, 0, 150, 488, 112, 120, 267, 0, 80, 572, 196],
[ 77, 351, 63, 0, 134, 530, 154, 105, 309, 34, 29, 0],
[ 259, 555, 372, 175, 338, 264, 232, 249, 0, 505, 289, 262],
[ 476, 196, 360, 444, 402, 495, 0, 353, 282, 110, 324, 61],
[ 208, 292, 250, 352, 154, 0, 324, 638, 437, 240, 421, 329],
[ 297, 314, 95, 578, 435, 0, 70, 567, 191, 27, 346, 83],
[ 47, 68, 189, 439, 287, 254, 0, 211, 466, 74, 182, 243],
[ 105, 150, 108, 326, 336, 184, 391, 145, 0, 268, 420, 53],
[ 239, 199, 123, 207, 165, 383, 240, 140, 448, 202, 57, 0],
[ 246, 745, 472, 237, 528, 364, 332, 349, 202, 685, 542, 157],
[ 289, 426, 483, 0, 121, 518, 142, 84, 297, 35, 29, 36],
[ 236, 390, 238, 301, 55, 96, 153, 336, 0]]"""


# Instantiate the data problem.
data = create_data_model()
data['distance_matrix'] = matrizDistancias

#Salida de diagnóstico
#print(len(data['distance_matrix']))
#input()

# Create the routing index manager.
manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
									   data['num_vehicles'], data['depot'])
# Create Routing Model.
routing = pywrapcp.RoutingModel(manager)

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc.
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
	routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# #Profundización de la búsqueda
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.local_search_metaheuristic = (
    routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
search_parameters.time_limit.seconds = 2
search_parameters.log_search = True

#Dibujer grafo completo antes de resolver (opcional)
dibujarGrafoCompleto(coordenadasClientes)

# Solve the problem.
assignment = routing.SolveWithParameters(search_parameters)

# # Print solution on console.
# if assignment:
# 	print_solution(manager, routing, assignment)

#Obtener del contenedor de la solución arrojado por ORTOOLS
index = routing.Start(0)
plan_output = ''
while not routing.IsEnd(index):
	plan_output += ' {} ->'.format(manager.IndexToNode(index))
	previous_index = index
	index = assignment.Value(routing.NextVar(index))	
plan_output += ' {}\n'.format(manager.IndexToNode(index))

#Obtener el tour generado por el solver
tour = list(map(int, plan_output.split("->") )) 
#Salida de diagnóstico
#print("Ver la ruta antes del split")
#print(   list(map(int, plan_output.split("->") ))   )


#Presentar modo de ejecución
print("------------------------")
print("Simulador Agente Viajero")
print("------------------------")
print("1 - Solución Algoritmo VS Orden de Ingreso")
print("2 - Equipo1 VS Equipo2")
print("3 - Equipo3 VS Equipo4")
print("4 - Final")
print("5 - Algoritmo VS Campeón ")
print("------------------------")
op = input("Ingresar opción (1 por defecto): ")

#Revisar opción seleccionada
if op == '1' or op == str():
    
    #Mostrar solución de OR-Tools en consola si se logró obtener
	if assignment:
		print_solution(manager, routing, assignment)
    
    # #Recorrido tortuga con tour calculado
	# dibujarPuntosTortuga(coordenadasClientes,tour,-300,0,"Algoritmo (Programa)")

	# #Generar un recorrido aleatorizado
	# tourAleatorizado = list(tour)
	# tourAleatorizado.pop(0)
	# tourAleatorizado.pop(-1)
	# random.shuffle(tourAleatorizado)
	# tourAleatorizado.insert(0,0)
	# tourAleatorizado.append(0)
	# dibujarPuntosTortuga(coordenadasClientes,tourAleatorizado,-100,-300,"Orden Etiquetas")
 
 	#Imprimir solución gráfica
	dibujarSolucion(coordenadasClientes,tour)
 
	#Imprimir solución óptima si se tiene para realizar comparación
	#dibujarSolucion(coordenadasClientes,indicesSolucionesOptimasTSPLIB())
 
elif op == '2':
    
	nombresEquipos = list()
	solucionesEquipos = list()

	with open("equipo1vsEquipo2.txt","r") as fSol:
		for linea in fSol:
			lineaLimpia = linea.strip()
			tourArchivo = lineaLimpia.split()
			nombresEquipos.append(tourArchivo[0])
			tourArchivo.pop(0)
			solucionesEquipos.append(list(map(lambda x : int(x),tourArchivo)))
			
	#Salida de diagnóstico
	print("Equipos y soluciones cargadas: ")
	print(nombresEquipos)
	print(solucionesEquipos)

	#Simulación equipo 1    
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[0],-300,0,nombresEquipos[0])
	#Simulación equipo 2
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[1],-100,-300,nombresEquipos[1])
 
	# #Imprimir solución gráfica generada por OR-Tools
	# dibujarSolucion(coordenadasClientes,tour)
 
	input()#Pausar ejecución para revisar el resultado

elif op == '3':
    
	nombresEquipos = list()
	solucionesEquipos = list()

	with open("equipo3vsEquipo4.txt","r") as fSol:
		for linea in fSol:
			lineaLimpia = linea.strip()
			tourArchivo = lineaLimpia.split()
			nombresEquipos.append(tourArchivo[0])
			tourArchivo.pop(0)
			solucionesEquipos.append(list(map(lambda x : int(x),tourArchivo)))
			
	#Salida de diagnóstico
	print("Equipos y soluciones cargadas: ")
	print(nombresEquipos)
	print(solucionesEquipos)

	#Simulación equipo 1    
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[0],-300,0,nombresEquipos[0])
	#Simulación equipo 2
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[1],-100,-300,nombresEquipos[1])
 
	# #Imprimir solución gráfica generada por OR-Tools
	# dibujarSolucion(coordenadasClientes,tour)
 
	input()#Pausar ejecución para revisar el resultado
 
elif op == '4':

	nombresEquipos = list()
	solucionesEquipos = list()

	with open("final.txt","r") as fSol:
		for linea in fSol:
			lineaLimpia = linea.strip()
			tourArchivo = lineaLimpia.split()
			nombresEquipos.append(tourArchivo[0])
			tourArchivo.pop(0)
			solucionesEquipos.append(list(map(lambda x : int(x),tourArchivo)))
			
	#Salida de diagnóstico
	print("Equipos y soluciones cargadas: ")
	print(nombresEquipos)
	print(solucionesEquipos)

	#Simulación equipo 1    
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[0],-300,0,nombresEquipos[0])
	#Simulación equipo 2
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[1],-100,-300,nombresEquipos[1])

	# #Imprimir solución gráfica generada por OR-Tools
	# dibujarSolucion(coordenadasClientes,tour)
 
	input()#Pausar ejecución para revisar el resultado
 
elif op == '5':

	nombresEquipos = list()
	solucionesEquipos = list()

	with open("campeon.txt","r") as fSol:
		for linea in fSol:
			lineaLimpia = linea.strip()
			tourArchivo = lineaLimpia.split()
			nombresEquipos.append(tourArchivo[0])
			tourArchivo.pop(0)
			solucionesEquipos.append(list(map(lambda x : int(x),tourArchivo)))
			
	#Salida de diagnóstico
	print("Equipos y soluciones cargadas: ")
	print(nombresEquipos)
	print(solucionesEquipos)
 
	#Mostrar solución de OR-Tools en consola si se logró obtener
	if assignment:
		print_solution(manager, routing, assignment)

	#Simulación campeón    
	dibujarPuntosTortuga(coordenadasClientes,solucionesEquipos[0],-300,0,nombresEquipos[0])
	#Simulación solución encontrada por el algoritmo
	dibujarPuntosTortuga(coordenadasClientes,tour,-100,-300,"Algoritmo (Programa)")
 
	#Imprimir solución gráfica generada por OR-Tools
	dibujarSolucion(coordenadasClientes,tour)