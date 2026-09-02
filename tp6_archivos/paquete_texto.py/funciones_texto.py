# ------------------------------------------------------------
# Este archivo contiene funciones que imprimen en la terminal.
# ------------------------------------------------------------

def show_data(dictionary):
    '''
    Imprime los datos de un diccionario de productos con formato.
    '''

    print(f'Producto: {dictionary['nombre']} | Precio: ${dictionary['precio']:.1f} | Cantidad: {dictionary['cantidad']}')