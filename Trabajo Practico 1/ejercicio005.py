"""
Escribir un programa que solicite al usuario ingresar dos notas de un alumno. 
El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: 
"Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".

Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: 
"Notas: 7 , 8 ==> promedio: 7.5".

"""
nota1 = float(input("La nota es :"))
nota2 = float(input("La nota es :"))


prom_notas = (nota1 + nota2)/2

# Usás comas (,) para separar elementos.Python automáticamente agrega espacios entre cada cosa.Todo lo que está entre comillas 
# "..." se muestra literalmente,
#  o sea: "Notas: [",nota1,"]","[",nota2,"]==> ", "Promedio:  [(nota1+nota2)/2] =  " se muestra tal cual, y luego se muestran los valores de nota1, nota2 y prom_notas
print("Notas:","[",nota1,"]","[",nota2,"]==> ", "Promedio:  [(nota1+nota2)/2] = ", prom_notas)

# Solicitar las dos notas al usuario
not1 = float(input("Ingresá la primera nota: "))
not2 = float(input("Ingresá la segunda nota: "))

# Calcular el promedio
promedio = (not1 + not2) / 2

# Mostrar el resultado
# f-string permite mostrar todo con el formato exacto que pide el ejercicio.
# Las llaves {} permiten insertar variables y operaciones reales.
print(f"Notas: {not1} , {not2} ==> promedio: {promedio}")

#Dentro de {} podés poner:

#variables
#operaciones
#funciones
#"texto" → Python no piensa, solo muestra
#f"texto {algo}" → Python piensa y reemplaza {algo}
