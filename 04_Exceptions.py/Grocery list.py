#####-> LISTA DE COMPRAS <-#####
"""
Suponga que tiene la costumbre de hacer una lista de los articulos que necesita en el supermcado...
Solicitar elementos al usuario, uno por linea, hasta que el usuario ingrese control-d. Luege genere 
la lista de compras del usuario en mayusculas, ordenadas alfabeticamente por articulo, anteponiendo
cada linea con el numero de veces que el usuario ingreso ese articulo. No es necesario pluralizar los
elementos. Trate la entrada del usuario sin distinguir entre mayusculas o minusculas."""


#Entrada del usuario.
lista_compras={}
while True:
    elementos=str(input("elementos: "))
    if elementos.lower()=="control -d":
        break
    
#Verificar si el elemento esta en el dic
    if elementos.title() in lista_compras:
        lista_compras[elementos.title()]+=1

#Si no se encuentra agregarlo, con el valor 1.
    else:
        lista_compras[elementos.title()]=1

#Ordenar la lista alfabeticamente
#items= crear una tupla
lista_ordenada=dict(sorted(lista_compras.items()))    

#Otra manera de recorrer un dict.
for keys,value in lista_ordenada.items():
   print(f"{value} {keys}")