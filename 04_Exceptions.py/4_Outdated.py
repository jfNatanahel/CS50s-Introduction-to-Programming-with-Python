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
mes=[
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
#Pedir usuario fecha en formato mes-dia-año . Donde el mes debe corresponder alguno de la list.
#Mostrar en formato YYYY-MM-DD (completar con ceros)
while True:
    fecha=input("ingresar fecha en formato: mes/dia/año ")
#Errores
    mes,dia,año=fecha.split()