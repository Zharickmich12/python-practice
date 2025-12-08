# ================================
# ESTRUCTURAS DE CONTROL EN PYTHON
# ================================

"""
Las sentencias condicionales permiten tomar decisiones dentro del programa.
Evalúan condiciones (True/False) y ejecutan distintos bloques según el resultado.
"""

# -------------------------------
# OPERADORES BOOLEANOS (LÓGICOS)
# -------------------------------

"""
Operadores:
    and  -> True solo si ambos operandos son True
    or   -> True si al menos uno es True
    not  -> invierte el valor booleano

Prioridad:
    1. not
    2. and
    3. or

Elementos considerados False:
    0, 0.0, "", None, listas vacías, tuplas vacías, etc.

Función bool(): verifica si algo es True o False
"""

# Ejemplos
bool(0)      # False
bool(5)      # True
bool("SENA") # True


# -------------------------------
# OPERADORES DE COMPARACIÓN
# -------------------------------

"""
    >   Mayor que
    >=  Mayor o igual
    <   Menor que
    <=  Menor o igual
    ==  Igual a
    !=  Diferente a
"""

# Ejemplos:
2 == 3   # False
2 > 1    # True
8 >= 5   # True
5 != 6   # True


# -------------------------------
# SENTENCIA IF (condicional simple)
# -------------------------------

"""
Sintaxis:
if condicion:
    bloque verdadero
"""

numero = -2
if numero < 0:
    print("El número es negativo")
    numero = 0  # se modifica si la condición es verdadera

# -------------------------------
# SENTENCIA IF - ELSE
# -------------------------------

"""
if condicion:
    bloque verdadero
else:
    bloque falso
"""

x = 7
if x % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Uso de 'pass' para no hacer nada
edad = 130
if edad < 99:
    pass
else:
    print("¡No creo que tenga esa edad!")


# -------------------------------
# CONDICIONALES ANIDADAS
# -------------------------------

curso1 = "Requerimientos"
curso2 = "Algoritmos"

if curso1 == "Requerimientos":
    if curso2 == "Algoritmos":
        print("Estudia Programación de Software")
    else:
        print("Estudia otro programa")


# -------------------------------
# ELIF (Condicionales encadenadas)
# -------------------------------

"""
if condicion1:
    bloque
elif condicion2:
    bloque
elif condicion3:
    bloque
else:
    bloque por defecto
"""

voto = 3
if voto == 1:
    print("Votó por el candidato X")
elif voto == 2:
    print("Votó por Y")
elif voto == 3:
    print("Votó por Z")
else:
    print("Voto inválido")


# -------------------------------
# EXPRESIONES BOOLEANAS COMPUESTAS
# -------------------------------

"""
Ejemplo: encontrar el menor de tres números usando 'and'
"""

a = 7
b = 3
c = 9

if a < b and a < c:
    print("El menor es:", a)
elif b < c:
    print("El menor es:", b)
else:
    print("El menor es:", c)