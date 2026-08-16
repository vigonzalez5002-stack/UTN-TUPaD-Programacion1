'''
Actividad 7
Programa que calcula el promedio de las mínimas, máximas y muestra en que día se registró
la mayor amplitud térmica a partir de una matriz 7x2.
'''
# -------------------------------------------------------------------
# Matriz 7x2 que contiene la mínima y máxima de cada día de la semana
# en grados Celsius
# Filas = Día(Domingo a sábado)
# Columnas = Temperaturas(Mínima y Máxima)
# -------------------------------------------------------------------
matriz = [
    [12, 15],
    [12, 17],
    [10, 14],
    [ 8, 12],
    [ 9, 12],
    [ 8, 15],
    [ 7, 13],
]

# ------------------------------------------------------------------------
# Se crean a partir de la matriz tres listas formadas por las temperaturas
# mínimas y las máximas y la amplitud térmica respectivamente.
# El índice de cada lista corresponde al día de la semana -1.
# ------------------------------------------------------------------------
temperaturas_minimas = []
temperaturas_maximas = []
amplitudes_termicas = []
for dia in matriz:
    temperaturas_minimas.append(dia[0])
    temperaturas_maximas.append(dia[1])
    amplitudes_termicas.append(dia[1] - dia[0])

# Cálculo del promedio de las temperaturas máximas y mínimas
promedio_minimos = sum(temperaturas_minimas) / len(temperaturas_minimas)
promedio_maximos = sum(temperaturas_maximas) / len(temperaturas_maximas)

# Búsqueda de la amplitud térmica máxima y los días que lo alcanzan
amplitud_maxima = max(amplitudes_termicas)
amplitudes_maximas = []
for i in range(len(amplitudes_termicas)):
    if amplitudes_termicas[i] == amplitud_maxima:
        amplitudes_maximas.append(i)

# -------------------------------------------------------------------------
# Se imprimen por consola el promedio de las temperaturas mínimas y máximas
# de la semana. También, el día que se registró la mayor amplitud térmica.
# -------------------------------------------------------------------------
# Promedios
print(f'Promedio de las temperaturas mínimas de la semana: {promedio_minimos:.2f}ºC')
print(f'Promedio de las temperaturas máximas de la semana: {promedio_maximos:.2f}ºC')

# Días que registraron la amplitud máxima utilizando una lista auxiliar
dias = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
print('El/los día/s ', end='')
for i in amplitudes_maximas:
    if amplitudes_maximas.index(i) != len(amplitudes_maximas) - 1:
        print(dias[i], end=', ')
    else:
        print(dias[i], end=' ')
print(f'registra/n la mayor amplitud térmica de la semana, siendo {amplitud_maxima:.2f}ºC')