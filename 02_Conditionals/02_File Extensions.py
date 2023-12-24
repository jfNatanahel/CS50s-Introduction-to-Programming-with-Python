"""
En un archivo llamado extensions.py, implemente un programa que solicite al usuario 
el nombre de un archivo y luego genere el tipo de medio de ese archivo si el nombre 
del archivo termina, sin distinguir entre mayúsculas y minúsculas, en cualquiera de 
estos sufijos:
.gif = image/gif
.jpg = image/jpeg
.jpeg = image/jpeg
.png = image/png
.pdf = application/pdf
.txt = text/plain
.zip = application/zip
Si el nombre del archivo termina con algún otro sufijo o no tiene ningún sufijo, se 
genera application/octet-streamen su lugar, que es un valor predeterminado común.
"""

#Solicitar al usuario el nombre de un archivo.
nombre_archivo=str(input("Ingresar el nombre del archivo son su sufijo:  ")).lower().strip()

#Separar en dos para obtener los resultados.
separacion=nombre_archivo.split(".")
tamaño_lista=len(separacion)

#Si el tamaño de la lista es 1 quiere decir que no puso el prefijo.
if tamaño_lista==1:
    print("application/octet-streamen")

#Si no imprimimos dependiendo del resultado.
else:
    if separacion[1] == "gif":
        print("image/gif")
    elif separacion[1]=="jpeg" or separacion[1]=="jpg":
        print("image/jpeg")
    elif separacion[1]=="png":
        print("image/png")
    elif separacion[1]=="pdf":
        print("application/pdf")
    elif separacion[1]=="txt":
        print("text/plain")
    elif separacion[1]=="zip":
        print("application/zip")

    
