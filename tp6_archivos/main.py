# -----------------------------------------------------------------------
# Este es el archivo principal donde se ejecutarán todas las actividades.
# -----------------------------------------------------------------------
import paquete_principal.funciones_principales as fp
import paquete_validaciones.funciones_validaciones as fv

while True:
    print('''
==========================================
 - - - - - - Menú de opciones - - - - - -
==========================================
1. Cargar los productos para gestionarlos.
2. Mostrar productos.
3. Agregar un producto a la lista.
4. Buscar producto por nombre.
5. Guardar cambios.
6. Salir del programa.
==========================================''')
    menu_option = fv.enter_number('Opción: ', 1, 6, True, True, True)

    try:
        match menu_option:

            case 1: # Carga los productos en una lista de diccionarios
                products_list = fp.load_products()

            case 2: # Muestra los productos
                fp.show_products(products_list)

            case 3: # Agrega un producto
                while True:
                    fp.add_product(products_list)
                    
                    print('\n¿Deseas añadir otro producto?')
                    add_option = fv.enter_word('S para sí, N para no: ', ['s', 'n'])
                    if add_option == 'n':
                        print('\n>> Volviendo al menú de opciones.')
                        break

            case 4: # Busca un producto por nombre
                fp.find_product(products_list)

            case 5:
                fp.save_products(products_list)

            case 6:
                print('\n>> Saliendo del programa...')
                break

    except NameError:
        print('[X] Error: No se cargaron los productos.')
        print('> Primero carga los productos.')
    