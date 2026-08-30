'''
Actividad 4
Programa que almacena números telefónicos a un registro y busca el el número
dentro del registro.
'''

# Se hará uso de un paquete para la validación de datos y así evitar repetir código
from paquete_validaciones.funciones_validaciones import ingresar_numero, ingresar_texto

# ---------------------------------------------------------------------------------
# El siguiente código almacenta a un diciconario 5 números de contacto.
# Los pares clave-valor corresponden al nombre del contacto y el número de teléfono
# de los contactos respectivamente.
# ---------------------------------------------------------------------------------

contact_dictionary = {}
for i in range(1, 6):
    print(f'\nIngrese el contacto Nº{i}')
    name = ingresar_texto('Ingresa el nombre del contacto: ', list(contact_dictionary.keys()), not_text_valid = True)
    phone_number = ingresar_numero()
    contact_dictionary[name] = phone_number 
print()

# --------------------------------------------------------------------------------
# El siguiente código busca el número de contacto dentro del diccionario a partir
# del nombre de contacto. Para eseto se usa un bucle de validación para asegurarse
# de que el contacto a ingresar se encuentre registrado en el diccionario.
# --------------------------------------------------------------------------------

contact_list = list(contact_dictionary.keys()) # Lista de los nombres de los contactos

# Esto valida el nombre del contacto
contact = ingresar_texto('Ingresa el nombre del contacto a buscar: ', contact_list)

# Esto imprime el número de contacto correspondiente
print(f'\nEl número de teléfono de {contact} es {contact_dictionary.get(contact)}')