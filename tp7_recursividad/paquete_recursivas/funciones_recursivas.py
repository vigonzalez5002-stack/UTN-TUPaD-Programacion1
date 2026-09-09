# -----------------------------------------------------------------------------------------------
# Este módulo de funciones corresponde con las funciones recursivas que solicitan los ejercicios.
# -----------------------------------------------------------------------------------------------

# Actividad 1
def factorial(number):
    '''
    Esta función calcula el factorial de un número de forma recursiva.
    '''

    # Caso base
    if number == 0:
        return 1

    # Caso recursivo
    return number * factorial(number - 1)

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------


# Actividad 2
def fibonacci(number):
    '''
    Esta función recursiva recibe un número y calcula su valor en la sucesión de fibonacci.
    '''

    # Caso base
    if number <= 1:
        return number

    # Caso recursivo
    return fibonacci(number - 1) + fibonacci(number - 2)

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 3
def exponential(base, exponent):
    '''
    Función recursiva que calcula la potencia de un número elevado a un exponente.
    '''

    # Caso base
    if exponent == 0:
        return 1

    # Caso recursivo para exponente negativo
    elif exponent < 0:
        return base * exponential(base, -exponent + 1)

    # Caso recursivo para exponente positivo o cero
    return base * exponential(base, exponent - 1)

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 4
def binary(number):
    '''
    Recibe un número entero positivo en base decimal y retorna su representación en binario
    como una cadena de texto.
    '''

    # Casos base
    if number == 0:
        return '0'

    elif number == 1:
        return '1'

    # Caso recursivo
    return binary(number // 2) + str(number % 2)

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 5
def es_palindromo(palabra):
    '''
    Recibe una cadena de texto sin espacios ni tildes y devuelve True si es un palíndromo, False
    si no lo es.
    '''

    # Casos base
    if len(palabra) < 2:
        return True

    elif palabra[0] != palabra[-1]:
        return False

    # Caso recursivo
    return es_palindromo(palabra[1:-1])

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 6