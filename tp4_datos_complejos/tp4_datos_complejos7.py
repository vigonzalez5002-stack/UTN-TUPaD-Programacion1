'''
Actividad 7
Recibe un registro diario de asistencia a una capacitación en forma de lista.
El programa generará un conjunto a partir de la lista y mostrará la lista original,
el conjunto y cuantas veces asistió un empleado.

NOTA: Si bien la actividad no exije un sistema que permita ingresar las asistencias,
se decidió añadirlo para hacer más flexible el ejercicio a todo tipo de posibilidades.
''' 

# Se importarán paquetes para optimizar el código
from paquete_validaciones.funciones_validaciones import ingresar_texto, ingresar_numero
from paquete_texto.funciones_texto import imprimir_secuencia, imprimir_diccionario

# Lista de asistencia a la capacitación
attendance_list = []

# ----------------------------------------------------------------------------------
# Este código es un menú que permite registrar la asistencia de un empleado, mostrar
# la lista de asistencias, mostrara los empleados que asistieron al menos una vez y 
# cuantas veces asistió cada empleado.
# ----------------------------------------------------------------------------------

while True:

    # Menú
    print('''
------------------------- Menú -------------------------
1. Añadir a un empleado a la lista de asistencias.
2. Mostrar la lista de asistencias completa.
3. Mostrar los empleados que asistieron al menos una vez.
4. Mostrar cuantas veces asistió cada empleado.
5. Salir del programa.
--------------------------------------------------------''')
    option = int(ingresar_numero('Opción: ', 1, 5, True, True, True))

    match option:

        case 1: # Añade un empleado a la lista de asistencias
            print()
            name = ingresar_texto('Ingresa el nombre del empleado: ')
            attendance_list.append(name)
            print('\n[✔] Empleado se añadió a la lista de asistencias exitosamente.')

        case 2: # Muestra la lista de asistencias
            print()
            imprimir_secuencia(attendance_list, 'Lista completa de asistencias:')

        case 3: # Muestra los empleados que asistieron al menos una vez
            print()
            attendance_set = set(attendance_list)
            imprimir_secuencia(list(attendance_set), 'Empleados que asistieron al menos una vez:')

        case 4: # Muestra la cantidad de asistencias por empleado
            print()
            attendance_set = set(attendance_list)
            attendance_dictionary = {}
            for employee in attendance_set:
                attendance_dictionary[employee] = attendance_list.count(employee)
            imprimir_diccionario(attendance_dictionary, 'Cantidad de asistencias por empleado:')

        case 5: # Termina el programa
            print()
            print('Saliendo del programa...')
            break