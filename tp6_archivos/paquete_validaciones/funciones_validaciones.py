# -------------------------------------------------------------------------------
# Este módulo contiene funciones de validación de valores de ingreso del usuario.
# -------------------------------------------------------------------------------

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