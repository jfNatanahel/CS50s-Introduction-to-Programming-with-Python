import re

def es_fecha_valida(fecha):
    # Verificar si la fecha tiene un formato válido
    patron_fecha1 = re.compile(r"\d{1,2}/\d{1,2}/\d{4}")
    patron_fecha2 = re.compile(r"[a-zA-Z]+\s\d{1,2},\s\d{4}")

    if patron_fecha1.match(fecha) or patron_fecha2.match(fecha):
        return True
    else:
        return False

def convertir_a_YYYY_MM_DD(fecha):
    # Convertir la fecha a formato YYYY-MM-DD
    meses = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    if "/" in fecha:
        mes, dia, año = fecha.split("/")
    else:
        mes, dia, año = re.findall(r"([a-zA-Z]+) (\d{1,2}), (\d{4})", fecha)[0]

    numero_mes = meses.get(mes)
    dia_str = str(dia).zfill(2)

    return f"{año}-{numero_mes}-{dia_str}"

def main():
    while True:
        fecha = input("Ingrese una fecha en formato mes-día-año: ").title()

        if es_fecha_valida(fecha):
            fecha_convertida = convertir_a_YYYY_MM_DD(fecha)
            print(f"Fecha convertida: {fecha_convertida}")
            break
        else:
            print("Fecha no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    main()
