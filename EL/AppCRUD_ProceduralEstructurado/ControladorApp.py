#Aplicación CRUD Tareas
#----------------------

import ModuloInterfaces.InterfazConsola as ic
import CRUD
import sys

#Precarga de las tareas -> CRUD -> Modelo (BD, Archivo, RAM)
tasks = None
tasks = CRUD.carga()
if tasks == None:
    ic.mensaje("Error cargando tareas por defecto!!")
    sys.exit(1) #Reportar error

#Inicia la aplicación (mainloop)
mainloop = True
while mainloop:
    opcion = ic.formularioMenuAppCRUD()
    
    #Adicionar
    if opcion == 1:         
        
        ic.mensaje("-- Adicionando tarea!")
                 
        #Presentar formulario adicionar tarea y capturarla
        tarea = ic.formularioAdicionarTarea()        

        #Actualizar el modelo con la información recogida
        CRUD.CREATE(tarea,tasks)

    #Listar
    elif opcion == 2:
        ic.mensaje("Listar Tareas!")        
        ic.presentarTareas(tasks)
    
    #Actualizar
    elif opcion == 3:
        ic.mensaje("En construcción!!")
        
    #Eliminar
    elif opcion == 4:
        ic.mensaje("En construcción!!")
        
    #Salida de la aplicación
    elif opcion == 5:
        ic.mensaje("Salida exitosa!")
        mainloop = False
    
    #Opciones no implementadas
    else:
        ic.mensaje("Opción inválida!!")    
    
    
        
    
        
        
        