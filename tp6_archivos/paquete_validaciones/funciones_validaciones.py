# -------------------------------------------------------------------------------
# Este módulo contiene funciones de validación de valores de ingreso del usuario.
# -------------------------------------------------------------------------------
from math import inf as infinite

def enter_word(prompt = '', valid_words = [], invert_condition = False, invalid_prompt = ''):
    '''
    Esta función es un bucle de validación de palabras que ingrese el usuario. Se romperá dicho bucle si
    el usuario ingresa una palabra válida y retornará dicha palabra. Una condición obligatoria es que la 
    palabra sea un string de carácteres alfabéticos. 

    prompt sirve para indicarle al usuario que debe ingresar.

    El parámetro valid_words es una lista de palabras válidas que puede ingresar el usuario.
    
    invert_condition invierte la condición de valid_words, haciendo que la lista de palabras válidas se
    vuelvan inválidas, obligando al usuario que no ingrese esas palabras.

    invalid_prompt indica que la palabra ingresada no es válida, esto aplica solo si se invierte la
    condición de valid_words.
    '''

    while True:
        word = input(prompt).lower().strip()

        # Cambio de la condición de palabras válidas
        words_condition = valid_words != [] and not word in valid_words
        prompt_error = '[X] Error: No está entre las opciones válidas.'
        if invert_condition:
            words_condition = valid_words != [] and word in valid_words
            prompt_error = invalid_prompt

        if not word.isdigit(): # Validación de palabra de carácteres alfabéticos
            print('[X] Error: Carácter inválido. Solo se admiten carácteres alfabéticos.')

        elif words_condition:
            print(prompt_error)

        else:
            return word

def enter_number(prompt = '', inf = -infinite, sup = infinite, is_min = False, is_max = False, integer = False):
    '''
    Esta función es un bucle de validación de números que ingrese el usuario. Se romperá dicho bucle si
    el usuario ingresa un número válido, retornando dicho número. Por defecto, una condición obligatoria
    es que el número sea real/punto blotante, pero puede cambiarse a número entero si se cambia el parámetro
    integer a True.

    Los parámetros inf y sup son extremos de un intervalo de números válidos. Por defecto ambos son infinitos.
    Ambos parámetros no están incluidos en los intervalos, para incluirlos cambiar los parámetros is_min o
    is_max a True respectivamente.
    '''

    while True:
        try:
            number = float(input(prompt).strip())
            # Esto convierte el número a entero
            if integer:
                number = int(number)

            # Condiciones del intervalo válido
            inf_condition = inf < number
            sup_condition = number < sup
            if is_min:
                inf_condition = inf <= number
            if is_max:
                sup_condition = number <= sup

            # Esto valida si el número está o no en el intervalo válido
            if not (inf_condition and sup_condition):
                print('[X] Error: Número fuera de rango.')

        except ValueError:
            print('[X] Error: Se debe ingresar un número.')

        except Exception as unexpected_exception:
            print('[X] Ocurrió un error inesperado.')
            print(f'> Error {type(unexpected_exception).__name__}: {unexpected_exception}')

        else:
            return number