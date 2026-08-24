
# Ejercicio 27:
"""Escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
un género ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), 
informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, 
sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, 
si la persona está en edad de jubilarse."""

edad = int(input("Ingrese edad: "))
genero = input("Ingrese género (F/M): ").upper()
nombre = input("Ingrese nombre: ")

if edad < 1 or edad > 120 or (genero != "F" and genero != "M"):
    print("Datos incorrectos para", nombre)
else:
    if (genero == "F" and edad >= 60) or (genero == "M" and edad >= 65):
        print(nombre, "está en edad de jubilarse")
    else:
        print(nombre, "no está en edad de jubilarse")