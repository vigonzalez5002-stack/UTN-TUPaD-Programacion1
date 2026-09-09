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
    option = fv.enter_number('Opción: ', 1, 9, True, True, True)

    match option:

        # Actividad 1
        case 1:
            print()
            stop = fv.enter_number('Ingrese hasta que factorial calcular: ', 1, is_min = True, is_integer = True)
            print('\n Lista de factoriales')
            for i in range(1, stop + 1):
                print(f'Factorial de {i} es {fr.factorial(i)}')

        # Actividad 2
        case 2:
            pass

        # Actividad 3
        case 3:
            pass

        # Actividad 4
        case 4:
            pass

        # Actividad 5
        case 5:
            pass

        # Actividad 6
        case 6:
            pass

        # Actividad 7
        case 7:
            pass

        # Actividad 8
        case 8:
            pass

        # Salir del programa
        case 9:
            pass