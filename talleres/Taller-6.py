# TALLER 6 PYTHON

from datetime import date

# Fecha actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()

print("TALLER 6: CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()

# Función auxiliar para pedir enteros con validación
def pedir_entero(prompt, min_val=None, max_val=None):
    while True:
        try:
            n = int(input(prompt))
            if (min_val is not None and n < min_val) or (max_val is not None and n > max_val):
                print(f"Por favor ingresa un entero entre {min_val} y {max_val}.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Por favor digite un número entero.")

# Ciclo controlado por contador
print("1) Ciclo controlado por contador")
n = pedir_entero("Digite un número entero positivo (ej. 5): ", min_val=0)
print(f"Imprimiendo desde 1 hasta {n} usando while:")

i = 1
while i <= n:
    print(i)
    i += 1
print("fin del ciclo\n")

# Ciclo controlado por evento (adivinar número)
print("2) Ciclo controlado por evento — Adivina el número (1 a 10)")
numero_objetivo = 5  # número a adivinar
intentos = 0

numero_usuario = pedir_entero("Digite un número de 1 a 10: ", 1, 10)
while numero_usuario != numero_objetivo:
    intentos += 1
    print("No es correcto. Intenta de nuevo.")
    numero_usuario = pedir_entero("Digite un número de 1 a 10: ", 1, 10)

# Si salió del while es porque acertó
intentos += 1  # contar el intento en el que acertó
print("Acertaste en el intento No.", intentos)
print("fin del ciclo\n")


# Ciclo abortado con break (recorrido de caracteres)
print("3) Ciclo abortado con break — Recorrido de caracteres de un nombre de amistad")
amistad = input("Digite nombre de una amistad: ").strip()
amistad = amistad.upper()

print("Recorriendo caracteres (se sale si encuentra la letra 'A'):")
for caracter in amistad:
    print(caracter)
    if caracter == "A":
        print("Se encontró 'A' — se aborta el recorrido con break.")
        break
else:
    # Este else se ejecuta si el bucle for terminó sin encontrar 'A'
    print("No se encontró la letra 'A' en el nombre.")

print("fin del ciclo\n")

# continue y pass dentro de while

print("4) Ejemplo adicional: uso de continue y pass dentro de while")

contador = 10
print("Mostrando valores desde 10 decreciendo de 1 en 1, saltando el 7 (continue) y mostrando pass en 5:")
while contador >= 0:
    contador -= 1
    if contador == 7:
        # skip 7
        continue
    if contador == 5:
        # placeholder, no hace nada, solo ejemplifica pass
        pass
    print("Valor actual de contador:", contador)
print("fin del ciclo\n")

# while con else

print("5) Ejemplo: while con else")
tope = pedir_entero("Ingrese un tope positivo para contar hasta (ej. 3): ", min_val=1)
i = 1
while i <= tope:
    print(i)
    i += 1
else:
    print("El while terminó porque la condición ya no se cumplía.")

print("\nFIN")