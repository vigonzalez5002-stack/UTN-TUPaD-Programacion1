from math import inf as infinite # Para uso de intervalos de extremos infinitos

# ----------------------------------------------------------------------
# Este archivo contiene funciones que sirven para condiciones booleanas.
# ----------------------------------------------------------------------

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

def es_negativo(number_txt, integer = False):
    '''
    Función que recibe un string y retorna un booleano.
    El parámetro integer fuerza a que el string deba ser estrictamente un número entero.
    
    True si el string es un número negativo o cero, False si no lo es.
    '''

    return len(number_txt) > 1 and number_txt[0] == '-' and es_positivo(number_txt[1:], integer)

def en_intervalo(number, inf = -infinite, sup = infinite, is_min = False, is_max = False):
    '''
    Retorna un booleano en función de si el número ingresado está o no en un intervalo.
    Los parámetros inf, sup son los extremos del intervalo abierto. Por defecto, ambos son infinitos.
    
    Si deseas incluir alguno de los los extremos en el intervalo, cambia alguno de los parámetros is_min o is_max a True.
    
    Retornará True si el número está en el intervalo, False en caso contrario.
    '''

    inf_condition = number > inf # Condición del ínfimo del intervalo
    sup_condition = number < sup # Condición del supremo del intervalo
    if is_min:
        inf_condition = number >= inf # Cambio de condición para incluir el ínfimo en el intervalo
    if is_max:
        sup_condition = number <= sup # Cambio de condición para incluir el supremo en el intervalo

    return inf_condition and sup_condition

if __name__ == '__main__':
    print(es_positivo('10'))
    print(es_negativo('-10'))
    print(en_intervalo(10, inf = 11, is_min = True))