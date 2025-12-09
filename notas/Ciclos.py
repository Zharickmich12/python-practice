# ---------------------------------------------
# CICLOS ITERATIVOS
# ---------------------------------------------

# Introducción:
# Un ciclo repetitivo o iterativo ejecuta un bloque de instrucciones varias veces.
# Puede repetirse un número fijo de veces (for) o mientras una condición siga siendo verdadera (while).

# ----------------------------------------------------------
# 1. CICLO FOR
# ----------------------------------------------------------
# Se usa cuando sabemos cuántas veces queremos repetir un bloque.
# Sirve para recorrer listas, cadenas, tuplas, conjuntos y diccionarios.

# Ejemplo básico:
animales = ['leon', 'tigre', 'cocodrilo']
for animal in animales:
    print("El animal es:", animal, "tamaño de palabra:", len(animal))


# ----------------------------------------------------------
# 1.1 USO DE RANGE
# ----------------------------------------------------------
# range(valor_final)
for i in range(5):
    print(i)
print("fin del ciclo")

# range(valor_inicial, valor_final)
for i in range(2, 5):
    print(i, i**3)
print("fin del ciclo")

# range(valor_inicial, valor_final, incremento)
for i in range(10, 0, -2):
    print(i)
print("fin del ciclo")


# ----------------------------------------------------------
# 1.2 CICLO FOR EN DIFERENTES ESTRUCTURAS
# ----------------------------------------------------------

# CADENAS
for character in "hola mundo":
    print(character)
print("fin del ciclo")


# LISTAS
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros:
    print(numero, end=" ")
print("fin del ciclo")


# TUPLAS
conexion_bd = ("115.16.10.5", "root", "7890", "clientes")
for parametro in conexion_bd:
    print(parametro)
print("fin del ciclo")


# CONJUNTOS
A = {1, 2, 3, 5, 3, 6, 4, 2}  # el conjunto elimina duplicados
for elemento in A:
    print(elemento)
print("fin del ciclo")


# DICCIONARIOS – Forma 1
ensalada = {'Manzana': 'verde', 'Patilla': 'rosado', 'Banano': 'amarillo', 'Papaya': 'naranja'}
for nombre, color in ensalada.items():
    print(nombre, "es de color", color)
print("fin del ciclo")

# DICCIONARIOS – Forma 2
for elemento in ensalada:
    print(elemento, "es de color", ensalada[elemento])
print("fin del ciclo")


# ----------------------------------------------------------
# 1.3 SENTENCIAS BREAK, CONTINUE y PASS en FOR
# ----------------------------------------------------------

# BREAK
print("Uso de la sentencia BREAK")
for caracter in "PYTHON SENA":
    if caracter == "N":
        break
    print("El caracter actual es:", caracter)
print("fin del ciclo")


# CONTINUE
print("Uso de la sentencia CONTINUE")
variable = 15
while variable > 1:
    variable -= 2
    if variable == 9:
        continue
    print("Valor actual de la variable:", variable)
print("fin del ciclo")


# PASS
print("Uso de la sentencia PASS")
for letra in "PYTHON SENA":
    if letra == "N":
        pass  # no hace nada
    print("El caracter actual es:", letra)
print("fin del ciclo")


# ----------------------------------------------------------
# 1.4 FOR + ELSE
# ----------------------------------------------------------
db_connection = ("115.0.0.5", "7890", "root", "empleados")
for parametro in db_connection:
    print(parametro)
else:
    print(f"""El comando PostgreSQL es:
$ psql -h {db_connection[0]} -p {db_connection[1]} -U {db_connection[2]} -d {db_connection[3]}""")


# ----------------------------------------------------------
# 2. CICLO WHILE
# ----------------------------------------------------------
# Se ejecuta mientras la condición sea verdadera.

i = 1
while i <= 11:
    print(i)
    i += 2
print("Programa finalizado")


# ----------------------------------------------------------
# Ejemplo: Adivinar número
# ----------------------------------------------------------
i = 1
numero1 = 100
numero2 = int(input("Digite un número de 1 a 100: "))

while numero2 != numero1:
    i += 1
    numero2 = int(input("Digite un número de 1 a 100: "))

print("Acertaste en el intento No.", i)


# ----------------------------------------------------------
# 2.2 TIPOS DE WHILE
# ----------------------------------------------------------

# WHILE CONTROLADO POR CONTADOR
print("Uso del ciclo while con contador")
total, valor = 0, 1

while valor <= 12:
    print(valor)
    total += valor
    print("el total parcial es", total)
    valor += 1

print("El total final es", total)
print("fin del ciclo while")


# WHILE CONTROLADO POR EVENTO
print("Uso del ciclo while controlado por evento")
promedio, total, contador = 0, 0, 0

placa = input("Introduzca la placa del vehículo (99 para salir): ")
while placa != "99":
    valor = float(input("Digite valor del parqueadero: "))
    total += valor
    contador += 1
    placa = input("Introduzca la placa del vehículo (99 para salir): ")

promedio = round(total / contador)
print("Promedio de vr. parqueadero:", promedio)
print("Total dinero recaudado:", round(total))
print("fin del ciclo while")


# WHILE + ELSE
print("Uso del ciclo while + else")
promedio, total, contador = 0, 0, 0

placa = input("Introduzca la placa del vehículo (99 para salir): ")
while placa != "99":
    valor = float(input("Digite valor del parqueadero: "))
    total += valor
    contador += 1
    placa = input("Introduzca la placa del vehículo (99 para salir): ")
else:
    promedio = round(total / contador)
    print("Promedio:", promedio)
    print("Total recaudado:", round(total))

print("final del ciclo while + else")


# ----------------------------------------------------------
# 2.3 BREAK, CONTINUE, PASS EN WHILE
# ----------------------------------------------------------

# BREAK
print("Uso de BREAK en while")
variable = 35
while variable > 1:
    variable -= 5
    if variable == 10:
        break
    print("Valor actual:", variable)
print("fin del ciclo")


# CONTINUE
print("Uso de CONTINUE en while")
variable = 35
while variable > 1:
    variable -= 5
    if variable == 15:
        continue
    print("Valor actual:", variable)
print("fin del ciclo")


# PASS
print("Uso de PASS en while")
variable = 35
while variable > 1:
    variable -= 5
    if variable == 25:
        pass
    print("Valor actual:", variable)
print("fin del ciclo")
