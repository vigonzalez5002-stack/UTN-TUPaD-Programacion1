def es_positivo(number_txt):
    '''
    Función que recibe un string y retorna un booleano.
    True si el string es un número positivo.
    False si no lo es.
    '''
    number_list = number_txt.split('.')
    if len(number_list) == 2 and number_list[0].isdigit() and number_list[1].isdigit():
        return True
    elif len(number_list) == 1 and number_list[0].isdigit():
        return True
    return False

def es_negativo(number_txt):
    '''
    Función que recibe un string y retorna un booleano.
    True si el string es un número negativo.
    False si no lo es.
    '''
    return len(number_txt) > 1 and number_txt[0] == '-' and es_positivo(number_txt[1::])
