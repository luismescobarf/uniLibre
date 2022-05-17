#Librerías de apoyo
#------------------
import random
import pprint as pp
from functools import reduce

#Definición de funciones
#-----------------------

#Carga de datos
#--------------
cafe = [
    [
        {'Producto':'Café','Precio':2000},
        {'Producto':'Helado','Precio':3000},
        {'Producto':'Agua con gas','Precio':2300}
    ],
    [
        {'Producto':'Papas gratinadas','Precio':8000},
        {'Producto':'Banan split','Precio':7000}
    ],
    [
        {'Producto':'Té helado','Precio':2560},
        {'Producto':'Tortilla huevo','Precio':5300},       
        {'Producto':'Café','Precio':2000}       
    ]    
]

#Sección principal
#------------------

# Ejemplo básico función lambda
# incrementoDoble = lambda x:x+2
# print("Ejemplo")
# print(list(map(incrementoDoble, [i for i in range(7)] )))

#Ejemplo básico de reduce
def suma(a,b):
    return a+b
coleccion = list(range(1,5))
print("-------------------------------------------")
print(f"Coleccion: {coleccion}")
print(f"Reducción de la colección (agregación)->{reduce(suma,coleccion)}")

#Ejemplo list (dict) comprehension diccionario cuadrado de números
diccionarioCuadrados = {i:i**2 for i in range(7)}
print("---List comprehension aplicado a diccionarios---")
pp.pprint(diccionarioCuadrados)

#Requerimientos para resolver en funcional:
"""
1)  Ordenar cada una de las mesas de mayor a menor por precio
2)  Obtener el producto más costoso de cada mesa
3)  Obtener el producto más barato de cada mesa
4)  Obtener el total (la cuenta) de cada una de las mesas
4b) Incorporar el total de cada mesa como un atributo
    en cada una de las mesas.
5)  Obtener el total de ventas que se van a obtener por
    todos los productos que están servidos en las mesas.
6)  a. Filtrar en cada mesa todos los productos de más de 3000 pesos
    b. Filtrar en cada mesa todos los productos menores a 3000 pesos
"""

#Requerimiento (1):
#Ordenar cada una de las mesas de mayor a menor por precio
def ordenarProductosMesaPrecioMayor(mesa):
    return sorted(mesa,key = lambda x:x['Precio'],reverse=True)
print("Antes de ordenamiento:")
pp.pprint(cafe)  
print()
print("Mesas ordenadas por precio:")
cafeOrdenadoPrecioMesas = list(map(ordenarProductosMesaPrecioMayor,cafe))
pp.pprint(cafeOrdenadoPrecioMesas)    
print("-------------------------------------------")

#Requerimiento (2):
#Obtener el producto más costoso de cada mesa
def productoMasCostosoMesa(mesa):
    return max(mesa,key = lambda x:x['Precio'])
print("-------------------------------------------")
print("Producto Más Costoso de Cada Mesa: ")
productosCostosos = list(map(productoMasCostosoMesa,cafe))
pp.pprint(productosCostosos)

#Requerimiento (3):
#Obtener el producto menos costoso de cada mesa
def productoMenosCostosoMesa(mesa):
    return min(mesa,key = lambda x:x['Precio'])
print("-------------------------------------------")
print("Producto Más Barato de Cada Mesa: ")
productosBaratos = list(map(productoMenosCostosoMesa,cafe))
pp.pprint(productosBaratos)

#Requerimiento (4):
#Obtener el total (la cuenta) de cada una de las mesas
def extraerPrecio(mesa):
    return list(map(lambda x:x['Precio'],mesa))
coleccionesPrecios = list(map(extraerPrecio,cafe))
totalesPorMesa = list(map(lambda x : sum(x) ,coleccionesPrecios))
print("-------------------------------------------")
print("Total a pagar en cada mesa: ")
pp.pprint(totalesPorMesa)

#Requerimiento (4b):
# Incorporar el total de cada mesa como un atributo 
# en cada una de las mesas.
print("-------------------------------------------")
print("Total incorporado en la colección general: ")
# def incorporarTotal(lista,totalPagar):
#     return list(reduce(lambda acumulador=list(),
#                        elemento=dict():acumulador+elemento,
                       
#                        ))
pp.pprint(list(map(lambda x,y: x+[{'Total':y}],cafe,totalesPorMesa)))

#Requerimiento (5):    
# Obtener el total de ventas que se van a obtener por
# todos los productos que están servidos en las mesas.

#Ejemplo de reducción para acumulación
def acumular(coleccion=list(),producto=None):
    #En caso de que haya diccionarios de diferente tipo
    #return coleccion+producto if 'Producto' in producto.keys() else coleccion    
    return coleccion+producto
reduccionProductos = reduce(acumular,cafe)
print("Reducción de productos: ")
[print(producto) for producto in reduccionProductos]
#Sumatoria total sobre los productos:
print(f"Total Restaurante = {sum(list(map(lambda x:int(x['Precio']),reduccionProductos)))}")

#Requerimiento (6):
# 6)  a. Filtrar en cada mesa todos los productos de más de 3000 pesos (en promoción)
#     b. Filtrar en cada mesa todos los productos menores a 3000 pesos (sin promoción)
#Predicados
def productoEnPromocion(producto):
    return True if producto['Precio']>3000 else False
def productoSinPromocion(producto):
    return True if producto['Precio']<=3000 else False
def filtrarProductosPromocion(productos):
    return list(filter(productoEnPromocion,productos))
def filtrarProductosSinPromocion(productos):
    return list(filter(productoSinPromocion,productos))
mesasConProductosPromocion = map(filtrarProductosPromocion,cafe)
mesasConProductosSinPromocion = map(filtrarProductosSinPromocion,cafe)
print("--------a) Productos en Promoción (mayores a 3000)---------")
[pp.pprint(mesa) for mesa in mesasConProductosPromocion]
print("--------b) Productos sin Promoción (menores o iguales a 3000)---------")
[pp.pprint(mesa) for mesa in mesasConProductosSinPromocion]

#Ejemplo básico zip -> incorporar bebidas a las mesas
listadoNombres = ['Malteada','Limonada Cherry','Jugo']
etiquetasProducto = ['Producto']*len(listadoNombres)
print(etiquetasProducto)
listadoPrecios = [7900,3800,3120]
etiquetasPrecio = ['Pecio']*len(listadoPrecios)
print(etiquetasPrecio)
print("-----/Observar colección de tuplas del zip: ")
#pp.pprint(list(zip(etiquetasPrecio,listadoPrecios)))
pp.pprint(list(zip(etiquetasPrecio,listadoPrecios))+list(zip(etiquetasProducto,listadoNombres)))
print("-----/Diccionario Parcial: ")
pp.pprint(dict(list(zip(etiquetasPrecio,listadoPrecios))+list(zip(etiquetasProducto,listadoNombres))))







    







