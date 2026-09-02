# ----------------------------------------------------------------------------------
# Este archivo contiene las funciones principales que corresponden a las actividades
# del trabajo.
# ----------------------------------------------------------------------------------

from paquete_utilidades.funciones_utiles import load_products

ARCHIVE = 'products.txt'

# Actividad 2
def show_archive(input_file):
    '''
    Esta función lee y muestra el archivo de texto plano ingresado con un formato.
    '''
    try:
        product_list = load_products(input_file)
        

    except FileNotFoundError:
        print('Error: El archivo no existe.')

    except Exception as unexpected_error:
        print('Ha ocurrido un error inesperado.')
        print(f'{type(unexpected_error).__name__}: {unexpected_error}')

    finally:
        print('Volviendo al menú.')