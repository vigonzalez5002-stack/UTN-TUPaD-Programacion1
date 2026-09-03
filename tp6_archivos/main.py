# -----------------------------------------------------------------------
# Este es el archivo principal donde se ejecutarán todas las actividades.
# La resolución de los ejercicios combina cada uno en un único programa
# que hace lo siguiente en un menú:
# 
# - Carga los productos en una lista(4) y si no existe el archivo, 
# lo crea(1)
# - Muestra los productos(2)
# - Agrega un producto(3)
# - Busca un producto(5)
# - Guarda los cambios(6)
#
# Cuando se intenta realizar algúna de las opciones sin antes haber
# cargado los productos en una lista, el programa marcará un error.
# De esta forma, cada uno de los ejercicios dependerá de la lista de
# diccionarios cargada. Por lo que en caso de añadir un producto, se
# modifique la lista cargada y no el archivo.
# 
# Esto se hace con el objetivo de evitar que cada resolución funcione de
# forma independiente a otro, haciendo redundante alguno.
# Por ejemplo, en el ejercicio 2 se puede inferir que se debe abrir el
# archivo en modo "a", añadiendo de forma directa los cambios, pero esto 
# dejaría redundante al ejercicio 6.
# Además, de esta forma, se evita tener que abrir el archivo múltiples
# veces por actividad, accediendo a los datos a partir de los datos
# cargados.
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
    