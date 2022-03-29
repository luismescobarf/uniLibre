#Variables de entrada
Codigo = "AA0010276"
nota1 = 40
nota2 = 50
nota3 = 39
nota4 = 76
nota5 = 96
# Codigo = input("Ingrese el codigo del estudiante: ")
# nota1 = float(input("Ingrese la primera nota: "))
# Conversion1 = (nota1*5.00)/100
# nota2 = float(input("Ingrese la segunda nota: "))
# Conversion2 = (nota2*5.00)/100
# nota3 = float(input("Ingrese la tercera nota: "))
# Conversion3 = (nota3*5.00)/100
# nota4 = float(input("Ingrese la cuarta nota: "))
# Conversion4 = (nota4*5.00)/100
# nota5 = float(input("Ingrese la quinta nota: "))
# Conversion5 = (nota5*5.00)/100
Notas=[nota1,nota2,nota3,nota4,nota5]
Notas.remove(min(Notas))
Promedio100 = sum(Notas)/ len(Notas) 
Promedio5 = round(Promedio100 / 20, 2)
print(f"El promedio ajustado del estudiante {Codigo} es {Promedio5}")