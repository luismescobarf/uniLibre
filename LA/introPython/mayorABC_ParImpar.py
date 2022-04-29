#Algoritmo que recibe tres números y determina cuál de ellos es el mayor, 
# sin utilizar listas o colecciones (condicionales). Luego informar si el mayor es par o impar.

a = int(input("ingrese numero 1: "))
b = int(input("ingrese numero 2: "))
c = int(input("ingrese numero 3: "))
p = int()
if (a>b and a>c):
    print("es mayor a")
    p = a
        
if (b>a and b>c):
    print("es mayor b")
    p = b
        
if (c>b and c>a):
    print("es mayor c")
    p = c
    
if (p%2==0):
    print(f"El numero {p} es par.")
    
else:
    print(f"El numero {p} es impar.")