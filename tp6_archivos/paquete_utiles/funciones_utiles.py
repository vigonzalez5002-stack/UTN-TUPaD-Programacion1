# -----------------------------------------------------------------------------------------
# Este módulo contiene funciones que servirán de asistencia para las funciones principales.
# -----------------------------------------------------------------------------------------

def show_data(product):
    '''
    Esta función muestra los datos de un diccionario de datos de un producto y lo muestra
    con el siguiente formato:

    Producto: <nombre> | Precio: $<precio> | Cantidad: <cantidad>
    '''

    print(f'Producto: {product['nombre'].capitalize()} | Precio: ${float(product['precio']):.1f} | Cantidad: {product['cantidad']}')