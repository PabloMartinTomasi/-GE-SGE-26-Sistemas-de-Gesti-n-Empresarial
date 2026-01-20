"""
1-- Modifica el ejercicio para que el usuario pueda introducir los datos desde la terminal
e indicar si es un menor de edad
Crear una clase persona con los atributos:
**** nombre, edad, dni
Con los métodos:
init()
es_mayor_de_edad() esre restorna True cuando cumple la condición
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
        

nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))
dni = input("Ingresa el dni: ")

persona1 = Persona(nombre, edad, dni)

print("El nombre es: ", persona1.nombre)
if persona1.es_mayor_de_edad():
    print(persona1.nombre, "es mayor de edad")
else:
    print(persona1.nombre, "es menor de edad")