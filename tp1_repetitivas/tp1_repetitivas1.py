''' 
Ejercicio 1 --- Caja del Kiosco
Programa que simula una compra. 
El programa recibe el nombre del cliente(name), cantidad de productos a comprar(number_items), el precio de cada producto(price)
y si tiene descuento(discount) o no. Se valida cada una de estas variables de ingreso.
El programa muestra en consola el total con y sin descuentos, el ahorro total y el promedio por producto.
'''

# Ingreso del nombre del cliente y validación(No vacío y solo letras).
while True:
    name = input('Ingrese el nombre del cliente: ').capitalize().strip()
    if len(name) == 0:
        print('No se ha ingresado el nombre del cliente. Inténtelo de nuevo.')
    elif not name.isalpha():
        print(f'{name} tiene un carácter inválido. Ingrese un nombre solo con letras.')
    else:
        break

# Ingreso de la cantidad de productos a comprar y validación(No vacío, no negativo, solo dígitos, no debe ser 0).
while True:
    number_items = input('\nIngrese la cantidad de productos: ').strip()
    if len(number_items) == 0:
        print('No se ha ingresado la cantidad de productos. Inténtelo de nuevo.')
    elif not number_items.isdigit():
        print(f'{number_items} tiene un carácter inválido. La cantidad debe ser entera positiva.')
    elif int(number_items) == 0:
        print('La cantidad no puede ser 0. Inténtelo de nuevo.')
    else:
        number_items_int = int(number_items)
        break

# Bucle de ingreso del precio de cada producto y procesamiento de datos.
total = 0
total_discount = 0
for amount in range(1, number_items_int + 1):

    # Ingreso y validación del precio de cada producto.
    while True:
        price = input(f'\nIngrese el precio del producto Nº{amount}: ').strip()
        if len(price) == 0:
            print('No se ha ingresado un precio. Inténtelo de nuevo.')
        elif not price.isdigit():
            print(f'{price} no es válido. El precio debe ser un número entero positivo.')
        else:
            price_int = int(price)
            break

    # Ingreso del descuento y validación.
    apply_discount = 0 # Descuento por defecto.
    while True:
        discount = input('Indique si tiene descuento(S/N): ').upper().strip()
        if discount == 'S':
            apply_discount = 0.1 # Descuento del 10%.
            break
        elif discount == 'N':
            break
        else:
            print(f'{discount} no es válido. Sólo se admite S(Sí) o N(No).')

    # Procesamiento de datos.
    total += price_int
    total_discount += price_int - price_int*apply_discount
saving = total - total_discount
average = total_discount / number_items_int

# Salida.
print(f'''
Cliente: {name}
Cantidad de productos: {number_items_int}
Total sin descuentos: ${total}
Total con descuentos: ${total_discount:.2f}
Ahorro: ${saving:.2f}
Promedio por producto: ${average:.2f}
''')
