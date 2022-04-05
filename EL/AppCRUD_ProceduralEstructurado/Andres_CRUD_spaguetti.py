tasks = [
    ['Estudiar', 2, 'SI'],
    ['Hacer compras', 3, 'SI'],
    ['Organizar cuarto', 1, 'NO'],
    ['Preparar almuerzo', 2, 'NO'],
    ['Programar', 2, 'NO']
]

user_option = None

MENU = """
----- CRUD -----
:: Ingrese una opción
1 -> Crear Tarea
2 -> Ver tarea
3 -> Actualizar tarea
4 -> Borrar Tarea
5 -> Más opciones
0 -> Salir
"""

OPTIONS = """
A -> Tiempo promedio de las tareas registradas
B -> Número de tareas que requieren desplazamiento
C -> Número de tareas que NO requieren desplazamiento
D -> Tarea con máxima duración
E -> Tarea con mínima duración
"""

# Mostrar menu
print(MENU)
user_option = int(input('::Ingresa una opción: '))

while user_option != 0:

    # CREATE
    if user_option == 1:
        description = input('-> Ingrese una descripción de la tarea: ')
        time = int(input('-> Tiempo estimado (horas): '))
        displacement = input('La tarea requiere desplazamiento? SI/NO: ')
        displacement.upper()
        tasks.append([description, time, displacement])

        # Mostrar menu
        print(MENU)
        user_option = int(input('::Ingresa una opción: '))

    # READ
    elif user_option == 2:
        print('----- Tareas guardadas -----')
        for i, task in enumerate(tasks):
            print(f'{i}: {task}')

        # Mostrar menu
        print(MENU)
        user_option = int(input('::Ingresa una opción: '))

    # UPDATE
    elif user_option == 3:
        print('----- Tareas guardadas -----')
        print('|Indice ----- | Tarea ----- |')
        for i, task in enumerate(tasks):
            print(f'{i}: {task}')
        
        task_id = int(input('::Ingrese el índice de la tarea a actualizar: '))

        description = input('-> Ingrese una descripción de la tarea: ')
        time = int(input('-> Tiempo estimado: '))
        displacement = input('La tarea requiere desplazamiento? SI/NO: ')
        displacement.upper()
        tasks[task_id] = [description, time, displacement]

        print('----- Tareas actualizadas -----')
        print('|Indice ----- | Tarea ----- |')
        for i, task in enumerate(tasks):
            print(f'{i}: {task}')

        # Mostrar menu
        print(MENU)
        user_option = int(input('::Ingresa una opción: '))

    # DELETE
    elif user_option == 4:
        task_id = int(input('::Ingrese el índice de la tarea a eliminar: '))
        tasks.pop(task_id)

        print('----- Tareas actualizadas -----')
        print('|Indice ----- | Tarea ----- |')
        for i, task in enumerate(tasks):
            print(f'{i}: {task}')

        # Mostrar menu
        print(MENU)
        user_option = int(input('::Ingresa una opción: '))

    elif user_option == 5:
        # Mostrar opciones
        print(OPTIONS)
        option = input('::Ingresa una opción: ')
        option.upper()

        if option == 'A':
            total_time = 0

            for task in tasks:
                total_time += task[2]

            print(f'El promedio es: {total_time / len(tasks)}')

            # Mostrar opciones
            print(OPTIONS)
            option = input('::Ingresa una opción: ')
            option.upper()

        elif option == 'B':
            task_matched = 0

            for task in task:
                if task[2] == 'SI':
                    task_matched += 1
            
            print(f'::Número de tareas que requieren desplazamiento: {task_matched}')

            # Mostrar opciones
            print(OPTIONS)
            option = input('::Ingresa una opción: ')
            option.upper()

        elif option == 'C':
            task_matched = 0

            for task in task:
                if task[2] == 'NO':
                    task_matched += 1
            
            print(f'::Número de tareas que NO requieren desplazamiento: {task_matched}')

            # Mostrar opciones
            print(OPTIONS)
            option = input('::Ingresa una opción: ')
            option.upper()

        elif option == 'D':
            max = list(tasks[0])

            for i in range(1, len(tasks)):
                if max[1] < tasks[i][1]:
                    max = list(tasks[i])

            print(f'Tarea con máxima duración {max}')

            # Mostrar opciones
            print(OPTIONS)
            option = input('::Ingresa una opción: ')
            option.upper()

        elif option == 'E':
            pass
