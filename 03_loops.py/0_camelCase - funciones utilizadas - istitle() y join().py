#el caso de Carmel
"""
Python, por el contrario, recomienda el caso de serpiente , donde las palabras están separadas por guiones 
bajos ( _), con todas las letras en minúsculas. Por ejemplo, esas mismas variables se llamarían name, 
first_namey preferred_first_name, respectivamente, en Python.

En un archivo llamado camel.py, implemente un programa que solicite al usuario el nombre de una variable en
caso de camello y genere el nombre correspondiente en caso de serpiente. Supongamos que la entrada del usua-
rio será en formato camello.
"""
lista=[]
nueva_lista=[]
camel_case=str(input("camelCase: "))
lista.append(camel_case)
for palabra in lista:
    for letra in palabra:
        if letra.istitle(): #Mayuscula
            if nueva_lista: #Verificar si la lista no esta vacia.
                nueva_lista.append("_")
            nueva_lista.append(letra)

        else:
            nueva_lista.append(letra)

print("".join(nueva_lista).lower())
#####-> FUNCIONES UTILIZADAS <-#####
"""
.istitle()=Devuelve True si la cadena es una cadena con título en mayúsculas y hay al menos un carácter  ; 
por ejemplo, los caracteres en mayúsculas solo pueden seguir a los caracteres sin mayúsculas y los carac-
teres en minúsculas solo a los que están en mayúsculas. Devolver False en caso contrario.

El método str.join(iterable)  es usado para unir todos los elementos de un iterable con un espefico string
str in Python. Si, el iterable no contiene ningún valor en los strings, Esto conduce a un TypeError exception.

iterable: Todos los iterables de un string. Podrian ser listas, tuplas de strings o un string plano.
Ejemplos
Concatena la lista de strings con ":"

print(":".join(["freeCodeCamp", "es", "divertido"]))
freeCodeCamp:es:divertido
"""