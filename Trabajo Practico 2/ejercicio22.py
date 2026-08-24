

# <<<Ejercicio 22:>>>
# <<<Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.>>>





num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))

mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print("El mayor es:", mayor)