'''
Actividad 3
A partir del código del ejercicio 1, se mantiene el código original pero se le
añaden los bloques try-except para que la ejecución del programa no se frene
por errores.
'''

a = 10

b = input('Introduce un número: ')

try:
    result = a / b

    print(f'Resultado: {result}')

except:
    print('Ocurrió un error, no se pudo realizar la división porque el valor ingresado no es un número o es cero.')

numbers = [1, 2, 3]

try:
    print(numbers[5])

except:
    print('El índice ingresado está fuera del rango de la lista.')