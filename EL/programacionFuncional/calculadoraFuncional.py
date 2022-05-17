#Ejemplo: funciones de primera clase y orden superior

#Función de orden superior 
# -> retornar funciones que construye en tiempo de ejecución
def operacion(signo):
    if signo == '+':
        #Función de primera clase
        def suma(a=0,b=0):
            return a + b
        #Tratar a la función de primera clase -> Tipo de dato
        #envoltura = suma
        return suma
    elif signo == '-':
        def resta(a=0,b=0):
            return a - b
        return resta
    elif signo == '*':
        # def multiplicacion(a=0,b=0):
        #     return a * b
        # return multiplicacion
        return lambda a=0,b=0 : a*b
    
def calculadora(signo,a,b):
    # funcion = operacion(signo)    
    return operacion(signo)(a,b)

#Llamados
print(f"{calculadora('+',15,12)}")
print(f"{calculadora('*',7,3)}")
print(f"{calculadora('-',5,10)}")



    

