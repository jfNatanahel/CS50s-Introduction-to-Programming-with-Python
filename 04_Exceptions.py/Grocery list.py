#####-> LISTA DE COMPRAS <-#####
"""
Suponga que tiene la costumbre de hacer una lista de los articulos que necesita en el supermcado.
Solicitar elementos al usuario, uno por linea, hasta que el usuario ingrese control-d. Luege genere la lista de compras del usuario en
mayusculas, ordenadas alfabeticamente por articulo, anteponiendo cada linea con el numero de veces que el usuario ingreso ese articulo.
No es necesario pluralizar los elementos. Trate la entrada del usuario sin distinguir entre mayusculas o minusculas."""


#Entrada del usuario.
lista_compras={}
while True:
    elementos=str(input("elementos: "))
    if elementos.lower()=="control -d":
        break
    lista_compras[elementos.title()]=lista_compras.get(elementos,0)+1
print(lista_compras)