def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = round(dollars * percent, 2)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Elimina el símbolo "$" y convierte la cadena a float
    cantidad = float(d[1:])
    return cantidad


def percent_to_float(p):
    # Elimina el símbolo "%" y convierte la cadena a float
    porcentaje = float(p[:-1]) /100
    return porcentaje


main()
