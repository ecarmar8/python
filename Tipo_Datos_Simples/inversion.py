nombre = str(input("Introduce tu nombre: "))
inversion = float(input("Introduce la cantidad que deseas invertir: "))
tiempo = int(input("introduce el número de años que deseas tener tu inversión: "))
interes_anual = 16  # Tasa de interés anual del 16%

interes_total = inversion * (interes_anual / 100) * tiempo
total_inversion = inversion + interes_total
print(f"{nombre}, la cantidad total de tu inversión después de {tiempo} años es: {total_inversion:.2f} pesos")
print(f"El interés total ganado en {tiempo} años es: {interes_total:.2f} pesos")
print(f"El interés anual es: {interes_anual}%")