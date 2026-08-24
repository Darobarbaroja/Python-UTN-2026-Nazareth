
#Ejercicio 33:
#La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:
#•	Menor de $5500.0 el descuento es del 4.5%
#•	Entre $5500.0 y $10000.0 el descuento es del 8%
#•	Más de $10000.0 el descuento es del 10.5%
#Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.

importe = float(input("Ingrese importe de compra: "))

if importe < 5500:
    descuento = importe * 0.045
elif importe <= 10000:
    descuento = importe * 0.08
else:
    descuento = importe * 0.105

neto = importe - descuento

print("Descuento: $", descuento)
print("Precio final: $", neto)
