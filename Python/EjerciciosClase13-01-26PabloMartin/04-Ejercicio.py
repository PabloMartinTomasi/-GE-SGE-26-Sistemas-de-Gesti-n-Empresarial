capitalInicial = float(input("Ingresa el capital inicial: "))
interesAnual = float(input("Ingresa el interés anual (en %): "))
anios = int(input("Ingresa el número de años: "))

montoFinal = capitalInicial * (1 + interesAnual/100) ** anios

print(f"El monto final es de: {montoFinal}€")