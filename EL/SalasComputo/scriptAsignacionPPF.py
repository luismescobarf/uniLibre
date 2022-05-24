# --------------------------------------------------------
# Rutina de asignación de requerimientos Paradigma Funcional
# Estructura de Lenguajes
# Evaluación tercer corte 2022-1
# --------------------------------------------------------
import random
codigos = [
    '1092850194',
    '1001022405',
    '1004012388',
    '1002543833',
    '1193047915',
    '1006398802',
    '1004701080'
]
numerales = [
    '(a)',
    '(b)',
    '(c)',
    '(d)',
    '(e)',
    '(f)',
    '(g)',
    '(h)',
    '(i)'
]
for codigo in codigos:
    random.shuffle(numerales)
    print("----------------------")
    print(f"{codigo} desarrolla {numerales[0]} y {numerales[1]}")
    print("----------------------") 
