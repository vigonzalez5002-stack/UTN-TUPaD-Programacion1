'''
Actividad 4
Crea una lista sin elementos repetidos a partir de una lista predefinida y muestra el resultado.
'''
# Lista predefinida
data = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# -----------------------------
# Lista sin elementos repetidos
# -----------------------------
unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)

# --------------------------------------------------
# Bucles para mostrar la comparación de ambas listas
#---------------------------------------------------
print('>> Comparación ambas listas')

# Bucle para mostrar la lista original
print('Lista de datos original:')
for i in range(len(data)):
    if i != len(data) - 1:
        print(f'{data[i]}, ', end='')
    else:
        print(data[i], end='\n')

# Bucle para mostrar la lista sin los elementos repetidos
# NOTA: Se aplica otra forma de mostrar la lista sin utilizar estructuras repetitivas.
print('Lista de datos sin elementos repetidos:')
print(*unique_data, sep=', ')