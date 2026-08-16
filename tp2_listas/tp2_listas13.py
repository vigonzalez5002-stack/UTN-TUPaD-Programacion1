'''
Actividad 13
Programa que, a partir de una lista de puntajes, muestra el puntaje más alto y el más bajo;
la lista ordenada de mayor a menor(ranking) y en que posición del ranking se encuentra el
puntaje 990.
'''
# Lista de puntajes
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Lista Ranking
ranking = sorted(puntajes, reverse=True)

# Esto muestra el puntaje más alto y más bajo
print(f'El puntaje más alto es {max(puntajes)}.')
print(f'El puntaje más bajo es {min(puntajes)}.')

# Esto muestra la lista ordenada
print('Ranking: ', end='')
for i in range(len(ranking)):
    print(ranking[i], end='')
    if i != len(ranking) - 1:
        print(', ', end='')

# Esto indica la posición del puntaje 990 en el ranking
puntaje_index = ranking.index(990)
print(f'\nEl puntaje 990 se encuentra la posición {puntaje_index + 1} del ranking.')