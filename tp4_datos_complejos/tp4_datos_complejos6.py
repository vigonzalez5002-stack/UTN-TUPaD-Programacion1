'''
Actividad 6
Programa que permite registrar las notas de 3 alumnos en tuplas y calcula el promedio.
'''

# Se utiliza un paquete de funciones para optimizar el código.
from paquete_validaciones.funciones_validaciones import ingresar_texto, ingresar_nota
from paquete_texto.funciones_texto import imprimir_secuencia

# --------------------------------------------------------------------------------------
# Esto registra las notas de 3 alumnos y lo añade al diccionario de estudiantes.
# El par clave-valor corresponde al nombre del estudiante y sus 3 notas respectivamente.
# --------------------------------------------------------------------------------------

# Diccionario de estudiantes
student_dictionary = {}

# Este código almacena el par nombre-notas de 3 estudiantes en el diccionario.
for i in range(1, 4):

    # Validación del nombre del estudiante
    print()
    name = ingresar_texto(f'Ingresa el nombre del alumno Nº{i}: ', list(student_dictionary.keys()), not_text_valid = True)

    # Bucle que almacena 3 notas en una lista temporal
    list_grade = [] # Lista temporal para almacenar notas 
    for i in range(1, 4):
        print(f'Nota Nº{i} de {name}:')
        grade = ingresar_nota() # Validación de la nota del estudiante
        list_grade.append(grade)

    # Esto añade al diccionario
    student_dictionary[name] = tuple(list_grade)

# ---------------------------------------------------------------------------
# Este código imprime en la terminal las notas del estudiante y su prompedio.
# ---------------------------------------------------------------------------

for name in student_dictionary.keys():

    # Esto imprime el promedio del estudiante
    average = sum(student_dictionary[name]) / 3
    print(f'El promedio de {name} es: {average:.2f}')

    # Esto imprime las notas del estudiante
    imprimir_secuencia(student_dictionary[name], f'Sus notas:')