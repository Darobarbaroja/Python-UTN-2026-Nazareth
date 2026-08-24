#Ejericio 13: Cálculo de sueldo de un vendedor
"""
Escribir un programa para calcular el importe a cobrar por un vendedor, 
considerando su sueldo fijo de $200000 pesos más el 16% del monto total de ventas realizadas durante un mes.

Pensando los pasos para resolver el problema:
Solicitar al usuario que ingrese el monto total de ventas realizadas por el vendedor durante el mes en una variable correspondiente.

Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.

Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

Mostrar el importe a cobrar por el vendedor.

Para pensar:
¿Qué pasaría si se modificara el sueldo fijo del vendedor?

Si se modifica el sueldo fijo del vendedor, entonces la fórmula utilizada para calcular 
el salario total debería ser actualizada para reflejar el nuevo sueldo fijo.

En este caso, si el sueldo fijo aumenta, entonces el salario total también aumentaría.
De igual manera, si el sueldo fijo disminuye, entonces el salario total también disminuiría.
Es importante actualizar la fórmula en el programa para asegurarse de que el cálculo 
del salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.

¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono?

"""
sueldo_fijo = float(input("Ingresá el sueldo fijo: "))
ventas = float(input("Ingresá el total de ventas: "))

sueldo_total = sueldo_fijo + (ventas * 0.16)

print(f"Sueldo a cobrar: ${sueldo_total}")