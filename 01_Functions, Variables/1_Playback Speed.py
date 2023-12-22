#Velocidad de Reproduccion
"""
Algunas personas tienen la costumbre de dar conferencias hablando bastante rápido, 
y sería bueno reducirlas, como la velocidad de reproducción de 0,75 de YouTube, o 
incluso hacerles pausas entre palabras.

En un archivo llamado playback.py, implemente un programa en Python que solicite al
usuario una entrada y luego genere esa misma entrada, reemplazando cada espacio con
...(es decir, tres puntos).
"""
name = input("What's your name? ")
reemplazando=name.replace(" ","...")
print(reemplazando)

#¿Que es replace?
"""replace es un método en Python que se utiliza para reemplazar una subcadena con otra
en una cadena dada. Este método pertenece al tipo de datos de cadena (str)"""
#¿Sintaxis?
"""entrada_reemplazada = entrada.replace(" ", "...")"""
#Explicacion:
"""
-El primer argumento " " es la subcadena que se busca en entrada para ser reemplazada.
-El segundo argumento "..." es la cadena con la que se reemplazará cada ocurrencia de 
la subcadena encontrada."""
