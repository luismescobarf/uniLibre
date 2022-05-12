#Librerías
import random

#Declaración de las funciones
def obtenerPrimeraVocal(nombre):   
    primeraVocal = str()
    
    #Primer recorrido busca la primera vocal
    for letra in nombre:
        if letra in 'aeiou':
            primeraVocal = letra
            break
    
    return primeraVocal

def obtenerPrimeraConsonante(nombre):    
    primeraConsonante = str()    
    #Segundo recorrido busca la primera consonante
    for letra in nombre:
        if letra not in 'aeiou':
            primeraConsonante = letra
            break
    return primeraConsonante

def concatenarPEF(cadena, flotante):
    parteEntera = int(flotante)   
    letraPE = str(parteEntera)            
    cadena = cadena + letraPE
    return cadena

#Sección principal
#-------------------

estudiantes = [
    ['Juan',4.1],
    ['Ana',3.8],
    ['Andrea',5.0],
    ['Pedro',4.9]
]

#Recorrido de estudiantes
for i in range(len(estudiantes)):
    #Extraer el nombre del estudiante i-ésimo
    nombre = estudiantes[i][0]
    #El nombre extraído actualizarlo
    #convirtiéndolo a minúscula
    nombre = nombre.lower()
    
    #Inicializamos el código
    codigo = ''
    
    #Concatenar primera vocal
    codigo = codigo + obtenerPrimeraVocal(nombre)    
        
    #Concatenar primera consonante
    codigo = codigo + obtenerPrimeraConsonante(nombre)
        
    #Incorporar parte entera calificación
    codigo = concatenarPEF(codigo,estudiantes[i][1])
    
    #Incorporar la calificación en los estudiantes
    estudiantes[i].append(codigo)
    
#Mostramos en pantalla la nueva base de datos de estudiantes
print(estudiantes)
        

        
    
    