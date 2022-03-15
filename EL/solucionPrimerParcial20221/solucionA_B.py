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
        ['Banana split',7000]
    ],
    #Mesa 3
    [
        ['Té helado',2000],
        ['Tortilla de huevo',3000],
        ['Café',2000]        
    ],
]

pp.pprint(cafe)

print("Productos de la mesa 1:")
print(cafe[0])
print("Precio del último producto de la mesa 1:")
print(cafe[0][2][1])
print("(SubNeg) Precio del último producto de la mesa 1:")
print(cafe[0][-1][1])
print("(SubNeg) Nombre del último producto de la mesa 1:")
print(cafe[0][-1][0])










