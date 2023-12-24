#Interpetre matematico
"""
implemente un programa que solicite al usuario una expresión aritmética y luego calcule y genere el 
resultado como un valor de punto flotante formateado con un decimal. Supongamos que la entrada del 
usuario tendrá el formato x y z, con un espacio entre x y y un espacio entre y y z, donde:
-x: es un numero entero
-y: es +, -, *, o/
-z: es un numero entero
Por ejemplo, si el usuario ingresa 1 + 1, su programa debería generar 2.0. Supongamos que, si yes /, 
entonces z no lo será 0.


Tenga en cuenta que, así como pythonél mismo es un intérprete de Python, ¡también lo será usted interpreter.pyun intérprete de matemáticas!
"""
expresion_matematica=str(input("Ingresar una expresion Aritmetica: "))
x,y,z=expresion_matematica.split(" ")
print(x)
print(y)
print(z)