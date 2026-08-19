# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.
 
nombre = str(input("Introduce tu nombre: "))
horas_trabajadas = float(input("Introduce la cantidad de horas trabajadas: "))
valor_hora = float(input("Introduce el valor por hora: "))
Operacion = valor_hora * horas_trabajadas
print(nombre, "Su salario es: ", Operacion)