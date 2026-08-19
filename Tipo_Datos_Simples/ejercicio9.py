#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

nombre = str(input("Introduce tu nombre: "))
inversion = float(input("Introduce la cantidad que deseas invertir: "))
interes_anual = float(input("Introduce el interés anual: "))
num_anios = int(input("Introduce el número de años: "))

capital_final = inversion * (1 + interes_anual) ** num_anios
print("Hola " + nombre + ", el capital obtenido en la inversión es: " + str(round(capital_final, 2)))