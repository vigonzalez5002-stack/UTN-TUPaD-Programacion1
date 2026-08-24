import funciones_booleanas as fb

def bucle_ingresar_palabra(prompt = ''):
    '''
    Función que mantiene un bucle hasta que se el string a ingresar sea una palabra de solo letras.
    El parámetro prompt  es la indicación de lo que debe ingresar el usuario, al igual que la función input.
    Esta función retorna el texto en formato string que ingresa el usuario.
    '''
    while True:
        text = input(prompt).strip()
        if not text.isalpha():
            print(f'Error: Solo se admiten letras.')
        else:
            return text

def bucle_ingresar_numero(prompt = ''):
    '''
    Función que mantiene un bucle hasta que el string a ingresar sea un número.
    El parámetro prompt es la indicación de lo que debe ingresar el usuario, al igual que la función input.
    Esta función retorna el número en formato string que ingresa el usuario.
    '''
    while True:
        number = input(prompt).strip()
        if not fb.es_positivo(number) or not fb.es_negativo(number):
            print(f'Error: Solo se admiten números.')
        else:
            return number