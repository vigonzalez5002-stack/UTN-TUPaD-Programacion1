# -------------------------------------------------------------------------------
# Este paquete contiene funciones de utilidades que ayudan a optimizar el código.
# -------------------------------------------------------------------------------

import csv

def load_products(input_file):
    '''
    Esta función recibe un archivo que contiene productos y los retorna una lista
    donde cada elemento es un diccionario con las claves nombre, precio, cantidad.
    '''

    try:
        with open(input_file, 'r', encoding = "utf-8") as file:
            product_list = csv.DictReader(file)

    except FileNotFoundError:
        print('Error: El archivo no existe.')
        return None
    
    except Exception as unexpected_error:
        print('Ha ocurrido un error inesperado.')
        print(f'{type(unexpected_error).__name__}: {unexpected_error}')
        return None

    else:
        return product_list