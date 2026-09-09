# -----------------------------------------------------------------------------------------------
# Este módulo de funciones corresponde a funciones de validación de datos que ingresa el usuario.
# -----------------------------------------------------------------------------------------------

from math import inf as infinite
import paquete_extras.funciones_booleanas as fb

def enter_number(prompt = '', inf = -infinite, sup = infinite, is_min = False, is_max = False, is_integer = False):
    '''
    Valida el número que ingresa el usuario, retornando dicho número si es válido, si no lo es,
    debe volver a intentarlo.

    prompt: Mensaje de indicación de lo que debe ingresar el usuario.

    inf, sup: Extremos de un intervalo abierto válido.

    is_min, is_max: Incluye los extremos en el intervalo.

    is_integer: Fuerza a que el número a ingresar deba ser entero.
    '''

    while True:
        try:
            number = input(prompt).strip()

            # Validación y transformación si el número es flotante
            if not is_integer:
                number = float(number)

            # Validación si se ingresa un número decimal
            elif len(number.split('.')) != 1:
                print('Error: El número debe ser entero.')
                continue

            # Validación y transformación si el número es entero
            else:
                number = int(number)


            # Validación del intervalo
            if not fb.in_range(number, inf, sup, is_min, is_max):
                print('Error: Número fuera de rango')

            else:
                return number

        except ValueError:
            print('Error: Se debe ingresar un número.')

        except Exception as unexpected_exception:
            print('Ha ocurrido un error inesperado.')
            print(f'{type(unexpected_exception).__name__}: {unexpected_exception}')

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

def enter_word(prompt = ''):
    '''
    Valida la palabra ingresada por el usuario. Si es válida la retornará todo en minúsculas, 
    si no debe volver a intentarlo.

    prompt: Mensaje de indicación de lo que debe ingresar el usuario.
    
    '''

    while True:
        word = input(prompt).strip()

        # Validación si se ingresa un carácter inválido
        if not word.isalpha():
            print('Error: Se ingresó un carácter inválido.')

        # Validación si se ingresa un carácter con tilde
        elif fb.has_accent(word):
            print('Error: Se ingresó una palabra con tilde.')

        else:
            return word.lower()
