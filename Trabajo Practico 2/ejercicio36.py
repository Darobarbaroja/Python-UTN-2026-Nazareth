
#<<<Ejercicio 36:>>>
#Escribir un programa que permita ingresar dos números enteros y 
# la operación a realizar ('+', '-', '*', '/'). 
# Debe mostrarse el resultado para la operación ingresada. 
# Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
op = input("Ingrese operación (+, -, *, /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("ERROR")
    else:
        print(num1 / num2)
else:
    print("Operación inválida")