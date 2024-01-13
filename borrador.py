menu = {
    "Baja Taco": 4.24,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 9.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

costo_total = 0

while True:
    articulo = input("Ingresar artículo a comprar: ")
    
    if articulo.lower() == "control -d":
        break
    else:
        try:
            costo_total += menu[articulo.title()]
            print("Costo total hasta el momento: ${:.2f}".format(costo_total))
        except KeyError:
            print("Artículo no encontrado en el menú. Por favor, ingrese un artículo válido.")

print("Costo total de la orden: ${:.2f}".format(costo_total))
