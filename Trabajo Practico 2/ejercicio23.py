
# <<<Ejercicio 23:>>>
# <<<Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y el valor que está en medio.>>>
# <<<Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 5 como el menor, el número 7 como el mayor y el número 3 como el que esta en medio.>>>
# <<<Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?>>






num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

lista = [num1, num2, num3]
lista.sort()

print("Menor:", lista[0])
print("Medio:", lista[1])
print("Mayor:", lista[2])
