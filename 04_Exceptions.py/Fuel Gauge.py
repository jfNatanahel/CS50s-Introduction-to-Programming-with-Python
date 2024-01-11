"""
Implemente un programa que se solicite al usuario una fracción, formateada como X/Y, donde cada uno de los
X y Y sean un numero entero, y luego genere como un porcentaje redondeado al entero mas cercano, cuanto
combustible hay en el tanque. Sin embargo, si queda 1% o menos, la salida E indica que el tanque esta prac-
ticamente vacio. Y si queda 99% o mas, la salida F indica que el tanque esta esencialmente lleno.

Si X o Y no es un numero entero y X es mayor que Y o Y es 0, pregunte al usuario nuevamente. Debo detectar
excepciones como ValueError o ZeroDivisionError"""

def principal_nafta():
    fraccion=(secundaria_calculos)

def secundaria_calculos(calculos):
    calculos=int(input("Fraccion(X/Y): "))
    x,y=calculos.split("/")
    porcentaje=x/y.round()*100
    while True:
        try:
        except ValueError:
            print("Error")
        except ZeroDivisionError:
            print("Error")
        else:
            break
    return porcentaje

main()

#Solicitar al usuario una fraccion:
#Generar un porcentaje redondeado al entero mas cercano.
#Si queda 1% -> E
#Si queda 99% o mas -> F 
