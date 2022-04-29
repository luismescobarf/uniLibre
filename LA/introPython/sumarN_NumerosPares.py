#Algoritmo que suma los números pares hasta
#el número ingresado

num = int(input('Ingresar número: '))

sumatoriaPares = 0

# #Versión for
# for i in range(1,num+1):
#     if i%2==0:
#         #sumatoriaPares = sumatoriaPares + i
#         sumatoriaPares += i
        
# #Versión while
# i = 1
# while i <= num:
#     if i%2==0:        
#         sumatoriaPares += i
#     i = i + 1

print("Mostrar secuencia que se va a generar en el ciclo: ")
print(list(range(2,num+1,2)))

for i in range(2,num+1,2):            
    sumatoriaPares += i
        
print(f"Sumatoria de pares hasta {num} es -> {sumatoriaPares}")


