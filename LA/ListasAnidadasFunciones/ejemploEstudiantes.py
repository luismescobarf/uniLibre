notas = [
    ['Juan',4.1],
    ['Ana',3.8],
    ['Andrea',5.0],
    ['Pedro',4.9]
]

#Colección de notas mayores a 4.5
notasMayores = list()
#notasMayores = []

#Recorrido de estudiantes
for i in range(len(notas)):    
    if(notas[i][1]>4.5):
        notasMayores.append(notas[i][1])
        
print(notasMayores)
        
    
    