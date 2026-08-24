"""
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:

a. Multiplicado por 10. (utilizar el operador *) 
a. Dividido por 10. (utilizar el operador /) 
a. Elevado al cuadrado. (utilizar el operador **)

Cada resultado debe mostrarse en una línea distinta.

Ejemplo de ejecución:

Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25

"""

n1= int(input("ingrese un numero entero: "))

mult=n1 * 10
print("Multiplicado por 10 = ", mult)
div = n1/10
print("Dividido por 10 = ", div)
elev=n1**2
print("elevado al cuadrado = ", elev)