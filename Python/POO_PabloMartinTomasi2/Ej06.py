"""Sistema de control de inventario de una tienda.
Crea una clase Articulo con nombre, stock y precio.
Usa condicionales para avisar cuando el stock sea bajo.
Permite actualizar el stock mediante un bucle de opciones.
El usuario debe insertar los datos por consola."""

class Gestor:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def actualizar_stock(self, stock):
        self.stock = stock
    
    def stock_bajo(self):
        if self.stock < 5:
            return f"El producto {self.nombre}, tiene un stock de {self.stock}"



productos = []


while True:
    print("***GESTOR DE PRODUCTOS")
    print("1- Registrar producto nuevo")
    print("2- Actualizar stock")
    print("3- Mostrar productos con stock bajo")
    print("4- Salir")

    opcion_menu = int(input("\nIngresa una opcion del menu: "))

    if (opcion_menu == 1):
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        stock = int(input("Ingresa el stock del producto: "))

        producto = Gestor(nombre, precio, stock)
        productos.append(producto)
        continue
    
    elif (opcion_menu == 2):
        nombre = input("Ingresa el nombre del producto para poder actualizar el stock: ")
        stock = int(input("Ingresa el nuevo stock del producto: "))

        encontrado = False
        for producto in productos:
            producto.actualizar_stock(stock)
            print("El stock ha sido actualizado correctamente")
            encontrado = True
            break

        continue
    
    elif (opcion_menu == 3):
        for producto in productos:
            if producto.stock_bajo():
                print(f"{producto.nombre} - Stock: {producto.stock}")
    
    elif opcion_menu == 4:
        print("Saliendo del gestor de productos")
        break

    else:
        print("Escoje una opcion del menu")
        break
