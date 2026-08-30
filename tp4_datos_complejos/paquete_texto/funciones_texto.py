def imprimir_diccionario(dictionary, prompt = 'Diccionario:'):
    '''
    Imprime los pares clave valor de un diccionario con formato.
    El parámetro prompt permite añadir un texto previo a la impresión,
    como por ejemplo "Diccionario de frutas".
    '''
    print(prompt)
    for key, value in dictionary.items():
        print(f'{key}: {value}')
    print()

def imprimir_secuencia(sequence, prompt=''):
    '''
    Imprime una secuencia como listas o tuplas con formato.
    El parámetro prompt permite añadir un texto previo a la impresión,
    como por ejemplo "Lista de compras".
    '''

    print(prompt)
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            print(sequence[i], end = ', ')
        else:
            print(sequence[i])