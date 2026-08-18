numero1 = float (input("Introduce el primer número: "))
numero2 = float (input("Introduce el segundo número: "))
if numero2 == 0:
    print("No se puede dividir por cero.")
else:
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)