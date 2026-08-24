#Ejercicio 30:
#Escribir un programa que permita al usuario ingresar dos números enteros. 
# La computadora debe indicar si el mayor es divisible por el menor.
#(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)


num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

mayor = max(num1, num2)
menor = min(num1, num2)

if mayor % menor == 0:
    print("Es divisible")
else:
    print("No es divisible")