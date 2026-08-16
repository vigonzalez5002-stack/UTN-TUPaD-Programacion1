'''
Actividad 9
Programa que, a partir de una matriz que simula un tablero de Ta-Te-Ti,
permite que dos jugadores ingresen posiciones(fila, columna) para colocar
"X" o "O".
NOTA: Si bien la actividad no pide que simule el juego en sí, sino que
simula el tablero y cómo se colocan "X" y "O", decidí realizar el sistema
de victoria para hacer la actividad más completa. Además, se omitirán las
validaciones, excepto de si la posición ya está ocupada o no.
'''
# Matriz 3x3 que simula el tablero
tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Turno inicial
turno_jugador1 = True

# Simulación
while True:
    # Esto imprime en pantalla el tablero
    for i in range(3):
        print(end=' ')
        for j in range(3):
            if j != 2:
                print(tablero[i][j], end=' | ')
            else:
                print(tablero[i][j])
        if i != 2:
            print('---+---+---')

# Lista de posiciones ganadoras
    posiciones_ganadoras = [
    [tablero[0][0], tablero[0][1], tablero[0][2]], # Combinación fila 1
    [tablero[1][0], tablero[1][1], tablero[1][2]], # Combinación fila 2
    [tablero[2][0], tablero[2][1], tablero[2][2]], # Combinación fila 3
    [tablero[0][0], tablero[1][0], tablero[2][0]], # Combinación columna 1
    [tablero[0][1], tablero[1][1], tablero[2][1]], # Combinación columna 2
    [tablero[0][2], tablero[1][2], tablero[2][2]], # Combinación columna 3
    [tablero[0][0], tablero[1][1], tablero[2][2]], # Combinación diagonal hacia abajo a la derecha
    [tablero[0][2], tablero[1][1], tablero[2][0]] # Combinación diagonal hacia abajo a la izquierda
]

    # Condición para terminar el programa
    if ['X', 'X', 'X'] in posiciones_ganadoras:
        print('\n>> El jugador 1 ganó el juego.')
        break
    elif ['O', 'O', 'O'] in posiciones_ganadoras:
        print('\n>> El jugador 2 ganó el juego.')
        break
    elif '-' not in tablero[0] and '-' not in tablero[1] and '-' not in tablero[2]:
        print('\n>> Ya no se puede colocar ningún otro símbolo en el tablero.(Empate)')
        break

    # Esto reinicia los bucles para colocar los símbolos
    X_colocado = False
    O_colocado = False

    if turno_jugador1 == True: # Turno del jugador 1
        while X_colocado == False:
            print('\n>> Turno del jugador 1, su símbolo es la X')
            fila = int(input('Ingrese la fila(1-3): ').strip()) - 1
            columna = int(input('Ingrese la columna(1-3): ').strip()) - 1
            if tablero[fila][columna] == '-':
                tablero[fila][columna] = 'X'
                X_colocado = True
                turno_jugador1 = False
            else:
                print('Esa posición ya está usada. Inténtalo de nuevo.')

    else: # Turno del jugador 2
        while O_colocado == False:
            print('\n>> Turno del jugador 2, su símbolo es la O')
            fila = int(input('Ingrese la fila(1-3): ').strip()) - 1
            columna = int(input('Ingrese la columna(1-3): ').strip()) - 1
            if tablero[fila][columna] == '-':
                tablero[fila][columna] = 'O'
                O_colocado = True
                turno_jugador1 = True
            else:
                print('Esa posición ya está usada. Inténtalo de nuevo.')
