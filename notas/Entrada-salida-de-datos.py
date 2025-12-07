# -----------------------------
# Entrada y salida de datos en Python
# -----------------------------

# -----------------------------
# 1. Entrada de datos
# -----------------------------

# Entrada estándar con input()
# La entrada siempre es tipo cadena (str)
edad = input("¿Cuántos años tienes? ")
print("Tu edad es:", edad)

# Convertir a entero
celular = int(input("Danos tu número de celular: "))
print("Número celular:", celular)

# Convertir a float
estatura = float(input("Cuál es tu estatura? "))
print("Estatura:", estatura)

# -----------------------------
# 1.2 Entrada por script
# -----------------------------
# Guardar instrucciones en un script permite ejecutar varias líneas
# de código de forma organizada

print("\n--- Ejemplo de script ---")
nombre = input("Digite un nombre: ")
numero = int(input("Digite un número: "))
print("Su nombre es", nombre)
print("Su número es", numero)
cuadrado = numero ** 2
print("El valor del número al cuadrado es", cuadrado)

# -----------------------------
# 2. Salida de datos
# -----------------------------

# 2.1 Usando print
salario = 234500
empleado = "MARIA"
print("El salario devengado por", empleado, "es la suma de", salario)
print("El salario devengado por", empleado, "\nes la suma de $", salario)
print("El salario devengado por \t", empleado, "\tes la \tsuma de $", salario)

# 2.2 Salida con formato
titulo = "raíz cuadrada de tres"
valor = 3**0.5

# Usando % para formatear
print("El resultado de %s es %f" % (titulo, valor))
print("El resultado de %s es %.8f" % (titulo, valor))  # 8 decimales
print("El resultado de %s es %.1f" % (titulo, valor))  # 1 decimal

# 2.3 Impresión de cadenas y métodos útiles
frase1 = "El perro"
frase2 = "Manchas"
frase3 = "ladra en la oscuridad"

# Concatenar cadenas
print(frase1 + " " + frase2 + " " + frase3 + "?")

# Repetir cadenas
print(frase2 * 3)

# Métodos de cadenas
print(frase3.capitalize())  # Primera letra mayúscula
print(frase1.center(18))    # Centrar en ancho 18
print(frase2.lower())       # Todo minúscula
print(frase2.upper())       # Todo mayúscula
print(frase3.title())       # Mayúsculas iniciales de cada palabra