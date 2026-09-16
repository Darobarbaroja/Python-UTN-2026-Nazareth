

# Funciones del sistema de inventario

from base_datos import conexion, cursor
from colorama import Fore
# ------------------------------------------
# Registrar un nuevo producto
# ------------------------------------------
def registrar_producto():

    print("\n=== Registrar Producto ===")

    # Validación del nombre
    while True:
        nombre = input("Nombre: ").strip()
        if nombre != "":
            break
        print("El nombre no puede estar vacío.")

    descripcion = input("Descripción: ").strip()

    # Validación de cantidad
    while True:
        cantidad = input("Cantidad: ")

        if cantidad.isdigit():
            cantidad = int(cantidad)
            break

        print("Ingrese una cantidad válida.")

    # Validación del precio
    while True:
        precio = input("Precio: ")

        try:
            precio = float(precio)
            break
        except ValueError:
            print("Ingrese un precio válido.")

    categoria = input("Categoría: ").strip()

    cursor.execute("""
        INSERT INTO productos(nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()

    print(Fore.GREEN + "Producto registrado correctamente.")


# ------------------------------------------
# Mostrar todos los productos
# ------------------------------------------
def mostrar_productos():

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if len(productos) == 0:
        print("\nNo hay productos registrados.")
        return

    print("\n===== PRODUCTOS =====")

    for producto in productos:
        print("----------------------------------")
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: ${producto[4]}")
        print(f"Categoría: {producto[5]}")


# ------------------------------------------
# Buscar producto por ID
# ------------------------------------------
def buscar_producto():

    id_producto = input("Ingrese el ID del producto: ")

    if not id_producto.isdigit():
        print("ID inválido.")
        return

    cursor.execute(
        "SELECT * FROM productos WHERE id=?",
        (int(id_producto),)
    )

    producto = cursor.fetchone()

    if producto:

        print("\nProducto encontrado")
        print("---------------------")
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: ${producto[4]}")
        print(f"Categoría: {producto[5]}")

    else:
        print("No existe un producto con ese ID.")


# ------------------------------------------
# Actualizar producto
# ------------------------------------------
def actualizar_producto():

    id_producto = input("Ingrese el ID del producto: ")

    if not id_producto.isdigit():
        print("ID inválido.")
        return

    id_producto = int(id_producto)

    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        print("No existe un producto con ese ID.")
        return

    print("\nIngrese los nuevos datos")

    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    cursor.execute("""
        UPDATE productos
        SET nombre=?,
            descripcion=?,
            cantidad=?,
            precio=?,
            categoria=?
        WHERE id=?
    """, (nombre, descripcion, cantidad, precio, categoria, id_producto))

    conexion.commit()

    print("Producto actualizado correctamente.")


# ------------------------------------------
# Eliminar producto
# ------------------------------------------
def eliminar_producto():

    id_producto = input("Ingrese el ID del producto a eliminar: ")

    if not id_producto.isdigit():
        print("ID inválido.")
        return

    id_producto = int(id_producto)

    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        print("No existe un producto con ese ID.")
        return

    cursor.execute("DELETE FROM productos WHERE id=?", (id_producto,))
    conexion.commit()

    print(Fore.RED +"Producto eliminado correctamente.")


# ------------------------------------------
# Reporte de stock bajo
# ------------------------------------------
def reporte_stock():

    limite = input("Mostrar productos con cantidad menor o igual a: ")

    if not limite.isdigit():
        print("Ingrese un número válido.")
        return

    limite = int(limite)

    cursor.execute("""
        SELECT * FROM productos
        WHERE cantidad <= ?
    """, (limite,))

    productos = cursor.fetchall()

    if len(productos) == 0:
        print("No hay productos con stock bajo.")
        return

    print("\n===== REPORTE DE STOCK =====")

    for producto in productos:
        print("----------------------------------")
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: ${producto[4]}")


# ------------------------------------------
# Cerrar conexión con la base de datos
# ------------------------------------------
def cerrar_conexion():
    conexion.close()

