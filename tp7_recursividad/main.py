# -----------------------------------------------------------------------
# Este es el archivo principal, donde se ejecutarán todos los ejercicios.
# -----------------------------------------------------------------------

import paquete_recursivas.funciones_recursivas as fr
import paquete_extras.funciones_validacion as fv

while True:
    print('''
===============================================================
- - - - - - - - - - - Menú de actividades - - - - - - - - - - - 
===============================================================
1. Mostar factoriales.
2. Mostrar la sucesión de Fibonacci
3. Calcular la potencia de un número elevado a otro.
4. Transformar número a binario.
5. Verificar si un número es un palíndromo.
6. Sumar dígitos de un número.
7. Mostrar total de bloques para construir una pirámide.
8. Contar la cantidad de apariciones de un dígito en un número.
9. Salir del programa
===============================================================''')
    option = fv.enter_number('> Opción: ', 1, 9, True, True, True)

    match option:

        # Actividad 1
        case 1:
            stop = fv.enter_number('\nIngrese hasta que factorial calcular: ', 1, is_min = True, is_integer = True)
            print('\n>> Lista de factoriales:')
            for i in range(1, stop + 1):
                print(f'{i}! = {fr.factorial(i)}')

        # Actividad 2
        case 2:
            stop = fv.enter_number('\nIndique hasta que valor evaluar la sucesión de Fibonacci: ', 0, is_min = True, is_integer = True)
            print('\n>> Lista de la sucesión de Fibonacci:')
            for i in range(stop + 1):
                print(f'Fibonacci({i}) = {fr.fibonacci(i)}')

        # Actividad 3
        case 3:
            base = fv.enter_number('\nIngrese la base de la potencia: ', 0, is_min = True)
            exponent = fv.enter_number('\nIngrese el exponente: ')
            print(f'\n>> {base} elevado a {exponent} da {fr.exponential(base, exponent)}.')

        # Actividad 4
        case 4:
            number = fv.enter_number('\nIngrese un número entero positivo: ', 0, is_integer = True)
            print(f'\n>> El número {number} en binario es {fr.binary(number)}')

        # Actividad 5
        case 5:
            word = fv.enter_word('\nIngrese una palabra: ')
            print(f'\n>> ¿Es {word} palíndromo? {fr.is_palindrome(word)}')

        # Actividad 6
        case 6:
            number = fv.enter_number('\nIngrese un número entero positivo: ', 0, is_integer = True)
            print(f'\n>> La suma de los dígitos de {number} es {fr.sum_digits(number)}')
            
        # Actividad 7
        case 7:
            pass

        # Actividad 8
        case 8:
            pass

        # Salir del programa
        case 9:
            pass