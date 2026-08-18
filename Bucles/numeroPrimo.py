numero = int(input("Introduce un número entero: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
# Este código verifica si un número es primo o no.