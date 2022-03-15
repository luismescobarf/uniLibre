import pprint as pp

nodos = []
nodos.append([8,11])#A
nodos.append([10,10])#E
nodos.append([7,8])#B
nodos.append([9,7])#D
nodos.append([9.5,5])#C
tabla_asociativa = ['A','E','B','D','C']
nodoOrigen = input("Ingrese la etiqueta del nodo origen: ")
nodoDestino = input("Ingrese la etiqueta del nodo destino: ")

#Obtener la posición de la etiqueta ingresada origen
posicion_origen = int()
for i,valorTablaAsociativa in enumerate(tabla_asociativa):
    if valorTablaAsociativa == nodoOrigen:
        posicion_origen = i
        break

#Obtener la posición de la etiqueta ingresada destino
posicion_destino = int()
for i,valorTablaAsociativa in enumerate(tabla_asociativa):
    if valorTablaAsociativa == nodoDestino:
        posicion_destino = i
        break

#Calcular la distancia teniendo las posiciones
distanciaNodosIngresados = ((((nodos[posicion_origen][0]-nodos[posicion_destino][0])**2))+(((nodos[posicion_origen][1]-nodos[posicion_destino][1])**2)))**0.5

#Reportar distancia
print(f"La distancia entre {nodoOrigen} y {nodoDestino} es {distanciaNodosIngresados}" )
    
