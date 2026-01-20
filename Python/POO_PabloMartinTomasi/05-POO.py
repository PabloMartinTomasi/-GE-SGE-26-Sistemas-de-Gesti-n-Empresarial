"""
2-- Crear una clase Rectangulo con los siguientes atributos:
    base: base del rectangulo
    altura: altura del rectangulo

La clase debe tener los siguientes metodos:
 ** __init__ (self, base, altura): inicializa los ataributos de la clase
 ** calcular_area(self): calcula y devueleve area del rectangulo
 ** calcular_perimetro(self): calcula y devuelve el perimetro del rectangulo

Los datos hay que ponerlos por el usuario
"""

class Rectangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))

rectangulo1 = Rectangulo(base, altura)

print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")
print(f"El perimetro del rectangulo es: {rectangulo1.calcular_perimetro()}")