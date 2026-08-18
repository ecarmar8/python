n = int(input("Ingrese la altura del triángulo: "))
for i in range(n):
    for j in range(i + 1):
        print("*" , end="")  # Imprime i asteriscos en la fila i
    print("")