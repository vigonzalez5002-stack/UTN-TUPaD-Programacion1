'''
Actividad 9
Programa que permita consultar qué actividad hay en cierto día y hora de una ajenda de eventos.
'''
from paquete_validaciones.funciones_validaciones import ingresar_texto, ingresar_hora

# Ajenda predefinida
planner = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '15:00'): 'Clase de inglés'
}

# Lista de días de la semana para mayor flexibilidad.
week = ['lunes', 'martes', 'miércoles', 'jueves', 'sábado', 'domingo']

# --------------------------------------------------------------
# Este código consulta la actividad que hay en cierto día y hora
# y lo imprime en la terminal.
# --------------------------------------------------------------

day = ingresar_texto('Ingrese el día a consultar: ', week)
hour = ingresar_hora()

if (day, hour) in planner:
    print(f'\nEl día {day} a las {hour} hay un evento.')
    print(f'Evento: {planner[(day, hour)]}')
    
else:
    print(f'\nNo hay ningún evento agendado para el {day} a las {hour}')