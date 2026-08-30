# -----------------------------------------------------
# Este archivo contiene funciones retornan un booleano.
# -----------------------------------------------------

def es_positivo(number_txt, integer = False):
    '''
    Función que recibe un string y retorna un booleano.
    El parámetro integer fuerza a que el string deba ser estrictamente un número entero.
    
    True si el string es un número positivo o cero, False si no lo es.
    '''

    # Para entero
    if integer:
        return number_txt.isdigit()

    # Para decimal
    number_list = number_txt.split('.')
    if len(number_list) == 2:
        return number_list[0].isdigit() and number_list[1].isdigit()
    return number_txt.isdigit()