#Algoritmo que recibe dos números y determina
#cuál es el mayor de ellos. 
#Revisar luego si el mayor es par o impar

#Pseudocódigo
#1) Recoger los números
#2) Compararlos a través de una sentencia declarativa.
#3) A partir de ese valor de verdad establecer cuál es el mayor
#4) Informar si el mayor es par o impar

#1) Recoger los números
a = int(input('Ingresar primer número: '))
b = int(input('Ingresar segundo número: '))

#2) Compararlos a través de una sentencia declarativa.
if a > b:
    #3) A partir de ese valor de verdad establecer cuál es el mayor
    print(f"El mayor número es {a}")    
    #4) Informar si el mayor es par o impar
    if a % 2 == 0:
        print(f"{a} es par")
    else:
        print(f"{a} es impar")
else:
    #3) A partir de ese valor de verdad establecer cuál es el mayor
    print(f"El mayor número es {b}")
    #4) Informar si el mayor es par o impar
    if b % 2 == 0:
        print(f"{b} es par")
    else:
        print(f"{b} es impar")    