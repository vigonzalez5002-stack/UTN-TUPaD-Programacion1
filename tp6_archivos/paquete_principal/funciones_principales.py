# -------------------------------------------------------------------------
# Este módulo contiene todas las funciones que corresponden a la resolución
# de las actividades.
# -------------------------------------------------------------------------

FILE = r'tp6_archivos\products.txt'

def load_products():
    '''
    Esta función carga los productos del archivo products.txt a una lista de
    diccionarios y retornará dicha lista.

    Si no existe el archivo, lo crea con 3 productos.
    '''

    print('==========================================')
    print('\n Cargando productos en la memoria RAM...')

    # Lista de diccionarios de los productos
    product_list = []

    try:
        with open(FILE, 'r') as file:
            # Esto lee el archivo y divide las lineas en encabezado y filas
            lines = file.readlines()
            columns = lines[0].strip().split(',')
            rows = lines[1:]

            # Esto procesa cada linea de datos para añadirlo a la lista
            for row in rows: 
                product_dictionary = {}
                product_data = row.strip().split(',')

                # Esto almacena los datos de un producto en un diccionario
                for i in range(len(columns)): 
                    product_dictionary[columns[i]] = product_data[i]

                # Esto carga el diccionario a la lista
                product_list.append(product_dictionary)
    

    except FileNotFoundError:
        print('[X] Error: No se encontró el archivo.')

    except Exception as unexpected_exception:
        print('[X] Ocurrió un error inesperado.')
        print(f'> Error {type(unexpected_exception).__name__}: {unexpected_exception}')

    else:
        print('[✓] Productos cargados correctamente.')
        return product_list

    finally:
        print('>> Volviendo al menú de opciones.')