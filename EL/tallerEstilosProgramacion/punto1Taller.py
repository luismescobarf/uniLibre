#Sin utilizar funciones de minimización,
# maximización, sin condicionales, sin ciclos,
#sin vectores y todo en un solo bloque.

#Variables de entrada
codigo = "AA0010276"
nota1 = 40
nota2 = 50
nota3 = 39
nota4 = 76
nota5 = 96

#Encontrar la peor nota
notaMenor = nota1
notaMenor = (nota2+notaMenor) - (notaMenor * (bool)(notaMenor//nota2) + nota2 * (bool)(nota2//notaMenor))
notaMenor = (nota3+notaMenor) - (notaMenor * (bool)(notaMenor//nota3) + nota3 * (bool)(nota3//notaMenor))
notaMenor = (nota4+notaMenor) - (notaMenor * (bool)(notaMenor//nota4) + nota4 * (bool)(nota4//notaMenor))
notaMenor = (nota5+notaMenor) - (notaMenor * (bool)(notaMenor//nota5) + nota5 * (bool)(nota5//notaMenor))

#Cálculo del promedio ajustado
promedio100 = (nota1+nota2+nota3+nota4+nota5-notaMenor)/4

#Cambio de escala
promedio5 = promedio100 / 20

#Presentar resultado
print(f"El promedio ajustado del estudiante {codigo} es: {promedio5} ")



