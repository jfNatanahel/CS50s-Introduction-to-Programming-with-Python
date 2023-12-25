#Hora de comer
"""
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar entre las
12:00 y las 13:00 y cenar entre las 18:00 y las 19:00. ¿No sería bueno si tuvieras un programa que pudiera 
decirte qué comer y cuándo?

En meal.py, implemente un programa que solicite al usuario una hora y genere si es breakfast time, lunch 
timeo dinner time. Si no es hora de comer, no saques nada. Supongamos que la entrada del usuario se forma-
teará en formato de 24 horas como #:## o ##:##. Y suponga que el rango de tiempo de cada comida es inclusivo. 
Por ejemplo, ya sean las 7:00, 7:01, 7:59 u 8:00, o en cualquier momento intermedio, es hora de desayunar.

Estructura tu programa según lo siguiente, donde convert hay una función (que puede ser llamada por main) que
convierte time, stren formato de 24 horas, al número correspondiente de horas como float. Por ejemplo, dado 
un time Me gusta "7:30"(es decir, 7 horas y 30 minutos), convert debería devolver 7.5(es decir, 7,5 horas).

"""
#Desafio
#Si está preparado para un desafío, opcionalmente agregue soporte para tiempos de 12 horas, lo que permite al
#usuario ingresar tiempos también en estos formatos:
#:## a.m. y ##:## a.m.
#:## p.m. y ##:## p.m.

def main():
    hora_usuario=str(input("Ingresar hora en formato 24 horas: "))
    resultado=convert(hora_usuario)


def convert(time): #Convertir en float 
    hora , minutos=time.split(":")
#En vez de pasar a float podria hacer: hora, minutos=map(int,time.split(":")) mapea y los convierte en enteros.
    tiempo_decimal=float(hora)+float(minutos)/60
    hora , minutos= int(hora) , int(minutos)

#Condiciones para los horarios
    if hora>=7 and hora <=8 and minutos <=59:
        print("BREAKFAST TIME, DESAYUNAR")
    elif  hora>=12 and hora <=13 and minutos <=59:
        print("LUNCH BETWEEN, ALMORZAR ")
    elif hora>=18 and hora <=19 and minutos <=59:
        print("DINNER BETWEEN, CENAR")
    else:
        print(" ")
    
if __name__ == "__main__":
    main()