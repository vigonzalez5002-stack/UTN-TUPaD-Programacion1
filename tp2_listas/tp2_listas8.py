'''
Actividad 8
Programa que, a partir de una matriz con las notas de 5 estudiantes en 3
materias, muestra el promedio de cada estudiante y de cada materia.
'''
# -----------------------------------------------------------------
# Matriz 5x3 que registra las notas de los estudiantes en materias.
# Filas = Estudiantes
# Columnas = Materias
# -----------------------------------------------------------------
matriz = [
    [ 5, 7,  3],
    [10, 8,  9],
    [ 1, 10, 5],
    [ 6, 6,  8],
    [ 2, 7, 10]
]

# Promedio de cada estudiante
print('Promedio de cada estudiante:')
for i in range(len(matriz)):
    print(f'Promedio del estudiante {i + 1}: {(sum(matriz[i]) / 3):.2f}')

# Promedio de cada materia
print('\nPromedio de cada materia:')
for i in range(3):
    suma_notas = 0
    for fila in matriz:
        suma_notas += fila[i]
    print(f'Promedio de la materia {i + 1}: {(suma_notas / 5):.2f}')