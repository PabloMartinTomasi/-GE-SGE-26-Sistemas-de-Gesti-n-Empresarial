"""
3-- Crear la clase libro con estos atributos:
**** titulo, autor, editorial, anio_publicacion

metodos:
contructor para inicializar los atributos

determina si el libro es del año 2020 hacia atras debe inidicar que es antiguo
si es del 2020 hasta la fecha actual, debe ejecutarse hasta que encuentre editorial "Espanola"
"""

""" class Libro:
    def __init__(self, titulo, autor, editorial, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion

    def libro_antiguo(self):
        return self.anio_publicacion < 2000

while(True):
    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingresa el autor del libro: ")
    editorial = input("Ingresa la editorial del libro: ")
    anio_publicacion = int(input("Ingresa el año de publicacion: "))

    libro = Libro(titulo, autor, editorial, anio_publicacion)

    if libro.libro_antiguo():
        print("El libro es antiguo")
    
    if libro.editorial == "Espanola":
        print("El libro es de la editorial espanola")
        break

    else:
        print("El libro no es de la editorial espanola") """





















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

""" class Coche:
    def __init__(self, marca, modelo, matricula, km_inicial):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km_inicial =  km_inicial
        self.km_final = km_inicial
    
    def km_entrega(self, km_final):
        if km_final < self.km_final:
            print("El kilometraje final debe de ser superior al kilometraje inicial")
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
print(coche1.mostrar_datos()) """
















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





""" class Persona:
    def __init__(self, nombre, edad):
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
        return f"Nombre: {self.nombre} \nEdad: {self.edad}"
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "es mayor de edad"
        else:
            return "es menor de edad"


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

persona = Persona(nombre, edad)

print(f"\nDatos de {persona.get_nombre()}:\n{persona.mostrar()}")
print(f"\n{persona.get_nombre()}, {persona.es_mayor_de_edad()}") """








""" class Moto:
    def __init__(self, marca, modelo, matricula, km_actual):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km_actual = km_actual
        self.km_final = km_actual
    
    def registrar_km_salida(self):
        return f"La moto antes de ser alquilada tenia {self.km_actual}km"
    
    def registrar_km_llegada(self, km_final):
        if km_final < self.km_actual:
            return "El kilometraje final no puede ser al kilometraje actual"
        else:
            self.km_final = km_final
    
    def mostrar_datos(self):
        return self.__dict__

marca = input("Ingresa la marca de la moto: ")
modelo = input("Ingresa el modelo de la moto: ")
matricula = input("Ingrese la matricula de la moto: ")
km_actual = float(input("Ingrese el kilometraje de la moto: "))

moto = Moto(marca, modelo, matricula, km_actual)

moto.registrar_km_salida()

km_final = float(input("Ingresa el kilometraje final: "))
moto.registrar_km_llegada(km_final)

print(f"{moto.mostrar_datos()}") """




















































































""" 
class Camion:
    def __init__(self, marca, matricula, km_inicio, km_fin):
        self.marca = marca
        self.matricula = matricula
        self.km_inicio = km_inicio
        self.km_fin = km_fin
    
    def km_inicial(self):
        return f"El kilometrage incial del camion es de {self.km_inicio}km"
    
    def km_final(self):
        if self.km_fin < self.km_inicio:
            return "El kilometraje final no puede ser inferior al incial"
        else:
            self.km_fin = self.km_fin
    
    def mostrar_datos(self):
        return self.__dict__


marca = input("Ingresa el nombre de la marca: ")
matricula = input("Ingresa la matricula: ")
km_inicio = int(input("Ingresa los km del inicio: "))
km_fin = int(input("Ingresa los km finales: "))

camion = Camion(marca, matricula, km_inicio, km_fin)
camion.km_inicial()
camion.km_final()

print(f"{camion.mostrar_datos()}") """







""" class Alumno:
    def __init__(self, nombre, edad):
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
        return f"Nombre: {self.nombre} || Edad: {self.edad}"
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

estudiante = Alumno(nombre, edad)

print(f"{estudiante.mostrar()}")
print(f"{estudiante.es_mayor_de_edad()}") """


















class Persona:
    def __init__(self, nombre, edad):
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
    





