#Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

precio_barras = 3.49
barras_no_frescas = int(input("Ingrese el número de barras de pan que no son del día: "))
descuento = precio_barras * 0.60
coste_total = barras_no_frescas * (precio_barras - descuento)

print(f"El precio habitual de una barra de pan es: {precio_barras:.2f}€")
print(f"El descuento por no ser fresca es: {descuento:.2f}€")
print(f"El coste final total es: {coste_total:.2f}€")