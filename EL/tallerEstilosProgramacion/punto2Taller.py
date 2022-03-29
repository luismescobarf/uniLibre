#Funcionalidades

#Menor entre dos valores
def menorValor(a,b):
    return (a+b) - (a * (bool)(a//b) + b * (bool)(b//a))

#Peor nota
def peorNota(nota1,nota2,nota3,nota4,nota5):
    notaMenor = nota1    
    notaMenor = menorValor(nota2,notaMenor)
    notaMenor = menorValor(nota3,notaMenor)
    notaMenor = menorValor(nota4,notaMenor)
    notaMenor = menorValor(nota5,notaMenor)
    return notaMenor    

#Promedio ajustado
def promedioAjustado(nota1,nota2,nota3,nota4,nota5,notaMenor):
    return (nota1+nota2+nota3+nota4+nota5-notaMenor)/4

#Cambio de escala
def convertirEscala5(nota100):
    return nota100/20

#Sección principal
#-----------------

#Variables de entrada
codigo = "AA0010276"
nota1 = 40
nota2 = 50
nota3 = 39
nota4 = 76
nota5 = 96

#Encontrar la peor nota
notaMenor = peorNota(nota1,nota2,nota3,nota4,nota5)

#Cálculo del promedio ajustado
promedio100 = promedioAjustado(nota1,nota2,nota3,nota4,nota5,notaMenor)

#Cambio de escala
promedio5 = convertirEscala5(promedio100)

#Presentar resultado
print(f"El promedio ajustado del estudiante {codigo} es: {promedio5} ")



