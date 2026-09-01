'''
Actividad 7
Se repite el ejercicio 6, pero añadiendo la posibilidad del usuario para que lo intente de nuevo.
'''
while True:
    try:
        number = int(input('Ingresa un número: '))

    except ValueError:
        print('\nError: El valor ingresado debe ser un número entero.')

    except Exception as unknown_exception:
        print(f'\nSe produjo un error inesperado: {type(unknown_exception).__name__}')

    else:
        print(f'El número ingresado fue: {number}')
        break