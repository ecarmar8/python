#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que 
# deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
# y calcule el peso total del paquete que será enviado.

peso_payasos = 112
peso_munecas = 75
payasos = int(input("Ingrese la cantidad de payasos: "))
munecas = int(input("Ingrese la cantidad de muñecas: "))
peso_total = (payasos * peso_payasos) + (munecas * peso_munecas)
print("El peso total de los juguetes es: " + str(peso_total) + "gramos")