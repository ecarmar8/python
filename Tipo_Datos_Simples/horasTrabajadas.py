# Este programa calcula el salario de un trabajador basado en las horas trabajadas y el valor por hora.nombre = str(input("Introduce tu nombre: "))
nombre = str(input("Introduce tu nombre: "))
horas_trabajadas = int(input("Introduce la cantidad de horas trabajadas: "))
valor_hora = float(input("Introduce el valor por hora: "))
Operacion = valor_hora * horas_trabajadas
print(nombre, "Su salario es: ", Operacion)