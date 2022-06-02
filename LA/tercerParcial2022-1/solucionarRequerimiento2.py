#Librerías
import random

"""
Recibir una matriz impar cuadrada 
(igual número de filas que de columnas)
de tamaño n, y retornar una cadena de caracteres compuesta
por la concatenación de la palabra que surge
al concatenar los caracteres que se encuentran
en la mitad de la fila superior,
mitad de la última columna, 
mitad de la fila inferior y primera columna.
Si la matriz no es impar, retornar la cadena
"PAR"
"""

#Definiciones
#------------

#Función que responde al requerimiento
def generarCadena(matriz):
    
    #Validar si es impar
    if len(matriz) % 2 != 0:
    
        """Desarrollar aquí la solución
            que construye la cadena"""
        
        #Retornar el valor construído
        return cadena
    
    else:
        
        #No es impar la matriz
        return "PAR"        
        

#Generar valores de entrada
caracteres = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

#Sección principal
#-----------------

n = int(input("Ingresar dimensión: "))

matriz = []
for _ in range(n):
    filaAuxiliar = []
    for _ in range(n):
        filaAuxiliar.append(random.choice(caracteres))
    matriz.append(filaAuxiliar)
    
#Salida de diagnóstico
print("Matriz ingresada: ")
[print(fila) for fila in matriz]

print(f"Cadena generada -> {generarCadena(matriz)}")