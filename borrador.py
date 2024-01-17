meses=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
"""while True:
        try:
            fecha=str(input("ingresar fecha en formato: mes/dia/año ")).title()
            if "/" in fecha:
                mes,dia,año=fecha.split("/")
            else:
                mes,dia,año=fecha.split(" ")

            print("variable",mes)

            # Verificar si el mes está en la lista usando index
            mes_index = meses.index(mes)
            print("index",mes_index)

        #el mes no se encuentra en la lista.
        except ValueError:
            print("Error: Mes no válido. Intente nuevamente.")"""


fecha=input("ingresar fecha en formato: mes/dia/año ").title()
if "/" in fecha:
    mes,dia,año=fecha.split("/")
else:
    mes,dia,año=fecha.split(" ")
for i in meses:
    if i==mes:
        print("Encontrado")
    else:
        print("Elemento no encontrado")