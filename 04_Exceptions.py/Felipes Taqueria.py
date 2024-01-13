"""
Tiene un diccionario donde el valor de cada lalve es un precio en dolares.
{

}
implementar un programa que permita a un usuario realizar un pedido, solicitandole articulos, uno por linea, hasta que el usuario
ingrese control -d(que es una forma comun de finalizar la entrada a un programa). Despues de cada articulo ingresado, muestre el 
costo total de todos los articulos ingresados hasta el momento, con el prefijo de un signo de dolar($) y con formato de dos decimales. 
Trate el caso de entrada del usuario sin sensibilidad. Ignore cualquier entrada que no sea un elemento. Supongamos que cada elemento 
del menu tendra un titulo."""


#Solicitar articulos (dentro de un ciclo)
#El ciclo termina cuando ingrese control -d
#Mostrar el costo total de todos los articulos (+) -- 1.Con el signo dolar y con formato de dos decimales.

menu={
    "Baja Taco":4.24,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 9.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
costo_total=0
while True:
    articulos=input("ingresar articulos a comprar: ")
    if articulos.lower()=="control -d":
        break
    else:
        try:
            costo_total=costo_total+menu[articulos.title()] #No es necesario un ciclo for.
            print("Costo total hasta el momento: ${:.2f}".format(costo_total))
        except KeyError:
            print("Artículo no encontrado en el menú. Por favor, ingrese un artículo válido.")

print("Costo total: ${:.2f}".format(costo_total))

