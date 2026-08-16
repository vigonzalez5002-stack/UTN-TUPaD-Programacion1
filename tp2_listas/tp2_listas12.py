'''
Actividad 12
Programa que recibe 8 números enteros y los almacena en una lista.
Dicha lista debe ser ordenada de forma ascendente o descendente.
NOTA: La explicación del funcionamiento de la función sorted y del parámetro reverse
está en la actividad 2.
'''

# Ingreso de números
number_list = []
for i in range(8):
    while True:
        number = input('Ingrese un número entero: ').strip()
        if not number.isdigit():
            print('ERROR: Se debe ingresar un número entero.')
        else:
            number_list.append(int(number))
            print(f'[✔] El número {number} se ingresó a la lista exitosamente.\n')
            break

# ----------------------------------------------------------------------------------
# Se muestra la lista original, ordenada de forma ascendente y de forma descendente.
# ----------------------------------------------------------------------------------
# Esto muestra la lista original
print('Lista original: ', end='')
for i in range(len(number_list)):
    if i != len(number_list) - 1:
        print(number_list[i], end=', ')
    else:
        print(number_list[i])

# Esto muestra la lista ordenada de forma ascendente
ascending_number_list = sorted(number_list)
print('\nLista ordenada de menor a mayor: ', end='')
for i in range(len(ascending_number_list)):
    if i != len(ascending_number_list) - 1:
        print(ascending_number_list[i], end=', ')
    else:
        print(ascending_number_list[i])

# Esto meustra la lista ordenada de forma descendente
descending_number_list = sorted(number_list, reverse=True)
print('\nLista ordenada de mayor a menor: ', end='')
for i in range(len(descending_number_list)):
    if i != len(descending_number_list) - 1:
        print(descending_number_list[i], end=', ')
    else:
        print(descending_number_list[i])