'''
Ejercicio 4 --- Escape Room: La Bóveda
Programa que simula un Escape Room:
Un agente(El usuario) intenta acceder a una bóveda con 3 cerraduras. El agente tiene un límite de energía y tiempo.
El usuario tiene a su disposición el menú de acciones: Forzar cerradura, hackear panel, descansar.
Donde cada uno suma o resta energía y tiempo.
Además, la acción Forzar cerradura tiene una regla de anti-spam para evitar elegir la opción 3 veces seguidas.
'''
# Variables prefijadas
energy = 100
time = 12
open_locks = 0
alarm = False
partial_code = ''
force_lock_count = 0
alarm_lockout = False

while True:
    agent = input('Ingrese el nombre del agente: ').capitalize().strip()
    if not agent.isalpha():
        print('Error: El nombre del agente debe estar formado por letras.')
    else:
        break

while energy > 0 and time > 0 and open_locks < 3 and alarm_lockout == False:
    # Menú de acciones y estado actual del agente.
    print(f'''
Agente: {agent}
------------- Estado Actual del Agente -------------
Energía: {energy} | Tiempo: {time} | Cerraduras abiertas: {open_locks}
Código parcial actual: {partial_code}
Estado de la alarma(ON = True, OFF = False): {alarm}

----------------- Menú de Acciones -----------------
1 - Forzar cerradura. (Costo: -20 energía, -2 tiempo)
2 - Hackear panel. (Costo: -10 energía, -3 tiempo)
3 - Descansar. (Costo: +15 energía(máximo 100), -1 tiempo; Si la alarma está encendida: -10 energía extra)
----------------------------------------------------''')
    while True:
        menu_action = input('Elija una opción del menú: ').strip()
        if not menu_action.isdigit():
            print('Error: Para elegir una opción, escriba el número entero asociado.')
        elif not ( 1 <= int(menu_action) <= 3):
            print('Error: Opción fuera de rango.')
        else:
            menu_action_int = int(menu_action)
            break

    match menu_action_int:
        case 1: # Forzar cerradura
            print('\n[1] Forzando cerradura...')
            energy -= 20
            time -= 2
            force_lock_count += 1
            print('[-] Se ha usado 20 unidades de energía y 2 unidades de tiempo.')
        
            if force_lock_count >= 3: # Regla anti-spam
                alarm = True
                print('[!] ALERTA: La cerradura trabada, alarma activada.')
            elif energy < 40: # Riesgo de alarma
                while True:
                    get_number = input('Ingrese un número entero del 1 al 3: ').strip()
                    if not get_number.isdigit():
                        print('Error: Se debe ingresar un número entero.')
                    elif not (1 <= int(get_number) <= 3): 
                        print('Error: Número fuera de rango.')
                    else:
                        break
                if int(get_number) == 3:
                        alarm = True
                        print('[!] ALERTA: Se activó la alarma.')

            if alarm == False:
                    open_locks += 1
                    print('[✓] Se abrió 1 cerradura.')
            else:
                print('[!] La alarma está encendida, no se puede abrir la cerradura.')

        case 2: # Hackear panel
            print('\n[2] Hackeando panel. Generando fragmentos...')
            energy -= 10
            time -= 3
            force_lock_count = 0
            print('[-] Se ha usado 10 unidades de energía y 3 unidades de tiempo.')

            for i in range(1, 5):
                partial_code += '0'
                print(f'Paso {i}/4: Generando código parcial: {partial_code}...')
            print(f'[✓] Hackeo completado. Código parcial generado: {partial_code}')

            if len(partial_code) >= 8:
                open_locks += 1
                partial_code = '' # Reseteo del código parcial para evitar un abuso del hackeo.
                print('[✓] El código generado logró abrir 1 cerradura.')
                print('[-] El código parcial se reinició.')

        case 3: # Descansar
            # Para evitar que la energía recuperada supere el máximo de energía, se utiliza la variable more_energy.
            print('\n[3] Descansando...')
            if alarm == True:
                more_energy = -10
            elif energy < 85: 
                more_energy = 15
            else:
                more_energy = 100 - energy
            energy += more_energy
            time -= 1
            force_lock_count = 0
            print(f'[-] Se ha recuperado {more_energy} unidades de energía y se ha usado 1 unidad de tiempo.')

    if alarm == True and time <= 3 and open_locks < 3: # Regla de bloqueo por alarma
            alarm_lockout = True
            print('\n[!] ALERTA: Sistema bloqueado.')

# Resultados del juego
if open_locks == 3:
    print('\n[✓] VICTORIA')
elif alarm_lockout == True:
    print('\n[X] DERROTA POR SISTEMA BLOQUEADO')
elif energy <= 0 or time <= 0:
    print('\n[X] DERROTA')
print(f'''Resultados del agente {agent}:
- Energía: {energy}
- Tiempo: {time}
- Cerraduras abiertas: {open_locks}
- Código parcial: {partial_code}
- Estado de la alarma: {alarm}
''')
