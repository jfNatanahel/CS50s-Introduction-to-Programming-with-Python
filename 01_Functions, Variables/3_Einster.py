#Einstein E=mc(cuadrado)
"""
Incluso si no has estudiado física (¡recientemente o nunca!), es posible que hayas oído eso , donde representa energía (medida en julios), M
representa la masa (medida en kilogramos), y C representa la velocidad de la luz (medida aproximadamente como 300000000 metros por segundo),
según Albert Einstein et al. Básicamente, la fórmula significa que masa y energía son equivalentes.

En un archivo llamado einstein.py, implemente un programa en Python que solicite al usuario la masa como un número entero (en kilogramos) 
y luego genere el número equivalente de julios como un número entero. Supongamos que el usuario ingresará un número entero.

Consejos

"""
def formula(masa):
    resultado=masa*300000000**2
    return resultado
entrada=int(input("ingresar masa (kilogramos): "))
imprimir=formula(entrada)
print(imprimir)