import pprint as pp
import json
import random

#Lectura básica
def lecturaEstdiantesPlano(rutaArchivo):

    try:
        #Abrimos la comunicación con el archivo mediante la API del SO
        #manejadorArchivo = open('Estudiantes.txt')        
        with open(rutaArchivo) as manejadorArchivo:

            #Estructura de datos que se alimenta de la BD
            coleccionEstudiantes = list()

            #Recorrido de todas las líneas del archivo (cada línea es una entidad del mundo del problema)
            for linea in manejadorArchivo:
                lineaLimpia = linea.strip()
                atributosEstudiante = lineaLimpia.split(' ')
                atributosEstudiante[2] = int(atributosEstudiante[2])
                coleccionEstudiantes.append(atributosEstudiante)    

        # #Cerrar la comunicación
        # manejadorArchivo.close()

        #Estructura de datos -> RAM
        #pp.pprint(coleccionEstudiantes)
        
        return coleccionEstudiantes
        
    except:
        print("Problemas accediendo al archivo")
        
    # print("Continuar con una carga por defecto")
    # print("Continuar con una carga por defecto")
    # print("Continuar con una carga por defecto")

#Modifica la ED -> Guarda en la BD -> Generan efectos colaterales
#Escritura básica
def escrituraEstdiantesPlano(rutaArchivo,nuevoEstudiante=['Pedro','IngCivil',24]):

    try:        
        with open(rutaArchivo,'a') as manejadorArchivo:
            estudianteCaracteres = str()
            for atributo in nuevoEstudiante:
                estudianteCaracteres += str(atributo)+' '
            estudianteCaracteres += '\n'
            manejadorArchivo.write(estudianteCaracteres)
    except:
        print("Problemas actualizando el archivo!!!")
        
#1) Cargar desde el txt a ED
coleccionEstudiantes = lecturaEstdiantesPlano('Estudiantes.txt')
#2) ED Lista/Listas -> ED Diccionario (Profundidad)
diccionarioGrupo = dict()
diccionarioGrupo['NGrupo'] = 'Estructura de Lenguajes'
diccionarioGrupo['Codigo'] = '05'
diccionarioGrupo['Estudiantes'] = list()
for estudiante in coleccionEstudiantes:
    diccionarioGrupo['Estudiantes'].append(
        {
            'Nombre':estudiante[0],
            'Programa':estudiante[1],
            'Edad':estudiante[2],
            'Promedios': [random.randint(0,3),random.randint(0,5),random.randint(0,4)]
        }
    )        
#3) Persistencia en JSON
try:
    with open('GrupoEstudiantes.json','w') as f:
        json.dump(diccionarioGrupo,f)
except:
    print("Error guardando los estudiantes!!")


#4) Carga del primer archivo JSON generado
coleccionPrimerArchivo = dict()
try:
    with open('GrupoEstudiantes1.json') as f:
        coleccionPrimerArchivo = json.load(f)
except:
    print("Error cargando los estudiantes desde JSON!!")

print("Grupo cargado: ")
pp.pprint(coleccionPrimerArchivo)

#Buscar estudiante que se llama Ana y mostrar su promedio en pantalla
notasAna = list()
for estudiante in coleccionPrimerArchivo['Estudiantes']:
    if estudiante['Nombre'] == 'Ana':
        notasAna = estudiante['Promedios']
    
print(f"Promedio de Ana es = { sum(notasAna)/len(notasAna) }")





