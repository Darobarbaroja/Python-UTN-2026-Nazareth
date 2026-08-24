"""Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, 
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. 
Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?"""
#sueldo = salario_base + (cantidad_ventas * comision_fija) + (0.05 * total_ventas)

# Datos fijos (los define la empresa)
salario_base = 500000
comision_por_venta = 20000

# Datos del usuario
nombre = input("Nombre del vendedor: ")
cantidad_ventas = int(input("Cantidad de ventas: "))
total_ventas = float(input("Valor total de ventas: "))

# Cálculo del sueldo
sueldo = salario_base + (cantidad_ventas * comision_por_venta) + (0.05 * total_ventas)

# Resultado
print(f"El vendedor {nombre} tiene un salario de: ${sueldo}")