import pprint as pp

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
                linea_n = linea_n.split(';')
                
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
        linea_n = linea_n.split(';')       
        
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


#Carga por solicitud web
url = 'https://raw.githubusercontent.com/luismescobarf/uniLibre/main/LA/aplicacionesListas/extractoBeneficiariosFamiliasEnAccion.csv'
baseDeDatos = convertirSolicitud(cargaSolicitud(url))

#Requerimientos: 
# - No utilizar librerías para resolver los requerimientos, solamente funciones nativas, esto con el fin de aplicar los conceptos de lógica vistos en el curso.

#1) Desarrollar una función que reciba la base de datos y retorne cuántos 
# beneficiarios del programa son hombres.

#2) Desarrollar una función que reciba la base de datos y retorne cuántos 
# beneficiarios del programa son mujeres.

#3) Desarrollar una función que reciba la base de datos y retorne una lista
# con los departamentos, sin repeticiones y sin el encabezado de la columna
# que recibieron el subsidio.

#4) Desarrollar una función que reciba la base de datos y retorne el porcentaje de
#beneficiarios que presentan PRIMARIA como nivel de escolaridad

#5) Desarrollar una función que reciba la base de datos y retorne el listado de etnias registradas en la base de
#datos de beneficiarios, sin repeticiones y sin el encabezado. La misma etnia puede repetirse
# en el listado resultante si presentan caracteres diferentes o alguna variación.

#6) Desarrollar una función que reciba la base de datos y retorne cuántos beneficiarios
#están bancarizados y son mayores de edad, es decir, que el tipo de documento sea 
#diferente a la Tarjeta de Identidad TI

#7) Desarrollar una función que reciba la base de datos y retorne el listado de los municipios
#del Eje Cafetero ('CALDAS','RISARALDA', 'QUINDIO') donde se han realizado beneficios 
# sin repeticiones (se permiten repeticiones  cuando hay variaciones en los caracteres). 
# Se aclara que se requiere el listado de los municipios sin encabezados.


#8) Desarrollar una función que reciba la base de datos de beneficiarios y retorne el porcentaje 
# de menores de edad que esta presenta, es decir, cuyo tipo de documento sea la taerjeta de
#identidad TI

#9) Desarrollar una función que reciba la base de datos y retorne el número de beneficiarios
# que presenta cada una de las etnias sin repeticiones en una lista de listas con el formato
#que se presenta a continuación. Recuerde que la salida debe ser exactamente igual, porque si
# no el requerimiento no quedará satisfecho.

# [['Etnia', 'NoBeneficiarios'],
#  ['AFROCOLOMBIANO – NEGRO', 691],
#  ['ND', 7154],
#  ['INDIGENA', 492],
#  .
#  .
#  .
#  ['ROM O GITANO', 5],
#  ['ROM', 2]]

#10) Desarrollar una función que reciba la base de datos y determine de cuál de los dos
# géneros hay más beneficiarios y cuántos, por lo tanto, debe devolver dos valores
#de forma simultánea, es decir, si son mujeres retornar 'Mujer' y el número correspondiente
# y si son hombres retornar 'Hombre' y el número correspondiente

#11) Desarrollar una función que reciba la base de datos y retorne qué porcentaje de los
#hombres beneficiarios son discapacitados

#12) Desarrollar una función que reciba la base de datos y retorne un listado con los niveles
# de estudio sin repeticiones de los beneficiarios pertenecientes a la etnia INDIGENA


#13) Desarrollar una función que reciba la base de datos y retorne el departamento 
# con el mayor número de beneficiarios


#14) Desarrollar una función que recibe la base de datos del caso de estudio 
# y retorna la cantidad de DESPLAZADOS que hay en el VALLE

#15) Desarrollar una función que recibe la base de datos del caso de estudio 
# y retorna la cantidad de rangos de edad diferentes que hay registrados.

#16) Desarrollar una función que reciba la base de datos y retorne el porcentaje 
# de beneficiarios que reciben el apoyo por pertenecer al SISBEN 

#17) Desarrollar una función que reciba la base de datos y retorne el listado de
# departamentos sin repeticiones con beneficiarios de etnia tipo MESTIZO.

#18) Desarrollar una función que reciba la base de datos y retorne la cantidad
# de mujeres beneficiarias titulares de ANTIOQUIA

#19) Desarrollar una función que reciba la base de datos y retorne el listado de etnias
# sin repeticiones de los hombres beneficiarios en NARIÑO

#20) Desarrollar una función que reciba la base de datos y retorne el porcentaje
# de beneficiarios bancarizados que hay en el departamento de CHOCO

#21) Desarrollar una función que reciba la base de datos y retorne el número de beneficiarios
#que presentan incapacidad

#22) Desarrollar una función que reciba la base de datos y retorne el número de mujeres
# beneficiarias que han alcanzado SECUNDARIA

#23) Desarrollar una función que reciba la base de datos y retorne el listado de departamentos
# sin repeticiones donde existe por lo menos 5 o más beneficiarios NO ACTIVOS

#24) Desarrollar una función que reciba la base de datos y retorne el porcentaje de mujeres
# cuyo tipo de asignación del beneficio es MONETARIO

#25) Desarrollar una función que reciba la base de datos y retorne cuántas mujeres 
#beneficiarias hay en la ciudad de MEDELLIN.

#26) Desarrollar una función que reciba la base de datos y retorne True si la cantidad
#de mujeres beneficiarias discapacitadas en PEREIRA es mayor que la cantidad de 
#hombres discapacitados, y False en caso contrario.

#27) Desarrollar una función que reciba la base de datos y retorne la cantidad de municipios
# de Santander donde hay 5 o más beneficiarios discapacitados.

#28) Desarrollar una función que reciba la base de datos y retorne el porcentaje de beneficiarios
# que cuentan con cédula de ciudadanía.

#29) Desarrollar una función que reciba la base de datos y retorne el listado sin repeticiones
# de municipios del Chocó a los cuales han llegado estos beneficios.

#30) Desarrollar una función que reciba la base de datos y retorne el número de beneficiarios
#que han accedido al beneficio orientado a NUTRICIÓN.

#31) Desarrolllar una función que reciba la base de datos y retorne el listado sin repeticiones
#y sin encabezado, de los tipos de beneficios que ofrece el programa Familias en Acción.

#32) Desarrollar una función que reciba la base de datos y retorne el porcentaje total de 
#beneficiarios inactivos en los principales departamentos del país, es decir,
# de ANTIOQUIA, VALLE y CUNDINAMARCA.

#33) Desarrollar una función que reciba la base de datos y retorne dos números de forma simultánea
#uno con el nombre de mujeres discapacitadas de Pasto, y el segundo con el número de hombres
# discapacitados de Pasto que son beneficiarios del programa.

#34) Desarrollar una función que reciba la base de datos y retorne 
# el número de menores de edad registrados en el departamento de ANTIOQUIA.

#35) Desarrollar una función que reciba la base de datos y retorne el número de hombres
#y el número de mujeres que no tienen definido si presentan o no discapacidad. Lo anterior
# implica una función que retorna estos dos valores de forma simultánea y en el orden establecido.
