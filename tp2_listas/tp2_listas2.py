'''
Actividad 2
Programa que carga 5 productos en una lista a elección del usuario, la muestra ordenada alfabéticamente. 
Además, el usuario puede eliminar y actualizar la lista.
NOTA: Se considerarán ciertas validaciones para que el código sea sostenible. También se añadirá una opción
de añadir producto por si el usuario desea extender la cantidad de productos a la lista.

Explicación de la función sorted():
Si bien la función del método .sort() y la función sorted() es el mismo, la función sorted() no modifica la
lista original, sino que crea una nueva lista con los elementos ordenados a partir de la lista original.
Sintaxis de la función sorted:
sorted(Iterable, key=None, reverse=False) -> list
- El primer parámetro es cualquier tipo de estructura iterable a ordenar, como las listas o diccionarios.
- El segundo parámetro es una regla que define la forma en la que se deben ordenan los elementos del iterable,
por defecto está en None, donde los elementos se ordenan de forma ascendente utilizando la regla de menor a mayor
para los números o la regla de orden alfabético para los strings.
- El tercer parámetro sólo admite booleanos, y define si se ordena de forma ascendente(False) o descendente(True),
por defecto está en False.
- NOTA: Es importante que los elementos del iterable sean datos de la misma naturaleza, es decir que sean comparables
si se intentara comparar un entero con un string la función largaría un error.
'''
# Lista de productos
product_list = []

# Ingreso de 5 productos
for i in range(5):
    # Validación del producto a añadir a la lista
    while True:
        product = input('Ingrese el nombre del producto: ').capitalize().strip()
        if not product.isalpha():
            print('ERROR: El nombre del producto debe ser una única palabra formado por solo letras.')
        else:
            break
    product_list.append(product)
    print(f'[✓] El producto {product} se añadió a la lista exitosamente.')

# Menú de opciones
while True:
    print('''
-------------------- Menú --------------------
A - Mostrar la lista ordenada alfabéticamente.
B - Añadir producto a la lista.
C - Eliminar producto de la lista.
D - Salir del programa.
----------------------------------------------''')
    
    # No se hará validación de esto
    option = input('Elija una de las opciones: ').upper().strip()

    match option:
        case 'A': # Mostrar lista ordenada alfabéticamente
            # Aplicando el método sorted para este caso
            sorted_list = sorted(product_list)
            print(f'\nLista de productos ordenada: ')
            for i, product in enumerate(sorted_list): # Uso enumerate para mostrar la ubicación del producto.
                print(f'Producto {i + 1}: {product}')
        
        case 'B': # Añadir producto a la lista
            # Validación del producto a añadir a la lista
            while True:
                product = input('Ingrese el nombre del producto: ').capitalize().strip()
                if not product.isalpha():
                    print('ERROR: El nombre del producto debe ser una única palabra formado por solo letras.')
                else:
                    break
            product_list.append(product)
            print(f'[✓] El producto {product} se añadió a la lista exitosamente.')

        case 'C': # Eliminar producto de la lista
            # Validación del producto a eliminar de la lista
            while True:
                product = input('Ingrese el nombre del producto: ').capitalize().strip()
                if not product.isalpha():
                    print('ERROR: El nombre del producto debe ser una única palabra formado por solo letras.')
                else:
                    break
            if product in product_list:
                product_list.remove(product)
                print(f'[✓] El producto {product} se eliminó de la lista exitosamente.')
            else:
                print('[X] El producto no se encuentra en la lista.')
            
        case 'D':
            print('Saliendo del programa.')
            break