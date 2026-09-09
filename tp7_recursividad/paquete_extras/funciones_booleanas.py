# ----------------------------------------------------------------------------------------------
# Este módulo contiene funciones booleanas que servirán para asistir a las funciones validación.
# ----------------------------------------------------------------------------------------------

from math import inf as infinite

def in_range(number, inf = -infinite, sup = infinite, is_min = False, is_max = False):
    '''
    Retorna True si el número se encuentra en el intervalo, False en caso contrario.

    inf, sup: Extremos de un intervalo abierto válido.
    
    is_min, is_max: Incluye los extremos en el intervalo.
    '''

    # Cambio de condición del intervalo
    inf_condition = inf < number
    sup_condition = number < sup
    if is_min:
        inf_condition = inf <= number
    if is_max:
        sup_condition = number <= sup

    # Retorno del booleano
    if inf_condition and sup_condition:
        return True

    return False

# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------

def has_accent(word):
    '''
    Retorna True si la palabra tiene una tilde, False en caso contrario.
    '''

    # Chequeo carácter por carácter
    for char in word:
        if char.lower() in 'áéíóú':
            return True

    return False