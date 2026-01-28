class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def consultar_saldo(self):
        return self.saldo
    
    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Se han ingresado {cantidad:.2f}€. Nuevo saldo: {self.saldo:.2f}€"
        else:
            return "La cantidad a ingresar debe ser positiva."
    
    def retirar_dinero(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Se han retirado {cantidad:.2f}€. Nuevo saldo: {self.saldo:.2f}€"
            else:
                return "No hay suficiente saldo para realizar la retirada."
        else:
            return "La cantidad a retirar debe ser positiva."
    

cuentaBancaria = CuentaBancaria("Juan", 1000)

while True:
    print("\n***Cajero automatico***")

    print("1- Consultar saldo")
    print("2- Ingresar dinero")
    print("3- Retirar dinero")
    print("4- Salir")

    opcion_menu = int(input("\nIngresa una opcion del menu: "))

    if (opcion_menu == 1):
        print(f"\nEl saldo actual es: {cuentaBancaria.consultar_saldo():.2f}€")
        continue

    elif (opcion_menu == 2):
        cantidad = float(input("\nIngresa la cantidad que deseas ingresar: "))

        cuentaBancaria.ingresar_dinero(cantidad)
        print(f"Has ingresado un total de {cantidad:.2f}€. Tu saldo actual es de {cuentaBancaria.consultar_saldo():.2f}€")
        continue

    elif (opcion_menu == 3):
        cantidad = float(input("\nIngresa la cantidad que deseas retirar: "))

        resultado_retiro = cuentaBancaria.retirar_dinero(cantidad)
        print(resultado_retiro)
        continue

    elif (opcion_menu == 4):
        print("Saliendo del cajero automatico")
        break

    else:
        print("Opcion no valida, por favor ingresa una opcion del menu.")
        continue