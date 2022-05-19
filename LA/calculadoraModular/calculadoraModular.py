"""Calculadora:
    - Operaciones binarias
    - Menú para ofrecer las opciones"""

#Definición de funciones

#Interacción
def mensaje(texto):
    print(f"---> {texto} ")    

def mostrarResultado(c):
    print()
    print(f"El resultado es: {c}")    
    print()
    
def capturarOperandos():
    a = int(input("Ingresar primer valor: "))
    b = int(input("Ingresar segundo valor: "))
    return a,b

def mostrarMenu():
    print("---- Operaciones Calculadora ----")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) Potencia")
    print("5) División")
    print("6) Salir")
    opcion = int(input("Ingrese una opción: "))#Captura del operador
    return opcion    

#Lógicas
def suma(a,b):
    c = a + b
    return c
    
def resta(a,b):
    c = a - b
    return c

def multiplicacion(a,b):
    c = a * b
    return c

def potencia(a,b):
    c = a * b
    return c

def division(a,b):
    c = a / b
    return c
    
#Sección principal
#-----------------
continuar = True 
while continuar:
        
    #Presentar el menú de las operaciones -> Interacción
    # print("---- Operaciones Calculadora ----")
    # print("1) Suma")
    # print("2) Resta")
    # print("3) Multiplicación")
    # print("4) Potencia")
    # print("5) División")
    # print("6) Salir")
    # opcion = int(input("Ingrese una opción: "))#Captura del operador
    opcion = mostrarMenu()
    
    #Revisar cuál es la opción ingresada
    if opcion == 1:
        
        #Interacción -> Captura de los operandos
        #print("---> Sumando: ")
        mensaje("Sumando:")
        # a = int(input("Ingresar primer valor: "))
        # b = int(input("Ingresar segundo valor: "))
        a,b = capturarOperandos()
        
        #Lógica
        # c = a + b
        c = suma(a,b)
        
        #Interacción -> mostrar el resultado en pantalla
        # print(f"El resultado es: {c}")
        mostrarResultado(c)
    
    elif opcion == 2:
        
        #Interacción -> Captura de los operandos
        # print("---> Restando: ")
        mensaje("Restando:")
        # a = int(input("Ingresar primer valor: "))
        # b = int(input("Ingresar segundo valor: "))
        a,b = capturarOperandos()
        
        #Lógica
        # c = a - b
        c = resta(a,b)
        
        #Interacción -> mostrar el resultado en pantalla
        # print(f"El resultado es: {c}")
        mostrarResultado(c)
        
    elif opcion == 3:
        
        #Interacción -> Captura de los operandos
        # print("---> Multiplicación: ")
        mensaje("Multiplicación:")
        # a = int(input("Ingresar primer valor: "))
        # b = int(input("Ingresar segundo valor: "))
        a,b = capturarOperandos()
        
        #Lógica
        # c = a * b
        c = multiplicacion(a,b)
        
        #Interacción -> mostrar el resultado en pantalla
        # print(f"El resultado es: {c}")
        mostrarResultado(c)
        
    elif opcion == 4:
        
        #Interacción -> Captura de los operandos
        # print("---> Potencia: ")
        mensaje("Potencia:")
        # a = int(input("Ingresar primer valor: "))
        # b = int(input("Ingresar segundo valor: "))
        a,b = capturarOperandos()
        
        #Lógica
        # c = a ** b
        c = multiplicacion(a,b)
        
        #Interacción -> mostrar el resultado en pantalla
        # print(f"El resultado es: {c}")
        mostrarResultado(c)
        
    elif opcion == 5:
        
        #Interacción -> Captura de los operandos
        # print("---> División: ")
        mensaje("División:")
        # a = int(input("Ingresar primer valor: "))
        # b = int(input("Ingresar segundo valor: "))
        a,b = capturarOperandos()
        
        #Lógica
        # c = a / b
        c = division(a,b)
        
        #Interacción -> mostrar el resultado en pantalla
        # print(f"El resultado es: {c}")   
        mostrarResultado(c)
    
    elif opcion == 6:
        
        #Interacción -> Reportar salida exitosa
        # print("---> Salida exitosa!")       
        mensaje("Salida exitosa!")
        
        #Lógica
        continuar = False
        #break
        #continue
        
        
    else:
        
        #Interacción -> Reportar que no se tiene registrada esa opción
        # print("---> Opción inválida!! ")
        mensaje("Opción inválida!!")
        
    #Pausa para mostrar el resultado
    input()
                