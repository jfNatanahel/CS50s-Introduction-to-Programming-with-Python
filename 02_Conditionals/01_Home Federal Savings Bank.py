#Inicio Caja Federal de Ahorros
"""
En un archivo llamado bank.py, implemente un programa que solicite un saludo al usuario. Si el saludo comienza con "hola", envíe $0. 
Si el saludo comienza con una “h” (pero no “hola”), envíe $20. De lo contrario, genere $100. Ignore cualquier espacio en blanco inicial
en el saludo del usuario y trate el saludo del usuario sin distinguir entre mayúsculas y minúsculas.
"""
saludo=str(input("Ingresar saludo: ")).lower()

#1er condicion es igual a "hola"=$0
if saludo =="hola":
    print("$0")

#Si el saludo es distinto de todos mostrar $100
elif saludo.startswith("h"):
    print("$20")

#Si el saludo comienza con una "h" distinto de hola muestra $20
else: 
    print("$100")


#### FUNCION NUEVA!! UTILIZADA ####
#sintaxis= str.startswith(prefix[, start[, end]])
"""Devuelve Verdadero si la cadena comienza con el prefijo; de lo contrario, devuelve Falso. El prefijo también puede ser una tupla de 
prefijos a buscar. Con inicio opcional, pruebe la cadena comenzando en esa posición. Con el final opcional, deje de comparar cadenas 
en esa posición."""




