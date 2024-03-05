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

#guia
#1)Hacer un ciclo hasta que el usuario ingrese en el formato correcto la fecha.
#2)Pedir usuario fecha en formato mes-dia-año . Donde el mes debe corresponder alguno de la list.
#3)Identificar cual de los dos formatos es: 1->"5-23-2004" or 2-> September 8, 1636??
#3)El mes se encuentra en la lista??? comprobar con un index. Si no se encuentra volver a ingresar fecha.
#4)Lograr identificarlos por - o ,
#5) if se encuentran "-" -> separlos con un split en las variables mes,dia,año=...
#6) else significa se encuentra una "," -> separlos con un split...
#7)Agregar a la variable mes los 0 correspondientes. 

#Mostrar en formato YYYY-MM-DD (completar con ceros)
meses=[
    "January", "February",  "March", 
    "April",    "May",      "June",
    "July",     "August",   "September", 
    "October",  "November", "December"
]




    
   

