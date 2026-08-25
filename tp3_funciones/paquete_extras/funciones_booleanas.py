# ----------------------------------------------------------------------
# Este archivo contiene funciones que sirven para condiciones booleanas.
# ----------------------------------------------------------------------

def es_positivo(number_txt, integer = False):
    '''
    Función que recibe un string y retorna un booleano.
    El parámetro integer fuerza a que el string deba ser estrictamente un número entero.
    
    True si el string es un número positivo, False si no lo es.
    '''

    if not integer: # Para separar la parte entera de la decimal
        number_list = number_txt.split('.')
    else:
        number_list = [number_txt]
    
    if len(number_list) == 2 and number_list[0].isdigit() and number_list[1].isdigit(): # Para decimal
        return True
    elif len(number_list) == 1 and number_list[0].isdigit(): # Para entero
        return True
    return False

def es_negativo(number_txt, integer):
    '''
    Función que recibe un string y retorna un booleano.
    El parámetro integer fuerza a que el string deba ser estrictamente un número entero.
    
    True si el string es un número negativo, False si no lo es.
    '''

    return len(number_txt) > 1 and number_txt[0] == '-' and es_positivo(number_txt[1::], integer)

def en_intervalo(number, inf = None, sup = None, min = False, max = False):
    '''
    Retorna un booleano en función de si el número ingresado está o no en un intervalo.
    Los parámetros inf, sup son los extremos del intervalo abierto. Por defecto, ambos son None.
    
    Si deseas incluir alguno de los los extremos en el intervalo, cambia alguno de los parámetros min o max a True.
    
    Retornará True si el número está en el intervalo, False en caso contrario.
    '''

    inf_condition = inf == None or number > inf # Condición del ínfimo del intervalo
    sup_condition = sup == None or number < sup # Condición del supremo del intervalo
    if min:
        inf_condition = inf == None or number >= inf
    if max:
        sup_condition = sup == None or number <= sup

    return inf_condition and sup_condition

if __name__ == '__main__':
    print(es_positivo('10'))
    print(es_negativo('10'))
    print(en_intervalo(10, inf = 5, sup = 10, min = False, max = True))