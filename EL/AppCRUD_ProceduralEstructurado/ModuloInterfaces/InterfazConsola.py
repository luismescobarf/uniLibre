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
    opcion = None
    while opcion == None:
        try:
            opcion = int(input("Ingrese una opción: "))
        except:
            print("Caracter inválido!!!")    
            
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
        
    
    
    
    