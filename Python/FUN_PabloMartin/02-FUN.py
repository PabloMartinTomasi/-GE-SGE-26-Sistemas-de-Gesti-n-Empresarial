"""
Escribe una funcion para calcular el volumen de un cilindro
"""

import math

def volumen_cilindro(radio, altura):
    return math.pi * radio **2 * altura

radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

volumen = volumen_cilindro(radio, altura)
print(f"El volumen del cilindro con un radio de {radio} y una altura de {altura} es {volumen}")