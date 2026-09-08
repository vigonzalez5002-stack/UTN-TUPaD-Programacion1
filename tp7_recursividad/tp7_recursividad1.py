'''
Actividad 1.
Se usa una función recursiva para calcular el factorial de un número. Luego, con dicha función,
se muestra en pantalla el factorial de todos los números enteros entre el 1 y el número que
indique el usuario.
'''

def factorial(number):
    '''
    Esta función calcula el factorial de un número de forma recursiva.
    '''

    if number == 0:
        return 1
    return number * factorial(number - 1)

# ----------------------------------------------------------------------------------------------
# Este código muestra en pantalla el factorial de todos los númerose enteros entre 1 y el número
# que indique el usuario.
# ----------------------------------------------------------------------------------------------

stop = int(input('Ingrese hasta que factorial calcular: '))
for i in range(1, stop + 1):
    print(f'\nEl factorial de {i} es {factorial(i)}')