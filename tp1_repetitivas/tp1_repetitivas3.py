'''
Ejercicio 3 --- Agenda de Turnos con Nombres
El sistema recibe el nombre del operador(operator) y reserva; cancela; muestra turnos, a quien corresponde dicho turno 
y en que día; y muestra un resumen general de los turnos.
Las variables que recibe el sistema se someten a validación utilizando .isalpha() para el ingreso de nombres e
.isdigit() para el ingreso de números, además de su respectivo rango de valores.

NOTA: Si bien es posible desarrollar el sistema de turnos adaptando los strings para que emulen ser listas y así poder
reservar, cancelar, mostrar y contar turnos, la legibilidad del código se vería afectada. Por lo que se decidió
utilizar variables independientes para cada turno.
'''
# Turnos
monday_1 = ''
monday_2 = ''
monday_3 = ''
monday_4 = ''
tuesday_1 = ''
tuesday_2 = ''
tuesday_3 = ''

# Solicitud del nombre del operador.
while True:
    operator = input('Ingrese el nombre del operador: ').capitalize().strip()
    if not operator.isalpha():
        print('Error: El nombre del operador debe tener solo letras.')
    else:
        break

while True:
    print('''
-------- Menú --------
1. Reservar turno.
2. Cancelar turno.
3. Ver agenda del día.
4. Ver resumen general.
5. Cerrar sistema.
----------------------
''')
    while True:
        option = input('Elija una opción del menú: ')
        if not option.isdigit():
            print('Error: La opción debe ser un número entero.')
        elif not (option == '1' or option == '2' or option == '3' or option == '4' or option == '5'):
            print('Error: Opción fuera de rango.')
        else:
            break

    match option:
        case '1': # Reservar turno.
            while True:
                print('\n1 - Lunes \n2 - Martes')
                day = input('Ingrese el día: ')
                if not day.isdigit():
                    print('Error: El día debe ser un número entero.')
                elif not (day == '1' or day == '2'):
                    print('Error: Día fuera de rango.')
                else:
                    if day == '1':
                        print('Ha seleccionado el día lunes.')
                    elif day == '2':
                        print('Ha seleccionado el día martes.')
                    break

            while True:
                name = input('\nIngrese el nombre del paciente: ').capitalize().strip()
                if not name.isalpha():
                    print('Error: El nombre del paciente debe tener solo letras.')
                else:
                    break

            # Reservación de turnos para el día lunes.
            if day == '1':
                if monday_1 == name or monday_2 == name or monday_3 == name or monday_4 == name:
                    print(f'El paciente {name} ya reservó un turno para este día.')
                elif monday_1 == '':
                    monday_1 = name
                    print(f'Turno reservado para {name} en el día lunes.')
                elif monday_2 == '':
                    monday_2 = name
                    print(f'Turno reservado para {name} en el día lunes.')
                elif monday_3 == '':
                    monday_3 = name
                    print(f'Turno reservado para {name} en el día lunes.')
                elif monday_4 == '':
                    monday_4 = name
                    print(f'Turno reservado para {name} en el día lunes.')
                else:
                    print('No hay turnos disponibles para el día lunes.')

            # Reservación de turnos para el día martes.
            elif day == '2':
                if tuesday_1 == name or tuesday_2 == name or tuesday_3 == name:
                    print(f'El paciente {name} ya reservó un turno para este día.')
                elif tuesday_1 == '':
                    tuesday_1 = name
                    print(f'Turno reservado para {name} en el día martes.')
                elif tuesday_2 == '':
                    tuesday_2 = name
                    print(f'Turno reservado para {name} en el día martes.')
                elif tuesday_3 == '':
                    tuesday_3 = name
                    print(f'Turno reservado para {name} en el día martes.')
                else:
                    print('No hay turnos disponibles para el día martes.')

        case '2': # Cancelar turno.
            while True:
                print('\n1 - Lunes \n2 - Martes')
                day = input('Ingrese el día: ')
                if not day.isdigit():
                    print('Error: El día debe ser un número entero.')
                elif not (day == '1' or day == '2'):
                    print('Error: Día fuera de rango.')
                else:
                    if day == '1':
                        print('Ha seleccionado el día lunes.')
                    elif day == '2':
                        print('Ha seleccionado el día martes.')
                    break

            while True:
                name = input('\nIngrese el nombre del paciente: ').capitalize().strip()
                if not name.isalpha():
                    print('Error: El nombre del paciente debe tener solo letras.')
                else:
                    break

            # Cancelación de turnos para el día lunes.
            if day == '1':
                if monday_1 == name:
                    monday_1 = ''
                    print(f'Turno cancelado para {name} en el día lunes.')
                elif monday_2 == name:
                    monday_2 = ''
                    print(f'Turno cancelado para {name} en el día lunes.')
                elif monday_3 == name:
                    monday_3 = ''
                    print(f'Turno cancelado para {name} en el día lunes.')
                elif monday_4 == name:
                    monday_4 = ''
                    print(f'Turno cancelado para {name} en el día lunes.')
                else:
                    print(f'El paciente {name} no reservó un turno para este día.')
    
            # Cancelación de turnos para el día martes. 
            elif day == '2':
                if tuesday_1 == name:
                    tuesday_1 = ''
                    print(f'Turno cancelado para {name} en el día martes.')
                elif tuesday_2 == name:
                    tuesday_2 = ''
                    print(f'Turno cancelado para {name} en el día martes.')
                elif tuesday_3 == name:
                    tuesday_3 = ''
                    print(f'Turno cancelado para {name} en el día martes.')
                else:
                    print(f'El paciente {name} no reservó un turno para este día.')
            
        case '3': # Ver agenda del día.
            while True:
                print('\n1 - Lunes \n2 - Martes')
                day = input('Ingrese el día: ')
                if not day.isdigit():
                    print('Error: El día debe ser un número entero.')
                elif not (day == '1' or day == '2'):
                    print('Error: Día fuera de rango.')
                else:
                    if day == '1':
                        print('Ha seleccionado el día lunes.')
                    elif day == '2':
                        print('Ha seleccionado el día martes.')
                    break

            # Agenda del día lunes.
            if day == '1':
                if monday_1 == '':
                    print('\nTurno 1: libre')
                else:
                    print(f'\nTurno 1: {monday_1}')
                if monday_2 == '':
                    print('Turno 2: libre')
                else:
                    print(f'Turno 2: {monday_2}')
                if monday_3 == '':
                    print('Turno 3: libre')
                else:
                    print(f'Turno 3: {monday_3}')
                if monday_4 == '':
                    print('Turno 4: libre')
                else:
                    print(f'Turno 4: {monday_4}')
            
            # Agenda del día martes.
            elif day == '2':
                if tuesday_1 == '':
                    print('\nTurno 1: libre')
                else:
                    print(f'\nTurno 1: {tuesday_1}')
                if tuesday_2 == '':
                    print('Turno 2: libre')
                else:
                    print(f'Turno 2: {tuesday_2}')
                if tuesday_3 == '':
                    print('Turno 3: libre')
                else:
                    print(f'Turno 3: {tuesday_3}')

        case '4': # Resumen general.
            # Contadores de turnos ocupados.
            monday_count = 0
            tuesday_count = 0
            if monday_1 != '':
                monday_count += 1
            if monday_2 != '':
                monday_count += 1
            if monday_3 != '':
                monday_count += 1
            if monday_4 != '':
                monday_count += 1
            if tuesday_1 != '':
                tuesday_count += 1
            if tuesday_2 != '':
                tuesday_count += 1
            if tuesday_3 != '':
                tuesday_count += 1

            print(f'\nResumen general del operador {operator}:')
            if monday_count > tuesday_count:
                print(f'El día con más turnos es lunes con {monday_count} turnos ocupados.')
            elif tuesday_count > monday_count:
                print(f'El día con más turnos es martes con {tuesday_count} turnos ocupados.')
            else:
                print(f'Ambos días tienen la misma cantidad de turnos ocupados: {monday_count} turnos.')
            print(f'El día lunes tiene {monday_count} turnos ocupados y {4 - monday_count} turnos disponibles.')
            print(f'El día martes tiene {tuesday_count} turnos ocupados y {3 - tuesday_count} turnos disponibles.')

        case '5': # Cerrar sistema.
            print('Cerrando sistema...')
            break
