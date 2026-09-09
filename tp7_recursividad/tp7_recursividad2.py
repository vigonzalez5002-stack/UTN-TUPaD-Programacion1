'''
Actividad 2
Se usa una función recursiva que calcula el valor de la sucesión de fibonacci de un número.
Luego, se usa dicha función para mostrar la sucesión completa hasta el número de fibonacci del
número ingresado.
'''

def fibonacci(number):
    '''
    Esta función recursiva recibe un número y calcula su valor de la sucesión de fibonacci.
    '''

    # Caso base
    if number <= 1:
        return number

    # Caso recursivo
    return fibonacci(number - 1) + fibonacci(number - 2)

# --------------------------------------------------------------------------------------
# Este código muestra la sucesión de fibonacci completa hasta el número ingresado por el 
# usuario.
# --------------------------------------------------------------------------------------

stop = int(input('Ingresa hasta que posición calcular: '))
for i in range(stop + 1):
    print(f'\nFibonacci({i}) = {fibonacci(i)}')