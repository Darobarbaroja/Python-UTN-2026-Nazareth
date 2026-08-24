
# <<<Ejercicio 21:>>>
""" Escribir un programa que permita ingresar dos números enteros 
e indicar si el primero es mayor, menor o igual al segundo."""


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primero es mayor")
elif num1 < num2:
    print("El primero es menor")
else:
    print("Son iguales")