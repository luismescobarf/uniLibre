"""Calculadora:
    - Operaciones binarias
    - Menu para ofrecer las opciones"""

#Interaccion
import interaccion as ic

#Logicas
import logica as op
    
#Seccion principal
#-----------------
continuar = True 
while continuar:
        
    #Presentar el menu de las operaciones -> Interaccion    
    opcion = ic.mostrarMenu()
    
    #Revisar cual es la opcion ingresada
    if opcion == 1:
        ic.mensaje("Sumando:")
        a,b = ic.capturarOperandos()        
        ic.mostrarResultado(op.suma(a,b))    
    elif opcion == 2:        
        ic.mensaje("Restando:")
        a,b = ic.capturarOperandos()
        ic.mostrarResultado(op.resta(a,b))        
    elif opcion == 3:       
        ic.mensaje("Multiplicacion:")        
        a,b = ic.capturarOperandos()
        ic.mostrarResultado(op.multiplicacion(a,b))       
    elif opcion == 4:           
        ic.mensaje("Potencia:")        
        a,b = ic.capturarOperandos()
        ic.mostrarResultado(op.potencia(a,b))        
    elif opcion == 5:
        ic.mensaje("Division:")        
        a,b = ic.capturarOperandos()
        ic.mostrarResultado(op.division(a,b))
    elif opcion == 6:       
        ic.mensaje("Salida exitosa!")
        continuar = False
    else:       
        ic.mensaje("Opcion invalida!!")            
    