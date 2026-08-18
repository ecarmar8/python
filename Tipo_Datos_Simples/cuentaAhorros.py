nombre = str(input("Introduce tu nombre: "))
inversion = float(input("Introduce la cantidad de dinero que vas a invertir: "))
interes_anual = 0.04
balance1 = inversion * (1 + interes_anual)
print(nombre, "El balance después del primer año es: ", round(balance1, 2))
balance2 = balance1 * (1 + interes_anual)
print(nombre, "El balance después del segundo año es: ", round(balance2, 2))
balance3 = balance2 * (1 + interes_anual)
print(nombre, "El balance después del tercer año es: ", round(balance3, 2))