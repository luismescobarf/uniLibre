"""Calculadora:
    - Operaciones binarias
    - Menú para ofrecer las opciones"""
    
#Sección principal
#-----------------
continuar = True 
while continuar:
        
    #Presentar el menú de las operaciones -> Interacción
    print("---- Operaciones Calculadora ----")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) Potencia")
    print("5) División")
    print("6) Salir")
    opcion = int(input("Ingrese una opción: "))#Captura del operador
    
    #Revisar cuál es la opción ingresada
    if opcion == 1:
        
        #Interacción -> Captura de los operandos
        print("---> Sumando: ")
        a = int(input("Ingresar primer valor: "))
        b = int(input("Ingresar segundo valor: "))
        
        #Lógica
        c = a + b
        
        #Interacción -> mostrar el resultado en pantalla
        print(f"El resultado es: {c}")
    
    elif opcion == 2:
        
        #Interacción -> Captura de los operandos
        print("---> Restando: ")
        a = int(input("Ingresar primer valor: "))
        b = int(input("Ingresar segundo valor: "))
        
        #Lógica
        c = a - b
        
        #Interacción -> mostrar el resultado en pantalla
        print(f"El resultado es: {c}")
        
    elif opcion == 3:
        
        #Interacción -> Captura de los operandos
        print("---> Multiplicación: ")
        a = int(input("Ingresar primer valor: "))
        b = int(input("Ingresar segundo valor: "))
        
        #Lógica
        c = a * b
        
        #Interacción -> mostrar el resultado en pantalla
        print(f"El resultado es: {c}")
        
    elif opcion == 4:
        
        #Interacción -> Captura de los operandos
        print("---> Potencia: ")
        a = int(input("Ingresar primer valor: "))
        b = int(input("Ingresar segundo valor: "))
        
        #Lógica
        c = a ** b
        
        #Interacción -> mostrar el resultado en pantalla
        print(f"El resultado es: {c}")
        
    elif opcion == 5:
        
        #Interacción -> Captura de los operandos
        print("---> División: ")
        a = int(input("Ingresar primer valor: "))
        b = int(input("Ingresar segundo valor: "))
        
        #Lógica
        c = a / b
        
        #Interacción -> mostrar el resultado en pantalla
        print(f"El resultado es: {c}")   
    
    elif opcion == 6:
        
        #Interacción -> Reportar salida exitosa
        print("---> Salida exitosa!")       
        
        #Lógica
        continuar = False
        
    else:
        
        #Interacción -> Reportar que no se tiene registrada esa opción
        print("---> Opción inválida!! ")
        
        
        
    
    
    