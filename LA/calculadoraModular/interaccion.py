def mensaje(texto):
    print("---> "+texto+" ")
   
def mostrarResultado(c):
    print()
    print("El resultado es: "+ str(c) )    
    print()
    
def capturarOperandos():
    try:
        a = int(input("Ingresar primer valor: "))
        b = int(input("Ingresar segundo valor: "))
        return a,b
    except:
        print("Error en el valor ingresado!!!")

def mostrarMenu():
    print("---- Operaciones Calculadora ----")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Potencia")
    print("5) Division")
    print("6) Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))#Captura del operador
        return opcion 
    except:
        print("Error en la opcion ingresada!")
    