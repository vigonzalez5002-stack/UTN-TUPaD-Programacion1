'''
Actividad 4
Se realiza lo mismo que el ejercicio 3 pero aplicando múltiples excepciones
para los diferentes tipos de errores posibles.
'''

a = 10

b = input('Introduce un número: ')

try:
    result = a / b

    print(f'Resultado: {result}')

except TypeError:
    print('Error: No se puede dividir un número entero por un string.')

except ZeroDivisionError: # Nunca pasará este error porque el código recibe el 0 como string, no como número.
    print('Error: No se puede dividir por cero.')

# NOTA: En caso de que se use el constructor int o float a la variable b, habría que añadir el error ValueError
# al intentar convertir un string que no está formado por números, por ejemplo int('Hola')

numbers = [1, 2, 3]

try:
    print(numbers[5])

except IndexError:
    print('El índice ingresado está fuera del rango de la lista.')