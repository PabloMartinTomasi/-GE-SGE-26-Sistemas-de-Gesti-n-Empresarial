"""
5-- Crear una clase llamada Persona
con los siguientes atributos:
** nombre, edad

** un constructor, donde los datos pueden estar vacios
** los setters y getters para cada uno de los atributos

para cada uno de los atributos
* mostrar(): muestra los datos de la persona
* es_mayor_de_edad(): devuelve el valor logico 
inidicando si es mayor de edad
"""

class Persona:
    def __init__(self, nombre = "", edad = 0):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    

    def set_edad(self, edad):
        self.edad = edad
    
    def get_edad(self):
        return self.edad
    

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "es mayor de edad"
        else:
            return "es menor de edad"


nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))

persona1 = Persona()
persona1.set_nombre(nombre)
persona1.set_edad(edad)

print(f"\nDatos de {persona1.get_nombre()}:\n{persona1.mostrar()}")
print(f"\n{persona1.get_nombre()}, {persona1.es_mayor_de_edad()}")





























