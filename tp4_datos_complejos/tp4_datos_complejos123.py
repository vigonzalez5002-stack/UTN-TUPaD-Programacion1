'''
Este archivo corresponde a las actividades 1, 2 y 3 debido a que los tres
utilizan el mismo diccionario precios_frutas.
'''
# Se hará uso de un paquete para evitar repetir código.
from paquete_texto.funciones_texto import imprimir_diccionario, imprimir_secuencia

# Diccionario que se usará.
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
    }

# Esto imprime el diccionario original
imprimir_diccionario(precios_frutas, 'Diccionario original:')


# ------------------------------------------------------------------------
# Actividad 1
# Código que añade al diccionario tres frutas con sus respectivos precios.
# ------------------------------------------------------------------------

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Esto imprime el diccionario modificado por el código de la actividad 1
imprimir_diccionario(precios_frutas, 'Diccionario modificado por la actividad 1:')

# ------------------------------------------------
# Actividad 2
# Código que actualiza los precios de tres frutas.
# ------------------------------------------------

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Esto imprime modificado por el código de la actividad 2
imprimir_diccionario(precios_frutas, 'Diccionado modificado por la actividad 2:')

# -----------------------------------------------------------------------------
# Actividad 3
# Código que crea una lista que contiene únicamente las frutas sin los precios.
# -----------------------------------------------------------------------------

lista_frutas = list(precios_frutas.keys())

# Esto imprime una lista con las claves tomadas del diccionario
imprimir_secuencia(lista_frutas, 'Lista generada a partir de las claves del diccionario:')
