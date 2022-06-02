# --------------------------------------------------------
# Rutina de asignación de numerales 2 y 3
# Lógica y Algoritmos
# Evaluación tercer corte 2022-1
# --------------------------------------------------------
import random
codigos = [
    '1114149109',
    '1085716618',
    '1089931822',
    '1088244874',
    '1089599453',
    '1004720345',
    '1004718114',
    '1004776323',
    '1089932201',
    '1077997121',
    '1088240040',
    '1108332514',
    '1114148533',
    '1111662143',
    '1057330367',
    '1004719303',
    '1089598522',
    '1088241078',
    '1029980139',
    '1004520854',
    '1000179645',
    '1093589016',
    '1114398740',
    '1088355585'
]
numerales = [
    '(2)',
    '(3)'
]
for i,codigo in enumerate(codigos):
    random.shuffle(numerales)
    print("----------------------")
    print(f"{i+1}) {codigo} desarrolla {numerales[0]} ")
    print("----------------------") 
