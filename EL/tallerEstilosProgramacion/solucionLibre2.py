#Variables de entrada
codigo = "AA0010276"
nota1 = 40
nota2 = 50
nota3 = 39
nota4 = 76
nota5 = 96

#Coleccionar las notas
listaNotas = [nota1, nota2, nota3, nota4, nota5]

#Identificar el menor
notaMenor = 99999
posicion = int()
for i in range(len(listaNotas)):
    if listaNotas[i] < notaMenor:
        notaMenor = listaNotas[i]
        posicion = i
        
#Descartar la peor nota
listaNotas.pop(posicion)
        
#Calcular el promedio ajustado en escala de 0 a 100
promedio100 = sum(listaNotas) / len(listaNotas)

#Cambio de escala
promedio5 = round( promedio100/20  ,2)

#Presentar el resultado con el mensaje establecido
print(f"El promedio ajustado del estudiante {codigo} es: {promedio5} ")
