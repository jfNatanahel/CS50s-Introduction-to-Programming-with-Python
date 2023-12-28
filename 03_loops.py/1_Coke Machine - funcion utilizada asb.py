#Máquina de coque
"""
Supongamos que una máquina vende botellas de Coca-Cola (Coca-Cola) a 50 céntimos y sólo acepta monedas de 
estas denominaciones: 25 céntimos, 10 céntimos y 5 céntimos.

En un archivo llamado coke.py, implemente un programa que solicite al usuario que inserte una moneda, una 
a la vez, informándole cada vez el monto adeudado. Una vez que el usuario haya ingresado al menos 50 
centavos, indique cuántos centavos de cambio se le deben al usuario. Supongamos que el usuario solo 
ingresará números enteros e ignorará cualquier número entero que no sea una denominación aceptada.
"""
#Monedas aceptadas:
monedas_aceptadas=[25,10,5]
print("Monedas aceptadas: $25 , $ 10 , $5")

moneda_inicial=50
while moneda_inicial>0:
    #Usuario inserte una moneda.
    moneda_usuario=int(input("Insertar una moneda: "))
    if moneda_usuario in monedas_aceptadas: #La moneda se encuentra en la lista   
        print("Moneda adeudado:", moneda_inicial)   
        moneda_inicial=moneda_inicial-moneda_usuario #Operaciones para su vuelto.
        print("Vuelto restante:", moneda_inicial)
    else: #La moneda no se encuentra en la lista
        print("Moneda no valida. Monto adecuado:",moneda_inicial)

#Imprimir el cambio al usuario
print("¡Gracias por su compra! su cambio es de", abs(moneda_inicial))

###-> FUNCION <-###
#Abs= obtener el valor absoluto de un nmero.