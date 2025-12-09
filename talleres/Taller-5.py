# TALLER 5 PYTHON

from datetime import date

# Fecha actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()

print("TALLER 5: CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()

# --- Entrada de datos: dos números (num1 y num2) ---
# Se intenta convertir a int; si el usuario escribe mal, se volverá a pedir.
def pedir_entero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor digite un número entero.")

num1 = pedir_entero("Digite el primer número (puede ser 0 o positivo): ")
num2 = pedir_entero("Digite el segundo número (debe ser mayor que el primero): ")

# Si num2 no es mayor, ajustamos para evitar bucles vacíos o errores.
if num2 <= num1:
    print(f"ATENCIÓN: el segundo número ({num2}) no es mayor que el primero ({num1}).")
    num2 = num1 + 1
    print(f"Se ajustó el segundo número a {num2} para que el rango sea válido.")
print()

# --- Ciclo 1: for desde 0 hasta num1-1 (range(num1)) ---
print(f"Ciclo para el primer número: for i in range({num1}):")
for i in range(num1):
    print(i)
print("fin del ciclo")
print()

# --- Ciclo 2: for desde num1 hasta num2-1 (range(num1, num2)) ---
print(f"Ciclo desde el primer número hasta el segundo: for i in range({num1}, {num2}):")
for i in range(num1, num2):
    print(i)
print("fin del ciclo")
print()

# --- Ciclo 3: for desde num1 hasta num2-1 con paso 2 (range(num1, num2, 2)) ---
print(f"Ciclo desde {num1} hasta {num2} con incremento de 2: for i in range({num1}, {num2}, 2):")
for i in range(num1, num2, 2):
    print(i)
print("fin del ciclo")
print()

# --- Ejemplo recorriendo una cadena (nombre de empresa) ---
empresa = input("Digite el nombre de una empresa: ")
# Mostrar versiones en mayúsculas y minúsculas
print("Empresa (original):", empresa)
print("Empresa en mayúsculas:", empresa.upper())
print("Empresa en minúsculas:", empresa.lower())
print()

# Recorrer cada carácter de la cadena
print("Recorrido carácter a carácter:")
for caracter in empresa:
    print(caracter)
print("fin del ciclo de caracteres")
print()

# Ejemplo de uso de break y continue dentro de un for
print("Ejemplo: mostrar caracteres hasta encontrar un espacio (uso de break):")
for caracter in empresa:
    if caracter == " ":
        print("(Se encontró un espacio; se sale del bucle con break)")
        break
    print(caracter)
print("fin del ejemplo break")
print()

print("Ejemplo: mostrar solo caracteres que no sean vocales (uso de continue):")
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
for caracter in empresa:
    if caracter in vocales:
        continue
    print(caracter, end=" ")
print("\nfin del ejemplo continue")
print()

print("FIN")