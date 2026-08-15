'''
Actividad 3
Programa que genera una lista con 15 números enteros al azar entre 1 y 100. Crea una 
lista con los pares y otra con los impares y muestra cuantos números tiene cada una.
'''
from random import randint

# Generando la lista de números enteros
random_list = []
for i in range(15):
    random_list.append(randint(1, 100))

# -----------------------------------------------------------
# Crea una lista con los números pares y otra con los impares
# -----------------------------------------------------------
even_number_list = []
odd_number_list = []
for number in random_list:
    if number % 2 == 0:
        even_number_list.append(number)
    else:
        odd_number_list.append(number)

# Cantidad de elementos en cada lista
print(random_list)
print(f'La lista de números pares tiene {len(even_number_list)} elementos.')
print(f'La lista de números impares tiene {len(odd_number_list)} elementos.')