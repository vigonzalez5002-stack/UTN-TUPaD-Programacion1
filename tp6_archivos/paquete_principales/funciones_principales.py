# ----------------------------------------------------------------------------------
# Este archivo contiene las funciones principales que corresponden a las actividades
# del trabajo.
# ----------------------------------------------------------------------------------

ARCHIVE = 'products.txt'

# Actividad 2
def show_archive(input_file):
    '''
    Esta función lee y muestra el archivo de texto plano ingresado con un formato.
    '''
    try:
        with open(input_file, 'r') as file:
            file_lines = file.readlines()
            

    except FileNotFoundError:
        print('Error: El archivo no existe.')

    except Exception as unexpected_error:
        print('Ha ocurrido un error inesperado.')
        print(f'{type(unexpected_error).__name__}: {unexpected_error}')

    finally:
        print('Volviendo al menú.')