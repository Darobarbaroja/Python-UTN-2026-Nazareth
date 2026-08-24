# Python-UTN-2026-Nazareth
PYTHON DESDE CERO - INTRODUCCIÓN A LA PROGRAMACIÓN
La programación es el proceso de crear instrucciones que una computadora puede ejecutar para resolver un problema o realizar una tarea.
Escribir un programa es como escribir una receta: paso a paso, sin ambigüedades.
¿Qué es programar?
Programar es darle instrucciones a una computadora para que haga algo. Es como una receta de cocina:
•     Paso 1 → hacer esto
•     Paso 2 → hacer aquello
•     Paso 3 → mostrar resultado
La computadora no piensa. Solo hace exactamente lo que le decimos.
Lenguaje de Programación
Un lenguaje de programación es un conjunto de reglas y palabras que permiten comunicarnos con la 
computadora.
Python es un lenguaje de programación de alto nivel:
•     De sintaxis simple y clara
•     Muy usado en educación
•     Aplicado en desarrollo web, automatización, ciencia de datos e inteligencia artiﬁcial
•     Fácil de leer
•     Potente (se usa en inteligencia artiﬁcial, ciencia de datos, automatización, desarrollo web, etc.)

Ideal para empezar Ejemplo: print("Hola mundo") Eso ya es un programa.

Algoritmo: Un algoritmo es una secuencia ordenada de pasos para resolver un problema.
Ejemplo cotidiano:
1.   Encender la computadora
2.   Abrir el navegador
3.   Buscar información
PRIMER PROGRAMA: El clásico: Hola Mundo
print("Hola mundo")                
¿Qué hace?
• print() → significa "mostrar en pantalla"
• Lo que está entre comillas es el texto que se imprime
  
VARIABLES: Una variable es un espacio en memoria donde se guarda un dato que puede cambiar durante la ejecución del programa. Una cajita donde guardamos información.
Ejemplo: edad = 15
Aquí:
•     edad es la variable
•     15 es el valor de guardado

Tipos de Datos: Son las distintas clases de valores que puede almacenar una variable.
•     Entero (int): números sin decimales
•     Decimal (ﬂoat): números con decimales
•     Texto (str): cadenas de caracteres
•     Booleano(bool): verdadero o Falso

Operadores: Son símbolos que permiten realizar operaciones Aritméticos:
| + suma 
| - resta
| * multiplicación
| / división

Comparación:
|  == igual
|  != distinto
|  >  mayor
|  <  menor
|  >= mayor o igual
|  <= menor o igual

CONDICIONALES: Una estructura condicional permite tomar decisiones según se cumpla o no una condición.
Se utiliza con:   if, elif y else. Permite que el programa elija un camino u otro, como también tomar decisiones.

BUCLES: Un bucle es una estructura que repite un bloque de código varias veces.
While: Repite mientras una condición sea verdadera.
For: Repite una cantidad determinada de veces.
Sirven para repetir acciones.

LISTAS (Colecciones de datos) ¿Qué es una lista? Una lista es una estructura que permite guardar varios datos en una sola variable.
Es como una caja con varios compatimentos.
Ejemplo:
numeros = [10, 20, 30, 40]
Aquí guardamos 4 números en una sola variable.
¿Cómo funciona internamente? Cada elemento Tiene una posición.
Posición    Valor
0            10
1            20
2            30
3            40
Importante: En Python las posiciones comienzan en 0.


FUNCIONES: ¿Qué es una función? Una función es un bloque de código que realiza una tarea específica.
Sirve para:
• Organizar mejor el programa
• Reutilizar código
• Hacer programas más profesionales
• Recibir datos (parámetros)
• Devolver resultados (return)
Parámetro: Un parámetro es un dato que se envía a una función para que lo u􀆟lice en su ejecución.
Return: La palabra return permite que una función devuelva un resultado al lugar donde fue llamada.

TUPLAS Y DICCIONARIOS: 

TUPLAS
¿Qué es una tupla?: Es muy parecida a una lista, pero con una diferencia clave:
No se puede modificar.
Ejemplo:
  colores = ("rojo", "verde", "azul")
  dias = ("lunes", "martes")
Se usan paréntesis en lugar de corchetes.
¿Cuándo usar una tupla? Cuando los datos:
• No deben cambiar
• Son valores fijos
• Representan algo constante (como días de la semana)

Ejemplo:
  dias = ("lunes", "martes", "miércoles", "jueves", "viernes")

DICCIONARIOS: Un diccionario es una estructura que almacena datos en formato:
Permite organizar información de manera más estructurada.
clave : valor
Ejemplo:
alumno = { "nombre": "Darío", "edad": 15, "curso": "3A" }
persona = { "nombre": "Ana", "edad": 20 }

¿Cómo acceder a los datos?
print(alumno["nombre"])
Resultado: Dario
¿Para qué sirven?: Son ideales cuando queremos representar:
• Personas
• Productos
• Registros
• Datos organizados

MANEJO DE ERRORES
El manejo de errores permite evitar que el programa se detenga ante un problema inesperado. En programación, los errores son normales.
Python permite manejarlos con:
try:
  numero = int(input("Ingrese un número: ")) 
except:
    print("Eso no es un número válido")
Esto evita que el programa se rompa.

ARCHIVOS (Nivel Intermedio) Un archivo es un medio para guardar información de forma permanente.
Python permite:
•     Crear archivos
•     Escribir en ellos
•     Leer información guardada Ejemplo:
with open("datos.txt", "w") as archivo: archivo.write("Hola mundo")
Para leer:
with open("datos.txt", "r") as archivo: contenido = archivo.read() print(contenido)
Esto ya es programación más cercana a la realidad.
























