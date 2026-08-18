# Este programa solicita al usuario cuatro números enteros y realiza una operación aritmética
# específica con ellos, mostrando el resultado final.
numero1 = int(input("introduce un número entero: "))
numero2 = int(input("introduce otro número entero: "))
numero3 = int(input("Introduce un tercer número entero: "))
numero4 = int(input("inptroduce un cuarto número entero: "))

operacion = (((numero1 + numero2) / (numero3 * numero4))**2)
print("El resultado de la operación es: ", operacion)