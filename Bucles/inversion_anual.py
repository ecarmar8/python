inversion = float(input("Ingrese el monto de la inversión inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en %): "))
anios = int(input("Ingrese el número de años: "))
for i in range(1, anios + 1):
    inversion *= (1 + tasa_interes / 100)
    print(f"Año {i}: {inversion:.2f}")