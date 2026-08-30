# ---------------------------------------------------------
# Este archivo contiene funciones hechos para la validación
# de datos ingresados por el usuario.
# ---------------------------------------------------------

from math import inf as infinite
import paquete_validaciones.funciones_booleanas as fbool

def ingresar_texto(prompt = '', text_valid = [], not_text_valid = False):
    '''
    Esta función es un bucle de validación que controla el ingreso
    de textos. Este bucle se terminará y retornará el texto si es 
    un string de únicamente letras.
    
    El parámetro prompt permite darle indicaciones de que ingresar al
    usuario.

    El parámetro text_valid permite establecer una lista de textos válidos.

    El parámetro not_text_valid invierte la lógica del parámetro text_valid,
    permitiendo admitir como válido el ingreso de textos que no se encuentran
    en la lista, mientras que un texto que se encuentre en la lista se toma
    como texto inválido.
    '''

    while True:
        text = input(prompt).strip()

        if not text.isalpha(): # Si el texto tiene carácteres inválido
            print('Error: Solo se admiten letras.')

        elif text_valid != []: #Si el text_valid no es vacío 
            # Cambio de condición por el parámetro not_text_valid
            text_valid_condition = text not in text_valid
            text_valid_error = 'Error: No se encuentra entre las opciones.'
            if not_text_valid:
                text_valid_condition = text in text_valid
                text_valid_error = f'Error: {text} ya está agregado'

            if text_valid_condition: # Condición del text_valid
                print(text_valid_error)
            else:
                return text
            
        else:
            return text

def ingresar_numero(prompt = '', inf = -infinite, sup = infinite, is_min = False, is_max = False, integer = False):
    '''
    Función que mantiene un bucle hasta que el string a ingresar sea un número real 
    dentro de un intervalo.
    
    El parámetro prompt es la indicación de lo que debe ingresar el usuario 
    al igual que la función input.
    
    Los parámetros inf, sup son los extremos del intervalo abierto. 
    Por defecto, ambos son infinitos.Si deseas incluir alguno de los 
    extremos en el intervalo cambia alguno de los parámetros min o max a True. 
    
    Si quieres que el número sea estrictamente un número entero, cambia el parámetro integer a True.

    Esta función retorna el número que ingresa el usuario en formato string.
    '''

    # Cambia el mensaje de error dependiendo de si se debe ingresar un número real o entero.
    not_number_error = 'Error por carácter inválido: Solo se admiten números.' 
    if integer:
        not_number_error = 'Error por carácter inválido: Solo se admiten números enteros.'

    while True:
        number = input(prompt).strip()
        if not (fbool.es_positivo(number, integer) or fbool.es_negativo(number, integer)): # Si no es un número
            print(not_number_error)
        elif not fbool.en_intervalo(float(number), inf, sup, is_min, is_max): # Si no se encuentra en un intervalo
            print(f'Error: Número fuera de rango. El rango de números es de {inf} a {sup}')
        else: # Si pasa las validaciones
            return number

def ingresar_telefono():
    '''
    Esta función es un bucle de validación que controla el ingreso de un
    número de teléfono. Este bucle se terminará y retornará el número de
    teléfono como entero si se ingresa un número de entero válido.
    '''

    while True:
        phone_number = input('Ingrese un número de teléfono: ').strip()
        if phone_number.isdigit() and len(phone_number) <= 15:
            return int(phone_number)
        else:
            print('Error: Número de teléfono inválido, ingrese un número válido que no exceda los 15 dígitos.')