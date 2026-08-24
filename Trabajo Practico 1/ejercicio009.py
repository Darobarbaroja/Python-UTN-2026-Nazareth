"""
Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. 
Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores 
(que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.

Como pensarlo:

Pedir al usuario que ingrese un valor para la variable num1.

Pedir al usuario que ingrese un valor para la variable num2.

Mostrar por pantalla el valor de las variables num1 y num2.

Intercambiar los valores de las variables num1 y num2.

Mostrar por pantalla el valor de las variables num1 y num2.

Otra forma de resolverlo:
a=10
b=20
print(a,b)
a = a + b;
b = a - b;
a = a - b;
print(a,b)

"""

a = 10
print("Mostrar numero 1: ",a)
b = 20
print("Mostrar numero 2: ",b)
a= a + b
print("a + b = ",a)
b= a - b 
print("a - b = ",b)
a= a - b
print("a - b = ",a)
print("Mostrar numero 1 y 2 invertido los valores: ",a,",",b)
