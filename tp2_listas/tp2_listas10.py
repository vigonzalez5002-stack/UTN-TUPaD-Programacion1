'''
Actividad 10
Programa que, a partir de una matriz que registra las ventas de 4 productos durante 7 días,
imprime en consola el total vendido por cada producto, el día con mayores ventas totales
y el producto más vendido en la semana.
NOTA: Para la búsqueda de máximos(día y producto) se considerará el primer máximo de la lista
para simplificar el código.
'''
# -----------------------------------------------------------------
# Matriz 4x7 que registra las ventas de 4 productos durante 7 días.
# Filas = Productos
# Columnas = Días
# -----------------------------------------------------------------
ventas = [
    [ 6, 13, 5, 1, 20, 34, 17],
    [10, 22, 14, 11, 33, 2, 1],
    [3, 5, 24, 17, 18, 1, 0],
    [0, 0, 2, 34, 12, 8, 15]
]

# Esto calcula el total vendido de cada producto y lo guarda en una lista
total_producto = []
for producto in ventas:
    total_producto.append(sum(producto))

# Esto calcula las ventas por día y los guarda en una lista
total_dias = []
for i in range(7): # Recorre por día
    total_dia = 0
    for producto in ventas: # Recorre para sumar las ventas en ese día
        total_dia += producto[i]
    total_dias.append(total_dia)

# ------------------------------------------------------------------
# Se imprimen en consola el total vendido por cada producto, el día
# con mayores ventas totales y el producto más vendido en la semana.
# ------------------------------------------------------------------

# Muestra el total vendido por cada producto
print('Total vendido por cada producto:')
for i, total in enumerate(total_producto):
    print(f'El producto {i + 1} se vendió un total de {total} unidades en 7 días.')

# Muestra el día con mayores ventas totales utilizando una lista auxiliar
nombres_dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
dia_maximo = max(total_dias)
indice_dia = total_dias.index(dia_maximo)
print(f'El día con mayores ventas totales es {nombres_dias[indice_dia]} con {dia_maximo} ventas.')

# Indica el producto más vendido en la semana
producto_maximo = max(total_producto)
indice_producto = total_producto.index(producto_maximo)
print(f'El producto más vendido en la semana fue el producto {indice_producto + 1} con un total de {producto_maximo} unidades. ')