'''
Actividad 8
Programa que permite consultar el stock, añadir unidades al stock y agregar un nuevo producto
utilizando un diccionario.
'''

# Para optimizar el código se utilizarán paquetes
from paquete_validaciones.funciones_validaciones import ingresar_texto, ingresar_numero

# Diccionario de productos y su stock
product_dictionary = {}

# ---------------------------------------------------------------------------------------
# Menú que permite que el usuario pueda consultar y añadir unidades a un stock, además de
# agregar un nuevo producto al diccionario.
# ---------------------------------------------------------------------------------------

while True:

    # Menu
    print('''
----------------- Menu -----------------
1. Consultar el stock de un producto.
2. Agregar o quitar unidades a un stock.
3. Agregar un producto.
4. Salir del programa.
----------------------------------------''')
    option = int(ingresar_numero('Opcion: ', 1, 4, True, True, True))

    match option:

        case 1: # Consulta el stock
            print()
            product = ingresar_texto('Ingresa el nombre del producto a consultar: ')
            if product not in list(product_dictionary.keys()):
                print('El producto no se encuentra en el diccionario')
            else:
                print(f'Stock de {product}: {product_dictionary[product]}')

        case 2: # Agrega o quita unidades a un stock
            print()
            product = ingresar_texto('Ingresa el nombre del producto: ')
            if product not in list(product_dictionary.keys()):
                print('El producto no se encuentra en el diccionario')
                continue
            add_stock = int(ingresar_numero('Ingresa las unidades a añadir. Si desea quitar unidades, ingresa una cantidad negativa: ', integer = True))
            if product_dictionary[product] + add_stock < 0:
                print('[X]La cantidad a quitar sobrepasa la cantidad que hay de stock.')
            else:
                product_dictionary[product] += add_stock
                print('[✔] Stock actualizado correctamente.')

        case 3: # Agrega un producto al diccionario
            print()
            product = ingresar_texto('Ingresa el nombre del producto: ', list(product_dictionary.keys()), True)
            stock = int(ingresar_numero('Ingresa el stock: ', 0, is_min = True, integer = True))
            product_dictionary[product] = stock
            print('[✔] Se añadió el producto correctamente.')

        case 4: # Termina el programa
            print()
            print('Saliendo del programa...')
            break
