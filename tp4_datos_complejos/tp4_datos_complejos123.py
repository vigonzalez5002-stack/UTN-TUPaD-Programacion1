'''
Este archivo corresponde a las actividades 1, 2 y 3 debido a que los tres
utilizan el mismo diccionario precios_frutas.

Actividad 1: Se añaden 3 frutas con sus respectivos precios al diccionario.

Actividad 2: Se actualizan los precios de 3 frutas.

Actividad 3: Se crea una lista que contenga únicamente las frutas.
'''

# Diccionario que se usará.
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
    }

# Esto imprime el diccionario original
print('Diccionario original:')
for key, value in precios_frutas.items():
    print(f'{key}: {value}')
print()


# ------------------------------------------------------------------------
# Actividad 1
# Código que añade al diccionario tres frutas con sus respectivos precios.
# ------------------------------------------------------------------------

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Esto imprime el diccionario modificado por el código de la actividad 1
print('Diccionario original:')
for key, value in precios_frutas.items():
    print(f'{key}: {value}')
print()