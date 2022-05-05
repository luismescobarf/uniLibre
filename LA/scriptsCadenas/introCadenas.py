# Comentario de una línea
"""
Esto
es 
un
comentario
varias 
líneas
"""

""""
Ejemplo: Algoritmo que reciba una cadena
e imprima la primera letra, la última letra
y luego cada letra en un renglón separado
"""

#Recibir cadena
palabra = input('Ingrese una palabra: ')

#Imprimir primera letra
print(f"Primera letra: {palabra[0]}")

#Imprimir última letra
print(f"Última letra: {palabra[ len(palabra)-1 ]}")
print(f"Última letra (subíndice negativo): {palabra[ -1 ]}")

#Cantidad de elementos
print(f"Cantidad de elementos: {len(palabra)}")

#Cada letra en un renglón
for i in range( len(palabra) ):
    print(f"Subíndice {i} letra: {palabra[i]}")
    
#Recorrer todos los elementos sin subíndice
print("Recorrido por colección:")
for letra in palabra:
    print(letra)
    
#Imprimir las primeras tres letras de una palabra recibida
print("Primera tres letras de la cadena: ")
for i in range (3):
    print(palabra[i])
    
#Imprimir las primeras tres letras con slice
print("Emplando slice: ")
print( palabra[:3] )

#Slice especificando
pedazoPalabra = palabra[3:5]
print(f"Pedazo obtenido: {pedazoPalabra}")