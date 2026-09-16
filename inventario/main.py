# Importar las funciones del archivo funciones.py
from funciones import *
from colorama import init, Fore

# Inicializar Colorama
init(autoreset=True)

# Variable para mantener el menú en ejecución
ejecutando = True

while ejecutando:

    print(Fore.CYAN +"\n===================================")
    print(Fore.RED +"     SISTEMA DE INVENTARIO")
    print(Fore.CYAN +"===================================")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock bajo")
    print("7. Salir")
    print("===================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        actualizar_producto()

    elif opcion == "5":
        eliminar_producto()

    elif opcion == "6":
        reporte_stock()

    elif opcion == "7":
        print("\nGracias por utilizar el sistema.")
        cerrar_conexion()
        ejecutando = False

    else:
        print("\nOpción inválida. Intente nuevamente.")


