#Algoritmo que recibe dos números y determina
#cuál es el mayor de ellos.

#Pseudocódigo
#1) Recoger los números
#2) Compararlos a través de una sentencia declarativa.
#3) A partir de ese valor de verdad establecer cuál es el mayor

#1) Recoger los números
a = int(input('Ingresar primer número: '))
b = int(input('Ingresar segundo número: '))

#2) Compararlos a través de una sentencia declarativa.
if a > b:
    print(f"El mayor número es {a}")
else:
    print(f"El mayor número es {b}")