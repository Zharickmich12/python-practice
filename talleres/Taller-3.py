# TALLER 3 PYTHON  
# AUTORA: Zharick Fetecua
# FECHA: 12/08/2025

from datetime import date

# Fecha actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()

# ---------------------------------------
# Comparación entre dos números
# ---------------------------------------

a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))

if a > b:
    print("A es mayor que B")
else:
    print("A es menor o igual que B")

print()

# ---------------------------------------
# Validación de cursos
# ---------------------------------------

curso1 = "Requerimientos"
curso2 = "Algoritmos"

print("El curso 1 es:", curso1)
print("El curso 2 es:", curso2)

if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print("Usted estudia Programación de Software")
else:
    print("Usted estudia otro programa diferente a Programación de Software")

print()
print("** Final del Análisis del Programa de Formación SENA **")
print()

# ---------------------------------------
# Trabajo con cadenas
# ---------------------------------------

frase = input("Digite una oración: ")

print("La frase en mayúscula es:", frase.upper())
print("La longitud de la frase es:", len(frase), "caracteres")

if len(frase) > 10:
    print("La frase contiene más de 10 caracteres")
else:
    print("La frase contiene 10 caracteres o menos")

print()
print("FIN")