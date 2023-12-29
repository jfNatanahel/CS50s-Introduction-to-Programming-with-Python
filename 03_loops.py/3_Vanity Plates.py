"""
En Massachusetts, sede de la Universidad de Harvard, es posible solicitar una matrícula
personalizada para su automóvil, con su elección de letras y números en lugar de números 
aleatorios. Sin embargo, entre los requisitos se encuentran:

1)"Todos los platos personalizados deben comenzar con al menos dos letras".

2)“… los platos personalizados pueden contener un máximo de 6 caracteres (letras o números)
y un mínimo de 2 caracteres”.

3)“Los números no se pueden utilizar en medio de un plato; deben llegar al final. Por ejemplo,
AAA222 sería un plato de tocador aceptable...; AAA22A no sería aceptable."El primer número , 
utilizado no puede ser un '0'”.

4)"No se permiten puntos, espacios ni signos de puntuación".

En plates.py, implemente un programa que solicite al usuario un plato de tocador y luego gene-
re Valid si cumple con todos los requisitos o Invalidno. Supongamos que todas las letras en la 
entrada del usuario estarán en mayúsculas. Estructura tu programa según lo siguiente, donde 
is_validregresa Truesi scumple con todos los requisitos y Falsesi no los cumple.Supongamos que
 sserá un str. Le invitamos a implementar funciones adicionales para is_validllamar (por ejemplo, una función por requisito).
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        tiene_dos_letras(s) and maximo_minimo_caracteres(s) and 
        tercera_condicion(s) and caracteres_especiales(s) ) 

#1
def tiene_dos_letras(s):
    return s[0:2].isalpha()

#2
def maximo_minimo_caracteres(s):
    return 2<= len(s) <=6

#3
def tercera_condicion(s):
    return s[1:-1].isalpha() and s[0].isalpha() and s[0]!="0"

#4
def caracteres_especiales(s):
    return all(c.isalpha() for c in s)
main()


###########################--->EXPLICACION<---###########################
#4
"""
recorre un ciclo for sobre cada caracter de la palabra (for c in s) y pregunta si cada palabra es un 
caracter alfanumerico devolvera un valor booleano True o False. no debe tener ningun caracter especial
entonces decimos que si (all) todos los elementos son True quiere decir son alfanumericos."""
