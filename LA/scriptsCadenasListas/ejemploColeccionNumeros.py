"""
Ejemplo de inicialización de una
lista, que se llenará con 10 números
aleatorios entre 1 y 100.
"""

#Librería para generar aleatorios
import random

#Inicializar lista
listadoNumeros = []

#Iterar 10 veces solicitando aleatorio
for i in range(10):
    #Generar el número aleatorio
    numeroGenerado = random.randint(1,100)
    #Guardar o coleccionarlo
    listadoNumeros.append(numeroGenerado)

#Presentar los números generados
print("Números generados aleatoriamente:")
print(listadoNumeros)