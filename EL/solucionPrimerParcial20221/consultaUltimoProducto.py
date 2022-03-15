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
        ['Tortilla de huevo',3000]        
    ],
    #Mesa 5
    [
        ['Café',2000],
        ['Helado',3000],
        ['Agua con gas',2300]
    ]
]

#Mostrar las mesas
for id_mesa,mesa in enumerate(cafe):
    print()
    print(f"----Mesa {id_mesa+1}----")
    print("Nombre     Precio")
    for producto in mesa:
        print(f"{producto[0]}    {producto[1]}")

#Preguntar al usuario la mesa que quiere revisar
id_consultado = int(input("Ingrese el número de la mesa: "))
print("El último producto es:")
print(cafe[id_consultado-1][-1])

        
        























