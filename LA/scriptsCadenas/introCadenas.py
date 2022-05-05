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

#Cantidad de elementos
print(f"Cantidad de elementos: {len(palabra)}")

#Cada letra en un renglón
for i in range( len(palabra) ):
    print(f"Subíndice {i} letra: {palabra[i]}")