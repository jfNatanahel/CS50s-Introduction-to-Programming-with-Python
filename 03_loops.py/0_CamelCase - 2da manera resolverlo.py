lista = []
nueva_lista = []

camel_case = str(input("camelCase: "))
lista.append(camel_case)

#Con un solo ciclo for.
for letra in lista[0]:
    if letra.istitle():  # Mayúscula
        if nueva_lista:  # Verifica si nueva_lista no está vacía
            nueva_lista.append("_")
        nueva_lista.append(letra.lower())
    else:
        nueva_lista.append(letra)

print("".join(nueva_lista))
