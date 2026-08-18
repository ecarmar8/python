peso_payasos = 112
peso_munecas = 75
payasos = int(input("Ingrese la cantidad de payasos: "))
munecas = int(input("Ingrese la cantidad de muñecas: "))
peso_total = (payasos * peso_payasos) + (munecas * peso_munecas)
print("El peso total de los juguetes es: " + str(peso_total) + "gramos")