fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
dia = fecha[:fecha.find('/')]
mes = fecha[fecha.find('/')+1:fecha.rfind('/')]
anio = fecha[fecha.rfind('/')+1:]

# Convertir a enteros para validar
try:
    dia_int = int(dia)
    mes_int = int(mes)
    anio_int = int(anio)
    if not (1 <= dia_int <= 31):
        print("Día fuera de rango (1-31).")
    elif not (1 <= mes_int <= 12):
        print("Mes fuera de rango (1-12).")
    elif not (1900 <= anio_int <= 2100):
        print("Año fuera de rango (1900-2100).")
    else:
        print("Día:", dia)
        print("Mes:", mes)
        print("Año:", anio)
except ValueError:
    print("Formato incorrecto. Usa números para día, mes y año.")