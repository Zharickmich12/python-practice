# TALLER 1 PYTHON

from datetime import date

# Obtener la fecha actual
hoy = date.today()
print("Hoy es el día:", hoy)

# Entrada de datos del usuario
n1 = int(input("Digite el primer número: "))
n2 = int(input("Digite el segundo número: "))

# Operaciones básicas
suma = n1 + n2
resta = n1 - n2
producto = n1 * n2

# Para la división, se verifica que el segundo número no sea cero
if n2 != 0:
    division = n1 / n2
else:
    division = "Indefinida (no se puede dividir entre 0)"

# Salida de resultados
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", producto)
print("La división es:", division)

print("FIN")