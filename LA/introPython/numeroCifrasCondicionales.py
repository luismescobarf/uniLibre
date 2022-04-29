#Algoritmo recibe un número y determina la cantidas de cifras

#Recibir el número
num = int(input('Ingrese el número: '))

#Clasificar con condicionales en cascada

#Primer intervalo -> 1 cifra
if num >= 0 and num <= 9:
    print(f"{num} tiene 1 cifra")
else:
    if num >= 10 and num <= 99:
        print(f"{num} tiene 2 cifras")
    else:
        if num >= 100 and num <= 999:
            print(f"{num} tiene 3 cifras")
        else:
            print(f"{num} tiene más de 3 cifras")

        
    
