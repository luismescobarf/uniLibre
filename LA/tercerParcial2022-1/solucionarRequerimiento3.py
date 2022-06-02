#Librerías
import random

"""
Recibir una matriz par cuadrada 
(igual número de filas que de columnas)
de tamaño n, y retornar una cadena de caracteres compuesta
por la concatenación de la palabra que surge
al concatenar los caracteres que se encuentran
en la segunda mitad de la fila superior,
con los caracteres que están en la primera mitad
de la última columna.
Si la matriz no es par, retornar la cadena
"IMPAR"
"""

#Definiciones
#------------

#Función que responde al requerimiento
def generarCadena(matriz):
    
    #Validar si es par
    if len(matriz) % 2 == 0:
    
        """Desarrollar aquí la solución
                que construye la cadena"""                
        
        #Retornar el valor construído
        return cadena
    
    else:
        
        #No es par la matriz
        return "IMPAR"
        
        

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




