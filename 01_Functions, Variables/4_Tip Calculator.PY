#Calculadora de propinas
"""
En los Estados Unidos, es costumbre dejar una propina al camarero después de cenar en un restaurante, normalmente una cantidad 
equivalente al 15% o más del coste de la comida. Pero no te preocupes, ¡hemos escrito una calculadora de propinas para ti a continuación!
Bueno, hemos escrito la mayor parte de una calculadora de propinas para usted. Desafortunadamente, no tuvimos tiempo de implementar dos 
funciones:

-dollars_to_float, que debería aceptar un strcomo entrada (formateado como $##.##, donde cada uno # es un dígito decimal), 
eliminar el inicial $ y devolver la cantidad como un float. Por ejemplo, dado $50.00como entrada, debería devolver 50.0.

-percent_to_float, que debería aceptar a strcomo entrada (formateado como ##%, donde cada uno #es un dígito decimal), elimi-
nar el final % y devolver el porcentaje como float. Por ejemplo, dado 15%como entrada, debería devolver 0.15.

Supongamos que el usuario ingresará valores en los formatos esperados. """
def main():
    dollars = float(dollars_to_float(input("How much was the meal? ")))
    percent = float(percent_to_float(input("What percentage would you like to tip? ")))
    tip = round(dollars * percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    borrar=d.replace("$","")
    
    return d,borrar


def percent_to_float(p):
    borrar2=p.replace("%","")
    #float(percent_to_float)
    return p,borrar2


main()
