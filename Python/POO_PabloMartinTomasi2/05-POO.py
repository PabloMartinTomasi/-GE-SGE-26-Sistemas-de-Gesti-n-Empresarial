"""
Representa un cuenta bancaria con deposito y 
retiro. Debe de haber un titular y un sueldo. Utiliza POO
"""

class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso: {cantidad:.2f}€. Saldo actual: {self.saldo:.2f}€"
        else:
            return "La cantidad a depositar debe ser positiva"
    
    def retiro(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Retiro exitoso: {cantidad:.2f}€. Saldo actual: {self.saldo:.2f}€"
            else:
                return "Saldo insuficiente para el retiro"
        else:
            return "La cantidad a retirar debe ser positiva"
    
    def mostrar(self):
        print(self.__dict__)



nombre = input("Ingrese el nombre del titular de la cuenta: ")
saldo = float(input("Ingrese el saldo inicial de la cuenta: "))

cuenta1 = Cuenta(nombre, saldo)
cuenta1.mostrar()
cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
print(cuenta1.depositar(cantidad_deposito))
cuenta1.mostrar()
cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
print(cuenta1.retiro(cantidad_retiro))
cuenta1.mostrar()