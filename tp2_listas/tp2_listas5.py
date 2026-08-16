'''
Programa que genera una lista con los nombres de 8 estudiantes presentes en clase.
Con funcionalidad de añadir un nuevo estudiante o eliminar uno existente y de mostrar
la lista final actualizada.
'''

# ----------------------------------------------
# Lista de los 8 estudiantes presentes en clase.
# ----------------------------------------------
student_list = []
for i in range(8):
    while True:
        student = input(f'Nombre del estudiante {i + 1}: ').capitalize().strip()
        if not student.isalpha():
            print('ERROR: El nombre debe contener solo letras.')
        else:
            print('>> El estudiante se ha añadido a la lista.\n')
            student_list.append(student)
            break

# ---------------------------
# Bucle del menú de opciones.
# ---------------------------
while True:
    print(f'''--------- Menú de opciones ---------
1 - Agregar un nuevo estudiante.
2 - Eliminar uno existente.
3 - Mostrar lista final actualizada.
4 - Salir del programa.
------------------------------------''')
    # Validación de la opción
    while True:
        option = input('Opción elegida: ').strip()
        if not option.isdigit():
            print('ERROR: La opción debe ser un número entero.')
        elif option not in '1234':
            print('ERROR: Opción fuera de rango.')
        else:
            break

    # Ejecución del menú
    match option:
        case '1': # Añadir un nuevo estudiante a la lista
            while True:
                student = input(f'Nombre del nuevo estudiante: ').capitalize().strip()
                if not student.isalpha():
                    print('ERROR: El nombre debe contener solo letras.')
                else:
                    print('>> El estudiante se ha añadido a la lista.\n')
                    student_list.append(student)
                    break

        case '2': # Eliminar un estudiante de la lista
            while True:
                student = input(f'Nombre del nuevo estudiante: ').capitalize().strip()
                if not student.isalpha():
                    print('ERROR: El nombre debe contener solo letras.')
                else:
                    break
            if student in student_list:
                student_list.remove(student)
                print('>> El estudiante se ha eliminado de la lista.\n')
            else:
                print('>> El estudiante no está en la lista.\n')

        case '3': # Mostrar la lista
            print('Lista final actualizada:')
            for i in range(len(student_list)):
                print(f'Estudiante {i + 1}: {student_list[i]}')

        case '4':
            print('Saliendo del programa.')
            break