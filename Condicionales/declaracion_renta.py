nombre = (input("Ingrese su nombre: "))
salario_mensual = float(input("Ingrese su salario mensual: "))
if salario_mensual < 2000000:
    print(f"{nombre}, declara el 5% de impuestos. Su impuesto es: {salario_mensual * 0.05}")
else:
    if salario_mensual >= 2000000 and salario_mensual < 4000000:
        print(f"{nombre}, declara el 10% de impuestos. Su impuesto es: {salario_mensual * 0.10}")
    else:
        if salario_mensual >= 4000000 and salario_mensual < 6000000:
            print(f"{nombre}, declara el 15% de impuestos. Su impuesto es: {salario_mensual * 0.15}")
        else:
            if salario_mensual >= 6000000 and salario_mensual <= 8000000:
                print(f"{nombre}, declara el 18% de impuestos. Su impuesto es: {salario_mensual * 0.18}")
            else:
                print(f"{nombre}, declara el 20% de impuestos. Su impuesto es: {salario_mensual * 0.20}")