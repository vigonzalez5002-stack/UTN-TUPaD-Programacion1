# -------------------------------------------------------------------------
# Este módulo contiene todas las funciones que corresponden a la resolución
# de las actividades.
# -------------------------------------------------------------------------
from paquete_validaciones.funciones_validaciones import enter_number, enter_word
from paquete_utiles.funciones_utiles import show_data, load_product_names

FILE = 'products.txt'

# =============================================================================================

# =============================================================================================

def load_products():
    '''
    Esta función carga los productos del archivo products.txt a una lista de
    diccionarios y retornará dicha lista.

    Si no existe el archivo, lo crea con 3 productos dados por el usuario.
    '''

    print('\n=======================================')
    print('Cargando productos en la memoria RAM...')

    # Lista de diccionarios de los productos
    products_list = []

    try:
        with open(FILE, 'r') as file:
            # Esto lee el archivo y crea una lista de lineas
            lines = file.readlines()

            # Esto procesa cada linea de datos para añadirlo a la lista
            for line in lines[1:]: 
                product_data = line.strip().split(',')
                products_list.append({
                    'nombre': product_data[0], 
                    'precio': float(product_data[1]), 
                    'cantidad': int(product_data[2])
                    })

    except FileNotFoundError:
        print('[X] Error: No se encontró el archivo.')
        print('> Creando el archivo...')

        # Esto crea el archivo
        with open(FILE, 'w') as file:
            file.write('nombre,precio,cantidad\n')

            # Esto añade 3 productos al archivo.
            products_added = [] # Lista para evitar que ingrese el mismo producto.
            for i in range(1, 4):
                print(f'\n> Ingresando el producto Nº{i}...')
                name = enter_word('\nIngresa el nombre del producto: ', products_added, True, '[X] Error: El producto ya fue añadido.')
                price = enter_number('\nIngrese el precio del producto: ', 0, is_min = True)
                amount = enter_number('\nIngrese el stock: ', 0, is_min = True, integer = True)
                file.write(f'{name},{price},{amount}\n')
                products_added.append(name)
                products_list.append({
                    'nombre': name, 
                    'precio': price, 
                    'cantidad': amount})

        print('\n[✓] Archivo creado exitosamente.')
        print('\n[✓] Productos cargados correctamente.')
        return products_list

    except Exception as unexpected_exception:
        print('[X] Ocurrió un error inesperado.')
        print(f'> Error {type(unexpected_exception).__name__}: {unexpected_exception}')

    else:
        print('\n[✓] Productos cargados correctamente.')
        return products_list

    finally:
        print('\n>> Volviendo al menú de opciones.')

# =============================================================================================

# =============================================================================================

def show_products(products_list):
    '''
    Esta función imprime en la terminal los productos cargados 
    en una lista de diccionarios.
    '''

    try:
        print('\n===================')
        print('Lista de productos:')
        # Esto muestra los productos uno por uno
        for product in products_list:
            show_data(product)

    except TypeError:
        print('[X] Error: No se han cargado los productos a la memoria.')

    finally:
        print('\n>> Volviendo al menú de opciones.')

# =============================================================================================

# =============================================================================================

def add_product(products_list : list):
    '''
    Esta función añade a la lista de diccionarios un producto.
    '''

    print('\n===================================')
    print('Añadiendo un producto a la lista...')

    # Esto crea un diccionario del producto.
    name = enter_word('\nIngresa el nombre del producto: ', load_product_names(products_list), True, '[X] Error: El producto ya fue añadido.')
    price = enter_number('\nIngrese el precio del producto: ', 0, is_min = True)
    amount = enter_number('\nIngrese el stock: ', 0, is_min = True, integer = True)
    product_dictionary = {'nombre': name, 'precio': price, 'cantidad': amount}

    products_list.append(product_dictionary)
    print('[✓] Se añadió el producto exitosamente')

# =============================================================================================

# =============================================================================================

def find_product(products_list : list):
    '''
    Esta función busca un producto en la list de diccionarios. Si lo encuentra
    lo mostrará con formato, si no lo encuentra mostrará un error.
    '''

    print('\n=======================')
    print('Buscando un producto...')
    try:
        name = enter_word('\nIngresa el nombre del producto a buscar: ')

        if name not in load_product_names(products_list):
            print('[X] Error: El producto no se encuentra añadido.')

        else:
            index_name = load_product_names(products_list).index(name)
            show_data(products_list[index_name])

    except Exception as unexpected_exception:
            print('[X] Ocurrió un error inesperado.')
            print(f'> Error {type(unexpected_exception).__name__}: {unexpected_exception}')

    finally:
        print('\n>> Volviendo al menú de opciones.')

# =============================================================================================

# =============================================================================================

def save_products(product_list):
    '''
    Esta función guarda los productos en el archivo productos.txt.
    '''
    
    print('\n=========================================')

    try:
        with open(FILE, 'w') as file:
            file.write('nombre,precio,cantidad\n')
            lines = []
            for product in product_list:
                lines.append(f'{product['nombre']},{product['precio']},{product['cantidad']}\n')
            file.writelines(lines)

    except TypeError:
        print('[X] Error: No se han cargado los productos a la memoria.')

    else:
        print('[✓] Se guardaron los datos correctamente.')

    finally:
        print('\n>> Volviendo al menú de opciones.')