'''
Actividad 5
El programa recibe una frase e imprime las palabras únicas y la cantidad de veces
que se repite cada palabra.
'''
# Se importarán paquetes para ahorrar código
from paquete_texto.funciones_texto import imprimir_secuencia, imprimir_diccionario
from paquete_validaciones.funciones_validaciones import ingresar_frase

# -----------------------------------------------------------------------------------------
# Este código pide al usuario una frase y separa la frase en un conjunto de palabras.
# A partir de este conjunto, se hace un conteo de apariciones de dicha palabra en la frase.
# -----------------------------------------------------------------------------------------

# Esto le pide la frase al usuario y la separa en un conjunto de palabras
phrase = ingresar_frase()
word_set = set(phrase.split(' '))

# Esto hace un conteo de apariciones de cada palabra de la frase y la almacena en un diccionario
word_dictionary = {}
for word in word_set:
    word_dictionary[word] = phrase.count(word)

# -----------------------------------------------------------------------------------
# Este código imprime en la terminal las palabras únicas y la cantidad de apariciones
# de cada palabra.
# Para imprimir el conjunto con formato, se tranformará dicho conjunto a una lista.
# Esto debido a que los conjuntos no son un tipo de dato secuencial, por lo que no
# tienen un orden.
# -----------------------------------------------------------------------------------

imprimir_secuencia(list(word_set), '\nConjunto de palabras de la frase:')
imprimir_diccionario(word_dictionary, 'Diccionario con la cantidad de apariciones de cada palabra:')