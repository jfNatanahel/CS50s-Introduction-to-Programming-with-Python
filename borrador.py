lista_compras = {}

while True:
    elementos = str(input("Elemento: "))
    
    if elementos.lower() == "control -d":
        break

    # Verificar si el elemento ya está en la lista
    if elementos.title() in lista_compras:
        lista_compras[elementos.title()] += 1
    else:
        # Si no está en la lista, agregarlo con valor 1
        lista_compras[elementos.title()] = 1

print(lista_compras)
