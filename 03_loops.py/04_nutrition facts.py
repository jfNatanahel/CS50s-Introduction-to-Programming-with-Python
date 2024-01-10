"""
implementar un programa que solicita a los consumidores que ingresen una fruta (sin
distinguir entre mayusculas y minusculas) y luego genera la cantidad de calorias en
una porcion de esa fruta, segun el cartel de frutas de la FDA, que tambien esta dis-
ponible en texto. Dejando a un lado las mayusculas, suponga que los usuarios ingresan
frutas exactamente como esta escrito en el cartel (por ejemplo, strawberries no 
strawberry). Ignora cualquier entrada que no sea una fruta.
"""
#Crear un diccionario segun el cartel de frutas de la FDA
frutas_fda={
    "APPLE":130 , "AVOCADO":50 , "BANANA":110 , "CANTALOUPE":50 , "GRAPEFUIT":60 ,
    "GRAPES":90 , "HONEYDEW MELON":50 , "KIWIFRUIT":90 , "LEMON":15 , "LIME":20 , 
    "NECTARINE":60 , "ORANGE":80 , "PEACH":60 , "PEAR":100 , "PINEAPPLE":50 , 
    "PLUMS":70 , "STRAWBERRIES":50 , "SWEET CHERRIES":100 , "TANGERINE":50 ,
    "WATERMELON":80
}

#Entrada del usuario.
fruta=str(input("Ingresar una fruta: ")).upper()

#Recorrer el dic.
for frutas in frutas_fda:

#Si la entrada del usuario se encuentra en el dic mostrar el valor.
    if fruta == frutas:
        print(frutas_fda[frutas])