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
c = int()

#2) Compararlos a través de una sentencia declarativa.
if a > b:
    #3) A partir de ese valor de verdad establecer cuál es el mayor
    print(f"El mayor número es {a}")
    c = a    
else:
    #3) A partir de ese valor de verdad establecer cuál es el mayor
    print(f"El mayor número es {b}")
    c = b    
        
#4) Informar si el mayor es par o impar
    if c % 2 == 0:
        print(f"{c} es par")
    else:
        print(f"{c} es impar") 