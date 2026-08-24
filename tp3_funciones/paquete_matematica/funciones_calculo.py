from math import pi

# Actividad 4.1 (Cálculo de area del un círculo)
def calcular_area_circulo(radio : int) -> float:
    '''
    Recibe el radio de un círculo y devuelve el área del mismo.
    '''
    return pi * (radio ** 2)

# Actividad 4.2 (Cálculo del perímetro de un círculo)
def calcular_perimetro_circulo(radio : int) -> float:
    '''
    Recibe el radio de un círculo y devuelve su perímetro.
    '''
    return 2 * pi * radio

# Actividad 5
def segundos_a_horas(second : int) -> float:
    '''
    Retorna la cantidad de horas que le corresponde a la cantidad de segundos ingresado.
    NOTA: Esta función retorna la hora en flotante.
    '''
    return second / 3600

def multiplicar(number1 : int, number2 : int) -> int:
    '''
    Retorna la multiplicación entre los dos números que recibe.
    '''
    return number1 * number2

if __name__ == '__main__':
    print(calcular_perimetro_circulo(1))