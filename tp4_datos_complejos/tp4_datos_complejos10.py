'''
Actividad 10
El programa invierte los pares clave-valor de un diccionario que mapea los nombres de los países
con sus capitales. De esta forma, el diccionario invertido será de pares clave-valor que mapea
los nombres de las capitales con sus países.
'''
from paquete_texto.funciones_texto import imprimir_diccionario

# Diccionario original
original_dictionary = {
    'Argentina': 'Buenos Aires',
    'Chie': 'Santiago',
}

# --------------------------------------------------------------------------
# Este código crea un nuevo diccionario con los pares clave-valor invertidos
# y los imprime en la terminal.
# --------------------------------------------------------------------------

# Esto construye el nuevo diccionario con los pares invertidos
reverse_dictionary = {}
for key, value in original_dictionary.items():
    reverse_dictionary[value] = key

# Esto muestra en la terminal ambos diccionarios
imprimir_diccionario(original_dictionary, 'Diccionario original:')
imprimir_diccionario(reverse_dictionary, 'Diccionario invertido:')