class Pedido:
    def __init__(self, numero_pedido, nombre_cliente, lista_productos, importe_total):
        self.numero_pedido = numero_pedido
        self.cliente = nombre_cliente
        self.productos = lista_productos
        self.importe_total = importe_total
    
    def calcular_pedido_con_iva(self):
        iva = self.importe_total * 0.21
        return self.importe_total + iva
    
    def resumen_pedido(self):
        return (f"Número de pedido: {self.numero_pedido} || Cliente: {self.cliente} || Productos: {', '.join(self.productos)} || Importe total (sin IVA): {self.importe_total:.2f}€ || Importe total (con IVA): {self.calcular_pedido_con_iva():.2f}€\n")    

pedidos = []

while True:
    print("\n***GESTOR DE PEDIDOS***")

    print("1- Crear un nuevo pedido")
    print("2- Resumen total de los pedidos")
    print("3- Salir")

    opcion_menu = int(input("\nIngresa una opcion del menu: "))

    if (opcion_menu == 1):
        numero_pedido = input("\nIngresa el número de pedido: ")
        nombre_cliente = input("Ingresa el nombre del cliente: ")

        lista_productos = []
        while True:
            producto = input("Ingresa el nombre de un producto o 'fin' para terminar: ")
            if producto.lower() == 'fin':
                break
            lista_productos.append(producto)

        importe_total = float(input("Ingresa el importe total del pedido (sin IVA): "))

        pedido = Pedido(numero_pedido, nombre_cliente, lista_productos, importe_total)
        pedidos.append(pedido)
        print("Pedido creado correctamente.")
        continue

    elif (opcion_menu == 2):
        print("\nResumen de todos los pedidos:")
        for pedido in pedidos:
            print(pedido.resumen_pedido())
        continue

    elif (opcion_menu == 3):
        print("Saliendo del gestor de pedidos")
        break

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
        continue