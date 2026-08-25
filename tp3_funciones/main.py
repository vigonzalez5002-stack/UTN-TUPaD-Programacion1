import paquete_texto.funciones_texto as ftext
import paquete_matematica.funciones_calculo as fmath
import paquete_extras.funciones_bucle as floop

# --------------------------------------------------------------------------------
# Este archivo es el programa principal donde se ejecutarán todas las resoluciones
# de los ejercicios.
# 
# Acerca del paquete extras: Creé un paquete extra de funciones con el objetivo de 
# aplicar validaciones a los ingresos del usuario.
# --------------------------------------------------------------------------------

while True:
    print(f'''
------------ Menú de opciones -----------------
1. Para imprimir "Hola mundo!".
2. Para saludarte.
3. Para presentarte.
4. Para mostar el área y el perímetro de un círculo.
5. Para convertir los segundos a horas.
6. Para mostrar la tabla de multiplicar de un número.
7. Para mostrar los resultados de operacionese básicas con dos números.
8. Para mostrar tu índice de masa corporal.
9. Para convertir la temperatura de grados Celsius a grados Fahrenheit.
10. Para mostrar el promedio de tres números.
11. Para finalizar el programa.
-----------------------------------------------''')
    option = int(floop.bucle_ingresar_numero('Opción: ', 1, 11, min = True, max = True, integer = True))
    print()

    match option:
        case 1: # Actividad 1
            ftext.imprimir_hola_mundo()

        case 2: # Actividad 2
            name = floop.bucle_ingresar_palabra('Ingresa tu nombre: ')
            ftext.saludar_usuario(name)

        case 3: # Actividad 3
            name = floop.bucle_ingresar_palabra('Ingresa tu nombre: ')
            surname = floop.bucle_ingresar_palabra('Ingresa tu apellido: ')
            age = floop.bucle_ingresar_numero('Ingresa tu edad: ', 0, min = True, integer = True)
            residence = floop.bucle_ingresar_palabra('Ingresa tu residencia: ')
            ftext.informacion_personal(name, surname, age, residence)

        case 4: # Actividad 4
            radio = float(floop.bucle_ingresar_numero('Ingrese el radio de la circunferencia: ', 0, min = True))
            area = float(fmath.calcular_area_circulo(radio))
            perimeter = fmath.calcular_perimetro_circulo(radio)
            print(f'El círculo de radio {radio} tiene un área de {area:.2f} unidades cuadradas y un perímetro de {perimeter:.2f} unidades.')
            
        case 5: # Actividad 5
            seconds = float(floop.bucle_ingresar_numero('Ingresa los segundos a convertir: ', 0, min = True))
            hour = fmath.segundos_a_horas(seconds)
            print(f'{seconds} segundos equivale a {hour:.2f} horas.')
            
        case 6: # Actividad 6
            number = int(floop.bucle_ingresar_numero('Ingresa un número: ', integer = True))
            ftext.tabla_multiplicar(number)
            
        case 7: # Actividad 7
            number1 = int(floop.bucle_ingresar_numero('Ingresa el primer número: ', integer = True))
            number2 = int(floop.bucle_ingresar_numero('Ingresa el segundo número: ', integer = True))
            ftext.mostrar_operaciones(number1, number2)

        case 8: # Actividad 8
            weight = float(floop.bucle_ingresar_numero('Ingresa tu peso en kilogramos: ', 0))
            height = float(floop.bucle_ingresar_numero('Ingresa tu altura en metros: ', 0))
            imc = fmath.calcular_imc(weight, height)
            print(f'Con tu peso de {weight} kg y una altura de {height} metros tu índice de masa corporal es {imc:.2f}')

        case 9: # Actividad 9
            celsius = float(floop.bucle_ingresar_numero('Ingresa los celsius a convertir: '))
            fahrenheit = fmath.celsius_a_fahrenheit(celsius)
            print(f'{celsius}ºC equivale a {fahrenheit:.2f}ºF.')

        case 10: # Actividad 10
            number1 = float(floop.bucle_ingresar_numero('Ingresa el primer número: '))
            number2 = float(floop.bucle_ingresar_numero('Ingresa el segundo número: '))
            number3 = float(floop.bucle_ingresar_numero('Ingresa el tercer número: '))
            average = fmath.calcular_promedio(number1, number2, number3)
            print(f'El promedio entre {number1}, {number2} y {number3} es {average:.2f}')

        case 11: # Finalizar programa
            print('Finalizando programa.')
            break