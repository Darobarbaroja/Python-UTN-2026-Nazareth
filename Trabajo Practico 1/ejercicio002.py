
# Ejercicio 4

enunciado ="""Realiza un programa que permita ingresar 3 notas pertenecientes
a tres trimestres distintos para cierto alumno de nivel secundario.
Debe calcularse y mostrarse la nota promedio.

leer 3 numeros 
leer 1 numero
leer 1 numero
leer 1 numero
calcular promedio
mostrar resultado

"""
#print(enunciado)
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

promedio = (n1 + n2 + n3) / 3
print("Notas:",n1,n2,n3,"Promedio: ",promedio)
# Ahora con números decimales
n4 = float(input("Numero 4: "))
n5 = float(input("Numero 5: "))
n6 = float(input("Numero 6: "))

promediofloat = ( n4 + n5 + n6)/3
print("Notas:",n4,n5,n6,"Promedio: ",promediofloat)


print("Notas:","[",n1,n2,n3,"]==> ", "Promedio: ",promedio)

# Utilizando formato de cadena
cadena_formato = f"Notas: <[{n1},{n2},{n3}]==> Promedio: {promedio:.2}" 
print(cadena_formato)
