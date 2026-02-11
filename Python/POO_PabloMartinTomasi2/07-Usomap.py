"""
Elevar al cuadrado una lista de numeros
utilizando map()
"""

def cuadrado(x):
    return x ** 2

numeros = [1, 5, 6, 9, 62, 10, 999]
cuadrados = list(map(cuadrado, numeros))

print(numeros)
print(cuadrados)