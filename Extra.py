# Lista donde se guardan los productos
# Cada producto tendrá: nombre, categoría y precio
productos = []

# Variable para controlar el menú
opcion = 0

# Menú principal
while opcion != 5:

    print("\n----- SISTEMA DE PRODUCTOS -----")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    # Pedimos una opción
    opcion = int(input("Ingrese una opción: "))

    # ------------------------------------------------
    # AGREGAR PRODUCTO
    # ------------------------------------------------
    if opcion == 1:

        nombre = input("Ingrese nombre del producto: ")
        categoria = input("Ingrese categoría: ")
        precio = int(input("Ingrese precio sin centavos: "))

        # Agregamos el producto a la lista
        productos.append([nombre, categoria, precio])

        print("Producto agregado correctamente")

    # ------------------------------------------------
    # MOSTRAR PRODUCTOS
    # ------------------------------------------------
    elif opcion == 2:

        # Verificamos si hay productos
        if len(productos) == 0:

            print("No hay productos cargados")

        else:

            # Ordenamos la lista
            productos.sort()

            print("\n----- LISTA DE PRODUCTOS -----")

            # Recorremos la lista con FOR
            for i in range(len(productos)):

                print("\nProducto", i + 1)
                print("Nombre:", productos[i][0])
                print("Categoría:", productos[i][1])
                print("Precio:", productos[i][2])

    # ------------------------------------------------
    # BUSCAR PRODUCTO
    # ------------------------------------------------
    elif opcion == 3:

        if len(productos) == 0:

            print("No hay productos cargados")

        else:

            buscar = input("Ingrese nombre del producto: ")

            encontrado = False

            # Recorremos la lista
            for i in range(len(productos)):

                # Comparamos el nombre ingresado
                if buscar.lower() == productos[i][0].lower():

                    print("\nProducto encontrado")
                    print("Nombre:", productos[i][0])
                    print("Categoría:", productos[i][1])
                    print("Precio:", productos[i][2])

                    encontrado = True

            # Si no encuentra coincidencias
            if encontrado == False:

                print("No se encontraron resultados")

    # ------------------------------------------------
    # ELIMINAR PRODUCTO
    # ------------------------------------------------
    elif opcion == 4:

        if len(productos) == 0:

            print("No hay productos para eliminar")

        else:

            print("\n----- PRODUCTOS DISPONIBLES -----")

            # Mostramos productos numerados
            for i in range(len(productos)):

                print(i + 1, "-", productos[i][0])

            # Pedimos número de producto
            eliminar = int(input("Ingrese número de producto a eliminar: "))

            # Convertimos al índice real
            eliminar = eliminar - 1

            # Verificamos que exista
            if eliminar >= 0 and eliminar < len(productos):

                productos.pop(eliminar)

                print("Producto eliminado correctamente")

            else:

                print("Número inválido")

    # ------------------------------------------------
    # SALIR
    # ------------------------------------------------
    elif opcion == 5:

        print("Programa finalizado")

    # ------------------------------------------------
    # OPCIÓN INCORRECTA
    # ------------------------------------------------
    else:

        print("Opción incorrecta")