'''
Actividad 6
Programa que rota todos los una posición hacia la derecha, donde el último
elemento pasa a ser el primero.
'''
# Lista de números
number_list = [1, 2, 3, 4, 5, 6, 7]

# ---------------------------------------------------------------
# Bucle que cambia la posición de los elementos uno a la derecha.
# ---------------------------------------------------------------
copy_number_List = number_list.copy()
for i in range(len(copy_number_List)):
    if i != len(copy_number_List) - 1:
        copy_number_List[i + 1] = number_list[i]
    else:
        copy_number_List[0] = number_list[i]


# ------------------------------------------------------------
# Bucles para mostrar la lista original y la lista reordenada.
# ------------------------------------------------------------
# Bucle para mostrar la lista original
print('Lista original:')
for i in range(len(number_list)):
    if i != len(number_list) - 1:
        print(f'{number_list[i]}', end=', ')
    else:
        print(number_list[i])
        
# Bucle para mostrar la lista con los elementos trasladados
print('\nLista de los elementos rotados una posición hacia la derecha:')
for i in range(len(copy_number_List)):
    if i != len(copy_number_List) - 1:
        print(f'{copy_number_List[i]}', end=', ')
    else:
        print(copy_number_List[i])