'''
Actividad 4
Se realiza lo mismo que el ejercicio 3 pero aplicando múltiples excepciones
para los diferentes tipos de errores posibles.

NOTA: Se modifica el código original para que sea viable la posibilidad de que
se ejecute el bloque else del primer try-except. Por lo que se cambiará lo siguiente:

- Bucle while True para poder mostrar que el bloque finally se ejecuta siempre.

- Aplicación del constructor int al valor ingresado por el usuario para garantizar
la posible ejecución del bloque de excepción ZeroDivisiónError y el bloque else.

- Se reemplaza TypeError por ValueError debido a que al aplicar el constructor int
el TypeError no sucederá, en cambio, puede ocurrir un ValueError.
'''

a = 10

while True:
    try:
        b = int(input('Introduce un número: '))

        result = a / b

        print(f'Resultado: {result}')

    except ValueError:
        print('Error: El valor ingresado debe ser un número entero.')

    except ZeroDivisionError:
        print('Error: No se puede dividir por cero.')

    else:
        print('Esto se ejecutará si no hubo un error.')
        break

    finally:
        print('Esto se ejecutará siempre')



numbers = [1, 2, 3]

try:
    print(numbers[5])

except IndexError:
    print('El índice ingresado está fuera del rango de la lista.')
