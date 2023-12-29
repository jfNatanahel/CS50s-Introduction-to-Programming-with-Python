#Solo arreglando mi twttr
"""
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar
tiempo o espacio, como omitiendo vocales, de forma muy parecida a como Twitter se 
llamaba originalmente twttr . En un archivo llamado twttr.py, implemente un programa
que solicite al usuario un str texto y luego genere ese mismo texto pero con todas las
vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.
"""
vocales=["A","E","I","O","U"]
texto=str(input("texto: ")).upper()
for vocal in vocales: #Recorro list vocales.
    texto=texto.replace(vocal,"") #vocal que se encuentra en el texto = ""
print(texto)