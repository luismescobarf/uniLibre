
estudiantes = [
    ['Juan',4.1],
    ['Ana',3.8],
    ['Andrea',5.0],
    ['Pedro',4.9]
]

#Recorrido de estudiantes
for i in range(len(estudiantes)):
    #Extraer el nombre del estudiante i-ésimo
    nombre = estudiantes[i][0]
    #El nombre extraído actualizarlo
    #convirtiéndolo a minúscula
    nombre = nombre.lower()
    
    #Inicializamos el código
    codigo = ''
    
    #Primer recorrido busca la primera vocal
    for letra in nombre:
        if letra in 'aeiou':
            codigo = codigo + letra
            break
        
    #Segundo recorrido busca la primera consonante
    for letra in nombre:
        if letra not in 'aeiou':
            codigo = codigo + letra
            break
    
    #Incorporar parte entera calificación
    parteEntera = int(estudiantes[i][1])   
    letraPE = str(parteEntera)            
    codigo = codigo + letraPE
    
    #Incorporar la calificación en los estudiantes
    estudiantes[i].append(codigo)
    
#Mostramos en pantalla la nueva base de datos de estudiantes
print(estudiantes)
        

        
    
    