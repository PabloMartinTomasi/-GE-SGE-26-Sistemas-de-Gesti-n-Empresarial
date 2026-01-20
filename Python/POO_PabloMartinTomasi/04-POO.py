"""
Crear una clase persona con los atributos:
**** nombre, edad, dni
Con los métodos:
init()
es_mayor_de_edad() esre restorna True cuando cumple la condición
"""


"""
Un metodo se llama dentro de una clase y siempre tiene self como primer parametro
Una funcion es un bloque de codigo reutilizabeble que no pertenece a una clase
"""

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
    
persona1 = Persona("Vegeta777", 26, "11111111A")

print("El nombre es: ", persona1.nombre)
if persona1.es_mayor_de_edad():
    print(persona1.nombre, "es mayor de edad")

