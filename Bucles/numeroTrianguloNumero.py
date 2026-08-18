n = int(input("Ingrese la altura del triángulo en número positivo: "))
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end="")  # Imprime el número i+1 en la fila i
    print("")  # Salto de línea después de cada fila