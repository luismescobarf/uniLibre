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
    c = a ** b
    return c

def division(a,b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print("Division entre cero retornamos infinito!")
        return 9999999
    except TypeError:
        print("Error de tipado")