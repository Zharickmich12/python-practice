# ============================================================
#                VARIABLES EN PYTHON
# ============================================================

# Una variable es un nombre que referencia un dato almacenado en memoria.
# Es un contenedor cuyo valor puede cambiar durante la ejecución del programa.

# Ejemplo básico:
suma = 1 + 2      # Variable que almacena el resultado de una operación
print(suma)       # 3


# ============================================================
#         ASIGNAR UN VALOR A UNA VARIABLE
# ============================================================

# Se usa el operador "="
a = 1
a = 3 * 4
a = 'Pythonista'   # A una misma variable se le puede asignar otro tipo


# Si intentamos usar una variable no definida:
# print(x)   --> NameError: name 'x' is not defined


# ============================================================
#                 TIPOS DE DATOS EN VARIABLES
# ============================================================

# Python infiere automáticamente el tipo de dato al ejecutar.
a = 1        # int
b = 'Hola'   # str
a = 'Hola'   # ahora la variable cambia a tipo str


# ============================================================
#                MODIFICAR EL VALOR DE UNA VARIABLE
# ============================================================

a = 1
print(a)   # 1
a = 3
print(a)   # 3


# ============================================================
#                         LITERALES
# ============================================================

# Un literal es un dato en crudo escrito directamente en el código.
n1 = 1            # literal numérico
n2 = 3.14         # literal float
c1 = "Hola"       # literal string
b1 = True         # literal booleano
vacio = None      # literal especial (ausencia de valor)


# ============================================================
#         ASIGNAR EL MISMO VALOR A MÚLTIPLES VARIABLES
# ============================================================

a = b = c = 1
print(a, b, c)   # 1 1 1


# ============================================================
#         ASIGNAR VARIOS VALORES A VARIAS VARIABLES
# ============================================================

a, b, c = 1, 2, 3
print(a, b, c)   # 1 2 3


# ============================================================
#                  VARIABLES Y MEMORIA
# ============================================================

# En Python TODO es un objeto.
# Las variables guardan referencias a objetos (no el valor directamente).

a = 1
b = 1

# a y b apuntan al MISMO objeto
print(id(a))
print(id(b))
print(id(1))

# Si ahora cambiamos b:
b = 2
print(id(a))     # sigue apuntando al objeto "1"
print(id(b))     # nueva dirección (objeto "2")

# Ahora igualamos ambas:
a = b
print(id(a))     # misma dirección
print(id(b))