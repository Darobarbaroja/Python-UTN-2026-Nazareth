# Sistema básico de gestión de productos

# Lista donde se guardarán los productos
# Cada producto será: [nombre, categoria, precio]
productos = []

# Variable para controlar el programa
ejecutando = True

while ejecutando:

    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # =========================
    # OPCIÓN 1: AGREGAR PRODUCTO
    # =========================
    if opcion == "1":

        # Validar nombre
        while True:
            nombre = input("Ingrese el nombre del producto: ").strip()

            if nombre != "":
                break
            else:
                print("Error: el nombre no puede estar vacío.")

        # Validar categoría
        while True:
            categoria = input("Ingrese la categoría del producto: ").strip()

            if categoria != "":
                break
            else:
                print("Error: la categoría no puede estar vacía.")

        # Validar precio
        while True:
            precio = input("Ingrese el precio del producto (sin centavos): ")

            if precio.isdigit():
                precio = int(precio)
                break
            else:
                print("Error: debe ingresar un número entero válido.")

        # Guardar producto en la lista
        producto = [nombre, categoria, precio]
        productos.append(producto)

        print("Producto agregado correctamente.")

    # =========================
    # OPCIÓN 2: MOSTRAR PRODUCTOS
    # =========================
    elif opcion == "2":

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\n===== LISTA DE PRODUCTOS =====")

            for i in range(len(productos)):
                print(
                    f"{i + 1}. "
                    f"Nombre: {productos[i][0]} | "
                    f"Categoría: {productos[i][1]} | "
                    f"Precio: ${productos[i][2]}"
                )

    # =========================
    # OPCIÓN 3: BUSCAR PRODUCTO
    # =========================
    elif opcion == "3":

        buscar = input("Ingrese el nombre del producto a buscar: ").strip()

        encontrado = False

        for producto in productos:

            # Comparación sin importar mayúsculas/minúsculas
            if buscar.lower() in producto[0].lower():

                print("\nProducto encontrado:")
                print(f"Nombre: {producto[0]}")
                print(f"Categoría: {producto[1]}")
                print(f"Precio: ${producto[2]}")

                encontrado = True

        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    # =========================
    # OPCIÓN 4: ELIMINAR PRODUCTO
    # =========================
    elif opcion == "4":

        if len(productos) == 0:
            print("No hay productos para eliminar.")

        else:
            print("\n===== PRODUCTOS REGISTRADOS =====")

            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i][0]}")

            posicion = input("Ingrese el número del producto a eliminar: ")

            if posicion.isdigit():

                posicion = int(posicion)

                # Validar rango
                if 1 <= posicion <= len(productos):

                    eliminado = productos.pop(posicion - 1)

                    print(f"Producto '{eliminado[0]}' eliminado correctamente.")

                else:
                    print("Error: número fuera de rango.")

            else:
                print("Error: debe ingresar un número válido.")

    # =========================
    # OPCIÓN 5: SALIR
    # =========================
    elif opcion == "5":

        print("Saliendo del sistema...")
        ejecutando = False

    # =========================
    # OPCIÓN INVÁLIDA
    # =========================
    else:
        print("Opción inválida. Intente nuevamente.")