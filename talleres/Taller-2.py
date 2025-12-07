# TALLER 2 PYTHON

from datetime import date

hoy = date.today()  # fecha actual
print("Hoy es el día: ", hoy)

# Entrada de 3 números enteros
a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
c = int(input("Digite el tercer número: "))

x = [a, b, c]

print("El valor máximo es:", max(x))
print("El valor mínimo es:", min(x))
print("La suma de los 3 números es:", sum(x))
print()

# Entrada de un número decimal y redondeo
z = float(input("Digite un número con decimales: "))
redondo = round(z)
print("El valor de", z, "redondeado es:", redondo)
print()

# Entrada de una frase y manipulación de cadenas
frase = input("Digite una oración: ")
print("La frase en mayúscula es:", frase.upper())
print("La frase en minúscula es:", frase.lower())
print("La frase con mayúscula inicial es:", frase.capitalize())
print("La frase con palabras en mayúsculas es:", frase.title())
print("La longitud de la frase es:", len(frase), "caracteres")
print()

print("FIN")
