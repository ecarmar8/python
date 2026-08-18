#Este programa calcula el índice de masa corporal (IMC) de una persona.
# El IMC se calcula dividiendo el peso en kilogramos por el cuadrado de la altura en metros.
# El resultado se redondea a dos decimales para una mejor presentación.
nombre = str(input("Introduce tu nombre: "))
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
IMC = peso/ (altura ** 2)
print(nombre, "Tu IMC es: ", round(IMC, 2))