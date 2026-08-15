'''
Actividad 1
Programa que muestra una lista con las notas de 10 estudiantes, el promedio y las notas
más altas y bajas.
'''
# Lista inventada
student_grades = [10, 5, 3.5, 8.75, 6.25, 1, 1, 7.50, 2, 3.75]

# -----------------------------------------
# Bucle FOR para mostrar la lista completa.
print('Notas de los estudiantes:')
for index, grade in enumerate(student_grades):
    print(f'Nota del alumno {index + 1}: {grade}')

# ----------------------------------------------------------------------------------------
# Cálculo del promedio e impresión del mismo.
# NOTA: Otra forma de hacerlo es utilizando un bucle para sumar cada elemento de la lista
# para luego dividirlo por la cantidad de elementos que tiene la lista.
average = sum(student_grades) / len(student_grades)
print(f'\nEl promedio general es {average}')

# ----------------------------------------------------------------------------------------
# Búsqueda de la nota más alta y la nota más baja entre todas las notas.
# NOTA: Se aplicará la función max() para la nota más alta, mientras que la nota más baja
# se aplicará un bucle FOR con el objetivo de mostrar diversas formas de resolución.

# >> Nota más alta
print('\nAlumn@/s con la nota más alta:')
max_grade = max(student_grades)
# Bucle para mostrar múltiples alumnos con la nota máxima
for i in range(len(student_grades)):
    if student_grades[i] == max_grade:
        print(f'La nota más alta es {max_grade} y corresponde al alumno {i + 1}.')

# >> Nota más baja
print('\nAlumn@s con la nota más alta:')
min_grade = student_grades[0]
for grade in student_grades:
    if grade < min_grade:
        min_grade = grade
# Bucle para mostrar múltiples alumnos con la nota mínima
for i in range(len(student_grades)):
    if student_grades[i] == min_grade:
        print(f'La nota más baja es {min_grade} y corresponde al alumno {i + 1}')