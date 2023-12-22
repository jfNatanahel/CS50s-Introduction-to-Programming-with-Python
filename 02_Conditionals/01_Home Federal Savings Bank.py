#Inicio Caja Federal de Ahorros
"""
En un archivo llamado bank.py, implemente un programa que solicite un saludo al usuario. Si el saludo comienza con "hola", envíe $0. 
Si el saludo comienza con una “h” (pero no “hola”), envíe $20. De lo contrario, genere $100. Ignore cualquier espacio en blanco inicial
en el saludo del usuario y trate el saludo del usuario sin distinguir entre mayúsculas y minúsculas.
"""
saludo=input("Ingresar saludo: ")
if saludo == "hola":
    print("$0")
elif saludo in "h":
    print("$20")

else:
    print("$100")