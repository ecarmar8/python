nombre = (input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
ingreso = float(input("Ingrese su ingreso mensual: "))
if edad > 16 and ingreso > 1000:
    print(f"{nombre}, usted debe pagar impuestos.")
else:
    print(f"{nombre}, usted no debe pagar impuestos.")