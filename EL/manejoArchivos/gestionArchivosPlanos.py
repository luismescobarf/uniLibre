import pprint as pp

#Lectura básica

try:
    #Abrimos la comunicación con el archivo mediante la API del SO
    #manejadorArchivo = open('Estudiantes.txt')        
    with open('Estudiantes.txt') as manejadorArchivo:

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
    pp.pprint(coleccionEstudiantes)
    
except:
    print("Problemas accediendo al archivo")
    
# print("Continuar con una carga por defecto")
# print("Continuar con una carga por defecto")
# print("Continuar con una carga por defecto")


