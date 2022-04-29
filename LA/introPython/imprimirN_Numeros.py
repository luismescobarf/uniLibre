#Algoritmo recibe un número e imprime los números desde
#1 hasta el número recibido

num = int(input('Ingresar número: '))

# print(1)
# print(2)
# print(3)
# .
# .
# print(num)

# #Solución en terminos de while
# i = 0
# while i < num:
#     print(i+1) 
#     i = i + 1

#Solución en términos de para
for i in range(0,num,1):
    print(i+1)
print("------")
#Equivalencias
for i in range(num,2):
    print(i+1)
print("------")    
for i in range(0,num):
    print(i+1)
print("------")

print("Variación -> 2 en 2")
for i in range(0,num,2):
    print(i+1)
print("------")