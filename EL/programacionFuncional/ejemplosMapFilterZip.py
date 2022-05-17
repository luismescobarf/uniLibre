import random
import pprint as pp

#List comprehension
coleccion1 = [i for i in range(1,20,2)]
coleccion2 = [random.randint(0,20) for _ in range(1,11)]

print(coleccion1)
print(coleccion2)

print("Elevar al cuadrado los elementos de la primera colección: ")
def cuadrado(x):
    return x**2
print( list(map(cuadrado,coleccion1)) )

print("Sumatoria de las componentes de cada lista: ")
def suma(x,y):
    return x+y
print( list(map(suma,coleccion1,coleccion2)) )
print( list(map(lambda x,y:x+y,coleccion1,coleccion2)) )

#Elevar al cuadrado y restar 1 a la colección 1
print( list(map(lambda x : x-1, map(cuadrado,coleccion1))) )

#Ejemplo de filter:
#Colección2 (Aleatorios) -> Queremos solamente los pares
#Funciones para procesar varios valores de verdad:
#all(True,a==b,False), any([True,a==b,False])
def esPar(x):
    return all([x % 2 == 0,
                x != 0 ])
print("Solo pares colección2:")
print(list(filter(esPar,coleccion2)))

#Ejemplo zip -> listado de tuplas (c1,c1**2)
cuadrados = list(zip(coleccion1, map(cuadrado,coleccion1)))
[print(pareja) for pareja in cuadrados]

#Zip para diccionarios
pp.pprint( dict(zip(coleccion1, map(cuadrado,coleccion1))) )


