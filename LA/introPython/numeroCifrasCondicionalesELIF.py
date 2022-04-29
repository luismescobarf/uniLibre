#Algoritmo recibe un número y determina la cantidas de cifras
#Manejo de negativos para la clasificación

#Recibir el número
numeroIngresado = int(input('Ingrese el número: '))

#Manejo si es negativo
num = int()
if numeroIngresado < 0:
    num = numeroIngresado * -1
else:
    num = numeroIngresado

#Clasificar con condicionales en cascada

#Primer intervalo -> 1 cifra
if num >= 0 and num <= 9:
    print(f"{numeroIngresado} tiene 1 cifra")
elif num >= 10 and num <= 99:
    print(f"{numeroIngresado} tiene 2 cifras")
elif num >= 100 and num <= 999:
    print(f"{numeroIngresado} tiene 3 cifras")
else:
    print(f"{numeroIngresado} tiene más de 3 cifras")

        
    
