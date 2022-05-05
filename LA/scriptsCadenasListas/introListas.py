lista = ["hola",4,True,"carro",3.5,'c',"prueba"]

print("Contenido de la lista")
for i in range(len(lista)):
    print(lista[i])
print("----------------")    
for elemento in lista:
    print(elemento)

print("Probando notación de listas:")
    
#Acceder a la última letra de la primera posición (cadena)
print(lista[0][-1])

#Última posición de la lista
print(lista[-1])

#Toda la palabra de la primera posición de la lista
print(lista[0])

"""
Imprimir la última letra
de todos los elementos de la lista
que sean palabras
"""
print("Últimas letras--------------")
for i in range(len(lista)):
    if isinstance(lista[i],str):
        print(lista[i][-1])
        
#Actualizar contenido de la lista
lista2 = ["hola",
         4,
         True,
         "carro",
         3.5,
         'c',
         "prueba"]

print("Contenido antes de modificar: ")
print(lista2)  

#Actualización
lista2[0] = "Nueva palabra"
lista2[4] = lista2[4] + 0.5
#Eliminación
lista2.pop()
#Adicionar al final
lista2.append("CADENA")
#Insertar o adicionar al comienzo
lista2.insert(0,155)


print("Contenido después de modificar: ")
print(lista2) 


