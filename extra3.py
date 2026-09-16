productos = []

# Menú principal
while True:
    print("=" * 40)
    print("Sistema básico de gestión de productos")
    print("=" * 40)
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

    opcion = int(input("Ingrese una opción: "))

    # AGREGAR PRODUCTO
    if opcion == 1:
        nombre = input("Ingrese nombre del producto: ")
        categoria = input("Ingrese categoría: ")
        precio = input("Ingrese precio: ")

        # Guardamos los datos en una lista
        productos.append([nombre, categoria, precio])

        print("Producto agregado correctamente")

    # MOSTRAR PRODUCTOS
    elif opcion == 2:

        if len(productos) == 0:
            print("No hay productos agregados")

        else:
            print("\nLISTA DE PRODUCTOS")

            for i in range(len(productos)):
                print("-" * 30)
                print("Producto", i + 1)
                print("Nombre:", productos[i][0])
                print("Categoría:", productos[i][1])
                print("Precio:", productos[i][2])

    # BUSCAR PRODUCTO
    elif opcion == 3:

        productobuscado = input("Ingrese el producto que desea buscar: ")

        encontrado = False

        for i in range(len(productos)):

            if productobuscado.lower() == productos[i][0].lower():

                print("\nProducto encontrado")
                print("Nombre:", productos[i][0])
                print("Categoría:", productos[i][1])
                print("Precio:", productos[i][2])

                encontrado = True

        if not encontrado:
            print("Producto no encontrado")

    # ELIMINAR PRODUCTO
    elif opcion == 4:

        if len(productos) == 0:
            print("No hay productos para eliminar")

        else:
            print("\nProductos disponibles:")

            for i in range(len(productos)):
                print(i + 1, "-", productos[i][0])

            productoeliminado = int(input("Ingrese el número del producto a eliminar: "))

            productoeliminado = productoeliminado - 1

            if 0 <= productoeliminado < len(productos):
                eliminado = productos.pop(productoeliminado)
                print("Producto eliminado:", eliminado[0])

            else:
                print("Número inválido")

    # SALIR
    elif opcion == 5:
        print("Gracias, vuelva pronto")
        break

    else:
        print("Opción inválida")