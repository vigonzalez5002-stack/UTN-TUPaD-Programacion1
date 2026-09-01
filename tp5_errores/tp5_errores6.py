'''
Actividad 6
Programa que pide un número al usuario y valida si el número ingresado es
númerico o hay algún otro tipo de error, imprimiendo en la terminal dichos
errores.
En caso de que el número ingresado sea válido, se imprimirá dicho número
en pantalla.
'''

try:
    number = int(input('Ingresa un número: '))

except ValueError:
    print('\nError: El valor ingresado debe ser un número entero.')

except Exception as unknown_exception:
    print(f'\nSe produjo un error inesperado: {type(unknown_exception).__name__}')

else:
    print(f'El número ingresado fue: {number}')
