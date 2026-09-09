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
        return 1/ exponential(base, -exponent)

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
    if number < 2:
        return str(number)

    # Caso recursivo
    return binary(number // 2) + str(number % 2)

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 5
def is_palindrome(palabra):
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
    return is_palindrome(palabra[1:-1])

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 6
def sum_digits(number):
    '''
    Recibe un número entero positivo y retorna la suma de sus dígitos.
    '''

    # Caso base
    if number < 10:
        return number

    # Caso recursivo
    return sum_digits(number // 10) + number % 10

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 7
def count_blocks(level):
    '''
    Esta función recibe la cantidad de niveles que tiene una pirámide y retorna
    el total de bloques que se necesita para construirla.
    '''

    # Caso base
    if level == 0:
        return 0

    # Caso recursivo
    return level + count_blocks(level - 1)

# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------

# Actividad 8
def count_digit(number, digit):
    '''
    Función que recibe un número entero positivo y un dígito entre 0 y 9 y retorna cuantas
    veces aparece el dígito dentro del número.
    '''
    # Contador
    if number % 10 == digit:
        count = 1
    else:
        count = 0
            
    # Caso base
    if number < 10:
        return count

    # Caso recursivo
    return count + count_digit(number // 10, digit)
