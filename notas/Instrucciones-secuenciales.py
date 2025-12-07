# ======================================
# Instrucciones secuenciales en Python
# ======================================

# --------------------------------------
# 3.1 Comentarios en Python
# --------------------------------------
# Comentarios de una línea
# SENA: Colombia
# Regional: Santander

a = 30  # a representa el número de aprendices por Ficha
b = 9   # b representa el número de Fichas de programación de software

# Comentario de varias líneas
"""
Estos son datos de los 8 centros de formación ubicados en el departamento de Santander.
"""

# --------------------------------------
# 3.2 Instrucciones de asignación y operadores
# --------------------------------------
a = 8
b = 5

# Operadores aritméticos
c = a + b       # Suma
print("Suma:", c)

c = a - b       # Resta
print("Resta:", c)

c = a * b       # Multiplicación
print("Multiplicación:", c)

c = a / b       # División
print("División:", c)

c = a % b       # Módulo o residuo
print("Módulo:", c)

c = a ** b      # Potencia
print("Potencia:", c)

c = a // b      # División entera
print("División entera:", c)

# --------------------------------------
# 3.3 Inicialización de variables
# --------------------------------------
b = 100
c = b ** 3
print("Valor de c:", c)

# --------------------------------------
# 3.4 Uso de constantes y variables
# --------------------------------------
IVA = 0.19
precio_inicial = 3000
precio_final = precio_inicial * (1 + IVA)
print("Precio final:", precio_final)

a = 10000
b = a * 2 / 100
c = "JUAN CARLOS"
print(c, "debe la suma de $", a + b)

# Inicializar varias variables a la vez
a = b = c = 10
print(a, b, c)

# Inicializar con valores diferentes
a, b, c = 100, 200, 300
print(a, b, c)

# Acumulador y contador
suma = 0
edad = 25
suma += edad
print("Suma de edades:", suma)

total = 0
total += 1
print("Contador total:", total)

# --------------------------------------
# 3.5 Funciones predefinidas de Python
# --------------------------------------
texto = "Mario eS mi Aprendiz"
print("Longitud:", len(texto))
print("En minúsculas:", texto.lower())
print("En mayúsculas:", texto.upper())
print("Reemplazar:", texto.replace("Aprendiz", "Estudiante"))

a = "El mundo está en aislamiento preventivo"
lista_b = a.split()
print("Split:", lista_b)

x = range(6)
print("Rango:", list(x))

print("Convertir a string:", str(100))
print("Convertir a int:", int('89'))
print("Convertir a float:", float('3.14'))

x = [1, 3, 2]
print("Máximo:", max(x))
print("Mínimo:", min(x))
print("Lista de range:", list(range(4)))
print("Valor ASCII de 'C':", ord('C'))
print("Redondeo:", round(15.92))

# --------------------------------------
# 3.6 Librerías de fecha, random y matemáticas
# --------------------------------------
# Librerías de fecha
from datetime import date, datetime

hoy = date.today()
print("Hoy es el día:", hoy)

fecha = datetime.now()
print("Fecha completa:", fecha)

# Librería random
import random

a = random.randint(10, 100)
print("Entero aleatorio:", a)

b = random.randrange(0, 100, 5)
print("Randrange:", b)

c = random.random()
print("Float aleatorio 0-1:", c)

d = random.uniform(100, 200)
print("Float aleatorio 100-200:", d)

amigos = ['Luis', 'Mauricio', 'Patricia', 'Carlos']
ganador = random.choice(amigos)
print("Ganador:", ganador)

naipes = [1,2,3,4,5,6,7,10,11,12]
random.shuffle(naipes)
print("Naipes barajados:", naipes)
print("Muestra de 3 cartas:", random.sample(naipes, 3))

# Librería math
import math

a = 123.56
print("Truncado:", math.trunc(a))

a = -200.45
print("Valor absoluto:", math.fabs(a))

a = 6
print("Factorial:", math.factorial(a))

c = math.fmod(16, 5)
print("Residuo float:", c)

a = 3
print("Raíz cuadrada:", math.sqrt(a))

angulo = 60
radianes = math.radians(angulo)
print("Radianes:", radianes)
print("Seno:", math.sin(radianes))
print("Coseno:", math.cos(radianes))
print("Tangente:", math.tan(radianes))