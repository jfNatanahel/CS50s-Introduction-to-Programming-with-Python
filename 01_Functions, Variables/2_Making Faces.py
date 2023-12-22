#Haciendo caras
"""
implemente una función llamada convert que acepte a str como entrada y devuelva esa misma entrada con cualquier :)convertido a 🙂
(también conocido como una cara ligeramente sonriente ) y cualquier :(convertido a 🙁(también conocido como una cara ligeramente
fruncida ). El resto del texto debe devolverse sin cambios.
"""
def convert(text):
    resultado=text.replace(":)","🙂").replace(":(","🙁")
    return resultado
palabra=str(input("Cara??: "))
mostrar=convert(palabra)
print(mostrar)