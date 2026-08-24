
#Ejercicio 34:
#Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y 
# su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad,
#  mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. 
# También se le realizan los siguientes descuentos:
#•	Jubilación: 11%
#•	Obra Social: 3%
#•	Sindicato: 3%
#Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
#Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años
#Descuentos:
#•	Jubilación - 999,99
#•	Obra Social - 999,99
#•	Sindicato - 999,99
#Sueldo Neto 999,99

sueldo_basico = float(input("Ingrese sueldo básico: "))
antiguedad = int(input("Ingrese antigüedad: "))
estado = input("Estado civil (S/C): ").upper()

if estado == "S":
    adicional = sueldo_basico * 0.05 * antiguedad
else:
    adicional = sueldo_basico * 0.07 * antiguedad

sueldo_bruto = sueldo_basico + adicional

jubilacion = sueldo_bruto * 0.11
obra_social = sueldo_bruto * 0.03
sindicato = sueldo_bruto * 0.03

sueldo_neto = sueldo_bruto - jubilacion - obra_social - sindicato

print("Jubilación:", jubilacion)
print("Obra Social:", obra_social)
print("Sindicato:", sindicato)
print("Sueldo Neto:", sueldo_neto)