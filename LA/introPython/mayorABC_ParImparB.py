#Algoritmo que recibe tres números y determina cuál de ellos es el mayor, 
# sin utilizar listas o colecciones (condicionales). Luego informar si el mayor es par o impar.

a = int(input("ingrese numero 1: "))
b = int(input("ingrese numero 2: "))
c = int(input("ingrese numero 3: "))
p = int()

if a>b:
    if a>c:
        print(f"{a} es el mayor")
        p=a
    else:
        print(f"{c} es el mayor")
        p=c
else:
    if b>c:
        print(f"{b} es el mayor")
        p=b
    else:
        print(f"{c} es el mayor")
        p=c
    
if (p%2==0):
    print(f"El numero {p} es par.")    
else:
    print(f"El numero {p} es impar.")