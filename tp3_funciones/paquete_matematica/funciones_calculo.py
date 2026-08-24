from math import pi

# Actividad 4.1 (Cálculo de area del un círculo)
def calcular_area_circulo(radio):
    '''
    Recibe el radio de un círculo y devuelve el área del mismo.
    '''
    return pi * (radio ** 2)

# Actividad 4.2 (Cálculo del perímetro de un círculo)
def calcular_perimetro_circulo(radio):
    '''
    Recibe el radio de un círculo y devuelve su perímetro.
    '''
    return 2 * pi * radio

# Actividad 5
def segundos_a_horas(second):
    '''
    Retorna la cantidad de horas que le corresponde a la cantidad de segundos ingresado.
    NOTA: Esta función retorna la hora como punto flotante.
    '''
    return second / 3600

# Actividad 7
def operaciones_basicas(number1, number2):
    '''
    Retorna una tupla con el resultado de operaciones básicas.
    Tupla retornada: (sumados, restados, multiplicados, divididos)
    '''
    return number1 + number2, number1 - number2, number1 * number2, number1 / number2

# Actividad 8
def calcular_imc(weight, height):
    '''
    Recibe el peso en kilogramos y la altura en metros y retorna el índice de masa corporal.
    '''
    return weight / (height ** 2)

# Actividad 9
def celsius_a_fahrenheit(celsius):
    '''
    Esta función hace la conversión de temperatura de Celsius a Fahrenheit, retornando esta última.
    '''
    return 1.8 * celsius + 32

# Actividad 10
def calcular_promedio(number1, number2, number3):
    '''
    Retorna el promedio de 3 números.
    '''
    return (number1 + number2 + number3) / 3