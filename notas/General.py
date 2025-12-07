# ============================================================
#                       COMANDO PRINT
# ============================================================

# print permite que el programa muestre información en pantalla.
print("Esto es un texto")

# ============================================================
#                  VARIABLES: TEXTO Y NÚMEROS
# ============================================================

# Una variable almacena información.
# Python distingue mayúsculas/minúsculas (case sensitive).
# No se pueden usar tildes, ñ ni nombres reservados (if, for, etc.)

# ============================================================
#                         TIPOS BÁSICOS
# ============================================================

# -------------------- NÚMEROS --------------------

# int: enteros
# float: números reales (con punto decimal)
numero1 = int(2)
numero2 = float(2.5)

print(numero1)   # 2
print(numero2)   # 2.5

# Saber el tipo de una variable:
# type(variable)
print(type(numero1))  # <class 'int'>
print(type(numero2))  # <class 'float'>


# -------------------- TEXTO (str) --------------------

texto = "Esto es un texto"
texto2 = 'Esto es otro texto'
print(texto)
print(texto2)

# Texto multilinea:
texto3 = """Hola
caracola"""
print(texto3)

# Convertir números a texto:
texto_num = str(54)
print(texto_num)

# Concatenar texto:
print("Hola" + " Caracola")

# Precaución al unir texto + números:
texto = "Esto es un texto"
numero = 15

# print(texto + " " + numero)  # ERROR
print(texto + " " + str(numero))  # Correcto


# ============================================================
#                       LISTAS EN PYTHON
# ============================================================

# Las listas:
# - Tienen orden
# - Permiten modificar valores
# - Aceptan duplicados
# - Se crean con []

Ferrari2014 = ["Fernando Alonso", "Kimi Raikkonen"]
Ferrari2013 = ["Fernando Alonso", "Felipe Massa"]
print(Ferrari2014)
print(Ferrari2013)

# Operaciones comunes en listas:
# lista[i]              → acceder al elemento i
# lista.pop(i)          → extrae y borra el elemento i
# lista.append(x)       → añade al final
# lista.insert(i, x)    → inserta en la posición i
# lista.extend(lista2)  → fusiona listas
# lista.remove(x)       → elimina el primer x

print(Ferrari2014[1])  # Acceso por índice

Ferrari2014.pop(1)
print(Ferrari2014)

Ferrari2014.append("Kimi Raikkonen")
print(Ferrari2014)

del Ferrari2014[0]
Ferrari2014.insert(0, "Fernando Alonso")
print(Ferrari2014)

Ferrari2014.extend(Ferrari2013)
print(Ferrari2014)

Ferrari2014.remove("Fernando Alonso")
print(Ferrari2014)


# ============================================================
#                   DICCIONARIOS EN PYTHON
# ============================================================

# Se crean con {} usando pares "key: value".
# No pueden tener keys duplicadas.

diccionario = {
    'Piloto 1': 'Fernando Alonso',
    'Piloto 2': 'Kimi Raikkonen',
    'Piloto 3': 'Felipe Massa'
}

print(diccionario)

# Operaciones comunes:
# dic.get('key')                  → devuelve valor
# dic.pop('key')                  → devuelve valor y elimina
# dic.update({'key': valor})      → actualiza o crea key
# 'key' in diccionario            → True/False
# valor in diccionario.values()   → True/False

print(diccionario.get('Piloto 1'))

print(diccionario.pop('Piloto 1'))
print(diccionario)

diccionario.update({'Piloto 4': 'Lewis Hamilton'})
diccionario.update({'Piloto 2': 'Sebastian Vettel'})
print(diccionario)

print("Piloto 1" in diccionario)
print("piloto 1" in diccionario)
print("Sebastian Vettel" in diccionario)
print("Sebastian Vettel" in diccionario.values())

del diccionario['Piloto 2']
print(diccionario)


# ============================================================
#                          CONJUNTOS (set)
# ============================================================

# Los conjuntos:
# - No tienen elementos duplicados
# - Se crean con {}
# - Sirven para operaciones de conjuntos

lista = ['Fernando', 'Fernando', 'Felipe']
print(lista)

# Eliminar duplicados:
lista = list(set(lista))
print(lista)

conjunto = {'Fernando Alonso', 'Kimi Raikkonen', 'Felipe Massa'}
print(conjunto)

# Operaciones:
# A | B → unión
# A & B → intersección
# A - B → diferencia
# A ^ B → diferencia simétrica


# ============================================================
#                         IF / ELIF / ELSE
# ============================================================

Alonso_Position = 1

if Alonso_Position == 1:
    print("Espectacular Alonso, se ha hecho justicia a pesar del coche")
    print("Ya queda menos para ganar el mundial")
elif Alonso_Position > 1:
    print("Gran carrera de Alonso, lástima que el coche no esté a la altura")
else:
    print("No ha podido terminar la carrera por una avería mecánica")

# Condiciones comunes:
# ==
# <
# >
# not
# and
# or


# ============================================================
#                          BUCLE WHILE
# ============================================================

vuelta = 1
while vuelta < 10:
    print("Vuelta " + str(vuelta))
    vuelta = vuelta + 1  # Evitar bucles infinitos


# ============================================================
#                           BUCLE FOR
# ============================================================

for vuelta in range(1, 10):
    print("Vuelta " + str(vuelta))

coches = ('Ferrari', 'Tesla', 'BMW', 'Audi')

for coche in coches:
    print(coche)

for i, coche in enumerate(coches):
    print(str(i) + " - " + coche)


# ============================================================
#                           MÓDULOS
# ============================================================

# Un módulo es código ya hecho que podemos reutilizar.

# Instalación (ejemplo con Anaconda):
# conda install html5lib

# Cargar un módulo:
# import modulo

# Usar una función de un módulo:
# modulo.funcion()

import math
print(math.sqrt(16))  # Ejemplo