#Librería para vista o interacción por consola

def mensaje(info=''):
    print()
    print("--------------")
    print(info)
    print("--------------")
    print()
    
def formularioMenuAppCRUD():
    print("")
    print("1. Adicionar Tarea")
    print("2. Listar Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
    
    #Recoger la opción que ingresa el usuario
    # opcion = None
    # while opcion == None:
    #     try:
    #         opcion = int(input("Ingrese una opción: "))
    #     except:
    #         print("Caracter inválido!!!")    
    opcion = capturaCampoNumerico("Ingrese una opción: ","Caracter inválido!!!")
            
    #Aplicar la lógica propia de la vista
    return opcion
    
def formularioAdicionarTarea():
    pass

def presentarTareas(tasks):
    print("---Listado Tareas ---")
    print("ID - Descripción - Duración - Desplazamiento")
    for i,tarea in enumerate(tasks):        
        desplazamiento = 'SI' if tarea[2] else 'NO'
        print(f"{i} - {tarea[0]} - {tarea[1]} - {desplazamiento}")
        
def formularioAdicionarTarea():
    mensaje("Formulario Adición de Tareas")
    descripcion = input("Ingrese descripción: ")    
    # duracion = None
    # while duracion == None:
    #     try:
    #         duracion = int(input("Ingrese duración: "))
    #     except:
    #         print("Duración debe ser numérica!!!")
    duracion = capturaCampoNumerico("Ingrese duración: ","Duración debe ser numérica!!!")
    # desplazamiento = None
    # while desplazamiento == None:
    #     try:
    #         desplazamiento = int(input("Ingrese desplazamiento (1/0): "))
    #     except:
    #         print("Desplazamiento debe ser binaria!!!")    
    desplazamiento = capturaCampoBooleano("Ingrese desplazamiento (1/0): ","Desplazamiento debe ser binaria!!!")
    
    tarea = [descripcion,duracion,bool(desplazamiento)]                
    
    return tarea

def capturaCampoNumerico(label,reporteError = ''):
    entrada = None
    while entrada == None:
        try:
            entrada = int(input(label))
        except:
            print(reporteError)
    return entrada

def capturaCampoBooleano(label,reporteError = ''):
    entrada = None
    while entrada == None:
        try:
            entrada = int(input(label))
        except:
            print(reporteError)
    return bool(entrada)
    
        
    
    
    
    