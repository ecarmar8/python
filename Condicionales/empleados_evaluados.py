print("Niveles de rendimiento:")
print("inaceptable: 0.0")
print("aceptable: 0.4")
print("moderado: 0.6 o más")

nombre_empleado = input("Ingrese el nombre del empleado: ")
nivel = float(input("Ingrese el nivel del empleado (0.0, 0.4, 0.6 o más): "))

if nivel == 0.0:
    nivel_texto = "inaceptable"
elif nivel == 0.4:
    nivel_texto = "aceptable"
elif nivel >= 0.6:
    nivel_texto = "moderado"
else:
    nivel_texto = None

if nivel_texto:
    dinero = 2400 * nivel
    print(f"{nombre_empleado} tiene un nivel {nivel_texto} y recibirá ${dinero:.2f}.")
else:
    print("Nivel no válido. Debe ser 0.0, 0.4 o 0.6 o más.")