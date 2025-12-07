# ------------------------------------------------------------
# Python como lenguaje
# ------------------------------------------------------------
# Python es un lenguaje interpretado, multiplataforma
# y multiparadigma.
# Permite desarrollar aplicaciones web, móviles, videojuegos,
# algoritmos científicos y Machine Learning.
#
# Su sintaxis es clara y usa indentación para definir bloques
# de código, lo cual mejora la legibilidad.


# ------------------------------------------------------------
# Comentarios en Python
# ------------------------------------------------------------
# Un comentario es una línea NO ejecutable.
# Se usan para documentar y explicar el código.

# 1. Comentarios de una sola línea → usando #
# Ejemplo:
# Autor: Pepito Pérez
# Ciudad: Bogotá

x = 0
y = 8   # También pueden ir al final de una línea

# 2. Comentarios multilínea → usando triple comilla
"""
Este es un comentario multilínea.
Puede ocupar varias líneas consecutivas.
"""


# ------------------------------------------------------------
# Errores y excepciones
# ------------------------------------------------------------
# Si escribimos algo incorrecto, Python mostrará un mensaje
# de error indicando el tipo de error y la ubicación.
#
# Ejemplo:
# 1 + 2)
# SyntaxError: unmatched ')'
#
# Los errores en Python se llaman "excepciones".


# ------------------------------------------------------------
# TIPOS DE DATOS EN PYTHON
# ------------------------------------------------------------

# Python tiene tipos básicos:
# - Numéricos (int, float, complex)
# - Booleanos (bool)
# - Cadenas de caracteres (str)

# Y tipos compuestos:
# - Secuencias: list, tuple, range
# - Conjuntos: set
# - Mapas: dict


# ============================================================
# A. DATOS NUMÉRICOS
# ============================================================

# -----------------------------
# 1. Enteros → int
# -----------------------------
v = -3          # int
m = v + 8       # int → resultado: 5
z = round(m/2)  # int → redondeo

# Representación en otros sistemas numéricos:
decimal = 8
binario = 0b1101       # binario → 13
octal = 0o11           # octal → 9
hexadecimal = 0xc      # hexadecimal → 12


# -----------------------------
# 2. Flotantes → float
# -----------------------------
real = 1.1 + 2.2
round(real, 1)     # muestra 3.3


# -----------------------------
# 3. Complejos → complex
# -----------------------------
complejo = 5 + 3j
complejo.real   # 5.0
complejo.imag   # 3.0

# Para operaciones complejas avanzadas usar: import cmath


# -----------------------------
# Aritmética numérica
# -----------------------------
# Operaciones comunes: +, -, *, /
# Exponente: **
# División entera: //
# Mezcla tipos: el resultado usa el tipo "más grande":
# int < float < complex

x = 2
a = x**3        # 8
b = 31
c = b // 4      # 7
g = 31.0
h = g / 4       # 7.75 (float)
1 + 2.0         # 3.0
2 + 3j + 5.7    # (7.7+3j)


# ============================================================
# B. DATO BOOLEANO — bool
# ============================================================
a = False
b = True

# Objetos considerados falsos:
# None
# False
# 0, 0.0, 0j
# '', (), [], {}, set(), range(0)

c = None
type(c)         # <class 'NoneType'>


# ============================================================
# C. CADENAS DE CARACTERES — str
# ============================================================
saludo1 = 'Hola "María"'
saludo2 = 'Hola \'María\''
saludo3 = "Hola 'María'"

# En Python no existe tipo char, pero un string de un carácter sirve.
caracter = 'z'


# ============================================================
# D. OTROS TIPOS COMPUESTOS
# ============================================================

# -----------------------------
# LISTAS → list
# -----------------------------
lista = [3, 4.2, 'SENA', [8, 9], 5]

# Acceso:
lista[0]      # 3
lista[3][0]   # 8
lista[1:3]    # [4.2, 'SENA']


# -----------------------------
# TUPLAS → tuple
# -----------------------------
tupla = (8, "b", 4.91)
len(tupla)        # 3
tupla_vacia = ()
una_tupla = (3,)  # tupla de un elemento


# -----------------------------
# CONJUNTOS → set
# -----------------------------
frutas = set(['mango', 'pera', 'manzana', 'limón'])
frutas.remove('manzana')


# -----------------------------
# DICCIONARIOS → dict
# -----------------------------
futbolistas = {
    13: "Mina",
    21: "Lucumi",
    17: "Fabra",
    11: "Cuadrado",
    9:  "Falcao",
    19: "Muriel",
    15: "Uribe",
    10: "James Rodriguez",
    16: "Lerma",
    5:  "Wilmar Barrios",
    3:  "Murillo"
}

futbolistas[9]   # 'Falcao'


# Ejemplo conjunto:
lista_demo = [1, 2, 3, 8, 9]
tupla_demo = (1, 4, 8, 0, 5)
conjunto_demo = set([1, 3, 1, 4])    # {1, 3, 4}
diccionario_demo = {'a': 1, 'b': 3, 'z': 8}


# ============================================================
# 2.2 IDENTIFICAR TIPOS → type() e isinstance()
# ============================================================
type(5)                # int
type(3.14)             # float
type("Hola")           # str

isinstance(8, int)     # True
isinstance(False, bool)# True


# ============================================================
# 2.3 CONVERSIÓN DE TIPOS
# ============================================================
edad = "25"
edad = int(edad) + 10  # convierte str → int
edad = str(edad)       # convierte int → str

float("18.66")         # válido
# float("hola") → error: ValueError