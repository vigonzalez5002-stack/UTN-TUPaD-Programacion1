'''
Ejercicio 5 --- Escape Room: La Arena del Gladiador
Programa que simula un Escape Room:
El Escape Room es un simulador de batalla por turnos donde un gladiador(El usuario) se enfrenta al programa(Enemigo).
El objetivo es reducir la vida del enemigo a 0 antes que él lo haga contigo.
Las posibles acciones que puede elegir el gladiador son: Ataque pesado, ráfaga veloz, usar poción de salud.
El daño del gladiador varía según el ataque que realice. Además, el ataque pesado asegura un golpe crítico cuando
la vida del enemigo es menor a 20.
'''
# Estadísticas predefinidas.
gladiator_hp = 100
enemy_hp = 100
health_potion = 3
gladiator_base_attack = 15
enemy_base_attack = 12
is_gladiator_turn = True

print('----- BIENVENID@ A LA ARENA -----')
while True:
    gladiator = input('Ingrese el nombre del Gladiador: ').strip()
    if not gladiator.isalpha():
        print('Error: Solo se permiten letras. ')
    else:
        break

while gladiator_hp > 0 and enemy_hp > 0:
    # Turno del Gladiador
    if is_gladiator_turn == True:
        print(f'''
---------------- ESTADO ACTUAL DEL COMBATE ----------------
{gladiator} (HP: {gladiator_hp}) vs Enemigo (HP: {enemy_hp})
- Elige una acción:
1. Ataque Pesado
2. Ráfaga Veloz
3. Usar Poción de Salud ({health_potion} pociones disponibles)
-----------------------------------------------------------
>>> Turno del jugador:''')
        while True:
            action = input('Acción: ').strip()
            if not action.isdigit():
                print('Error: La acción debe ser un número entero.')
            elif not (1 <= int(action) <= 3):
                print('Error: Acción fuera de rango.')
            else:
                action_int = int(action)
                break
        
        match action_int:
            case 1: # Ataque Pesado
                print('\n>> ¡Realizas un ataque pesado!')
                damage = gladiator_base_attack
                if enemy_hp < 20:
                    damage = gladiator_base_attack * 1.5
                enemy_hp -= damage
                is_gladiator_turn = False
                print(f'> ¡Acestaste {damage} puntos de daño al enemigo!')
                
            case 2: # Ráfaga Veloz
                print('\n>> ¡Inicias una ráfaga de golpes veloz!')
                for i in range(3):
                    enemy_hp -= 5
                    print(f'> Golpe de Ráfaga Veloz {i}: ¡Acestaste 5 puntos de daño al enemigo!')
                is_gladiator_turn = False
            
            case 3: # Usar Poción
                if health_potion > 0: # Si hay pociones
                    print('\n>> ¡Intentas recuperar vida con una poción!')
                    health_restored = 0
                    if gladiator_hp < 70:
                        health_restored = 30
                        gladiator_hp += health_restored
                        health_potion -= 1
                        print('> ¡Has recuperado 30 puntos de vida!')
                    elif gladiator_hp < 100:
                        health_restored = 100 - gladiator_hp # Limitador para que la curación no supere la vida máxima.
                        gladiator_hp += health_restored
                        health_potion -= 1
                        print(f'> ¡Has recuperado {health_restored} puntos de vida!')
                    else:
                        print('> ¡Tienes la vida completa! No gastarás una poción por esto.')
                
                else: # Si no hay pociones
                    print('\n>> ¡No quedan pociones! Pierdes tu turno.')
                    is_gladiator_turn = False

    # Turno del Enemigo
    else: 
        print('\n>>> Turno del enemigo:')
        gladiator_hp -= 12
        is_gladiator_turn = True
        print('> ¡El enemigo te quitó 12 puntos de vida!')

if gladiator_hp > 0:
    print(f'\n¡VICTORIA! El gladiador {gladiator} ha ganado la batalla.')
else:
    print(f'\n¡DERROTA! El gladiador {gladiator} ha caído en combate.')
    