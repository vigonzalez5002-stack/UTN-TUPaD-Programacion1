# ---------------------------------------------------------
# Este archivo contiene funciones hechos para la validación
# de datos ingresados por el usuario.
# ---------------------------------------------------------

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

def ingresar_nota():
    '''
    Esta función es un bucle de validación que controla el ingreso de una nota.
    Este bucle se terminará y retornará la nota como punto flotante.
    '''

    while True:
        grade = input('Ingresa la nota: ').strip()
        if not fbool.es_positivo(grade):
            print('Error: La nota debe ser un número positivo o cero.')
        elif not (0 <= float(grade) <= 10):
            print('Error: Nota fuera de rango. Debe ser un número del 0 al 10.')
        else:
            return float(grade)

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