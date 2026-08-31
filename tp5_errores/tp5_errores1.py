'''
Actividad 1
Identificación de errores de un código.
'''

a = 10

b = input('Introduce un número: ')

result = a / b # TypeError: b es un string, por lo que no se puede realizar la división.

print(f'Resultado: {result}')

numbers = [1, 2, 3]

print(numbers[5]) # IndexError: El índice máximo de la lista es 2 y aquí intenta acceder a un indice fuera de rango.

# NOTA: Otro potencial error es en la linea 10, Si b llegara a ser el entero 0, no string 0, habría un ZeroDivisionError
# sin embargo, no lo consideraré pues b dentro de este código jamás será un entero, sino un string por cómo se definió
# la variable