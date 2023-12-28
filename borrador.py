# Monedas aceptadas:
monedas_aceptadas = [25, 10, 5]
print("Monedas aceptadas: $25, $10, $5")

moneda_inicial = 50
while moneda_inicial > 0:
    # Usuario inserta una moneda.
    moneda_usuario = int(input("Insertar una moneda: "))
    if moneda_usuario in monedas_aceptadas:  # La moneda se encuentra en la lista
        print("Monto adeudado:", moneda_inicial)
        moneda_inicial -= moneda_usuario  # Operaciones para su vuelto.
        print("Vuelto restante:", moneda_inicial)
    else:  # La moneda no se encuentra en la lista
        print("Moneda no válida. Monto adeudado:", moneda_inicial)

# Imprimir el cambio al usuario
print("¡Gracias por su compra! Su cambio es de", abs(moneda_inicial), "centavos.")
