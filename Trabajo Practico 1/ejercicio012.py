"""
Escribir un programa en Python que solicite al usuario ingresar dos valores 
que representen las medidas en grados de dos ángulos interiores de un triángulo. 
Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.

Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. 
Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados.
 Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."

Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?
¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?

"""
# Solicitar al usuario ingresar dos ángulos interiores de un triángulo
# Codigo Simple
angulo1 = float(input("Ingresá el primer ángulo: "))
angulo2 = float(input("Ingresá el segundo ángulo: "))

angulo_restante = 180 - (angulo1 + angulo2)

print(f"El ángulo restante es: {angulo_restante}°")
angulo1 = float(input("Ingresá el primer ángulo: "))
angulo2 = float(input("Ingresá el segundo ángulo: "))


#Version Mejorada
# Validar que los ángulos ingresados sean positivos y que la suma de los ángulos no sea mayor o igual a 180 grados
if angulo1 <= 0 or angulo2 <= 0:
    print("Error: los ángulos deben ser positivos")
elif angulo1 + angulo2 >= 180:
    print("Error: la suma de los ángulos debe ser menor a 180")
else:
    angulo_restante = 180 - (angulo1 + angulo2)
    print(f"El ángulo restante es: {angulo_restante}°")