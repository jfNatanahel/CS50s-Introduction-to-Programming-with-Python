#Obsoleto
"""
Afortunadamente, las computadoras tienden a usar ISO 8601 , un estándar internacional que prescribe que las
fechas deben formatearse en orden año-mes-día (AAAA-MM-DD), sin importar el país, formateando años con cua-
tro dígitos, meses con dos dígitos, y días con dos dígitos, “rellenando” cada uno con ceros a la izquierda
según sea necesario.

En un archivo llamado outdated.py, implemente un programa que solicite al usuario una fecha, anno Domini , 
en orden mes-día-año, con formato como 9/8/1636 o September 8, 1636, donde el mes en este último podría ser 
cualquiera de los valores a continuación list:

Luego envíe esa misma fecha en YYYY-MM-DD formato. Si la entrada del usuario no es una fecha válida en nin-
guno de los formatos, pregunte al usuario nuevamente. Supongamos que cada mes no tiene más de 31 días; no 
es necesario validar si un mes tiene 28, 29, 30 o 31 días."""

#Pedir usuario fecha en formato mes-dia-año . Donde el mes debe corresponder alguno de la list.
#Mostrar en formato YYYY-MM-DD (completar con ceros)
def main():
    entrada_usuario=algoritmo()

def algoritmo():
    while True:
        try:
            fecha=input("ingresar fecha en formato: mes/dia/año ")
            if "/" in fecha:
                mes,dia,año=fecha.split("/")
            else:
                mes,dia,año=fecha.split(" ")

            # Verificar si el mes está en la lista usando index
            mes_index = meses.index(mes)

        #el mes no se encuentra en la lista.
        except ValueError:
            print("Error: Mes no válido. Intente nuevamente.")

            # Si llegamos aquí, la entrada fue válida, podemos salir del bucle
            #break


    return print("hola")
main()
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