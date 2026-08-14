'''
Ejercicio 2 --- Acceso al Campus y Menú Seguro
Sistema de login con intectos y un menú de acciones con validación estricta.
Login:
Ingreso y validación de usuario(user) y contraseña(password) hasta 3 intentos.
Menú:
Ingreso y validación de opciones(options).
Estado de inscripción.
Cambio de clave con validación y actualización de clave válida.
Mensaje motivacional.
Salida del programa.
'''
# Credenciales fijas.
valid_user = 'alumno'
valid_password = 'python123'

# Login.
attempts = 1 # Cantidad de intentos
is_logged = False # Flag de inicio del menú.
while attempts <= 3:
    print(f'\nIntentos {attempts}/3')
    user = input('Ingrese el nombre de usuario: ')
    password = input('Ingrese la contraseña: ')
    if user != valid_user or password != valid_password:
        print('Error: Usuario o contraseña inválida.')
        attempts += 1
    else:
        print('Acceso concedido.')
        is_logged = True
        break
if attempts == 4:
        print('Cuenta bloqueada.')

# Menú.
while is_logged == True:
    # Lista de opciones.
    print('''
------------- Menú -------------
1. Ver estado de la inscripción.
2. Cambiar contraseña.
3. Mostrar mensaje motivacional.
4. Salir.
--------------------------------''')
    
    # Ingreso y validación de opciones del menú.
    while True:
        option = input('Ingrese una opción: ').strip()
        if not option.isdigit():
            print('Error: Ingrese un número válido.')
        elif  not (1 <= int(option) <= 4):
            print('Error: Opción fuera de rango.')
        else:
            option_int = int(option)
            break

    # Ejecución de la opción elegida.   
    match option_int:
        case 1: # Estado de inscripción.
            print('Usuario inscripto.')
        case 2: # Cambio de contrasñea.
            while True:
                new_password = input('Ingrese una nueva contraseña. Debe tener un mínimo de 6 carácteres: ')
                if len(new_password) < 6:
                    print('Error: La contraseña debe tener un mínimo de 6 carácteres.')
                    continue
                confirm_password = input('Confirme la contraseña: ')
                if new_password != confirm_password:
                    print('Error: Las contraseñas no coinciden.')
                else:
                    print('Contraseña cambiada.')
                    valid_password = new_password # Inutilizable en esta resolución del ejercicio.
                    break
        case 3: # Mostrar mensaje motivacional.
            print('Equivocarse no es el final, es una oportunidad para ser mejor.')
        case 4: # Salir
            print('Saliendo del campus.')
            is_logged = False