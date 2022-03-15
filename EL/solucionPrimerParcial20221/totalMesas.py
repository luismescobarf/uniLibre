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

print("Formatear estado de las mesas")
for id_mesa,mesa in enumerate(cafe):
    total = 0
    for producto in mesa:
        total += producto[1]        
    print()
    print(f"----Total Mesa {id_mesa+1}----")
    print(total)
        
        























