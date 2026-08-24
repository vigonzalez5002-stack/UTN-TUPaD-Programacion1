from paquete_matematica.funciones_calculo import multiplicar

# Actividad 1
def imprimir_hola_mundo():
    '''
    Al invocar esta función imprime en la terminal "Hola mundo!."
    '''
    print('Hola mundo!')

# Actividad 2
def saludar_usuario(name : str):
    '''
    Recibe el nombre de un usuario e imprime un saludo personalizado.
    '''
    print(f'Hola {name}!')

# Actividad 3
def informacion_personal(name : str, surname : str, age : int, residence : int):
    '''
    Recibe la información personal(nombre, apellido, edad y recidencia) e imprime una presentación.
    '''
    print(f'Soy {name} {surname}, tengo {age} años y vivo en {residence}.')

# Actividad 6
def tabla_multiplicar(number : int):
    '''
    Imprime en la terminal la tabla de multiplicar de un número.
    '''
    print(f'Tabla de multiplicar del {number}')
    for factor in range(1, 11):
        print(f'{number} * {factor} = {multiplicar(number, factor)}')

if __name__ == '__main__':
    tabla_multiplicar(1)