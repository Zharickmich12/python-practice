# TALLER 4 PYTHON

from datetime import date

# Fecha actual
hoy = date.today()
print("Hoy es el día:", hoy)
print()

# EJERCICIO DE LAS CLASES DE TRIÁNGULOS
ai = int(input("Digite el valor de Ai: "))
bt = int(input("Digite el valor de Bt: "))
gt = int(input("Digite el valor de Gt: "))

# Clasificación del triángulo
if ai == bt == gt:
    print("EL TRIÁNGULO ES EQUILÁTERO")
elif ai == bt or ai == gt or bt == gt:
    print("EL TRIÁNGULO ES ISÓSCELES")
else:
    print("EL TRIÁNGULO ES ESCALENO")
print()

# EJERCICIO DE ANIMALES
animal = input("Digite un animal: ")
animal = animal.upper()  # Convertir a mayúsculas para estandarizar

if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre:", animal)
elif animal == "GATO":
    print("Este animal persigue a los ratones:", animal)
elif animal == "OSO":
    print("Este animal vive en el polo norte:", animal)
else:
    print("No es PERRO, ni GATO, ni OSO:", animal)

print()
print("FIN")