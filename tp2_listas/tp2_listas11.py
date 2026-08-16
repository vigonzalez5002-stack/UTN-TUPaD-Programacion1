'''
Actividad 11
Programa que, a partir de una lista con los nombres de 10 estudiantes, el usuario pueda buscar
el nombre de un estudiante, indicando si se encuentra o no en la lista. De estarlo, indica
la posición en la que aparece y si no se encuentra, que informe que no está en la lista.
'''
# Lista de estudiantes
students = ['Miguel', 'Sofía', 'Emma', 'Pedro', 'Daniel', 'Juan', 'Victoria', 'Mónica', 'Tomas', 'Mateo']

# Ingreso del nombre a buscar y validación
while True:
    name = input('Ingrese el nombre del estudiante que desea buscar: ').capitalize().strip()
    if not name.isalpha():
        print('ERROR: El nombre debe contener solo letras.')
    else:
        break

# Búsqueda del nombre del estudiante en la lista
if name in students:
    student_index = students.index(name)
    print(f'{name} se encuentra en la posición {student_index + 1} de la lista.')
else:
    print(f'{name} no se encuentra en la lista.')