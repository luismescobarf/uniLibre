#Librerías
import pprint as pp
import random

#Códigos de los estudiantes del grupo
codigosEstudiantes = """
1114149109
1085716618
1089931822
1088244874
1089599453
1004720345
1004718114
1004776323
1089932201
1077997121
1088240040
1108332514
1114148533
1111662143
1057330367
1004719303
1089598522
1088241078
1029980139
1004520854
1000179645
1093589016
1114398740
1088355585
"""
#Limpiar comienzo y final
codigosEstudiantes = codigosEstudiantes.strip()

#Convertir el bloque de códigos en un listado
listadoCodigos = codigosEstudiantes.split("\n")

#Mostrar el contenido almacenado en el contenedor
#print("Códigos Ingresados:")
#[print(codigo) for codigo in listadoCodigos]

#Opciones de asignación
opcionesAsignacion = ["Quiz Tipo A", "Quiz Tipo B"]

#Contenedor de asignaciones
detalleAsignaciones = list()

#Preparar conjuntos de control
estudiantesSinAsignar = set(listadoCodigos)
estudiantesAsignados = set()

#Asignar la primera opción a la mitad del listado de estudiantes seleccionados aleatoriamente
numeroMitadGrupo = len(listadoCodigos) // 2
for _ in range(numeroMitadGrupo):	
	while True:
		elegido = random.choice(listadoCodigos)
		if elegido not in estudiantesAsignados:
			estudiantesAsignados.add(elegido)
			estudiantesSinAsignar.remove(elegido)
			detalleAsignaciones.append([elegido,opcionesAsignacion[0]])
			break

#Asignar la segunda opción al resto
listadoRestantes = list(estudiantesSinAsignar)
for estudianteFaltante in listadoRestantes:
	detalleAsignaciones.append([estudianteFaltante,opcionesAsignacion[1]])
	
#Presentar toda la asignación
print("------------------------------")
print("CódigoEstudiante -> Tipo Quiz")
print("------------------------------")
[print(f"{asignacion[0]} -> {asignacion[1]}") for asignacion in detalleAsignaciones]




