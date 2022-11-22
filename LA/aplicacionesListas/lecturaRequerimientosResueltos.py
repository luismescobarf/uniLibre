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
# - Enviar como parámetro a todas las funciones la base de datos y los parámetros que se especifiquen en los requerimientos.
# - No utilizar librerías para resolver los requerimientos, solamente funciones nativas, esto con el fin de aplicar los conceptos de lógica vistos en el curso.

#1) Desarrollar una función que reciba la base de datos y retorne cuántos 
# beneficiarios del programa son hombres.

def punto1(baseDeDatos):
    numeroBeneficiariosHombres = 0
    for registro in baseDeDatos:
        if registro[7] == 'Hombre':
            numeroBeneficiariosHombres += 1
    return numeroBeneficiariosHombres

print("Punto 1)---------------------------------------------")
print(f"Número de beneficiarios hombres: {punto1(baseDeDatos)}")

#2) Desarrollar una función que reciba la base de datos y retorne cuántos 
# beneficiarios del programa son mujeres.

def punto2(baseDeDatos):
    numeroBeneficiariosMujer = 0
    for registro in baseDeDatos:
        if registro[7] == 'Mujer':
            numeroBeneficiariosMujer += 1
    return numeroBeneficiariosMujer

print("Punto 2)---------------------------------------------")
print(f"Número de beneficiarios mujeres: {punto2(baseDeDatos)}")

#3) Desarrollar una función que reciba la base de datos y retorne una lista
# con los departamentos, sin repeticiones y sin el encabezado de la columna
# que recibieron el subsidio.

def punto3(baseDeDatos):
    listadoDepartamentos = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][9] not in listadoDepartamentos:
            listadoDepartamentos.append(baseDeDatos[i][9]) 
    return listadoDepartamentos

print("Punto 3)---------------------------------------------")
print("Listado de departamentos beneficiados: ")
pp.pprint(punto3(baseDeDatos))

#4) Desarrollar una función que reciba la base de datos y retorne el porcentaje de
#beneficiarios que presentan PRIMARIA como nivel de escolaridad

def punto4(baseDeDatos):
    conteoPrimaria = 0
    for registro in baseDeDatos:
        if registro[8] == 'PRIMARIA':
            conteoPrimaria += 1
    return (conteoPrimaria/(len(baseDeDatos)-1)) * 100

print("Punto 4)---------------------------------------------")
print(f"El porcentaje de beneficiarios con nivel de estudios de primaria es: {punto4(baseDeDatos)}")

#5) Desarrollar una función que reciba la base de datos y retorne el listado de etnias registradas en la base de
#datos de beneficiarios, sin repeticiones y sin el encabezado. La misma etnia puede repetirse
# en el listado resultante si presentan caracteres diferentes o alguna variación.

def punto5(baseDeDatos):
    listadoEtnias = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][5] not in listadoEtnias:
            listadoEtnias.append(baseDeDatos[i][5])
    return listadoEtnias

print("Punto 5)---------------------------------------------")
print("Listado de etnias : ")
pp.pprint(punto5(baseDeDatos))

#6) Desarrollar una función que reciba la base de datos y retorne cuántos beneficiarios
#están bancarizados y son mayores de edad, es decir, que el tipo de documento sea 
#diferente a la Tarjeta de Identidad TI

def punto6(baseDeDatos):
    numeroBancarizados = 0
    for registro in baseDeDatos:
        if registro[0] == 'SI' and registro[14] != 'TI':
            numeroBancarizados += 1
    return numeroBancarizados

print("Punto 6)---------------------------------------------")
print(f"El número de beneficiarios bancarizados y mayores de edad es {punto6(baseDeDatos)}")

#7) Desarrollar una función que reciba la base de datos y retorne el listado de los municipios
#del Eje Cafetero ('CALDAS','RISARALDA', 'QUINDIO') donde se han realizado beneficios 
# sin repeticiones (se permiten repeticiones  cuando hay variaciones en los caracteres). 
# Se aclara que se requiere el listado de los municipios sin encabezados.

def punto7(baseDeDatos):
    listadoMunicipios = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][9] in ['CALDAS','RISARALDA', 'QUINDIO'] and (baseDeDatos[i][10] not in listadoMunicipios):
            listadoMunicipios.append(baseDeDatos[i][10])
    return listadoMunicipios

print("Punto 7)---------------------------------------------")
print("Listado de municipios del Eje Cafetero con beneficiarios: ")
print(punto7(baseDeDatos))

#8) Desarrollar una función que reciba la base de datos de beneficiarios y retorne el porcentaje 
# de menores de edad que esta presenta, es decir, cuyo tipo de documento sea la taerjeta de
#identidad TI

def punto8(baseDeDatos):
    numeroMenoresEdad = 0
    for registro in baseDeDatos:
        if registro[14] == 'TI':
            numeroMenoresEdad += 1
    return (numeroMenoresEdad/(len(baseDeDatos)-1))*100

print("Punto 8)---------------------------------------------")
print(f"El porcentaje de menores de edad es: {punto8(baseDeDatos)}")

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

def punto9(baseDeDatos):
    consulta = [['Etnia','NoBeneficiarios']]
    #Obtener el conjunto de etnias
    etnias = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][5] not in etnias:
            etnias.append(baseDeDatos[i][5])
    for etnia in etnias:
        conteoEtnia = 0
        for registro in baseDeDatos:
            if etnia == registro[5]:
                conteoEtnia += 1
        consulta.append([etnia,conteoEtnia])
    return consulta

print("Punto 9)---------------------------------------------")
pp.pprint(punto9(baseDeDatos))
print(f"Totalización de la consulta: { sum(list(map(lambda x:x[1],punto9(baseDeDatos)[1:]))) }")
print(f"Total de registros -> {len(baseDeDatos)-1}")

#10) Desarrollar una función que reciba la base de datos y determine de cuál de los dos
# géneros hay más beneficiarios y cuántos, por lo tanto, debe devolver dos valores
#de forma simultánea, es decir, si son mujeres retornar 'Mujer' y el número correspondiente
# y si son hombres retornar 'Hombre' y el número correspondiente

def punto10(baseDeDatos):
    conteoHombres = 0
    conteoMujeres = 0
    for registro in baseDeDatos:
        if registro[7] == 'Mujer':
            conteoMujeres += 1
        if registro[7] == 'Hombre':
            conteoHombres += 1
    
    if conteoHombres > conteoMujeres:
        return 'Hombre', conteoHombres
    else:
        return 'Mujer', conteoMujeres
    
print("Punto 10)---------------------------------------------")
print(f"El género con mayor número de beneficiarios es: {punto10(baseDeDatos)}")

#11) Desarrollar una función que reciba la base de datos y retorne qué porcentaje de los
#hombres beneficiarios son discapacitados

def punto11(baseDeDatos):
    conteoHombres = 0
    hombresDiscapacitados = 0
    for registro in baseDeDatos:
        if registro[7] == 'Hombre':
            conteoHombres += 1
            if registro[3] == 'SI':
                hombresDiscapacitados += 1
    return (hombresDiscapacitados/conteoHombres)*100

print("Punto 11)---------------------------------------------")
print(f"El porcentaje de hombres discapacitados es: {punto11(baseDeDatos)}")

#12) Desarrollar una función que reciba la base de datos y retorne un listado con los niveles
# de estudio sin repeticiones de los beneficiarios pertenecientes a la etnia INDIGENA


def punto12(baseDeDatos):
    listadoNivelesEstudioIndigena = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][5] == 'INDIGENA' and (baseDeDatos[i][8] not in listadoNivelesEstudioIndigena):
            listadoNivelesEstudioIndigena.append(baseDeDatos[i][8])
    return listadoNivelesEstudioIndigena

print("Punto 12)---------------------------------------------")
print("Listado niveles de estudio etnia INDIGENA: ")
print(punto12(baseDeDatos))

#13) Desarrollar una función que reciba la base de datos y retorne el departamento 
# con el mayor número de beneficiarios

def punto13(baseDeDatos):
    #Obtener el listado de departamentos
    listadoDepartamentos = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][9] not in listadoDepartamentos:
            listadoDepartamentos.append(baseDeDatos[i][9])

    #Preparar lista del ranking
    listadoConteos = []
                
    #Conteo por cada departamento
    for departamento in listadoDepartamentos:
        conteoDepartamento = 0
        for registro in baseDeDatos:
            if registro[9] == departamento:
                conteoDepartamento += 1
        listadoConteos.append([departamento,conteoDepartamento])
    
    # print()
    # pp.pprint(listadoConteos)
    # print()
    
    #Recorrer el listado de departamentos
    departamentoMayor = str()
    conteoMayor = -1000
    for infoDepto in listadoConteos:
        if infoDepto[1] > conteoMayor:
            conteoMayor = infoDepto[1]
            departamentoMayor = infoDepto[0]
    
    return departamentoMayor

print("Punto 13)---------------------------------------------")
print(f"Departamento con mayor número de beneficiarios: {punto13(baseDeDatos)}")


#14) Desarrollar una función que recibe la base de datos del caso de estudio 
# y retorna la cantidad de DESPLAZADOS que hay en el VALLE

def punto14(baseDeDatos):
    
    #Departamento -> Columna 9
    #Tipo de población -> Columna 15
    conteoDesplazadosValle = 0
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][9] == 'VALLE' and baseDeDatos[i][15] == 'DESPLAZADOS':
            conteoDesplazadosValle += 1
            
            # #Salida de diagnóstico
            # print(f"Columna Departamento -> {baseDeDatos[i][9]}")
            # print(f"Columna Tipo de Población -> {baseDeDatos[i][15]}")
            # input()
            
    return conteoDesplazadosValle   
    

print("Punto 14)---------------------------------------------")
print(f"Desplazados que hay en el departamento del Valle: {punto14(baseDeDatos)}")

#15) Desarrollar una función que recibe la base de datos del caso de estudio 
# y retorna la cantidad de rangos de edad diferentes que hay registrados.

def punto15(baseDeDatos):
    listadoRangosEdad = []
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][19] not in listadoRangosEdad:
            listadoRangosEdad.append(baseDeDatos[i][19])
    
    # #Salida de diagnóstico
    # print(f"Rangos de edad registrados: {listadoRangosEdad}")
    
    return len(listadoRangosEdad)            
    

print("Punto 15)---------------------------------------------")
print(f"Cantidad de rangos de edad diferentes registrados: {punto15(baseDeDatos)}")

#16) Desarrollar una función que reciba la base de datos y retorne el porcentaje 
# de beneficiarios que reciben el apoyo por pertenecer al SISBEN 

def punto16(baseDeDatos):    
    
    # Salida de diagnóstico tipos de población
    # valoresTipoPoblacion = []
    # for i in range(1,len(baseDeDatos)):
    #     if baseDeDatos[i][15] not in valoresTipoPoblacion:
    #         valoresTipoPoblacion.append(baseDeDatos[i][15])
    
    # print()
    # print()
    # pp.pprint(valoresTipoPoblacion)
    # input()
    
    #Solución del requerimiento
    numeroBeneficiariosSisben = 0
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][15] == 'SISBEN':
            numeroBeneficiariosSisben += 1
            
    #Retornar el porcentaje
    return  (numeroBeneficiariosSisben/(len(baseDeDatos)-1)) * 100   
    

print("Punto 16)---------------------------------------------")
print(f"Procentaje de beneficiarios que reciben el apoyo por pertenecer al SISBEN: {punto16(baseDeDatos)}")

#17) Desarrollar una función que reciba la base de datos y retorne el listado de
# departamentos sin repeticiones con beneficiarios de etnia tipo MESTIZO.

def punto17(baseDeDatos):    
    
    # #Salida de diagnóstico
    # etniasRegistradas = []
    # for i in range(1,len(baseDeDatos)):
    #     if baseDeDatos[i][5] not in etniasRegistradas:
    #         etniasRegistradas.append(baseDeDatos[i][5])
    # print()
    # print()    
    # pp.pprint(etniasRegistradas)
    # input()
    
    departamentosBeneficiariosMestizos = []
    for i in range(1,len(baseDeDatos)):
        if (baseDeDatos[i][9] not in departamentosBeneficiariosMestizos) and (baseDeDatos[i][5]=='MESTIZO'):
            departamentosBeneficiariosMestizos.append(baseDeDatos[i][9])
    return departamentosBeneficiariosMestizos   

print("Punto 17)---------------------------------------------")
print(f"Departamentos con beneficiarios de etnia tipo MESTIZO: {punto17(baseDeDatos)}")


#18) Desarrollar una función que reciba la base de datos y retorne la cantidad
# de mujeres beneficiarias titulares de ANTIOQUIA

def punto18(baseDeDatos):
    numeroMujeresTitularesAntioquia = 0    
    for i in range(1,len(baseDeDatos)):       
        
        if (baseDeDatos[i][7] == 'Mujer') and (baseDeDatos[i][9] == 'ANTIOQUIA') and (baseDeDatos[i][20] == 'SI'):        
            numeroMujeresTitularesAntioquia += 1            
            # #Salida de diagnóstico
            # print()
            # print("Campos observados: ")
            # print(f"{baseDeDatos[i][7]} {baseDeDatos[i][9]} {baseDeDatos[i][20]}")
            # input()
        
    return numeroMujeresTitularesAntioquia

print("Punto 18)---------------------------------------------")
print(f"Cantidad de mujeres beneficiarias titulares de ANTIOQUIA: {punto18(baseDeDatos)}")

#19) Desarrollar una función que reciba la base de datos y retorne el listado de etnias
# sin repeticiones de los hombres beneficiarios en NARIÑO

def punto19(baseDeDatos):    
    listadoEtniasHombresNarino = []
    for i in range(1,len(baseDeDatos)):
        if (baseDeDatos[i][7] == 'Hombre') and (baseDeDatos[i][9] == 'NARIÑO') and (baseDeDatos[i][5] not in listadoEtniasHombresNarino):
            listadoEtniasHombresNarino.append(baseDeDatos[i][5]) 
    return listadoEtniasHombresNarino    

print("Punto 19)---------------------------------------------")
print(f"Listado de etnias sin repeticiones de los hombres beneficiarios en NARIÑO: {punto19(baseDeDatos)}")

#20) Desarrollar una función que reciba la base de datos y retorne el porcentaje
# de beneficiarios bancarizados que hay en el departamento de CHOCO

def punto20(baseDeDatos):
    
    numeroBeneficiariosBancarizadosChoco = int()
    numeroBeneficiariosChoco = int()
    sinBancarizar = int()
    
    #Contenedor de diagnóstico
    valoresBancarizadoChoco = []
        
    for i in range(1,len(baseDeDatos)):
        if (baseDeDatos[i][9] == 'CHOCO'):            
            
            numeroBeneficiariosChoco += 1
            
            if baseDeDatos[i][0] not in valoresBancarizadoChoco:
                valoresBancarizadoChoco.append(baseDeDatos[i][0])
            
            if (baseDeDatos[i][0] == 'SI'):
                numeroBeneficiariosBancarizadosChoco += 1
            elif (baseDeDatos[i][0] == 'NO'):
                sinBancarizar += 1
                
    # #Salida de diagnóstico
    # print(f"Sin bancarizar de Chocó: {(sinBancarizar/numeroBeneficiariosChoco) * 100}")
    # pp.pprint(valoresBancarizadoChoco)
    # print()    
                        
    return (numeroBeneficiariosBancarizadosChoco/numeroBeneficiariosChoco) * 100

print("Punto 20)---------------------------------------------")
print(f"Porcentaje de beneficiarios bancarizados que hay en el departamento de CHOCO: {punto20(baseDeDatos)}")

#21) Desarrollar una función que reciba la base de datos y retorne el número de beneficiarios
#que presentan incapacidad

def punto21(baseDeDatos):
    numeroBeneficiariosIncapacidad = int()
    for i in range(1,len(baseDeDatos)):
        if baseDeDatos[i][3] == 'SI':
            numeroBeneficiariosIncapacidad += 1
    return numeroBeneficiariosIncapacidad

print("Punto 21)---------------------------------------------")
print(f"Número de beneficiarios que presentan discapacidad: {punto21(baseDeDatos)}")

#22) Desarrollar una función que reciba la base de datos y retorne el número de mujeres
# beneficiarias que han alcanzado SECUNDARIA

def punto22(baseDeDatos):    
    numeroMujeresBeneficiariasSecundaria = int()
    
    for i in range(1,len(baseDeDatos)):       
        
        # #Salida de diagnóstico
        # print(f"Género = {baseDeDatos[i][7]} NivelEscolaridad = {baseDeDatos[i][8]}")
        # input()
        
        if (baseDeDatos[i][7] == 'Mujer') and (baseDeDatos[i][8] == 'SECUNDARIA'):
            numeroMujeresBeneficiariasSecundaria += 1                    
            
        
    return numeroMujeresBeneficiariasSecundaria
    

print("Punto 22)---------------------------------------------")
print(f"Número de mujeres beneficiarias que han alcanzado SECUNDARIA: {punto22(baseDeDatos)}")


#23) Desarrollar una función que reciba la base de datos y retorne el listado de departamentos
# sin repeticiones donde existe por lo menos 5 o más beneficiarios NO ACTIVOS

def punto23(baseDeDatos):
    
    #Listado de departamentos con beneficiarios
    listadoDepartamentos = []
    
    #Recorrer todos los registros sin el encabezado para obtener los departamentos registrados
    for registro in baseDeDatos[1:]:
        if registro[9] not in listadoDepartamentos:
            listadoDepartamentos.append(registro[9])            
    
    #Lista paralela con el número de no activos de cada departamento
    numeroNoActivosDepartamento = []
    
    #Recorrer el listado de departamentos registrados en la base de datos
    for departamento in listadoDepartamentos:        
        
        #Conteo por cada departamento de beneficiarios NO ACTIVOS 
        numeroNoActivosDepartamentoActual = int()
        
        #Recorrer cada uno de los beneficiarios
        for registro in baseDeDatos[1:]:
            if (registro[9] == departamento) and (registro[4] == 'NO ACTIVO'):
                numeroNoActivosDepartamentoActual += 1
        
        #Agregar a la lista paralela el número de no activos
        numeroNoActivosDepartamento.append(numeroNoActivosDepartamentoActual)
        
    # #Salida de diagnóstico
    # print()
    # [print(f"Depto = {listadoDepartamentos[i]} NO ACTIVOS = {numeroNoActivosDepartamento[i]}") for i in range(len(listadoDepartamentos))]
    # print(f"Número de departamentos = {len(listadoDepartamentos)}")
    # print()    
    # input()
    
    #Filtrar por el número de no activos
    departamentosNoActivos5Arriba = []
    for i in range(len(listadoDepartamentos)):
        if numeroNoActivosDepartamento[i] >= 5:
            departamentosNoActivos5Arriba.append(listadoDepartamentos[i])
            
    # #Salida de diagnóstico
    # print(f"Número de departamentos con 5 o más beneficiarios NO ACTIVOS {len(departamentosNoActivos5Arriba)}")
    # input()
    
    #Retornar el listado del requerimiento
    return departamentosNoActivos5Arriba

print("Punto 23)---------------------------------------------")
print(f"Listado de departamentos sin repeticiones donde existe por lo menos 5 o más beneficiarios NO ACTIVOS: {punto23(baseDeDatos)}")

#24) Desarrollar una función que reciba la base de datos y retorne el porcentaje de mujeres
# cuyo tipo de asignación del beneficio es MONETARIO

def punto24(baseDeDatos):
    
    #Obtener el número de mujeres beneficiarias y el número de aquellas cuya asignación es monetaria
    numeroMujeres = int()
    numeroMujeresBeneficioMonetario = int()
    for registro in baseDeDatos[1:]:
        if registro[7] == 'Mujer':
            numeroMujeres += 1
            if registro[12] == 'MONETARIO':
                numeroMujeresBeneficioMonetario +=1
                
                # #Salida de diagnóstico
                # print(f"Género -° {registro[7]} TipoAsignaciónBeneficio -° {registro[12]}")
                # input()
                
    #Retornar el porcentaje de mujeres de este tipo (relativo a las mujeres beneficiarias)
    return (numeroMujeresBeneficioMonetario/numeroMujeres)*100    

print("Punto 24)---------------------------------------------")
print(f"El porcentaje de mujeres cuyo tipo de asignación del beneficio es MONETARIO: {punto24(baseDeDatos)}")


#25) Desarrollar una función que reciba la base de datos y retorne cuántas mujeres 
#beneficiarias hay en la ciudad de MEDELLIN.

def punto25(baseDeDatos):
    
    numeroMujeresBeneficiariasMedellin = int()    
    
    for registro in baseDeDatos[1:]:        
        if (registro[7] == 'Mujer') and (registro[10] == 'MEDELLIN'):
            numeroMujeresBeneficiariasMedellin += 1
    
    return numeroMujeresBeneficiariasMedellin 
    

print("Punto 25)---------------------------------------------")
print(f"Número mujeres beneficiarias que hay en la ciudad de MEDELLIN: {punto25(baseDeDatos)}")


#26) Desarrollar una función que reciba la base de datos y retorne True si la cantidad
#de mujeres beneficiarias discapacitadas en PEREIRA es mayor que la cantidad de 
#hombres discapacitados, y False en caso contrario.

def punto26(baseDeDatos):
    
    numeroMujeresDiscapacitadasPereira = int()
    numeroHombresDiscapacitadosPereira = int()    
    
    numeroDiscapacitadoPereira = int()
    
    for registro in baseDeDatos[1:]:
        
        #Conteo de diagnóstico
        if registro[10] == 'PEREIRA' and registro[3] == 'SI':
            numeroDiscapacitad1oPereira += 1
        
        # #Salida de diagnóstico
        # print(f"Genero -° {registro[7]} Municipio -° {registro[10]} Discapacidad -° {registro[3]}")
        # input()
        
        if registro[7] == 'Hombre' and registro[10] == 'PEREIRA' and registro[3] == 'SI' :
            numeroHombresDiscapacitadosPereira += 1
        elif registro[7] == 'Mujer' and registro[10] == 'PEREIRA' and registro[3] == 'SI':
            numeroMujeresDiscapacitadasPereira += 1   
    
        
    # #Salida de diagnóstico
    # print(f"Numero de discapacitados en Pereira = {numeroDiscapacitadoPereira}")    
    # print(f"Mujeres PEI DISC = {numeroMujeresDiscapacitadasPereira}  Hombres PEI DISC = {numeroHombresDiscapacitadosPereira}")    
    # input()
    
    #Retornar valor de verdad dependiendo de lo que se detecte
    if numeroMujeresDiscapacitadasPereira > numeroHombresDiscapacitadosPereira:
        return True
    else:
        return False
    
    
print("Punto 26)---------------------------------------------")
print(f" Hay mayor número de mujeres discapacitadas en PEREIRA que hombres? : {punto26(baseDeDatos)}")

#27) Desarrollar una función que reciba la base de datos y retorne la cantidad de municipios
# de Santander donde hay 5 o más beneficiarios discapacitados.

def punto27(baseDeDatos):   
    
    #Listado de municipios de Santander con beneficiarios y sin repeticiones
    listadoMunicipiosSantander = []
    
    #Conteo general de discapacitados santander
    discapacitadosSantander = int()
    
    #Recorrer todos los registros sin el encabezado para obtener los departamentos registrados
    for registro in baseDeDatos[1:]:
        if (registro[9] == 'SANTANDER') and (registro[10] not in listadoMunicipiosSantander) :
            listadoMunicipiosSantander.append(registro[10])
    
    #Lista paralela con el número de discapacitados en cada municipio
    numeroBeneficiariosDiscapacitadosMunicipio = []
    
    #Recorrer el listado de municipios de Santander registrados en la base de datos
    for municipio in listadoMunicipiosSantander:        
        
        #Conteo por cada departamento de beneficiarios NO ACTIVOS 
        discapacitadosMunicipio = int()
        
        #Recorrer cada uno de los beneficiarios de los municipios de SANTANDER con discapacidad
        for registro in baseDeDatos[1:]:
            if (registro[10] == municipio) and (registro[3] == 'SI'):
                discapacitadosMunicipio += 1
                
                #Conteo para diagnóstico
                discapacitadosSantander += 1
        
        #Agregar a la lista paralela el número de no activos
        numeroBeneficiariosDiscapacitadosMunicipio.append(discapacitadosMunicipio)
        
    # #Salida de diagnóstico
    # print()
    # [print(f"Depto = {listadoMunicipiosSantander[i]} NO DISCAPACITADOS = {numeroBeneficiariosDiscapacitadosMunicipio[i]}") for i in range(len(listadoMunicipiosSantander))]
    # print(f"Número de municipios = {len(listadoMunicipiosSantander)}")
    # print(f"Discapacitados general Santander -° {discapacitadosSantander}")
    # print()   
    
    
    #Filtrar por el número de discapacitados
    municipiosNoDiscapacitados5Arriba = []
    for i in range(len(listadoMunicipiosSantander)):
        if numeroBeneficiariosDiscapacitadosMunicipio[i] >= 5:
            municipiosNoDiscapacitados5Arriba.append(listadoMunicipiosSantander[i])
            
    # # #Salida de diagnóstico
    # print()
    # print(f"Municipios con más de 5 discapacitados: {listadoMunicipiosSantander}")
    # print(f"Número de departamentos con 5 o más beneficiarios NO ACTIVOS {len(listadoMunicipiosSantander)}")    
    
    #Retornar el número de minicipios
    return len(municipiosNoDiscapacitados5Arriba)

print("Punto 27)---------------------------------------------")
print(f"La cantidad de municipios de Santander donde hay 5 o más beneficiarios discapacitados es: {punto27(baseDeDatos)}")

#28) Desarrollar una función que reciba la base de datos y retorne el porcentaje de beneficiarios
# que cuentan con cédula de ciudadanía.

def punto28(baseDeDatos):
    
    numeroBeneficiariosConCedula = int()
    
    for registro in baseDeDatos[1:]:
        if registro[14] == 'CC':
            numeroBeneficiariosConCedula += 1
        
    return ( numeroBeneficiariosConCedula/(len(baseDeDatos)-1) )*100


print("Punto 28)---------------------------------------------")
print(f"El porcentaje de beneficiarios que cuentan con cédula de ciudadanía es: {punto28(baseDeDatos)}")


#29) Desarrollar una función que reciba la base de datos y retorne el listado sin repeticiones
# de municipios del Chocó a los cuales han llegado estos beneficios.

def punto29(baseDeDatos):
    
    listadoMunicipiosChoco = []
    
    for registro in baseDeDatos[1:]:
        if (registro[9] == 'CHOCO') and (registro[10] not in listadoMunicipiosChoco):
            listadoMunicipiosChoco.append(registro[10])             
    
    return listadoMunicipiosChoco

print("Punto 29)---------------------------------------------")
print(f"El listado sin repeticiones de municipios del Chocó a los cuales han llegado estos beneficios: {punto29(baseDeDatos)}")

#30) Desarrollar una función que reciba la base de datos y retorne el número de beneficiarios
#que han accedido al beneficio orientado a NUTRICIÓN.

def punto30(baseDeDatos):
    
    numeroBeneficiariosNutricion = int()
    
    #Listado de beneficios registrados
    beneficiosRegistrados = []
    
    
    for registro in baseDeDatos[1:]:
        if registro[13] == 'NUTRICIÓN':        
            numeroBeneficiariosNutricion += 1            
            
        if registro[13] not in beneficiosRegistrados:
            beneficiosRegistrados.append(registro[13])
            
    # #Salida de diagnóstico
    # print()
    # print("Beneficios registrados: ")
    # pp.pprint(beneficiosRegistrados)
    # print()    
    # print()    
    
    return numeroBeneficiariosNutricion
    

print("Punto 30)---------------------------------------------")
print(f"El número de beneficiarios que han accedido al beneficio orientado a NUTRICIÓN es: {punto30(baseDeDatos)}")

#31) Desarrolllar una función que reciba la base de datos y retorne el listado sin repeticiones
#y sin encabezado, de los tipos de beneficios que ofrece el programa Familias en Acción.

def punto31(baseDeDatos):       
    
    #Listado de beneficios registrados
    beneficiosRegistrados = []
    
    for registro in baseDeDatos[1:]:           
        if registro[13] not in beneficiosRegistrados:
            beneficiosRegistrados.append(registro[13])
    
    return beneficiosRegistrados
    

print("Punto 31)---------------------------------------------")
print(f"Listado sin repeticiones y sin encabezado, de los tipos de beneficios que ofrece el programa Familias en Acción: {punto31(baseDeDatos)}")

#32) Desarrollar una función que reciba la base de datos y retorne el porcentaje total de 
#beneficiarios inactivos en los principales departamentos del país, es decir,
# de ANTIOQUIA, VALLE y CUNDINAMARCA.

def punto32(baseDeDatos):    
    
    numeroBeneficiariosPrincipalesDepartamentos = int()
    numeroBeneficiariosInactivosPrincipalesDepartamentos = int()
    
    for registro in baseDeDatos[1:]:
        if registro[9] == 'ANTIOQUIA' or registro[9] == 'VALLE' or registro[9] == 'CUNDINAMARCA':
            numeroBeneficiariosPrincipalesDepartamentos += 1
            if registro[4] == 'NO ACTIVO':
                numeroBeneficiariosInactivosPrincipalesDepartamentos += 1         
        
    
    return (numeroBeneficiariosInactivosPrincipalesDepartamentos/numeroBeneficiariosPrincipalesDepartamentos)*100

print("Punto 32)---------------------------------------------")
print(f"Porcentaje total de beneficiarios inactivos en los principales departamentos del país, es decir, de ANTIOQUIA, VALLE y CUNDINAMARCA: {punto32(baseDeDatos)}")

#33) Desarrollar una función que reciba la base de datos y retorne dos números de forma simultánea
#uno con el número de mujeres discapacitadas de Pasto, y el segundo con el número de hombres
# discapacitados de Pasto que son beneficiarios del programa.

def punto33(baseDeDatos):
    
    numeroMujeresDiscapacitadasPasto = int()
    numeroHombresDiscapacitadosPasto = int()
    
    for registro in baseDeDatos[1:]:
        if registro[10] == 'PASTO':
            
            if registro[7] == 'Mujer' and registro[3] == 'SI':
                numeroMujeresDiscapacitadasPasto += 1
                
            if registro[7] == 'Hombre' and registro[3] == 'SI':
                numeroHombresDiscapacitadosPasto += 1
                
    
    return numeroMujeresDiscapacitadasPasto, numeroHombresDiscapacitadosPasto    
    

print("Punto 33)---------------------------------------------")
print(f"El número de mujeres discapacitadas de Pasto y el número de hombres respectivamente es: {punto33(baseDeDatos)}")

#34) Desarrollar una función que reciba la base de datos y retorne 
# el número de menores de edad registrados en el departamento de ANTIOQUIA.

def punto34(baseDeDatos):
    
    numeroMenoresEdadAntioquia = int()
    
    for registro in baseDeDatos[1:]:
        if registro[14] == 'TI' and registro[9] == 'ANTIOQUIA':
            numeroMenoresEdadAntioquia += 1
    
    return numeroMenoresEdadAntioquia
    

print("Punto 34)---------------------------------------------")
print(f"El número de menores de edad registrados en el departamento de ANTIOQUIA es: {punto34(baseDeDatos)}")

#35) Desarrollar una función que reciba la base de datos y retorne el número de hombres
#y el número de mujeres que no tienen definido si presentan o no discapacidad. Lo anterior
# implica una función que retorna estos dos valores de forma simultánea y en el orden establecido.

def punto35(baseDeDatos):
    
    numeroMujeresSinDefinir = int()
    numeroHombresSinDefinir = int()
    
    conteoGeneral = int()
    
    for registro in baseDeDatos[1:]:        
        if registro[3] != 'SI' and registro[3] != 'NO':
            conteoGeneral += 1
            
            if registro[7] == 'Hombre':
                numeroHombresSinDefinir += 1
                
            if registro[7] == 'Mujer':
                numeroMujeresSinDefinir += 1                    
    
    
    # #Salida de diagnóstico
    # print()
    # print(f"Conteo general sin definir: {conteoGeneral}")
    # print()        
    
    return numeroHombresSinDefinir, numeroMujeresSinDefinir
    

print("Punto 35)---------------------------------------------")
print(f"El número de hombres y el número de mujeres que no tienen definido si presentan o no discapacidad respectivamente es: {punto35(baseDeDatos)}")