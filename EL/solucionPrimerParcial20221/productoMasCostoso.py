import pprint as pp

#Lista de listas: mutable (editar), conserva
#el orden de los elementos, la anidación
#permite expresar la jerarquía.

cafe = [
    #Mesa 1
    [
        ['Café',2000],
        ['Helado',3000],
        ['Agua con gas',2300]
    ],
    #Mesa 2
    [
        ['Papas gratinadas',8000],        
        ['Banana split',7000],
        ['Café',1500]
    ],
    #Mesa 3
    [
        ['Té helado',2000],
        ['Tortilla de huevo',3000],
        ['Café',2000]        
    ],
    #Mesa 4
    [        
        ['Tortilla de huevo',3000],        
        ['Picada para 2 personas',30000]        
    ],
    #Mesa 5
    [
        ['Café',2000],
        ['Helado',3000],
        ['Agua con gas',2300]
    ]
]

#Recorrer mesas y productos para obtener el más costoso
id_mesa_costoso = int()
id_producto_costoso = int()
nombre_producto_costoso = str()
precio_mas_alto = -999999
for id_mesa,mesa in enumerate(cafe):    
    for id_producto,producto in enumerate(mesa):
        if producto[1] >= precio_mas_alto:
            id_mesa_costoso = id_mesa
            id_producto_costoso = id_producto            
            precio_mas_alto = producto[1]
            nombre_producto_costoso = producto[0]

print(f"En la mesa {id_mesa_costoso} se está consumiendo {nombre_producto_costoso}, es el producto más caro con un valor de {precio_mas_alto}")



        
        























