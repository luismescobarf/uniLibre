Coleccion1 = list(range(10))
Coleccion2 = [2,4,6,8,10]
def cuadrado(x):
    return x**2
print(tuple(map(cuadrado, Coleccion1)))