#Pensamiento profundo
"""
implemente un programa que solicite al usuario la respuesta a la Gran Pregunta de la Vida, el Universo y Todo, generando Yessi el 
usuario ingresa 42o (sin distinguir entre mayúsculas y minúsculas) forty-twoo forty two. De lo contrario, salida No."""

#ingresar el numero. La funcion .lower es para convertir en minusculas
pregunta=str(input("¿Cuál es la respuesta a la gran pregunta de la vida, el universo y todo?: ")).lower

#Verificar si la respuesta del usuario es correcta
if pregunta=="42" or pregunta=="cuarenta y dos":
    print("yes")
else:
    print("No")