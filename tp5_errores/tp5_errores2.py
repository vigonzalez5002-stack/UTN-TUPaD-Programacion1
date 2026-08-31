'''
Actividad 2
Corrección del código del ejercicio 1
'''

a = 10

while True: # Validación del ingreso de un número entero positivo para evitar el TypeError
    b = input('Introduce un número: ').strip()

    if not b.isdigit():
        print('Error: Ingrese un número entero positivo.')
    elif int(b) == 0: # Para evitar el ZeroDivisionError
        print('Error: El número no puede ser 0.')
    else:
        b = int(b)
        break

result = a / b 

print(f'Resultado: {result}')

numbers = [1, 2, 3]

print(numbers[2]) # Cambio el índice a 2 pues es el índice máximo para evitar el IndexError