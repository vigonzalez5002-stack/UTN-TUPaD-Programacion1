from paquete_matematica.funciones_calculo import operaciones_basicas
# ---------------------------------------------------------------------
# Este archivo contiene funciones que imprimen mensajes en la terminal.
# ---------------------------------------------------------------------

# Actividad 1
def imprimir_hola_mundo():
    '''
    Al invocar esta función imprime en la terminal "Hola mundo!."
    '''

    print('Hola mundo!')

# Actividad 2
def saludar_usuario(name):
    '''
    Recibe el nombre de un usuario e imprime un saludo personalizado.
    '''

    print(f'Hola {name}!')

# Actividad 3
def informacion_personal(name, surname, age, residence):
    '''
    Recibe la información personal(nombre, apellido, edad y recidencia) e imprime una presentación.
    '''

    print(f'Soy {name} {surname}, tengo {age} años y vivo en {residence}.')

# Actividad 6
def tabla_multiplicar(number):
    '''
    Imprime en la terminal la tabla de multiplicar de un número.
    '''

    print(f'Tabla de multiplicar del {number}:')
    for factor in range(1, 11):
        resultado = operaciones_basicas(number, factor)[2] # Uso de la actividad 7
        print(f'{number} * {factor} = {resultado}')

# Actividad 7 (Impresión)
def mostrar_operaciones(number1, number2):
    '''
    Recibe dos números y muestra los resultados de las operaciones básicas(Suma, resta, multiplicación
    y división).
    '''

    operation = ['+', '-', '*', '/']
    result = operaciones_basicas(number1, number2)

    print('Resultados de cada operación:')
    for i in range(4):
        result_string = f'{result[i]}'
        if i == 3:
            result_string = f'{result[i]:.2f}'
        print(f'{number1} {operation[i]} {number2} = {result_string}')