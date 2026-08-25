import paquete_extras.funciones_booleanas as fb
# -------------------------------------------------------------
# Este archivo contiene funciones que son bucles de validación.
# -------------------------------------------------------------

def bucle_ingresar_palabra(prompt = '', text_valid = []):
    '''
    Función que mantiene un bucle hasta que se el string a ingresar sea una palabra de solo letras
    dentro de una lista de strings válidos.
    
    El parámetro prompt es la indicación de lo que debe ingresar el usuario
    al igual que la función input.

    El parámetro text_valid es una lista de strings que son válidos para romper el bucle.
    
    Esta función retorna el texto que ingresa el usuario  en formato string.
    '''

    while True:
        text = input(prompt).strip()
        if not text.isalpha():
            print('Error: Solo se admiten letras.')
        elif text_valid != [] and text not in text_valid:
            print('Error: No está dentro de los textos válidos.')
        else:
            return text

def bucle_ingresar_numero(prompt = '', inf = None, sup = None, min = False, max = False, integer = False):
    '''
    Función que mantiene un bucle hasta que el string a ingresar sea un número real 
    dentro de un intervalo.
    
    El parámetro prompt es la indicación de lo que debe ingresar el usuario 
    al igual que la función input.
    
    Los parámetros inf, sup son los extremos abiertos del intervalo abierto. 
    Por defecto, ambos son None.
    
    Si deseas incluir alguno de los los extremos en el intervalo
    cambia alguno de los parámetros min o max a True. Si quieres que el número sea
    estrictamente un número entero, cambia el parámetro integer a True.

    Esta función retorna el número que ingresa el usuario en formato string.
    '''

    # Cambia el mensaje de error dependiendo de si se debe ingresar un número real o entero.
    not_number_error = 'Error: Solo se admiten números.' 
    if integer == True:
        not_number_error = 'Error: Solo se admiten números enteros.'

    while True:
        number = input(prompt).strip()
        if not fb.es_positivo(number, integer) and not fb.es_negativo(number, integer): # Si no es un número
            print(not_number_error)
        elif not fb.en_intervalo(float(number), inf, sup, min, max): # Si no se encuentra en un intervalo
            print('Error: Número fuera de rango.')
        else:
            return number

if __name__ == '__main__':
    bucle_ingresar_palabra('Texto: ', ['Test1', 'Test2'])
    bucle_ingresar_numero(prompt='Número: ', inf=3, sup=20, min=True, max=True)