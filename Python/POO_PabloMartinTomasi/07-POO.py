"""
4-- Crear el procedimiento para poder resgistrar el kilometraje inicial y final
que una empresa de renta de vehículos

crea una clase coche con los siguientes atributos:
**** marca, modelo, matricula, km

con los siguientes métodos:
__init__ como contructor
km_entrega del vehiculo
mostrar por pantalla los datos iniciales y finales mediante un diccionario __dict__
"""

class Coche:
    def __init__(self, marca, modelo, matricula, km_inicial):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km_inicial = km_inicial
        self.km_final = km_inicial
    
    def km_entrega(self, km_final):
        if km_final < self.km_inicial:
            print("El kilometraje final no puede ser menor que el inicial")
        else:
            self.km_final = km_final
    
    def mostrar_datos(self):
        return self.__dict__

marca = input("Ingresa la marca del coche: ")
modelo = input("Ingresa el modelo del coche: ")
matricula = input("Ingresa la matrícula del coche: ")
km_inicial = int(input("Ingresa el kilometraje inicial del coche: "))

coche1 = Coche(marca, modelo, matricula, km_inicial)

km_final = int(input("\nIngrese el kilometraje al entregar el coche: "))
coche1.km_entrega(km_final)

print("\nDatos del coche:")
print(coche1.mostrar_datos())