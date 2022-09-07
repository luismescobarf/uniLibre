import random
import time
nombres = [
    'Diana',
    'Mateo',
    'Isabel',
    'Santiago',
    'Juan David',
    'Mateo',
    'Estefania'
]

numeroVeces = random.randint(0,10)
for _ in range(numeroVeces):
    time.sleep(random.randint(0,3))
    print(random.choice(nombres))


