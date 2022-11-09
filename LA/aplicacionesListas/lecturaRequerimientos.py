def cargarBD(ruta):
    
    #Contenedor salida
    matrizBD = []
    
    
    #Intentar abrir el archivo 
    try:
        
        #Ciclo general del recorrido del archivo mientras está abierto
        with open(ruta) as manejadorArchivo: 
            
            #Contador de líneas
            contadorLineas = 0           
         
            #Recorrer cada línea
            for linea_n in manejadorArchivo:
                
                #Cargar línea, limpiar caracteres especiales y volverlo un arreglo
                linea_n = linea_n.strip()
                linea_n = linea_n.split(',')
                
                #Intentar realizar conversión por cada uno de los campos
                linea_formateada = []
                for campo in linea_n:
                    
                    #Intentar realizar la conversión si es posible
                    try:
                        linea_formateada.append(float(campo))
                    except:
                        linea_formateada.append(campo)
                        
                    
                #Teniendo lista la línea, la agregamos a la base de datos en formato matricial
                matrizBD.append(linea_formateada)     
            
    except:
         return 'Error en la carga del archivo csv!!' 
    
    #Retornar la matriz resultante para el procesamiento de indicadores
    return matrizBD 

def convertirSolicitud(texto):
    
    #Base de datos en formato matricial    
    matrizBD = []    
    
    #Partir el texto
    texto = texto.split("\n")          
    
    #Recorrer cada línea o registro del texto partido por movimientos de carro
    for linea_n in texto:              
        
        #Cargar línea, limpiar caracteres especiales y volverlo un arreglo
        # linea_n = linea_n.strip()
        linea_n = linea_n.split(',')       
        
        #Intentar realizar conversión por cada uno de los campos
        linea_formateada = []
        for campo in linea_n:           
            
            #Intentar realizar la conversión si es posible
            try:
                linea_formateada.append(float(campo))
            except:
                linea_formateada.append(campo)
                
            
        #Teniendo lista la línea, la agregamos a la base de datos en formato matricial
        matrizBD.append(linea_formateada)     
            
      
    #Retornar la matriz resultante para el procesamiento de indicadores
    return matrizBD 

def cargaSolicitud(url):
    import requests as req
    resp = req.get(url) 
    return str(resp.text)

#Requerimientos: 
# - Enviar como parámetro a todas las funciones la base de datos y los parámetros que se especifiquen en los requerimientos.
# - No utilizar librerías para resolver los requerimientos, solamente funciones nativas, esto con el fin de aplicar los conceptos de lógica vistos en el curso.

#0a) Fución que reciba un número n y retorna los n primeros registros de la base de datos incluyendo encabezado (lista compuesta)

#0b) Fución que reciba un número m y retorna las m primeras columnas de la base de datos, incluyendo sus encabezados (lista compuesta)

#1) Fución que reciba un listado con el índice de una serie de registros (no necesariamente consecutivos), y retorna una lista con estos registros incluyendo el encabezado

#2) Fución que reciba un listado con el índice de una serie de columnas (no necesariamente consecutivas), y retorna una lista con estas filas incluyendo el encabezado

#3) Desarrollar una función que retorne la edad más alta registrada en la base de datos.

#4) Desarrollar una función que retorne la edad más baja registrada en la base de datos.

#5) Escribir una función que retorna la edad promedio de las personas casadas.

#6) Función que obtiene la edad promedio de las personas solteras.

#7) Función que genera la siguiente lista compuesta, con el conteo de cada una de las edades registradas:
#La primera fila o lista de la lista compuesta presenta el encabezado
#Las siguientes cada una de las edades encontradas y el número de ocurrencias en la base de datos
#Ejemplo:
# [
#     ['Edad', 'Conteo'],
#     [30.0, 150],
#     [33.0, 186],
#     [35.0, 180],
#     [59.0, 71],
#     [36.0, 188],
#     .
#     .
#     .
#     [76.0, 2],
#     [87.0, 1],
#     [84.0, 1]
# ]

#8) Función que genera un listado de los clientes (registros completos) que no han sido contactados aún, para priorizarlos en la siguiente campaña de mercadeo.
#Revisar quiénes son los que no han sido contactados en el archivo bank-names.txt

#9) Retornar el mes en español y completo (es decir una cadena) que con mayor frecuencia se tuvo el último contacto con los clientes bancarios.

#10) De los clientes contactados, cuál es el medio más común utilizado para contactarlos, y cuántas veces fue utilizado. Implementar esto con una función que retorne una lista sencilla que retorne el nombre del medio y el número de veces utilizado.

#11) Desarrollar una función que retorne un listado compuesto, ordenado y con encabezados, indicando las dos ocupaciones o trabajos con mayor balance promedio anual.
#Ejemplo:
# [
#     ['Ocupación', 'Balance'],
#     ['abcdef', 55555],
#     ['xxxxx', 44444]
# ]  

#Espacio recomendado para realizar la definición de las funciones   
#Espacio recomendado para realizar la definición de las funciones   
#Espacio recomendado para realizar la definición de las funciones  
def punto0a(baseDeDatos,n):
    consulta = []
    for i in range(0,n+1):
        consulta.append( baseDeDatos[i] )
    return consulta

def punto0b(baseDeDatos,m):
    consulta = []
    for registro in baseDeDatos:
        consulta.append( registro[0:m] )
    return consulta

def punto1(baseDeDatos, listaSeleccionados):
    consulta = []
    consulta.append(baseDeDatos[0])
    for i in listaSeleccionados:
        consulta.append(baseDeDatos[i])
    return consulta

#Sección principal
#-----------------

#Carga por solicitud web
url = 'https://raw.githubusercontent.com/luismescobarf/uniLibre/main/SO/tallerTematicaPrimerParcial/bank.csv'
baseDeDatos = convertirSolicitud(cargaSolicitud(url))

#Carga si el archivo está en la misma ubicación de este script
# baseDeDatos = cargarBD('bank.csv')

#Llamado de las funciones que responden a los requerimientos para observar sus salidas
#Llamado de las funciones que responden a los requerimientos para observar sus salidas
#Llamado de las funciones que responden a los requerimientos para observar sus salidas

# #Solución punto 0a
# consulta = punto0a(baseDeDatos,5)
# [print(registro) for registro in consulta]

#Solución punto 0b
# [print(registro) for registro in punto0a(punto0b(baseDeDatos,2),10)]

#Solucion punto 1
consulta = punto1(baseDeDatos,[1,3,5])
[print(registro) for registro in consulta]