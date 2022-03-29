#Funcionalidades

#Menor entre dos valores
def menorValor(a,b):
    return (a+b) - (a * (bool)(a//b) + b * (bool)(b//a))

#Peor nota
def peorNota(nota1,nota2,nota3,nota4,nota5):   
    return menorValor( menorValor( menorValor( menorValor(nota1,nota2) , nota3 ), nota4 ), nota5 ) 

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
#Cálculo del promedio ajustado
#Cambio de escala

#Presentar resultado
print(f"El promedio ajustado del estudiante {codigo} es: {convertirEscala5(promedioAjustado(nota1,nota2,nota3,nota4,nota5, peorNota(nota1,nota2,nota3,nota4,nota5) ))} ")



