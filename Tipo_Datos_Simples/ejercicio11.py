#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
# segundo y tercer años. Redondear cada cantidad a dos decimales.

dinero_depositado = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

interes_anual = 0.04

ahorros_primer_anio = dinero_depositado * (1 + interes_anual)
ahorros_segundo_anio = ahorros_primer_anio * (1 + interes_anual)
ahorros_tercer_anio = ahorros_segundo_anio * (1 + interes_anual)

print(f"La cantidad de ahorros tras el primer año es: {ahorros_primer_anio:.2f}")
print(f"La cantidad de ahorros tras el segundo año es: {ahorros_segundo_anio:.2f}")
print(f"La cantidad de ahorros tras el tercer año es: {ahorros_tercer_anio:.2f}")